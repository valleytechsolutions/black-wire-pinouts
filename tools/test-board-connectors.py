import copy, hashlib, importlib.util, json, pathlib, subprocess, sys, tempfile, unittest
TOOL = pathlib.Path(__file__).with_name('build-board-connectors.py')
spec = importlib.util.spec_from_file_location('compiler', TOOL)
compiler = importlib.util.module_from_spec(spec); spec.loader.exec_module(compiler)
queue_spec = importlib.util.spec_from_file_location('queue_builder', TOOL.with_name('prepare-transcription-queue.py'))
queue_builder = importlib.util.module_from_spec(queue_spec); queue_spec.loader.exec_module(queue_builder)

class CompilerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root = pathlib.Path(self.tmp.name)
        self.folder = self.root / 'catalog/pin-transcriptions'
        for name in ('passes/a', 'passes/b', 'reviewed'): (self.folder/name).mkdir(parents=True)
        (self.root/'library/media').mkdir(parents=True)
        raw=b'source fixture'; sha=hashlib.sha256(raw).hexdigest(); self.image=f'media/{sha}.png'
        (self.root/'library'/self.image).write_bytes(raw)
        self.record={'id':'board','name':'Fixture board','assets':[{'type':'pinout image','file':self.image,'hash':sha}]}
        self.data={'recordId':'board','pass':'a','date':'2026-10-04','status':'transcribed','images':[{'file':self.image,'sha256':sha}], 'connectors':[{'id':'J1','image':self.image,'rows':1,'orderNote':'Printed pin numbers','pins':[{'position':1,'label':'GND','functions':[]},{'position':2,'label':'3V3','functions':[]}]}], 'unreadable':[], 'notes':''}
        self.write(self.folder/'policy.json',{'mode':'single-read-with-checks'})
        self.write(self.root/'library/catalog.json',{'boards':[self.record],'makerParts':[],'stats':{}})
        self.write(self.root/'library/maker-parts.json',{'parts':[]})
        self.write(self.folder/'run-2026-10.json',{'batches':[{'batch':1,'records':['board']}]})
    def write(self,path,value): path.write_text(json.dumps(value))
    def run_tool(self,*args):
        result=subprocess.run([sys.executable,str(TOOL),'--root',str(self.root),*args],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        return json.loads(result.stdout)
    def save(self,data=None): self.write(self.folder/'passes/a/board.json',self.data if data is None else data)
    def test_single_entry_exports_without_inventing_second_pass(self):
        self.save(); result=self.run_tool(); self.assertEqual(result['single-entry'],1)
        exported=json.loads((self.root/'catalog/board-connectors.json').read_text())['records'][0]
        self.assertEqual(exported['review'],'single-entry'); self.assertFalse(list((self.folder/'passes/b').glob('*.json')))
        self.assertEqual(self.run_tool('--strict-double-entry')['exportedRecords'],0)
    def test_uncertainty_missing_images_and_unknown_labels_are_held(self):
        for change in ({'unreadable':['pin unreadable']},{'uncertain':['orientation unclear']},{'notes':'Ambiguous orientation'}):
            with self.subTest(change=change):
                self.save({**self.data,**change}); r=self.run_tool(); self.assertEqual(r['exportedRecords'],0); self.assertEqual(r['needs-review'],1)
        record={**self.record,'assets':self.record['assets']+[{'type':'pinout image','file':'media/other.png'}]}
        self.assertIn('Some pinout images have not been read',compiler.single_pass_issues(self.data,record))
        d=copy.deepcopy(self.data);d['connectors'][0]['pins'][0]['label']='?';self.save(d);self.assertEqual(self.run_tool()['needs-review'],1)
    def test_invalid_record_cannot_poison_other_exports(self):
        self.save(); (self.folder/'passes/a/broken.json').write_text('{broken')
        r=self.run_tool(); self.assertEqual(r['single-entry'],1);self.assertEqual(r['invalid'],1)
        queue=json.loads((self.root/'catalog/pin-review-queue.json').read_text())['records'];self.assertEqual(queue[0]['recordId'],'broken')
    def test_hash_failure_and_invalid_other_pass_prevent_export(self):
        self.save();d={**self.data,'pass':'b'};d['images']=[{'file':self.image,'sha256':'0'*64}]
        self.write(self.folder/'passes/b/board.json',d);r=self.run_tool();self.assertEqual(r['exportedRecords'],0);self.assertEqual(r['invalid'],1)
    def test_matching_labels_in_different_images_do_not_count_as_agreement(self):
        a=copy.deepcopy(self.data);b=copy.deepcopy(self.data);b['connectors'][0]['image']='media/another.png'
        agreed,conflicts=compiler.compare(a,b);self.assertEqual(agreed,[]);self.assertEqual(len(conflicts),2)
    def test_dry_run_does_not_write(self):
        self.save(); before=(self.root/'library/catalog.json').read_bytes();r=self.run_tool('--dry-run')
        self.assertEqual(r['single-entry'],1);self.assertEqual((self.root/'library/catalog.json').read_bytes(),before);self.assertFalse((self.root/'catalog/board-connectors.json').exists())
    def test_existing_disagreement_is_never_demoted_to_single_entry(self):
        self.save();d=copy.deepcopy(self.data);d['pass']='b';d['connectors'][0]['pins'][0]['label']='5V'
        self.write(self.folder/'passes/b/board.json',d);r=self.run_tool();self.assertEqual(r['single-entry'],0);self.assertEqual(r['conflict'],1)
    def test_queue_skips_saved_reads_and_survives_malformed_json(self):
        self.save();self.run_tool();q=queue_builder.prepare(self.root)
        self.assertEqual(q['summary']['ready'],1);self.assertEqual(q['nextReads'],[])
        (self.folder/'passes/a/board.json').write_text('{broken');self.run_tool();q=queue_builder.prepare(self.root)
        self.assertEqual(q['summary']['needs-review'],1);self.assertEqual(q['nextReads'],[])
    def test_queue_finds_shared_images_without_fabricating_reads(self):
        self.write(self.root/'library/catalog.json',{'boards':[self.record,{**self.record,'id':'board2'}],'makerParts':[],'stats':{}})
        self.write(self.folder/'run-2026-10.json',{'batches':[{'batch':1,'records':['board','board2']}]})
        self.run_tool();q=queue_builder.prepare(self.root)
        self.assertEqual(q['summary']['needs-read'],2);self.assertEqual(q['duplicateImageSets'],[['board','board2']]);self.assertFalse(list((self.folder/'passes/a').glob('*.json')))

verify_spec = importlib.util.spec_from_file_location('verifier', TOOL.with_name('verify-transcriptions.py'))
verifier = importlib.util.module_from_spec(verify_spec); verify_spec.loader.exec_module(verifier)

class OcrPolicyTests(CompilerTests):
    def ocr(self, verdict='confirmed', uncertainty=(), connectors=None):
        self.write(self.folder/'ocr-checks.json', {'records': {'board': {'a': {'verdict': verdict, 'uncertainty': list(uncertainty), 'connectors': connectors or {'J1': {'verdict': verdict}}}}}})
    def exported(self): return json.loads((self.root/'catalog/board-connectors.json').read_text())['records']
    def test_confirmed_clean_reading_exports_as_ocr_checked(self):
        self.save(); self.ocr(); r=self.run_tool(); self.assertEqual(r['ocr-checked'],1); self.assertEqual(self.exported()[0]['review'],'ocr-checked')
    def test_ocr_settles_order_doubts_but_keeps_the_pin1_caveat(self):
        self.save({**self.data,'uncertain':['which end is nearest USB is unclear']}); self.ocr(uncertainty=['order'], connectors={'J1':{'verdict':'confirmed','unconfirmed':['GPIO11']}})
        r=self.run_tool(); self.assertEqual(r['ocr-checked'],1)
        self.assertEqual(self.exported()[0]['caveats'],['Pin 1 end inferred by the reader','Not machine-confirmed: GPIO11'])
    def test_unconfirmed_doubtful_reading_stays_in_review(self):
        self.save({**self.data,'uncertain':['label mapping inferred']}); self.ocr(verdict='partial', uncertainty=['mapping']); r=self.run_tool()
        self.assertEqual(r['exportedRecords'],0); self.assertEqual(r['needs-review'],1)
    def test_identity_doubts_never_export_and_are_listed_for_image_fixes(self):
        self.save({**self.data,'uncertain':['image is titled for a different board variant']}); self.ocr(uncertainty=['identity','order']); r=self.run_tool()
        self.assertEqual(r['exportedRecords'],0); self.assertEqual(r['identity'],1)
        listed=json.loads((self.root/'catalog/image-identity-issues.json').read_text())['records']; self.assertEqual(listed[0]['recordId'],'board')
    def test_ocr_arbitrates_a_disagreement_only_when_one_side_is_confirmed(self):
        self.save(); d=copy.deepcopy(self.data); d['pass']='b'; d['connectors'][0]['pins'][0]['label']='5V'; self.write(self.folder/'passes/b/board.json',d)
        self.write(self.folder/'ocr-checks.json',{'records':{'board':{'a':{'verdict':'confirmed','uncertainty':[],'connectors':{'J1':{'verdict':'confirmed'}}},'b':{'verdict':'partial','uncertainty':[],'connectors':{'J1':{'verdict':'partial'}}}}}})
        r=self.run_tool(); self.assertEqual(r['ocr-arbitrated'],1); self.assertEqual(self.exported()[0]['connectors'][0]['pins'][0]['label'],self.data['connectors'][0]['pins'][0]['label'])
        self.write(self.folder/'ocr-checks.json',{'records':{'board':{k:{'verdict':'confirmed','uncertainty':[],'connectors':{'J1':{'verdict':'confirmed'}}} for k in 'ab'}}})
        self.assertEqual(self.run_tool()['exportedRecords'],0)
    def test_rules_v3_fixes_are_applied_in_code(self):
        self.assertEqual([compiler.fix_prefix(x) for x in ['I012','M0SI','MTD0','LD02','ADC1_CHO','UOTXD','GPIO10']],['IO12','MOSI','MTDO','LDO2','ADC1_CH0','U0TXD','GPIO10'])
        self.assertTrue(compiler.polarity_only({'pins':[{'label':'+'},{'label':'-'}]})); self.assertFalse(compiler.polarity_only({'pins':[{'label':'+'},{'label':'GND'}]}))

class VerifierTests(unittest.TestCase):
    """The machine check on synthetic OCR lines: labels along a column at fixed x."""
    size=(1000,1000)
    def lines(self, labels, x=100, extra=()):
        return [{'text':t,'confidence':1,'box':[x,100+i*40,60,20]} for i,t in enumerate(labels)] + list(extra)
    def connector(self, labels): return {'id':'J1','rows':1,'pins':[{'position':i+1,'label':l,'functions':[]} for i,l in enumerate(labels)]}
    def test_correct_reading_confirms_and_errors_fail(self):
        printed=['3V3','GND','GPIO1','GPIO2','GPIO3','GPIO4','GPIO5','GPIO6','GPIO7','GPIO8','GPIO9','GPIO10']
        lines=self.lines(printed, extra=[{'text':'GPIO21','confidence':1,'box':[600,100,60,20]}])
        check=lambda labels: verifier.check_connector(self.connector(labels), lines, self.size)['verdict']
        self.assertEqual(check(printed),'confirmed')
        swapped=printed[:]; swapped[3],swapped[6]=swapped[6],swapped[3]; self.assertNotEqual(check(swapped),'confirmed')
        elsewhere=printed[:]; elsewhere[4]='GPIO21'; self.assertNotEqual(check(elsewhere),'confirmed')
        duplicated=printed[:]; duplicated[4]='GPIO2'; self.assertNotEqual(check(duplicated),'confirmed')
        self.assertEqual(check(printed[::-1]),'confirmed')  # pin-1 direction is not checkable: exported with a caveat instead
    def test_boundaries_and_ocr_lookalikes(self):
        self.assertEqual(verifier.find('GPIO1', [{'text':'GPIO10','confidence':1,'box':[0,0,60,20]}]), [])
        self.assertEqual(len(verifier.find('GPIO4', [{'text':'GPI04 ADC1_CH4','confidence':1,'box':[0,0,140,20]}])), 1)
        self.assertEqual(len(verifier.find('ADC1_CH0', [{'text':'ADC1 CHO','confidence':1,'box':[0,0,80,20]}])), 1)
    def test_uncertainty_notes_are_triaged(self):
        self.assertIn('identity', verifier.classify('Image is titled ESP32 DevKitC-1, record is ESP32S3-A'))
        self.assertIn('order', verifier.classify('which end is nearest USB is unclear'))
        self.assertIn('mapping', verifier.classify('label-to-pad mapping inferred from leader lines'))

if __name__=='__main__':unittest.main()

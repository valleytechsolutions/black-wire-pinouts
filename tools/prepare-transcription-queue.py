"""Build a resumable queue from saved files, not historical batch completion messages.

Run after build-board-connectors.py. Never writes or copies transcription passes.
"""
import argparse
import json
from pathlib import Path


def prepare(root):
    folder = root / 'catalog' / 'pin-transcriptions'
    plan = json.loads((folder / 'run-2026-10.json').read_text())
    catalog = json.loads((root / 'library' / 'catalog.json').read_text())
    records = {r['id']: r for r in catalog['boards'] + catalog.get('makerParts', [])}
    passes = {key: {} for key in ('a', 'b')}
    for key in passes:
        for path in (folder / 'passes' / key).glob('*.json'):
            try:
                data = json.loads(path.read_text())
                if not isinstance(data, dict): raise ValueError('Expected an object')
                passes[key][path.stem] = data
            except (ValueError, OSError): passes[key][path.stem] = {'status': 'invalid'}
    reviewed = {p.stem for p in (folder / 'reviewed').glob('*.json')}
    exported = {r['recordId']: r for r in json.loads((root / 'catalog' / 'board-connectors.json').read_text())['records']}
    review = {r['recordId']: r for r in json.loads((root / 'catalog' / 'pin-review-queue.json').read_text())['records']}
    tasks, duplicate_sets = [], {}
    summary = {key: 0 for key in ('total', 'ready', 'needs-review', 'no-connector-map', 'needs-read', 'awaiting-compile')}
    for batch in plan['batches']:
        for rid in batch['records']:
            record = records[rid]
            sources = [passes[k][rid] for k in ('a', 'b') if rid in passes[k]]
            images = [{'file': a['file'], 'sha256': a['hash'], 'width': a.get('width'), 'height': a.get('height')} for a in record.get('assets', []) if a.get('type') == 'pinout image']
            if rid in review: status = 'needs-review'
            elif rid in exported or rid in reviewed: status = 'ready'
            elif sources and all(s.get('status') == 'no-connector-map' for s in sources): status = 'no-connector-map'
            elif sources: status = 'awaiting-compile'
            else: status = 'needs-read'
            summary['total'] += 1; summary[status] += 1
            task = {'recordId': rid, 'name': record['name'], 'batch': batch['batch'], 'status': status, 'savedPasses': [k for k in ('a', 'b') if rid in passes[k]], 'images': images}
            if rid in review: task['review'] = review[rid]
            if status == 'needs-read':
                key = tuple(sorted(i['sha256'] for i in images))
                duplicate_sets.setdefault(key, []).append(rid)
            tasks.append(task)
    duplicates = [ids for key, ids in duplicate_sets.items() if key and len(ids) > 1]
    reads = sorted((t for t in tasks if t['status'] == 'needs-read'), key=lambda t: (len(t['images']), sum((i['width'] or 0) * (i['height'] or 0) for i in t['images']), t['recordId']))
    return {'mode': 'single-read-with-checks', 'summary': summary, 'duplicateImageSets': duplicates, 'duplicateScope': 'Candidates for shared image reading only; confirm the diagram represents each product before reuse. Never copy pass A into pass B.', 'nextReads': reads, 'reviewQueue': [t for t in tasks if t['status'] == 'needs-review'], 'records': tasks}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path)
    parser.add_argument('--next', type=int, default=0, metavar='N', help='Also print a compact packet of the next N unread boards')
    args = parser.parse_args()
    result = prepare(args.root.resolve())
    output = args.output or args.root / 'catalog' / 'pin-transcriptions' / 'queue.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=1) + '\n')
    print(json.dumps({**result['summary'], 'duplicateImageSets': len(result['duplicateImageSets']), 'queue': str(output)}, indent=2))
    if args.next > 0: print(json.dumps(result['nextReads'][:args.next], ensure_ascii=False, indent=1))


if __name__ == '__main__': main()

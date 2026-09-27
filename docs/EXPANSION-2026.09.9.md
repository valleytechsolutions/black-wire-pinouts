# First Edition source sweep / 2026.09.9

This snapshot adds six board records, fills one empty record and adds 24 reference entries, including four physical pinout-image entries. One corrupt reference was retired, and two empty records created from scraped footnote numbers were merged into their real models. The resulting catalog has **2,593 board/device listings, 501 maker listings, 3,377 board references and 1,515 physical pinout-image entries across 70 populated source groups**. Counts include related and shared records, not unique independently approved hardware.

| Hardware | Saved evidence | Scope |
|---|---|---|
| Espressif ESP-Mosaico | CoreBoard V1.0 schematic, H1/H2 connector schematics, component views and source pin tables | Connector schematics are not physical board maps. H1 orientation and shared audio pins matter. |
| ESP32-P4X-C5-Function-EV-Board | V2.0 schematic, board labels and J1 signal table | P4 and C5 processors are both searchable. |
| ESP32-P4X-EYE | Manufacturer component views | Supporting references; full physical GPIO map still needed. |
| ESP32-P4X-Function-EV-Board | V1.6 front view and J1 table | Manufacturer reuses a V1.5.2 back image; that revision remains labeled. |
| BrisbaneSilicon ELM11 Feather | 49-page board datasheet, three physical pinout sheets, block diagram and dimensions | Match FPGA overlays 00002, 00003 or 00013. Creator lists pre-orders; shipping dates are estimates. |
| Terasic Atum A3 Nano | 48-page hardware manual and JP1 map with pin-1 orientation | JP1 only; full manual covers other connectors. |
| Steiert Solutions CycloMod | Creator board photo and RP2350/FPGA block diagram | Pre-release campaign. Board datasheet and physical MicroMod pinout remain missing. |

Original document URLs, SHA-256 hashes, revisions, rights and correction evidence are in [the intake ledger](../catalog/expansion-2026.09.9.json). Board pages link original files. Reference art retains its source rights; it is not relicensed by the editorial license.

## Corrections and source conflicts

- Nine display-board processor classifications corrected: four CrowPanel P4 boards had been marked S3; four S3 display boards had been marked S31; one C6 display board had been marked C61. Display sizes must not be appended to chip identifiers.
- Two imported Waveshare labels, `ESP32-S3-Touch-LCD-3.5B1` and `ESP32-S3-ePaper-13.3E67`, were footnote-suffix errors. Canonical records remain; legacy IDs and search aliases resolve to the real models.
- A truncated ReSpeaker Lite front PNG was confirmed identical at the upstream URL and removed from the current bundle. Its valid physical pinout image remains. Separate source working collections and older releases are unchanged.
- Five missing manufacturer/documentation endpoints were replaced with checked model resources: Saola-1, WisMesh Base and three Waveshare boards. The two invalid Waveshare endpoints disappeared with the merged records.
- **ESP-Mosaico H2 GPIO19 remains a source conflict:** the HTML pin table says ADC, while the connector schematic marks TOUCH. The guide preserves both and flags the discrepancy. It does not invent a corrected analog capability or infer a power-input range from an output rail.

## Audit results and limits

All **3,094 listing names** pass their own name searches with ordinary dashes, Unicode dashes and spaces. **7,493 visual files** passed decode/parse checks, including PDF pages and existing previews; 18 non-visual files were classified separately. Four exceptionally large source PNGs were checked with sequential libvips decoding. This does not independently verify every printed pin assignment.

**7,560 manifest paths and 3,745 original-source hashes** pass integrity checks. The [endpoint audit](LINK-AUDIT.md) associates 2,230 distinct documentation URLs with 2,498 listings: 1,705 responded, six returned not found, 14 restricted access, 17 had connection errors and 488 were deferred after repeated publisher-host errors. Deferred URLs were not checked. These results do not certify document model identity. The six remaining missing endpoints are old ODROID-GO and XNucleo model pages; available local references and separately identified manuals remain usable.

Only eight board/device listings currently have explicitly classified board datasheets, and 93 have board hardware guides. Older unclassified documents and missing manufacturer datasheets remain research gaps; a chip datasheet or schematic is not silently counted as a board datasheet. See [every listing's documentation coverage](../DOCUMENTATION.md).

This is a substantial audited update, not a complete worldwide inventory or a zero-bug guarantee. First Edition / 2026 is unchanged. The book draft was not edited.

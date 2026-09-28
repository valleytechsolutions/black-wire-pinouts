# Radios, GPIO devices and connector references — collection 2026.09.13

**34 new records, 12 enriched records, 104 reference attachments and 164 sourced pin-function rows.** Of the new attachments, 25 are physical pinout images; the remaining material includes connector references, schematics, original PDFs, mechanical drawings, labels and identification photographs. These counts describe attachments, not independently approved all-pin maps.

## What was added

- **RAKwireless:** WisBlock core/base/power references, RAK11160/11161 and RAK3112/3212. RAK11310, RAK11722 and RAK4631 have offline WisConnector tables. The 40 numbered connector contacts and four F contacts are distinct from castellated module numbering.
- **Heltec:** HT-1303, HT-N5262M, Mesh Node T1 and T096, plus Wireless Paper source PDFs. HT-N5262M's overview links a missing datasheet; its physical pin map and schematic are available. T1's saved preliminary document has conflicting footer/revision dates, and a complete external GPIO map remains missing.
- **Elecrow:** 14 distinct RA-08H, LR1302, LR1262 and nRFLR module/carrier variants. A module pin map must not be substituted for the carrier header layout.
- **Seeed Studio:** reviewed existing Wio Tracker L1 variants, added Wio-LR1121 documentation and a separate Wio-SX1262-LF module record. The LF document identifies STM32WLE5JC and 28 SMT contacts; it is not the similarly named HF add-on. Raw Seeed working collections were not edited.
- **OpenSourceSDRLab / PortaPack:** H4M Pro source schematics and product identification, an ESP32-MDK record with GPIO schematics, and the original H4M connector source. H4M Pro compatibility is not inferred from older H4M drawings.
- **Hat Labs:** HALMET, HALPI2 and SH-ESP32 hardware/interface references. Power domains, jumper requirements and revision differences remain explicit.
- **LOLIN:** D1 mini V4.0.0, Lite V1.0.0 and Pro V2.0.0 manufacturer photographs/schematics; Lite and Pro gain sourced header-function tables. Existing NodeMCU 0.9 and 1.0 records remain available.
- **REYAX:** the original RYLR998 datasheet and physical five-pin map, discovered through Voltaat and checked against the manufacturer PDF.

[Exact records and intake counts](../catalog/radio-research-2026.09.13.json) · [Research leads and gaps](../catalog/radio-discovery-2026.09.13.json) · [Browse the collection](../BROWSE.md)

## Discovery does not establish coverage

DigiKey supplied an original RAK4631 manufacturer PDF. Mouser's LR 14 Click lead, Electromaker's LR Click listing, further Elecrow ThinkNode devices and other RAK/Heltec catalog pages remain leads requiring exact physical-map review. Tindie's search returned an access restriction, so its catalog has not been audited. One Voltaat LoRa listing mixed TTGO/Heltec naming and radio specifications; it was not used to assign an identity or pinout.

[Random Nerd Tutorials' ESP32/RFM95 tutorial](https://randomnerdtutorials.com/esp32-lora-rfm95-transceiver-arduino-ide/) is linked as further learning with author-site attribution. Its example wiring is not a universal ESP32 pinout, and its text and illustrations were not imported into unrelated board records.

Many additional radio modules and development boards remain unreviewed. Missing exact GPIO maps, datasheets and manufacturer identification remain visible in the documentation and pinout audits. This is a bounded collection update, not a complete worldwide inventory.

## Evidence and rights

Manufacturer originals retain source URLs, SHA-256 hashes, revision scope and separate review/rights status. PDF page images record the source PDF hash and page. Original photos and block diagrams are not counted as physical pinouts. No pin assignments or electrical limits were independently bench-tested, and no new Power Desk ratings are approved by this update.

Original artwork belongs to its manufacturers and contributors. Heltec documents explicitly restrict commercial reproduction without permission; SH-ESP32 hardware cites CC BY-SA 4.0. Unknown redistribution and book-print rights remain unknown. Black Wire's editorial license does not relicense third-party diagrams. **First Edition / 2026** remains the editorial edition. The book draft is unchanged.

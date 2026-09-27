# HaleHound and Elechouse / collection 2026.09.11

First Edition / 2026. Adds **32 listings**: eight board/device records and 24 maker-module records. There are **106 reference attachments**, backed by **94 distinct media files**. Six attachments are classified as partial physical pinout images; the other files are original PDFs, connector tables, wiring diagrams, labeled hardware and identification photos. None is an independent all-connector approval.

## HaleHound and its CYD base boards

The original 18-page **HaleHound CYD Build Guide v1.4.1** is saved with its SHA-256 hash. Selected original pages are also available as readable PNGs, with page numbers and a link back to the unchanged PDF. Credits remain with HaleHound, Bkbroiler and the original contributors.

Separate records cover the original non-SPI 2.8-inch CYD build, the SPI-exposed 2.8-inch build and the 3.5-inch SPI build. The QDtech E32R28T and E32R35T base boards have separate LCDwiki specifications, user manuals and schematics. Kit modifications must not be applied to an unmodified base board by assumption.

The build guide contains revision-dependent CS assignments, ambiguous GPS TX/RX labels and questionable regulator terminology. The 3.5-inch instructions are described as work in progress in places. Those limitations are visible in the records. No electrical claims from this guide were imported as verified Power Desk ratings. The standalone ESP32 module map on page 7 was not added as a development-board pinout image.

## Elechouse

Four current shop pages yielded 41 product listings. This intake includes 26 pin-connected hardware products plus the legacy PN532 V3 referenced by the HaleHound guide. Passive tags, antennas, cables and a custom service are recorded as exclusions, not extra GPIO-board records.

Included families: serial RFID V5, PN532 V3/V4/Purple/Evolution/external-antenna/USB/MINI variants, PN5180, CLRC663, PN7150, PN7160 and PN7161 I2C/SPI variants, ST25R3916/B and MINI, Network RFID V0.1H, Proxmark3 V2, CC1101, motor drivers, a power module, two voice-recognition modules and TAIJIUINO Due R3S.

**36 pin-purpose rows across five module variants** are transcribed from manufacturer connector tables, with exact PDF hashes and page references. They cover PN5321 MINI, PN7160 MINI I2C, standard PN7160/PN7161 I2C and full-size ST25R3916B. Pin numbers follow the source table; a cable's mating face may reverse the apparent order.

## Source differences and remaining work

- The serial RFID V5 product links a manual titled SSRFIDV3.0. It remains a labeled legacy reference.
- PN5321 MINI web and PDF specifications disagree about supply range and ISO15693 support. The saved September 2026 hardware-V2 PDF and the conflict are recorded separately.
- The legacy CC1101 manual mentions CC1100 and has conflicting interface-voltage wording. The old PN532 V3 manual also has questionable TTL-voltage wording. Neither establishes verified electrical limits here.
- PN716x and ST25R3916B manufacturer characterization results remain in their original documents. They are not Black Wire bench tests or guaranteed maximum ratings.
- Some exact models still need physical connector maps. Exact Ebyte E07, Cinder Ferret carrier and generic power-module PCB identities need further review.
- Asset-specific redistribution and print rights are not established by Black Wire's editorial license. Manufacturer artwork retains its original rights.

This is a documented intake, not a complete historical inventory. The existing catalog, galleries, search, document viewer and wiki architecture are retained. No book files were edited.

[Per-record evidence and exclusions](../catalog/halehound-elechouse-research-2026.09.11.json) · [Documentation coverage](../DOCUMENTATION.md) · [Pinout coverage](../PINOUT_COVERAGE.md) · [HaleHound source](https://halehound.com/products/diy-halehound-kit) · [Elechouse](https://www.elechouse.com/shop/)

For the collection download, extract **all Black-Wire-Pinouts-2026.09.11-part-XX.zip files into the same folder**. Checksums accompany the files. This reference collection does not contain the desktop executable.

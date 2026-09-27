# Inland, DFRobot and distributor-source expansion / 2026.09.10

First Edition / 2026 remains the editorial edition. This is a digital collection snapshot; the book draft was not edited.

**118 new listings: 68 board/device records and 50 maker-module records.** Three existing DFRobot records were enriched. The collection now has 2,661 board/device listings, 551 maker listings, 3,504 board reference entries and 1,549 board physical-pinout image entries. The maker index has 124 unique physical-reference images. Counts include variants and shared images; they are not unique-device or completeness claims.

## Inland coverage

Reviewed all **48 articles** returned by Micro Center's Inland Maker Products support category and all **49 Inland products** returned by its current Boards/Projects category, including unavailable stock. An additional Super Learning Kit guide supplies archived board references. The result is **67 Inland records: 17 boards/devices and 50 modules, shields, sensors and kits**, with **eight physical pinout-image attachments**. Retail and archive pages often overlap.

[Exact source/SKU checklist](../catalog/inland-coverage.json) · [Browse modules](../MAKERS.md) · [Browse boards](../BROWSE.md)

Saved physical diagrams include ESP32 Core, UNO R3, Pro Micro, RC522, LCD1602 keypad shield, the archived PIR carrier, ESP-01 and an archived UNO kit board. Supporting images are labeled separately. The source ESP-01 reset label conflicts with its surrounding text and remains flagged. A source image is not electrical approval.

The newer USB-C ESP32 and 2.8-inch ESP32 display have separate records; generic CYD maps are not substituted. Current PIR and breadboard-power photos differ from the old articles linked by Micro Center, so their records remain separate. The ESP32-CAM article linked by the vendor returns Article not found. Kits still need constituent-by-constituent review. More historical SKUs and other retail categories may exist; this is not a complete Inland census.

## DFRobot coverage

All **50 SKU pages** in the official MCU category were reviewed, covering C3, C5, C5-U, C6, S3, P4, RP2040, RP2350, AVR, M0 and Intel Curie products. The broader official wiki category inventory has **807 distinct product URLs**; it is a research queue, not 807 saved pinouts.

[DFRobot inventory and reviewed SKU ledger](../catalog/dfrobot-coverage.json) · [Official MCU category](https://wiki.dfrobot.com/category-312/)

Board schematics and manuals are saved where collected. PDFs named Datasheet sometimes describe only a processor, radio module or power IC; those links are explicitly component datasheets. The FireBeetle ESP32 document is a board user manual. DFR1139's N16R8 heading conflicts with its N16R2 title and diagram. C5 kit and antenna variants share source artwork, with its limited scope stated. Failed image hosts and missing diagrams remain gaps.

## Mouser-discovered references

The first distributor-source batch adds TI LP-CC2651R3SIPA and LP-CC2651P3 LaunchPads, Microchip AVR-IoT WG AC164160, and Silicon Labs EFM32ZG-STK3200. Each retains the manufacturer PDF and rendered physical-map page. Expansion/debug header pages are supporting connector references. Silicon Labs marks the older board Not Recommended for New Designs. Products are indexed under their manufacturer, not Mouser.

Mouser's broader development-tool inventory remains to be reviewed. Further leads include NXP FRDM-i.MX93, Altera FPGA kits, Sensiedge and third-party carrier boards; no matching pinout is claimed until the exact reference is collected and inspected.

## Verification and remaining work

Original asset hashes, manifest paths, reference types, source URLs, separate model identities and private-data scans are checked before publishing. HTTP availability is reported separately from model/revision review. Physical-map images are not a certification of every connector or electrical limit. The Power Desk did not gain unverified ratings; conflicting Inland CCS811 power figures are explicitly noted.

The collection and Windows library now use independent ZIP parts below GitHub's per-file limit. Extract every collection part into the same folder; Windows users keep every matching library part beside the installer. Existing published snapshots remain immutable.

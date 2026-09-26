# Manufacturer and SBC expansion / 2026.09.7

This First Edition / 2026 snapshot adds **107 board/device listings**, **229 reference entries** and **127 physical pinout-image entries** relative to 2026.09.6. Fifteen linked maker records make selected sensors, controls, displays, radio/driver and FPGA boards easier to discover. Linked records and shared images are not unique-hardware counts.

## What was collected

- Adafruit physical PrettyPins references, including AVR, SAMD, nRF52, Trinkey, PyPortal and additional ESP32/RP boards.
- SparkFun graphical datasheets, including ESP32, MicroMod, Arduino-compatible, Artemis and QuickLogic EOS S3 boards. Original PDFs remain alongside rendered image pages.
- Sipeed Tang Nano 4K/20K and 1BitSquared iCEBreaker v1.0b physical board references.
- PortaPack H4M's 12-pin external connector map, credited to the Mayhem documentation contributors. This does not cover every internal connection.
- LattePanda IOTA, Sigma, Alpha, Delta, V1, 3 Delta, Mu and Mu Ultra; Milk-V Mars's 40-pin GPIO connector. Mu/Mu Ultra orientation images and original signal spreadsheets are supporting references, not counted as physical pinout images.
- Architecture metadata for new records and 22 existing SBC records, checked against manufacturer processor documentation. Unknown architectures remain unassigned. Mixed ARM/RISC-V hardware is searchable under either architecture.

## Model and evidence corrections

Sparkle Motion Stick now has its own record instead of inheriting the larger Sparkle Motion board's identity. The legacy Metro Mini sheet is explicitly distinguished from the current V2 product. Feather M4 CAN's processor is ATSAME51. SHT45 Trinkey retains SHT4x as a search alias. Alpha and Delta remain separate records despite sharing a publisher diagram.

SparkFun ESP32-C5 gains an original schematic, not a physical pinout. Its documentation contains conflicting C6 wording; no C5 pin assignments were inferred from that text. Thing Plus RP2040 gains partial power/debug/shared-GPIO references; a complete physical map remains a gap.

## Discovery and source records

The [repository discovery ledger](../catalog/manufacturer-discovery-2026.09.7.json) records a 752-repository scan, including 664 Adafruit PCB-search repositories, SparkFun processor searches and selected FPGA/device repositories. It is a repository discovery sample, not a complete manufacturer product census. No filename match does not establish absence of documentation.

[Reference intake](../catalog/expansion-2026.09.7.json) · [Architecture intake](../catalog/architecture-intake-2026.09.7.json) · [Specifications coverage](../catalog/specification-coverage.csv) · [Per-image attribution](../catalog/attributions.csv).

The import retains original image/PDF bytes, source URLs, hashes, model/revision notes and per-asset rights. New source candidates were visually reviewed; photos, schematics, chip-package maps and software screenshots were not promoted to physical board pinouts. Specifications links and general source links are distinguished in app 0.7.0 and board pages.

## Current coverage and validation

There are **2,514 board/device listings**, **1,806 with files**, **3,240 board reference entries**, **1,496 pinout-image entries**, and **501 maker listings** across **64 brands/source groups**. Of the board listings, 986 have physical pinout sources, 818 have supporting references only, 3 have functions only and 707 have no reference. Maker coverage is 166 with physical sources, 288 supporting only, 30 functions only and 17 missing.

All 7,300 library manifest paths and 3,608 original/model file hashes passed validation. Source-map availability is not an independently approved all-pin reference; there are still zero complete-device approvals. Existing malformed-source and low-resolution limitations remain in the catalog. Original licenses do not relicense manufacturer artwork. The book draft and parallel manufacturer working collections were not changed.

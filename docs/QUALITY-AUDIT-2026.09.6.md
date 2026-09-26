# Reference audit / snapshot 2026.09.6

Checked September 26, 2026. This is a focused source review plus a full local catalog/file integrity pass, not a worldwide hardware census or independent electrical verification.

## Changes

- Added separate SparkFun ESP32 Thing Plus records for **WRL-20168 (USB-C)** and **WRL-15663 (micro-B)**. Their header mappings differ. Each retains the manufacturer PDF and a page-rendered physical header reference, including original credit. Source power-summary and alternate-function claims still need independent electrical review.
- Populated SparkFun Pro Micro RP2350 and Thing Plus RP2350 with manufacturer header-label photos. These are supporting references, **not complete physical pinouts**. The latter retains the manufacturer's v10/v11 battery-polarity distinction.
- Populated ESP32-P4-Function-EV-Board **v1.5.2** with its original six-page schematic and front component-location image. The schematic and component labels do not count as a physical all-pin map. v1.4 and P4X must not inherit these mappings.
- Recorded an ESP32-C5 source conflict rather than transcribing C6-labeled text into a C5 pinout.

The [intake ledger](../catalog/reference-intake-2026.09.6.json) preserves asset URLs, exact hashes, revision scope and review status. No manufacturer artwork was stripped of its branding or relicensed as Black Wire artwork.

## Full-library checks

`python tools/validate-library.py` checks every manifest path, linked board, referenced derivative and original hash, along with core catalog totals. No missing file or hash mismatch was found. The initial app audit parsed and rendered all **191 existing PDFs / 724 pages** in the PDF.js browser engine. Added PDFs are checked separately before publication.

The image decode pass inspected **6,646 existing original/preview/thumbnail paths**. Three enormous M5Stack originals exceeded the audit decoder's pixel limit; their existing screen previews and thumbnails decoded successfully. One Seeed reSpeaker Lite front PNG is malformed; fetching its official URL again returned identical bytes. The app now explicitly identifies that reference as needing replacement instead of offering a potentially incomplete image as a usable preview. Its original remains downloadable. The separate Seeed and M5Stack working source collections were not modified.

## Remaining coverage

The **2,407 board/device listings** include 877 with pinout sources, 3 with pin functions only, 814 with supporting references only, and 713 without documentation. The **486 maker listings** include 151 with pinout sources, 30 with functions only, 288 with supporting references only, and 17 without references. Linked records can describe the same hardware.

The [per-listing coverage ledger](../catalog/pinout-coverage.json) accounts for every record. Source presence is not confirmation that every connector is covered. Zero complete-device electrical approvals are inferred. The book was not changed in this update.

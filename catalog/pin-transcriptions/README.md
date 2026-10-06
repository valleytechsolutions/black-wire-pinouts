# Pin transcriptions

Structured connector lists transcribed from pinout images already in this library. They let the breadboard maker load a board's terminals in physical order. They are **transcriptions of the cited image, not independent electrical verification** and never mark a pinout complete or approved.

`tools/build-board-connectors.py` preserves independent A/B readings already saved and exports single readings under the active policy below. Exports distinguish `ocr-checked`, `single-entry`, `double-entry`, `ocr-arbitrated`, `partial` and `reviewed`. Uncertain, conflicting, or invalid entries go to `catalog/pin-review-queue.json`. A human-reviewed file in `reviewed/` replaces the readings and is exported as `reviewed`.

## Active workflow (2026-10-06): one reading, then a machine check

The owner selected **one image reading per board, with no second AI reading**. The second check is deterministic code:

1. **Read once.** Save one file per board in `passes/a/` following the rules below, with `unreadable` and `uncertain` arrays. Do not redo an existing reading.
2. **Machine check.** `python3 tools/verify-transcriptions.py` runs Apple Vision OCR (macOS, offline, cached per image hash in `.cache/ocr/`) on every cited image and asks, per connector: is every label printed on this connector's own line of text, and do the labels run in strict transcribed order along it? A label found only elsewhere on the page, a repeated signal name, or any out-of-order pin fails the connector. At most one pin (or 10%) the OCR cannot read at all is tolerated and named in the export. Results: `ocr-checks.json`.
3. **Compile.** `python3 tools/build-board-connectors.py` exports:
   - `ocr-checked` — one reading that the machine check confirmed. Reader doubts about order, label mapping, grouping or legibility are settled by the check; an order doubt still exports the caveat *Pin 1 end inferred by the reader*, because OCR cannot tell which end is pin 1.
   - `single-entry` — a clean reading the OCR could not confirm (stylised fonts, rotated text, graphics).
   - `double-entry`, `partial` — earlier independent A/B readings. `ocr-arbitrated` — A/B readings that disagreed, where the machine check confirmed exactly one side.
   - Never exported: board-identity doubts (listed in `catalog/image-identity-issues.json` for a corrected image), structural problems, and doubtful readings the check could not confirm (`catalog/pin-review-queue.json`).
4. `python3 tools/prepare-transcription-queue.py` refreshes `queue.json`. Tests: `python3 tools/test-board-connectors.py`.

None of these levels is electrical verification. The app shows the level, any caveats and the source image for every transcribed device.

## Transcription rules (v3, after the 2026-10 full run)

Use **only the provided image files**. Do not use memory of the board, datasheets, other images or web pages. If something is not legible in the image, record it as unreadable rather than guessing.

**What to transcribe**

1. Transcribe every physical wiring point shown: pin headers, castellated/edge pads, labeled connectors (JST, Qwiic/STEMMA, Grove, screw terminals, FPC breakouts whose individual contacts are labeled), and labeled single test pads (each as a 1-pin connector, flagged as grouping in `uncertain` only if its grouping is unclear). Skip USB/antenna connectors unless their contacts are individually labeled, buttons, LEDs, unlabeled test points, capacitive touch pads, card sockets, prototyping-area rails, and labels that point to an abstract block rather than contacts.
2. **Polarity marks (+/−) alone are not pin names.** Skip battery, speaker and RTC connectors whose only labels are +/− (also enforced in code).
3. A header with no per-pin labels at all is skipped. A single unlabeled pad inside a labeled row is kept as `"?"` so positions stay physical.
4. One connector entry per physical row or connector. A 2×N header is one connector with `rows: 2`; a 3×N servo/Gravity header (signal, V, GND per column) uses `rows: 3`. Castellated modules numbered continuously around their sides are split into one connector per side, keeping the printed numbers in `functions`. Pin-grid arrays: one connector per side, two deep (`rows: 2`), corners belong to the top and bottom sides.
5. `id`: the printed designator (`J1`, `P3`, `CN1`, `H2`) when shown; otherwise a descriptive lowercase id (`left-header`, `top-header`, `edge-pads`, `grove-port`…) in the image's orientation. Connectors from a second image get `-img2`, `-img3`.

**Pin order** (`position` 1…n; state the rule used in `orderNote`)

6. Follow printed **header/connector position numbers** or a marked pin 1. MCU package pin numbers, GPIO numbers and around-the-board callout numbers are *not* position numbers; keep them as functions. If printed position numbers are visibly wrong or repeated, order physically and record the discrepancy in `uncertain`.
7. Otherwise start at the end **closest to the USB device connector** (USB-C before USB-A host ports; a metal receptacle counts even if unlabeled). Measure straight-line distance. If both ends are equally close — the USB sits centred on, opposite or parallel to the row — start at the **top** (vertical rows) or **left** (horizontal rows) of the image as displayed. With no USB visible in the view the labels come from, use top/left too.
8. 2×N headers without printed numbers: position 1 at the start end of the row nearest the board edge, then alternate rows (1 outer, 2 inner, 3 outer…). If no board edge is visible (detached or magnified insets, cropped images), the left column or top row is outer. Pin-1 marks on a mating connector on another board do not apply.
9. Use **only the view the labels are read from** for ordering. An inset drawn rotated or detached is ordered as drawn. A square or shaped pad, triangle or dot is not a pin-1 mark unless labeled `1`.

**Labels**

10. `label`: the pin's functional name when printed: the GPIO name (`GPIO4`, `IO4`) or power/control name (`3V3`, `5V`, `GND`, `VIN`, `EN`, `RST`). When a power pin shows both a board name and a function box (`Vin` / `VIN 5V`), use the function box. Port names (`PA22`, `P0.13`, `PD1`) count as the GPIO name when no `GPIOn` name is printed; an Arduino-style board name (`D4`, `A0`) is used only when neither is printed. Put a different silkscreen spelling first in `functions`.
11. Split combined callouts: `RXD(GPIO38)` → label `GPIO38`, function `RXD`; `D13/SCK` → label `D13`, function `SCK`. Peripheral functions printed as a column header plus a number are written `I2C0 SDA`, `SPI0 RX`.
12. Copy spelling exactly as printed, including typos and leading `*`. Resolve O/0 by context: the letter O inside letter sequences and signal names (`IO12`, `MOSI`, `MTDO`, `LDO2`, `OUT`), the digit 0 in numbers and indices (`CH0`, `U0TXD`); note undecidable cases in `unreadable` (common misreadings are also corrected in code).
13. `functions`: other names printed for the pin, read **outward from the pin**, without repeats of the label. Include short printed notes (`Input only`, `Used in reset`, `1.8V`) and category words printed beside one pin (`STRAP`); omit colors, group-only tags (`UART`, `FREE`) without a signal name, icons and symbols.
14. Mirrored or bottom-side labels belong to the pad they are printed beside; if that is ambiguous, record the assignment in `uncertain` (mapping).

**Identity and scope**

15. If the image shows a different product, carrier/base board or an unnamed variant, use `no-connector-map` (different product) or add a board-identity entry to `uncertain` (possible variant). Identity problems are never exported; they need a corrected image.
16. If an image shows no physical pin positions (chip package only, block diagram, a function or plug-contact table without positions), return `"status": "no-connector-map"` with an explanation in `notes`.
17. `uncertain` lists only doubts the rules do not settle: identity, a label-to-pin mapping that had to be inferred, a pin position not shown, or a grouping the image leaves open. Choices these rules decide go in `orderNote`/`notes`.
18. Copy image file names and SHA-256 values exactly from the batch (by script, never retyped). Each reader uses its own scratch directory.

## Pass file format

`passes/<a|b>/<recordId>.json`

```json
{
  "recordId": "espressif-esp32-esp32-c5-devkitc-1",
  "pass": "a",
  "date": "2026-10-03",
  "status": "transcribed",
  "images": [{"file": "media/<sha256>.png", "sha256": "<sha256>"}],
  "connectors": [
    {"id": "J1", "name": "Left header", "image": "media/<sha256>.png", "rows": 1, "orderNote": "Pin 1 marked",
     "pins": [{"position": 1, "label": "3V3", "functions": []}, {"position": 2, "label": "RST", "functions": ["EN"]}]}
  ],
  "unreadable": [],
  "notes": ""
}
```

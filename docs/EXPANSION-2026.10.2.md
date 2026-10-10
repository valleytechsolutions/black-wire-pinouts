# Vendor reference expansion / collection 2026.10.2

**10 new records, 124 enriched records, 232 reference attachments and 159 sourced external pin-purpose rows.** First Edition / 2026 is unchanged. This is a digital collection update, not a new book edition or desktop installer release.

The attachments comprise 14 physical pinout images, 152 original reference PDFs, 13 pin-function sheets, 51 component-label images, one GPIO block/layout reference and one connector reference. Supporting diagrams and circuit schematics are not counted as physical pinouts. Original files and SHA-256 hashes are preserved; the eight extracted Arduino/Renesas PDF pages retain the source PDF, page number and rendering provenance.

## New records

- [M5Stack Chain MIC](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-chain-mic) — STM32G031G8U6.
- [M5Stack Chain Switch](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-chain-switch) — STM32G031G8U6.
- [M5Stack ToughC5](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-toughc5) — ESP32-C5HR8.
- [M5Stack PaperMono-Lite](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-papermono-lite) — ESP32-S3R8.
- [M5Stack StackChan Core](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-stackchan-core) — ESP32-S3.
- [M5Stack Chain RGB](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-chain-rgb) — STM32G031G8U6.
- [M5Stack DinMeter v1.1](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-dinmeter-v1-1) — ESP32-S3FN8.
- [M5Stack AI Pyramid-Pro](https://valleytech-black-wire-guide.pages.dev/?board=m5stack-ai-pyramid-pro) — Axera AX8850.
- [Arduino UNO Breakout Carrier](https://valleytech-black-wire-guide.pages.dev/?board=arduino-uno-breakout-carrier) — Passive UNO Q carrier; MCU and MPU signals have different logic voltages.
- [Renesas EK-RA8P1 v1](https://valleytech-black-wire-guide.pages.dev/?board=renesas-ek-ra8p1-v1) — RA8P1.

## Scope and evidence

This targeted pass reviewed 171 retrievable source pages, using [M5Stack release history](https://docs.m5stack.com/en/history), [Seeed documentation](https://wiki.seeedstudio.com/), [Waveshare hardware documentation](https://www.waveshare.com/wiki/Main_Page), the [DigiKey boards guide](https://www.digikey.com/en/maker/resources/boards-guide), and Mouser's [UNO Q](https://co.mouser.com/en/new/arduino/arduino-uno-q-platform/) and [UNO Breakout Carrier](https://eu.mouser.com/pl/new/arduino/arduino-asx00085-uno-breakout-carrier-board/) discovery pages. Saved technical references come from manufacturer documentation. DigiKey and Mouser discovery listings are not counted as pinout evidence.

Seeed additions include original XIAO schematics and searchable standard-edge pin functions. M5Stack additions include original schematics and selected external HY2.0, Hat2-Bus and Cardputer-Adv EXT tables. Waveshare additions concentrate on previously empty MCU board records. Adafruit Fruit Jam and Sparkle Motion, DFRobot UNIHIKER K10, Arduino and Renesas receive additional original references.

The UNO Breakout Carrier source contains three actual PDF pages, although page 1 says four. Its 3.3 V MCU and 1.8 V MPU signals must remain distinct; advanced assignments may not be supported by Arduino software. Renesas EK-RA8P1 v1 pages retain switch/jumper requirements and unpopulated-connector notes. Native tables cover named external connectors only and do not assert all-connector completeness.

## Remaining work

This pass does not establish a complete worldwide inventory. The [coverage audit](../PINOUT_COVERAGE.md) continues to identify missing physical maps and incomplete electrical/revision review for every listing. [Exact intake, exclusions and pending downloads](../catalog/vendor-intake-2026.10.2.json) record the attempted sources. Some M5Stack downloads timed out, several links returned HTML instead of images, and the VENTUNO Q schematic exceeded the intake size limit; these do not count as imported assets. Pixelblaze V3, Raspberry Pi 500+ and D-Robotics RDK X5M/X5 remain explicit follow-up leads requiring exact-variant evidence.

Generic Raspberry Pi maps found on Waveshare pages, an unrelated ESP32 map, and a sibling LCD model's image were excluded. GPIO block diagrams and component-location photographs retain their supporting-reference labels. Manufacturer artwork retains its original rights; unknown reuse/print rights remain unresolved. No new complete-device electrical approval is implied.

## Publication

The source catalog and browser guide use collection 2026.10.2. Existing downloadable releases and installed desktop catalogs remain at their original published versions. The current browser/source app remains 0.15.0; this content update does not distribute a new installer. Local guide copies are synchronized after the production deployment is verified.

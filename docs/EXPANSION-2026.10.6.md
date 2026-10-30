# Collection 2026.10.6 — October 30 manufacturer review

**First Edition / 2026** remains the editorial edition. This snapshot adds **nine board/module listings and four maker sensor listings**, updates one existing board, and saves **39 reference attachments, including five physical pinout images**.

## Physical pinout additions

- **Wireless-Tag WT9932S31-TINY:** manufacturer pinout v1.0, schematic v1.0 and English user guide v1.1. Manufacturer resource history dates the documentation to October 23–25. This is an ESP32-S31 development board, not a chip-package pin map.
- **Adafruit Metro ESP32-P4 Hydra:** original PrettyPins SVG and printable PDF, linked rev A schematic/PCB CAD and v1-chip product specifications. The board must not be confused with an ESP32-P4X/v3 variant. Generic PSRAM wording in the product text conflicts with board-specific wording; no inferred power or memory limits were added.
- **Waveshare ESP32-S3-LR1121-ePaper-2.9:** physical map, 14-pin expansion interface and schematic. Match HF/LF antenna bands, battery connector polarity and PCB revision.
- **Waveshare ESP32-P4-Core:** castellated circuit-board module map and schematic. This is distinct from the already-listed Core DEV KIT.
- **M5Stack Stamp Timer Power2 (S021):** original physical pad map extracted losslessly from page 4 of the manufacturer manual, plus that manual and schematic. The source PDF hash, page, image object and extracted-image hash are recorded. Power-management pins are not attached-host GPIO.

## Supporting references

- **M5Stack Unit DoF6, DoF9, DoF10 and BMM350:** manufacturer history records release on October 23. Hardware manuals, source schematics/component datasheet links and enclosure connector-label images are recorded. DoF6/DoF9 schematic PDFs are saved; DoF10/BMM350 standalone schematic downloads were unavailable during this pass, with source links retained. Connector labels are not counted as complete physical maps.
- **LattePanda Sigma 2:** ten original connector/switch diagrams covering GPIO, serial, front panel/audio, USB, power, fans and RTC battery. The 34-pin header exposes RP2350 and Intel PCH signals. These are connector references, not a complete board overview; manufacturer specifications and electrical GPIO guidance are linked. A separate board PDF datasheet remains unverified.
- **Wireless-Tag WTDKP4C5-S1, WT99P461-S1 and WT9932P4-MINI-A1:** saved manufacturer user guides and schematics fill older collection omissions. Separate physical map images remain missing; some original manuals are in Chinese.
- **Waveshare ESP32-DEV-KIT-XX:** saved its board schematic. The currently published pinout image matches the existing SHA-256, so it was not duplicated.

## Discovery register and remaining leads

Source discovery was attempted for all **163 existing brand labels** across 256 seed URLs, followed by targeted manufacturer documentation checks. Forty-seven initial page requests failed; successful retries and focused checks recovered some. Brand labels include sellers and aliases. An unchanged or unavailable seed page does not prove that a brand has no new products. This is a dated discovery pass, not a complete worldwide inventory.

[Brand-by-brand JSON](../catalog/brand-sweep-2026.10.6.json) · [CSV](../catalog/brand-sweep-2026.10.6.csv) · [Intake and original hashes](../catalog/vendor-intake-2026.10.6.json)

Follow-up leads remain explicit:

- Adafruit RV-8803 breakout: product and component datasheet available; board-specific physical pinout not yet verified.
- Wireless-Tag WT9932P4C61-TINY and other P4/S3 variants: resources need further retrieval and exact-model visual review.
- HardKernel ODROID-M1S Lite: manufacturer shop links older M1S header photos; these were not imported as Lite pinouts. Exact-model connector documentation needs review.
- Makerfabs LR2021 image-transmission prototype: October 23 development report; no verified production-board physical pinout in the reviewed article.
- Milk-V Titan and Antmicro Jetson expansion boards: connector/board documentation needs further physical-map review.
- Existing NodeMCU identity gaps, older pico-clone omissions and brands with source-access gaps remain open. No new NodeMCU hardware launch was established in this pass.

## Provenance and rights

Every addition has an original manufacturer link and reference-scope labels. Board schematics, hardware manuals, component datasheets and physical pinouts are distinct. No new independent electrical tests or all-connector completeness approvals are claimed.

Adafruit's Hydra design repository states **CC BY-SA 3.0 Unported**, designed by **Limor Fried/Ladyada for Adafruit Industries**. Its original README and license are included unchanged under [library/licenses/adafruit-metro-esp32-p4-hydra](../library/licenses/adafruit-metro-esp32-p4-hydra/README.md), and references retain that attribution. Other manufacturer artwork keeps its existing rights status; the project's code/editorial license does not relicense it.

## Brand source-discovery results

| Brand label | Existing records | Added/updated records | Result |
|---|---:|---:|---|
| 01space | 4 | 0 | discovery reviewed follow up needed |
| 0xCB | 2 | 0 | discovery reviewed follow up needed |
| 1BitSquared | 2 | 0 | discovery reviewed follow up needed |
| 2231puppy | 1 | 0 | source access or identity gap |
| 42. Keebs | 1 | 0 | discovery reviewed follow up needed |
| 8086 Consultancy | 2 | 0 | discovery reviewed follow up needed |
| ATMegaZero | 1 | 0 | discovery reviewed follow up needed |
| Adafruit | 185 | 1 | reviewed additions |
| Ai-Thinker | 4 | 0 | discovery reviewed follow up needed |
| Antmicro | 1 | 0 | discovery reviewed follow up needed |
| Arduino | 94 | 0 | discovery reviewed follow up needed |
| Autosport Labs | 1 | 0 | discovery reviewed follow up needed |
| Banana Pi | 81 | 0 | source access or identity gap |
| BeagleBoard.org | 8 | 0 | discovery reviewed follow up needed |
| Benjamin Shockley | 1 | 0 | discovery reviewed follow up needed |
| Boardsource | 1 | 0 | discovery reviewed follow up needed |
| Bradán Lane STUDIO | 1 | 0 | discovery reviewed follow up needed |
| BrainBoardz Inc. | 1 | 0 | discovery reviewed follow up needed |
| Breadstick Innovations | 1 | 0 | discovery reviewed follow up needed |
| BrisbaneSilicon | 1 | 0 | discovery reviewed follow up needed |
| CRCibernetica | 1 | 0 | discovery reviewed follow up needed |
| CircuitArt | 1 | 0 | discovery reviewed follow up needed |
| Community | 1 | 0 | discovery reviewed follow up needed |
| CrumpSpace | 1 | 0 | discovery reviewed follow up needed |
| Cytron Technologies | 8 | 0 | source access or identity gap |
| Czech maker & Make More | 1 | 0 | discovery reviewed follow up needed |
| DFRobot | 75 | 0 | discovery reviewed follow up needed |
| DIY-Thermocam reference / OEM unconfirmed | 1 | 0 | discovery reviewed follow up needed |
| DOIT | 2 | 0 | discovery reviewed follow up needed |
| Dangerous Prototypes | 1 | 0 | discovery reviewed follow up needed |
| Datanoise | 1 | 0 | source access or identity gap |
| DatanoiseTV | 1 | 0 | discovery reviewed follow up needed |
| Diodes Delight | 1 | 0 | discovery reviewed follow up needed |
| Double Take Labs | 1 | 0 | discovery reviewed follow up needed |
| ELECFREAKS | 1 | 0 | discovery reviewed follow up needed |
| Elechouse | 27 | 0 | discovery reviewed follow up needed |
| Elecrow | 40 | 0 | discovery reviewed follow up needed |
| Electrolama | 1 | 0 | discovery reviewed follow up needed |
| Electronic Cats | 1 | 0 | discovery reviewed follow up needed |
| Espressif | 70 | 0 | discovery reviewed follow up needed |
| Fablab Barcelona | 1 | 0 | discovery reviewed follow up needed |
| Flipper Devices | 1 | 0 | discovery reviewed follow up needed |
| Flipper Zero | 1 | 0 | discovery reviewed follow up needed |
| Franzininho | 2 | 0 | discovery reviewed follow up needed |
| Freenove | 7 | 0 | discovery reviewed follow up needed |
| FriendlyELEC | 69 | 0 | discovery reviewed follow up needed |
| FutureKeys | 1 | 0 | discovery reviewed follow up needed |
| Generic | 1 | 0 | discovery reviewed follow up needed |
| Generic - manufacturer unconfirmed | 8 | 0 | discovery reviewed follow up needed |
| Generic / manufacturer unconfirmed | 16 | 0 | source access or identity gap |
| Gravitech | 4 | 0 | discovery reviewed follow up needed |
| Guition | 27 | 0 | discovery reviewed follow up needed |
| HEIA-FR | 2 | 0 | discovery reviewed follow up needed |
| HXR.DK | 1 | 0 | discovery reviewed follow up needed |
| Hack Club | 2 | 0 | discovery reviewed follow up needed |
| HaleHound | 3 | 0 | discovery reviewed follow up needed |
| Hangzhou LeBan | 1 | 0 | discovery reviewed follow up needed |
| HardKernel | 1 | 0 | discovery reviewed follow up needed |
| Hat Labs | 3 | 0 | discovery reviewed follow up needed |
| Heltec | 43 | 0 | discovery reviewed follow up needed |
| High Code | 2 | 0 | discovery reviewed follow up needed |
| Inland | 67 | 0 | discovery reviewed follow up needed |
| Invector Labs | 10 | 0 | discovery reviewed follow up needed |
| JPConstantineau | 5 | 0 | discovery reviewed follow up needed |
| Joy-IT | 41 | 0 | discovery reviewed follow up needed |
| Kevin Matocha | 1 | 0 | source access or identity gap |
| LILYGO | 151 | 0 | discovery reviewed follow up needed |
| LOLIN | 3 | 0 | discovery reviewed follow up needed |
| LattePanda | 8 | 1 | reviewed additions |
| Luatos | 2 | 0 | source access or identity gap |
| Luckfox | 18 | 0 | discovery reviewed follow up needed |
| M5Stack | 660 | 5 | reviewed additions |
| Maker Go | 2 | 0 | discovery reviewed follow up needed |
| MakerM0 | 1 | 0 | discovery reviewed follow up needed |
| Makerfabs | 1 | 0 | discovery reviewed follow up needed |
| Maple | 1 | 0 | discovery reviewed follow up needed |
| Melopero | 1 | 0 | discovery reviewed follow up needed |
| MicroDev | 2 | 0 | source access or identity gap |
| Microchip | 1 | 0 | source access or identity gap |
| Milk-V | 6 | 0 | source access or identity gap |
| Mixly | 2 | 0 | discovery reviewed follow up needed |
| Morpheans | 1 | 0 | discovery reviewed follow up needed |
| Muselab | 2 | 0 | discovery reviewed follow up needed |
| Music Thing Modular | 1 | 0 | discovery reviewed follow up needed |
| NHB Systems | 1 | 0 | source access or identity gap |
| NVIDIA | 8 | 0 | discovery reviewed follow up needed |
| Newsan | 1 | 0 | discovery reviewed follow up needed |
| NodeMCU | 3 | 0 | discovery reviewed follow up needed |
| Nologo | 51 | 0 | discovery reviewed follow up needed |
| OTAKE Takayoshi | 1 | 0 | discovery reviewed follow up needed |
| Oak Development Technologies | 4 | 0 | discovery reviewed follow up needed |
| Olimex | 5 | 0 | discovery reviewed follow up needed |
| OpenSourceSDRLab | 3 | 0 | discovery reviewed follow up needed |
| Orange Pi | 40 | 0 | discovery reviewed follow up needed |
| Oxocard | 4 | 0 | discovery reviewed follow up needed |
| PCBCupid | 1 | 0 | discovery reviewed follow up needed |
| PJRC | 12 | 0 | discovery reviewed follow up needed |
| PROVES Kit | 1 | 0 | source access or identity gap |
| Pajenicko s.r.o. | 1 | 0 | discovery reviewed follow up needed |
| PandaByte | 1 | 0 | discovery reviewed follow up needed |
| Pcbcupid | 5 | 0 | discovery reviewed follow up needed |
| Pimoroni | 31 | 0 | discovery reviewed follow up needed |
| Pololu | 6 | 0 | source access or identity gap |
| Potekku | 1 | 0 | source access or identity gap |
| Prokyber | 1 | 0 | discovery reviewed follow up needed |
| QDtech | 2 | 0 | discovery reviewed follow up needed |
| Quadbit | 1 | 0 | discovery reviewed follow up needed |
| RAKwireless | 51 | 0 | discovery reviewed follow up needed |
| REYAX | 1 | 0 | discovery reviewed follow up needed |
| RF.Guru | 1 | 0 | discovery reviewed follow up needed |
| Radomir Dopieralski | 2 | 0 | discovery reviewed follow up needed |
| Radxa | 12 | 0 | discovery reviewed follow up needed |
| Raspberry Pi | 23 | 0 | source access or identity gap |
| Renesas | 1 | 0 | discovery reviewed follow up needed |
| RockBase IoT / NMTech | 2 | 0 | discovery reviewed follow up needed |
| STMicroelectronics | 42 | 0 | source access or identity gap |
| SecuringHardware.com | 1 | 0 | discovery reviewed follow up needed |
| Seeed Studio | 538 | 0 | discovery reviewed follow up needed |
| Silicognition LLC | 1 | 0 | discovery reviewed follow up needed |
| Silicon Labs | 1 | 0 | source access or identity gap |
| Sipeed | 6 | 0 | discovery reviewed follow up needed |
| Smart Bee Designs | 3 | 0 | discovery reviewed follow up needed |
| Solder Party | 5 | 0 | discovery reviewed follow up needed |
| Soldered | 1 | 0 | discovery reviewed follow up needed |
| SparkFun | 55 | 0 | discovery reviewed follow up needed |
| SplitKB | 1 | 0 | discovery reviewed follow up needed |
| Spotpear | 2 | 0 | discovery reviewed follow up needed |
| Spotpear (manufacturer unconfirmed) | 3 | 0 | discovery reviewed follow up needed |
| Squarofumi | 1 | 0 | discovery reviewed follow up needed |
| Steiert Solutions | 1 | 0 | discovery reviewed follow up needed |
| StudioLab | 1 | 0 | source access or identity gap |
| Sunrom (seller; OEM unconfirmed) | 5 | 0 | discovery reviewed follow up needed |
| Sunton | 40 | 0 | discovery reviewed follow up needed |
| Targett | 2 | 0 | source access or identity gap |
| TechOverflow | 2 | 0 | discovery reviewed follow up needed |
| Teenage Engineering | 1 | 0 | discovery reviewed follow up needed |
| Terasic | 1 | 0 | discovery reviewed follow up needed |
| Texas Instruments | 2 | 0 | source access or identity gap |
| ThingPulse | 1 | 0 | discovery reviewed follow up needed |
| TinyCircuits | 2 | 0 | discovery reviewed follow up needed |
| Turkish Technology Team Foundation | 6 | 0 | discovery reviewed follow up needed |
| Unattributed chip reference | 2 | 0 | source access or identity gap |
| Unexpected Maker | 26 | 0 | discovery reviewed follow up needed |
| Unknown | 1 | 0 | discovery reviewed follow up needed |
| VCC-GND Studio | 4 | 0 | discovery reviewed follow up needed |
| VIDI | 1 | 0 | discovery reviewed follow up needed |
| WEEKIN | 1 | 0 | source access or identity gap |
| WIZnet | 9 | 0 | source access or identity gap |
| Waveshare | 386 | 3 | reviewed additions |
| WeAct Studio | 49 | 0 | discovery reviewed follow up needed |
| Wee Noise Makers | 3 | 0 | discovery reviewed follow up needed |
| Wemos | 13 | 0 | discovery reviewed follow up needed |
| WiPhone | 1 | 0 | discovery reviewed follow up needed |
| Wireless-Tag | 1 | 4 | reviewed additions |
| WisdPi | 2 | 0 | discovery reviewed follow up needed |
| Xteink | 1 | 0 | discovery reviewed follow up needed |
| Yoto Limited | 2 | 0 | discovery reviewed follow up needed |
| Zach Richard | 1 | 0 | discovery reviewed follow up needed |
| cezerio | 2 | 0 | source access or identity gap |
| dronecz | 1 | 0 | discovery reviewed follow up needed |
| micro-bit Educational Foundation | 2 | 0 | discovery reviewed follow up needed |
| nullbits | 1 | 0 | discovery reviewed follow up needed |
| senseBox | 3 | 0 | discovery reviewed follow up needed |

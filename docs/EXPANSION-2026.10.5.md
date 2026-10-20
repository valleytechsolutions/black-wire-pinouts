# Collection 2026.10.5 — brand discovery and reviewed additions

Checked 2026-10-20. **First Edition / 2026** remains the editorial edition.

**16 board/device records + 16 maker-module records; 72 reference attachments, including nine physical-pinout image entries.** The remaining attachments are original schematics, hardware manuals, board datasheet and labeled PCB layouts. These are newly collected records, not 32 claimed new product launches.

## Added physical maps

- Seeed Studio XIAO STM32C5: front/back maps and v1.0 schematic.
- M5Stack PaperDIY: external SPI/I2S FPC and e-paper connector maps plus schematic. K159 and K159-B kit aliases share one controller record. PMIC signals and display supply rails are not general-purpose ESP32 GPIO.
- 01space RP2040-0.42LCD, ESP32-S3-0.42OLED and ESP32-PICO-D4-RGB: original physical maps; the latter two also have board schematics. These fill older omissions.
- WIZnet W6100-EVB-Pico and W6100-EVB-Pico2: original pinout maps and schematics. The older Pico map has a W5100S legend on the W6100 page; retain the original and cross-check the schematic.

## Supporting documentation and explicit gaps

W6300-EVB-Pico/Pico2, LILYGO T-Dongle-S3-Dual/Plus, Raspberry Pi Compute Module Zero, Radxa X5/Cubie A7S, Pimoroni Inventor 2350 W and SparkFun IoT RedBoard RP2350 have board documentation saved. They are not counted as new complete physical pinouts. WIZnet explicitly marks both W6300 pinout images as coming soon. CM0 has a physical footprint and a 132-contact function table in its board datasheet, not a one-sheet signal map.

Sixteen Adafruit sensor/interface breakouts have their hardware-guide PDFs, schematics and labeled PCB layouts saved. Pin functions are described in the manuals. PCB label layouts remain supporting references; all-connector review is pending. The records include CP2105, TSL2585, TCS3448, TMF8806/TMF8801, GP8403, ADS7128, STCC4/SHT41, APDS9999, MAX44009, VCNL4030, ADS122C04, TMP119, AS7343, AS7331 and TCS3430/TCS34303.

## Discovery coverage and limits

The pass attempted seed/source discovery for all **163 current brand labels** and compared visible candidate names with the existing catalog. This includes brand aliases, resellers and unidentified hardware. It is not a complete crawl of every product, and access failures cannot establish that a manufacturer has no new hardware. [Brand-by-brand JSON](../catalog/brand-sweep-2026.10.5.json) · [CSV](../catalog/brand-sweep-2026.10.5.csv).

Waveshare ESP32-C5-Pico/MINI-KIT, Arduino UNO Q/VENTUNO Q, SparkFun ESP32-C5 Thing Plus and LILYGO T-Display P4 variants already have records. Manufacturer navigation and aliases were checked before adding duplicate-looking models. NodeMCU source identity and unavailable manufacturer pages remain unresolved where noted in prior audits.

Follow-up leads still need exact model/revision and visual-map verification: Milk-V Titan connectors; other LILYGO aliases/new variants; remaining Adafruit arrivals; ST NUCLEO-C5/H5/U3 variants; Heltec V4-R8 expansion hardware; 01space ESP32-C3FH4-RGB and RP2040-1.14LCD. ESP32-S31 chip documentation alone is not an eligible development-board pinout.

## Validation

All 4,924 original/companion file hashes and 9,828 manifest paths passed collection validation. Existing board assets, connector references, power profiles and wiring guides were preserved. New-record endpoint checks reached 94 of 95 distinct URLs; the CM0 product page restricted automated access, while its official datasheet downloaded successfully. Older endpoint results retain their original dates.

## Provenance and use

Original asset bytes and SHA-256 hashes are preserved; every new record links to manufacturer documentation. Board manuals, schematics, board datasheets and component datasheets have distinct scopes. No new electrical test results or complete-device approvals are claimed. Manufacturer artwork retains its original rights; the project license does not grant redistribution or print permission for it.

[Machine-readable intake and asset hashes](../catalog/vendor-intake-2026.10.5.json) · [Documentation coverage](../DOCUMENTATION.md) · [Physical pinout coverage](../PINOUT_COVERAGE.md)

## Brand source-discovery register

| Brand label | Existing records | Added records | Discovery result |
|---|---:|---:|---|
| 01space | 1 | 3 | reviewed additions |
| 0xCB | 2 | 0 | discovery reviewed follow up needed |
| 1BitSquared | 2 | 0 | discovery reviewed follow up needed |
| 2231puppy | 1 | 0 | source access or identity gap |
| 42. Keebs | 1 | 0 | discovery reviewed follow up needed |
| 8086 Consultancy | 2 | 0 | discovery reviewed follow up needed |
| ATMegaZero | 1 | 0 | discovery reviewed follow up needed |
| Adafruit | 169 | 16 | reviewed additions |
| Ai-Thinker | 4 | 0 | source access or identity gap |
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
| HardKernel | 1 | 0 | source access or identity gap |
| Hat Labs | 3 | 0 | discovery reviewed follow up needed |
| Heltec | 43 | 0 | discovery reviewed follow up needed |
| High Code | 2 | 0 | discovery reviewed follow up needed |
| Inland | 67 | 0 | discovery reviewed follow up needed |
| Invector Labs | 10 | 0 | discovery reviewed follow up needed |
| JPConstantineau | 5 | 0 | discovery reviewed follow up needed |
| Joy-IT | 41 | 0 | discovery reviewed follow up needed |
| Kevin Matocha | 1 | 0 | discovery reviewed follow up needed |
| LILYGO | 149 | 2 | reviewed additions |
| LOLIN | 3 | 0 | discovery reviewed follow up needed |
| LattePanda | 8 | 0 | discovery reviewed follow up needed |
| Luatos | 2 | 0 | source access or identity gap |
| Luckfox | 18 | 0 | discovery reviewed follow up needed |
| M5Stack | 659 | 1 | reviewed additions |
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
| Nologo | 51 | 0 | source access or identity gap |
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
| Pimoroni | 30 | 1 | reviewed additions |
| Pololu | 6 | 0 | source access or identity gap |
| Potekku | 1 | 0 | discovery reviewed follow up needed |
| Prokyber | 1 | 0 | discovery reviewed follow up needed |
| QDtech | 2 | 0 | discovery reviewed follow up needed |
| Quadbit | 1 | 0 | discovery reviewed follow up needed |
| RAKwireless | 51 | 0 | discovery reviewed follow up needed |
| REYAX | 1 | 0 | discovery reviewed follow up needed |
| RF.Guru | 1 | 0 | discovery reviewed follow up needed |
| Radomir Dopieralski | 2 | 0 | discovery reviewed follow up needed |
| Radxa | 10 | 2 | reviewed additions |
| Raspberry Pi | 22 | 1 | reviewed additions |
| Renesas | 1 | 0 | discovery reviewed follow up needed |
| RockBase IoT / NMTech | 2 | 0 | discovery reviewed follow up needed |
| STMicroelectronics | 42 | 0 | source access or identity gap |
| SecuringHardware.com | 1 | 0 | discovery reviewed follow up needed |
| Seeed Studio | 537 | 1 | reviewed additions |
| Silicognition LLC | 1 | 0 | discovery reviewed follow up needed |
| Silicon Labs | 1 | 0 | source access or identity gap |
| Sipeed | 6 | 0 | discovery reviewed follow up needed |
| Smart Bee Designs | 3 | 0 | discovery reviewed follow up needed |
| Solder Party | 5 | 0 | discovery reviewed follow up needed |
| Soldered | 1 | 0 | discovery reviewed follow up needed |
| SparkFun | 54 | 1 | reviewed additions |
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
| WEEKIN | 1 | 0 | discovery reviewed follow up needed |
| WIZnet | 5 | 4 | source access or identity gap |
| Waveshare | 386 | 0 | discovery reviewed follow up needed |
| WeAct Studio | 49 | 0 | discovery reviewed follow up needed |
| Wee Noise Makers | 3 | 0 | discovery reviewed follow up needed |
| Wemos | 13 | 0 | discovery reviewed follow up needed |
| WiPhone | 1 | 0 | discovery reviewed follow up needed |
| Wireless-Tag | 1 | 0 | discovery reviewed follow up needed |
| WisdPi | 2 | 0 | discovery reviewed follow up needed |
| Xteink | 1 | 0 | discovery reviewed follow up needed |
| Yoto Limited | 2 | 0 | discovery reviewed follow up needed |
| Zach Richard | 1 | 0 | discovery reviewed follow up needed |
| cezerio | 2 | 0 | source access or identity gap |
| dronecz | 1 | 0 | discovery reviewed follow up needed |
| micro-bit Educational Foundation | 2 | 0 | discovery reviewed follow up needed |
| nullbits | 1 | 0 | discovery reviewed follow up needed |
| senseBox | 3 | 0 | discovery reviewed follow up needed |

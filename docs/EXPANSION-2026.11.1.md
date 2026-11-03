# Collection 2026.11.1 — November 3 manufacturer documentation review

**First Edition / 2026** remains the editorial edition. Collection snapshots and desktop app versions do not create a new book edition.

**14 new listings · 3 existing listings updated · 32 saved reference attachments · 8 physical pinout images.** The saved attachments contain **32 distinct files**. Counts describe this intake, not a claim that every listing has a complete pinout or board datasheet.

## Discovery scope

Source discovery was attempted for all **163 existing brand labels** using **256 initial seed URLs**; **49 initial requests failed**. Later focused retrievals may recover individual sources. Labels include aliases, distributors and unidentified hardware. A successful page request, unchanged page or failed request does not establish that a manufacturer has no new products.

This pass combines selected current documentation with older collection omissions. Announcement dates, documentation timestamps, HTTP modification dates and board revisions describe different events. They are not interchangeable release dates.

[Brand register JSON](../catalog/brand-sweep-2026.11.1.json) · [CSV](../catalog/brand-sweep-2026.11.1.csv) · [Intake, original URLs and hashes](../catalog/vendor-intake-2026.11.1.json)

## Added and updated references

| Brand | Listing | Intake action | Saved references | Physical pinout images |
|---|---|---|---:|---:|
| Waveshare | ESP32-S31-Zero | board | 2 | 1 |
| Wireless-Tag | WT9932P4C61-TINY | board | 3 | 1 |
| Wireless-Tag | WT9932P4-TINY | board | 3 | 1 |
| Unexpected Maker | TinyC6[D] | board | 2 | 1 |
| Unexpected Maker | TinyPICO[D] | board | 2 | 1 |
| SparkFun | SparkFun 6DoF IMU Breakout - BMI330 (Qwiic) | maker | 2 | 0 |
| SparkFun | SparkFun Triple Axis Accelerometer Breakout - BMA456 (Qwiic) | maker | 2 | 0 |
| Adafruit | Adafruit RV-8803 High Accuracy Real Time Clock Breakout | maker | 3 | 0 |
| Unexpected Maker | Unexpected Maker TinyPICO NANO | existing-board-update | 1 | 1 |
| Sipeed | Tang Nano | board | 2 | 1 |
| Sipeed | Tang Nano 9K | board | 3 | 1 |
| Milk-V | Titan | board | 3 | 0 |
| Antmicro | PCIe Switch Expansion for Jetson Orin Baseboard | board | 1 | 0 |
| Elechouse | ST25R3916B Mini V2 | maker | 2 | 0 |
| Electronic Cats | Flipper Add-On CAN bus | maker | 1 | 0 |
| Seeed Studio | XIAO ePaper Display Board EN05 | existing-board-update | 0 | 0 |
| Seeed Studio | XIAO ePaper Display Board EN04 | existing-board-update | 0 | 0 |

### Exact-model scope and timing

- **Waveshare ESP32-S31-Zero:** Fresh manufacturer documentation: both supplied pinout assets report HTTP Last-Modified 2026-11-02. This is asset metadata, not a verified launch date. Physical board header map visually inspected on 2026-11-03; separate expansion reference shows exact orientation of the 40-pin board-to-board connector. The product-linked manual https://docs.waveshare.com/ESP32-S31-Zero returned HTTP 404 during review; no exact-board schematic/datasheet available from the fetched page. Do not mark complete documentation or electrically tested. Manufacturer artwork rights are not established.
- **Wireless-Tag WT9932P4C61-TINY:** Official resource-page history was updated 2026-11-02 for open-hardware links. Pinout V1.1 dates to the 2026-09-22 resource revision; this is a missing existing board, not a verified November launch. Original diagram visually identifies physical edge-header positions. FPC connector internals and independent electrical/all-connector completeness are not approved.
- **Wireless-Tag WT9932P4-TINY:** Official resource-page history was updated 2026-11-02 for open-hardware links. English guide V2.0 dates to the 2026-10-20 resource revision; initial documentation was 2025-09-10. This is an older omission, not a verified November launch. Original diagram visually identifies physical edge-header positions. FPC connector internals and independent electrical/all-connector completeness are not approved.
- **Unexpected Maker TinyC6[D]:** Distinct Series[D] model with switched onboard/u.FL antenna and fuel gauge, not the older non-D board. Current manufacturer pinout and specifications verified; exact public launch date not established. Source commit 59ec71985f461859e041932c7409b49421002314. Map includes edge pins and internal peripherals; electrical/all-connector completeness not independently approved.
- **Unexpected Maker TinyPICO[D]:** Distinct Series[D] model with switched onboard/u.FL antenna and fuel gauge, not the older non-D board. Current manufacturer pinout and specifications verified; exact public launch date not established. Source commit 59ec71985f461859e041932c7409b49421002314. Map includes edge pins and internal peripherals; electrical/all-connector completeness not independently approved.
- **SparkFun SparkFun 6DoF IMU Breakout - BMI330 (Qwiic):** Manufacturer announced this breakout on 2026-10-30 at https://news.sparkfun.com/17433 . Visually reviewed original labeled PCB photograph: physical through-hole pads are legibly labeled, but there is no separate full connector pin-reference diagram. Keep board labels classification and incomplete physical-pinout status. Component datasheet does not substitute for board documentation.
- **SparkFun SparkFun Triple Axis Accelerometer Breakout - BMA456 (Qwiic):** Manufacturer announced this breakout on 2026-10-30 at https://news.sparkfun.com/17433 . Visually reviewed original labeled PCB photograph: physical through-hole pads are legibly labeled, but there is no separate full connector pin-reference diagram. Keep board labels classification and incomplete physical-pinout status. Component datasheet does not substitute for board documentation.
- **Adafruit Adafruit RV-8803 High Accuracy Real Time Clock Breakout:** Official guide published 2026-11-02 and includes a labeled front/back board image, pin-function documentation, board schematic and fabrication print. Photo/fabprint are supporting board labels, not independently complete physical pinouts. Do not treat the RTC chip datasheet as the breakout datasheet.
- **Sipeed Tang Nano:** Older missing-board gap, not a newly released November 2026 board. Visually inspected manufacturer-hosted 1440x1014 diagram and original 5676x4000 artwork source: actual physical board with both header rows and JTAG pins mapped; preserve creator @kprasadvnsi. Dedicated board datasheet not located; manufacturer hardware guide and full schematic available. Match original GW1N-1 board; do not confuse with Nano 1K.
- **Sipeed Tang Nano 9K:** Older missing-board gap, not a new release. Physical board image visually verified: both 24-pin headers with FPGA I/O names, power, signal aliases and I/O-bank voltages; board silkscreen V1.0. Datasheet is a board datasheet, not chip-only. Schematic PDF has title Rev NO.01 and revision-history entries through 6202 / 2022-10-23; retain revision cautions rather than imply every production variant verified. Independent electrical review pending.
- **Milk-V Titan:** Supporting documentation only: V2.1 motherboard connector-location diagram, 28-page original schematic and 2-page component placement PDF visually verified. Interface image labels whole ports, not individual GPIO pins; must not count it as a complete physical pinout. Hardware guide contains separate front-panel/USB/fan pin tables; no complete board-wide physical pinout approved. No dedicated board datasheet identified.
- **Antmicro PCIe Switch Expansion for Jetson Orin Baseboard:** Manufacturer announcement 2026-10-27; this is an expansion board for Antmicro Jetson Orin Baseboard, not a standalone Jetson. Original 8-page schematic title date 2026-08-26, Rev1.0.0, printed commit f3082c87; URL artifact identifier d551c6be differs, retain both instead of calling them the same commit. Schematic only; no complete physical pinout image approved, no dedicated board datasheet. Useful supporting reference if gap status remains explicit.
- **Elechouse ST25R3916B Mini V2:** V2 ships in I2C mode, unlike V1. Original datasheet page 3 shows rear-side signal labels and a pin-function table. The extracted CAD image is supporting board labeling. Supply voltage and digital IO level differ. V1 current measurements in the V2 datasheet are not V2 tested limits; no power-test values were added.
- **Electronic Cats Flipper Add-On CAN bus:** Older omission. Original reference labels CAN H/L terminal wiring and the OBD-II cable; the host-header pins are not independently mapped here. Hardware sources and wiki are linked. MCP2515 is classical CAN 2.0B, not CAN FD. Component voltage/current specifications are not board power requirements.

## Selected review findings and remaining gaps

The notes below describe research outcomes. A researched lead or suggested relationship is not necessarily an imported listing; use the intake table above to see what changed.

- **Wireless-Tag:** WT9932P4C61-TINY and WT9932P4-TINY physical edge-header maps were reviewed. November 2 resource histories concern open-hardware links; underlying pinout/manual revisions predate those changes. These are older omissions, not verified November launches. Edge-header review does not establish all CSI/DSI connector contacts. [Source 1](https://wiki.wireless-tag.com/docs/en/WT9932P4C61-TINY/board_resources.html) · [Source 2](https://wiki.wireless-tag.com/docs/en/WT9932P4-TINY/board_resources.html)
- **Unexpected Maker:** TinyC6[D] and TinyPICO[D] are distinct current Series[D] designs; original 2026 map cards reviewed without precise launch dates. TinyPICO Nano V4 has a visibly identified physical pad map and should enrich the existing family record with explicit V4 scope. EdgeS3[D] II homepage wording did not establish a separate validated pinmap; do not duplicate or silently relabel older revisions. [Source 1](https://unexpectedmaker.com/)
- **SparkFun:** BMI330 SEN-31767 and BMA456 SEN-32097 were announced October 30. Labeled PCB pictures are supporting board labels, not independently complete pinouts. Hardware repositories identify CC BY-SA 4.0; that license does not extend to Bosch component PDFs. BMI330 guide temperature statements conflict and BMA456 product wording contains typo-like values; no Power Desk values were imported from these unresolved statements. [Source 1](https://news.sparkfun.com/17433)
- **Adafruit RV-8803 PID6538:** Guide publication November 2 is documentation timing, not proof of board launch. Front/back photograph and fabrication print were reviewed as board labels, not a complete physical pinout. PCB repository is CC BY-SA 3.0 with README accompaniment requested; photography rights were not independently established. [Source 1](https://www.adafruit.com/product/6538)
- **Adafruit Si5351C eight-channel TCXO PID6534:** Held for exact-model documentation: current eight-channel Si5351C product links an older guide describing three-channel Si5351A hardware from 2014/2022. Those older maps must not be used as the eight-channel board pinout. Product copy also differs on CLK6/7 limits; no Power Desk values should be copied until resolved. Component datasheet availability does not close the board-map gap. [Source 1](https://www.adafruit.com/product/6534) · [Source 2](https://cdn-shop.adafruit.com/product-files/6534/P6534+-+Si5351-B.pdf)
- **Arduino:** Existing collection already includes UNO Q, Nano R4 and Nesso N1. This bounded pass did not establish another post-October30 hardware launch; no exhaustive inventory claim. [Source 1](https://docs.arduino.cc/hardware/)
- **Espressif:** Existing catalog includes ESP-Mosaico, S31 Core/Korvo, P4X-C5 and P4X-EYE. Guessed discovery routes returned404; exact known identities and official search evidence were used. This is not an exhaustive product audit. [Source 1](https://docs.espressif.com/projects/esp-dev-kits/en/latest/)
- **WIZnet:** Existing W6300/W6100 Pico/Pico2 identities were not counted as new boards. Guessed entry routes failed; further catalog review remains necessary. [Source 1](https://docs.wiznet.io/Product/)
- **DFRobot:** Recent FireBeetle C5 and P4 identities are already cataloged. Manufacturer news checked; no independently verified additional post-October30 hardware launch in this bounded pass. [Source 1](https://www.dfrobot.com/new)
- **Pimoroni:** Tufty2350, Blinky2350 and Presto remain older candidate omissions. The new-products page is largely dynamic; no fully reviewed physical map was recovered. A firmware pin CSV is not a physical board map. [Source 1](https://shop.pimoroni.com/collections/new-products)
- **Inland:** Manufacturer community discovery endpoint returned403. Source-access gap remains; absence of additions is not evidence that there are no new products. [Source 1](https://community.microcenter.com/kb/categories/6-inland)
- **Elecrow:** Attempted new-arrivals discovery route was a soft404. Further catalog review is required; no complete-product or no-new-board claim. [Source 1](https://www.elecrow.com/wiki/)
- **Waveshare ESP32-S31-Zero:** Both official pin diagrams HTTP Last-Modified Mon, 02 Nov 2026 09:29 UTC; no launch-date assertion Manufacturer-linked https://docs.waveshare.com/ESP32-S31-Zero returns 404; no exact-board datasheet/schematic yet verified. Not established; manufacturer attribution retained, not relicensed by guide. Actual header photo and pin labels inspected; 40-pin B2B diagram separately scoped. [Source 1](https://www.waveshare.com/product/esp32-s31-zero.htm)
- **Seeed Studio OpenDisplay 4.26-inch Mono Kit:** New assembled kit uses the already-cataloged EN05 (Mono) or EN04 (Color) board; add descriptive search alias/resource relationship if desired, without treating the kit as a new PCB or copying duplicate pinout images. Wiki last updated Oct 22 indicates documentation predates marketing announcement. [Source 1](https://www.seeedstudio.com/blog/2026/11/03/meet-the-opendisplay-4-26%E2%80%B3-mono-7-3%E2%80%B3-color-kits-ultra-low-power-epaper-dashboards-for-home-assistant/)
- **Seeed Studio OpenDisplay 7.3-inch Color Kit:** New assembled kit uses the already-cataloged EN05 (Mono) or EN04 (Color) board; add descriptive search alias/resource relationship if desired, without treating the kit as a new PCB or copying duplicate pinout images. Wiki last updated Oct 22 indicates documentation predates marketing announcement. [Source 1](https://www.seeedstudio.com/blog/2026/11/03/meet-the-opendisplay-4-26%E2%80%B3-mono-7-3%E2%80%B3-color-kits-ultra-low-power-epaper-dashboards-for-home-assistant/)
- **Heltec RC32:** Older omission; no launch after 2026-10-30 established. Product page and resource index confirm exact family/variants. No original pin-map images or PDFs copied into public collection. Pin-map images linked from product page but not visually inspected in this pass. Heltec site terms section 2 covers photos/graphics, grants personal noncommercial/internal-business download use, and reserves other rights. RC52-62 and RCC6-62 PDFs explicitly restrict copying/distribution for commercial use without written permission. No separate public redistribution permission for product pin-map images found. Link-only; rights and technical review pending [Source 1](https://heltec.org/project/rc32/) · [Source 2](https://heltec.org/info/terms-and-conditions/)
- **Heltec RC32-62:** Older omission; no launch after 2026-10-30 established. Product page and resource index confirm exact family/variants. No original pin-map images or PDFs copied into public collection. Pin-map images linked from product page but not visually inspected in this pass. Official RC32-62 schematic directory links file named RCC6-L62_V1.0.PDF. Target contents not inspected; do not assert exact-board schematic validity from directory name. Heltec site terms section 2 covers photos/graphics, grants personal noncommercial/internal-business download use, and reserves other rights. RC52-62 and RCC6-62 PDFs explicitly restrict copying/distribution for commercial use without written permission. No separate public redistribution permission for product pin-map images found. Link-only; rights and technical review pending [Source 1](https://heltec.org/project/rc32/) · [Source 2](https://heltec.org/info/terms-and-conditions/)
- **Heltec RC32-68:** Older omission; no launch after 2026-10-30 established. Product page and resource index confirm exact family/variants. No original pin-map images or PDFs copied into public collection. Pin-map images linked from product page but not visually inspected in this pass. Heltec site terms section 2 covers photos/graphics, grants personal noncommercial/internal-business download use, and reserves other rights. RC52-62 and RCC6-62 PDFs explicitly restrict copying/distribution for commercial use without written permission. No separate public redistribution permission for product pin-map images found. Link-only; rights and technical review pending [Source 1](https://heltec.org/project/rc32/) · [Source 2](https://heltec.org/info/terms-and-conditions/)
- **Heltec RCC6:** Older omission; no launch after 2026-10-30 established. Product page and resource index confirm exact family/variants. No original pin-map images or PDFs copied into public collection. Pin-map images linked from product page but not visually inspected in this pass. RCC6-62 datasheet external-header table includes S3-like GPIO44/43/42/41/40/39/38, inconsistent with ESP32-C6 and other tables. Do not derive wiring or power tables until manufacturer resolves this conflict. RCC6 base PDF is listed but web tool returned 404; resource availability needs recheck. Heltec site terms section 2 covers photos/graphics, grants personal noncommercial/internal-business download use, and reserves other rights. RC52-62 and RCC6-62 PDFs explicitly restrict copying/distribution for commercial use without written permission. No separate public redistribution permission for product pin-map images found. Link-only; rights and technical review pending [Source 1](https://heltec.org/project/rcc6/) · [Source 2](https://heltec.org/info/terms-and-conditions/)
- **Heltec RCC6-62:** Older omission; no launch after 2026-10-30 established. Product page and resource index confirm exact family/variants. No original pin-map images or PDFs copied into public collection. Pin-map images linked from product page but not visually inspected in this pass. RCC6-62 datasheet external-header table includes S3-like GPIO44/43/42/41/40/39/38, inconsistent with ESP32-C6 and other tables. Do not derive wiring or power tables until manufacturer resolves this conflict. RCC6 base PDF is listed but web tool returned 404; resource availability needs recheck. Datasheet revision history 1.0.0 dated 2026-06-10 says Dev-Preview Version; resource modified October 9/10, not launch evidence. Heltec site terms section 2 covers photos/graphics, grants personal noncommercial/internal-business download use, and reserves other rights. RC52-62 and RCC6-62 PDFs explicitly restrict copying/distribution for commercial use without written permission. No separate public redistribution permission for product pin-map images found. Link-only; rights and technical review pending [Source 1](https://heltec.org/project/rcc6/) · [Source 2](https://heltec.org/info/terms-and-conditions/)
- **Heltec RC52-62:** Older omission; no launch after 2026-10-30 established. Product page and resource index confirm exact family/variants. No original pin-map images or PDFs copied into public collection. Pin-map images linked from product page but not visually inspected in this pass. Datasheet revision history 1.0.0 dated 2026-06-10 says Dev-Preview Version; resource modified October 9/10, not launch evidence. Heltec site terms section 2 covers photos/graphics, grants personal noncommercial/internal-business download use, and reserves other rights. RC52-62 and RCC6-62 PDFs explicitly restrict copying/distribution for commercial use without written permission. No separate public redistribution permission for product pin-map images found. Link-only; rights and technical review pending [Source 1](https://heltec.org/project/rc52/) · [Source 2](https://heltec.org/info/terms-and-conditions/)
- **Heltec WiFi LoRa 32 Expansion Kit V2:** V2 uses V4-R8 already cataloged; adds TF/SD, aluminum base, and differs from V1 firmware. Product Pin Map is the already-cataloged WiFi LoRa32 V4-R8 main-board pinout, not a complete kit/baseboard GPIO map. Do not duplicate as a complete new pinout. Older omission / dedicated expansion-board pin map missing [Source 1](https://heltec.org/project/v4-r8-ex/)
- **RAKwireless RAK3172-F:** Official August 24, 2026 bulletin announces external 512 KB flash variant. Product states pin-compatible with RAK3172 but links generic RAK3172-module documents. Do not silently relabel original RAK3172 map as independently verified -F reference. Not claimed new since Oct 30. Older omission; exact-variant physical map and documentation cross-check pending [Source 1](https://store.rakwireless.com/products/rak3172-f-fuota-lorawan-module) · [Source 2](https://news.rakwireless.com/rakwireless-bulletin-new-modules-for-lorawan-r-real-world-use-cases-and-growing-ecosystem-partnerships/)
- **M5Stack:** Latest official launch is Stamp Timer Power2 S021 Oct 30, already cataloged. Oct 23 DoF6/9/10/BMM350 also already cataloged. No post-Oct 30 launch identified. [Source 1](https://docs.m5stack.com/en/history)
- **NodeMCU:** Official page still presents ESP8266 DevKit; no new official board launch identified. Do not equate unverified seller-branded clones with NodeMCU official designs. [Source 1](https://www.nodemcu.com/index_en)
- **LILYGO:** Compared official directory to 151 existing records. Recent T-Dongle-S3-Dual/Plus,T-Display P4,T-Halow P4,T-Deck Max,T-Watch Ultra,T-Echo Card,T7 C5 etc already covered. No post-Oct 30 launch established; older modem/shield omissions remain for deeper review. Guessed shop new-arrival URL returned 404, not evidence of no launches. [Source 1](https://wiki.lilygo.cc/products/)
- **Seeed Studio:** Nov 3 OpenDisplay kits verified; existing EN04/EN05 physical boards account for these. Oct 30 XIAO Development Hub is tools/documentation update, not itself new hardware. New-arrivals storefront was JS-only and no product list extracted. [Source 1](https://www.seeedstudio.com/blog/news-center/)
- **RAKwireless:** September 24 bulletin includes RAK7392, RAK7268CV2-V, WisMesh Repeater Mini V2. Physical GPIO maps not verified; not added as complete pinouts. RAK3172-F older gap retained above. [Source 1](https://news.rakwireless.com/rakwireless-bulletin-gateway-management-new-hardware-field-stories-upcoming-events/)
- **Raspberry Pi:** Official November2 news is a price change for 16GB boards; no new hardware launch confirmed since October30. Zero3W/Pi4A kernel-patch search leads are not official board pinout sources and were not added. Existing Pico/Pi5/Pi500Plus entries already present. News landing-page check; not exhaustive all accessory SKUs. [Source 1](https://www.raspberrypi.com/news/)
- **LattePanda:** Sigma2 already exists in catalog; current manufacturer home references Sigma2 accessories. No additional post-October30 board pinout located. Current product/home spot check. [Source 1](https://www.lattepanda.com/) · [Source 2](https://docs.lattepanda.com/)
- **Radxa:** Current product leads X5/CubieA7S already tracked. Blog latest listed 2026 entry is June3 NAS announcement; no post-October30 release verified. X5 physical GPIO map remains a separate documentation gap. Public blog and product index; direct products HTTP403 limited retrieval. [Source 1](https://radxa.com/blog/) · [Source 2](https://radxa.com/products/)
- **Orange Pi:** OrangePi6Plus missing in catalog. Search-indexed manufacturer-authored manual shows V1.1 physical 40-pin board map, but indexed PDF returns404 and official orangepi.org endpoint refuses connection. Distributor current manuals index lacks Linux6Plus PDF. Do not substitute old OrangePi6Plus maps or claim retrieved asset. Remains high-priority retrieval gap. Primary-site retrieval blocked; distributor source is identified as reseller, not manufacturer. No new-release claim. [Source 1](https://www.orangepi.org/orangepiwiki/index.php/Orange_Pi_6_Plus) · [Source 2](https://orangepi.net/wp-content/uploads/2026/01/OrangePi_6_Plus_Cix_Linux-System_User-Manual_v0.7.pdf) · [Source 3](https://orangepi.net/user-manuals.html)
- **Banana Pi:** Current home product list includes M8/M7S/F4/Forge1/CanMVK230DZero/M5Pro/R4Pro/R4Lite/RV2/AI2N/SM10/CM6/CM5Pro; extensive existing catalog covers current models. No post-October30 new pinout verified in this bounded pass. Official current product landing page, not full historical/all-SKU audit. [Source 1](https://www.banana-pi.org/)
- **Milk-V:** Titan V2.1 missing. Collected connector-location artwork, schematic and assembly drawing; not a complete physical pinout. All are in the research notes. Titan targeted documentation follow-up; no exhaustive entire brand claim. [Source 1](https://milkv.io/docs/titan/getting-started/hardware) · [Source 2](https://milkv.io/docs/titan/getting-started/resources)
- **FriendlyELEC:** Current home highlights NanoPiR28S/M6V2/NEO3Plus/NanoPCT6Plus/M5/R3SLTS/Zero2 and existing tracked models; no new post-October30 release verified. Current manufacturer catalog landing page compared with existing brand names. [Source 1](https://www.friendlyelec.com/)
- **NVIDIA:** Official portal highlights JetsonThor and OrinNanoSuper. Existing catalog includes Thor and OrinNano. No new developer-kit pinout confirmed since October30; do not treat OrinNano2 third-party support mention as a new NVIDIA physical kit map. Official platform/product landing page. [Source 1](https://developer.nvidia.com/embedded-computing)
- **HardKernel:** ODROID-M1SLite2GB exists as a current shop listing, but page mixes Lite2GB/32GB configuration with older generic M1S specifications. Linked connector page is genericM1S and returns403; cannot validate Lite-specific physical pinmap. Not added with reused older map. Known watchlist follow-up; explicit revision/documentation gap. [Source 1](https://www.hardkernel.com/shop/odroid-m1s-lite-2gb/) · [Source 2](https://wiki.odroid.com/internal/odroid-m1s/hardware/expansion_connectors)
- **Sipeed:** Two strong older omissions: original TangNano and TangNano9K physical maps, schematics, plus9K board datasheet. Saved in the research notes. Primer15K English page header2026-10-30 is documentation timestamp, body has outdated2024 releaseTBD and pinoutTBD; no new-release claim or complete map. Wider Tang family still has many older gaps. Targeted physical-map review; not all current FPGA product SKUs. [Source 1](https://wiki.sipeed.com/hardware/en/tang/Tang-Nano/Nano.html) · [Source 2](https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-9K/Nano-9K.html) · [Source 3](https://wiki.sipeed.com/hardware/en/tang/tang-primer-15k/primer-15k.html)
- **Olimex:** News through October26 includes C6 software tutorial and October19 level-shifter products; no post-October30 board release verified. New-products forum latest listed October26. Manufacturer/news/index; no full FPGA hardware catalog pass. [Source 1](https://www.olimex.com/) · [Source 2](https://www.olimex.com/forum/)
- **Antmicro:** October27 PCIe expansion for JetsonOrinBaseboard missing. Schematic1.0.0 retrieved, Apache2.0 repository verified. Physical pinout not found. November2 blog entries are software. Supporting candidate in the research notes. Known new board follow-up; no full openhardware portal audit. [Source 1](https://antmicro.com/blog/) · [Source 2](https://antmicro.com/blog/2026/10/PCIe-Switch-expansion-for-Antmicro-Baseboard-for-NVIDIA-Jetson-Orin) · [Source 3](https://openhardware.antmicro.com/boards/jetson-orin-baseboard-pcie-switch-expansion/?tab=features)
- **Other FPGA vendors / close SBC vendors:** No independently validated additional post-October30 physical-map candidates collected within this pass. TerasicAtumA3Nano already present. Do not report a complete scan of every FPGA/SBC vendor. Unfinished breadth; remaining work explicitly retained.

## Provenance, electrical review and rights

Physical board pinouts, connector-purpose labels, port-location photographs, schematics, assembly drawings and component datasheets remain distinct reference types. Only attachments explicitly classified as physical pinout images enter the count above. Supporting diagrams do not establish complete all-connector coverage. No new independent electrical tests or validated power measurements are claimed.

Original creators and manufacturer sources remain credited. Public availability and attribution alone do not grant redistribution or print rights. Each asset retains its rights/review status; the guide's code and editorial licenses do not relicense manufacturer artwork. Source access failures, mismatched models/revisions, incomplete manuals and unresolved rights remain documentation gaps.

## Brand source-discovery register

| Brand label | Existing records | Added/updated records | Result |
|---|---:|---:|---|
| 01space | 4 | 0 | source discovery only follow up needed |
| 0xCB | 2 | 0 | source discovery only follow up needed |
| 1BitSquared | 2 | 0 | source discovery only follow up needed |
| 2231puppy | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| 42. Keebs | 1 | 0 | source discovery only follow up needed |
| 8086 Consultancy | 2 | 0 | source discovery only follow up needed |
| ATMegaZero | 1 | 0 | source discovery only follow up needed |
| Adafruit | 186 | 1 | reviewed additions or updates |
| Ai-Thinker | 4 | 0 | source discovery only follow up needed |
| Antmicro | 1 | 1 | reviewed additions or updates |
| Arduino | 94 | 0 | selected documentation reviewed |
| Autosport Labs | 1 | 0 | source discovery only follow up needed |
| Banana Pi | 81 | 0 | selected documentation reviewed; seed source access or identity gap |
| BeagleBoard.org | 8 | 0 | source discovery only follow up needed |
| Benjamin Shockley | 1 | 0 | source discovery only follow up needed |
| Boardsource | 1 | 0 | source discovery only follow up needed |
| Bradán Lane STUDIO | 1 | 0 | source discovery only follow up needed |
| BrainBoardz Inc. | 1 | 0 | source discovery only follow up needed |
| Breadstick Innovations | 1 | 0 | source discovery only follow up needed |
| BrisbaneSilicon | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| CRCibernetica | 1 | 0 | source discovery only follow up needed |
| CircuitArt | 1 | 0 | source discovery only follow up needed |
| Community | 1 | 0 | source discovery only follow up needed |
| CrumpSpace | 1 | 0 | source discovery only follow up needed |
| Cytron Technologies | 8 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Czech maker & Make More | 1 | 0 | source discovery only follow up needed |
| DFRobot | 75 | 0 | selected documentation reviewed |
| DIY-Thermocam reference / OEM unconfirmed | 1 | 0 | source discovery only follow up needed |
| DOIT | 2 | 0 | source discovery only follow up needed |
| Dangerous Prototypes | 1 | 0 | source discovery only follow up needed |
| Datanoise | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| DatanoiseTV | 1 | 0 | source discovery only follow up needed |
| Diodes Delight | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Double Take Labs | 1 | 0 | source discovery only follow up needed |
| ELECFREAKS | 1 | 0 | source discovery only follow up needed |
| Elechouse | 27 | 1 | reviewed additions or updates |
| Elecrow | 40 | 0 | selected documentation reviewed |
| Electrolama | 1 | 0 | source discovery only follow up needed |
| Electronic Cats | 1 | 1 | reviewed additions or updates |
| Espressif | 70 | 0 | selected documentation reviewed |
| Fablab Barcelona | 1 | 0 | source discovery only follow up needed |
| Flipper Devices | 1 | 0 | source discovery only follow up needed |
| Flipper Zero | 1 | 0 | source discovery only follow up needed |
| Franzininho | 2 | 0 | source discovery only follow up needed |
| Freenove | 7 | 0 | source discovery only follow up needed |
| FriendlyELEC | 69 | 0 | selected documentation reviewed |
| FutureKeys | 1 | 0 | source discovery only follow up needed |
| Generic | 1 | 0 | source discovery only follow up needed |
| Generic - manufacturer unconfirmed | 8 | 0 | source discovery only follow up needed |
| Generic / manufacturer unconfirmed | 16 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Gravitech | 4 | 0 | source discovery only follow up needed |
| Guition | 27 | 0 | source discovery only follow up needed |
| HEIA-FR | 2 | 0 | source discovery only follow up needed |
| HXR.DK | 1 | 0 | source discovery only follow up needed |
| Hack Club | 2 | 0 | source discovery only follow up needed |
| HaleHound | 3 | 0 | source discovery only follow up needed |
| Hangzhou LeBan | 1 | 0 | source discovery only follow up needed |
| HardKernel | 1 | 0 | selected documentation reviewed |
| Hat Labs | 3 | 0 | source discovery only follow up needed |
| Heltec | 43 | 0 | selected documentation reviewed |
| High Code | 2 | 0 | source discovery only follow up needed |
| Inland | 67 | 0 | selected documentation reviewed |
| Invector Labs | 10 | 0 | source discovery only follow up needed |
| JPConstantineau | 5 | 0 | source discovery only follow up needed |
| Joy-IT | 41 | 0 | source discovery only follow up needed |
| Kevin Matocha | 1 | 0 | source discovery only follow up needed |
| LILYGO | 151 | 0 | selected documentation reviewed |
| LOLIN | 3 | 0 | source discovery only follow up needed |
| LattePanda | 9 | 0 | selected documentation reviewed |
| Luatos | 2 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Luckfox | 18 | 0 | source discovery only follow up needed |
| M5Stack | 665 | 0 | selected documentation reviewed |
| Maker Go | 2 | 0 | source discovery only follow up needed |
| MakerM0 | 1 | 0 | source discovery only follow up needed |
| Makerfabs | 1 | 0 | source discovery only follow up needed |
| Maple | 1 | 0 | source discovery only follow up needed |
| Melopero | 1 | 0 | source discovery only follow up needed |
| MicroDev | 2 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Microchip | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Milk-V | 6 | 1 | reviewed additions or updates; seed source access or identity gap |
| Mixly | 2 | 0 | source discovery only follow up needed |
| Morpheans | 1 | 0 | source discovery only follow up needed |
| Muselab | 2 | 0 | source discovery only follow up needed |
| Music Thing Modular | 1 | 0 | source discovery only follow up needed |
| NHB Systems | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| NVIDIA | 8 | 0 | selected documentation reviewed |
| Newsan | 1 | 0 | source discovery only follow up needed |
| NodeMCU | 3 | 0 | selected documentation reviewed |
| Nologo | 51 | 0 | source discovery only follow up needed |
| OTAKE Takayoshi | 1 | 0 | source discovery only follow up needed |
| Oak Development Technologies | 4 | 0 | source discovery only follow up needed |
| Olimex | 5 | 0 | selected documentation reviewed |
| OpenSourceSDRLab | 3 | 0 | source discovery only follow up needed |
| Orange Pi | 40 | 0 | selected documentation reviewed |
| Oxocard | 4 | 0 | source discovery only follow up needed |
| PCBCupid | 1 | 0 | source discovery only follow up needed |
| PJRC | 12 | 0 | source discovery only follow up needed |
| PROVES Kit | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Pajenicko s.r.o. | 1 | 0 | source discovery only follow up needed |
| PandaByte | 1 | 0 | source discovery only follow up needed |
| Pcbcupid | 5 | 0 | source discovery only follow up needed |
| Pimoroni | 31 | 0 | selected documentation reviewed |
| Pololu | 6 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Potekku | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Prokyber | 1 | 0 | source discovery only follow up needed |
| QDtech | 2 | 0 | source discovery only follow up needed |
| Quadbit | 1 | 0 | source discovery only follow up needed |
| RAKwireless | 51 | 0 | selected documentation reviewed |
| REYAX | 1 | 0 | source discovery only follow up needed |
| RF.Guru | 1 | 0 | source discovery only follow up needed |
| Radomir Dopieralski | 2 | 0 | source discovery only follow up needed |
| Radxa | 12 | 0 | selected documentation reviewed |
| Raspberry Pi | 23 | 0 | selected documentation reviewed; seed source access or identity gap |
| Renesas | 1 | 0 | source discovery only follow up needed |
| RockBase IoT / NMTech | 2 | 0 | source discovery only follow up needed |
| STMicroelectronics | 42 | 0 | source discovery only follow up needed; seed source access or identity gap |
| SecuringHardware.com | 1 | 0 | source discovery only follow up needed |
| Seeed Studio | 538 | 2 | reviewed additions or updates |
| Silicognition LLC | 1 | 0 | source discovery only follow up needed |
| Silicon Labs | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Sipeed | 6 | 2 | reviewed additions or updates |
| Smart Bee Designs | 3 | 0 | source discovery only follow up needed |
| Solder Party | 5 | 0 | source discovery only follow up needed |
| Soldered | 1 | 0 | source discovery only follow up needed |
| SparkFun | 55 | 2 | reviewed additions or updates |
| SplitKB | 1 | 0 | source discovery only follow up needed |
| Spotpear | 2 | 0 | source discovery only follow up needed |
| Spotpear (manufacturer unconfirmed) | 3 | 0 | source discovery only follow up needed |
| Squarofumi | 1 | 0 | source discovery only follow up needed |
| Steiert Solutions | 1 | 0 | source discovery only follow up needed |
| StudioLab | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Sunrom (seller; OEM unconfirmed) | 5 | 0 | source discovery only follow up needed |
| Sunton | 40 | 0 | source discovery only follow up needed |
| Targett | 2 | 0 | source discovery only follow up needed; seed source access or identity gap |
| TechOverflow | 2 | 0 | source discovery only follow up needed |
| Teenage Engineering | 1 | 0 | source discovery only follow up needed |
| Terasic | 1 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Texas Instruments | 2 | 0 | source discovery only follow up needed; seed source access or identity gap |
| ThingPulse | 1 | 0 | source discovery only follow up needed |
| TinyCircuits | 2 | 0 | source discovery only follow up needed |
| Turkish Technology Team Foundation | 6 | 0 | source discovery only follow up needed |
| Unattributed chip reference | 2 | 0 | source discovery only follow up needed; seed source access or identity gap |
| Unexpected Maker | 26 | 3 | reviewed additions or updates |
| Unknown | 1 | 0 | source discovery only follow up needed |
| VCC-GND Studio | 4 | 0 | source discovery only follow up needed |
| VIDI | 1 | 0 | source discovery only follow up needed |
| WEEKIN | 1 | 0 | source discovery only follow up needed |
| WIZnet | 9 | 0 | selected documentation reviewed; seed source access or identity gap |
| Waveshare | 388 | 1 | reviewed additions or updates |
| WeAct Studio | 49 | 0 | source discovery only follow up needed |
| Wee Noise Makers | 3 | 0 | source discovery only follow up needed |
| Wemos | 13 | 0 | source discovery only follow up needed |
| WiPhone | 1 | 0 | source discovery only follow up needed |
| Wireless-Tag | 5 | 2 | reviewed additions or updates |
| WisdPi | 2 | 0 | source discovery only follow up needed |
| Xteink | 1 | 0 | source discovery only follow up needed |
| Yoto Limited | 2 | 0 | source discovery only follow up needed |
| Zach Richard | 1 | 0 | source discovery only follow up needed |
| cezerio | 2 | 0 | source discovery only follow up needed; seed source access or identity gap |
| dronecz | 1 | 0 | source discovery only follow up needed |
| micro-bit Educational Foundation | 2 | 0 | source discovery only follow up needed |
| nullbits | 1 | 0 | source discovery only follow up needed |
| senseBox | 3 | 0 | source discovery only follow up needed |

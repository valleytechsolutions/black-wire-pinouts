# Power reference review / 2026.09.7

The 13 existing power profiles and 22 published operating observations were rechecked against manufacturer documentation on 2026-09-26. This is a documentation review, not independent electrical testing. [Citation ledger](../catalog/power-review-2026.09.7.json).

- Pico / Pico 2: VSYS limits remain separate from USB and GPIO. Pico's published current scenario includes an expansion board and is not a maximum supply requirement.
- Arduino UNO R3: the recommended 7–12 V external range remains distinct from absolute limits and the regulated output pins.
- Raspberry Pi computers: recommended supply capacity remains distinct from typical bare-board consumption. The dead hardware-table URL was replaced with a pinned official documentation revision. Differences between the 5 V plug description, 5.1 V supply description and Zero 2 W supply tables are disclosed. No input tolerance is inferred.
- Teensy: AVR and 4.x profiles remain separate; VIN/USB isolation notes are visible. GPIO output ratings are not treated as board consumption.
- ESP32-C5-DevKitC-1: the profile applies to v1.2. USB, 5 V and 3.3 V supply methods remain distinct. J5 measures the module, not the whole attached system.
- Heltec Wireless Paper: Table 2.2 values were visually checked in the original PDF. Its 3.7 V and 5 V operating figures do not establish an input acceptance range or guaranteed maximum current.

The app now shows board-specific notes and a direct source for each operating observation. Source digests identify fetched document bytes where available; changing HTML may have a different digest later. Missing ratings remain null. Other boards still need sourced power profiles.

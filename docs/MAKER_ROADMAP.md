# A reference makers can trust at the workbench

Black Wire is expanding from development boards into pin-connected displays,
sensors, controls and modules. First Edition / 2026 remains the editorial edition.
The first maker intake is a documented starting point, not a claim to include
every product ever manufactured. Record counts include families and unresolved
variants; they must never be presented as complete physical pinouts.

## Available in the first maker update

Searchable records connect primary manufacturer documents and the existing
module collection. Search accepts controller names, manufacturer names, function,
recorded interface, display size and resolution. Exact numeric identities remain
distinct: BME280 is not BMP280, and 1.3 inches is not 13 inches. Nearby spellings
are suggestions that the reader must choose. Blank electrical fields never mean
that a part is compatible with every host.

## Coverage sequence

1. **Display identification.** Separate controller, resolution, diagonal, color
   capability, connector, interface and PCB revision. Expand OLED, character and
   graphic LCD, TFT, memory LCD, e-paper, seven-segment and matrix displays. Keep
   bare panels and carrier boards distinct. Include discontinued variants when
   documents exist; record unknown availability without guessing.
2. **Sensors and controls.** Add temperature/humidity/pressure, air quality,
   distance, optical, force/load, magnetic and inertial sensing, then buttons,
   encoders, touch inputs and keypads. Separate bare sensing elements from
   breakouts with regulators, pull-ups or comparators.
3. **Supporting modules.** Expand ADC/DAC, GPIO expanders, multiplexers, level
   translation, RTC, storage, audio, radio, motor/servo drivers, power and charging.
   Record both input and output connector roles; an accessory name is insufficient.
4. **Generic variants.** Photograph/identify both sides and all markings for each
   actual variant, preserve seller/source evidence, and compare circuit and pin
   order. A clone joins an exact identity only when the evidence supports it.
   Do not assign a universal pinout to a marketplace search phrase.

The concrete manufacturer/category queue and failed retrievals are in
[the research backlog](../catalog/maker-research-backlog.json).

## What makes this a must-have resource

| Reader need | Deliverable | Evidence required before calling it complete |
|---|---|---|
| Identify the part in a drawer | Marking/connector search, side-by-side variant comparison | Exact PCB identity and documented differences |
| Wire it correctly | Original readable physical diagrams with pin 1 and viewing side | Every displayed assignment tied to source and independently reviewed |
| Check host compatibility | Separate supply, logic, input tolerance, pull-ups and current fields | Exact board circuit/revision; unknowns remain explicit |
| Make it work in software | Driver selection, addresses, SPI mode, initialization and minimal example | Library/framework version and reproducible hardware test |
| Diagnose failure | Known pitfalls and measured troubleshooting steps | Observed setup, revision, symptoms and confirmed fix |
| Plan a project | Comparison, connector/pin allocation and power budget | Conflicts visible; no assumed interchangeable pin/function mapping |
| Keep a dependable reference | Offline app, searchable web guide and readable physical book | Shared record IDs, edition manifest, errata and tested builds |

Next implementation priorities are exact display variant comparison, structured
electrical facts, then original diagrams and tested connection examples. A
compatibility recommender must wait for sufficient electrical evidence.

## Record and publication contract

Each record has a stable ID, identity kind, manufacturer, model/revision, source
URL and checked date. New documentation captures a SHA-256 fingerprint. Fields
must retain a source locator; unresolved discrepancies stay in notes. A label
list has no physical order and is never counted as a completed pinout.

For original diagrams, add connector geometry and viewing side, position, signal,
direction, alternate functions, voltage restrictions and source evidence. Technical
review, artwork rights, layout review and physical proof are separate gates.
Source artwork is not relicensed by the compilation license. New maker metadata
does not republish downloaded manufacturer illustrations.

Contributions should include an exact model/revision, public source link, the
affected record ID, and a precise correction or missing field. Do not submit
credentials, private purchase details or artwork without its rights basis. Follow
[CONTRIBUTING.md](../CONTRIBUTING.md). Review contributions before release; do not
automatically promote scraped pages to verified wiring instructions.

Track coverage using separate numbers for discovered records, identified products,
source documents, physical maps, technical approvals, tested examples and print
approvals. Publish corrections as new immutable digital snapshots and app
versions; freeze the physical First Edition only after its reviews and proof.

<p align="center">
  <img src="docs/brand/black-wire.png" width="110" alt="Black Wire logo"> &nbsp;&nbsp;
  <img src="docs/brand/valleytech.png" width="80" alt="Valleytech Solutions logo">
</p>
<h1 align="center">Black Wire<br>Technical Reference Guide</h1>
<p align="center"><strong>Know your board. Make the connection.</strong><br>A Valleytech Solutions project, made for the workbench.</p>
<p align="center">Makers · Educators · Students · Hobbyists · Engineers</p>

<p align="center"><a href="https://github.com/valleytechsolutions/black-wire-pinouts/releases">Download the collection</a> · <a href="BROWSE.md">Browse boards</a> · <a href="catalog/attributions.csv">Source credits</a> · <a href="https://github.com/valleytechsolutions/black-wire-desktop/releases">Download the desktop app</a> · <a href="CONTRIBUTING.md">Contribute a reference</a></p>

## Maker expansion / September 2026

[Browse displays, sensors and modules](MAKERS.md) or [search the parts desk](https://valleytech-black-wire-guide.pages.dev/?tab=makers). The new intake has **457 records**: **173 manufacturer documentation records**, **268 existing collection references** and **16 generic families** needing identification. These are source records, not 457 newly completed pinouts. [Coverage and product roadmap](docs/MAKER_ROADMAP.md).

## A reference shelf for your next project

Find the picture that tells you **which physical pin does what**. This collection brings together original board pinouts, connector labels, GPIO references and supporting documents, organized by manufacturer, processor and exact board identity. The companion desktop app makes the same collection searchable offline.

| First Edition · snapshot 2026.09.3 | Count |
|---|---:|
| Reviewed physical board pinout images | **1,365** |
| Searchable reference entries | **3,003** |
| Catalog records with files | **1,688** |
| Manufacturers and source groups | **60** |
| Unique original media files, including vector companions | **2,953** |

Records include shared references, variants, devices and unreviewed source products. These counts are **not a census of unique development boards**. Coverage is growing; it is not complete.

![The Black Wire desktop library browsing this collection](docs/screenshots/library.png)

## Devices & IoT

**[Browse 310 device records](DEVICES.md)** or use the new **[Devices & IoT tab](https://valleytech-black-wire-guide.pages.dev/?tab=devices)**. Find T-Embed, T-Beam, T-Deck, Cardputer, Flipper, wearables, LoRa nodes, smart displays and controllers by category, manufacturer and MCU. Missing sheets and in-development documentation are explicitly labeled.

![Devices and IoT browsing in Black Wire](docs/screenshots/devices-iot.png)

This update adds **15 original images, including 7 pinout/connector sheets**, and six newly populated device records. [First Edition policy and update details](EDITION.md).

## Find your board

**[Search the complete current collection in your browser](https://valleytechsolutions.tech/pages/bwm-technical-reference-guide)** on the Valleytech store. No download or installation is needed. The [full-screen guide](https://valleytech-black-wire-guide.pages.dev/) includes manufacturer/processor filters, pinout viewing and power tools.

Start at **[Browse manufacturers and boards](BROWSE.md)**. Each board page includes a preview, original-resolution downloads, model/revision notes, and source credits. ESP32-C5, C6, S3 and other variants remain separate; RP2040, RP2350, CYD, Arduino, Teensy, SBCs and devices with GPIO have their own records.

| What you need | Where to look |
|---|---|
| Physical board pins | Board pages marked **pinout image** |
| Connector or GPIO labels | **GPIO reference image** and **board labeling image** |
| Manuals, schematics or supporting material | **Original PDF** / **source reference**; check the review label |
| Full-resolution originals | `library/media/`; linked from every board page |
| Provenance, hashes and rights | [`catalog/attributions.csv`](catalog/attributions.csv) and [`library/catalog.json`](library/catalog.json) |
| Fast offline search and power tools | [Black Wire desktop](https://github.com/valleytechsolutions/black-wire-desktop) |

Original files are stored once by content hash; board pages provide the human-friendly organization. Shared images remain linked to all applicable records. Thumbnails and large-image previews are convenience derivatives, not replacements for the originals.

## Use it offline

Download a versioned ZIP from this repository's **[collection releases](https://github.com/valleytechsolutions/black-wire-pinouts/releases)**. Each release includes the full reference collection, board indexes, source credits, license/rights notices and a SHA-256 checksum. Extract the whole ZIP and begin with `README.md` and `BROWSE.md`. The files work on **Windows, Linux and macOS** with an image/PDF viewer and a Markdown reader; no installer is needed for the collection.

The guide remains **First Edition / 2026**. The latest collection snapshot is **[2026.09.2 — Devices & IoT](https://github.com/valleytechsolutions/black-wire-pinouts/releases/tag/v2026.09.2)**; [2026.09.1](https://github.com/valleytechsolutions/black-wire-pinouts/releases/tag/v2026.09.1) remains available unchanged. Collection snapshots and app versions are independent of the future annual book editions; see [EDITION.md](EDITION.md). The [desktop repository](https://github.com/valleytechsolutions/black-wire-desktop/releases) provides application installers and states which operating systems actually have downloads.

You can also clone the current repository (about **1.8 GB** of reference data). Keep the folder structure intact. Local Markdown viewers can follow the board pages; the desktop app provides the full searchable image/PDF interface. See [release and checksum instructions](RELEASES.md).

```sh
git clone https://github.com/valleytechsolutions/black-wire-pinouts.git
```

## Attribution, quality and publication

**Original guide/editorial and compilation contributions are [CC BY 4.0](LICENSING.md): reuse, adapt and share, including commercially, with attribution to Kal / Valleytech Solutions, a license link and a note of changes.** See [suggested attribution](NOTICE.md) and [privacy](PRIVACY.md).

Read [ATTRIBUTION.md](ATTRIBUTION.md) and [RIGHTS.md](RIGHTS.md). Every image retains its recorded source, rights status and SHA-256. **Attribution is not permission to relicense or commercially print an image.** Many source licenses have not yet been established; any book edition needs a rights review for those images. No collection-wide open license is claimed for manufacturer artwork.

“Reviewed” means categorized against its source, not electrically bench-verified. Some references have unidentified revisions, partial maps or low resolution. Chip-package diagrams are separately labeled and excluded from the physical-board pinout count. One unreviewed reSpeaker Lite source PNG is truncated; its original is retained with a preview-error note.

## Help build the field guide

Send a board reference, correction, revision clarification, a better original or verified license information through [the contribution template](CONTRIBUTING.md). The long-term direction is an offline reference app, a browsable wiki and annual book editions; only the current collection and workshop app are available today.

---
Created and curated by **—your pal kal** · [@valleytechsolutions on YouTube](https://www.youtube.com/@valleytechsolutions)

Black Wire and Valleytech logos belong to their creator. Manufacturer names and trademarks identify the referenced hardware; they do not imply endorsement.

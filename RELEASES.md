# Pinout collection releases

[Download collection editions](https://github.com/valleytechsolutions/black-wire-pinouts/releases) · [Desktop application downloads](https://github.com/valleytechsolutions/black-wire-desktop/releases)

These are two independent release streams. A **collection release** contains images, PDFs, indexes and attribution records. A **desktop app release** contains an application for the operating systems listed in that release. A collection ZIP is not a desktop installer.

## September 2026 snapshot — 2026.09.1

The first downloadable collection edition includes 2,988 reference entries, 1,358 reviewed physical board pinout images, 1,682 populated catalog records, 59 manufacturer/source groups and 2,938 unique original media files. Counts include shared references and unreviewed source products; this is not a complete census of boards.

Download `Black-Wire-Pinouts-2026.09.1.zip` and `SHA256SUMS.txt` from the [same release](https://github.com/valleytechsolutions/black-wire-pinouts/releases/tag/v2026.09.1). Extract the full ZIP on Windows, Linux or macOS and open `README.md` or `BROWSE.md` in a Markdown viewer. Follow board-page links to the original diagrams and PDFs. No executable or installer is included.

## Verify the ZIP

Windows PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '.\Black-Wire-Pinouts-2026.09.1.zip'
```

Compare that hash with the matching filename in `SHA256SUMS.txt`. On Linux, run `sha256sum -c SHA256SUMS.txt`; on macOS, run `shasum -a 256 -c SHA256SUMS.txt` from the folder containing both downloads. A checksum detects a changed download; it is not a publisher signature or an electrical verification of the diagrams.

## Rights travel with the collection

Preserve `LICENSE`, `LICENSING.md`, `NOTICE.md`, `RIGHTS.md`, `ATTRIBUTION.md` and the per-reference ledger under `catalog/`. Our original editorial and compilation contributions use CC BY 4.0 with attribution to Kal / Valleytech Solutions. Manufacturer/community artwork retains its own rights and credits. Unknown source permissions remain unknown; the collection license does not relicense those images.

This snapshot includes partial references, unidentified revisions and unreviewed source material. One unreviewed reSpeaker Lite source PNG is truncated and retained with its recorded preview-error note. “Reviewed” is a categorization status, not a claim of independent electrical testing.

## Preparing future editions

Use an edition tag such as `vYYYY.MM.N` and export its exact reviewed Git commit with `git archive`. Do not ZIP the working directory: it may contain `.git`, private local files or untracked research material. Preserve original reference bytes and use a single clearly named top-level folder in the archive.

Verify ZIP integrity, required notices, all library-manifest paths and content hashes for the original media. Generate SHA-256 from the final ZIP, upload to a draft release, compare GitHub's uploaded digest and byte size, then publish the edition. Keep checks and logs outside the tracked repository. Do not replace the contents of a published edition; issue a new edition for corrections.

# Privacy and public contributions

The desktop app stores bookmarks and personal measurement records on the user's device. The browser edition stores them in that browser's local storage. Black Wire has no account system, telemetry, analytics or cloud backup service. Exported workbench backups can contain personal notes; do not commit them or attach them to public issues.

The browser edition requests application and reference files from its hosting provider. GitHub, the store, hosting providers and external source/YouTube websites have their own privacy policies and may receive normal connection information such as IP addresses. Local storage is not encrypted storage. Other scripts on the same hosting origin may be able to access it.

## Keep out of public repositories and releases

- Passwords, tokens, cookies, environment files, signing certificates and private keys.
- Personal workbench backups, private test records, debug/task logs and user profile folders.
- Screenshots showing account details, private browser tabs, notifications or personal records.
- Private emails, home addresses and workstation paths in commits, documents or metadata.

Use a GitHub-provided no-reply commit email. The intended public creator identity is **Kal / Valleytech Solutions**, with the public YouTube handle **@valleytechsolutions**. Preserve third-party public source credits; do not replace the original creators' names with the curator's name.

Before publishing, inspect the staged file list and release contents, scan the working tree and full Git history for secrets (for example with Gitleaks), and review image/document metadata. Keep scan reports outside tracked files. Automated scans reduce risk; they cannot guarantee that every form of sensitive information is detected.

If a secret is discovered, revoke or rotate it first. Deleting the current file does not remove earlier commits or copies already downloaded. Report security-sensitive details privately through GitHub's security reporting feature if enabled; do not post credentials in a public issue.

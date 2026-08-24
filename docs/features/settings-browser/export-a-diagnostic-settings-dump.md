# Export a diagnostic settings dump

Export a sanitized text dump of the entire AetherSDR settings store, with credential-shaped values redacted, to share with support or review your own configuration.

## Before you start

- AetherSDR does not need to be connected to a radio to export settings.
- The export is a diagnostic snapshot, not a backup — it cannot be re-imported to restore settings.

## Steps

1. Open the **Settings** menu and select **Settings Browser...**.
2. Click **Export Sanitized…**.
3. Choose a location and filename in the file dialog, then confirm.

The exported text file contains the full settings tree — application keys, the station section, and radio-scoped feature documents — with any credential-shaped values (passwords, tokens, API keys) redacted.

## What each control does

| Control | Behavior |
| --- | --- |
| **Filter** | Live, case-insensitive substring search over the keys and values shown in the current scope. |
| **Export Sanitized…** | Writes the secret-redacted diagnostic dump to a text file. Credential-shaped values are masked. Diagnostic output only — not a restorable backup. |

## Tips

- The export is intentionally **not** a backup. To save or restore your actual configuration, use `Profiles > Import/Export Profiles...` instead.
- Credential-shaped values are redacted at any depth, so secrets never appear in the dump — even inside nested JSON documents.

## Troubleshooting

- **Export button is disabled** — If the settings tree is still loading, click **Refresh** and wait for it to populate, then try **Export Sanitized…** again.

## Related

- [Settings Browser overview](overview.md)
- [Browse all AetherSDR settings](browse-all-aethersdr-settings.md)
- [Edit a settings value from the Settings Browser](edit-a-settings-value-from-the-settings-browser.md)

# Reset AetherSDR Settings to Factory Defaults

Use this procedure to wipe AetherSDR's locally stored settings and NR2 wisdom cache back to their factory defaults. Settings stored on the radio itself are not affected.

## Before you start

- Close any active transmissions or audio streams before resetting.
- Note any custom settings you want to restore afterward — the reset cannot be undone.

## Steps

1. Open `Help > Support...` to open the Support & Diagnostics dialog.
2. Click `Reset Settings`.
3. When the confirmation prompt appears, confirm the action.
4. Restart AetherSDR for the reset to take full effect.

## What each control does

| Control | Description |
|---|---|
| `Reset Settings` | Deletes AetherSDR's local settings and NR2 wisdom cache. Settings stored on the FLEX-8600 radio are not changed. A confirmation prompt is shown before any data is deleted. |

## Tips

- Radio-side settings (profiles, panadapter layout stored on the radio, TX band settings) remain intact after a reset. Only AetherSDR's own persisted AppSettings and cached DSP data are removed.
- If you are resetting to resolve a reproducible problem, consider capturing a log first. See [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md).

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)
- [Support & Diagnostics overview](overview.md)

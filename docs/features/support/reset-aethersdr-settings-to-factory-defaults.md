# Reset AetherSDR Settings to Factory Defaults

Use this procedure to wipe AetherSDR's locally stored settings and NR2 wisdom cache back to their factory defaults. Settings stored on the radio itself are not affected.

## Before you start

- Close any active transmissions or audio streams before resetting.
- Note any custom settings you want to restore afterward — the reset cannot be undone.

## Steps

1. Open `Help > Reset Settings`.
2. When the confirmation prompt appears, confirm the action.
3. Restart AetherSDR for the reset to take full effect.

## What each control does

| Control | Description | Notes |
|---|---|---|
| Category checkboxes | Enable or disable logging per category. Each category has its own checkbox. | |
| Enable All | Turns on every logging category. | |
| Disable All | Turns off every logging category. | |
| Log path label | Shows the current log file path. | |
| Log viewer | Scrollable view of the most recent log text. | |
| Refresh | Reloads the log file. | |
| Clear Log | Truncates the current log file. | |
| Open Log Folder | Opens the log directory in the OS file browser. | |
| Close | Closes the dialog. | |
| Instructions (report-an-issue how-to) | Rich-text block pointing the user to Help > File an Issue for bug reporting once the relevant logging categories have been enabled and the problem reproduced. | New in v26.8.4: the 'Reset Settings' and 'File an Issue' buttons were removed from this dialog (they now live directly on the Help menu). |

## Indicators

| Indicator | Description |
|---|---|
| Log file size | Current size of the active log file. |

## What the reset removes

The reset removes the following files:

- The main settings database.
- SQLite write-ahead log and shared-memory sidecar files (`-wal`, `-shm`).
- The pre-SQLite XML settings snapshot, including `.bak`, `.tmp`, and `.corrupt` siblings.
- The NR2 wisdom cache file.
- Rolling automatic backups (`*-auto.db`, `*-postmigration.db`) in the backups directory.
- Quarantined corrupt settings stores.
- On macOS, the `com.aethersdr.AetherSDR.plist` preferences file.

A backup of the current settings is written to the AetherSDR backups directory before anything is removed, so a reset can be recovered. The pre-reset backup is written to a location the purge does not touch.

## Tips

- Radio-side settings (profiles, panadapter layout stored on the radio, TX band settings) remain intact after a reset. Only AetherSDR's own persisted AppSettings and cached DSP data are removed.
- If you are resetting to resolve a reproducible problem, consider capturing a log first. See [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md).
- The AI-assisted bug report includes system information (AetherSDR version, Qt version, OS, and radio type) and references the project's context at https://raw.githubusercontent.com/aethersdr/AetherSDR/main/CLAUDE.md.

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)
- [Support & Diagnostics overview](overview.md)
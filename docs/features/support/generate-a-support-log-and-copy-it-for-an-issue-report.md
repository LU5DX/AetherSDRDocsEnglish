# Generate a support log and copy it for an issue report

Generate a support log with the right logging categories enabled, then copy or attach it to a GitHub issue report so the AetherSDR developers can diagnose your problem.

## Before you start

- You have reproduced the issue or know the steps to reproduce it.
- You know which subsystem is involved (e.g., audio, radio connection, CW, DAX) to select the relevant logging category.

## Steps

1. Open Support & Diagnostics via `Help > Support...`.
2. In the Diagnostic Logging group, check the box next to the relevant category (e.g., the subsystem related to your problem). If unsure, click **Enable All** to turn on every category.
3. Click **Close**.
4. **Restart AetherSDR** — logging changes only take effect on the next launch.
5. Reproduce the problem.
6. Open Support & Diagnostics again via `Help > Support...`.
7. Review the log viewer. Click **Refresh** to reload the log file and ensure it contains the latest entries.
8. Click **Open Log Folder** to reveal the log file in your operating system's file browser.
9. Copy or drag the log file into your issue report:
   - From the file browser, copy the `.log` file.
   - Go to `Help > File an Issue...` to open the GitHub issue form.
   - Paste the log contents or drag the log file into the form.

## What each control does

| Control | Behavior |
| --- | --- |
| Category checkboxes | Enable or disable logging per category. Each row corresponds to one logging category; hover to see its description. |
| **Enable All** | Turns on every logging category. |
| **Disable All** | Turns off every logging category. |
| Log path label | Shows the full path of the active log file. |
| Log file size | Displays the current size of the active log file. |
| Log viewer | Scrollable, read-only view of the most recent log text (up to 2000 lines or 200 KB). |
| **Refresh** | Reloads the log file contents and scrolls to the bottom. |
| **Clear Log** | Truncates the current log file and refreshes the viewer. |
| **Open Log Folder** | Opens the log directory in the OS file browser. |
| **Close** | Closes the dialog. |

## Tips

- Clearing the log before reproducing a bug produces a smaller, focused log file that is easier for the developers to review — see [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md).
- When you report an issue via `Help > File an Issue...`, AetherSDR automatically collects radio info (model, serial, firmware, protocol version, callsign, IP) and bundles it with the log if a radio is connected.
- The instructions block inside the Support dialog itself mirrors these steps: enable relevant logging, restart, reproduce, then use `Help > File an Issue...`.

## Troubleshooting

- **Log file is empty** — Logging may be disabled for the relevant category. Open Support & Diagnostics, check the relevant category box (or click **Enable All**), click **Close**, and restart AetherSDR before reproducing the issue.
- **Log viewer shows "(unable to open log file)"** — The log file may be locked by another process or missing. Click **Open Log Folder** to inspect whether the log file exists; if not, restart AetherSDR to recreate it.
- **Log contains too little information** — Enable more categories via **Enable All**, restart, and reproduce the issue again. The log only captures events from categories that were enabled at the time the problem occurred.

## Related

- [Support & Diagnostics overview](overview.md)
- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)

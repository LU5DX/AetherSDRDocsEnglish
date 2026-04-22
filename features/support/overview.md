# Support & Diagnostics Overview

The Support & Diagnostics dialog gives you a single place to control what AetherSDR logs, inspect the live log, and submit a bug report. Open it any time from `Help > Support...` — no radio connection is required.

## How it works

The dialog is divided into three functional areas: logging category controls, a live log viewer, and action buttons for file management and bug reporting.

**Diagnostic Logging group**

Each logging category appears as a checkbox. Checking a category enables log output for that subsystem; unchecking it silences it. You do not need to restart AetherSDR for changes to take effect. The log file path and current file size are shown as read-only indicators directly below the group.

**Log viewer**

The log viewer is a scrollable, read-only text area showing the most recent log entries (up to 2,000 lines). It displays the contents of the active log file on disk.

**Action buttons**

The row of buttons at the bottom of the dialog drives all file and reporting actions.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Category checkboxes | Checkbox (one per category) | Enables or disables logging for that specific subsystem. |
| Enable All | Button | Turns on every logging category at once. |
| Disable All | Button | Turns off every logging category at once. |
| Log path label | Indicator | Shows the full path to the current log file. |
| Log file size | Indicator | Shows the current size of the active log file. |
| Log viewer | Scrollable text area | Displays the most recent log text from the log file (up to 2,000 lines). |
| Refresh | Button | Reloads the log file into the viewer. |
| Clear Log | Button | Truncates (empties) the current log file. |
| Open Log Folder | Button | Opens the directory containing the log file in your operating system's file browser. |
| Reset Settings | Button | Resets AetherSDR's local settings and NR2 wisdom cache to defaults, after confirmation. Radio settings stored on the radio are not affected. |
| File an Issue | Button | Launches the AI-assisted bug report flow: creates a support bundle, copies a pre-filled diagnostic prompt to your clipboard, and guides you through submitting a GitHub issue. |
| Close | Button | Closes the dialog. |

## Tips

- Enable only the categories relevant to the problem you are reproducing. A smaller log is easier to read and share.
- Click Clear Log before you reproduce a bug so the log contains only the relevant event sequence.
- The support bundle created by File an Issue includes your logs and settings. Attach it to the GitHub issue by dragging it from the folder that opens automatically.
- Reset Settings removes local AetherSDR preferences and the NR2 wisdom cache. It does not alter any settings stored on the FLEX-8600 itself.

## Related

- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [View the live log without leaving the app](view-the-live-log-without-leaving-the-app.md)
- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)
- [Reset AetherSDR settings to factory defaults](reset-aethersdr-settings-to-factory-defaults.md)

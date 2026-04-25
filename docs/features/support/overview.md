# Support & Diagnostics overview

The Support & Diagnostics dialog gives you a single place to control diagnostic logging, inspect the live log, and file bug reports. Open it from `Help > Support...`. No radio connection is required.

## How it works

The dialog has three areas: a logging control panel at the top, a log viewer in the middle, and a row of action buttons at the bottom.

**Diagnostic Logging panel**

The top group, labeled "Diagnostic Logging", lists every available logging category as a checkbox. Each checkbox enables or disables messages from that subsystem as AetherSDR runs. Changes take effect immediately — you do not need to restart.

**Log viewer**

Below the category panel, a read-only text area displays the most recent log entries. The log file path is shown above it; the current file size is shown on the right of the same row. The viewer holds up to 2000 lines. Use Refresh to reload the file on demand.

**Action buttons**

The button row at the bottom provides the following controls:

| Button | What it does |
|---|---|
| Enable All | Turns on every logging category at once. |
| Disable All | Turns off every logging category at once. |
| Refresh | Reloads the log file into the viewer. |
| Clear Log | Truncates the current log file. This cannot be undone. |
| Open Log Folder | Opens the log directory in your OS file browser so you can copy or attach multiple files. |
| Reset Settings | Resets AetherSDR settings to defaults after asking for confirmation. Radio settings stored on the radio are not affected. |
| File an Issue | Launches the AI-assisted bug report flow. Copies a diagnostic prompt (with your AetherSDR version, Qt version, OS, and connected radio details) to the clipboard, then walks you through opening an AI assistant and submitting a GitHub issue. |
| Close | Closes the dialog. |

## Tips

- Enable only the categories relevant to the problem you are chasing to keep the log readable.
- Click Clear Log immediately before reproducing a bug so the log contains only the relevant sequence of events.
- If you use File an Issue, the diagnostic prompt is pre-filled with your system information. Paste it into any AI assistant listed in the follow-up dialog, describe what went wrong, then use the AI's output as your GitHub issue body.
- The log folder opened by Open Log Folder is the same folder where support bundles are saved when you use File an Issue, so you can drag both the log and the bundle into a GitHub issue in one step.

## Related

- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [View the live log without leaving the app](view-the-live-log-without-leaving-the-app.md)
- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)
- [Reset AetherSDR settings to factory defaults](reset-aethersdr-settings-to-factory-defaults.md)

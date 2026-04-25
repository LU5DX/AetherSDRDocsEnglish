# View the Live Log Without Leaving the App

The Support & Diagnostics dialog includes a scrollable log viewer that lets you read recent log output without opening a file manager or terminal. Use this when you want to watch what AetherSDR is doing in real time or quickly spot an error after something unexpected happens.

## Before you start

- No radio connection is required to open the dialog or read the log.
- If you want to capture output for a specific event, consider clearing the log first so only relevant entries appear.

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. Find the **Log viewer** panel in the center of the dialog. It shows the most recent log text as a scrollable, read-only view.
3. Scroll through the log viewer to read current entries. The log path is shown in the **Log path label** above the viewer, and the current file size appears to the right of it.
4. If new activity has occurred since you opened the dialog, click **Refresh** to reload the log file and show the latest entries.
5. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Log path label | Indicator | Shows the full path to the current log file. |
| Log file size | Indicator | Shows the current size of the active log file. |
| Log viewer | Text field | Scrollable, read-only view of the most recent log text. Displays up to 2000 lines. |
| Refresh | Button | Reloads the log file into the viewer. |
| Clear Log | Button | Truncates the current log file. |
| Open Log Folder | Button | Opens the log directory in the OS file browser. |

## Tips

- The log viewer holds a maximum of 2000 lines. If the log file is large, only the most recent content is shown. Click **Open Log Folder** to access the full file.
- To control which categories appear in the log, use the category checkboxes in the **Diagnostic Logging** section at the top of the dialog. Click **Enable All** to turn on every category, or **Disable All** to silence all of them.

## Related

- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)

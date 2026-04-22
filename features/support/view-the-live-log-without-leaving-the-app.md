# View the Live Log Without Leaving the App

The Support & Diagnostics dialog includes a built-in log viewer so you can read log output in real time without opening a terminal or external file browser. Use this when you want to watch what AetherSDR is doing while you reproduce a problem.

## Before you start

- No radio connection is required. The log viewer works whether or not AetherSDR is connected to a FLEX-8600.
- If you want to capture a clean trace of a specific problem, consider clearing the log first before reproducing the issue.

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. Find the **Log viewer** — the large dark text area in the center of the dialog. It shows the most recent log entries automatically when the dialog opens.
3. Scroll through the log viewer to read recent entries. The viewer holds up to 2000 lines.
4. If new log activity has occurred since you opened the dialog, click **Refresh** to reload the log file and show the latest entries.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Log viewer | Scrollable text area | Displays the most recent log entries. Read-only. Holds up to 2000 lines. |
| Refresh | Button | Reloads the log file from disk and updates the log viewer. |
| Log path label | Indicator | Shows the full file path of the current log file. |
| Log file size | Indicator | Shows the current size of the active log file. |
| Clear Log | Button | Truncates the log file. The log viewer will be empty after clearing. |
| Open Log Folder | Button | Opens the log directory in your OS file browser. |

## Tips

- The log viewer loads automatically each time you open the dialog. You do not need to click **Refresh** on first open.
- If entries stop appearing, click **Refresh** — the viewer does not tail the file continuously.
- To increase the detail captured in the log, enable additional categories using the category checkboxes or click **Enable All** before reproducing your issue.
- The log path label shows exactly where the file lives if you need to open it in an external editor.

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)

# Enable Verbose Logging for a Specific Subsystem

Use the Support & Diagnostics dialog to turn on logging for individual subsystems. Enabling only the categories you need keeps the log readable and makes it easier to isolate a problem.

## Before you start

- Reproduce the issue after enabling logging, not before — the log viewer shows recent entries only.
- If you want a clean capture, clear the log first before reproducing the problem.

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. In the **Diagnostic Logging** group, find the checkbox row for the subsystem you want to trace.
3. Check the checkbox next to that category. The label on the checkbox identifies the subsystem. Logging for that category activates immediately — no apply or restart needed.
4. Reproduce the condition you are diagnosing.
5. Click **Refresh** to reload the log viewer with the latest entries.
6. Review the output in the **Log viewer**.

To disable the category when you are done, uncheck the same checkbox.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Category checkboxes | Checkbox (one per subsystem) | Enables or disables logging for that specific category. Changes take effect immediately. |
| Enable All | Button | Turns on every logging category at once. |
| Disable All | Button | Turns off every logging category at once. |
| Log viewer | Scrollable text area | Displays the most recent log entries (up to 2000 lines). |
| Refresh | Button | Reloads the log file into the log viewer. |
| Log path label | Indicator | Shows the file path of the current log file. |
| Log file size | Indicator | Shows the current size of the active log file. |

## Tips

- Use **Disable All** first, then check only the one category you need. This reduces noise in the log when you are chasing a specific issue.
- Use **Enable All** when you are not sure which subsystem is involved and want the broadest possible capture.
- The log viewer holds a maximum of 2000 lines. For longer sessions, click **Open Log Folder** to access the full file on disk.

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [View the live log without leaving the app](view-the-live-log-without-leaving-the-app.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)

# Open the log folder to grab multiple files

Use this page to open the directory that contains AetherSDR's log files in your operating system's file browser, so you can copy, attach, or archive multiple log files at once.

## Before you start

- No radio connection is required.
- Know where you want to copy the files (local folder, email attachment, issue tracker upload).

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. Click `Open Log Folder`.

Your OS file browser opens directly to the log directory. From there, select and copy whichever files you need.

## Tips

- The log path label at the top of the dialog shows the full path to the current log file, so you know which directory will open before you click.
- If you want only the current log file rather than the entire folder, check the log path label and navigate there manually.
- To capture a clean log before grabbing files, use `Clear Log` to truncate the current file, reproduce the problem, then click `Open Log Folder`.
- The `Log file size` indicator near the log viewer shows the current size of the active log file.

## Log viewer controls

The log viewer displays the most recent 2000 lines from the active log file. Use these controls to manage the log display:

| Control                               | Description                                                                                                                                                    | Notes                                                                                                                                     |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Category checkboxes                   | Enable or disable logging per category. Each category appears as its own checkbox row.                                                                         |                                                                                                                                           |
| Enable All                            | Turn on every logging category.                                                                                                                                |                                                                                                                                           |
| Disable All                           | Turn off every logging category.                                                                                                                               |                                                                                                                                           |
| Log path label                        | Shows the current log file path.                                                                                                                               |                                                                                                                                           |
| Log viewer                            | Scrollable view of the most recent log text (2000 lines maximum).                                                                                              |                                                                                                                                           |
| Refresh                               | Reloads the log file.                                                                                                                                          |                                                                                                                                           |
| Clear Log                             | Truncates the current log file.                                                                                                                                |                                                                                                                                           |
| Open Log Folder                       | Opens the log directory in the OS file browser.                                                                                                                |                                                                                                                                           |
| Close                                 | Closes the dialog.                                                                                                                                             |                                                                                                                                           |
| Instructions (report-an-issue how-to) | Rich-text block pointing the user to `Help > File an Issue` for bug reporting once the relevant logging categories have been enabled and the problem reproduced. | New in v26.8.4: the `Reset Settings` and `File an Issue` buttons were removed from this dialog (they now live directly on the Help menu). |

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [View the live log without leaving the app](view-the-live-log-without-leaving-the-app.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)
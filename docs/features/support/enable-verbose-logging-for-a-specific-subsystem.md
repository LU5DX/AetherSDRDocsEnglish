# Enable verbose logging for a specific subsystem

The Support & Diagnostics dialog lets you turn on logging for individual subsystems. Enable only the categories you need to keep log output focused and easier to read when diagnosing a problem.

## Before you start

- No radio connection is required to change logging categories.
- If you want a clean log that starts at the moment you reproduce a bug, clear the log first before enabling categories.

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. In the **Diagnostic Logging** group, find the checkbox row for the subsystem you want to diagnose.
3. Check the checkbox next to that category's label to enable logging for it. Uncheck it to disable.
4. Reproduce the behavior you are investigating. Log output begins immediately when a category is enabled.
5. Click **Refresh** to reload the log file and see the latest entries in the Log viewer.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Category checkboxes | Checkbox | One row per logging category. Check to enable, uncheck to disable. Changes take effect immediately. |
| Enable All | Button | Turns on every logging category at once. |
| Disable All | Button | Turns off every logging category at once. |
| Log viewer | Text area | Scrollable view of the most recent log text. Displays up to 2000 lines. |
| Refresh | Button | Reloads the log file into the Log viewer. |
| Log path label | Indicator | Shows the full path of the current log file. |
| Log file size | Indicator | Shows the current size of the active log file. |

## Tips

- Use **Enable All** only when you are unsure which subsystem is involved. The log will be large. For a targeted investigation, enable only the relevant category checkbox.
- Use **Disable All** after you have captured what you need to stop further log growth.
- The Log viewer shows a maximum of 2000 lines. If you need the full file, click **Open Log Folder** to access it directly in your file browser.

## Related

- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [View the live log without leaving the app](view-the-live-log-without-leaving-the-app.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)

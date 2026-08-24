# View the Live Log Without Leaving the App

The Support & Diagnostics dialog includes a scrollable log viewer that lets you read recent log output without opening a file manager or terminal. Use this when you want to watch what AetherSDR is doing in real time or quickly spot an error after something unexpected happens.

## Before you start

- No radio connection is required to open the dialog or read the log.
- If you want to capture output for a specific event, consider clearing the log first so only relevant entries appear.

## Steps

1. Open the **Help** menu.
2. Select **File an Issue** only if you want to file a bug report; the dialog itself is opened via **Support...**.
3. In the **Support & Diagnostics** dialog, find the **Log viewer** panel in the center. It shows the most recent log text as a scrollable, read-only view.
4. Scroll through the log viewer to read current entries. The log path is shown in the **Log path label** above the viewer, and the current file size appears to the right of it.
5. If new activity has occurred since you opened the dialog, click **Refresh** to reload the log file and show the latest entries.
6. To manage which log categories appear, use the **Category checkboxes** in the **Diagnostic Logging** section at the top. Click **Enable All** to turn on every category, or **Disable All** to silence all of them.
7. Click **Close** when finished.

## What each control does

| Control                               | Kind          | Behavior                                                                                                                              |
|---------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Category checkboxes                   | Checkbox      | Per-category log enable/disable, one row per category.                                                                                 |
| Enable All                            | Button        | Turns on every logging category.                                                                                                      |
| Disable All                           | Button        | Turns off every logging category.                                                                                                     |
| Log path label                        | Indicator     | Shows the full path to the current log file.                                                                                          |
| Log file size                         | Indicator     | Shows the current size of the active log file.                                                                                        |
| Log viewer                            | Text field    | Scrollable, read-only view of the most recent log text. Displays up to 2000 lines.                                                    |
| Refresh                               | Button        | Reloads the log file into the viewer.                                                                                                 |
| Clear Log                             | Button        | Truncates the current log file.                                                                                                       |
| Open Log Folder                       | Button        | Opens the log directory in the OS file browser.                                                                                       |
| Close                                 | Button        | Closes the dialog.                                                                                                                    |
| Instructions (report-an-issue how-to) | Rich text     | Points the user to **Help > File an Issue** for bug reporting once the relevant logging categories have been enabled and the problem reproduced. |

> **Note (v26.8.4):** The **Reset Settings** and **File an Issue** buttons were removed from this dialog in v26.8.4. Both actions now live directly on the **Help** menu.

## File an Issue

The **File an Issue** entry on the **Help** menu starts an AI-Assisted Bug Report process.

1. Click **Help > File an Issue**.
2. In the dialog that appears, describe the problem you are experiencing.
3. Click one of the provided AI service buttons to open the AI tool with a pre-filled prompt that includes your system information and the bug description.
4. The AI will generate a complete GitHub bug report. Follow the AI's instructions to submit it at `https://github.com/aethersdr/AetherSDR/issues/new`.

## Reset Settings

The **Reset Settings** entry on the **Help** menu removes AetherSDR's app-specific settings only. It does not change settings stored on the radio.

1. Click **Help > Reset Settings**.
2. A confirmation dialog appears listing the files that will be removed. Before anything is removed, a backup of the current settings is written to the backups directory (shown in the prompt).
3. Click **Yes** to proceed. AetherSDR will close immediately after the reset so the settings files are not recreated.

## Tips

- The log viewer holds a maximum of 2000 lines. If the log file is large, only the most recent content is shown. Click **Open Log Folder** to access the full file.
- To control which categories appear in the log, use the category checkboxes in the **Diagnostic Logging** section at the top of the dialog. Click **Enable All** to turn on every category, or **Disable All** to silence all of them.
- The dialog remembers its position and size between sessions.

## Related

- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [Clear the log before reproducing a bug](clear-the-log-before-reproducing-a-bug.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
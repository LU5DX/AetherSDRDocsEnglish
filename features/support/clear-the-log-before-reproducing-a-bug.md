# Clear the Log Before Reproducing a Bug

Clearing the log before you trigger a bug ensures the resulting log file contains only the events relevant to that bug, making it easier to diagnose and report.

## Before you start

- Open AetherSDR. A radio connection is not required for this task.
- Know the steps needed to reproduce the bug so you can trigger it immediately after clearing.

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. Click `Clear Log`. This truncates the current log file immediately — there is no confirmation prompt.
3. Verify the log viewer is empty, then reproduce the bug.
4. Click `Refresh` to reload the log file and confirm the new entries are captured.
5. Click `Open Log Folder` if you need to attach the log file to a bug report.

## Tips

- Enable verbose logging for the relevant subsystem before clearing, so the reproduction run captures detailed output. Use the category checkboxes or click `Enable All` to turn on every logging category at once.
- Clear the log and reproduce the bug in one uninterrupted sequence. Any restart of AetherSDR between clearing and reproducing may add unrelated startup entries.

## Related

- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [View the live log without leaving the app](view-the-live-log-without-leaving-the-app.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)

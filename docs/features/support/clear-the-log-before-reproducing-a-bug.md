# Clear the Log Before Reproducing a Bug

Clearing the log before you trigger a problem ensures the log file contains only the relevant session, making it easier to isolate and report the issue.

## Before you start

- Open AetherSDR. A radio connection is not required for this procedure.
- If you want verbose output captured during the reproduction, enable the relevant logging categories first. See [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md).

## Steps

1. Click `Help > Support...` to open the Support & Diagnostics dialog.
2. Click `Clear Log`.
3. Confirm that the log viewer is now empty.
4. Close the dialog or leave it open, then perform the actions that trigger the bug.
5. Return to `Help > Support...` and click `Refresh` to reload the log file.
6. Review the log viewer to confirm the relevant output was captured.
7. Click `Open Log Folder` to access the log file in your OS file browser if you need to attach it to a report.

## Tips

- Click `Refresh` after reproducing the bug before reading the log. The log viewer does not update automatically.
- If you intend to file a report immediately after capturing the log, click `File an Issue` to start the AI-assisted bug report flow. See [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md).

## Troubleshooting

- **Log viewer is still showing old entries after clicking `Clear Log`** — Click `Refresh` to reload the now-truncated file. The viewer does not clear its display automatically on truncation.

## Related

- [Enable verbose logging for a specific subsystem](enable-verbose-logging-for-a-specific-subsystem.md)
- [View the live log without leaving the app](view-the-live-log-without-leaving-the-app.md)
- [File an AI-assisted bug report](file-an-ai-assisted-bug-report.md)
- [Open the log folder to grab multiple files](open-the-log-folder-to-grab-multiple-files.md)

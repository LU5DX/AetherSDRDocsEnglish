# Refresh the snapshot after changing slice state

The Slice Troubleshooting dialog captures radio state at the moment it opens. If you change a slice setting — such as unmuting a slice, switching an antenna, or adjusting DAX channel assignment — click **Refresh Snapshot** to pull the updated state into the dialog before reading the summary or sharing data with support.

## Before you start

- AetherSDR must be connected to the radio. The dialog is unavailable without an active radio connection.
- Open the dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Make your changes to the slice state in the main AetherSDR window (for example, unmute a slice, change the antenna, or adjust a DAX channel).
2. Return to the Slice Troubleshooting dialog.
3. Click **Refresh Snapshot**.
4. Check the status label at the bottom of the dialog. It will read something like `Snapshot refreshed: 2 slice(s), 4 global meter(s), 48 total meter(s).` confirming the update completed.
5. Review the updated results on the **Issue Summary** tab or the **JSON** tab.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Plain-language bullet list of detected problems such as missing audio, stuck mute, or missing antenna. |
| **JSON** | Tab | Full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Updates both tabs and the status label. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON to the clipboard. |
| **Export JSON...** | Button | Opens a save dialog and writes the JSON to a file. |
| **Close** | Button | Closes the dialog. |

## Tips

- The dialog reads from AetherSDR's in-memory model, not by re-querying the radio directly. If the radio itself has not yet propagated a change back to the client, wait a moment before clicking **Refresh Snapshot**.
- After refreshing, use **Copy Summary** or **Copy JSON** to capture the new state for a bug report or support request.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

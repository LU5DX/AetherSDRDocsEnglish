# Refresh the snapshot after changing slice state

The Slice Troubleshooting dialog captures a snapshot of radio state when it opens. If you change a slice setting after opening the dialog — for example, unmuting a slice or switching its antenna — the displayed data will be stale. Click **Refresh Snapshot** to re-read the current state so the **Issue Summary** and **JSON** tabs reflect your changes.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- The Slice Troubleshooting dialog must already be open. If it is not, go to `Help > Slice Troubleshooting...`.

## Steps

1. Make whatever slice state change you want to capture (for example, unmute a slice, change its mode, or reassign its antenna).
2. In the Slice Troubleshooting dialog, click **Refresh Snapshot**.
3. Check the status label at the bottom of the dialog. It will show a message in the form `Snapshot refreshed: N slice(s), N global meter(s), N total meter(s).`
4. Review the updated content on the **Issue Summary** tab or the **JSON** tab as needed.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Displays a plain-language bullet list of detected problems found in the refreshed snapshot. |
| **JSON** | Tab | Displays the full JSON snapshot of slices and DAX channels produced by the last refresh. |
| **Refresh Snapshot** | Button | Re-reads current slice state into the snapshot and updates both tabs. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. The status label confirms with `Issue summary copied to clipboard.` |
| **Copy JSON** | Button | Copies the full JSON to the clipboard. The status label confirms with `JSON copied to clipboard.` |
| **Export JSON...** | Button | Opens a file save dialog and writes the JSON to a file. |
| **Close** | Button | Closes the dialog. |

## Tips

- The dialog does not poll the radio continuously. Every time you change slice state and want fresh data, click **Refresh Snapshot** again.
- After refreshing, use **Copy Summary** to copy the updated issue list, or **Copy JSON** to copy the raw snapshot, before sharing with support.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

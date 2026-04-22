# Copy the Full JSON Snapshot to the Clipboard

Copy the complete JSON snapshot of your slice, panadapter, and meter state to the clipboard so you can paste it into a support request, GitHub issue, or AI-assisted troubleshooting session.

## Before you start

- AetherSDR must be connected to a radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the dialog before copying. If you have not opened it yet, continue to the steps below.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog.
2. Click the `JSON` tab to verify the snapshot content.
3. If the data looks stale or you have changed slice state since opening the dialog, click `Refresh Snapshot` to re-read the current state.
4. Click `Copy JSON`.
5. Paste the clipboard contents into your support ticket, chat message, or document.

The status label at the bottom of the dialog shows `JSON copied to clipboard.` when the copy succeeds.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `JSON` (tab) | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| `Refresh Snapshot` | Button | Re-reads slice state into the snapshot. Use this after changing slice settings to ensure the JSON is current. |
| `Copy JSON` | Button | Copies the full JSON to the clipboard. |
| `Export JSON...` | Button | Saves the JSON to a file instead of the clipboard. |
| `Copy Summary` | Button | Copies the plain-language issue summary to the clipboard instead of the raw JSON. |
| `Close` | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action. |

## Tips

- The dialog does not re-query the radio automatically. If you change a slice setting after opening the dialog, click `Refresh Snapshot` before clicking `Copy JSON` to ensure the snapshot reflects the current state.
- If you need to attach the JSON as a file rather than paste it inline, use `Export JSON...` instead.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

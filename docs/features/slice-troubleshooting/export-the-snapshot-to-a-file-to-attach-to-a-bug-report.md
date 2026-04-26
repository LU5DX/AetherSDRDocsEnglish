# Export the snapshot to a file to attach to a bug report

Use this page to save the JSON snapshot from the Slice Troubleshooting dialog to a file so you can attach it to a support request or bug report.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click `Refresh Snapshot` to ensure the snapshot reflects current radio state.
3. Click `Export JSON...`.
4. In the file dialog that opens, choose a destination folder and filename, then confirm the save.
5. Check the status label at the bottom of the dialog to confirm the export completed.
6. Attach the saved file to your bug report or support ticket.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Refresh Snapshot` | Button | Re-reads current slice, panadapter, transverter, and DAX channel state into the snapshot. Click this before exporting if slice state has changed. |
| `Export JSON...` | Button | Opens a file dialog and saves the full JSON snapshot to the chosen file. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard instead of saving to a file. |
| `JSON (tab)` | Tab | Displays the full JSON snapshot in the dialog so you can review it before exporting. |
| `Issue Summary (tab)` | Tab | Displays a plain-language list of detected problems alongside the raw JSON. |
| Status label | Indicator | Shows the result of the last copy or export action. |

## Tips

- Click `Refresh Snapshot` immediately before exporting if you have made any slice changes since opening the dialog. The snapshot does not update automatically.
- If your bug tracker does not accept file attachments, use `Copy JSON` to paste the snapshot directly into a comment or form field.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)

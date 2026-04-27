# Export the snapshot to a file to attach to a bug report

Use this page to save the JSON snapshot from the Slice Troubleshooting dialog to a file on disk so you can attach it to a support request or bug report.

## Before you start

- AetherSDR must be connected to a radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Open the Slice Troubleshooting dialog: `Help > Slice Troubleshooting...`
2. Click `Refresh Snapshot` to ensure the snapshot reflects current slice state.
3. Click `Export JSON...`.
4. In the file save dialog that appears, choose a destination folder and filename, then confirm the save.
5. Check the status label at the bottom of the dialog to confirm the export succeeded.
6. Attach the saved file to your bug report or support ticket.

## Tips

- If you have made changes to slice settings since opening the dialog, click `Refresh Snapshot` again before exporting to capture the latest state.
- If you only need to paste the snapshot into a web form or email rather than attach a file, use `Copy JSON` instead of `Export JSON...`.

## Troubleshooting

- **The status label shows no confirmation after clicking `Export JSON...`** — You may have cancelled the file save dialog without choosing a location. Click `Export JSON...` again and confirm the save.
- **`Export JSON...` is unavailable** — The dialog requires an active radio connection. Verify AetherSDR is connected to the radio before opening the dialog.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)

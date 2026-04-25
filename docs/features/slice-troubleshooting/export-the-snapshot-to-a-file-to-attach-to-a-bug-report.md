# Export the snapshot to a file to attach to a bug report

Save the current slice snapshot as a JSON file so you can attach it to a GitHub issue or support request.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog.
2. Click `Refresh Snapshot` to make sure the snapshot reflects the current radio state.
3. Click `Export JSON...`.
4. In the file save dialog that appears, choose a destination folder and filename, then confirm the save.
5. Attach the saved file to your bug report or GitHub issue.

The status label at the bottom of the dialog confirms the result of the export.

## Tips

- If you have just changed slice settings (mode, antenna, mute state), click `Refresh Snapshot` before exporting so the file reflects the latest state.
- The `JSON (tab)` shows exactly what will be saved. Review it before exporting if you want to confirm the snapshot content.
- If you only need to paste the data rather than attach a file, use `Copy JSON` instead.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)

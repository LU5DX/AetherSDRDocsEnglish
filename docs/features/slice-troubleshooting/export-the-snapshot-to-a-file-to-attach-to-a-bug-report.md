# Export the snapshot to a file to attach to a bug report

Use this page to save the JSON snapshot from the Slice Troubleshooting dialog to a file on disk, so you can attach it to a bug report or support request.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. In the Slice Troubleshooting dialog, click the `JSON` tab to confirm the snapshot contains current data. If the data looks stale, click `Refresh Snapshot` before exporting.
2. Click `Export JSON...`.
3. In the file save dialog that opens, choose a destination folder and filename, then confirm the save.
4. Check the status label at the bottom of the dialog to confirm the export succeeded.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Issue Summary` (tab) | Tab | Shows a plain-language bullet list of detected problems. |
| `JSON` (tab) | Tab | Shows the full JSON snapshot of slices and DAX channels. |
| `Refresh Snapshot` | Button | Re-reads slice state into the snapshot. Click this before exporting if slice state has changed. |
| `Copy Summary` | Button | Copies the issue summary text to the clipboard. |
| `Copy JSON` | Button | Copies the full JSON to the clipboard. |
| `Export JSON...` | Button | Opens a file save dialog and writes the JSON snapshot to disk. |
| `Close` | Button | Closes the dialog. |
| Status label | Indicator | Displays the result of the last copy or export action. |

## Tips

- Click `Refresh Snapshot` immediately before exporting if you have changed any slice settings since opening the dialog. The export writes whatever is currently shown in the `JSON` tab.
- If you need to paste the snapshot directly into a web form or email rather than attach a file, use `Copy JSON` instead.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

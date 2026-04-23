# Export the snapshot to a file to attach to a bug report

Save the current slice troubleshooting snapshot as a JSON file so you can attach it to a GitHub issue or support request.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click the `JSON` tab to confirm the snapshot contains data.
3. If the snapshot is stale, click `Refresh Snapshot` to re-read the current slice state.
4. Click `Export JSON...`.
5. In the file dialog, confirm or change the filename and destination. The default filename is `aethersdr-slice-troubleshooting-YYYYMMDD-HHmmss.json` in your home directory.
6. Click Save.
7. Check the status label at the bottom of the dialog. A successful export shows no error. If the file could not be written, the status label shows `Unable to write '<path>'`.
8. Attach the saved `.json` file to your bug report.

## Tips

- The default filename includes a timestamp, so repeated exports do not overwrite each other.
- If you only need the text and do not want a file, use `Copy JSON` to put the snapshot on the clipboard instead.

## Troubleshooting

- **Status label shows `Unable to write '<path>'`** — The chosen path is not writable. Select a directory where you have write permission, such as your home directory or Desktop.
- **Snapshot looks outdated** — Click `Refresh Snapshot` before clicking `Export JSON...`. The dialog does not re-query the radio automatically after it opens.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)

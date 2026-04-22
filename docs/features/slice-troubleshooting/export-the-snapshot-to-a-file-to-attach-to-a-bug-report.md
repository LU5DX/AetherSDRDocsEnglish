# Export the snapshot to a file to attach to a bug report

Save the current slice troubleshooting snapshot as a JSON file on disk so you can attach it to a GitHub issue or support request.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click `JSON` to confirm the snapshot contains current data. If the state looks stale, click `Refresh Snapshot` first.
3. Click `Export JSON...`.
4. In the file-save dialog, choose a destination folder and confirm or edit the filename. The default filename is `aethersdr-slice-troubleshooting-YYYYMMDD-HHmmss.json`, placed in your home directory.
5. Click Save.
6. Check the status label at the bottom of the dialog. If the export succeeded, the label shows the result. If the write failed, the label shows `Unable to write` followed by the path — check that the destination folder exists and that you have write permission, then try again.

## Tips

- The default filename includes a timestamp, so exporting multiple snapshots before and after a configuration change will not overwrite previous files.
- If you cannot attach a JSON file directly (for example, a forum that blocks `.json` uploads), use `Copy JSON` instead and paste the text into a code block in your report.

## Troubleshooting

- **Status label shows "Unable to write `<path>`"** — The file could not be created. Verify the destination folder exists and that your user account has write permission to it. Try saving to your home directory.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

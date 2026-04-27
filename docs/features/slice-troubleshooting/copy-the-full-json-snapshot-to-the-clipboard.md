# Copy the full JSON snapshot to the clipboard

The Slice Troubleshooting dialog captures a JSON snapshot of every slice, panadapter, transverter, and DAX channel. This page explains how to copy that snapshot to the clipboard so you can paste it into a support ticket, forum post, or bug report.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- If slice state has changed since you last opened the dialog, click "Refresh Snapshot" before copying to ensure the data is current.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click the `JSON` tab.
3. Click `Copy JSON`.
4. Confirm the status label reads `Copied to clipboard`.
5. Paste into your target application.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `JSON` (tab) | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| `Issue Summary` (tab) | Tab | Displays a plain-language bullet list of detected problems. |
| `Refresh Snapshot` | Button | Re-reads current slice state into the snapshot. Click this after making any slice changes before copying. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard. |
| `Copy Summary` | Button | Copies the issue summary text to the clipboard instead. |
| `Export JSON...` | Button | Saves the JSON snapshot to a file. |
| `Close` | Button | Closes the dialog. |

## Tips

- If you want only a plain-language problem summary rather than the full JSON, use `Copy Summary` on the `Issue Summary` tab instead.
- To get the most accurate snapshot, make any slice configuration changes first, then click `Refresh Snapshot`, then `Copy JSON`.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)

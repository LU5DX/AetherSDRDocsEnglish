# Copy the Full JSON Snapshot to the Clipboard

Copy the raw JSON snapshot of all slices and DAX channels to the clipboard so you can paste it into a support ticket, forum post, or bug report.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Slice Troubleshooting dialog requires an active radio connection.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click the `JSON` tab to confirm the snapshot contains the data you want to share.
3. If the data looks stale, click `Refresh Snapshot` to re-read current slice state.
4. Click `Copy JSON`.
5. The status label in the dialog updates to confirm the copy (for example, "Copied to clipboard").
6. Paste the clipboard contents into your support ticket or forum post.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Issue Summary` tab | Tab | Switches the view to a plain-language bullet list of detected problems. |
| `JSON` tab | Tab | Switches the view to the full JSON snapshot of slices and DAX channels. |
| `Refresh Snapshot` | Button | Re-reads slice state and updates the snapshot. Click this after changing slice settings before copying. |
| `Copy Summary` | Button | Copies the plain-language issue summary to the clipboard, not the full JSON. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard. |
| `Export JSON...` | Button | Saves the JSON snapshot to a file instead of the clipboard. |
| `Close` | Button | Closes the dialog. |

## Tips

- Click `Refresh Snapshot` before `Copy JSON` if you have changed slice state since opening the dialog. The snapshot is not updated automatically.
- To attach the JSON as a file rather than paste it inline, use `Export JSON...` instead.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

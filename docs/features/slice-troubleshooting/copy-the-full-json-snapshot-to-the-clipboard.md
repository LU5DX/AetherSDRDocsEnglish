# Copy the full JSON snapshot to the clipboard

Copy the raw JSON snapshot from the Slice Troubleshooting dialog to your clipboard so you can paste it into a bug report, forum post, or support ticket.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click `Refresh Snapshot` to ensure the snapshot reflects the current slice state.
3. Click `Copy JSON`.
4. Check the status label at the bottom of the dialog. It will read `Copied to clipboard` when the operation succeeds.
5. Paste the clipboard contents into your target document.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `JSON (tab)` | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| `Issue Summary (tab)` | Tab | Displays a plain-language bullet list of detected problems. |
| `Refresh Snapshot` | Button | Re-reads slice state into the snapshot. Click before copying to ensure the data is current. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard. |
| `Copy Summary` | Button | Copies the issue summary text to the clipboard instead of the JSON. |
| `Export JSON...` | Button | Saves the JSON snapshot to a file. |
| `Close` | Button | Closes the dialog. |

## Tips

- If you have just changed a slice setting (mode, antenna, mute state), click `Refresh Snapshot` before `Copy JSON`. The snapshot is not updated automatically when radio state changes.
- To attach the snapshot as a file rather than paste it inline, use `Export JSON...` instead.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

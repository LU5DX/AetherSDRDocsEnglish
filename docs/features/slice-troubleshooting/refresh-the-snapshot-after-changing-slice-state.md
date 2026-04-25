# Refresh the snapshot after changing slice state

The Slice Troubleshooting dialog captures a snapshot of slice state when it opens. If you change something — unmute a slice, switch antennas, adjust DAX — the displayed data goes stale. Clicking "Refresh Snapshot" re-reads the current state so the summary and JSON reflect your changes.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Make the slice change you want to capture (for example, unmute a slice or reassign an antenna).
2. In the Slice Troubleshooting dialog, click `Refresh Snapshot`.
3. Check the `Issue Summary` tab to confirm the updated state is reflected in the problem list.
4. Switch to the `JSON` tab if you need to verify the raw values.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Refresh Snapshot` | Button | Re-reads slice state into the snapshot. Both the `Issue Summary` and `JSON` tabs update. |
| `Issue Summary` (tab) | Tab | Plain-language bullet list of detected problems based on the current snapshot. |
| `JSON` (tab) | Tab | Full JSON snapshot of slices and DAX channels based on the current snapshot. |
| `Copy Summary` | Button | Copies the issue summary to the clipboard. |
| `Copy JSON` | Button | Copies the full JSON to the clipboard. |
| `Export JSON...` | Button | Saves the JSON to a file. |
| `Close` | Button | Closes the dialog. |
| Status label | Indicator | Shows the last copy or export result, for example `Copied to clipboard`. |

## Tips

- The dialog does not re-query the radio continuously. Any state change made after the dialog opens will not appear until you click `Refresh Snapshot`.
- After refreshing, use `Copy Summary` or `Copy JSON` to capture the updated data for a support report.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

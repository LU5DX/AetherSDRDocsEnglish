# Refresh the snapshot after changing slice state

After you make a change to a slice — such as unmuting it, switching its antenna, or enabling DAX audio — the Slice Troubleshooting dialog does not update automatically. Use "Refresh Snapshot" to re-read the current slice state so the Issue Summary and JSON reflect your changes.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Make the slice change you want to verify (for example, unmute a slice or reassign its antenna).
2. In the Slice Troubleshooting dialog, click `Refresh Snapshot`.
3. Review the updated content on the `Issue Summary` tab or the `JSON` tab.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Refresh Snapshot` | Button | Re-reads slice state into the snapshot. Both tabs update immediately. |
| `Issue Summary` (tab) | Tab | Plain-language bullet list of detected problems based on the current snapshot. |
| `JSON` (tab) | Tab | Full JSON snapshot of slices and DAX channels based on the current snapshot. |
| `Copy Summary` | Button | Copies the issue summary to the clipboard. |
| `Copy JSON` | Button | Copies the full JSON to the clipboard. |
| `Export JSON...` | Button | Saves the JSON to a file. |
| `Close` | Button | Closes the dialog. |

## Tips

- Click `Refresh Snapshot` after every slice state change you want to evaluate. The dialog does not poll for changes on its own.
- After refreshing, use `Copy JSON` or `Export JSON...` to capture the updated snapshot before sharing it with support.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

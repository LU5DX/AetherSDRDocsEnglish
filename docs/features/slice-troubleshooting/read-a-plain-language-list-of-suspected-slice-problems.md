# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog analyzes your current slice state and presents detected problems in plain English. Use it when a slice is behaving unexpectedly and you want a quick summary before digging into settings or contacting support.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...`.
2. In the Slice Troubleshooting dialog, click the `Issue Summary` tab.
3. Read the bullet list of detected problems. Each item describes a likely issue such as missing audio, stuck mute, or missing antenna.
4. If the list does not reflect your current radio state, click `Refresh Snapshot` to re-read slice state, then re-check the `Issue Summary` tab.
5. To share the summary, click `Copy Summary`. The text is copied to the clipboard. The status label at the bottom of the dialog confirms the result.
6. Click `Close` when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| `Issue Summary` | Tab | Displays a plain-language bullet list of detected problems. |
| `JSON` | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| `Refresh Snapshot` | Button | Re-reads slice state into the snapshot. |
| `Copy Summary` | Button | Copies the issue summary text to the clipboard. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard. |
| `Export JSON...` | Button | Saves the JSON snapshot to a file. |
| `Close` | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action, for example "Copied to clipboard". |

## Tips

- The dialog does not continuously poll the radio. If you change slice settings after opening the dialog, click `Refresh Snapshot` before reading the `Issue Summary` tab again.
- The `Issue Summary` tab is suited for pasting into GitHub issue reports. For AI-assisted troubleshooting, use the `JSON` tab instead.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

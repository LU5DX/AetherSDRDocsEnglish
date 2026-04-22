# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog inspects AetherSDR's current slice state and displays a plain-language summary of detected problems — such as missing audio, stuck mute, or missing antenna. Use this when a slice behaves unexpectedly and you want a quick diagnosis before contacting support.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- The snapshot reflects AetherSDR's in-memory state at the moment you open or refresh it. It does not re-query the radio.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. The dialog opens with the **Issue Summary** tab active. Read the bullet list of detected problems.
3. If you have changed slice state since the dialog opened, click **Refresh Snapshot** to update the list.
4. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Displays a plain-language bullet list of detected problems with the current slices. |
| **JSON** | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot and updates both tabs. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Saves the JSON snapshot to a file. |
| **Close** | Button | Closes the dialog. |

The status label at the bottom of the dialog shows the result of the last action, such as "Issue summary copied to clipboard." or the slice and meter counts after a refresh.

## Tips

- The snapshot is taken automatically when the dialog opens. You do not need to click **Refresh Snapshot** unless you have changed something on the radio since opening the dialog.
- If you are filing a bug report, the **Issue Summary** tab content is suitable for pasting directly into a GitHub issue. Use **Copy Summary** to put it on the clipboard in one click.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

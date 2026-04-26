# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog analyzes your current slice state and displays a plain-language summary of detected problems — such as missing audio, stuck mute, or missing antenna — so you can quickly identify what is wrong without reading raw data.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click the **Issue Summary** tab.
3. Read the bullet list of detected problems.
4. If you have changed slice settings since opening the dialog, click **Refresh Snapshot** to re-read the current state before reading the summary again.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Shows a plain-language bullet list of detected problems. |
| **JSON** | Tab | Shows the full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Saves the JSON snapshot to a file. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action (for example, "Copied to clipboard"). |

## Tips

- If the **Issue Summary** tab shows no problems but audio is still missing, click **Refresh Snapshot** and check again. The snapshot reflects the state at the moment it was last captured, not continuously.
- Use **Copy Summary** to paste the issue list directly into a support message or forum post.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

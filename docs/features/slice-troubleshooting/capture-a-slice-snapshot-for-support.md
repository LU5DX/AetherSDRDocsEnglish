# Capture a slice snapshot for support

The Slice Troubleshooting dialog captures a snapshot of every slice's current state and summarizes likely problems. Use it to gather information before filing a bug report or asking for support.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog.
2. Review the **Issue Summary** tab for a plain-language list of detected problems (missing audio, stuck mute, missing antenna, and similar issues).
3. Click the **JSON** tab to view the full snapshot of slices and DAX channels.
4. Do one of the following to share the snapshot:
   - Click **Copy Summary** to copy the issue summary to the clipboard.
   - Click **Copy JSON** to copy the full JSON snapshot to the clipboard.
   - Click **Export JSON...** to save the JSON to a file you can attach to a bug report.
5. If you change slice state while the dialog is open, click **Refresh Snapshot** to re-read the current state before copying or exporting.
6. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Plain-language bullet list of detected problems. |
| **JSON** | Tab | Full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. |
| **Copy Summary** | Button | Copies the issue summary to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Saves the JSON to a file. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action (for example, "Copied to clipboard"). |

## Tips

- Use the **Issue Summary** tab when filing a GitHub issue. Use the **JSON** tab output when seeking AI-assisted troubleshooting or when support asks for the full state.
- Click **Refresh Snapshot** after making any change to slice configuration so the snapshot reflects the current state before you export or copy.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

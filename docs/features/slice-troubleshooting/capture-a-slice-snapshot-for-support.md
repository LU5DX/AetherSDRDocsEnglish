# Capture a slice snapshot for support

The Slice Troubleshooting dialog captures a point-in-time JSON snapshot of every slice and DAX channel, and summarizes detected problems in plain language. Use this when reporting a bug or asking for support — you can copy or export the data to share with the AetherSDR team.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog.
2. The snapshot is taken automatically when the dialog opens. Review the **Issue Summary** tab for a bullet list of detected problems (missing audio, stuck mute, missing antenna, and similar).
3. To see the raw data, click the **JSON** tab.
4. If you have changed slice state since opening the dialog, click `Refresh Snapshot` to re-read the current state.
5. To share the summary text, click `Copy Summary`. The text is placed on the clipboard. The status label confirms "Copied to clipboard".
6. To share the full JSON, click `Copy JSON`. Paste it into your support ticket or email.
7. To save the JSON to a file (for attaching to a bug report), click `Export JSON...` and choose a save location in the file dialog.
8. Click `Close` when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Plain-language bullet list of detected problems. |
| **JSON** | Tab | Full JSON snapshot of slices and DAX channels. |
| `Refresh Snapshot` | Button | Re-reads slice state into the snapshot. Use this after changing slice configuration. |
| `Copy Summary` | Button | Copies the issue summary text to the clipboard. |
| `Copy JSON` | Button | Copies the full JSON snapshot to the clipboard. |
| `Export JSON...` | Button | Opens a save dialog and writes the JSON to a file. |
| `Close` | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action (for example, "Copied to clipboard"). |

## Tips

- Take the snapshot before changing anything. If you reconfigure a slice to work around a problem, click `Refresh Snapshot` a second time after the change so you have both a before and after snapshot to compare.
- `Export JSON...` produces a file you can attach directly to a bug report without needing to paste large amounts of text.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

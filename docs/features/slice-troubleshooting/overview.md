# Slice Troubleshooting

The Slice Troubleshooting dialog captures a snapshot of every slice and DAX channel on the connected radio, then analyzes it for likely problems such as missing audio, stuck mute, and missing antenna. Use it to diagnose slice issues yourself or to collect information to share with support.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog requires an active radio connection.

## How it works

Open the dialog from `Help > Slice Troubleshooting...`. When it opens, AetherSDR reads the current state of all slices and DAX channels into a snapshot. The dialog presents that snapshot in two views, accessible as tabs.

**Issue Summary tab** — shows a plain-language bullet list of problems detected in the snapshot, such as missing audio devices, stuck mute states, or unconfigured antennas. Review this tab first to get a quick reading of what may be wrong.

**JSON tab** — shows the full snapshot as structured JSON, covering every slice property and DAX channel assignment. Use this view when the Issue Summary does not capture enough detail, or when a support contact asks for the raw data.

The snapshot is taken when the dialog opens. If you change slice settings while the dialog is open, click "Refresh Snapshot" to re-read the current state before copying or exporting.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Issue Summary (tab) | Tab | Displays a plain-language bullet list of detected slice problems. |
| JSON (tab) | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| Refresh Snapshot | Button | Re-reads slice state and updates both tabs with current data. |
| Copy Summary | Button | Copies the Issue Summary text to the clipboard. |
| Copy JSON | Button | Copies the full JSON snapshot to the clipboard. |
| Export JSON... | Button | Opens a file dialog to save the JSON snapshot to a file. |
| Close | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the most recent copy or export action (for example, "Copied to clipboard"). |

## Tips

- Click "Refresh Snapshot" after making any change to slice configuration — the dialog does not update automatically.
- Use "Copy Summary" to paste a concise problem list into a support forum post. Use "Copy JSON" or "Export JSON..." when a support contact needs the full snapshot.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

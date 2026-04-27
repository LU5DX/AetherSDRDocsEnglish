# Slice Troubleshooting

The Slice Troubleshooting dialog captures a snapshot of every slice, panadapter, transverter, and DAX channel on the connected radio and checks for likely configuration problems. Use it to diagnose audio, mute, antenna, and transverter issues, or to collect diagnostic data before contacting support.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog is not available without an active radio connection.

## How it works

Open the dialog with `Help > Slice Troubleshooting...`. When the dialog opens, AetherSDR reads the current radio state into a snapshot. The snapshot covers slices, panadapters, transverters, DAX channels, and associated metadata. The dialog checks that snapshot for a set of known problem patterns — missing audio, stuck mute, missing antenna, and transverter validity issues — and presents the results in two tabs.

**Issue Summary tab** shows a plain-language bullet list of detected problems. If nothing is wrong, the list is empty. This is the fastest way to see whether AetherSDR has identified a configuration issue.

**JSON tab** shows the full snapshot as structured JSON. This view contains every field AetherSDR collected: slice state, panadapter parameters, transverter RF/IF frequencies, offsets, validity flags, and DAX channel assignments. Support staff and advanced users can inspect individual field values here.

The snapshot reflects radio state at the moment it was taken. If you change slice settings while the dialog is open, click **Refresh Snapshot** to re-read the current state before drawing conclusions or sharing data.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Issue Summary | Tab | Displays a plain-language bullet list of detected problems. |
| JSON | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| Refresh Snapshot | Button | Re-reads slice state into the snapshot. Use this after changing radio configuration. |
| Copy Summary | Button | Copies the issue summary text to the clipboard. |
| Copy JSON | Button | Copies the full JSON snapshot to the clipboard. |
| Export JSON... | Button | Opens a file dialog to save the JSON snapshot to a file. |
| Close | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the most recent copy or export action (for example, "Copied to clipboard"). |

## Tips

- Take a new snapshot with **Refresh Snapshot** after every configuration change. The dialog does not update automatically while it is open.
- Use **Copy Summary** to paste a concise problem list into a support forum post or email. Use **Copy JSON** or **Export JSON...** when attaching full diagnostic data to a bug report.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)

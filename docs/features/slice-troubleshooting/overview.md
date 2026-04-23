# Slice Troubleshooting Overview

The Slice Troubleshooting dialog captures a snapshot of AetherSDR's current in-memory radio, panadapter, slice, and meter state. Use it to diagnose common slice problems yourself or to produce a report for support.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- The snapshot reflects in-memory state at the moment you open the dialog or click Refresh Snapshot. It does not re-query the radio.

## How it works

Open the dialog from `Help > Slice Troubleshooting...`. The snapshot is taken automatically when the dialog opens.

The dialog presents two views of the same snapshot, selectable by tab:

- **Issue Summary** — a plain-language bullet list of detected problems, such as missing audio, stuck mute, or missing antenna assignments.
- **JSON** — the full snapshot in JSON format, covering slices, DAX channels, panadapters, meters, client DSP state, and UI state.

Once you have the snapshot, you can copy or export it using the buttons along the bottom of the dialog. The status label above the buttons shows the result of the last action (for example, "Issue summary copied to clipboard." or "JSON copied to clipboard.").

To capture a fresh snapshot after making changes to slice state, click Refresh Snapshot. The status label then reports how many slices, global meters, and total meters were found.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Issue Summary | Tab | Displays a plain-language bullet list of detected slice problems. |
| JSON | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| Refresh Snapshot | Button | Re-reads slice state into the snapshot and updates both tabs. |
| Copy Summary | Button | Copies the issue summary text to the clipboard. |
| Copy JSON | Button | Copies the full JSON to the clipboard. |
| Export JSON... | Button | Opens a save dialog to write the JSON to a file. The default filename includes a timestamp, for example `aethersdr-slice-troubleshooting-20240501-143022.json`. |
| Close | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action, and the slice/meter counts after a refresh. |

## Tips

- Use the Issue Summary tab when filing a GitHub issue. Use the JSON tab when working through a problem with AI-assisted tools or attaching a file to a bug report.
- If you change a slice setting (such as unmuting or reassigning an antenna) while the dialog is open, click Refresh Snapshot to update the snapshot before copying or exporting.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

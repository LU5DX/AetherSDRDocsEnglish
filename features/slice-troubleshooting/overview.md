# Slice Troubleshooting Overview

The Slice Troubleshooting dialog captures a snapshot of AetherSDR's current in-memory slice, panadapter, and meter state and analyzes it for common problems. Use it to diagnose issues yourself or to gather information for a support request or bug report.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- The snapshot reflects AetherSDR's in-memory state at the moment it is taken. It does not re-query the radio.

## How it works

Open the dialog from `Help > Slice Troubleshooting...`. The snapshot is taken automatically when the dialog opens. Two tabs present the same data in different forms:

- **Issue Summary** — a plain-language bullet list of detected problems such as missing audio, stuck mute, and missing antenna assignments.
- **JSON** — the full structured snapshot covering slices, panadapters, DAX channels, meters, client DSP state, and UI state. This tab is suited for AI-assisted troubleshooting or attaching to a bug report.

After you change slice state — for example, unmuting a slice or reassigning an antenna — click **Refresh Snapshot** to update both views.

The status label at the bottom of the dialog confirms the result of each action, for example showing how many slices and meters were found, or confirming that content was copied or exported.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Issue Summary | Tab | Displays a plain-language bullet list of detected problems. |
| JSON | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| Refresh Snapshot | Button | Re-reads slice state into the snapshot and updates both tabs. |
| Copy Summary | Button | Copies the issue summary text to the clipboard. |
| Copy JSON | Button | Copies the full JSON to the clipboard. |
| Export JSON... | Button | Opens a save dialog to write the JSON to a file. The default filename is `aethersdr-slice-troubleshooting-<timestamp>.json` in your home directory. |
| Close | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last action, such as "Copied to clipboard" or a slice and meter count after a refresh. |

## Tips

- Use the **Issue Summary** tab when filing a GitHub issue. Use **Copy Summary** to paste its content directly into a report.
- Use **Export JSON...** to save a file you can attach to a bug report or share with support for AI-assisted analysis.
- The snapshot includes client-side DSP state (NR2, NR4, DFNR) alongside radio state, which helps reproduce problems that depend on both.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

# Slice Troubleshooting Overview

The Slice Troubleshooting dialog captures a snapshot of AetherSDR's current slice, panadapter, and DAX channel state, then analyzes it for common problems. Use it to diagnose audio, mute, and antenna issues yourself, or to gather diagnostic data before contacting support.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.

## How it works

Open the dialog from `Help > Slice Troubleshooting...`. When the dialog opens, AetherSDR reads the current in-memory radio and slice state into a snapshot. The snapshot is not automatically refreshed if you change slice settings after opening the dialog — click "Refresh Snapshot" to update it.

The dialog has two tabs:

- **Issue Summary** — shows a plain-language bullet list of detected problems, such as missing audio, stuck mute, or missing antenna assignments.
- **JSON** — shows the full snapshot as structured JSON, covering slices, panadapters, DAX channels, meters, and client DSP state.

A status label below the tabs confirms the result of copy and export actions (for example, "Copied to clipboard").

## What each control does

| Control | Kind | What it does |
|---|---|---|
| Issue Summary (tab) | Tab | Displays a plain-language bullet list of detected problems. |
| JSON (tab) | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| Refresh Snapshot | Button | Re-reads current slice state into the snapshot. Use this after changing slice configuration while the dialog is open. |
| Copy Summary | Button | Copies the issue summary text to the clipboard. |
| Copy JSON | Button | Copies the full JSON snapshot to the clipboard. |
| Export JSON... | Button | Opens a file save dialog to write the JSON snapshot to a file. |
| Close | Button | Closes the dialog. |

## Tips

- Use the **Issue Summary** tab and "Copy Summary" when filing a GitHub issue — the plain-language format is easier to read in a bug report.
- Use the **JSON** tab and "Copy JSON" or "Export JSON..." when you need to provide detailed diagnostic data, for example for AI-assisted troubleshooting or attaching to a support ticket.
- If you change a slice setting (mode, antenna, mute) while the dialog is open, click "Refresh Snapshot" before copying or exporting, otherwise the snapshot will reflect the state at the time the dialog was opened.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

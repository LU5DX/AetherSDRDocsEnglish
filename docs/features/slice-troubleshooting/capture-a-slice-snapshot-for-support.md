# Capture a slice snapshot for support

The Slice Troubleshooting dialog captures a point-in-time snapshot of every slice, panadapter, and DAX channel as a JSON document, and summarizes likely problems in plain language. Use it to gather the information a support request or bug report needs.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- Reproduce or reach the problem state before opening the dialog. The snapshot reads in-memory state at the moment you open or refresh it; it does not re-query the radio.

## Steps

1. Click `Help > Slice Troubleshooting...`. The Slice Troubleshooting dialog opens and immediately captures a snapshot.
2. Review the **Issue Summary** tab for a plain-language bullet list of detected problems (missing audio, stuck mute, missing antenna, and similar conditions).
3. Switch to the **JSON** tab if you need the full technical snapshot.
4. If you changed slice state after opening the dialog, click **Refresh Snapshot** to re-read the current state. The status label at the bottom of the dialog shows a count of slices and meters captured.
5. To share the issue summary (for example, in a GitHub issue), click **Copy Summary**. The status label confirms "Issue summary copied to clipboard."
6. To share the full JSON (for example, for AI-assisted troubleshooting), click **Copy JSON**. The status label confirms "JSON copied to clipboard."
7. To save the JSON as a file to attach to a bug report, click **Export JSON...**. A save dialog opens with a default filename of the form `aethersdr-slice-troubleshooting-YYYYMMDD-HHmmss.json` in your home directory. Choose a location and confirm.
8. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Displays a plain-language bullet list of detected problems in the current snapshot. |
| **JSON** | Tab | Displays the full JSON snapshot of slices, panadapters, DAX channels, and client DSP state. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Use this after changing slice configuration. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON text to the clipboard. |
| **Export JSON...** | Button | Opens a save dialog to write the JSON to a file. Default filename includes a timestamp. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last action, such as "Issue summary copied to clipboard." or a count of slices and meters after a refresh. |

## Tips

- The snapshot is taken from AetherSDR's in-memory model, not by sending new commands to the radio. If the radio state has changed, click **Refresh Snapshot** before copying or exporting.
- The **Issue Summary** tab content is formatted for readability in GitHub issues. The **JSON** tab content is better suited for pasting into AI chat tools or attaching as a file.
- The exported JSON filename includes a timestamp, so exporting multiple snapshots in sequence will not overwrite previous files.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

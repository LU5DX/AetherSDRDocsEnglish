# Capture a slice snapshot for support

The Slice Troubleshooting dialog captures a point-in-time snapshot of every slice, panadapter, and DAX channel in AetherSDR's current in-memory state. Use it to collect diagnostic information before filing a bug report or asking for help.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- Reproduce or confirm the problem you want to report before opening the dialog, so the snapshot reflects the relevant state.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. The dialog opens on the **Issue Summary** tab and takes a snapshot automatically. Review the bullet list for any detected problems (missing audio, stuck mute, missing antenna).
3. Click the **JSON** tab to see the full JSON snapshot of slices and DAX channels.
4. If you changed slice state after opening the dialog, click **Refresh Snapshot** to re-read the current state.
5. To share a plain-language summary, click **Copy Summary**. The text is copied to the clipboard.
6. To share the full technical detail, click **Copy JSON**. The full JSON is copied to the clipboard.
7. To save the snapshot as a file for attachment to a bug report, click **Export JSON...**, choose a save location, and confirm. The default filename is `aethersdr-slice-troubleshooting-<timestamp>.json` in your home directory.
8. Check the status label at the bottom of the dialog to confirm the last action (for example, `Issue summary copied to clipboard.` or `JSON copied to clipboard.`).
9. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Displays a plain-language bullet list of detected problems. |
| **JSON** | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. |
| **Copy Summary** | Button | Copies the issue summary to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON to the clipboard. |
| **Export JSON...** | Button | Opens a save dialog and writes the JSON to a file. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action. |

## Tips

- The dialog reads AetherSDR's in-memory state only. It does not re-query the radio over the network. If the radio state changed recently and the snapshot looks stale, click **Refresh Snapshot**.
- The **Issue Summary** tab is suited for pasting into GitHub issues or forum posts. The **JSON** tab output is better for detailed or AI-assisted troubleshooting.
- The exported filename includes a timestamp, so repeated exports do not overwrite each other.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

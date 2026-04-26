# Capture a slice snapshot for support

The Slice Troubleshooting dialog captures a full snapshot of your slices, panadapters, transverters, and DAX channels and summarizes likely problems in plain language. Use it to gather the information a support request needs before filing a bug report or asking for help.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog. The snapshot is taken automatically when the dialog opens.
2. Review detected problems on the **Issue Summary** tab. Each entry is a plain-language bullet describing a suspected issue such as missing audio, stuck mute, missing antenna, or an invalid transverter.
3. Switch to the **JSON** tab to see the full machine-readable snapshot covering every slice, panadapter, transverter, and DAX channel.
4. If you changed radio state after opening the dialog, click **Refresh Snapshot** to re-read the current slice state.
5. To share the summary with support, click **Copy Summary**. The issue summary is copied to the clipboard. The status label at the bottom of the dialog confirms the result.
6. To share the full detail, click **Copy JSON** to copy the complete JSON to the clipboard, or click **Export JSON...** to save it to a file you can attach to a bug report.
7. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Displays a plain-language bullet list of detected problems. |
| **JSON** | Tab | Displays the full JSON snapshot of slices, panadapters, transverters, and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Use this after changing radio configuration. |
| **Copy Summary** | Button | Copies the issue summary to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Opens a file save dialog and writes the JSON snapshot to a file. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action, for example "Copied to clipboard". |

## Tips

- Click **Refresh Snapshot** after making any change to slice, antenna, or DAX settings so the snapshot reflects the current state before you copy or export it.
- If you are filing a bug report, use **Export JSON...** rather than **Copy JSON** so you have a saved file to attach without risk of overwriting the clipboard.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)

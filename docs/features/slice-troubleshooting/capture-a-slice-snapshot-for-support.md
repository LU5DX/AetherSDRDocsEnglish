# Capture a slice snapshot for support

The Slice Troubleshooting dialog captures a point-in-time snapshot of every slice, panadapter, transverter, and DAX channel on the connected radio. Use it to gather information before filing a bug report or asking for support.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog is not available without an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...`. The Slice Troubleshooting dialog opens and immediately captures a snapshot.
2. Review detected problems on the **Issue Summary** tab. Each entry is a plain-language bullet describing a suspected issue such as missing audio, stuck mute, missing antenna, or an invalid transverter configuration.
3. Review the raw data on the **JSON** tab if you need the full detail or intend to attach it to a report.
4. If you changed slice state after opening the dialog, click **Refresh Snapshot** to re-read current slice state.
5. To share the summary text, click **Copy Summary**. The text is copied to the clipboard.
6. To share the full JSON, click **Copy JSON**. The full JSON snapshot is copied to the clipboard.
7. To save the JSON to a file, click **Export JSON...** and choose a save location in the file dialog that opens.
8. Watch the status label at the bottom of the dialog. It confirms the result of the last copy or export action (for example, "Copied to clipboard").
9. Click **Close** when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** | Tab | Displays a plain-language bullet list of detected problems, including missing audio, stuck mute, missing antenna, and transverter validity issues. |
| **JSON** | Tab | Displays the full JSON snapshot of all slices, panadapters, transverters, and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads current slice state from the radio and updates both tabs. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Opens a save dialog to write the JSON snapshot to a file. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action. |

## Tips

- Take the snapshot before and after changing slice configuration if you are trying to isolate a problem. Use **Refresh Snapshot** between captures to update the data.
- If you are reporting a transverter problem, the **JSON** tab includes each transverter's RF frequency, IF frequency, offset, and validity flags. The **Issue Summary** tab will flag any transverters where validity cannot be confirmed.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)

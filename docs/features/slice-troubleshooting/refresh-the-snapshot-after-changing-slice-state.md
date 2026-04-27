# Refresh the snapshot after changing slice state

After you change slice settings — such as adjusting audio routing, toggling mute, or switching antennas — the Slice Troubleshooting dialog does not update automatically. Use **Refresh Snapshot** to re-read the current slice state so the Issue Summary and JSON reflect your changes.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Make the slice state change you want to capture (for example, unmute a slice, reassign an antenna, or adjust a DAX channel).
2. In the Slice Troubleshooting dialog, click **Refresh Snapshot**.
3. The dialog re-reads all slice, panadapter, transverter, and DAX channel state.
4. Review the updated results on the **Issue Summary** tab or the **JSON** tab.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Use this after any slice configuration change. |
| **Issue Summary** (tab) | Tab | Shows a plain-language bullet list of detected problems based on the current snapshot. |
| **JSON** (tab) | Tab | Shows the full JSON snapshot of slices and DAX channels based on the current snapshot. |
| **Copy Summary** | Button | Copies the issue summary to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON to the clipboard. |
| **Export JSON...** | Button | Saves the JSON to a file. |
| **Close** | Button | Closes the dialog. |

## Tips

- After clicking **Refresh Snapshot**, check both the **Issue Summary** tab and the **JSON** tab to confirm the change you made is reflected before sharing the snapshot with support.
- If you plan to export or copy the snapshot for a bug report, always click **Refresh Snapshot** first to ensure the data is current.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

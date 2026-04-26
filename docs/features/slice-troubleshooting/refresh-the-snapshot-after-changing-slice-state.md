# Refresh the snapshot after changing slice state

After you make a change to a slice — such as unmuting audio, switching the antenna, or adjusting a DAX channel — the Slice Troubleshooting dialog does not update automatically. Use **Refresh Snapshot** to re-read the current slice state so the **Issue Summary** and **JSON** tabs reflect your changes.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Make the slice state change you want to verify (for example, unmute a slice, assign an antenna, or enable a DAX channel).
2. In the Slice Troubleshooting dialog, click **Refresh Snapshot**.
3. Check the **Issue Summary** tab for an updated plain-language list of detected problems, or click the **JSON** tab to inspect the full updated snapshot.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Refresh Snapshot** | Button | Re-reads all slice, panadapter, transverter, and DAX channel state into the snapshot. |
| **Issue Summary** (tab) | Tab | Displays a plain-language bullet list of detected problems based on the current snapshot. |
| **JSON** (tab) | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON to the clipboard. |
| **Export JSON...** | Button | Saves the JSON snapshot to a file. |
| **Close** | Button | Closes the dialog. |

## Tips

- After clicking **Refresh Snapshot**, check the status label at the bottom of the dialog to confirm the last operation result.
- If you are comparing state before and after a change, use **Export JSON...** to save a copy of the snapshot before refreshing.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

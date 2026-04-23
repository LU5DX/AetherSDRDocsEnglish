# Copy the full JSON snapshot to the clipboard

Copy the complete JSON snapshot of your radio's slice, panadapter, and meter state to the clipboard so you can paste it into a support thread, bug report, or AI-assisted troubleshooting session.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click the **JSON** tab to confirm the snapshot content looks current.
3. If you recently changed slice state and want the latest data, click **Refresh Snapshot** before copying.
4. Click **Copy JSON**.
5. The status label at the bottom of the dialog shows **JSON copied to clipboard.** confirming the copy succeeded.
6. Paste the clipboard contents wherever needed.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **JSON** (tab) | Tab | Displays the full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Click this after changing any slice settings to ensure the copied JSON reflects current state. |
| **Copy JSON** | Button | Copies the full JSON to the clipboard. |
| **Export JSON...** | Button | Saves the JSON to a file instead of the clipboard. |
| **Copy Summary** | Button | Copies the plain-language issue summary to the clipboard instead of the raw JSON. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last action, such as **JSON copied to clipboard.** |

## Tips

- The dialog does not re-query the radio automatically. If you have made changes since opening the dialog, click **Refresh Snapshot** before clicking **Copy JSON** to ensure the copied data is current.
- The snapshot includes slice state, panadapter state, meter readings, client DSP settings, and UI lock state. All of this is captured in a single clipboard paste.
- If you need a file attachment rather than clipboard text, use **Export JSON...** instead.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)

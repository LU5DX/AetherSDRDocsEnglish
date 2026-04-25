# Copy the full JSON snapshot to the clipboard

Copy the complete JSON snapshot of your slice, DAX, and radio state to the clipboard so you can paste it into a support thread, bug report, or AI-assisted troubleshooting session.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...`.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click the **JSON** tab to confirm the snapshot contains data.
3. If the data looks stale, click **Refresh Snapshot** to re-read the current slice state.
4. Click **Copy JSON**.
5. The status label at the bottom of the dialog shows `Copied to clipboard` when the operation succeeds.
6. Paste the clipboard contents into your support thread, chat, or document.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** (tab) | Tab | Plain-language bullet list of detected problems. |
| **JSON** (tab) | Tab | Full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON snapshot to the clipboard. |
| **Export JSON...** | Button | Saves the JSON to a file instead of the clipboard. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last copy or export action. |

## Tips

- If you want to share both a plain-language summary and the raw JSON, use **Copy Summary** first, then **Copy JSON** separately — each button overwrites the clipboard.
- To save the JSON as a file attachment rather than pasting it inline, use **Export JSON...** instead.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)

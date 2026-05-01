# Export the snapshot to a file to attach to a bug report

Use this page to save the JSON snapshot from the Slice Troubleshooting dialog to a file on disk so you can attach it to a support request or bug report.

## Before you start

- AetherSDR must be connected to a radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the Slice Troubleshooting dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Open the Slice Troubleshooting dialog: `Help > Slice Troubleshooting...`
2. Click `Refresh Snapshot` to ensure the snapshot reflects current slice state.
3. Click `Export JSON...`.
4. In the file save dialog that appears, choose a destination folder and filename, then confirm the save.
5. Check the status label at the bottom of the dialog to confirm the export succeeded.
6. Attach the saved file to your bug report or support ticket.

## Tips

- If you have made changes to slice settings since opening the dialog, click `Refresh Snapshot` again before exporting to capture the latest state.
- If you only need to paste the snapshot into a web form or email rather than attach a file, use `Copy JSON` instead of `Export JSON...`.

## What the Issue Summary includes

The **Issue Summary** tab displays a plain-language bullet list of detected problems. As of v0.9.4, the summary includes two additional remote audio RX entries:

- **Remote audio RX** — reports the stream ID, whether a stream is expected, whether creation is pending, whether a status message has been seen, whether the stream is owned by this client, and the compression setting in use.
- **Remote audio route note** — a free-text routing note that may indicate why a remote audio RX stream is not functioning as expected.

Each slice audio route section also now includes a **Radio stream route** line that reports the remote audio RX stream ID along with its expected, create-pending, remove-requested, status-seen, and owned-by-us flags. Review these lines first when diagnosing remote audio RX problems before contacting support.

## Troubleshooting

- **The status label shows no confirmation after clicking `Export JSON...`** — You may have cancelled the file save dialog without choosing a location. Click `Export JSON...` again and confirm the save.
- **`Export JSON...` is unavailable** — The dialog requires an active radio connection. Verify AetherSDR is connected to the radio before opening the dialog.
- **The remote audio RX fields all show placeholders** — AetherSDR has not yet received a status message from the radio for that stream. Click `Refresh Snapshot` after the radio has had a moment to send stream status, then check the **Issue Summary** tab again.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
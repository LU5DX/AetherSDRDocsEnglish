# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog analyzes AetherSDR's current in-memory slice state and displays a plain-language summary of likely problems, such as missing audio, stuck mute, or missing antenna. Use this when a slice is behaving unexpectedly and you want a quick diagnosis before contacting support.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- The snapshot reflects AetherSDR's in-memory state at the moment it is taken. It does not re-query the radio. If you have just changed slice settings, refresh the snapshot before reading results.

## Steps

1. Click `Help > Slice Troubleshooting...`.
2. The dialog opens with the **Issue Summary** tab active and a snapshot already taken.
3. Read the bullet list of detected problems in the **Issue Summary** tab.
4. If you have changed slice state since opening the dialog, click **Refresh Snapshot** to update the list.
5. When finished, click **Close**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Issue Summary** (tab) | Tab | Plain-language bullet list of detected problems. |
| **JSON** (tab) | Tab | Full JSON snapshot of slices and DAX channels. |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot and updates both tabs. |
| **Copy Summary** | Button | Copies the issue summary text to the clipboard. |
| **Copy JSON** | Button | Copies the full JSON to the clipboard. |
| **Export JSON...** | Button | Saves the JSON to a file. |
| **Close** | Button | Closes the dialog. |
| Status label | Indicator | Shows the result of the last action, for example "Issue summary copied to clipboard." or the slice and meter counts after a refresh. |

## Tips

- The status label at the bottom of the dialog shows the snapshot counts after each refresh: number of slices, global meters, and total meters. Use this to confirm the snapshot captured what you expect.
- If the issue summary is empty, no problems were detected in the current snapshot. Try **Refresh Snapshot** if you have recently changed slice state.
- To share findings with support, click **Copy Summary** and paste into a GitHub issue or forum post. For AI-assisted troubleshooting, use **Copy JSON** or **Export JSON...** instead.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)

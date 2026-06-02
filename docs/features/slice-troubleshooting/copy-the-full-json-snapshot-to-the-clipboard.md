# Copy the full JSON snapshot to the clipboard

The Slice Troubleshooting dialog captures a JSON snapshot (schema v3) of every slice, panadapter, transverter, DAX channel, audio device, client DSP state, audio endpoint, control-device (MIDI) bindings, and renderer state. This page explains how to copy that snapshot to the clipboard so you can paste it into a support ticket, forum post, or bug report.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- If slice state has changed since you last opened the dialog, click `Refresh Snapshot` before copying to ensure the data is current.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Click the `JSON` tab.
3. Click `Copy JSON`.
4. Confirm the status label reads `Copied to clipboard`.
5. Paste into your target application.

## What each control does

| Control               | Kind   | Behavior                                                                                                                                                                                   |
|-----------------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `JSON` (tab)          | Tab    | Displays the full JSON snapshot (schema v3) of slices, DAX channels, audio devices, client DSP state, control devices, audio endpoints, and renderer state.                                |
| `Issue Summary` (tab) | Tab    | Displays a plain-language bullet list of detected problems, including audio routing, DSP, control-device (MIDI) state, multi-client ownership, panadapter connection status, and audio endpoint state. |
| `Refresh Snapshot`    | Button | Re-reads current slice state into the snapshot. Click this after making any slice changes before copying.                                                                                  |
| `Copy JSON`           | Button | Copies the full JSON snapshot to the clipboard.                                                                                                                                            |
| `Copy Summary`        | Button | Copies the issue summary text to the clipboard instead.                                                                                                                                    |
| `Export JSON...`      | Button | Saves the JSON snapshot to a file.                                                                                                                                                         |
| `Close`               | Button | Closes the dialog.                                                                                                                                                                         |

## What the Issue Summary includes

The `Issue Summary` tab generates a plain-language bullet list from the snapshot. As of v26.6.1 the summary includes the following additional items:

### Remote audio RX (radio-level)

The summary now reports the radio-level remote audio RX stream state, including:

- Stream ID, whether the stream was expected, whether creation is pending, whether a status message has been seen, whether this client owns the stream, and the compression setting in use.
- A routing note that explains any detected routing problem for the remote audio RX stream.

### Remote audio RX (per-slice radio stream route)

For each slice, the summary also reports the per-slice radio stream route for remote audio RX, including:

- Stream ID, expected flag, create-pending flag, remove-requested flag, status-seen flag, and owned-by-us flag.

These entries appear alongside the existing audio device, DSP, and TX route information already present in the summary.

### Panadapter slice connection status

For each panadapter, the summary now reports its connection status to slices, including:

- State (e.g. "connected", "partially_connected"), summary of connection status, list of connected slice IDs, list of active slice IDs, and whether the connection requires attention.

### Audio endpoint status

For each audio endpoint, the summary reports:

- Name, direction (INPUT/OUTPUT), kind, operational flag, running flag, state, error, backend, device name, sample rate, channel count, sample format, resampling flag, buffer statistics (buffer bytes, buffer peak bytes, underrun count), and any user-facing note.

These entries appear alongside the existing audio device and control-device information.

## Tips

- If you want only a plain-language problem summary rather than the full JSON, use `Copy Summary` on the `Issue Summary` tab instead.
- To get the most accurate snapshot, make any slice configuration changes first, then click `Refresh Snapshot`, then `Copy JSON`.
- The JSON snapshot can be pasted directly into an AI assistant for guided troubleshooting.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
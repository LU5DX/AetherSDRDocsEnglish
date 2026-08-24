# Slice Troubleshooting

The Slice Troubleshooting dialog captures a JSON snapshot of every slice, panadapter, transverter, and DAX channel and summarizes likely problems (missing audio, stuck mute, missing antenna, XVTR validity) so you can share it with support.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Make the slice state change you want to capture (for example, unmute a slice, reassign an antenna, or adjust a DAX channel).
2. In the Slice Troubleshooting dialog, click **Refresh Snapshot**.
3. The dialog re-reads all slice, panadapter, transverter, DAX channel, audio device, client DSP, control-device (MIDI) binding, audio endpoint, renderer, remote audio RX, and panadapter slice connection state.
4. Review the updated results on the **Issue Summary** tab or the **JSON** tab.

## What each control does

| Control                 | Kind                                                                                           | Behavior                                                                                                                                                                                                                                                                         |
|-------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Refresh Snapshot**    | Button                                                                                         | Re-reads slice state into the snapshot. Use this after any slice configuration change.                                                                                                                                                                                           |
| **Issue Summary** (tab) | Tab                                                                                            | Shows a plain-language bullet list of detected problems based on the current snapshot, including audio routing, DSP, control-device (MIDI) state, multi-client ownership, remote audio RX routing, audio endpoint state, renderer state, and panadapter slice connection status. |
| **JSON** (tab)          | Tab                                                                                            | Shows the full JSON snapshot (schema version 3) of slices, DAX channels, audio devices, client DSP, control devices, audio endpoints, renderers, TX band settings, remote audio RX state, and panadapter slice connection status.                                                |
| **Copy Summary**        | Button                                                                                         | Copies the issue summary to the clipboard.                                                                                                                                                                                                                                       |
| **Copy JSON**           | Button                                                                                         | Copies the full JSON to the clipboard.                                                                                                                                                                                                                                           |
| **Export JSON...**      | Button                                                                                         | Saves the JSON to a file.                                                                                                                                                                                                                                                        |
| **Find:**               | Text field                                                                                     | Highlights matching occurrences of the entered term in the active tab (Issue Summary or JSON). Has clear button and placeholder 'Search snapshot...'. Enter jumps to the next match; tab sharing updates highlight counts. Status label shows '<N> match(es) in current tab.'    |
| **Find Next**           | Button                                                                                         | Jumps to the next match of the search term in the active tab. Wraps within the current tab. Empty term produces no matches.                                                                                                                                                      |
| **Close**               | Button                                                                                         | Closes the dialog.                                                                                                                                                                                                                                                               |

## What the Issue Summary reports

The **Issue Summary** tab includes the following categories of information. Each item appears as a plain-language bullet in the summary.

### Radio-level audio and hardware state

- Headphone gain, headphone mute, and front speaker mute status.
- Oscillator setting, lock state, external reference, and TCXO status.

### Transmitter meter state

The summary reports TX meter status, including whether the TX meters are live. If the TX meters are NOT live, a warning bullet is shown:

- **TX meters are NOT live** – Indicates that TX forward power is the last value received, not a current reading, and TX SWR is omitted rather than shown stale. The bullet includes the time since the last sample (for example, "last sample 250 ms ago") or notes that no TX meter sample has been received this session. This prevents a support bundle reader from mistaking a stale wattage reading next to a missing SWR for an antenna problem.

### Remote audio RX state

The summary includes two bullets for remote audio RX:

- **Remote audio RX:** Reports the stream ID, whether a stream is expected, whether creation is pending, whether a status message has been seen, whether this client owns the stream, and the compression setting in use.
- **Remote audio route note:** A plain-language note about the remote audio RX routing state, if one is available.

### Per-slice audio routing

For each slice, the summary reports:

- Engine RX volume, mute state, and whether RX audio is streaming.
- **Radio stream route:** Reports the remote audio RX stream ID, whether the stream is expected, whether creation or removal is pending, whether a status message has been seen, and whether this client owns the stream.
- TX input route, microphone selection, DAX TX mode, and related settings.

### Audio endpoint state

For each audio endpoint, the summary reports:

- Name, direction (INPUT or OUTPUT), and kind (endpoint type).
- Backend, device name, sample rate, channel count, sample format, and whether resampling is active.
- For voice input endpoints, additional resampling details are reported:
  - Voice input normalization to 48 kHz.
  - Voice egress resampling to 24 kHz.
  - RADE resampling to 24 kHz.
- Operational and running status, stream state, and error information.
- Buffer statistics (buffer bytes, peak bytes, and underrun count) if available.
- Any additional notes about the endpoint.

### Renderer state

For each renderer in the audio engine, the summary reports the renderer name, a backend identifier, the sample rate, and whether audio is currently active.

### Panadapter slice connection status

For each panadapter, the summary reports:

- The slice connection state, a human-readable summary of the link status, the list of connected slice IDs, the list of active slice IDs, and whether the connection requires attention.

### Control device (MIDI) bindings

The summary reports each control device and the MIDI bindings associated with it, including the scope, mapping details, and error conditions.

## JSON snapshot details

The JSON snapshot includes the following client DSP parameters for NR2 (noise reduction 2):

- `nr2_enabled` – Whether NR2 is enabled.
- `gain_method` – The gain reduction method name.
- `gain_method_id` – The gain reduction method ID.
- `npe_method` – The noise power estimation method name.
- `npe_method_id` – The noise power estimation method ID.
- `ae_filter` – Whether the adaptive echo filter is enabled.
- `gain_max` – Maximum gain reduction value.
- `gain_floor` – Gain floor value.
- `gain_smooth` – Gain smoothing factor.
- `qspp` – Quasi-stationary power processor value.

The retired `legacy_geometry_and_gain_mapping` parameter and its associated setting key (`NR2UseOriginalGeometry`) are no longer part of the snapshot.

## Status indicator

After you click **Copy Summary**, **Copy JSON**, or **Export JSON...**, a status label below the buttons shows the result of the operation (for example, *Copied to clipboard*). The status label also shows the search match count when you use **Find:** or **Find Next**.

## Tips

- After clicking **Refresh Snapshot**, check both the **Issue Summary** tab and the **JSON** tab to confirm the change you made is reflected before sharing the snapshot with support.
- If you plan to export or copy the snapshot for a bug report, always click **Refresh Snapshot** first to ensure the data is current.
- The remote audio RX routing note in the Issue Summary is a useful first indicator of stream ownership or creation problems when troubleshooting audio that is not reaching the client.
- The panadapter slice connection status and audio endpoint details can help identify connectivity or stream state issues that may not appear elsewhere.
- If the TX meters are reported as NOT live, the TX forward power shown is the last smoothed value received, not a live reading. Treat it accordingly when diagnosing antenna or amplifier issues.
- Use **Find:** to quickly locate a slice ID, DAX channel, or error string in either tab without exporting the snapshot.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
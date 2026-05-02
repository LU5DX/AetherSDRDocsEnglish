# Refresh the snapshot after changing slice state

After you change slice settings — such as adjusting audio routing, toggling mute, or switching antennas — the Slice Troubleshooting dialog does not update automatically. Use **Refresh Snapshot** to re-read the current slice state so the Issue Summary and JSON reflect your changes.

## Before you start

- AetherSDR must be connected to the radio. The Slice Troubleshooting dialog requires an active radio connection.
- Open the dialog via `Help > Slice Troubleshooting...` if it is not already open.

## Steps

1. Make the slice state change you want to capture (for example, unmute a slice, reassign an antenna, or adjust a DAX channel).
2. In the Slice Troubleshooting dialog, click **Refresh Snapshot**.
3. The dialog re-reads all slice, panadapter, transverter, DAX channel, audio device, client DSP, control-device (MIDI) binding, and remote audio RX state.
4. Review the updated results on the **Issue Summary** tab or the **JSON** tab.

## What each control does

| Control                 | Kind   | Behavior                                                                               |
|-------------------------|--------|----------------------------------------------------------------------------------------|
| **Refresh Snapshot**    | Button | Re-reads slice state into the snapshot. Use this after any slice configuration change. |
| **Issue Summary** (tab) | Tab    | Shows a plain-language bullet list of detected problems based on the current snapshot, including audio routing, DSP, control-device (MIDI) state, multi-client ownership, and remote audio RX routing. |
| **JSON** (tab)          | Tab    | Shows the full JSON snapshot (schema version 3) of slices, DAX channels, audio devices, client DSP, control devices, TX band settings, and remote audio RX state. |
| **Copy Summary**        | Button | Copies the issue summary to the clipboard.                                             |
| **Copy JSON**           | Button | Copies the full JSON to the clipboard.                                                 |
| **Export JSON...**      | Button | Saves the JSON to a file.                                                              |
| **Close**               | Button | Closes the dialog.                                                                     |

## What the Issue Summary reports

The **Issue Summary** tab includes the following categories of information. Each item appears as a plain-language bullet in the summary.

### Radio-level audio and hardware state

- Headphone gain, headphone mute, and front speaker mute status.
- Remote audio RX stream ID, whether a stream is expected, whether creation is pending, whether a status message has been seen, whether this client owns the stream, and the compression setting in use.
- Remote audio route note: a plain-language note about the remote audio RX routing state, if one is available.
- Oscillator setting, lock state, external reference, and TCXO status.

### Remote audio RX state

The summary includes two bullets for remote audio RX:

- **Remote audio RX:** Reports the stream ID, whether a stream is expected, whether creation is pending, whether a status message has been seen, whether this client owns the stream, and the compression setting in use.
- **Remote audio route note:** A plain-language note about the remote audio RX routing state, if one is available.

### Per-slice audio routing

For each slice, the summary reports:

- Engine RX volume, mute state, and whether RX audio is streaming.
- **Radio stream route:** Reports the remote audio RX stream ID, whether the stream is expected, whether creation or removal is pending, whether a status message has been seen, and whether this client owns the stream.
- TX input route, microphone selection, DAX TX mode, and related settings.

## What the JSON snapshot includes

The `rx_route` object in the JSON snapshot includes the following remote audio RX fields:

| Field                                    | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| `remote_audio_rx_stream_id`              | The stream ID assigned to the remote audio RX stream.                       |
| `remote_audio_rx_stream_id_known`        | Whether the stream ID is currently known to this client.                    |
| `remote_audio_rx_create_pending`         | Whether a stream creation request is pending.                               |
| `remote_audio_rx_remove_requested`       | Whether a stream removal has been requested.                                |
| `remote_audio_rx_status_seen`            | Whether a status message for the stream has been received.                  |
| `remote_audio_rx_owned_by_us`            | Whether this client owns the remote audio RX stream.                        |
| `remote_audio_rx_expected`               | Whether a remote audio RX stream is expected to exist.                      |

## Status indicator

After you click **Copy Summary**, **Copy JSON**, or **Export JSON...**, a status label below the buttons shows the result of the operation (for example, *Copied to clipboard*).

## Tips

- After clicking **Refresh Snapshot**, check both the **Issue Summary** tab and the **JSON** tab to confirm the change you made is reflected before sharing the snapshot with support.
- If you plan to export or copy the snapshot for a bug report, always click **Refresh Snapshot** first to ensure the data is current.
- The remote audio RX routing note in the Issue Summary is a useful first indicator of stream ownership or creation problems when troubleshooting audio that is not reaching the client.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-01 -->
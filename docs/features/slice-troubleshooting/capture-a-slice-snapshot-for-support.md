# Capture a slice snapshot for support

The Slice Troubleshooting dialog captures a point-in-time snapshot of every slice, panadapter, transverter, DAX channel, audio device, client DSP state, control-device (MIDI) bindings, and audio renderer endpoints on the connected radio. Use it to gather information before filing a bug report or asking for support, or to share with AI-assisted troubleshooting tools.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog is not available without an active radio connection.

## Opening the dialog

1. Click `Help > Slice Troubleshooting...`. The Slice Troubleshooting dialog opens and immediately captures a snapshot. The dialog remembers its previous size and position.
2. Review detected problems on the **Issue Summary** tab. Each entry is a plain-language bullet describing a suspected issue such as missing audio, stuck mute, missing antenna, an invalid transverter configuration, audio routing problems, DSP state issues, control-device (MIDI) state, multi-client ownership conflicts, audio renderer endpoint issues, or panadapter connection status.
3. Review the raw data on the **JSON** tab if you need the full detail or intend to attach it to a report. The snapshot uses schema version 3 and includes slices, DAX channels, audio devices, client DSP state, control devices, TX band settings, remote audio RX stream state, audio renderer endpoints, and panadapter slice connection status.

## Searching the snapshot

The dialog includes a Find search that works across the current tab (Issue Summary or JSON).

1. Type a term in the **Find:** field. The field has a clear button and placeholder "Search snapshot...".
2. The status label shows the number of matches, for example "3 match(es) in current tab."
3. Press Enter or click **Find Next** to jump to the next match. Searching wraps within the current tab.
4. Clear the field to remove highlighting.

## Copying and exporting data

1. To share the summary text, click **Copy Summary**. The text is copied to the clipboard.
2. To share the full JSON, click **Copy JSON**. The full JSON snapshot is copied to the clipboard.
3. To save the JSON to a file, click **Export JSON...** and choose a save location in the file dialog that opens.
4. Watch the status label at the bottom of the dialog. It confirms the result of the last copy or export action (for example, "Copied to clipboard").
5. Click **Close** when finished.

## Refreshing the snapshot

If you changed slice state after opening the dialog, click **Refresh Snapshot** to re-read current slice state.

## What each control does

| Control              | Kind       | Behavior                                                                                                                                                                                                                                        |
|----------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Issue Summary**    | Tab        | Displays a plain-language bullet list of detected problems, including audio routing, DSP, control-device (MIDI) state, multi-client ownership issues, audio renderer endpoint issues, and panadapter slice connection status.                   |
| **JSON**             | Tab        | Displays the full JSON snapshot (schema version 3) of slices, DAX channels, audio devices, client DSP state, control devices, TX band settings, remote audio RX stream state, audio renderer endpoints, and panadapter slice connection status. |
| **Refresh Snapshot** | Button     | Re-reads current slice state from the radio and updates both tabs.                                                                                                                                                                              |
| **Copy Summary**     | Button     | Copies the issue summary text to the clipboard.                                                                                                                                                                                                 |
| **Copy JSON**        | Button     | Copies the full JSON snapshot to the clipboard.                                                                                                                                                                                                 |
| **Export JSON...**   | Button     | Opens a save dialog to write the JSON snapshot to a file.                                                                                                                                                                                       |
| **Close**            | Button     | Closes the dialog.                                                                                                                                                                                                                              |
| Status label         | Indicator  | Shows the result of the last copy or export action (for example, "Copied to clipboard") or the search match count.                                                                                                                              |
| **Find:**            | Text field | Highlights matching occurrences of the entered term in the active tab (Issue Summary or JSON). Has clear button and placeholder "Search snapshot...". Enter jumps to the next match; tab sharing updates highlight counts.                         |
| **Find Next**        | Button     | Jumps to the next match of the search term in the active tab. Wraps within the current tab. Empty term produces no matches.                                                                                                                      |

## What the Issue Summary includes

The Issue Summary tab reports problems across several areas:

- **Radio-level remote audio RX** — Reports the stream ID, whether the stream is expected, whether creation is pending, whether a status message has been seen, whether the stream is owned by this client, the compression setting in use, and any routing note that explains why the stream is or is not active.
- **Per-slice radio stream route** — Reports the remote audio RX stream ID for the slice's RX route alongside flags for whether the stream is expected, creation is pending, removal has been requested, a status message has been seen, and whether the stream is owned by this client.
- **Audio renderer endpoints** — For each audio endpoint, reports the direction, kind, backend, device name, sample rate, channel count, sample format, resampling status, buffer bytes, buffer peak, underrun count, any operational or error state, and any additional notes.
- **Panadapter slice connection status** — For each panadapter, reports the connection state summary, which slice IDs are connected, which are active, and whether attention is required.
- **TX meters freshness** — When TX meter data is not live, the summary flags this with a caveat: TX forward power is the last smoothed value received rather than a current reading, and TX SWR is omitted rather than shown stale. The message shows the age of the last sample when available.

## What the JSON includes

The JSON snapshot includes all data from the Issue Summary plus detail for troubleshooting. From v26.6.1, the snapshot also includes:

- **Audio renderer endpoints** — Each endpoint's full configuration: name, direction, kind, backend, device, sample rate, channel count, sample format, resampling status, buffer statistics, operational and running flags, state, error, and notes.
- **Panadapter slice connection status** — For each panadapter, the `slice_connection_status` object containing the state, summary, connected slice IDs, active slice IDs, and attention required flag.
- **NR2 DSP configuration** — The full NR2 noise reduction settings including the `gain_floor` field alongside the existing `ae_filter`, `gain_method`, `gain_max`, `gain_smooth`, `npe_method`, and `qspp` fields.

From v26.8.4, the snapshot also includes:

- **Audio endpoint resampling details** — For audio endpoints that include voice input or resampling configuration, additional fields report voice input normalization to 48 kHz, voice egress resampling to 24 kHz, and RADE resampling to 24 kHz flags.
- **TX meter freshness** — The snapshot includes `tx_meters_fresh` and `tx_meters_age_ms` fields to indicate whether TX meter data is current.

## Tips

- Take the snapshot before and after changing slice configuration if you are trying to isolate a problem. Use **Refresh Snapshot** between captures to update the data.
- If you are reporting a transverter problem, the **JSON** tab includes each transverter's RF frequency, IF frequency, offset, and validity flags. The **Issue Summary** tab will flag any transverters where validity cannot be confirmed.
- If you are reporting a remote audio problem, the **Issue Summary** tab now includes remote audio RX stream state at both the radio level and the per-slice level. Copy or export the snapshot and share it with support or paste it into an AI-assisted troubleshooting tool for analysis.
- If you suspect an audio endpoint issue, check the audio renderer endpoint entries in the Issue Summary for underruns, error states, or configuration mismatches. The JSON tab provides full detail for each endpoint.
- If a TX meter issue is suspected, the Issue Summary will flag when TX meters are not live and explain that TX forward power and SWR readings may be stale or omitted.
- The dialog remembers its position and size between sessions. If you need to reset it, close the dialog and delete the `SliceTroubleshootingDialogGeometry` setting from the configuration file.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)
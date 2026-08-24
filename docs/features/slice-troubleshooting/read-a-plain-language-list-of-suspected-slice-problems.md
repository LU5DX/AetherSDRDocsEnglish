# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog analyzes your current slice, panadapter, transverter, DAX channel, audio device, client DSP state, control-device (MIDI) binding state, audio endpoint state, and renderer (display) state and presents a plain-language summary of detected problems. Use this when you suspect a configuration issue — such as missing audio, a stuck mute, a missing antenna, an invalid transverter, a broken remote audio stream, or a rendering issue — and want a quick diagnosis without reading raw data.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...`.
2. Click the **Issue Summary** tab if it is not already selected.
3. Read the bullet list of detected problems.
4. If you have recently changed slice settings and want the list to reflect the current state, click **Refresh Snapshot**.

## What each control does

| Control              | Kind   | Behavior                                                                                                                                                                                        |
|----------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Issue Summary**    | Tab    | Displays a plain-language bullet list of detected problems, including audio routing, DSP, control-device (MIDI) state, audio endpoint state, renderer state, and multi-client ownership issues. |
| **JSON**             | Tab    | Displays the full JSON snapshot of slices, panadapters, DAX channels, audio devices, client DSP, control devices, audio endpoints, renderers, and TX band settings.                             |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Click this after changing slice settings.                                                                                                               |
| **Copy Summary**     | Button | Copies the issue summary text to the clipboard.                                                                                                                                                 |
| **Copy JSON**        | Button | Copies the full JSON snapshot to the clipboard.                                                                                                                                                 |
| **Export JSON...**   | Button | Saves the full JSON snapshot to a file.                                                                                                                                                         |
| **Find:**            | Text   | Highlights matching occurrences of the entered term in the active tab (Issue Summary or JSON). Has clear button and placeholder 'Search snapshot...'. Enter jumps to the next match; tab sharing updates highlight counts. Status label shows '<N> match(es) in current tab.' |
| **Find Next**        | Button | Jumps to the next match of the search term in the active tab. Wraps within the current tab. Empty term produces no matches.                                                                     |
| **Close**            | Button | Closes the dialog.                                                                                                                                                                              |

The status label below the buttons confirms the result of the last copy or export action (for example, "Copied to clipboard") or shows the search match count.

## What the Issue Summary reports

The Issue Summary bullet list covers the following areas:

- **Audio outputs** — headphone gain and mute, front speaker mute.
- **Remote audio RX** — stream ID, whether the stream is expected, whether creation is pending, whether a status packet has been seen, whether this client owns the stream, and the compression setting. A separate routing note line explains any unusual routing condition detected for the remote audio RX stream.
- **Oscillator** — current setting, lock state, external reference, and TCXO presence.
- **Radio stream route** — the remote audio RX stream ID used by the current RX route, together with the expected, create-pending, remove-requested, status-seen, and owned-by-us flags for that stream.
- **TX input route** — input selection, mic and DAX sub-selections, PC mic gain, TX stream ID, DAX TX mode, and DAX radio route.
- **TX meters** — A warning line is emitted when the TX meters are not live. When TX forward power holds its last smoothed value while TX SWR correctly reads n/a, the warning makes clear that the displayed power is the last value received, not a current reading, and that TX SWR is omitted rather than shown stale. The warning includes the age of the last sample (for example, "last sample 1234 ms ago") or notes that no TX meter sample has been received this session.
- **Panadapters** — for each panadapter: ID, active status, center frequency, bandwidth, RF gain, preamp, WNB active/level, waterfall ID, and slice connection status (state, summary, connected slice IDs, active slice IDs, attention required flag).
- **Audio endpoints** — for each audio endpoint: name, direction, kind, operational and running status, state, error, backend, device, sample rate, channel count, sample format, resampling status, voice input normalization to 48 kHz status, voice egress resampling to 24 kHz status, RADE resampling to 24 kHz status, buffer bytes, buffer peak bytes, underrun count, and any notes.
- **Renderers (display engine)** — for each renderer: operational status, backend, device, state, error, sample rate, buffer info, and underrun metrics.

## What the JSON snapshot includes

The JSON tab shows the full diagnostic snapshot. In addition to the areas listed above, the snapshot includes the following client DSP configuration parameters:

- **NR2 settings**: gain method, NPE method, AE filter, gain max, gain floor, gain smooth, and QSPP.
- **NR4 settings**: enabled status and noise estimation method.
- **Audio endpoints**: voice input normalization to 48 kHz status, voice egress resampling to 24 kHz status, and RADE resampling to 24 kHz status for each endpoint.

## Tips

- Click **Refresh Snapshot** after making any slice, antenna, DAX, audio routing, panadapter, or renderer changes before sharing or re-reading the summary. The snapshot is not updated automatically.
- If a remote audio RX stream is listed as pending or not owned by this client, click **Refresh Snapshot** after a few seconds to check whether the stream has been established.
- If you need to send the details to support, use **Copy Summary** to paste the plain-language list into an email or forum post, or use **Export JSON...** to attach the full snapshot as a file.
- When the Issue Summary shows a warning that TX meters are not live, treat the displayed TX forward power as a stale reading, not a current measurement, and check your antenna and TX settings separately.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)
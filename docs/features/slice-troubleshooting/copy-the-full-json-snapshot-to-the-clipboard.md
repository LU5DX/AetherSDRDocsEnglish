# Slice Troubleshooting

The Slice Troubleshooting dialog captures a JSON snapshot (schema v3) of every slice, panadapter, transverter, DAX channel, audio device, client DSP state, audio endpoint, control-device (MIDI) bindings, and renderer state, and summarizes likely problems (missing audio, stuck mute, missing antenna, XVTR validity) in plain language. This page explains how to capture and share that snapshot for support.

## Before you start

- AetherSDR must be connected to a radio. The dialog requires an active radio connection.
- If slice state has changed since you last opened the dialog, click `Refresh Snapshot` before copying to ensure the data is current.

## Steps

1. Open `Help > Slice Troubleshooting...`.
2. Review the `Issue Summary` tab for a plain-language list of detected problems, or click the `JSON` tab to view the full snapshot.
3. Click `Copy Summary` to copy the issue summary to the clipboard, or `Copy JSON` to copy the full JSON snapshot.
4. Confirm the status label reads `Copied to clipboard`.
5. Paste into your target application.

## What each control does

| Control                | Kind       | Behavior                                                                                                                        |
|------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| `Issue Summary` (tab)  | Tab        | Displays a plain-language bullet list of detected problems.                                                                     |
| `JSON` (tab)           | Tab        | Displays the full JSON snapshot (schema v3) of slices, DAX channels, audio devices, client DSP state, control devices, audio endpoints, and renderer state. |
| `Refresh Snapshot`     | Button     | Re-reads current slice state into the snapshot. Click this after making any slice changes before copying.                      |
| `Copy Summary`         | Button     | Copies the issue summary text to the clipboard.                                                                                 |
| `Copy JSON`            | Button     | Copies the full JSON snapshot to the clipboard.                                                                                 |
| `Export JSON...`       | Button     | Saves the JSON snapshot to a file.                                                                                              |
| `Find:`                | Text field | Highlights matching occurrences of the entered term in the active tab (Issue Summary or JSON). Has clear button and placeholder 'Search snapshot...'. Enter jumps to the next match; tab sharing updates highlight counts. Status label shows '<N> match(es) in current tab.' |
| `Find Next`            | Button     | Jumps to the next match of the search term in the active tab. Wraps within the current tab. Empty term produces no matches.     |
| `Close`                | Button     | Closes the dialog.                                                                                                              |v

## What the Issue Summary includes

The `Issue Summary` tab generates a plain-language bullet list from the snapshot. As of v26.8.4 the summary includes the following:

### TX meter freshness

The summary now reports whether TX meters are live. If the TX meter sample is stale, the summary shows:

- A warning that TX meters are NOT live, with the age of the last sample (or a note that no TX meter sample has been received this session).
- An explanation that TX forward power shown is the last value received, not a current reading, and that TX SWR is omitted rather than shown stale.

This prevents misdiagnosis where a plausible wattage next to a missing SWR could lead a reader to conclude the antenna is the problem.

### Audio endpoint status

For each audio endpoint, the summary reports:

- Name, direction (INPUT/OUTPUT), kind, operational flag, running flag, state, error, backend, device name, sample rate, channel count, sample format, resampling flag, and buffer statistics (buffer bytes, buffer peak bytes, underrun count).
- When applicable, voice input normalization to 48 kHz, voice egress resampling to 24 kHz, and RADE resampling to 24 kHz flags.
- Any user-facing note.

### Remote audio RX (radio-level)

The summary reports the radio-level remote audio RX stream state, including:

- Stream ID, whether the stream was expected, whether creation is pending, whether a status message has been seen, whether this client owns the stream, and the compression setting in use.
- A routing note that explains any detected routing problem for the remote audio RX stream.

### Remote audio RX (per-slice radio stream route)

For each slice, the summary also reports the per-slice radio stream route for remote audio RX, including:

- Stream ID, expected flag, create-pending flag, remove-requested flag, status-seen flag, and owned-by-us flag.

### Panadapter slice connection status

For each panadapter, the summary reports its connection status to slices, including:

- State (e.g. "connected", "partially_connected"), summary of connection status, list of connected slice IDs, list of active slice IDs, and whether the connection requires attention.

### Client DSP NR2 settings

The summary includes the full NR2 noise reduction configuration read from the `Nr2SettingsModel`, including:

- Gain method and method name, NPE method and method name, AE filter enabled/disabled, gain max, gain floor, gain smooth, and Qspp.

## Tips

- Use the `Find:` field to search for specific terms within the active tab. The status label shows the match count, and `Find Next` jumps to the next occurrence (wrapping within the current tab).
- If you want only a plain-language problem summary rather than the full JSON, use `Copy Summary` on the `Issue Summary` tab instead.
- To get the most accurate snapshot, make any slice configuration changes first, then click `Refresh Snapshot`, then `Copy JSON`.
- The JSON snapshot can be pasted directly into an AI assistant for guided troubleshooting.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
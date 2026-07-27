# Slice Troubleshooting

The Slice Troubleshooting dialog captures a snapshot of every slice, panadapter, transverter, DAX channel, audio device, client DSP state, and control-device (MIDI) bindings on the connected radio and checks for likely configuration problems. Use it to diagnose audio, mute, antenna, transverter, and remote audio routing issues, or to collect diagnostic data before contacting support.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The dialog is not available without an active radio connection.

## How it works

Open the dialog with `Help > Slice Troubleshooting...`. When the dialog opens, AetherSDR reads the current radio state into a snapshot. The snapshot covers slices, panadapters, transverters, DAX channels, audio devices, client DSP state, control-device (MIDI) bindings, TX band settings, and audio endpoint state. The dialog checks that snapshot for a set of known problem patterns — missing audio, stuck mute, missing antenna, transverter validity issues, audio routing problems, DSP state anomalies, and multi-client ownership conflicts — and presents the results in two tabs.

**Issue Summary tab** shows a plain-language bullet list of detected problems. If nothing is wrong, the list is empty. This is the fastest way to see whether AetherSDR has identified a configuration issue.

The Issue Summary includes remote audio RX diagnostics. For the radio-level audio section, the summary reports the remote audio RX stream ID, whether a stream is expected, whether creation is pending, whether a status message has been seen, whether the stream is owned by the current client, the compression setting in use, and any routing note. For the per-slice audio routing section, the summary reports the remote audio RX stream ID alongside expected, create-pending, remove-requested, status-seen, and owned-by-us flags.

The Issue Summary also includes detailed audio endpoint diagnostics showing each endpoint's operational state, running state, backend, device name, sample rate, channel count, sample format, resampling status, buffer metrics, and any error or note.

**JSON tab** shows the full snapshot as structured JSON (schema version 3). This view contains every field AetherSDR collected: slice state, panadapter parameters, transverter RF/IF frequencies, offsets, validity flags, DAX channel assignments, audio devices, client DSP state, control-device bindings, TX band settings, remote audio RX state, and audio endpoint details. Support staff and advanced users can inspect individual field values here.

The snapshot reflects radio state at the moment it was taken. If you change slice settings while the dialog is open, click **Refresh Snapshot** to re-read the current state before drawing conclusions or sharing data.

The dialog remembers its window position and size between sessions. It will reopen in the same location where you last closed it.

## What each control does

| Control          | Kind      | Behavior                                                                                        |
|------------------|-----------|-------------------------------------------------------------------------------------------------|
| Issue Summary    | Tab       | Displays a plain-language bullet list of detected problems, including audio routing, DSP, control-device (MIDI) state, multi-client ownership, and audio endpoint diagnostics. |
| JSON             | Tab       | Displays the full JSON snapshot (schema version 3) of slices, DAX channels, audio devices, client DSP, control devices, TX band settings, remote audio RX state, and audio endpoints. |
| Refresh Snapshot | Button    | Re-reads slice state into the snapshot. Use this after changing radio configuration.            |
| Copy Summary     | Button    | Copies the issue summary text to the clipboard.                                                 |
| Copy JSON        | Button    | Copies the full JSON snapshot to the clipboard.                                                 |
| Export JSON...   | Button    | Opens a file dialog to save the JSON snapshot to a file.                                        |
| Close            | Button    | Closes the dialog.                                                                              |
| Status label     | Indicator | Shows the result of the most recent copy or export action (for example, "Copied to clipboard"). |

## Tips

- Take a new snapshot with **Refresh Snapshot** after every configuration change. The dialog does not update automatically while it is open.
- Use **Copy Summary** to paste a concise problem list into a support forum post or email. Use **Copy JSON** or **Export JSON...** when attaching full diagnostic data to a bug report.
- If you are troubleshooting remote audio, check both the radio-level remote audio RX section and the per-slice radio stream route section in the Issue Summary. Both sections must show consistent stream IDs and ownership flags for audio to route correctly.
- When investigating audio problems, review the audio endpoint diagnostics in the Issue Summary. Non-operational endpoints, high underrun counts, or error messages indicate audio backend considerations.

## Related

- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Copy the full JSON snapshot to the clipboard](copy-the-full-json-snapshot-to-the-clipboard.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)
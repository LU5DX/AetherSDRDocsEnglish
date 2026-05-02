The diff shows internal C++ refactoring only (moving a variable declaration earlier in `buildAudioDevicesSnapshot`, resetting meter model fields in `setTgxlHandle`). The user-visible output of the Issue Summary and JSON tabs — including the remote audio RX fields — is already fully documented in the current page. No user-facing behavior has changed.

# Read a plain-language list of suspected slice problems

The Slice Troubleshooting dialog analyzes your current slice, panadapter, transverter, DAX channel, audio device, client DSP state, and control-device (MIDI) binding state and presents a plain-language summary of detected problems. Use this when you suspect a configuration issue — such as missing audio, a stuck mute, a missing antenna, an invalid transverter, or a broken remote audio stream — and want a quick diagnosis without reading raw data.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio. The dialog requires an active radio connection.

## Steps

1. Click `Help > Slice Troubleshooting...`.
2. Click the **Issue Summary** tab if it is not already selected.
3. Read the bullet list of detected problems.
4. If you have recently changed slice settings and want the list to reflect the current state, click **Refresh Snapshot**.

## What each control does

| Control              | Kind   | Behavior                                                                                                                                                                                                              |
|----------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Issue Summary**    | Tab    | Displays a plain-language bullet list of detected problems, including audio routing, DSP, control-device (MIDI) state, and multi-client ownership issues.                                                             |
| **JSON**             | Tab    | Displays the full JSON snapshot (schema version 3) of slices, DAX channels, audio devices, client DSP, control devices, and TX band settings.                                                                        |
| **Refresh Snapshot** | Button | Re-reads slice state into the snapshot. Click this after changing slice settings.                                                                                                                                     |
| **Copy Summary**     | Button | Copies the issue summary text to the clipboard.                                                                                                                                                                       |
| **Copy JSON**        | Button | Copies the full JSON snapshot to the clipboard.                                                                                                                                                                       |
| **Export JSON...**   | Button | Saves the full JSON snapshot to a file.                                                                                                                                                                               |
| **Close**            | Button | Closes the dialog.                                                                                                                                                                                                    |

The status label below the buttons confirms the result of the last copy or export action (for example, `Copied to clipboard`).

## What the Issue Summary reports

The Issue Summary bullet list covers the following areas:

- **Audio outputs** — headphone gain and mute, front speaker mute.
- **Remote audio RX** — stream ID, whether the stream is expected, whether creation is pending, whether a status packet has been seen, whether this client owns the stream, and the compression setting. A separate routing note line explains any unusual routing condition detected for the remote audio RX stream.
- **Oscillator** — current setting, lock state, external reference, and TCXO presence.
- **Radio stream route** — the remote audio RX stream ID used by the current RX route, together with the expected, create-pending, remove-requested, status-seen, and owned-by-us flags for that stream.
- **TX input route** — input selection, mic and DAX sub-selections, PC mic gain, TX stream ID, DAX TX mode, and DAX radio route.

## Tips

- Click **Refresh Snapshot** after making any slice, antenna, DAX, or audio routing changes before sharing or re-reading the summary. The snapshot is not updated automatically.
- If a remote audio RX stream is listed as pending or not owned by this client, click **Refresh Snapshot** after a few seconds to check whether the stream has been established.
- If you need to send the details to support, use **Copy Summary** to paste the plain-language list into an email or forum post, or use **Export JSON...** to attach the full snapshot as a file.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Capture a slice snapshot for support](capture-a-slice-snapshot-for-support.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
- [Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis](inspect-each-transverter-s-rf-if-offset-and-validity-flags-for-xvtr-diagnosis.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-02 -->

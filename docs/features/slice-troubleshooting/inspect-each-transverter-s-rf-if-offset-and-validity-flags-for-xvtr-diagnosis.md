# Inspect each transverter's RF/IF, offset and validity flags for XVTR diagnosis

The Slice Troubleshooting dialog captures a snapshot of every transverter configured on your FLEX-8600 and displays its RF frequency, IF frequency, frequency offset, and validity flags. Use this when a transverter-based slice is misbehaving — wrong frequency, missing reception, or unexpected mode — and you need to confirm what the radio actually reports for each XVTR entry.

## Before you start

- AetherSDR must be connected to the radio. The dialog requires an active radio connection.
- Any transverters you want to inspect must already be configured on the FLEX-8600.

## Steps

1. Click `Help > Slice Troubleshooting...` to open the Slice Troubleshooting dialog.
2. Click the `Issue Summary` tab. Scan the bullet list for any XVTR validity warnings. The summary flags entries where `is_valid` is false or `has_is_valid` is false.
3. Click the `JSON` tab to see the full snapshot. Locate the transverter entries in the JSON. Each XVTR entry reports the following fields:
   - `name` — the label assigned to the transverter
   - `index` and `order` — position identifiers
   - `rf_freq_mhz` — the RF (over-the-air) frequency in MHz
   - `if_freq_mhz` — the IF (radio input) frequency in MHz
   - `offset_mhz` — the difference applied between IF and RF, in MHz
   - `is_valid` — whether the transverter entry is marked valid (`Yes` / `No`)
   - `has_is_valid` — whether the radio reported a validity flag at all (`Yes` / `No`)
   - `rx_only` — whether the entry is receive-only
   - `max_power` — maximum power in the XVTR entry
4. If you made changes to transverter settings after opening the dialog, click `Refresh Snapshot` to re-read the current state from the radio before drawing any conclusions.
5. To share the findings, click `Copy Summary` to copy the plain-language issue list to the clipboard, `Copy JSON` to copy the full JSON, or `Export JSON...` to save the JSON to a file.
6. Click `Close` when finished.

## What each control does

| Control             | Kind   | Behavior                                                                                        |
|---------------------|--------|-------------------------------------------------------------------------------------------------|
| `Issue Summary` tab | Tab    | Plain-language bullet list of detected problems, including audio routing, DSP, control-device (MIDI) state, multi-client ownership, and XVTR validity issues. |
| `JSON` tab          | Tab    | Full JSON snapshot (schema version 3) containing slices, DAX channels, audio devices, client DSP, control devices, TX band settings, and all transverter entries with RF, IF, offset, and validity fields. |
| `Refresh Snapshot`  | Button | Re-reads slice state into the snapshot.                                                         |
| `Copy Summary`      | Button | Copies the issue summary to the clipboard.                                                      |
| `Copy JSON`         | Button | Copies the full JSON snapshot to the clipboard.                                                 |
| `Export JSON...`    | Button | Saves the full JSON snapshot to a file.                                                         |
| `Close`             | Button | Closes the dialog.                                                                              |

## Remote audio RX fields in the snapshot

v0.9.4 adds remote audio RX state to both the radio-level and per-slice sections of the Issue Summary and JSON snapshot. These fields help diagnose problems where AetherSDR has requested a remote audio stream from the radio but audio is not flowing.

### Radio-level remote audio RX

In the Issue Summary, look for the line beginning **Remote audio RX:**. It reports the following:

| Field              | Meaning                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `stream_id`        | The stream identifier assigned by the radio, or `—` if none.           |
| `stream_expected`  | Whether AetherSDR expects this stream to exist (`Yes` / `No`).         |
| `create_pending`   | Whether a create request is still outstanding (`Yes` / `No`).          |
| `status_seen`      | Whether a status update for this stream has been received (`Yes` / `No`). |
| `owned_by_us`      | Whether this client owns the stream (`Yes` / `No`).                    |
| `compression`      | The compression type in use, or `—` if not reported.                   |

A second line, **Remote audio route note:**, contains a plain-language note about the routing state, or `—` if none was generated.

### Per-slice radio stream route

In the Issue Summary, look for the line beginning **Radio stream route: remote_audio_rx**. It reports the following:

| Field                              | Meaning                                                                   |
|------------------------------------|---------------------------------------------------------------------------|
| `remote_audio_rx_stream_id`        | The stream identifier for this slice's remote audio RX, or `—` if none.  |
| `remote_audio_rx_expected`         | Whether the stream is expected to exist.                                  |
| `remote_audio_rx_create_pending`   | Whether a create request is still outstanding.                            |
| `remote_audio_rx_remove_requested` | Whether a remove request has been sent but not yet confirmed.             |
| `remote_audio_rx_status_seen`      | Whether a status update for this stream has been received.                |
| `remote_audio_rx_owned_by_us`      | Whether this client owns the stream.                                      |

If `remote_audio_rx_expected` is true but `remote_audio_rx_status_seen` is false, the radio has not yet confirmed the stream. If `create_pending` is true for an extended period, the create request may not have reached the radio.

## Tips

- If `has_is_valid` is `No` for a transverter, the radio did not report a validity flag for that entry at all. This is distinct from `is_valid` being `No`, which means the radio reported the entry as explicitly invalid.
- Click `Refresh Snapshot` after adjusting transverter settings in SmartSDR or on the radio before re-reading the values. The snapshot is not updated automatically.
- The `offset_mhz` field should equal `rf_freq_mhz` minus `if_freq_mhz`. If it does not match your transverter configuration, that discrepancy is a likely cause of frequency errors on the slice.
- When investigating missing audio, check the remote audio RX fields first. If `owned_by_us` is `No` and `stream_expected` is `Yes`, another client may have taken ownership of the stream.

## Related

- [Slice Troubleshooting overview](overview.md)
- [Read a plain-language list of suspected slice problems](read-a-plain-language-list-of-suspected-slice-problems.md)
- [Refresh the snapshot after changing slice state](refresh-the-snapshot-after-changing-slice-state.md)
- [Export the snapshot to a file to attach to a bug report](export-the-snapshot-to-a-file-to-attach-to-a-bug-report.md)
<!-- docmesh:llm version=v0.9.4 date=2026-05-02 -->

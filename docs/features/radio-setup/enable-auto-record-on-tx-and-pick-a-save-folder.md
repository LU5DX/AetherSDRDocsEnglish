# Enable auto-record on TX and pick a save folder

When auto-record on TX is enabled, AetherSDR starts recording audio automatically each time you transmit and stops after a configurable idle timeout. This page explains how to turn that feature on and choose where recordings are saved.

## Before you start

- The radio must be connected. Radio Setup requires an active radio connection.
- Decide whether you want radio-side or client-side recording, as this affects where audio is captured.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Recording:**, click either **Radio Side** or **Client Side** to select where audio is captured. The active selection is highlighted. This choice is saved to `RecordMode`.
4. In the **Save to:** field, type the full path to your recordings folder, or click **...** to browse for a folder. The path is saved to `RecordDir`.
5. Check the **Auto-record on TX** checkbox. This enables automatic recording whenever the radio transitions to transmit. The setting is saved to `AutoRecordTx`.
6. Set **Idle timeout:** to the number of seconds of silence after which the recording stops. The value is saved to `RecordIdleTimeout`.
7. Close the dialog. Settings take effect immediately.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Recording: Radio Side / Client Side** | Selects whether audio is captured at the radio or at this PC. | — | Radio Side \| Client Side | `RecordMode` |
| **Save to:** | Folder path where recording files are written. | — | Any valid directory path | `RecordDir` |
| **...** | Opens a folder browser to select the save location. | — | — | — |
| **Auto-record on TX** | When checked, recording starts automatically on each transmit and stops after the idle timeout elapses. | — | Checked \| Unchecked | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence before the recording stops after TX ends. | — | — | `RecordIdleTimeout` |

## Tips

- If you use SmartLink or a VPN, consider whether **Radio Side** or **Client Side** better matches where you want the files stored. Radio-side recordings stay on the FLEX-8600; client-side recordings go to the folder set in **Save to:**.
- Set **Idle timeout:** to a low value (a few seconds) if you want each transmission captured as a separate file. A higher value merges pauses within a QSO into one file.

## Troubleshooting

- **No files appear in the save folder after transmitting** — Confirm **Auto-record on TX** is checked and that the path in **Save to:** exists and is writable. If the folder does not exist, AetherSDR cannot create the file.
- **Save to: field shows no path** — Click **...** and select a folder explicitly. Leaving the field empty may prevent recording from starting.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)

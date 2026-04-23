# Enable auto-record on TX and pick a save folder

AetherSDR can automatically start recording audio whenever you transmit and stop after a configurable period of silence. This page explains how to turn on that feature and choose where recordings are saved.

## Before you start

- AetherSDR must be connected to the radio. Radio Setup requires an active radio connection.
- Decide whether you want recordings made on the radio side or the client (PC) side before you begin.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Recording:**, click either **Radio Side** or **Client Side** to select where audio is captured. This sets `RecordMode`.
4. In the **Save to:** field, type a folder path directly, or click **...** to open a folder browser. The chosen path is saved as `RecordDir`.
5. Check **Auto-record on TX**. This sets `AutoRecordTx` and enables automatic recording whenever the radio keys up.
6. Set **Idle timeout:** to the number of seconds of silence after which the recording stops. This sets `RecordIdleTimeout`.
7. Click **Close**.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Recording: Radio Side / Client Side** | Selects whether audio is captured on the radio or on this PC. | — | Radio Side, Client Side | `RecordMode` |
| **Save to:** | Folder path where recording files are written. | — | Any writable path | `RecordDir` |
| **...** | Opens a folder-browser dialog to pick the save folder. | — | — | — |
| **Auto-record on TX** | When checked, recording starts automatically each time the radio transmits. | — | Checked / unchecked | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence before the active recording is closed. | — | — | `RecordIdleTimeout` |

## Tips

- The **...** button opens a standard folder-browser dialog. If you prefer to type a path, click in **Save to:** and edit it directly.
- Radio Side recording uses the radio's own audio path. Client Side recording captures the audio stream as it arrives at the PC. Choose Client Side if you are operating remotely over SmartLink and want to record what you actually hear.
- Setting **Idle timeout:** to a low value produces many short files if you have frequent brief transmissions. Set it higher to merge a contest exchange or a CW pileup into one file.

## Troubleshooting

- **Recordings are not created after transmitting** — Confirm **Auto-record on TX** is checked and that the path in **Save to:** exists and is writable by the user running AetherSDR. If the folder does not exist, create it first.
- **Save to: field is blank after reopening the dialog** — The path is stored in `RecordDir`. If no folder was ever selected, the field will be empty. Click **...** and choose a folder, then close the dialog to persist the setting.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)

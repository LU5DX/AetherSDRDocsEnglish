# Enable auto-record on TX and pick a save folder

Use this page to configure AetherSDR to start recording automatically whenever you transmit, and to choose where those recordings are saved.

## Before you start

- AetherSDR must be connected to the radio. Recording settings are not available until a connection is established.
- Decide whether you want the radio itself or your PC to handle the recording. See "What each control does" below for the difference.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Recording:**, click either **Radio Side** or **Client Side** to select where audio is captured. The active selection is highlighted.
4. In the **Save to:** field, type the full path to the folder where recordings should be saved, or click **...** to open a folder browser and select it.
5. Check **Auto-record on TX**. Recording will now start automatically each time you key the transmitter.
6. Set **Idle timeout:** to the number of seconds of silence after which the recording stops automatically.
7. Close the dialog. Settings are saved immediately.

## What each control does

| Control | What it does | Default | Valid range / values | Setting key |
|---|---|---|---|---|
| **Recording: Radio Side / Client Side** | Selects whether audio is captured on the radio hardware or on the PC running AetherSDR. | — | Radio Side, Client Side | `RecordMode` |
| **Save to:** | Folder path where recording files are written. | — | Any writable directory path | `RecordDir` |
| **...** | Opens a folder browser to select the save folder. | — | — | — |
| **Auto-record on TX** | When checked, recording starts automatically whenever the radio transmits and stops after the idle timeout expires. | — | Checked / unchecked | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence after TX ends before the recording file is closed. | — | — | `RecordIdleTimeout` |

## Tips

- If you leave **Save to:** empty, click **...** to browse to a folder rather than typing a path, to avoid typos that would silently prevent files from being written.
- **Idle timeout:** keeps short unkeyed pauses within a single file rather than splitting each transmission into a separate recording. Increase it if you want exchanges in a QSO captured together.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)

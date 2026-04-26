# Enable auto-record on TX and pick a save folder

AetherSDR can automatically start recording audio whenever you transmit and stop after a configurable period of silence. This page explains how to turn that feature on and set the folder where recordings are saved.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab in Radio Setup is not available without a radio connection.
- Decide whether you want recording to happen on the radio itself or on the PC running AetherSDR. You will need to set this before enabling auto-record.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Recording:**, click **Radio Side** or **Client Side** to select where recordings are captured. This sets `RecordMode`.
4. In the **Save to:** field, type a folder path directly, or click **...** to browse for a folder. The chosen path is saved as `RecordDir`.
5. Check **Auto-record on TX**. This sets `AutoRecordTx` and enables automatic recording whenever the radio transitions to transmit.
6. Adjust **Idle timeout:** to the number of seconds of silence after which the recording stops. This sets `RecordIdleTimeout`.
7. Close the dialog. Settings are saved immediately.

## What each control does

| Control | Behavior | Persisted key | Default | Valid range |
|---|---|---|---|---|
| **Recording: Radio Side / Client Side** | Selects whether audio is captured on the radio or on the PC. | `RecordMode` | — | Radio Side, Client Side |
| **Save to:** | Folder path where recording files are written. | `RecordDir` | — | Any valid directory path |
| **...** | Opens a folder browser to select the recording destination. | — | — | — |
| **Auto-record on TX** | When checked, recording starts automatically each time you transmit. | `AutoRecordTx` | — | Checked / unchecked |
| **Idle timeout:** | Seconds of post-TX silence before the recording file is closed. | `RecordIdleTimeout` | — | — |

## Tips

- If you want recordings separated per transmission rather than merged into one long file, keep **Idle timeout:** short so the file closes soon after you unkey.
- The **Save to:** path must exist and be writable before recording begins. AetherSDR does not create the directory automatically.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)

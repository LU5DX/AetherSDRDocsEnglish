# Enable auto-record on TX and pick a save folder

This page explains how to configure AetherSDR to start recording automatically whenever you transmit, and how to choose where those recordings are saved. This is useful for logging your transmissions without manually starting and stopping a recorder.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab in Radio Setup is not accessible without an active radio connection.
- Decide whether you want radio-side or client-side recording before you begin, as the recording mode affects where audio is captured.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. In the **Recording:** control, click **Radio Side** or **Client Side** to select where audio is captured. The currently active mode appears highlighted. This persists as `RecordMode`.
4. In the **Save to:** field, review the current folder path. To change it, click **...** next to the field and choose a folder in the file browser. The chosen path persists as `RecordDir`.
5. Check **Auto-record on TX**. When checked, AetherSDR begins recording each time the radio keys up and stops when transmission ends (subject to the idle timeout). This persists as `AutoRecordTx`.
6. Set **Idle timeout:** to the number of seconds of silence after which the recording stops. This persists as `RecordIdleTimeout`.
7. Close the dialog. Settings take effect immediately.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Recording: Radio Side / Client Side** | Selects whether audio is captured on the radio or on the PC running AetherSDR. | — | Radio Side \| Client Side | `RecordMode` |
| **Save to:** | Folder path where recording files are written. | — | Any valid directory path | `RecordDir` |
| **...** | Opens a folder browser to select the save directory. | — | — | — |
| **Auto-record on TX** | When checked, recording starts automatically on transmit and stops when idle. | — | Checked \| Unchecked | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence after transmit ends before the recording file is closed. | — | — | `RecordIdleTimeout` |

## Tips

- If you use SmartLink or a VPN, consider whether radio-side or client-side recording better captures the audio you want. Radio-side recording captures what the radio processes; client-side recording captures what reaches the PC.
- Set **Idle timeout:** to a value long enough to bridge brief pauses in your transmission (such as between over-and-out exchanges) without creating a new file for each key-up.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)

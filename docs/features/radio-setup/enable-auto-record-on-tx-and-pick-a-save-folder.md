# Enable auto-record on TX and pick a save folder

AetherSDR can start recording automatically whenever you transmit and stop after a configurable period of silence. This page shows how to turn on that feature and choose where recordings are saved.

## Before you start

- AetherSDR must be connected to the radio. Recording settings are in the Radio Setup dialog, which requires an active radio connection.
- Decide whether you want recordings made on the radio itself or on the PC running AetherSDR (see "Recording: Radio Side / Client Side" below).

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. In the **Recording:** row, click **Radio Side** or **Client Side** to choose where audio is captured. This sets `RecordMode`.
4. In the **Save to:** field, type a folder path directly, or click **...** to open a folder browser. The chosen path is saved as `RecordDir`.
5. Check **Auto-record on TX**. This sets `AutoRecordTx` and activates automatic recording whenever the radio keys up.
6. Set **Idle timeout:** to the number of seconds of silence after which the recording stops. This sets `RecordIdleTimeout`.
7. Close the dialog with **Close**. Settings are persisted immediately.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Recording: Radio Side / Client Side** | Selects whether audio is captured at the radio or on the client PC. | — | Radio Side, Client Side | `RecordMode` |
| **Save to:** | Folder path where recording files are written. | — | Any writable path | `RecordDir` |
| **...** | Opens a folder browser to set **Save to:** without typing. | — | — | — |
| **Auto-record on TX** | Starts recording automatically when the radio transmits; stops when idle timeout expires. | — | On / Off | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence before the recording stops after TX ends. | — | — | `RecordIdleTimeout` |

## Tips

- If you select **Client Side** recording, the saved files go to the path in **Save to:** on the machine running AetherSDR. If you select **Radio Side**, confirm that the radio has storage available.
- Set **Idle timeout:** to a short value (a few seconds) to keep individual transmissions as separate files rather than merging several overs into one long file.

## Troubleshooting

- **Recordings are not created after enabling Auto-record on TX** — Verify that the path in **Save to:** exists and is writable. If the field is empty, click **...** and select a folder before enabling the feature.
- **The Save to: field is grayed out or the ... button does nothing** — The dialog requires an active radio connection. Confirm the radio is connected before opening `Settings > Radio Setup...`.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)

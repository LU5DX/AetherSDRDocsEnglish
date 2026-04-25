# Choose PC input/output audio devices

This page explains how to select which PC sound card or audio interface AetherSDR uses to play received audio and capture microphone input. You need to do this any time you add a new audio device or the default system device is not the one you want to use with the radio.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Audio tab is not accessible when no radio is connected.
- The audio devices you want to use must already be recognised by the operating system and appear in its device list.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **PC Audio Devices:** section. It contains two drop-down lists labelled **Input:** and **Output:**.
4. Click the **Output:** drop-down and select the device you want AetherSDR to use for received audio playback.
5. Click the **Input:** drop-down and select the device you want AetherSDR to use for microphone input when transmitting.

Your selections take effect immediately. No additional Apply step is required.

## What each control does

| Control | What it does | Default | Range / Values | Setting key |
|---|---|---|---|---|
| **PC Audio Devices: Input:** | Selects the host audio device used for microphone capture. | System default | All devices reported by the OS | — |
| **PC Audio Devices: Output:** | Selects the host audio device used for received audio playback. | System default | All devices reported by the OS | — |
| **Audio Boost:** | Applies extra gain on the client-side audio path. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Increases the client audio buffer to reduce dropouts over VPN or SmartLink. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |
| **Recording: Radio Side / Client Side** | Chooses whether recordings are captured at the radio or at the PC. | — | Radio Side / Client Side | `RecordMode` |
| **Save to:** | Folder path where recordings are saved. | — | Any writable directory | `RecordDir` |
| **...** | Opens a folder browser to choose the recording directory. | — | — | — |
| **Auto-record on TX** | Automatically starts recording whenever you transmit. | Off | Checked / Unchecked | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence after which an active recording stops automatically. | — | — | `RecordIdleTimeout` |

## Tips

- If your preferred device does not appear in the **Input:** or **Output:** drop-down, close the dialog, verify the OS recognises the device, then reopen `Settings > Radio Setup...` and check the **Audio** tab again. The device list is populated when the tab is first opened.
- If received audio sounds distorted at normal volume, enable **Audio Boost:** only after confirming your OS output level is not already near maximum.
- When operating over a VPN or SmartLink connection with choppy audio, increase **Audio Buffer:** in small increments (for example, 100 ms at a time) until dropouts stop.

## Troubleshooting

- **No audio heard on receive despite a device being selected** — Confirm the selected **Output:** device is not muted at the OS level. Also check that the radio's **Line Out:** slider and **Headphone:** slider on the same Audio tab are not set to zero or muted.
- **Input device list is empty or missing a device** — The list is built when the Audio tab is first displayed. Close and reopen `Settings > Radio Setup...` after connecting or enabling the device in the OS.
- **Audio cuts out over SmartLink** — Increase **Audio Buffer:** (valid range 50–1000 ms) and consider switching **Audio Compression (SmartLink):** from Auto to Opus.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)

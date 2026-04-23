# Choose PC input/output audio devices

Select which PC sound card or audio interface AetherSDR uses to play received audio and capture microphone audio. This is separate from the radio's own Line Out and Headphone outputs.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible without an active radio connection.
- Your audio interface must already be recognized by the operating system before opening this dialog.

## Steps

1. Go to `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **PC Audio Devices:**, click the **Input:** drop-down and select the device to use for microphone or audio input.
4. Click the **Output:** drop-down and select the device to use for received audio playback.
5. Close the dialog. The selection takes effect immediately.

## What each control does

| Control | Description | Default | Valid range / values | Setting key |
|---|---|---|---|---|
| **PC Audio Devices: Input:** | Selects the host OS audio input device (microphone, line in). | System default | Devices enumerated from OS | — |
| **PC Audio Devices: Output:** | Selects the host OS audio output device (speakers, headphones, audio interface). | System default | Devices enumerated from OS | — |
| **Audio Boost:** | Applies extra gain on the client audio path. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Increases the audio buffer depth to absorb jitter on VPN or SmartLink connections. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |
| **Recording: Radio Side / Client Side** | Chooses whether recording is performed on the radio or on this PC. | — | Radio Side / Client Side | `RecordMode` |
| **Save to:** | Folder path where recordings are saved. | — | Any writable directory | `RecordDir` |
| **...** | Opens a folder browser to choose the recording directory. | — | — | — |
| **Auto-record on TX** | Automatically starts recording when the radio transmits. | Off | On / Off | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence after which an active recording stops. | — | — | `RecordIdleTimeout` |

## Tips

- If your preferred device does not appear in the drop-down, confirm the OS recognizes it, then close and reopen the **Radio Setup** dialog. The Audio tab enumerates devices when it is first displayed.
- Use **Audio Buffer:** to reduce audio dropouts when operating over a VPN or slow network link. Higher values add latency; 50 ms suits local LAN, while 200–400 ms suits most remote setups.
- **Audio Boost:** is useful when the incoming audio level is low even at maximum slice volume.

## Troubleshooting

- **No audio devices appear in the Input or Output drop-downs** — The Audio tab defers device enumeration until it is opened. If the list is still empty, verify the OS audio subsystem is running and that at least one device is enabled in system sound settings.
- **Audio drops out during remote operation** — Increase **Audio Buffer:** (range 50–1000 ms) and consider switching **Audio Compression (SmartLink):** from Auto to Opus to reduce bandwidth requirements.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)

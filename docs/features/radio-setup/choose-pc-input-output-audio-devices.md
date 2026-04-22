# Choose PC input/output audio devices

Select which PC audio device receives the radio's received audio and which device captures your microphone input. You configure both on the Audio tab of Radio Setup.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible without an active radio connection.
- Ensure your PC audio devices (headset, microphone, speakers) are recognized by the operating system before opening this dialog.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **PC Audio Devices:**, click the **Input:** drop-down and select the device that will capture your transmitted audio (microphone or headset).
4. Click the **Output:** drop-down and select the device that will play received audio (speakers or headset).
5. Close the dialog. AetherSDR applies the selection immediately.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **PC Audio Devices: Input:** | Selects the PC audio input device (microphone/headset) used for transmit audio. | System default | Available host devices | — |
| **PC Audio Devices: Output:** | Selects the PC audio output device (speakers/headset) used for received audio playback. | System default | Available host devices | — |
| **Audio Boost:** | Applies extra gain to the client audio path. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Sets the client-side audio buffer size. Increase this to reduce dropouts over VPN or SmartLink. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink):** | Selects the audio codec used over SmartLink or LAN. Three options: Auto, Uncompressed, Opus. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |
| **Recording: Radio Side / Client Side** | Picks whether recordings are captured at the radio or at the PC client. | — | Radio Side / Client Side | `RecordMode` |
| **Save to:** | Folder path where recordings are saved. Click **...** to browse. | — | Any writable path | `RecordDir` |
| **Auto-record on TX** | Starts recording automatically whenever you transmit. | Off | On / Off | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence after which an auto-recording stops. | — | — | `RecordIdleTimeout` |

## Tips

- If your headset appears in both Input and Output drop-downs, select it in both to keep transmit and receive audio on the same device.
- If audio drops out during SmartLink or VPN sessions, increase **Audio Buffer:** before switching codecs. Valid range is 50–1000 ms.
- **Audio Boost:** adds gain on the client path only. If the radio-side audio level is already sufficient, leave it off to avoid clipping.

## Troubleshooting

- **No devices appear in the Input or Output drop-down** — The Audio tab defers hardware probing until first opened. If devices are still missing, confirm the OS recognizes the device (check system sound settings), then close and reopen Radio Setup.
- **Output audio is silent after selecting a device** — Verify the selected output device is not muted in the OS mixer. Also check the **Line Out:** and **Headphone:** sliders on the same Audio tab, and confirm neither is muted via the corresponding **Mute** button.
- **Input device produces no level during TX** — Confirm the correct Input device is selected. On Linux (PipeWire/PulseAudio), the device must not be claimed exclusively by another application.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)

# Choose PC input/output audio devices

Select which PC audio input and output devices AetherSDR uses to route received audio to your speakers or headphones and to capture microphone audio for transmit.

## Before you start

- AetherSDR must be connected to a FLEX-8600. The Audio tab is unavailable without a radio connection.
- The audio devices you want to use must already be recognized by your operating system before opening this dialog.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **PC Audio Devices:**, click the **Input:** drop-down and select the microphone or line-in device you want to use for transmit audio.
4. Click the **Output:** drop-down and select the speaker, headphone, or line-out device you want to use for received audio.
5. Click **Close**.

## What each control does

| Control | What it does | Default | Range / Options | Setting key |
|---|---|---|---|---|
| **PC Audio Devices: Input:** | Selects the host PC audio input device (microphone or line-in) used for TX audio. | System default | All devices reported by the OS | — |
| **PC Audio Devices: Output:** | Selects the host PC audio output device (speakers or headphones) used for RX audio. | System default | All devices reported by the OS | — |
| **Audio Boost:** | Applies extra gain on the client audio path. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Increases the audio buffer to reduce dropouts over VPN or SmartLink. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |
| **Recording: Radio Side / Client Side** | Selects whether recordings are captured at the radio or on this PC. | — | Radio Side / Client Side | `RecordMode` |
| **Save to:** | Folder where recordings are written. | — | Any writable path | `RecordDir` |
| **...** | Opens a folder browser to choose the recording directory. | — | — | — |
| **Auto-record on TX** | Automatically starts recording whenever you transmit. | Off | On / Off | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence after which an automatic recording stops. | — | — | `RecordIdleTimeout` |
| **Line Out:** | Adjusts the radio's line-out gain. | — | — | — |
| **Mute (Line Out)** | Mutes the radio's line-out. | — | — | — |
| **Headphone:** | Adjusts the radio's headphone gain. | — | — | — |
| **Mute (Headphone)** | Mutes the radio's headphone output. | — | — | — |

## Tips

- If your device does not appear in the **Input:** or **Output:** drop-down, close the dialog, verify the OS recognizes the device, then reopen `Settings > Radio Setup...` and return to the **Audio** tab. Device enumeration happens when the tab is first opened.
- For remote or VPN operation, increase **Audio Buffer:** to reduce dropouts, and consider setting **Audio Compression (SmartLink):** to Opus. See [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md) and [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md).

## Troubleshooting

- **A device appears in the OS but not in the drop-down** — Close the Radio Setup dialog and reopen it. The device list is populated when the Audio tab is built; devices connected after the tab was opened will not appear until the dialog is closed and reopened.
- **Audio plays but sounds distorted or clipped** — Enable **Audio Boost:** only if the received signal is too quiet. If it is already on, turn it off to reduce distortion.
- **Dropouts during remote operation** — Increase **Audio Buffer:** toward 1000 ms and switch **Audio Compression (SmartLink):** to Opus.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)

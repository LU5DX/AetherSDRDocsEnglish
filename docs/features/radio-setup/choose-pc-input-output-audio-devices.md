# Choose PC input/output audio devices

This page explains how to select which PC audio devices AetherSDR uses for radio receive audio output and microphone input. You need to do this when you first set up AetherSDR or when you change headsets, speakers, or audio interfaces.

## Before you start

- The radio must be connected. Radio Setup controls are unavailable without an active radio connection.
- Know which audio input and output devices your PC exposes (check your OS audio settings if unsure).

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Audio** tab.
3. Under **PC Audio Devices:**, click the **Input:** drop-down and select the device you want to use for microphone or audio input.
4. Click the **Output:** drop-down and select the device you want to use for receive audio playback.
5. Close the dialog. The selections take effect immediately.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| **PC Audio Devices: Input:** | Selects the host audio input device (microphone, audio interface, etc.). | System default | Available input devices | — |
| **PC Audio Devices: Output:** | Selects the host audio output device (speakers, headphones, audio interface, etc.). | System default | Available output devices | — |
| **Audio Boost:** | Applies extra gain on the client audio path. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Increases the client audio buffer to absorb jitter on VPN or SmartLink connections. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |
| **Recording: Radio Side / Client Side** | Selects whether recordings are captured at the radio or the client. | — | Radio Side / Client Side | `RecordMode` |
| **Save to:** | Folder where recordings are saved. | — | Any valid path | `RecordDir` |
| **...** | Opens a folder browser to select the recording directory. | — | — | — |
| **Auto-record on TX** | Automatically starts recording when you transmit. | Off | Checked / Unchecked | `AutoRecordTx` |
| **Idle timeout:** | Seconds of silence after which an active recording stops automatically. | — | — | `RecordIdleTimeout` |

## Tips

- The Input and Output drop-downs list only devices the OS currently exposes. If a device is missing, connect it and reopen the Audio tab — device enumeration happens when the tab is first displayed.
- If receive audio sounds too quiet with your chosen output device, enable **Audio Boost:** before increasing OS volume.
- On VPN or SmartLink connections, raise **Audio Buffer:** to reduce dropouts. Values above 200 ms add noticeable delay.

## Troubleshooting

- **No audio devices appear in the drop-downs** — The Audio tab enumerates devices when it first loads. Close Radio Setup, verify the OS recognizes the device, then reopen `Settings > Radio Setup...` and click the Audio tab again.
- **Receive audio plays through the wrong device** — The Output drop-down may still be set to a previously selected device. Open the Audio tab and reselect the correct output.
- **Microphone is not heard by the radio** — Confirm the correct device is selected in the **Input:** drop-down, and that the OS has not muted or blocked access to that device.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)

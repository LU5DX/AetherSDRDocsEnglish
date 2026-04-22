# Choose PC input/output audio devices

Select which PC sound card or audio interface AetherSDR uses to route received audio to your speakers or headphones, and to capture your microphone for transmit. You must do this once after installation, and again whenever you change your audio hardware.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is only available when a radio connection is active.
- Know the name of the audio input and output devices you want to use (as your OS reports them).

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Audio** tab.
3. Under **PC Audio Devices:**, find the **Input:** drop-down. Select the device you want AetherSDR to use for microphone or line input.
4. Find the **Output:** drop-down immediately below it. Select the device you want AetherSDR to use for received audio playback.
5. Click **Close** to save and dismiss the dialog.

## What each control does

| Control | What it does | Default | Valid range / values | Setting key |
|---|---|---|---|---|
| **PC Audio Devices: Input:** | Selects the host audio input device (microphone or line in) used for transmit audio. | System default | All devices enumerated by the OS | — |
| **PC Audio Devices: Output:** | Selects the host audio output device (speakers or headphones) used for received audio. | System default | All devices enumerated by the OS | — |
| **Audio Boost:** | Enables extra gain on the client audio path. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Increases the playback buffer to absorb jitter on VPN or SmartLink connections. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink):** | Selects the audio codec used over SmartLink or LAN. Three positions: Auto, Uncompressed, Opus. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |

## Tips

- If you do not hear audio after selecting a device, check that the selected output device is not muted in your OS mixer.
- For remote or VPN operation, increasing **Audio Buffer:** reduces dropouts at the cost of added latency.
- **Audio Boost:** is useful when the received audio level is low after matching the OS volume and the radio's **Line Out:** or **Headphone:** sliders.

## Troubleshooting

- **Device names do not appear in the drop-down lists** — The lists are populated when the Audio tab is built. Close and reopen Radio Setup after connecting or enabling a new audio device in the OS.
- **Audio cuts out under SmartLink** — Increase **Audio Buffer:** (`AudioBuffer`) toward 1000 ms and switch **Audio Compression (SmartLink):** to Opus, which is more resilient to packet loss.
- **No transmitted audio received on the other end** — Verify the correct device is selected under **Input:** and that the OS has granted AetherSDR microphone access.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)

# Turn on audio boost or enlarge the audio buffer for remote operation

Use these settings when operating AetherSDR over a VPN or SmartLink connection and you need louder audio or smoother playback with reduced dropouts.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible without an active radio connection.
- If you are using SmartLink, confirm your audio compression setting first. See [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md).

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the `Audio` tab.
3. To increase the output level on the client, click `Audio Boost:` to toggle it on.
4. To reduce audio dropouts over a high-latency or jittery link, click the `Audio Buffer:` spinbox and set a value in milliseconds. Higher values add more latency but absorb more jitter.
5. Close the dialog. Settings are saved automatically on close.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| `Audio Boost:` | Enables extra gain on the client audio path. | Off | On / Off | `AudioBoost` |
| `Audio Buffer:` | Increases the client-side audio buffer to absorb VPN or SmartLink jitter. | — | 50–1000 ms | `AudioBuffer` |
| `Audio Compression (SmartLink):` | Selects the audio codec used over SmartLink or LAN. Choices are Auto, Uncompressed, and Opus. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |

## Tips

- Start with a modest `Audio Buffer:` increase (for example, 150–200 ms) before going higher. Larger values improve stability but increase the delay between transmitting and hearing the sidetone or monitor audio.
- `Audio Boost:` affects the client playback path only. It does not change the radio's line-out or headphone output levels.

## Troubleshooting

- **Audio still breaks up after increasing the buffer** — Check whether the codec is set to Uncompressed under `Audio Compression (SmartLink):`. Uncompressed audio demands significantly more bandwidth than Opus. Switch to Auto or Opus if your link is constrained.
- **No improvement after toggling Audio Boost:** — Verify your PC output device is correctly selected under `PC Audio Devices: Output:`. If the wrong device is selected, the boost has no audible effect.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)

# Turn on audio boost or enlarge the audio buffer for remote operation

Use these settings to compensate for low audio levels or choppy audio when operating AetherSDR over a VPN or SmartLink connection. Audio Boost adds extra gain on the client audio path; a larger Audio Buffer absorbs network jitter at the cost of additional latency.

## Before you start

- AetherSDR must be connected to the radio. These controls are in Radio Setup, which requires an active radio connection.
- If audio is cutting out, consider also checking your codec setting. See [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md).

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. To increase the client audio level, click **Audio Boost:** to toggle it on.
4. To increase the audio buffer, click the **Audio Buffer:** spinbox and enter a value between 50 and 1000 ms.
5. Close the dialog. Settings are saved immediately.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Audio Boost:** | Enables extra gain on the client audio path. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Sets the client-side audio buffer size. Larger values reduce dropouts over high-latency or jittery connections. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink):** | Selects the audio codec used over SmartLink or LAN (Auto / Uncompressed / Opus). | Auto | Auto / Uncompressed / Opus | `AudioCompression` |

## Tips

- Increase **Audio Buffer:** in steps of 50–100 ms until dropouts stop. Each increase adds the same amount of one-way audio latency, so use the minimum value that gives clean audio.
- **Audio Boost:** affects the client audio path only; it does not change the radio's Line Out or Headphone gain.

## Troubleshooting

- **Audio is still choppy after enlarging the buffer** — The codec may be the bottleneck. Switch **Audio Compression (SmartLink):** from Auto to Opus, which is designed for lossy or variable-bandwidth links. See [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md).
- **Audio Boost causes distortion** — The incoming signal may already be at or near full scale. Reduce the slice audio gain before enabling **Audio Boost:**, or disable it and raise the gain only as far as the signal allows without clipping.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

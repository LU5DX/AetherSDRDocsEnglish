# Turn on audio boost or enlarge the audio buffer for remote operation

Use this page to enable Audio Boost for extra receive gain or increase the Audio Buffer size to reduce dropouts over VPN or SmartLink connections with high latency or jitter.

## Before you start

- AetherSDR must be connected to the radio. These controls are unavailable when no radio is connected.
- Identify whether your problem is low receive volume (use Audio Boost) or choppy/stuttering audio (increase Audio Buffer).

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. To enable extra receive gain, click **Audio Boost:** to toggle it on. The button shows **Enabled** when active. This setting is saved as `AudioBoost`.
4. To reduce jitter-related dropouts, locate **Audio Buffer:** and set the value in milliseconds. The valid range is 50–1000 ms. This setting is saved as `AudioBuffer`.
5. Close the dialog. Changes take effect immediately.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Audio Boost:** | Enables extra gain on the client audio path. Toggle on to increase receive volume. | — | On / Off | `AudioBoost` |
| **Audio Buffer:** | Sets the client-side audio buffer size. Larger values absorb network jitter at the cost of added latency. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink):** | Selects the audio codec used over SmartLink or LAN (Auto / Uncompressed / Opus). | Auto | — | `AudioCompression` |

## Tips

- Increase **Audio Buffer:** in steps of 50–100 ms until dropouts stop. Use the smallest value that gives clean audio to keep latency low.
- If audio is already loud enough and dropouts are the problem, raise **Audio Buffer:** before enabling **Audio Boost:**. Boosting a clipping signal will not help.
- For codec selection over SmartLink, see [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md).

## Troubleshooting

- **Audio Boost: and Audio Buffer: controls are greyed out or missing** — The Audio tab requires an active radio connection. Connect to the radio first, then reopen `Settings > Radio Setup...`.
- **Audio is still choppy after increasing Audio Buffer:** — Check network conditions. A high-jitter or lossy link may also benefit from switching **Audio Compression (SmartLink):** to **Opus**, which is more resilient to packet loss than uncompressed audio.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)

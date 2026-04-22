# Turn on audio boost or enlarge the audio buffer for remote operation

Use this page to enable audio boost or adjust the audio buffer size when operating remotely over SmartLink or a VPN. Audio boost raises the client-side gain; a larger buffer reduces audio dropouts caused by network jitter.

## Before you start

- AetherSDR must be connected to the radio. These controls are unavailable without an active radio connection.
- Open the Audio tab in Radio Setup. Go to `Settings > Radio Setup...`, then click the **Audio** tab.

## Steps

1. Go to `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. To enable audio boost, click **Audio Boost:** to toggle it on.
4. To increase the audio buffer, locate **Audio Buffer:** and set the value in milliseconds. The valid range is 50–1000 ms. Raise this value if you hear dropouts or stuttering over a VPN or SmartLink connection.
5. Close the dialog. Settings are persisted automatically.

## What each control does

| Control | Description | Valid range / default | Setting key |
|---|---|---|---|
| **Audio Boost:** | Enables extra gain on the client audio path. | On / Off | `AudioBoost` |
| **Audio Buffer:** | Sets the client-side audio buffer size. Higher values absorb more network jitter at the cost of added latency. | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto (default), Uncompressed, Opus | `AudioCompression` |

## Tips

- If you are on a high-latency link such as a cellular or satellite VPN, raise **Audio Buffer:** incrementally (for example, 200 ms, then 400 ms) until dropouts stop. Avoid going higher than necessary, as it adds listening delay.
- **Audio Boost:** affects only the client audio path, not the radio's line-out or headphone outputs. Adjust those separately using **Line Out:** and **Headphone:** on the same tab.
- For codec selection on SmartLink connections, see [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md).

## Troubleshooting

- **Audio dropouts persist after raising Audio Buffer:** — Verify the codec setting. If **Audio Compression (SmartLink):** is set to Uncompressed, try switching to Opus, which is more tolerant of packet loss. See [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md).
- **Audio Boost: toggle has no effect** — Confirm the radio is connected. The control is inactive without a live connection.
- **Audio Buffer: spinbox is grayed out** — The radio must be connected for this control to accept changes.

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

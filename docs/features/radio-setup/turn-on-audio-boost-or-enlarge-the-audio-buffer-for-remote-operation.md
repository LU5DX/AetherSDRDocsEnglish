# Turn on audio boost or enlarge the audio buffer for remote operation

Use these settings to compensate for low receive volume or audio breakup when operating AetherSDR over a VPN or SmartLink connection. Audio Boost adds extra gain on the client audio path; a larger Audio Buffer absorbs network jitter at the cost of increased latency.

## Before you start

- AetherSDR must be connected to the radio. These controls are unavailable when no radio is connected.
- Open `Settings > Radio Setup...` and select the **Audio** tab before following the steps below.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. To increase receive volume, click **Audio Boost:** to toggle it on. The button shows its active state when enabled.
4. To reduce audio breakup or dropouts, click the **Audio Buffer:** spinbox and enter a value between 50 and 1000 ms. Higher values add more buffering at the cost of latency.
5. Close the dialog. Settings take effect immediately.

## What each control does

| Control | What it does | Valid range | Setting key |
|---|---|---|---|
| **Audio Boost:** | Enables extra gain on the client audio path. | On / Off | `AudioBoost` |
| **Audio Buffer:** | Sets the client-side audio buffer to absorb network jitter. Increase this when using VPN or SmartLink connections with unstable latency. | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto \| Uncompressed \| Opus | `AudioCompression` |

## Tips

- Start with a modest buffer increase (200–300 ms) before going higher. Very large values make the audio noticeably sluggish during QSOs.
- If audio quality is poor over SmartLink, also review the codec setting (**Audio Compression (SmartLink):**). Switching from Auto to Opus can reduce bandwidth and improve stability on slow connections.

## Troubleshooting

- **Audio Boost and Audio Buffer controls are greyed out or missing** — These controls are on the **Audio** tab. Confirm you have selected that tab, not another tab such as **RX** or **Phone/CW**.
- **Increasing Audio Buffer has no effect on dropouts** — The buffer absorbs jitter but cannot compensate for sustained packet loss. Check your network path; also see [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md).

## Related

- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

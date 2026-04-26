# Turn on audio boost or enlarge the audio buffer for remote operation

Use these settings when operating AetherSDR over SmartLink, a VPN, or any high-latency link where received audio is too quiet or stutters due to network jitter.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible when offline.
- Open `Settings > Radio Setup...` and click the **Audio** tab.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. To increase received audio level, click **Audio Boost:** to enable it. The button toggles on or off; no additional value is required.
4. To reduce audio dropouts caused by network jitter, locate **Audio Buffer:** and set it to a higher value in milliseconds. The valid range is 50–1000 ms. Increase the value in steps until dropouts stop.
5. Close the dialog. Settings are saved automatically.

## What each control does

| Control | What it does | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Audio Boost:** | Enables extra gain on the client audio path. Toggle on to raise the received audio level without adjusting the radio output level. | Off | On / Off | `AudioBoost` |
| **Audio Buffer:** | Sets the size of the client-side audio buffer. Larger values absorb more network jitter but add latency. | — | 50–1000 ms | `AudioBuffer` |
| **Audio Compression (SmartLink):** | Selects the audio codec used over SmartLink or LAN. Options are Auto, Uncompressed, and Opus. | Auto | Auto / Uncompressed / Opus | `AudioCompression` |

## Tips

- For SmartLink or VPN links with high round-trip time, start with an **Audio Buffer:** value around 200–300 ms and reduce it if latency becomes objectionable.
- **Audio Boost:** acts on the client path only and does not change the radio's line-out or headphone gain.
- If audio still breaks up after enlarging the buffer, switching **Audio Compression (SmartLink):** from Auto to Opus may help on low-bandwidth connections.

## Troubleshooting

- **Audio tab controls are greyed out or the tab is missing** — AetherSDR is not connected to a radio. Connect first via `Settings > Connect to Radio...`, then reopen `Settings > Radio Setup...`.
- **Audio Boost is on but audio is still quiet** — Check the **PC Audio Devices: Output:** selection on the same tab; the wrong output device may be selected. See [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md).
- **Dropouts persist after increasing Audio Buffer:** — Consider changing **Audio Compression (SmartLink):** to Opus, or reviewing network MTU. See [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md).

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

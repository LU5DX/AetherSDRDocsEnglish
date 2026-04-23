# Pick Opus vs Uncompressed Audio for SmartLink

Choose whether AetherSDR compresses audio over SmartLink using Opus, leaves it uncompressed, or lets the radio decide automatically. The right choice depends on your available bandwidth and acceptable latency.

## Before you start

- Be connected to a Flex radio.
- If using SmartLink over the internet or a VPN, have an estimate of your available uplink bandwidth.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Find the **Audio Compression (SmartLink):** control. It cycles through three states: **Auto**, **Uncompressed**, and **Opus**.
4. Click the button until it shows the mode you want.

The selection is saved immediately to `AudioCompression`.

## What each control does

| Control | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|
| **Audio Compression (SmartLink):** | Auto | Auto / Uncompressed / Opus | `AudioCompression` | Selects the audio codec used over SmartLink. Auto lets the radio negotiate the codec. Uncompressed sends raw PCM. Opus uses low-bitrate compressed audio. |
| **Audio Boost:** | — | On / Off | `AudioBoost` | Enables extra gain on the client audio path. |
| **Audio Buffer:** | — | 50–1000 ms | `AudioBuffer` | Increases the client-side audio buffer to absorb jitter on VPN or SmartLink connections. |
| **Recording: Radio Side / Client Side** | — | Radio Side / Client Side | `RecordMode` | Selects whether recordings are captured at the radio or at this client. |
| **Save to:** | — | Folder path | `RecordDir` | Folder where recordings are saved. Click **...** to browse. |
| **Auto-record on TX** | — | Checked / Unchecked | `AutoRecordTx` | Automatically starts recording whenever you transmit. |
| **Idle timeout:** | — | seconds | `RecordIdleTimeout` | Stops a recording after this many seconds of silence. |

## Tips

- Use **Opus** on slow or congested internet connections to reduce bandwidth at the cost of slight additional encoding latency.
- Use **Uncompressed** on a fast local LAN if you want the lowest possible audio latency and have bandwidth to spare.
- If you are unsure which to use, leave the setting on **Auto** and let the radio negotiate.
- If audio cuts out intermittently over a VPN, increase **Audio Buffer:** before changing the compression mode.

## Troubleshooting

- **Audio stutters or drops over SmartLink** — Try increasing **Audio Buffer:** toward 200–500 ms to absorb network jitter. If the problem persists, switch **Audio Compression (SmartLink):** to **Opus** to reduce bandwidth demand.
- **Audio sounds distorted or processed** — If you switched to **Opus** and find the quality unacceptable, set **Audio Compression (SmartLink):** to **Uncompressed** and ensure your link has sufficient bandwidth.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)

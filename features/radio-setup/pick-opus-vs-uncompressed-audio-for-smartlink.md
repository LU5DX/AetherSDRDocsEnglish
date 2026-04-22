# Pick Opus vs Uncompressed Audio for SmartLink

Choose whether AetherSDR compresses the audio stream to Opus, sends it uncompressed, or lets the radio decide automatically when using SmartLink or a LAN connection. The right choice depends on your available bandwidth and acceptable latency.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is unavailable when disconnected.
- Open `Settings > Radio Setup...` and click the **Audio** tab.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **Audio Compression (SmartLink):** control. It cycles through three states: **Auto**, **Uncompressed**, and **Opus**.
4. Click the button repeatedly until it shows the mode you want.
5. Close the dialog. The setting takes effect immediately and is saved automatically to `AudioCompression`.

## What each control does

| Control | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|
| **Audio Compression (SmartLink):** | Auto | Auto / Uncompressed / Opus | `AudioCompression` | Selects the audio codec for the SmartLink or LAN audio stream. **Auto** lets the radio negotiate. **Uncompressed** sends raw PCM — lowest latency, highest bandwidth. **Opus** compresses the stream — lower bandwidth, slightly higher latency. |
| **Audio Boost:** | — | On / Off | `AudioBoost` | Enables extra gain on the client audio path. |
| **Audio Buffer:** | — | 50–1000 ms | `AudioBuffer` | Increases the playback buffer to absorb jitter on VPN or SmartLink connections. |
| **Recording: Radio Side / Client Side** | — | Radio Side / Client Side | `RecordMode` | Picks whether recordings are captured at the radio or on the client PC. |
| **Save to:** | — | folder path | `RecordDir` | Folder where recordings are written. Click **...** to browse. |
| **Auto-record on TX** | — | checked / unchecked | `AutoRecordTx` | Starts recording automatically when the radio transmits. |
| **Idle timeout:** | — | seconds | `RecordIdleTimeout` | Stops an automatic recording after this many seconds of silence. |

## Tips

- Use **Opus** on slow or metered connections such as cellular or VPN links where bandwidth is limited.
- Use **Uncompressed** on a local gigabit LAN or when you need the lowest possible audio latency.
- If you are unsure, leave the setting on **Auto** and let the radio choose based on the connection type.
- If SmartLink audio is choppy, increase **Audio Buffer:** before switching codecs. Valid range is 50–1000 ms.

## Troubleshooting

- **Audio Compression control is greyed out or missing** — The radio must be connected before the Audio tab populates. Verify the connection, then reopen `Settings > Radio Setup...`.
- **Choppy audio after switching to Uncompressed** — Your link may not have sufficient bandwidth for uncompressed PCM. Switch to **Opus** or increase **Audio Buffer:**.
- **No audible difference after changing the setting** — The change applies to new audio streams. If audio was already flowing, disconnect from the radio and reconnect to force the codec to renegotiate.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

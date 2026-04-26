# Pick Opus vs uncompressed audio for SmartLink

Choose how AetherSDR compresses audio over a SmartLink or LAN connection. Selecting the right codec reduces bandwidth on slow or high-latency links, or preserves full audio quality on fast local networks.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible without an active connection.
- Open `Settings > Radio Setup...` and click the **Audio** tab.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **Audio Compression (SmartLink):** control.
4. Click the button to cycle to the desired mode: **Auto**, **Uncompressed**, or **Opus**.
5. Close the dialog. The setting is saved immediately to `AudioCompression`.

## What each control does

| Control | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|
| **Audio Compression (SmartLink):** | Auto | Auto / Uncompressed / Opus | `AudioCompression` | Selects the audio codec used over SmartLink or LAN. Auto lets the radio negotiate the codec. Uncompressed sends raw audio. Opus applies lossy compression to reduce bandwidth. |
| **Audio Boost:** | — | On / Off | `AudioBoost` | Enables extra gain on the client audio path. |
| **Audio Buffer:** | — | 50–1000 ms | `AudioBuffer` | Increases the client-side buffer to absorb jitter on VPN or SmartLink connections. |
| **Recording: Radio Side / Client Side** | — | Radio Side / Client Side | `RecordMode` | Picks whether recordings are captured at the radio or on the client PC. |
| **Save to:** | — | Folder path | `RecordDir` | Sets the folder where recordings are written. |
| **Auto-record on TX** | — | Checked / Unchecked | `AutoRecordTx` | Automatically starts recording whenever the radio transmits. |
| **Idle timeout:** | — | Seconds | `RecordIdleTimeout` | Stops a recording after this many seconds of silence. |

## Tips

- Use **Opus** when connecting over the internet or a VPN where bandwidth is limited. Opus significantly reduces the audio data rate compared to uncompressed.
- Use **Uncompressed** on a fast local network when audio fidelity is the priority and bandwidth is not a concern.
- **Auto** is suitable for most users and allows the radio firmware to choose the codec based on the connection type.
- If audio breaks up or drops on a remote connection, increase **Audio Buffer:** before changing the codec. The valid range is 50–1000 ms.

## Troubleshooting

- **Audio Compression control is greyed out or the Audio tab does not appear** — The radio is not connected. Connect to the radio first, then reopen `Settings > Radio Setup...`.
- **Audio is choppy after switching to Uncompressed** — The link does not have enough bandwidth for uncompressed audio. Switch to **Opus** or increase **Audio Buffer:**.
- **Opus is selected but audio quality is poor** — Increase **Audio Buffer:** to compensate for jitter, or check the network path for packet loss.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

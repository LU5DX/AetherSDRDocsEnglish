# Pick Opus vs Uncompressed Audio for SmartLink

Select the audio codec AetherSDR uses over SmartLink or LAN connections. Opus reduces bandwidth at the cost of a small amount of compression; uncompressed PCM preserves full fidelity when bandwidth allows. Auto lets the radio choose.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible without an active connection.
- Open `Settings > Radio Setup...` and click the **Audio** tab.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Audio Compression (SmartLink):**, click **Auto**, **Uncompressed**, or **Opus** to select the codec.
   - **Auto** — the radio negotiates the codec automatically (default).
   - **Uncompressed** — sends raw PCM audio; uses more bandwidth.
   - **Opus** — sends Opus-encoded audio; lower bandwidth, slight compression.
4. Close the dialog. The setting takes effect immediately and is saved.

## What each control does

| Control | Default | Valid values | Setting key |
|---|---|---|---|
| **Audio Compression (SmartLink):** Auto / Uncompressed / Opus | Auto | Auto, Uncompressed, Opus | `AudioCompression` |
| **Audio Boost:** | — | Enabled / Disabled | `AudioBoost` |
| **Audio Buffer:** | — | 50–1000 ms | `AudioBuffer` |
| **Recording:** Radio Side / Client Side | — | Radio Side, Client Side | `RecordMode` |
| **Save to:** | — | Folder path | `RecordDir` |
| **Auto-record on TX** | — | Checked / Unchecked | `AutoRecordTx` |
| **Idle timeout:** | — | seconds | `RecordIdleTimeout` |

## Tips

- On a fast local LAN, **Uncompressed** avoids any codec artefacts and is the better choice for critical listening or digital mode decoding.
- On a slow or congested link (VPN, cellular SmartLink), **Opus** reduces audio dropouts. Pair it with a larger **Audio Buffer:** value (50–1000 ms) to absorb jitter.
- If audio sounds thin or quiet over SmartLink, try enabling **Audio Boost:** alongside Opus.

## Troubleshooting

- **Audio Compression buttons are greyed out or missing** — the Audio tab only builds after you click it, and only when a radio is connected. Verify the connection, then click the Audio tab again.
- **Audio quality is poor even with Uncompressed selected** — check network bandwidth and latency. Consider increasing **Audio Buffer:** to reduce underruns. See [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md).

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

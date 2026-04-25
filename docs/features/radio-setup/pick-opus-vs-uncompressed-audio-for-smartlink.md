# Pick Opus vs Uncompressed Audio for SmartLink

Choose which audio codec AetherSDR uses when connecting to your FLEX-8600 over SmartLink or a LAN. Opus reduces bandwidth at the cost of a small amount of audio processing; uncompressed (PCM) preserves the raw audio stream. Auto lets the radio negotiate the best option.

## Before you start

- The radio must be connected. `Settings > Radio Setup...` is unavailable when no radio is connected.
- You must be using SmartLink or a LAN connection. This setting has no effect on direct USB audio.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Locate the **Audio Compression (SmartLink):** control.
4. Click the button to cycle through **Auto**, **Uncompressed**, and **Opus** until the label shows the mode you want.
5. Close the dialog. The setting is saved immediately to `AudioCompression`.

## What each control does

| Control | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|
| **Audio Compression (SmartLink):** | Auto | Auto / Uncompressed / Opus | `AudioCompression` | Selects the audio codec used for SmartLink and LAN audio streams. |
| **Audio Boost:** | — | On / Off | `AudioBoost` | Enables extra gain on the client audio path. |
| **Audio Buffer:** | — | 50–1000 ms | `AudioBuffer` | Increases the client-side buffer to absorb jitter on VPN or SmartLink connections. |
| **Recording: Radio Side / Client Side** | — | Radio Side / Client Side | `RecordMode` | Picks whether audio is recorded at the radio or on this PC. |
| **Save to:** | — | Any writable folder path | `RecordDir` | Folder where recordings are written. |
| **Auto-record on TX** | — | Checked / Unchecked | `AutoRecordTx` | Starts recording automatically whenever you transmit. |
| **Idle timeout:** | — | Seconds | `RecordIdleTimeout` | Stops an active recording after this many seconds of silence. |

## Tips

- **Auto** is the safest choice for most setups. The radio and client negotiate the codec at connection time.
- If you hear artifacts or dropouts over a slow or congested link, try **Opus** explicitly. If audio quality matters more than bandwidth — for example on a local gigabit LAN — choose **Uncompressed**.
- If your connection has variable latency (VPN, cellular), increase **Audio Buffer:** to reduce audio gaps. Valid range is 50–1000 ms.

## Troubleshooting

- **Audio Compression (SmartLink): button is missing or greyed out** — The dialog requires an active radio connection. Connect to the radio first, then open `Settings > Radio Setup...` and go to the **Audio** tab.
- **Changing the codec has no audible effect** — The codec change takes effect on the next connection. Disconnect from the radio and reconnect.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

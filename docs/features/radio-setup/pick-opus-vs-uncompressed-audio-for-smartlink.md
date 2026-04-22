# Pick Opus vs Uncompressed Audio for SmartLink

Choose the audio codec AetherSDR uses when connecting over SmartLink or a LAN. Opus reduces bandwidth at the cost of slight compression; uncompressed passes audio without codec processing. Auto lets the radio negotiate the best option.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab in Radio Setup is not available without an active connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Find the **Audio Compression (SmartLink):** control. It cycles between three states: **Auto**, **Uncompressed**, and **Opus**.
4. Click the button until it shows the mode you want.
5. Close the dialog. The setting is saved automatically to `AudioCompression`.

## What each control does

| Control | Default | Valid values | Setting key | Behavior |
|---|---|---|---|---|
| **Audio Compression (SmartLink):** | Auto | Auto / Uncompressed / Opus | `AudioCompression` | Selects the audio codec for SmartLink and LAN audio streams. |
| **Audio Boost:** | — | On / Off | `AudioBoost` | Enables extra gain on the client audio path. |
| **Audio Buffer:** | — | 50–1000 ms | `AudioBuffer` | Increases the playback buffer to absorb VPN or SmartLink jitter. |
| **Recording: Radio Side / Client Side** | — | Radio Side / Client Side | `RecordMode` | Picks whether recordings are captured at the radio or the client. |
| **Save to:** | — | Folder path | `RecordDir` | Folder where recordings are written. |
| **Auto-record on TX** | — | On / Off | `AutoRecordTx` | Starts recording automatically when you transmit. |
| **Idle timeout:** | — | Seconds | `RecordIdleTimeout` | Stops a recording after this many seconds of silence. |

## Tips

- Over a fast local network, **Uncompressed** gives the lowest processing overhead. Over a congested or high-latency link, **Opus** reduces the data rate.
- If audio drops out during remote operation, increase **Audio Buffer:** in addition to selecting **Opus**. Valid range is 50–1000 ms.

## Related

- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)

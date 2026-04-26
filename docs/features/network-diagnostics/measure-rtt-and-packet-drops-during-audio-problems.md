# Measure RTT and packet drops during audio problems

Use the Network Diagnostics dialog to read current round-trip time and per-category packet drop counts while you reproduce an audio problem. This lets you distinguish a network path issue from a local audio configuration issue.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but most indicators will be empty until the radio is connected.
- Reproduce or be ready to reproduce the audio problem so you can observe the values live.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Look at **Latency (RTT)** in the Network Status group. This shows the current round-trip time to the radio in milliseconds. Values below 1 ms are shown as `< 1 ms`.
3. Look at **Max Latency (RTT)**. This shows the highest RTT recorded since the radio connected. A large gap between **Latency (RTT)** and **Max Latency (RTT)** indicates periodic spikes on the network path.
4. Look at the **Audio** row under the Packet Loss (Sequence Gaps) group. The value shows dropped packets versus total packets and a percentage. Any non-zero percentage during audio problems points to packet loss on the UDP path.
5. Check **FFT**, **Waterfall**, **Meters**, and **DAX** drop rows in the same group to determine whether loss is specific to the audio stream or affects all categories.
6. Click Close when finished.

## What each control does

| Indicator | Group | Meaning |
|---|---|---|
| **Status** | Network Status | Overall link state. |
| **Target Radio IP** | Network Status | IP address of the connected radio. Shows `Not connected` when no radio is connected. |
| **Selected Source** | Network Status | Local network interface or bind path used for the connection. |
| **Local TCP** | Network Status | Local TCP endpoint in use. |
| **Local UDP** | Network Status | Local UDP endpoint in use. |
| **First UDP Packet** | Network Status | Whether the first UDP packet has been received (`Yes` or `No`). |
| **Latency (RTT)** | Network Status | Current round-trip time, updated every second. |
| **Max Latency (RTT)** | Network Status | Highest RTT seen since connect. |
| **Audio** (rate) | Incoming Stream Rates | Audio stream ingress rate in kbps. |
| **FFT** (rate) | Incoming Stream Rates | FFT stream ingress rate in kbps. |
| **Waterfall** (rate) | Incoming Stream Rates | Waterfall stream ingress rate in kbps. |
| **Meters** (rate) | Incoming Stream Rates | Meters stream ingress rate in kbps. |
| **DAX** (rate) | Incoming Stream Rates | DAX stream ingress rate in kbps. |
| **Total RX** | Incoming Stream Rates | Aggregate inbound bytes per second across all categories. |
| **Total TX** | Incoming Stream Rates | Aggregate outbound bytes per second. |
| **Audio** (drops) | Packet Loss (Sequence Gaps) | Audio dropped packets / total packets (percentage). Inferred from VITA sequence number gaps. |
| **FFT** (drops) | Packet Loss (Sequence Gaps) | FFT dropped packets / total packets (percentage). |
| **Waterfall** (drops) | Packet Loss (Sequence Gaps) | Waterfall dropped packets / total packets (percentage). |
| **Meters** (drops) | Packet Loss (Sequence Gaps) | Meters dropped packets / total packets (percentage). |
| **DAX** (drops) | Packet Loss (Sequence Gaps) | DAX dropped packets / total packets (percentage). |
| **RX Buffer Now** | Audio Playback | Current audio buffer fill in bytes and milliseconds. |
| **RX Buffer Peak** | Audio Playback | Peak audio buffer fill since connect. |
| **Underruns (total)** | Audio Playback | Cumulative audio buffer underrun count. |
| **Underruns (last sec)** | Audio Playback | Underruns recorded in the most recent one-second interval. |
| **Audio Arrival Gap** | Audio Playback | Current inter-packet arrival timing. |
| **Max Arrival Gap** | Audio Playback | Largest inter-packet arrival gap seen since connect. |
| **Network Jitter** | Audio Playback | Smoothed jitter estimate for the audio stream. |

All values refresh once per second.

## Tips

- Zero drops in the Packet Loss group does not rule out the problem. Large swings in the rate rows under Incoming Stream Rates can indicate bursty delivery without sequence-number gaps. Check **Audio Arrival Gap** and **Network Jitter** in the Audio Playback group to detect timing problems that do not show as drops.
- If **Underruns (total)** is climbing while **RX Buffer Now** is near zero, the audio playback side is starving. This points to a local audio configuration issue rather than network packet loss. See [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md).
- If drops appear across all categories (Audio, FFT, Waterfall, Meters), the problem is likely the network path rather than radio-side audio processing.

## Troubleshooting

- **All indicators show empty or zero immediately after opening the dialog** — The radio is not connected. Connect to the radio first, then reopen the dialog via `Settings > Network...`.
- **Latency (RTT) shows `< 1 ms` but audio is still poor** — RTT reflects TCP ping timing. UDP audio packet timing is separate. Check **Audio Arrival Gap**, **Max Arrival Gap**, and **Network Jitter** for UDP delivery problems.

## Related

- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- [Network Diagnostics overview](overview.md)

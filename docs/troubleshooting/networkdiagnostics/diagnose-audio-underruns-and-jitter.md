# Diagnose audio underruns and jitter

Use this page to read the audio buffer and jitter indicators in Network Diagnostics and identify why received audio sounds choppy, silent, or glitchy.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the audio indicators are only meaningful when a radio is connected and streaming audio.
- Open the dialog and leave it visible while you reproduce the audio problem.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Locate the **Audio Playback** group in the lower-right area of the dialog.
3. Watch **RX Buffer Now** and **RX Buffer Peak**. Values are shown in bytes and milliseconds. A buffer that stays near zero while underruns rise indicates the playback thread is starving.
4. Watch **Underruns (total)** and **Underruns (last sec)**. **Underruns (last sec)** resets each second, so a sustained non-zero value here means the problem is ongoing rather than historical.
5. Watch **Audio Arrival Gap** and **Max Arrival Gap**. These show the inter-packet arrival timing. A large **Max Arrival Gap** relative to **Audio Arrival Gap** indicates bursts of late packets even if no packets were dropped.
6. Watch **Network Jitter**. This is a smoothed estimate of timing variation in the audio stream. Rising jitter with rising underruns points to a network delivery problem rather than a local audio device problem.
7. Cross-check the **Packet Loss (Sequence Gaps)** group. Find the **Audio** row under that group. A non-zero drop count confirms actual packet loss in addition to any jitter.
8. Click Close when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| **RX Buffer Now** | Current audio buffer fill, in bytes and milliseconds. |
| **RX Buffer Peak** | Highest buffer fill seen since the dialog was opened. |
| **Underruns (total)** | Cumulative count of audio buffer underruns since connect. |
| **Underruns (last sec)** | Underruns counted in the most recent one-second interval. |
| **Audio Arrival Gap** | Typical inter-packet arrival interval, in milliseconds. |
| **Max Arrival Gap** | Largest single inter-packet gap seen, in milliseconds. |
| **Network Jitter** | Smoothed jitter estimate for the audio stream, in milliseconds. |

All indicators refresh every second.

## Tips

- Zero packet loss in the **Audio** drop row does not rule out jitter. Packets can arrive late in bursts without being dropped, and **Max Arrival Gap** will reflect that where the drop counter will not.
- If **Underruns (last sec)** is zero but **Underruns (total)** is non-zero, the problem was transient and may have resolved on its own.
- If **RX Buffer Peak** is high but **RX Buffer Now** is near zero and underruns are rising, the buffer filled briefly on connect and then drained, which can indicate the audio output device is running faster than the incoming stream rate.

## Troubleshooting

- **Underruns rising, RX Buffer Now near zero, Network Jitter low** — The network is delivering audio on time but the local audio output device may be consuming faster than packets arrive. Check your audio output sample rate and device settings in `Settings > Radio Setup...`.
- **Underruns rising, Max Arrival Gap much larger than Audio Arrival Gap** — Packets are arriving in bursts. The network path has bursty delay. Reduce other traffic on the local network or switch to a wired connection.
- **Audio drop count non-zero in Packet Loss group** — Packets are being lost in transit, not just delayed. Check for wireless interference or switch network interfaces. See [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md).
- **Network Jitter rising steadily** — The network path is increasingly unstable. Check **Latency (RTT)** and **Max Latency (RTT)** in the **Network Status** group for corroborating evidence.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)

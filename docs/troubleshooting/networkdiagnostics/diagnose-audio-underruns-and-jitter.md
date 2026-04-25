# Diagnose audio underruns and jitter

Use the Network Diagnostics dialog to read the audio buffer and jitter indicators in real time and identify the cause of clicks, dropouts, or stuttering audio.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the audio indicators are only meaningful while connected and receiving audio.
- Reproduce the audio problem before reading the indicators — the counters accumulate since the last connect and the rates update every second.

## Steps

1. Open `Settings > Network...`. The Network Diagnostics dialog opens.
2. Locate the **Audio Playback** group in the lower-right area of the dialog.
3. Read **RX Buffer Now**. This shows the current audio buffer fill in bytes and milliseconds. If this value is near zero while underruns are rising, playback is starving.
4. Read **RX Buffer Peak**. This shows the highest buffer fill seen since connect. A very low peak alongside frequent underruns confirms the buffer is never building adequate headroom.
5. Read **Underruns (total)**. This is the cumulative count of audio underruns since connect.
6. Read **Underruns (last sec)**. This shows how many underruns occurred in the most recent one-second window. A nonzero value here means the problem is active right now.
7. Read **Audio Arrival Gap** and **Max Arrival Gap**. These show the inter-packet arrival timing. A large **Max Arrival Gap** relative to a normal **Audio Arrival Gap** indicates occasional bursts of late packets rather than a steady stream.
8. Read **Network Jitter**. This is the smoothed jitter estimate for the audio stream. High jitter combined with a low **RX Buffer Now** value is the primary indicator that the receive buffer is too small to absorb timing variation on this network path.
9. Cross-check the **Packet Loss (Sequence Gaps)** group. Look at the **Audio** drop row. Zero drops with high jitter means packets are arriving but not on time. Nonzero audio drops mean packets are actually being lost.
10. Click **Close** when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| **RX Buffer Now** | Current audio buffer fill, shown in bytes and milliseconds. |
| **RX Buffer Peak** | Highest buffer fill recorded since connect. |
| **Underruns (total)** | Cumulative audio underrun count since connect. |
| **Underruns (last sec)** | Underruns observed in the last one-second interval. |
| **Audio Arrival Gap** | Typical inter-packet arrival interval for the audio stream. |
| **Max Arrival Gap** | Largest single inter-packet gap seen since connect. |
| **Network Jitter** | Smoothed jitter estimate for the audio stream. |
| **Audio** (Packet Loss row) | Dropped audio packets inferred from VITA sequence gaps, shown as errors / total packets and percentage. |

## Tips

- The dialog refreshes every second. Watch **Underruns (last sec)** rather than **Underruns (total)** to determine whether the problem is ongoing or historical.
- Zero packet loss in the **Packet Loss** group does not rule out jitter. Packets can arrive late — causing underruns — without being counted as drops.
- Large swings in the **Audio** rate in the **Incoming Stream Rates** group can indicate bursty delivery even when no sequence gaps are detected.

## Troubleshooting

- **Underruns (last sec) is nonzero but Audio drops show zero** — Packets are arriving in bursts. Network jitter is consuming the buffer. Check your switch, cable quality, or any QoS settings on the path between your computer and the radio.
- **Both underruns and Audio drops are rising** — Packets are being lost before they arrive. See [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md) for further steps.
- **RX Buffer Peak is very low** — The buffer never accumulated meaningful headroom. This can happen if audio started receiving immediately after connect before the buffer was primed; disconnect and reconnect, then monitor again.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)

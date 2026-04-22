# Diagnose audio underruns and jitter

Use the Network Diagnostics dialog to watch the audio buffer, underrun counters, arrival gap, and jitter estimate in real time. This helps you identify whether audio glitches are caused by a starving playback buffer, irregular packet delivery, or both.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the audio indicators are only meaningful while the radio is streaming audio.
- Reproduce or wait for the audio problem to occur while the dialog is open so the counters accumulate.

## Steps

1. Click `Settings > Network...`. The Network Diagnostics dialog opens.
2. Look at the **Audio Playback** group in the lower-right of the dialog.
3. Read **RX Buffer Now** to see the current fill level of the playback buffer in bytes and milliseconds. A value near zero while audio is playing indicates the buffer is starving.
4. Read **RX Buffer Peak** to see the highest fill level recorded since the dialog opened.
5. Read **Underruns (total)** for the cumulative count of buffer underruns since connect.
6. Read **Underruns (last sec)** to see whether underruns are occurring right now or are only a historical artifact.
7. Read **Audio Arrival Gap** for the current inter-packet arrival interval. Large values indicate bursts of delayed packets even when no packets are lost.
8. Read **Max Arrival Gap** for the worst arrival gap seen since the dialog opened.
9. Read **Jitter Estimate** for the smoothed jitter of the audio stream.
10. If underruns are rising but the buffer is near zero, the audio stream is being starved — check the **Audio** row in **Incoming Stream Rates** and **Packet Loss (Sequence Gaps)** for low throughput or packet loss on that stream.
11. If the buffer has healthy fill but underruns still occur, high jitter or large arrival gaps are the likely cause — compare **Jitter Estimate** and **Max Arrival Gap** against **Latency (RTT)** in the **Network Status** group.
12. Click Close when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| **RX Buffer Now** | Current audio playback buffer fill, shown in bytes and milliseconds. |
| **RX Buffer Peak** | Highest buffer fill recorded since the dialog was opened. |
| **Underruns (total)** | Cumulative count of audio buffer underruns since the radio connected. |
| **Underruns (last sec)** | Number of underruns that occurred in the most recent one-second window. |
| **Audio Arrival Gap** | Current time between consecutive incoming audio packet arrivals. |
| **Max Arrival Gap** | Largest arrival gap observed since the dialog was opened. |
| **Jitter Estimate** | Smoothed jitter value for the audio stream. |

All audio buffer sizes are displayed as bytes with a millisecond conversion based on the active sample rate. Values below 1 ms are shown as `< 1 ms`.

## Tips

- The dialog refreshes every second. Leave it open for at least 30–60 seconds during a problem to capture meaningful peak values.
- Zero packet loss in the **Packet Loss (Sequence Gaps)** group does not rule out jitter or late bursts as the cause of underruns. Always check **Audio Arrival Gap** and **Jitter Estimate** alongside the drop counters.
- Large swings in the **Audio** rate shown in **Incoming Stream Rates** can indicate bursty delivery even when no sequence-number gaps are detected.

## Troubleshooting

- **Underruns (last sec) is non-zero but Audio drops show zero** — Packets are arriving in order but with irregular timing. Check **Jitter Estimate** and **Max Arrival Gap**. The cause is likely network bufferbloat or competing traffic on the local network segment.
- **RX Buffer Now stays near zero** — The audio stream rate is too low to keep the buffer filled. Check the **Audio** row in **Incoming Stream Rates** for an unexpectedly low kbps value, and check **Audio** drops for sequence gaps that would indicate packet loss.
- **Max Arrival Gap is large but current Audio Arrival Gap looks normal** — A transient burst occurred earlier in the session. The peak value is not reset while the dialog is open; reconnect to the radio to clear historical peaks.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)

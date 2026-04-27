# Diagnose audio underruns and jitter

Use the Network Diagnostics dialog to read live audio buffer health, underrun counts, arrival gap timing, and jitter estimates. This helps you identify whether audio dropouts are caused by a starved buffer, bursty packet delivery, or network jitter.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the audio indicators are only meaningful while a radio is connected and streaming audio.
- Reproduce the audio problem before opening the dialog so the counters and peak values reflect the fault condition.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Locate the **Audio Playback** group in the lower-right area of the dialog.
3. Read **RX Buffer Now** to see how many bytes (and milliseconds) of audio are currently held in the playback buffer.
4. Read **RX Buffer Peak** to see the highest buffer fill recorded since the dialog was opened.
5. Read **Underruns (total)** to see the cumulative count of buffer underruns since the audio engine started.
6. Read **Underruns (last sec)** to see how many underruns occurred in the most recent one-second window. A non-zero value here while audio is actively streaming indicates an ongoing problem.
7. Read **Audio Arrival Gap** to see the current inter-packet arrival interval. A value significantly larger than the expected packet period indicates bursty delivery.
8. Read **Max Arrival Gap** to see the worst-case arrival gap recorded since the dialog was opened.
9. Read **Network Jitter** to see the smoothed jitter estimate for the audio stream.
10. If underruns are rising but **RX Buffer Now** stays near zero, the buffer is starving — see the tips below.
11. Click **Close** when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| **RX Buffer Now** | Current audio buffer fill, shown in bytes and milliseconds. |
| **RX Buffer Peak** | Highest buffer fill seen since the dialog was opened. |
| **Underruns (total)** | Cumulative count of audio buffer underruns since the audio engine started. |
| **Underruns (last sec)** | Number of underruns that occurred in the last one-second interval. |
| **Audio Arrival Gap** | Time between consecutive incoming audio packet arrivals. |
| **Max Arrival Gap** | Largest arrival gap recorded since the dialog was opened. |
| **Network Jitter** | Smoothed estimate of audio stream jitter. |

All indicators refresh once per second.

## Tips

- **Underruns rising, buffer near zero:** The audio stream is not arriving fast enough to keep the buffer filled. Check the **Audio** rate in the **Incoming Stream Rates** group and compare it to the expected bitrate. A very low or zero Audio rate means packets are not arriving at all.
- **Zero packet loss but still getting underruns:** The **Packet Loss (Sequence Gaps)** group counts only missing VITA sequence numbers. Packets that arrive late rather than missing will not increment the drop counter but will still cause jitter and underruns. Use **Audio Arrival Gap** and **Network Jitter** to detect this condition.
- **Large Max Arrival Gap with low average gap:** This indicates occasional bursts of delayed packets rather than sustained loss. Isolate the network path to the radio and check for competing traffic.
- **RX Buffer Peak is very low:** The buffer never built up a useful reserve. This makes the stream sensitive to any delivery variation. Check the network path and consider whether other heavy traffic is competing on the same link.

## Troubleshooting

- **All audio indicators show zero or no data** — The radio is not streaming audio. Confirm the radio is connected and a receiver slice is active.
- **Underruns (last sec) is non-zero but Underruns (total) is small** — The problem is intermittent. Leave the dialog open and wait for a longer observation period. Watch **Max Arrival Gap** for evidence of periodic bursts.
- **Network Jitter is high but Audio drops show zero** — Packets are arriving late rather than being lost. Jitter directly reduces the effective buffer margin. Check for other UDP traffic competing on the same interface.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)

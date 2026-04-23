# Diagnose audio underruns and jitter

Use the Network Diagnostics dialog to read the audio buffer health, underrun counters, and jitter indicators that identify the cause of choppy or interrupted received audio.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the audio indicators are only meaningful while a radio is connected and streaming audio.
- Reproduce the audio problem before opening the dialog so the counters accumulate during the fault.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Let the display refresh for at least 10–15 seconds while the audio problem is occurring. The dialog updates every second.
3. Look at the **Audio Playback** group in the lower-right of the dialog. Read these indicators in order:

   a. **RX Buffer Now** — current fill of the audio playback buffer, shown in bytes and milliseconds. A value near zero while underruns are rising means playback is starving for data.

   b. **RX Buffer Peak** — highest buffer fill recorded since the dialog opened. A very low peak combined with underruns confirms the buffer has never built up enough headroom.

   c. **Underruns (total)** — cumulative count of playback buffer underruns since the audio engine started.

   d. **Underruns (last sec)** — underruns that occurred in the most recent one-second window. A non-zero value here means the problem is active right now.

   e. **Audio Arrival Gap** — current inter-packet arrival interval for the audio stream.

   f. **Max Arrival Gap** — largest arrival gap seen since connect. A large max gap relative to a normal arrival gap points to burst delays rather than steady loss.

   g. **Jitter Estimate** — smoothed measure of timing variation in the audio stream. Rising jitter with a low buffer fill is a common cause of underruns.

4. Cross-check the **Packet Loss (Sequence Gaps)** group. Read the **Audio** drop row. If the drop count is zero but underruns are rising, the problem is delivery timing or buffer starvation, not packet loss.
5. Cross-check the **Incoming Stream Rates** group. Read the **Audio** rate row. Large swings from one second to the next indicate bursty delivery even when no packets are lost.
6. Click Close when done.

## What each control does

| Indicator | What it shows |
|---|---|
| **RX Buffer Now** | Current audio playback buffer fill, in bytes and milliseconds. |
| **RX Buffer Peak** | Highest buffer fill recorded since the dialog opened. |
| **Underruns (total)** | Total audio buffer underruns since the audio engine started. |
| **Underruns (last sec)** | Underruns in the most recent one-second interval. |
| **Audio Arrival Gap** | Current inter-packet arrival timing for the audio stream. |
| **Max Arrival Gap** | Largest inter-packet arrival gap seen since connect. |
| **Jitter Estimate** | Smoothed jitter of the incoming audio stream. |

None of these indicators have persisted setting keys. They are read-only live measurements.

## Tips

- Zero packet loss in the **Audio** drop row does not rule out underruns. Packets can arrive in bursts that exhaust the buffer without any sequence gaps.
- The dialog note for the Audio Playback group states: "If underruns rise while the buffer stays near zero, playback is starving." Check **RX Buffer Now** and **Underruns (last sec)** together, not separately.
- Arrival gap and jitter measure timing, not packet loss. A large **Max Arrival Gap** with a low **Jitter Estimate** suggests a single isolated burst rather than a chronic jitter problem.

## Troubleshooting

- **Underruns (last sec) is non-zero but Audio drop count is zero** — packets are arriving but not on time. The network path is introducing bursts or jitter. Investigate the switch, cable, or Wi-Fi segment between the host and the Flex radio.
- **RX Buffer Now reads near zero constantly** — the buffer is not filling. Check that the audio stream is active and that the **Audio** rate in the Incoming Stream Rates group is non-zero.
- **Max Arrival Gap is large but current Audio Arrival Gap is normal** — a single burst event occurred at some point since connect. Reopen the dialog and monitor over a longer period to determine whether it recurs.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)

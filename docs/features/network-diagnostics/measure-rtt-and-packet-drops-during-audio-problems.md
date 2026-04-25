# Measure RTT and packet drops during audio problems

Use the Network Diagnostics dialog to read live round-trip time and per-category packet drop counts while audio is breaking up. This helps you distinguish a lossy network path from a local buffer or jitter problem.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but RTT and drop counters will only show meaningful data while connected.
- Reproduce or wait for the audio problem to recur so you can observe the counters live.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Watch the **Latency (RTT)** field. It updates every second and shows the current round-trip time in milliseconds.
3. Watch the **Max Latency (RTT)** field. It shows the highest RTT recorded since the radio connected. A value significantly above your typical **Latency (RTT)** indicates periodic latency spikes.
4. In the **Packet Loss (Sequence Gaps)** group, check the **Audio** row. The value is shown as `errors / total packets (%)`. Any non-zero percentage during audio problems points to network packet loss as the cause.
5. Check the remaining drop rows — **FFT**, **Waterfall**, **Meters**, and **DAX** — to determine whether loss is limited to the audio stream or affects all categories. Loss on all streams points to a general network path problem rather than an audio-specific issue.
6. If the drop counts are zero but audio is still broken, move to the **Audio Playback** group and check **Underruns (total)**, **Underruns (last sec)**, **RX Buffer Now**, and **Network Jitter**. Zero drops with rising underruns indicate a local buffer starvation or jitter problem, not packet loss.
7. Click Close when finished.

## What each control does

| Indicator | Where it appears | Meaning |
|---|---|---|
| **Latency (RTT)** | Network Status | Current round-trip time to the radio, in milliseconds. Values below 1 ms are shown as `< 1 ms`. |
| **Max Latency (RTT)** | Network Status | Highest RTT seen since the radio connected. Resets on reconnect. |
| **Audio** (Packet Loss) | Packet Loss (Sequence Gaps) | Dropped audio packets inferred from missing VITA-49 sequence numbers, shown as `errors / total (%)`. |
| **FFT** (Packet Loss) | Packet Loss (Sequence Gaps) | Dropped FFT packets by the same method. |
| **Waterfall** (Packet Loss) | Packet Loss (Sequence Gaps) | Dropped waterfall packets. |
| **Meters** (Packet Loss) | Packet Loss (Sequence Gaps) | Dropped meter packets. |
| **DAX** (Packet Loss) | Packet Loss (Sequence Gaps) | Dropped DAX packets. |
| **RX Buffer Now** | Audio Playback | Current audio receive buffer fill, in bytes and milliseconds. |
| **RX Buffer Peak** | Audio Playback | Highest buffer fill seen since connect. |
| **Underruns (total)** | Audio Playback | Cumulative audio buffer underrun count since connect. |
| **Underruns (last sec)** | Audio Playback | Underruns that occurred in the most recent one-second window. |
| **Audio Arrival Gap** | Audio Playback | Inter-packet arrival interval, measuring delivery timing. |
| **Max Arrival Gap** | Audio Playback | Largest inter-packet gap seen since connect. |
| **Network Jitter** | Audio Playback | Smoothed estimate of audio stream jitter. |

## Tips

- All values refresh once per second automatically. Leave the dialog open during a problem period and note which counters change at the moment audio degrades.
- Zero packet loss in the **Packet Loss (Sequence Gaps)** group does not rule out jitter. The dialog's own note states: "Zero loss here does not rule out jitter or late bursts." Check **Network Jitter** and **Max Arrival Gap** as well.
- **Max Latency (RTT)** persists across the session. If it is much higher than **Latency (RTT)** at the time you open the dialog, a spike already occurred that you may have missed.

## Troubleshooting

- **All drop counters show 0 but audio still breaks up** — The problem is not packet loss. Check **Underruns (last sec)** and **Network Jitter** in the Audio Playback group. See [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md).
- **RTT shows `< 1 ms` and drop counts are all zero** — The radio may not be connected. Confirm **Status** and **Target Radio IP** in the Network Status group show an active connection. See [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md).
- **Only the Audio drop row is non-zero while FFT, Waterfall, and Meters show zero** — Loss is stream-specific rather than a broad network path failure. This can indicate QoS or switch behavior that treats UDP streams differently; the audio UDP stream may be deprioritized.

## Related

- [Network Diagnostics overview](overview.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

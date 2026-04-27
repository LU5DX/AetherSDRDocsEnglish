# Measure RTT and packet drops during audio problems

Use the Network Diagnostics dialog to read live round-trip time and per-category packet-drop counts while audio problems occur. This lets you distinguish network loss from other causes such as buffer starvation or jitter.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but RTT and drop counters are only meaningful while connected.
- Reproduce or wait for the audio problem to occur before reading the counters — drop counts accumulate since connect and RTT reflects the current moment.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Read `Latency (RTT)` for the current round-trip time to the radio.
3. Read `Max Latency (RTT)` for the highest RTT recorded since the connection was established.
4. Under the **Packet Loss (Sequence Gaps)** section, read the `Audio` drop counter. The value shows dropped packets, total packets, and a loss percentage.
5. Check the `FFT`, `Waterfall`, `Meters`, and `DAX` drop rows in the same section to see whether loss is isolated to audio or affects all streams.
6. Click `Close` when finished.

## What each control does

| Indicator | Meaning |
|---|---|
| `Latency (RTT)` | Current round-trip time to the radio. Displays `< 1 ms` when below 1 ms. |
| `Max Latency (RTT)` | Highest RTT seen since connect. Displays `< 1 ms` when below 1 ms. |
| `Audio` (Packet Loss) | Dropped packets / total packets (loss %) for the audio stream, inferred from missing VITA sequence numbers. |
| `FFT` (Packet Loss) | Same metric for the FFT stream. |
| `Waterfall` (Packet Loss) | Same metric for the waterfall stream. |
| `Meters` (Packet Loss) | Same metric for the meters stream. |
| `DAX` (Packet Loss) | Same metric for the DAX stream. |
| `Status` | Overall link state. |

All counters refresh once per second.

## Tips

- Zero loss in the Packet Loss section does not rule out the problem. Jitter and bursty late delivery can cause audio breaks without triggering sequence-number gaps. If drops are zero but audio is still broken, check `Underruns (total)`, `Underruns (last sec)`, `Audio Arrival Gap`, `Max Arrival Gap`, and `Jitter Estimate` in the **Audio Playback** section.
- `Max Latency (RTT)` is more useful than the current RTT for catching transient spikes that have already passed.
- Loss that appears on all stream categories simultaneously points to a shared network path problem rather than an audio-specific issue.

## Troubleshooting

- **All drop counters show 0 / 0** — No VITA packets have been received in that category. Confirm the radio is connected and transmitting the relevant streams.
- **RTT reads `< 1 ms` but audio is broken** — Network latency is not the cause. See the Audio Playback section for underrun and jitter data.

## Related

- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Network Diagnostics overview](overview.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

# Measure RTT and packet drops during audio problems

Use the Network Diagnostics dialog to read the current round-trip time to the radio and check whether UDP packets are being dropped — both useful first steps when audio is cutting out or sounding distorted.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but RTT and drop counters will only populate meaningful values when connected.

## Steps

1. Click `Settings > Network...`.
2. In the **Network Status** section, read **Latency (RTT)** for the current round-trip time in milliseconds.
3. Read **Max Latency (RTT)** to see the highest RTT recorded since the connection was established.
4. In the **Packet Loss (Sequence Gaps)** section, read the **Audio** drop counter. The value is shown as `<dropped> / <total> (<percent>%)`.
5. Check the **FFT**, **Waterfall**, **Meters**, and **DAX** drop counters in the same section if you want to confirm whether loss is isolated to the audio stream or affects all streams.
6. Let the dialog run for at least 30 seconds during the problem. Values refresh every second.
7. Click **Close** when finished.

## What each control does

| Indicator | What it shows |
|---|---|
| **Status** | Overall link state. |
| **Latency (RTT)** | Current round-trip time in ms. Displays `< 1 ms` when below 1 ms. |
| **Max Latency (RTT)** | Highest RTT seen since connect. Resets on reconnect. |
| **Audio** (Packet Loss) | Dropped audio packets vs. total received, with a percentage. Inferred from missing VITA sequence numbers. |
| **FFT** (Packet Loss) | Same metric for the FFT stream. |
| **Waterfall** (Packet Loss) | Same metric for the waterfall stream. |
| **Meters** (Packet Loss) | Same metric for the meters stream. |
| **DAX** (Packet Loss) | Same metric for the DAX audio stream. |

## Tips

- Zero loss in the **Packet Loss (Sequence Gaps)** section does not rule out the problem. Jitter or late-arriving bursts can cause audio glitches without triggering sequence-number gaps. If drops are zero but audio is still breaking up, check **Audio Arrival Gap**, **Max Arrival Gap**, and **Jitter Estimate** in the **Audio Playback** section.
- Large swings in the **Audio** rate under **Incoming Stream Rates** indicate bursty delivery even when no packets are counted as lost.
- **Max Latency (RTT)** accumulates from the moment of connection. If you opened the dialog after the problem started, the peak may not reflect the worst moment.

## Troubleshooting

- **All RTT fields show `< 1 ms` and drops stay at `0 / 0`** — The radio is not connected. Connect first via `Settings > Connect to Radio...`, then reopen `Settings > Network...`.
- **Audio drops are non-zero but RTT looks stable** — Loss is occurring at the UDP layer without affecting TCP ping timing. Check for Wi-Fi interference, QoS settings on switches, or other traffic competing on the same LAN segment.

## Related

- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

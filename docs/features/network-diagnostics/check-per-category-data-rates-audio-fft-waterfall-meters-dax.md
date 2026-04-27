# Check per-category data rates (audio, FFT, waterfall, meters, DAX)

The Network Diagnostics dialog shows live ingress rates for each stream category — Audio, FFT, Waterfall, Meters, and DAX — updated every second. Use this to confirm that each stream is delivering data at the expected rate and to identify which category is consuming bandwidth or dropping packets.

## Before you start

- AetherSDR must be running. The dialog opens whether or not a radio is connected, but rate values are meaningful only when connected.

## Steps

1. Click `Settings > Network...`.
2. Locate the **Incoming Stream Rates** group on the right side of the dialog.
3. Read the per-category rate indicators: **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX**. Each shows the current ingress rate in kbps, recalculated once per second.
4. Locate the **Packet Loss (Sequence Gaps)** group below the left column.
5. Read the corresponding **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX** drop indicators. Each shows dropped packets, total packets, and a loss percentage in the form `errors / total (pct%)`.
6. When finished, click Close.

## What each control does

| Indicator | Group | Meaning |
|---|---|---|
| **Audio** (rate) | Incoming Stream Rates | Ingress rate for the receiver audio stream, in kbps. |
| **FFT** (rate) | Incoming Stream Rates | Ingress rate for panadapter FFT data, in kbps. |
| **Waterfall** (rate) | Incoming Stream Rates | Ingress rate for waterfall data, in kbps. |
| **Meters** (rate) | Incoming Stream Rates | Ingress rate for meter data, in kbps. |
| **DAX** (rate) | Incoming Stream Rates | Ingress rate for DAX audio data, in kbps. |
| **Total RX** | Incoming Stream Rates | Aggregate receive rate across all stream categories, in kbps. |
| **Total TX** | Incoming Stream Rates | Aggregate transmit rate, in kbps. |
| **Audio** (drops) | Packet Loss (Sequence Gaps) | Dropped vs. total audio packets, with loss percentage. |
| **FFT** (drops) | Packet Loss (Sequence Gaps) | Dropped vs. total FFT packets, with loss percentage. |
| **Waterfall** (drops) | Packet Loss (Sequence Gaps) | Dropped vs. total waterfall packets, with loss percentage. |
| **Meters** (drops) | Packet Loss (Sequence Gaps) | Dropped vs. total meter packets, with loss percentage. |
| **DAX** (drops) | Packet Loss (Sequence Gaps) | Dropped vs. total DAX packets, with loss percentage. |

All rate values are computed from the byte-count delta over the preceding one-second interval and expressed as kbps. Drop counts are inferred from missing VITA-49 sequence numbers.

## Tips

- A rate of 0 kbps for a category that should be active (for example, **Audio** while a slice is open) indicates the stream has stopped arriving. Check the **Status** indicator in the **Network Status** group first.
- Large swings in a category rate from second to second can indicate bursty delivery even when the drop count remains at zero.
- Zero drops in the **Packet Loss** group does not rule out jitter or late-arriving bursts. If audio is choppy but drops show zero, check the **Audio Playback** group for underruns and jitter.

## Troubleshooting

- **All category rates show 0 kbps** — The radio is not streaming. Confirm the connection is active by checking **Status** and **Target Radio IP** in the **Network Status** group. Reconnect via `Settings > Connect to Radio...` if needed.
- **DAX rate shows 0 kbps while DAX is expected** — DAX streaming may not be enabled. Verify DAX is started; on supported platforms, check `Settings > Autostart DAX with AetherSDR`.
- **Drop percentage is non-zero on one category only** — Loss is isolated to that stream. This can indicate the radio is overloaded for that specific data type or that a network queue is preferentially dropping UDP packets of that size.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

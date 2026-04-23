# Check per-category data rates (audio, FFT, waterfall, meters, DAX)

The Network Diagnostics dialog shows live ingress rates for each stream category — Audio, FFT, Waterfall, Meters, and DAX — updated every second. Use this view to confirm that each stream type is flowing and to spot which category is consuming bandwidth when the link is under pressure.

## Before you start

- AetherSDR must be running. The dialog opens whether or not a radio is connected, but rates will read zero until a connection is active.
- A radio connection is recommended so that live data populates the rate fields.

## Steps

1. Click `Settings > Network...`.
2. The **Network Diagnostics** dialog opens. Locate the **Incoming Stream Rates** group on the right side of the dialog.
3. Read the per-category rate fields: **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX**. Each value is expressed in kbps and updates once per second.
4. Check **Total RX** for the aggregate inbound rate across all categories.
5. Check **Total TX** for the aggregate outbound rate.
6. To see whether any category is losing packets alongside its rate, look at the corresponding row in the **Packet Loss (Sequence Gaps)** group: **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX** drop counters appear there as `errors / total packets (%)`.
7. Click `Close` when finished.

## What each control does

| Indicator | What it shows |
|---|---|
| **Audio** (Incoming Stream Rates) | Inbound rate for the receive audio stream, in kbps. |
| **FFT** (Incoming Stream Rates) | Inbound rate for panadapter FFT data, in kbps. |
| **Waterfall** (Incoming Stream Rates) | Inbound rate for waterfall tile data, in kbps. |
| **Meters** (Incoming Stream Rates) | Inbound rate for meter data, in kbps. |
| **DAX** (Incoming Stream Rates) | Inbound rate for DAX audio streams, in kbps. |
| **Total RX** | Aggregate inbound bytes per second across all categories, in kbps. |
| **Total TX** | Aggregate outbound bytes per second, in kbps. |
| **Audio** (Packet Loss) | Dropped audio packets shown as `errors / total (%)`. |
| **FFT** (Packet Loss) | Dropped FFT packets shown as `errors / total (%)`. |
| **Waterfall** (Packet Loss) | Dropped waterfall packets shown as `errors / total (%)`. |
| **Meters** (Packet Loss) | Dropped meter packets shown as `errors / total (%)`. |
| **DAX** (Packet Loss) | Dropped DAX packets shown as `errors / total (%)`. |

## Tips

- Rates are computed from the change in byte counts over each one-second refresh interval. Large swings between seconds can indicate bursty delivery even when the drop counters remain at zero.
- A DAX rate of 0 kbps when DAX is expected to be active is a useful early signal that the DAX bridge is not running or not receiving data from the radio.
- Zero drop counts do not rule out jitter or late-arriving bursts. If audio quality is poor despite clean drop counts, check the **Audio Playback** group for underrun and jitter data.

## Troubleshooting

- **All rates show 0 kbps** — The radio is not connected or no streams have started. Verify the connection using `Settings > Connect to Radio...` and check the **Status** field in the **Network Status** group.
- **DAX rate is 0 kbps but other categories show traffic** — DAX may not be enabled. Check whether DAX autostart is active via `Settings > Autostart DAX with AetherSDR`.
- **Drop percentage is non-zero on FFT or Waterfall but audio sounds fine** — Visual stream drops are typically less noticeable than audio drops. Monitor over time; sustained loss above a few percent warrants investigating the network path.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

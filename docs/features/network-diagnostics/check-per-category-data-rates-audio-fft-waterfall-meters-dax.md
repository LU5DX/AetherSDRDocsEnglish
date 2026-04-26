# Check per-category data rates (audio, FFT, waterfall, meters, DAX)

The Network Diagnostics dialog shows live ingress rates for each stream category — Audio, FFT, Waterfall, Meters, and DAX — updated once per second. Use this to identify which stream type is consuming bandwidth or receiving no data during reception problems.

## Before you start

- AetherSDR must be running. The dialog opens whether or not a radio is connected, but rates will read 0 kbps until a connection is established.

## Steps

1. Click `Settings > Network...`.
2. Locate the **Incoming Stream Rates** group on the right side of the dialog.
3. Read the per-category values: **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX** each show a current rate in kbps, updated every second.
4. To check how many packets were dropped for each category, locate the **Packet Loss (Sequence Gaps)** group on the lower left. It lists **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX** drop counts in the format `errors / total packets (%)`.
5. When finished, click Close.

## What each control does

| Indicator | Location | Meaning |
|---|---|---|
| **Audio** (rate) | Incoming Stream Rates | Ingress rate for the receive audio stream, in kbps. |
| **FFT** (rate) | Incoming Stream Rates | Ingress rate for panadapter FFT data, in kbps. |
| **Waterfall** (rate) | Incoming Stream Rates | Ingress rate for waterfall tile data, in kbps. |
| **Meters** (rate) | Incoming Stream Rates | Ingress rate for meter data, in kbps. |
| **DAX** (rate) | Incoming Stream Rates | Ingress rate for DAX audio streams, in kbps. |
| **Total RX** | Incoming Stream Rates | Aggregate inbound rate across all streams, in kbps. |
| **Total TX** | Incoming Stream Rates | Aggregate outbound rate, in kbps. |
| **Audio** (drops) | Packet Loss (Sequence Gaps) | Audio packet errors vs. total packets received, with percentage. |
| **FFT** (drops) | Packet Loss (Sequence Gaps) | FFT packet errors vs. total packets received, with percentage. |
| **Waterfall** (drops) | Packet Loss (Sequence Gaps) | Waterfall packet errors vs. total packets received, with percentage. |
| **Meters** (drops) | Packet Loss (Sequence Gaps) | Meter packet errors vs. total packets received, with percentage. |
| **DAX** (drops) | Packet Loss (Sequence Gaps) | DAX packet errors vs. total packets received, with percentage. |

Rates are expressed in kbps and are recalculated from byte-count deltas each second. Drop counts are inferred from missing VITA sequence numbers.

## Tips

- A category showing 0 kbps while the radio is connected and that stream should be active points to a configuration or routing problem on that specific stream, not a general network failure.
- Large swings in a category rate from second to second can indicate bursty delivery even when the drop count is zero. Check **Waterfall** and **FFT** rates together: if waterfall is bursty but FFT is steady, the issue is likely with waterfall tile scheduling rather than the network path.
- The drop percentage is only meaningful once **total packets** is non-zero. A display of `0 / 0` means no packets have been received for that category yet.

## Troubleshooting

- **All rates show 0 kbps** — The radio is not connected or no streams have been started. Confirm connection status in the **Network Status** group: **Target Radio IP** should show an IP address, not "Not connected".
- **DAX rate shows 0 kbps but other streams are active** — DAX audio bridging may not be enabled. Check `Settings > Autostart DAX with AetherSDR` or start DAX manually from the applet panel.
- **Drop count climbs on one category while others stay at zero** — Loss is specific to that stream type. This can indicate the radio is sending more data than the network path can sustain for that particular stream; try reducing the FFT or waterfall update rate in radio settings.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

# Check per-category data rates (audio, FFT, waterfall, meters, DAX)

The Network Diagnostics dialog shows live ingress rates for each stream category — Audio, FFT, Waterfall, Meters, and DAX — updated every second. Use this to confirm the radio is delivering data on each stream and to spot bursty or missing traffic before it causes audio or display problems.

## Before you start

- AetherSDR must be running. The dialog is available whether or not a radio is connected, but rates will read zero until a connection is active.
- If you want to observe rates under load, have at least one panadapter and receiver active before opening the dialog.

## Steps

1. Click `Settings > Network...`.
2. In the **Network Diagnostics** dialog, locate the **Incoming Stream Rates** group on the right side of the window.
3. Read the per-category rate values: **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX**. Each value is displayed in kbps and refreshes once per second.
4. Read **Total RX** and **Total TX** below the category rows to see aggregate throughput in both directions.
5. Click Close when done.

## What each control does

| Indicator | What it shows |
|---|---|
| **Audio** (Incoming Stream Rates) | Ingress rate of the receive audio stream, in kbps. |
| **FFT** (Incoming Stream Rates) | Ingress rate of the panadapter FFT data stream, in kbps. |
| **Waterfall** (Incoming Stream Rates) | Ingress rate of the waterfall data stream, in kbps. |
| **Meters** (Incoming Stream Rates) | Ingress rate of the meter data stream, in kbps. |
| **DAX** (Incoming Stream Rates) | Ingress rate of the DAX audio stream, in kbps. |
| **Total RX** | Aggregate bytes per second received from the radio, in kbps. |
| **Total TX** | Aggregate bytes per second sent to the radio, in kbps. |
| **Audio** (Packet Loss) | Dropped packets inferred from missing VITA sequence numbers, shown as errors / total packets (%). |
| **FFT** (Packet Loss) | Same, for the FFT stream. |
| **Waterfall** (Packet Loss) | Same, for the waterfall stream. |
| **Meters** (Packet Loss) | Same, for the meter stream. |
| **DAX** (Packet Loss) | Same, for the DAX stream. |

All rate values are recalculated from byte-count deltas once per second. Drop counts are cumulative since the connection was established.

## Tips

- A category rate of 0 kbps while the radio is connected indicates that stream is not active or not subscribed. For example, DAX will read 0 kbps if DAX audio is not enabled.
- Large swings in a category rate from second to second can indicate bursty delivery even when the drop counters show zero loss. The in-dialog note for this group states: "Large swings can indicate bursty delivery even when no packets are lost."
- Drop counts are displayed as `errors / total packets (%)`. A value of `0 / 0` means no packets have been counted for that category yet.

## Troubleshooting

- **All category rates show 0 kbps** — No radio connection is active, or the connection was lost. Check **Status** and **Target Radio IP** in the **Network Status** group.
- **DAX rate shows 0 kbps but other streams are active** — DAX audio is not enabled. Enable DAX from the applet panel or check `Settings > Autostart DAX with AetherSDR`.
- **Drop count is non-zero for a category** — Packets with missing VITA sequence numbers were detected on that stream. This points to network packet loss on that specific stream type. See [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md) for further steps.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

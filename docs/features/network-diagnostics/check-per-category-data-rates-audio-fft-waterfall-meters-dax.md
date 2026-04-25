# Check per-category data rates (audio, FFT, waterfall, meters, DAX)

The Network Diagnostics dialog shows live ingress rates and packet-drop counts for each stream category — Audio, FFT, Waterfall, Meters, and DAX — updated once per second. Use this to identify which stream type is consuming bandwidth or losing packets during a problem.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but rate fields will read 0 kbps until the radio is connected and streaming.

## Steps

1. Click `Settings > Network...`.
2. The **Network Diagnostics** dialog opens. Locate the **Incoming Stream Rates** group on the upper-right side of the dialog.
3. Read the per-category rate fields: **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX**. Each shows the current ingress rate in kbps, recalculated every second.
4. Locate the **Packet Loss (Sequence Gaps)** group on the lower-left side. Read the matching **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX** drop fields. Each shows dropped packets, total packets, and a loss percentage.
5. Watch both groups for several seconds to see whether rates are steady or swinging. Large swings can indicate bursty delivery even when no packets are dropped.
6. Click **Close** when finished.

## What each control does

| Indicator | Location | Meaning |
|---|---|---|
| **Audio** (Incoming Stream Rates) | Incoming Stream Rates group | Ingress rate for the audio stream, in kbps. |
| **FFT** (Incoming Stream Rates) | Incoming Stream Rates group | Ingress rate for FFT (panadapter spectrum) data, in kbps. |
| **Waterfall** (Incoming Stream Rates) | Incoming Stream Rates group | Ingress rate for waterfall tile data, in kbps. |
| **Meters** (Incoming Stream Rates) | Incoming Stream Rates group | Ingress rate for meter data, in kbps. |
| **DAX** (Incoming Stream Rates) | Incoming Stream Rates group | Ingress rate for DAX audio data, in kbps. |
| **Total RX** | Incoming Stream Rates group | Aggregate inbound rate across all streams, in kbps. |
| **Total TX** | Incoming Stream Rates group | Aggregate outbound rate, in kbps. |
| **Audio** (Packet Loss) | Packet Loss (Sequence Gaps) group | Dropped / total audio packets and percentage, inferred from VITA sequence gaps. |
| **FFT** (Packet Loss) | Packet Loss (Sequence Gaps) group | Dropped / total FFT packets and percentage. |
| **Waterfall** (Packet Loss) | Packet Loss (Sequence Gaps) group | Dropped / total waterfall packets and percentage. |
| **Meters** (Packet Loss) | Packet Loss (Sequence Gaps) group | Dropped / total meter packets and percentage. |
| **DAX** (Packet Loss) | Packet Loss (Sequence Gaps) group | Dropped / total DAX packets and percentage. |

Rates are computed from the byte-count delta over the preceding one-second interval and expressed as kbps. Drop percentages are cumulative since the dialog was opened.

## Tips

- Zero drops in the **Packet Loss (Sequence Gaps)** group does not rule out jitter or late packet bursts. If audio is breaking up with zero drops, check the **Audio Playback** group for underrun and jitter figures.
- A DAX rate of 0 kbps while DAX is enabled can indicate the DAX bridge has not yet started or is not routing audio. Verify autostart state under `Settings > Autostart DAX with AetherSDR`.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

# Network Diagnostics overview

The Network Diagnostics dialog gives you a live, read-only view of the link between AetherSDR and your FLEX-8600. Use it to confirm the radio's IP and connection path, measure latency, check per-stream data rates, and diagnose audio problems such as underruns and jitter.

## Before you start

- No radio connection is required to open the dialog, but most indicators will be empty or show "Not connected" until you connect to a radio.

## How it works

Open the dialog with `Settings > Network...`. It refreshes all indicators once per second. Click Close when you are done.

The dialog is divided into four sections.

### Network Status

Confirms the connection path and TCP latency.

| Indicator | What it shows |
|---|---|
| Status | Overall link state. |
| Target Radio IP | IP address of the connected radio, or "Not connected". |
| Selected Source | Local NIC or bind path used for the connection. |
| Local TCP | Local TCP endpoint. |
| Local UDP | Local UDP endpoint. |
| First UDP Packet | "Yes" or "No" — whether a UDP packet has been received since connect. |
| Latency (RTT) | Current round-trip time in ms. Values below 1 ms display as "< 1 ms". |
| Max Latency (RTT) | Highest RTT seen since connecting. |

### Incoming Stream Rates

Shows the current receive and transmit bitrate for each stream type. Large swings can indicate bursty delivery even when no packets are dropped.

| Indicator | What it shows |
|---|---|
| Audio | Ingress rate of the audio stream, in kbps. |
| FFT | Ingress rate of the FFT stream, in kbps. |
| Waterfall | Ingress rate of the waterfall stream, in kbps. |
| Meters | Ingress rate of the meter stream, in kbps. |
| DAX | Ingress rate of the DAX stream, in kbps. |
| Total RX | Aggregate inbound bytes per second. |
| Total TX | Aggregate outbound bytes per second. |

### Packet Loss (Sequence Gaps)

Reports inferred packet loss derived from missing VITA sequence numbers. A zero count here does not rule out jitter or late packet bursts.

| Indicator | What it shows |
|---|---|
| Audio | Dropped packets / total packets (percentage) for the audio stream. |
| FFT | Dropped packets / total packets (percentage) for the FFT stream. |
| Waterfall | Dropped packets / total packets (percentage) for the waterfall stream. |
| Meters | Dropped packets / total packets (percentage) for the meter stream. |
| DAX | Dropped packets / total packets (percentage) for the DAX stream. |

### Audio Playback

Reflects speaker-side buffer health. If underruns rise while the buffer stays near zero, playback is starving. Arrival gap and jitter measure timing irregularity, not packet loss.

| Indicator | What it shows |
|---|---|
| RX Buffer Now | Current audio buffer fill, in bytes and ms. |
| RX Buffer Peak | Peak audio buffer fill seen since connect, in bytes and ms. |
| Underruns (total) | Cumulative audio buffer underrun count. |
| Underruns (last sec) | Underruns that occurred in the most recent one-second interval. |
| Audio Arrival Gap | Inter-packet arrival time, in ms. |
| Max Arrival Gap | Largest inter-packet arrival gap seen, in ms. |
| Jitter Estimate | Smoothed jitter of the audio stream, in ms. |

## Tips

- The dialog can remain open while you operate. Keeping it visible during an audio problem lets you watch all four sections simultaneously.
- Zero drops in the Packet Loss section does not mean the link is problem-free. Check Jitter Estimate and Max Arrival Gap for timing irregularities that can cause audio artifacts without dropping packets.

## Related

- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Watch the first-UDP-packet timestamp after connect](../../getting-started/setup/watch-the-first-udp-packet-timestamp-after-connect.md)

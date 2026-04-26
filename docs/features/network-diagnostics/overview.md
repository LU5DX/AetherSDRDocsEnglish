# Network Diagnostics overview

The Network Diagnostics dialog gives you a live, continuously updated view of the link between AetherSDR and your FLEX-8600. Use it to confirm connectivity details, measure latency, watch per-stream data rates, and identify the source of audio problems such as underruns and jitter.

## Before you start

- No radio connection is required to open the dialog, but most indicators will be empty or show "Not connected" unless AetherSDR is connected to a radio.

## How it works

Open the dialog via `Settings > Network...`. It refreshes all indicators once per second automatically. Click Close when you are done.

The dialog is divided into four groups:

**Network Status** — connection path and TCP latency.

**Incoming Stream Rates** — current bitrates per stream type, plus aggregate totals.

**Packet Loss (Sequence Gaps)** — dropped-packet counts inferred from missing VITA-49 sequence numbers.

**Audio Playback** — speaker-side buffer health, underrun counters, and timing metrics.

## What each control does

### Network Status

| Indicator | What it shows |
|---|---|
| Status | Overall link state reported by the radio model. |
| Target Radio IP | IP address of the connected radio. Shows "Not connected" when no radio is linked. |
| Selected Source | Local network interface or bind path used for the connection. |
| Local TCP | Local TCP endpoint (address and port). |
| Local UDP | Local UDP endpoint (address and port). |
| First UDP Packet | Whether the first UDP packet has been received since connect ("Yes" or "No"). |
| Latency (RTT) | Current round-trip time in milliseconds. Displays "< 1 ms" when below 1 ms. |
| Max Latency (RTT) | Highest RTT recorded since the current connection was established. |

### Incoming Stream Rates

| Indicator | What it shows |
|---|---|
| Audio | Ingress bitrate for the audio stream, in kbps. |
| FFT | Ingress bitrate for the FFT stream, in kbps. |
| Waterfall | Ingress bitrate for the waterfall stream, in kbps. |
| Meters | Ingress bitrate for the meters stream, in kbps. |
| DAX | Ingress bitrate for the DAX stream, in kbps. |
| Total RX | Aggregate inbound bytes per second across all streams, in kbps. |
| Total TX | Aggregate outbound bytes per second, in kbps. |

Large swings in individual stream rates can indicate bursty delivery even when no packets are dropped.

### Packet Loss (Sequence Gaps)

| Indicator | What it shows |
|---|---|
| Audio | Dropped vs. total packets for the audio stream, with percentage. |
| FFT | Dropped vs. total packets for the FFT stream, with percentage. |
| Waterfall | Dropped vs. total packets for the waterfall stream, with percentage. |
| Meters | Dropped vs. total packets for the meters stream, with percentage. |
| DAX | Dropped vs. total packets for the DAX stream, with percentage. |

Zero loss here does not rule out jitter or late packet bursts.

### Audio Playback

| Indicator | What it shows |
|---|---|
| RX Buffer Now | Current audio receive buffer fill, in bytes and milliseconds. |
| RX Buffer Peak | Highest buffer fill recorded since connect, in bytes and milliseconds. |
| Underruns (total) | Cumulative count of audio buffer underruns since connect. |
| Underruns (last sec) | Underruns that occurred in the most recent one-second interval. |
| Audio Arrival Gap | Time between consecutive incoming audio packets. |
| Max Arrival Gap | Largest inter-packet arrival gap recorded since connect. |
| Network Jitter | Smoothed jitter estimate for the audio stream. |

If underruns rise while RX Buffer Now stays near zero, the audio path is starving. Arrival Gap and Network Jitter measure timing, not packet loss.

### Button

| Control | Behavior |
|---|---|
| Close | Closes the dialog. |

## Tips

- The dialog does not require a connected radio to open. You can open it before connecting to confirm no stale values are present.
- All indicators reset their peak and cumulative values when a new connection is established.
- Zero packet loss in the Packet Loss group does not guarantee clean audio. Check Network Jitter and Underruns (last sec) as well.

## Related

- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Watch the first-UDP-packet timestamp after connect](../../getting-started/setup/watch-the-first-udp-packet-timestamp-after-connect.md)

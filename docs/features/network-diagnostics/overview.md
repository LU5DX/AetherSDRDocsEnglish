# Network Diagnostics overview

The Network Diagnostics dialog gives you a live view of the link between AetherSDR and your FLEX-8600. Use it to inspect TCP/UDP endpoints, round-trip time, per-category data rates, packet loss, and audio buffer health — all updated once per second without requiring an active radio connection.

## How it works

Open the dialog from `Settings > Network...`. It refreshes automatically every second. All indicators are read-only; there is nothing to configure here. Click Close when you are done.

The dialog is divided into four groups:

### Network Status

Confirms which network path AetherSDR is using and how responsive it is.

| Indicator | What it shows |
|---|---|
| Status | Overall link state. |
| Target Radio IP | IP address of the connected radio, or "Not connected". |
| Selected Source | Local NIC or bind path used for the connection. |
| Local TCP | Local TCP endpoint (address and port). |
| Local UDP | Local UDP endpoint (address and port). |
| First UDP Packet | Whether the first inbound UDP packet has been received ("Yes" or "No"). |
| Latency (RTT) | Current round-trip time in milliseconds, reported as "< 1 ms" when below 1 ms. |
| Max Latency (RTT) | Highest RTT recorded since the last connect. |

### Incoming Stream Rates

Shows current receive and transmit bitrates broken down by stream type. Large swings can indicate bursty delivery even when no packets are dropped.

| Indicator | What it shows |
|---|---|
| Audio | Ingress rate for the audio stream, in kbps. |
| FFT | Ingress rate for FFT data, in kbps. |
| Waterfall | Ingress rate for waterfall data, in kbps. |
| Meters | Ingress rate for meter data, in kbps. |
| DAX | Ingress rate for DAX audio, in kbps. |
| Total RX | Aggregate inbound rate across all streams, in kbps. |
| Total TX | Aggregate outbound rate, in kbps. |

### Packet Loss (Sequence Gaps)

Reports inferred packet loss derived from missing VITA-49 sequence numbers. Zero here does not rule out jitter or late packet bursts.

| Indicator | What it shows |
|---|---|
| Audio | Dropped packets / total packets (percentage) for the audio stream. |
| FFT | Dropped / total for FFT data. |
| Waterfall | Dropped / total for waterfall data. |
| Meters | Dropped / total for meter data. |
| DAX | Dropped / total for DAX audio. |

### Audio Playback

Reports speaker-side buffer health. Rising underruns combined with a near-zero buffer indicate the playback pipeline is starving. Arrival gap and jitter measure packet timing, not packet loss.

| Indicator | What it shows |
|---|---|
| RX Buffer Now | Current audio buffer fill, in bytes and milliseconds. |
| RX Buffer Peak | Highest buffer fill recorded since connect, in bytes and milliseconds. |
| Underruns (total) | Cumulative audio buffer underrun count. |
| Underruns (last sec) | Underruns that occurred in the most recent one-second interval. |
| Audio Arrival Gap | Measured gap between consecutive incoming audio packet arrivals. |
| Max Arrival Gap | Largest arrival gap recorded since connect. |
| Network Jitter | Smoothed jitter estimate for the audio stream. |

## Controls

| Control | Behavior |
|---|---|
| Close | Closes the dialog. |

## Tips

- The dialog does not require an active radio connection to open, but most indicators will show placeholder values until a connection is established.
- Packet loss indicators count sequence-number gaps in VITA-49 streams. A count of zero does not guarantee clean delivery — use the Audio Playback group to check for timing problems independently.
- "< 1 ms" in RTT fields means the measured value is below 1 ms, not that measurement failed.

## Related

- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Watch the first-UDP-packet timestamp after connect](../../getting-started/setup/watch-the-first-udp-packet-timestamp-after-connect.md)

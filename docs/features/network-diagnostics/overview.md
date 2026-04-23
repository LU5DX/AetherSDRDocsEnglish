# Network Diagnostics overview

The Network Diagnostics dialog gives you a live view of the link between AetherSDR and your Flex radio: connection endpoints, round-trip latency, per-stream data rates, packet loss counts, and audio buffer health. Use it to confirm your network path is stable or to isolate the cause of audio dropouts and waterfall stuttering.

## How it works

Open the dialog with `Settings > Network...`. It does not require an active radio connection, though most indicators will show placeholder values until you connect.

All values refresh automatically once per second. The dialog is read-only — no settings are changed here. Click Close when you are done.

The dialog is organized into four groups.

### Network Status

Connection path and TCP latency. Confirms which route AetherSDR is using to reach the radio.

| Indicator | What it shows |
|---|---|
| Status | Overall link state. |
| Target Radio IP | IP address of the connected radio. Shows "Not connected" when no radio is present. |
| Selected Source | Local network interface or bind path used for the connection. |
| Local TCP | Local TCP endpoint (address and port). |
| Local UDP | Local UDP endpoint (address and port). |
| First UDP Packet | Whether a UDP packet has been received since connect (Yes / No). |
| Latency (RTT) | Current round-trip time in milliseconds. Displays "< 1 ms" when below 1 ms. |
| Max Latency (RTT) | Highest RTT recorded since the last connect. |

### Incoming Stream Rates

Current receive and transmit bitrates by stream type, in kbps. Large swings can indicate bursty delivery even when no packets are lost.

| Indicator | What it shows |
|---|---|
| Audio | Ingress rate for the audio stream. |
| FFT | Ingress rate for the FFT (panadapter) stream. |
| Waterfall | Ingress rate for the waterfall stream. |
| Meters | Ingress rate for the meters stream. |
| DAX | Ingress rate for the DAX audio stream. |
| Total RX | Aggregate inbound bytes per second across all streams. |
| Total TX | Aggregate outbound bytes per second. |

### Packet Loss (Sequence Gaps)

Inferred packet loss derived from missing VITA-49 sequence numbers. Each entry shows dropped packets, total packets, and a percentage. Zero loss here does not rule out jitter or late bursts.

| Indicator | What it shows |
|---|---|
| Audio | Drop count and rate for the audio stream. |
| FFT | Drop count and rate for the FFT stream. |
| Waterfall | Drop count and rate for the waterfall stream. |
| Meters | Drop count and rate for the meters stream. |
| DAX | Drop count and rate for the DAX stream. |

### Audio Playback

Speaker-side buffer health. If underruns rise while the buffer stays near zero, playback is starving. Arrival gap and jitter measure timing, not packet loss.

| Indicator | What it shows |
|---|---|
| RX Buffer Now | Current audio buffer fill, in bytes and milliseconds. |
| RX Buffer Peak | Highest buffer fill recorded since connect. |
| Underruns (total) | Cumulative audio underrun count. |
| Underruns (last sec) | Underruns recorded in the most recent one-second window. |
| Audio Arrival Gap | Inter-packet arrival interval for the most recent audio packet. |
| Max Arrival Gap | Largest inter-packet arrival interval seen since connect. |
| Jitter Estimate | Smoothed jitter of the incoming audio stream. |

## Controls

| Control | Behavior |
|---|---|
| Close | Closes the dialog. |

## Tips

- The dialog can be left open while operating. Because it refreshes every second, it has negligible impact on the UI.
- Zero drops in the Packet Loss group do not guarantee clean audio. Check Jitter Estimate and Max Arrival Gap for timing-related problems even when loss is zero.
- Max Latency (RTT) accumulates from the moment of connect. Reconnect to the radio to reset it.

## Related

- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Watch the first-UDP-packet timestamp after connect](../../getting-started/setup/watch-the-first-udp-packet-timestamp-after-connect.md)

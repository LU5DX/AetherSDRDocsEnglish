# Network Diagnostics overview

The Network Diagnostics dialog gives you a live, per-second view of the network link between AetherSDR and your FLEX-8600. Use it to confirm connection endpoints, measure latency, inspect per-stream data rates, and diagnose audio buffer problems.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected, but most indicators will be empty until a connection is established.

## How it works

Open the dialog with `Settings > Network...`. All indicators update once per second automatically. Click Close when finished.

The dialog is divided into four groups:

### Network Status

Connection path and TCP latency. Confirms which route AetherSDR is using to reach the radio.

| Indicator | What it shows |
|---|---|
| Status | Overall link state. |
| Target Radio IP | IP address of the connected radio. Shows "Not connected" when no radio is linked. |
| Selected Source | Local network interface or bind path used for the connection. |
| Local TCP | Local TCP endpoint (address and port). |
| Local UDP | Local UDP endpoint (address and port). |
| First UDP Packet | Whether the first UDP packet has been received since connect ("Yes" or "No"). |
| Latency (RTT) | Current round-trip time in milliseconds. Displays "< 1 ms" when below 1 ms. |
| Max Latency (RTT) | Highest RTT measured since the radio connected. |

### Incoming Stream Rates

Per-category ingress rates and aggregate totals. Large swings indicate bursty delivery even when no packets are dropped.

| Indicator | What it shows |
|---|---|
| Audio | Incoming audio stream rate in kbps. |
| FFT | Incoming FFT stream rate in kbps. |
| Waterfall | Incoming waterfall stream rate in kbps. |
| Meters | Incoming meters stream rate in kbps. |
| DAX | Incoming DAX stream rate in kbps. |
| Total RX | Aggregate inbound rate across all streams in kbps. |
| Total TX | Aggregate outbound rate in kbps. |

### Packet Loss (Sequence Gaps)

Drop counts inferred from missing VITA sequence numbers. A zero count here does not rule out jitter or late delivery bursts.

| Indicator | What it shows |
|---|---|
| Audio | Dropped packets / total packets (percent) for the audio stream. |
| FFT | Dropped packets / total packets (percent) for the FFT stream. |
| Waterfall | Dropped packets / total packets (percent) for the waterfall stream. |
| Meters | Dropped packets / total packets (percent) for the meters stream. |
| DAX | Dropped packets / total packets (percent) for the DAX stream. |

### Audio Playback

Speaker-side buffer health. If underruns increase while the buffer stays near zero, playback is starving. Arrival gap and jitter measure timing, not packet loss.

| Indicator | What it shows |
|---|---|
| RX Buffer Now | Current audio receive buffer fill, in bytes and milliseconds. |
| RX Buffer Peak | Highest buffer fill seen since connect, in bytes and milliseconds. |
| Underruns (total) | Cumulative audio buffer underrun count since connect. |
| Underruns (last sec) | Audio buffer underruns that occurred in the most recent one-second interval. |
| Audio Arrival Gap | Time gap between consecutive incoming audio packets. |
| Max Arrival Gap | Largest arrival gap seen since connect. |
| Network Jitter | Smoothed jitter estimate of the incoming audio stream. |

## Controls

| Control | Behavior |
|---|---|
| Close | Closes the dialog. |

## Tips

- The dialog can remain open while you operate. All values refresh every second without any interaction required.
- Packet loss counts in the Packet Loss group are cumulative since the dialog was opened; close and reopen the dialog to reset the baseline.
- Zero packet loss combined with rising underruns points to a jitter or timing problem rather than outright loss — check Audio Arrival Gap and Network Jitter in that case.

## Related

- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Watch the first-UDP-packet timestamp after connect](../../getting-started/setup/watch-the-first-udp-packet-timestamp-after-connect.md)

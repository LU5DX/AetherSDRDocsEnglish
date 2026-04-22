# Measure RTT and packet drops during audio problems

Use the Network Diagnostics dialog to read live round-trip time and per-category packet drop counts while an audio problem is occurring. This helps you distinguish network loss from local audio starvation.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but meaningful RTT and drop data only appear after the radio is connected.
- Reproduce or sustain the audio problem so the counters are actively updating when you read them.

## Steps

1. Click `Settings > Network...`. The Network Diagnostics dialog opens.
2. Look at the **Latency (RTT)** indicator. This shows the current round-trip time to the radio in milliseconds. Values below 1 ms are displayed as `< 1 ms`.
3. Look at **Max Latency (RTT)**. This shows the highest RTT measured since the connection was established. A large gap between **Latency (RTT)** and **Max Latency (RTT)** indicates the link has spiked.
4. Under the **Packet Loss (Sequence Gaps)** group, read the **Audio** drop indicator. The value is shown as `errors / total packets (%)`. Any non-zero error count during audio problems points to network packet loss on the audio stream.
5. Check the remaining drop rows — **FFT**, **Waterfall**, **Meters**, and **DAX** — to determine whether loss is limited to audio or affects all stream categories. Loss across all categories suggests a general link problem rather than an audio-specific one.
6. Note the **Status** indicator for the overall link state.
7. Click **Close** when you are done.

## What each control does

| Indicator | Where it appears | Meaning |
|---|---|---|
| **Status** | Network Status group | Overall link state reported by the radio model. |
| **Latency (RTT)** | Network Status group | Current round-trip time, updated every second. Displayed in ms; shown as `< 1 ms` when below 1 ms. |
| **Max Latency (RTT)** | Network Status group | Highest RTT recorded since connect. Resets on reconnect. |
| **Audio** (Packet Loss) | Packet Loss (Sequence Gaps) group | Dropped audio packets inferred from missing VITA sequence numbers, shown as `errors / total (%)`. |
| **FFT** (Packet Loss) | Packet Loss (Sequence Gaps) group | Same metric for the FFT stream. |
| **Waterfall** (Packet Loss) | Packet Loss (Sequence Gaps) group | Same metric for the waterfall stream. |
| **Meters** (Packet Loss) | Packet Loss (Sequence Gaps) group | Same metric for the meters stream. |
| **DAX** (Packet Loss) | Packet Loss (Sequence Gaps) group | Same metric for the DAX stream. |

All indicators refresh every second. There are no persisted settings in this dialog.

## Tips

- Zero packet loss in the **Packet Loss (Sequence Gaps)** group does not rule out the problem. Jitter and late bursts can cause audio underruns without producing sequence-number gaps. If drops are zero but audio is still broken, check the **Audio Playback** group instead.
- Large swings in the **Incoming Stream Rates** group — even without dropped packets — can indicate bursty delivery that degrades audio.
- **Max Latency (RTT)** accumulates from the moment of connection. If you connected long before the audio problem started, the peak may predate the current issue. Disconnect and reconnect to reset it, then reproduce the problem.

## Troubleshooting

- **All indicators show dashes or zero with no radio connected** — RTT and drop data require an active radio connection. Connect to the radio first, then reopen the dialog.
- **Audio drops are zero but audio is still cutting out** — Network loss is not the cause. See [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md) for buffer and jitter analysis.

## Related

- [Network Diagnostics overview](overview.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)

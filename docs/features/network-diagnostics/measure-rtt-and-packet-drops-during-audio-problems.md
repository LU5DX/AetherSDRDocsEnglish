# Measure RTT and packet drops during audio problems

Use the Network Diagnostics dialog to read live round-trip time and per-category packet-drop counts while audio problems occur. This lets you distinguish network loss from other causes such as buffer starvation or jitter.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but RTT and drop counters are only meaningful while connected.
- Reproduce or wait for the audio problem to occur before reading the counters — drop counts accumulate since connect and RTT reflects the current moment.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Read `Latency (RTT)` for the current round-trip time to the radio.
3. Read `Max Latency (RTT)` for the highest RTT recorded since the connection was established.
4. Under the **Packet Loss (Sequence Gaps)** section, read the `Audio` drop counter. The value shows dropped packets, total packets, and a loss percentage.
5. Check the `FFT`, `Waterfall`, `Meters`, and `DAX` drop rows in the same section to see whether loss is isolated to audio or affects all streams.
6. Click `Close` when finished.

## What each control does

| Indicator                 | Meaning                                                                                                                                                                                                                          | Notes                                                                                                   |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| `Latency (RTT)`           | Current round-trip time to the radio. Displays `< 1 ms` when below 1 ms.                                                                                                                                                         |                                                                                                         |
| `Max Latency (RTT)`       | Highest RTT seen since connect. Displays `< 1 ms` when below 1 ms.                                                                                                                                                               |                                                                                                         |
| `Audio` (Packet Loss)     | Dropped packets / total packets (loss %) for the audio stream, inferred from missing VITA sequence numbers.                                                                                                                      |                                                                                                         |
| `FFT` (Packet Loss)       | Same metric for the FFT stream.                                                                                                                                                                                                  |                                                                                                         |
| `Waterfall` (Packet Loss) | Same metric for the waterfall stream.                                                                                                                                                                                            |                                                                                                         |
| `Meters` (Packet Loss)    | Same metric for the meters stream.                                                                                                                                                                                               |                                                                                                         |
| `DAX` (Packet Loss)       | Same metric for the DAX stream.                                                                                                                                                                                                  |                                                                                                         |
| `Status`                  | Overall link quality, color-coded green (Excellent) through red (Poor).                                                                                                                                                          |                                                                                                         |
| Overview (tab)            | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer).                                                     |                                                                                                         |
| Details (tab)             | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.                                                                                                           |                                                                                                         |
| Latency (tab)             | Full-width time-series graph of RTT, arrival gap and jitter in ms.                                                                                                                                                               |                                                                                                         |
| Rates (tab)               | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                                                                                                   |                                                                                                         |
| Packet Loss (tab)         | Full-width time-series graph of packet loss % per stream category.                                                                                                                                                               |                                                                                                         |
| Audio (tab)               | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. | v26.5.3 (#2889): per-stream RX diagnostics exposed in the support bundle and in this tab's detail view. |
| Logs (tab)                | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name.                                                                                                         | Timeframe selector is hidden while this tab is active.                                                  |
| Timeframe                 | Selects how far back the time-series charts display history. Default is 5 minutes; options are 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, and 1 week.                                                                       | Shown in the top-right corner of the tab bar; hidden when the Logs tab is active.                       |
| Filter Categories (Logs)  | Per-category checkboxes filter the log view. Includes a General (default) category plus all registered LogManager categories.                                                                                                    |                                                                                                         |
| Select All (Logs)         | Shows all log categories in the viewer.                                                                                                                                                                                          |                                                                                                         |
| Deselect All (Logs)       | Hides all log categories from the viewer.                                                                                                                                                                                        |                                                                                                         |
| Live / Paused (Logs)      | When Live, the viewer auto-scrolls to newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.                                                                                                      |                                                                                                         |
| Close                     | Closes the dialog.                                                                                                                                                                                                               |                                                                                                         |

All counters refresh once per second.

## Frameless mode

The Network Diagnostics dialog supports a frameless window mode that is controlled by the `FramelessWindow` setting in `Settings > Preferences > Advanced > Use frameless windows`. When enabled, the dialog has no title bar and can be dragged by its custom title bar area. The resize behavior (eight-axis cursor on edges and corners) remains active in frameless mode. When disabled, the dialog uses the standard OS window decoration with a regular title bar.

The frameless mode setting is applied immediately when changed in Preferences; you do not need to reopen the dialog.

## Logs tab

The Logs tab tails the AetherSDR log file in real time. The full path to the file being tailed is shown above the log viewer.

Log lines are syntax-highlighted by log level and category:

- Timestamps are shown in muted blue-grey.
- `DBG` lines are muted; `INF` lines are highlighted in light blue; `WRN` lines in amber; `CRT` and `FTL` lines in red.
- Category names are shown in bold.
- Numeric values (decimal, hex) are highlighted in green; protocol tokens (UDP, TCP, RX, TX, VITA-49, and similar) in light purple.

To filter the log output:

1. Click the **Logs** tab.
2. Use the **Filter Categories** checkboxes to select which categories appear. Click **Select All** to show every category or **Deselect All** to clear them.
3. To pause scrolling, scroll up in the viewer. The button switches to **Paused**. Click **Live** to resume auto-scrolling and jump to the newest line.

## Tips

- Zero loss in the Packet Loss section does not rule out the problem. Jitter and bursty late delivery can cause audio breaks without triggering sequence-number gaps. If drops are zero but audio is still broken, check `Underruns (total)`, `Underruns (last sec)`, `Audio Arrival Gap`, `Max Arrival Gap`, and `Jitter Estimate` in the **Audio Playback** section.
- `Max Latency (RTT)` is more useful than the current RTT for catching transient spikes that have already passed.
- Loss that appears on all stream categories simultaneously points to a shared network path problem rather than an audio-specific issue.
- Use the **Timeframe** selector to zoom the time-series charts in or out. Narrower timeframes (1 minute) make recent spikes easier to see; wider timeframes (1 hour or more) help identify recurring patterns.
- Use the **Logs** tab with appropriate category filters to correlate raw log events with the metrics shown in the other tabs.
- The frameless mode setting affects all AetherSDR frameless-capable dialogs. If the Network Diagnostics dialog does not show a title bar, check that `FramelessWindow` is enabled in Preferences.

## Troubleshooting

- **All drop counters show 0 / 0** — No VITA packets have been received in that category. Confirm the radio is connected and transmitting the relevant streams.
- **RTT reads `< 1 ms` but audio is broken** — Network latency is not the cause. See the Audio Playback section for underrun and jitter data.
- **Logs tab shows no output** — Check that at least one category checkbox is selected. Click **Select All** to restore all categories.
- **Dialog has no title bar and cannot be moved** — Frameless mode is enabled. Drag the dialog by clicking on the custom title bar area at the top. To disable frameless mode, go to `Settings > Preferences > Advanced` and uncheck `Use frameless windows`.

## Related

- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Network Diagnostics overview](overview.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- Advanced preferences
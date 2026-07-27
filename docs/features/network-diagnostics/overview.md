# Network Diagnostics overview

The Network Diagnostics dialog gives you a live, per-second view of the network link between AetherSDR and your FLEX-8600. Use it to confirm connection endpoints, measure latency, inspect per-stream data rates, diagnose audio buffer problems, and tail the application log.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected, but most indicators will be empty until a connection is established.

## How it works

Open the dialog with `Settings > Network...`. All indicators update once per second automatically. Click Close when finished.

The dialog uses a tree navigation panel on the left and a content area on the right. Seven pages are available: **Overview**, **Details**, **Latency**, **Rates**, **Packet Loss**, **Audio**, and **Logs**. Click any item in the navigation tree to open that page. A **Search** field at the top of the navigation panel lets you filter the tree items by name. A **Timeframe** selector in the top-right corner controls how far back the time-series charts display history; it is hidden when the Logs page is active.

The dialog remembers its window geometry between sessions. Position and size are saved when you close the dialog and restored the next time it opens.

The Details page organises all labeled indicators into four groups described below.

### Network Status

Connection path and TCP latency. Confirms which route AetherSDR is using to reach the radio.

| Indicator | What it shows |
|---|---|
| Status | Overall link quality, color-coded green → red. Possible states: Excellent, Very Good, Good, Fair, Poor. |
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

| Control                  | Behavior                                                                                                                                                                                                                         | Notes                                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| Navigation tree          | Tree panel on the left side of the dialog. Click any page name to open that page. Items are: Overview, Details, Latency, Rates, Packet Loss, Audio, Logs.                                                                       | Replaces the previous tab bar.                                                                          |
| Search                   | Filters the navigation tree items by name as you type.                                                                                                                                                                           | Located above the navigation tree.                                                                      |
| Overview (page)          | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer).                                                     |                                                                                                         |
| Details (page)           | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.                                                                                                           |                                                                                                         |
| Latency (page)           | Full-width time-series graph of RTT, arrival gap and jitter in ms.                                                                                                                                                               |                                                                                                         |
| Rates (page)             | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                                                                                                   |                                                                                                         |
| Packet Loss (page)       | Full-width time-series graph of packet loss % per stream category.                                                                                                                                                               |                                                                                                         |
| Audio (page)             | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. | v26.5.3 (#2889): per-stream RX diagnostics exposed in the support bundle and in this page's detail view. |
| Logs (page)              | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name.                                                                                                         | Timeframe selector is hidden while this page is active.                                                  |
| Timeframe                | Selects how far back the time-series charts display history. Default is 5 minutes. Available options: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week.                                                                    | Shown in the top-right corner of the page area; hidden when the Logs page is active.                     |
| Filter Categories (Logs) | Per-category checkboxes filter the log view. Includes a General (default) category plus all registered LogManager categories.                                                                                                    |                                                                                                         |
| Select All (Logs)        | Shows all log categories in the viewer.                                                                                                                                                                                          |                                                                                                         |
| Deselect All (Logs)      | Hides all log categories from the viewer.                                                                                                                                                                                        |                                                                                                         |
| Live / Paused (Logs)     | When Live, the viewer auto-scrolls to newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.                                                                                                      | Default state is Live.                                                                                  |
| Close                    | Closes the dialog.                                                                                                                                                                                                               |                                                                                                         |

## Logs page

The Logs page tails the AetherSDR log file in real time. The full path of the file being tailed is shown in the log path label at the top of the page.

Log lines are syntax-highlighted by log level (DBG, INF, WRN, CRT, FTL) and by category name. Use the **Filter Categories** checkboxes to limit output to the categories you are interested in. Click **Select All** to restore all categories or **Deselect All** to clear the view. The **Live / Paused** toggle controls auto-scroll: scrolling up pauses the view automatically; click **Live** to resume and jump back to the newest output.

## Tips

- The dialog can remain open while you operate. All values refresh every second without any interaction required.
- The dialog saves and restores its window position and size between sessions. If you prefer a different layout, resize and reposition the dialog before closing it.
- Packet loss counts in the Packet Loss group are cumulative since the dialog was opened; close and reopen the dialog to reset the baseline.
- Zero packet loss combined with rising underruns points to a jitter or timing problem rather than outright loss — check Audio Arrival Gap and Network Jitter in that case.
- On the Rates page the y-axis uses a logarithmic scale, which makes it easier to see low-rate streams (such as Meters) alongside the much higher RX total.

## Related

- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Watch the first-UDP-packet timestamp after connect](../../getting-started/setup/watch-the-first-udp-packet-timestamp-after-connect.md)
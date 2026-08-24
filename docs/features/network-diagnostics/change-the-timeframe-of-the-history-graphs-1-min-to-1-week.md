# Change the Timeframe of the History Graphs (1 Min to 1 Week)

The **Timeframe** control sets how far back the time-series charts display history in the Network Diagnostics dialog. Use it to zoom out for long-term trend analysis or zoom in to examine a short burst of packet loss or latency.

## Before you start

- Open the Network Diagnostics dialog via `View > Network Diagnostics` or the toolbar button.
- Navigate to any graph tab: **Overview**, **Latency**, **Rates**, **Packet Loss**, or **Audio**. The **Timeframe** control is hidden when the **Logs** tab is active. It is also hidden on the **TCI Clients** page.

## Steps

1. Open the Network Diagnostics dialog via `View > Network Diagnostics` or the toolbar button.
2. Select a graph tab — **Overview**, **Latency**, **Rates**, **Packet Loss**, or **Audio**.
3. Locate the **Timeframe** combo box in the top-right corner of the tab bar.
4. Click **Timeframe** and select the desired value from the drop-down list.

The charts update immediately to show the selected history window.

## What each control does

| Control                                | Kind                                                                                                                                                         | Default                                                                                                                                        |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Overview** (tab)                     | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer). | None                                                                                                                                           |
| **Connection Details** (page)          | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, Audio Playback, and the Adaptive Frame-Rate Throttle subsection. | Renamed from 'Details' in the v26.8.4 tree-navigation rework. Includes a Read-Only Clipboard Copy action to copy the whole diagnostic summary. |
| **Adaptive Frame-Rate Throttle** (section) | Shows the adaptive throttle's Current State, Pending Lift and Sessions This Run values. Reduces panadapter frame rates when latency or loss is detected.     | New in v26.8.4. Hidden until throttle data is available.                                                                                       |
| **Latency** (tab)                      | Full-width time-series graph of RTT, arrival gap and jitter in ms.                                                                                          | None                                                                                                                                           |
| **Rates** (tab)                        | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                              | None                                                                                                                                           |
| **Packet Loss** (tab)                  | Full-width time-series graph of packet loss % per stream category.                                                                                          | None                                                                                                                                           |
| **Audio** (tab)                        | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. | v26.5.3 (#2889): per-stream RX diagnostics exposed in the support bundle and in this tab's detail view.                                        |
| **Logs** (tab)                         | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name.                                     | Timeframe selector is hidden while this page is active.                                                                                        |
| **TCI Clients** (page)                 | Lists connected TCI clients with a live traffic monitor (Pause/Save log/Clear), answer-command suppression controls, and per-client details.                 | New in v26.8.4. Build-gated by HAVE_TCI / TCI support. Timeframe selector is hidden on this page.                                              |
| **Timeframe**                          | Combo box                                                                                                                                                    | 5 minutes                                                                                                                                      |
| **Filter Categories** (Logs)           | Per-category checkboxes filter the log view. Includes a 'General' (default) category plus all registered LogManager categories.                              | None                                                                                                                                           |
| **Select All** (Logs)                  | Push button that shows all log categories in the viewer.                                                                                                    | None                                                                                                                                           |
| **Deselect All** (Logs)                | Push button that hides all log categories from the viewer.                                                                                                  | None                                                                                                                                           |
| **Live / Paused** (Logs)               | Toggle button — when Live, the viewer auto-scrolls to newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.                   | Live                                                                                                                                           |
| **Close**                              | Push button that closes the dialog.                                                                                                                         | None                                                                                                                                           |

Valid values for **Timeframe**: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week.

## Tips

- The **Timeframe** selector applies to all graph tabs simultaneously. Switching tabs after changing the value keeps the same window.
- Selecting **1 week** on a freshly connected session will show empty graph area until enough data has been collected. The charts display "Collecting graph data" until at least one data point is available.
- Use **1 minute** or **5 minutes** to isolate a specific audio dropout or latency spike; use **1 hour** or longer to assess overall link stability over a session.

## Troubleshooting

- **Timeframe selector is not visible** — The **Logs** tab or the **TCI Clients** page is active. Switch to any other tab (**Overview**, **Latency**, **Rates**, **Packet Loss**, or **Audio**) and the selector reappears in the top-right corner of the tab bar.
- **Charts show "Collecting graph data" after changing to a longer timeframe** — Historical data is only available from the moment AetherSDR connected. No data is stored between sessions.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
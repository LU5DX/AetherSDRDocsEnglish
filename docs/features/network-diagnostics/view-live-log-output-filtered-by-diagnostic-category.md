# View live log output filtered by diagnostic category

The Logs tab in Network Diagnostics shows a live tail of the AetherSDR log file, filtered to only the diagnostic categories you choose. Use this when you need to watch specific subsystem messages in real time without wading through unrelated output.

## Before you start

- AetherSDR must be running. A radio connection is not required to view the log.
- Know which diagnostic category you want to watch (for example, `aether.connection`, `aether.cw`, `aether.dxcluster`).

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Click the **Logs** tab.
3. Review the log path shown in the **Log path label** at the top of the tab to confirm which file is being tailed.
4. Check or uncheck the per-category checkboxes under **Filter Categories** to show only the categories you want. By default, the **General** category is available; all registered diagnostic categories appear alongside it.
5. To show every category at once, click **Select All**. To hide all categories, click **Deselect All**, then check only the specific categories you need.
6. Watch the viewer. New entries scroll in automatically while the toggle reads **Live**.
7. When finished, click **Close**.

## What each control does

| Control                                | Behavior                                                                                                                                                                                                                         | Default                                                                                                                                        |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Overview** (tab)                     | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer).                                                     | —                                                                                                                                              |
| **Connection Details** (page)          | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, Audio Playback, and the Adaptive Frame-Rate Throttle subsection. Includes a Read-Only Clipboard Copy action to copy the whole diagnostic summary. | Renamed from 'Details' in the v26.8.4 tree-navigation rework.                                                                                  |
| **Latency** (tab)                      | Full-width time-series graph of RTT, arrival gap and jitter in ms.                                                                                                                                                               | —                                                                                                                                              |
| **Rates** (tab)                        | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                                                                                                   | —                                                                                                                                              |
| **Packet Loss** (tab)                  | Full-width time-series graph of packet loss % per stream category.                                                                                                                                                               | —                                                                                                                                              |
| **Audio** (tab)                        | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. | —                                                                                                                                              |
| **Logs** (tab)                         | Live tail of the AetherSDR log file filtered by category checkboxes. Syntax-highlighted by log level and category name. The **Timeframe** selector is hidden while this tab is active.                                           | —                                                                                                                                              |
| **TCI Clients** (page)                 | Lists connected TCI clients with a live traffic monitor (Pause/Save log/Clear), answer-command suppression controls, and per-client details. Build-gated by HAVE_TCI / TCI support. Timeframe selector is hidden on this page.  | —                                                                                                                                              |
| **Timeframe**                          | Selects how far back the time-series charts display history. Hidden when the Logs tab is active.                                                                                                                                 | 5 minutes                                                                                                                                      |
| **Filter Categories**                  | Per-category checkboxes. Check a category to include its lines; uncheck to hide them. Includes **General** plus all registered LogManager categories.                                                                            | —                                                                                                                                              |
| **Select All**                         | Shows all log categories in the viewer immediately.                                                                                                                                                                              | —                                                                                                                                              |
| **Deselect All**                       | Hides all log categories from the viewer immediately.                                                                                                                                                                            | —                                                                                                                                              |
| **Live / Paused**                      | When **Live**, the viewer auto-scrolls to the newest output. Scrolling up switches the state to **Paused**. Clicking the toggle when it reads **Paused** resumes auto-scroll and jumps to the tail.                              | Live                                                                                                                                           |
| **Log path label**                     | Displays the full filesystem path of the log file being tailed.                                                                                                                                                                  | —                                                                                                                                              |
| **Close**                              | Closes the dialog.                                                                                                                                                                                                               | —                                                                                                                                              |
| Adaptive Frame-Rate Throttle (section) | Shows the adaptive throttle's Current State, Pending Lift and Sessions This Run values. Reduces panadapter frame rates when latency or loss is detected. Hidden until throttle data is available.                                  | New in v26.8.4.                                                                                                                                 |
| Connection Details (page)              | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, Audio Playback, and the Adaptive Frame-Rate Throttle subsection. Includes a Read-Only Clipboard Copy action to copy the whole diagnostic summary. | Renamed from 'Details' in the v26.8.4 tree-navigation rework.                                                                                  |
| TCI Clients (page)                     | Lists connected TCI clients with a live traffic monitor (Pause/Save log/Clear), answer-command suppression controls, and per-client details. Build-gated by HAVE_TCI / TCI support. Timeframe selector is hidden on this page.  | New in v26.8.4.                                                                                                                                 |

## Network Diagnostics indicators

| Indicator | Description |
|---|---|
| **Status** | Overall link quality: Excellent, Very Good, Good, Fair, or Poor (color-coded green → red). |
| **Target Radio IP** | IP of connected radio, or 'Not connected'. |
| **Selected Source** | Local NIC/bind path used for the connection. |
| **Local TCP** | Local TCP endpoint. |
| **Local UDP** | Local UDP endpoint. |
| **First UDP Packet** | Whether the first UDP packet has been received since connect (Yes/No). |
| **Latency (RTT)** | Current round-trip time. Displays "not measured on this link" when the transport has no round trip to time. |
| **Max Latency (RTT)** | Highest RTT seen since connect. Displays "not measured on this link" when the transport has no round trip to time. |
| **Audio / FFT / Waterfall / Meters / DAX rates** | Per-category ingress rate in kbps. Displays "n/a" when the transport provides no per-stream category breakdown. |
| **Total RX / Total TX** | Aggregate bytes per second in each direction. |
| **Audio / FFT / Waterfall / Meters / DAX drops** | Per-category dropped-packet counts and percentage. Displays "n/a" when the transport provides no per-stream category breakdown. |
| **RX Buffer Now / Peak** | Current and peak audio buffer fill in bytes and ms. |
| **Underruns (total / last sec)** | Audio underrun counters. |
| **Audio Arrival Gap / Max Arrival Gap** | Inter-packet arrival timing. Displays "not measured on this link" when delivery-timing data is unavailable. |
| **Network Jitter** | Smoothed jitter estimate of audio stream in ms. Displays "not measured on this link" when delivery-timing data is unavailable. |

## Tips

- The Network Diagnostics dialog respects the **FramelessWindow** setting from AetherSDR preferences (`AppSettings > FramelessWindow`). When enabled, the dialog uses a persistent geometry that is saved and restored across sessions. When disabled, the dialog uses the standard window frame.
- The log view refreshes every 500 ms, so there is a short delay between a message being written and it appearing in the viewer.
- Syntax highlighting colors help distinguish log levels at a glance: `INF` lines appear in blue, `WRN` in amber, and `CRT`/`FTL` in red. Category names are shown in bold. Numbers and protocol tokens (such as `UDP`, `TCP`, `RX`, `TX`) are highlighted separately.
- If you want to freeze the display to read a specific entry, scroll up. The viewer switches to **Paused** automatically. Click **Live** to return to the tail.
- Clicking **Deselect All** and then checking a single category is the fastest way to isolate one subsystem's output.
- In v26.7.4, the dialog uses a navigation tree on the left and a content panel on the right. Click a page name in the **Network Diagnostics Navigation** tree to switch between pages. A search field at the top of the navigation tree allows you to filter available pages by name.
- In v26.8.4, the dialog was reworked to a category tree with searchable pages: Overview dashboard, Connection Details pane (including the Adaptive Frame-Rate Throttle section), Latency & Jitter, Stream Rates, Packet Loss, Audio trend graphs, Application Logs, per-stream RX audio diagnostics, and the TCI Clients page (build-gated).
- When a metric cannot be measured on the current link (for example, RTT on a transport with no round trip to time), the dialog displays "not measured on this link" instead of a value that could be mistaken for a real reading. Per-stream breakdowns display "n/a" when the transport carries everything in a single stream.

## Related

- [Pause log scrolling to inspect an older entry](pause-log-scrolling-to-inspect-an-older-entry.md)
- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
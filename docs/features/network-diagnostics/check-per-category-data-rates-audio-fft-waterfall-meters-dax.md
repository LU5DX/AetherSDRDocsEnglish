# Network Diagnostics dialog

The Network Diagnostics dialog provides a comprehensive live view of the network link to the radio. It features a multi-tab layout with an Overview dashboard with health cards and time-series charts, a Details pane with labeled metrics, per-stream Latency / Rates / Packet Loss / Audio graph tabs, and a live Logs tab for tailing the log file filtered by diagnostic category.

## Opening the dialog

1. Click **Settings** > **Network...**

The dialog opens whether or not a radio is connected, but metrics are meaningful only when connected.

## Tabs

| Tab | Description |
|-----|-------------|
| **Overview** | Four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer). |
| **Details** | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups. |
| **Latency** | Full-width time-series graph of RTT, arrival gap and jitter in ms. |
| **Rates** | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps. |
| **Packet Loss** | Full-width time-series graph of packet loss % per stream category. |
| **Audio** | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. |
| **Logs** | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name. The **Timeframe** selector is hidden while this tab is active. |

## Controls

| Control                      | Location                        | Description                                                                                                                                                                                     |
|------------------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Timeframe**                | Top-right corner of the tab bar | Selects how far back the time-series charts display history. Default is **5 minutes**. Options: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week. Hidden when the **Logs** tab is active. |
| **Filter Categories (Logs)** | Logs tab                        | Per-category checkboxes filter the log view. Includes a General (default) category plus all registered LogManager categories.                                                                   |
| **Select All (Logs)**        | Logs tab                        | Shows all log categories in the viewer.                                                                                                                                                         |
| **Deselect All (Logs)**      | Logs tab                        | Hides all log categories from the viewer.                                                                                                                                                       |
| **Live / Paused (Logs)**     | Logs tab                        | When set to **Live**, the viewer auto-scrolls to the newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.                                                      |
| **Close**                    | Bottom of dialog                | Closes the dialog.                                                                                                                                                                              |
## Indicators

| Indicator | Meaning |
|-----------|---------|
| **Status** | Overall link quality, color-coded green → red. States: Excellent, Very Good, Good, Fair, Poor. |
| **Target Radio IP** | IP of connected radio, or "Not connected". |
| **Selected Source** | Local NIC/bind path used for the connection. |
| **Local TCP** | Local TCP endpoint. |
| **Local UDP** | Local UDP endpoint. |
| **First UDP Packet** | Whether the first UDP packet has been received since connect. |
| **Latency (RTT)** | Current round-trip time. |
| **Max Latency (RTT)** | Highest RTT seen since connect. |
| **Audio / FFT / Waterfall / Meters / DAX rates** | Per-category ingress rate in kbps. |
| **Total RX / Total TX** | Aggregate bytes per second in each direction. |
| **Audio / FFT / Waterfall / Meters / DAX drops** | Per-category dropped-packet counts and percentage. |
| **RX Buffer Now / Peak** | Current and peak audio buffer fill in bytes and ms. |
| **Underruns (total / last sec)** | Audio underrun counters. |
| **Audio Arrival Gap / Max Arrival Gap** | Inter-packet arrival timing. |
| **Network Jitter** | Smoothed jitter estimate of audio stream in ms. |
| **Log path label** | Shows the full path of the log file being tailed. |

## Logs tab

The **Logs** tab tails the AetherSDR log file in real time. The full path of the file being tailed is shown in the log path label at the top of the tab.

Log output is syntax-highlighted by log level and category name:

- Timestamps are rendered in muted blue-grey.
- `DBG` entries are rendered in muted blue-grey.
- `INF` entries are rendered in light blue.
- `WRN` entries are rendered in amber.
- `CRT` and `FTL` entries are rendered in red.
- Category names are rendered in bold light grey.
- Numeric values and protocol tokens (for example, UDP, TCP, VITA-49, RX, TX) are rendered in distinct accent colors.

Use the **Filter Categories** checkboxes to show only the categories relevant to the problem you are diagnosing. Click **Select All** to restore all categories, or **Deselect All** to clear the view before selecting specific categories. Scroll up to pause auto-scrolling; click **Live** to resume and jump back to the tail.

## Tips

- A rate of 0 kbps for a category that should be active (for example, **Audio** while a slice is open) indicates the stream has stopped arriving. Check the **Status** indicator in the **Network Status** group on the **Details** tab first.
- Large swings in a category rate from second to second can indicate bursty delivery even when the drop count remains at zero.
- Zero drops in the **Packet Loss** group does not rule out jitter or late-arriving bursts. If audio is choppy but drops show zero, check the **Audio Playback** group on the **Details** tab for underruns and jitter, or review the **Audio** tab for a time-series view of buffer fill and underruns/s.
- The **Rates** tab uses a logarithmic y-axis, which makes it easier to see low-rate streams (for example, Meters) alongside high-rate streams (for example, RX total) on the same chart.
- Extend the **Timeframe** selector to **1 hour** or longer when investigating intermittent issues that occur infrequently.

## Troubleshooting

- **All category rates show 0 kbps** — The radio is not streaming. Confirm the connection is active by checking **Status** and **Target Radio IP** in the **Network Status** group on the **Details** tab. Reconnect via **Settings** > **Connect to Radio...** if needed.
- **DAX rate shows 0 kbps while DAX is expected** — DAX streaming may not be enabled. Verify DAX is started; on supported platforms, check **Settings** > **Autostart DAX with AetherSDR**.
- **Drop percentage is non-zero on one category only** — Loss is isolated to that stream. This can indicate the radio is overloaded for that specific data type or that a network queue is preferentially dropping UDP packets of that size.
- **Logs tab shows no output** — Confirm the log path label displays a valid file path. If the path is missing or the file does not exist, restart AetherSDR and re-open the dialog.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
# Check per-category data rates (audio, FFT, waterfall, meters, DAX)

The Network Diagnostics dialog shows live ingress rates for each stream category — Audio, FFT, Waterfall, Meters, and DAX — updated every second. Use this to confirm that each stream is delivering data at the expected rate and to identify which category is consuming bandwidth or dropping packets.

## Before you start

- AetherSDR must be running. The dialog opens whether or not a radio is connected, but rate values are meaningful only when connected.

## Steps

1. Click `Settings > Network...`.
2. Click the **Details** tab.
3. Locate the **Incoming Stream Rates** group on the right side of the tab.
4. Read the per-category rate indicators: **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX**. Each shows the current ingress rate in kbps, recalculated once per second.
5. Locate the **Packet Loss** group below the left column.
6. Read the corresponding **Audio**, **FFT**, **Waterfall**, **Meters**, and **DAX** drop indicators. Each shows dropped packets, total packets, and a loss percentage in the form `errors / total (pct%)`.
7. To see a time-series view of per-stream bitrates, click the **Rates** tab. Use the **Timeframe** selector in the top-right corner of the tab bar to choose how far back the chart displays history.
8. To see a time-series view of packet loss per stream category, click the **Packet Loss** tab.
9. When finished, click **Close**.

## What each control does

| Control / Indicator      | Location / Group                  | Meaning                                                                                                                                                      |
|--------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Overview** (tab)       | Tab bar                           | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer). |
| **Details** (tab)        | Tab bar                           | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.                                        |
| **Latency** (tab)        | Tab bar                           | Full-width time-series graph of RTT, arrival gap, and jitter in ms.                                                                                          |
| **Rates** (tab)          | Tab bar                           | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                                |
| **Packet Loss** (tab)    | Tab bar                           | Full-width time-series graph of packet loss % per stream category.                                                                                           |
| **Audio** (tab)          | Tab bar                           | Full-width time-series graph of playback buffer fill (ms) and underruns/s.                                                                                   |
| **Logs** (tab)           | Tab bar                           | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name. The **Timeframe** selector is hidden while this tab is active. |
| **Timeframe**            | Top-right corner of the tab bar   | Selects how far back the time-series charts display history. Default is **5 minutes**. Options: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week. Hidden when the **Logs** tab is active. |
| **Audio** (rate)         | Details > Incoming Stream Rates   | Ingress rate for the receiver audio stream, in kbps.                                                                                                         |
| **FFT** (rate)           | Details > Incoming Stream Rates   | Ingress rate for panadapter FFT data, in kbps.                                                                                                               |
| **Waterfall** (rate)     | Details > Incoming Stream Rates   | Ingress rate for waterfall data, in kbps.                                                                                                                    |
| **Meters** (rate)        | Details > Incoming Stream Rates   | Ingress rate for meter data, in kbps.                                                                                                                        |
| **DAX** (rate)           | Details > Incoming Stream Rates   | Ingress rate for DAX audio data, in kbps.                                                                                                                    |
| **Total RX**             | Details > Incoming Stream Rates   | Aggregate receive rate across all stream categories, in kbps.                                                                                                |
| **Total TX**             | Details > Incoming Stream Rates   | Aggregate transmit rate, in kbps.                                                                                                                            |
| **Audio** (drops)        | Details > Packet Loss             | Dropped vs. total audio packets, with loss percentage.                                                                                                       |
| **FFT** (drops)          | Details > Packet Loss             | Dropped vs. total FFT packets, with loss percentage.                                                                                                         |
| **Waterfall** (drops)    | Details > Packet Loss             | Dropped vs. total waterfall packets, with loss percentage.                                                                                                   |
| **Meters** (drops)       | Details > Packet Loss             | Dropped vs. total meter packets, with loss percentage.                                                                                                       |
| **DAX** (drops)          | Details > Packet Loss             | Dropped vs. total DAX packets, with loss percentage.                                                                                                         |
| **Filter Categories**    | Logs tab                          | Per-category checkboxes filter the log view. Includes a General (default) category plus all registered LogManager categories.                                 |
| **Select All**           | Logs tab                          | Shows all log categories in the viewer.                                                                                                                      |
| **Deselect All**         | Logs tab                          | Hides all log categories from the viewer.                                                                                                                    |
| **Live / Paused**        | Logs tab                          | When set to Live, the viewer auto-scrolls to the newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.                        |
| **Close**                | Bottom of dialog                  | Closes the dialog.                                                                                                                                           |

All rate values are computed from the byte-count delta over the preceding one-second interval and expressed as kbps. Drop counts are inferred from missing VITA-49 sequence numbers.

## Logs tab

The **Logs** tab tails the AetherSDR log file in real time. The full path of the file being tailed is shown in the log path label at the top of the tab.

Log output is syntax-highlighted by log level and category name:

- Timestamps are rendered in muted blue-grey.
- `DBG` entries are rendered in muted blue-grey.
- `INF` entries are rendered in light blue.
- `WRN` entries are rendered in amber.
- `CRT` and `FTL` entries are rendered in red.
- Category names are rendered in bold light grey.
- Numeric values and protocol tokens (for example, `UDP`, `TCP`, `VITA-49`, `RX`, `TX`) are rendered in distinct accent colors.

Use the **Filter Categories** checkboxes to show only the categories relevant to the problem you are diagnosing. Click **Select All** to restore all categories, or **Deselect All** to clear the view before selecting specific categories. Scroll up to pause auto-scrolling; click **Live** to resume and jump back to the tail.

## Tips

- A rate of 0 kbps for a category that should be active (for example, **Audio** while a slice is open) indicates the stream has stopped arriving. Check the **Status** indicator in the **Network Status** group on the **Details** tab first.
- Large swings in a category rate from second to second can indicate bursty delivery even when the drop count remains at zero.
- Zero drops in the **Packet Loss** group does not rule out jitter or late-arriving bursts. If audio is choppy but drops show zero, check the **Audio Playback** group on the **Details** tab for underruns and jitter, or review the **Audio** tab for a time-series view of buffer fill and underruns/s.
- The **Rates** tab uses a logarithmic y-axis, which makes it easier to see low-rate streams (for example, Meters) alongside high-rate streams (for example, RX total) on the same chart.
- Extend the **Timeframe** selector to **1 hour** or longer when investigating intermittent issues that occur infrequently.

## Troubleshooting

- **All category rates show 0 kbps** — The radio is not streaming. Confirm the connection is active by checking **Status** and **Target Radio IP** in the **Network Status** group on the **Details** tab. Reconnect via `Settings > Connect to Radio...` if needed.
- **DAX rate shows 0 kbps while DAX is expected** — DAX streaming may not be enabled. Verify DAX is started; on supported platforms, check `Settings > Autostart DAX with AetherSDR`.
- **Drop percentage is non-zero on one category only** — Loss is isolated to that stream. This can indicate the radio is overloaded for that specific data type or that a network queue is preferentially dropping UDP packets of that size.
- **Logs tab shows no output** — Confirm the log path label displays a valid file path. If the path is missing or the file does not exist, restart AetherSDR and re-open the dialog.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Verify the radio's IP and local bind address](verify-the-radio-s-ip-and-local-bind-address.md)
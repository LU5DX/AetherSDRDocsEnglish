# Change the Timeframe of the History Graphs (1 Min to 1 Week)

The **Timeframe** control sets how far back the time-series charts display history in the Network Diagnostics dialog. Use it to zoom out for long-term trend analysis or zoom in to examine a short burst of packet loss or latency.

## Before you start

- Open the Network Diagnostics dialog via `View > Network Diagnostics` or the toolbar button.
- Navigate to any graph tab: **Overview**, **Latency**, **Rates**, **Packet Loss**, or **Audio**. The **Timeframe** control is hidden when the **Logs** tab is active.

## Steps

1. Open the Network Diagnostics dialog via `View > Network Diagnostics` or the toolbar button.
2. Select a graph tab — **Overview**, **Latency**, **Rates**, **Packet Loss**, or **Audio**.
3. Locate the **Timeframe** combo box in the top-right corner of the tab bar.
4. Click **Timeframe** and select the desired value from the drop-down list.

The charts update immediately to show the selected history window.

## What each control does

| Control       | Kind      | Default   |
|---------------|-----------|-----------|
| **Timeframe** | Combo box | 5 minutes |

Valid values: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week.
## Tips

- The **Timeframe** selector applies to all graph tabs simultaneously. Switching tabs after changing the value keeps the same window.
- Selecting **1 week** on a freshly connected session will show empty graph area until enough data has been collected. The charts display "Collecting graph data" until at least one data point is available.
- Use **1 minute** or **5 minutes** to isolate a specific audio dropout or latency spike; use **1 hour** or longer to assess overall link stability over a session.

## Troubleshooting

- **Timeframe selector is not visible** — The **Logs** tab is active. Switch to any other tab (**Overview**, **Latency**, **Rates**, **Packet Loss**, or **Audio**) and the selector reappears in the top-right corner of the tab bar.
- **Charts show "Collecting graph data" after changing to a longer timeframe** — Historical data is only available from the moment AetherSDR connected. No data is stored between sessions.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
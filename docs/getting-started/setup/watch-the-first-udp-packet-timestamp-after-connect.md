# Network Diagnostics

Use the **Network Diagnostics** dialog to monitor the live network link between AetherSDR and the FLEX-8600 radio. The dialog provides a multi-pane layout with a navigation tree on the left, content area on the right, an Overview dashboard, detailed metric panels, per-stream performance graphs, and a live log viewer.

## Before you start

- AetherSDR must be running. The dialog can be opened whether or not a radio is connected, but indicators are only meaningful after a connection attempt.
- You must have already initiated a connection to a FLEX-8600 radio.

## Steps

1. Click `Settings > Network...`.
2. In the **Network Diagnostics** dialog, use the navigation tree on the left side to select the view you want to examine.
3. Click **Close** to dismiss the dialog.

## What each control does

| Indicator / Control                              | Meaning or Behavior                                                                                                                                                                                                              | Notes                                                                                                   |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **First UDP Packet**                             | Shows `Yes` or `No`. Updates once per second. Reflects whether any UDP packet from the radio has been received in the current session.                                                                                           |                                                                                                         |
| **Status**                                       | Overall link quality, color-coded green to red. States: Excellent, Very Good, Good, Fair, Poor.                                                                                                                                  |                                                                                                         |
| **Target Radio IP**                              | IP address of the connected radio, or "Not connected".                                                                                                                                                                           |                                                                                                         |
| **Selected Source**                              | Local NIC or bind path used for the connection.                                                                                                                                                                                  |                                                                                                         |
| **Local TCP**                                    | The local TCP endpoint in use for the current connection.                                                                                                                                                                        |                                                                                                         |
| **Local UDP**                                    | The local UDP endpoint AetherSDR is listening on. Useful for confirming the correct port is bound.                                                                                                                               |                                                                                                         |
| **Latency (RTT)**                                | Current round-trip time.                                                                                                                                                                                                         |                                                                                                         |
| **Max Latency (RTT)**                            | Highest RTT seen since connect.                                                                                                                                                                                                  |                                                                                                         |
| **Network Jitter**                               | Smoothed jitter estimate of the audio stream in ms.                                                                                                                                                                              |                                                                                                         |
| **Audio / FFT / Waterfall / Meters / DAX rates** | Per-category ingress rate in kbps.                                                                                                                                                                                               |                                                                                                         |
| **Total RX / Total TX**                          | Aggregate bytes per second in each direction.                                                                                                                                                                                    |                                                                                                         |
| **Audio / FFT / Waterfall / Meters / DAX drops** | Per-category dropped-packet counts and percentage.                                                                                                                                                                               |                                                                                                         |
| **RX Buffer Now / Peak**                         | Current and peak audio buffer fill in bytes and ms.                                                                                                                                                                              |                                                                                                         |
| **Underruns (total / last sec)**                 | Audio underrun counters.                                                                                                                                                                                                         |                                                                                                         |
| **Audio Arrival Gap / Max Arrival Gap**          | Inter-packet arrival timing.                                                                                                                                                                                                     |                                                                                                         |
| **Log path label**                               | Shows the full path of the log file being tailed in the Logs view.                                                                                                                                                                |                                                                                                         |
| Navigation tree (left pane)                      | Tree-style navigation replacing tab bar. Select an item to display its content in the main area.                                                                                                                                 |                                                                                                         |
| Search filter (above navigation tree)            | Text input field for filtering items in the navigation tree. Typing narrows the visible items.                                                                                                                                    |                                                                                                         |
| Page title (content area)                        | Large bold title at the top of the content area indicating the currently selected view.                                                                                                                                          |                                                                                                         |
| Overview (page)                                  | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer).                                                     |                                                                                                         |
| Details (page)                                   | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.                                                                                                           |                                                                                                         |
| Latency (page)                                   | Full-width time-series graph of RTT, arrival gap, and jitter in ms.                                                                                                                                                              |                                                                                                         |
| Rates (page)                                     | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                                                                                                   |                                                                                                         |
| Packet Loss (page)                               | Full-width time-series graph of packet loss % per stream category.                                                                                                                                                               |                                                                                                         |
| Audio (page)                                     | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. | v26.5.3 (#2889): per-stream RX diagnostics exposed in the support bundle and in this view's detail view. |
| Logs (page)                                      | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name.                                                                                                         | The Timeframe selector is hidden while this view is active.                                              |
| Timeframe                                        | Selects how far back the time-series charts display history. Default is 5 minutes. Options: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week.                                                                              | Shown in the top-right corner of the content area when viewing Overview, Details, Latency, Rates, Packet Loss, or Audio. Hidden when viewing Logs.                       |
| Filter Categories (Logs)                         | Per-category checkboxes filter the log view. Includes a General (default) category plus all registered LogManager categories.                                                                                                    |                                                                                                         |
| Select All (Logs)                                | Shows all log categories in the viewer.                                                                                                                                                                                          |                                                                                                         |
| Deselect All (Logs)                              | Hides all log categories from the viewer.                                                                                                                                                                                        |                                                                                                         |
| Live / Paused (Logs)                             | When Live, the viewer auto-scrolls to newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.                                                                                                      |                                                                                                         |
| Close                                            | Closes the dialog.                                                                                                                                                                                                               |                                                                                                         |

## Using the Logs view

The **Logs** view provides a live tail of the AetherSDR log file directly inside the dialog.

1. In the navigation tree, select **Logs**.
2. The full path of the log file being tailed is shown at the top of the view in the **Log path label**.
3. Use the **Filter Categories** checkboxes to show only the categories you are interested in. The **General** category is available by default; additional categories reflect all registered LogManager categories.
4. Click **Select All** to enable every category at once, or **Deselect All** to clear all selections.
5. The viewer starts in **Live** mode and auto-scrolls to the newest output. Scroll up at any time to pause auto-scrolling; the toggle switches to **Paused**.
6. Click **Live** to resume auto-scrolling and jump back to the tail.

Log entries are syntax-highlighted by log level (DBG, INF, WRN, CRT/FTL) and by category name, timestamps, numeric values, and protocol keywords.

> **Note:** The **Timeframe** selector is hidden while the Logs view is active. Switch to any other view to restore it.

## Tips

- The dialog refreshes all indicators once per second. If **First UDP Packet** stays `No` for several seconds after connecting, UDP traffic is not reaching the host — check firewall rules, routing, and that the local UDP endpoint shown in **Local UDP** is reachable from the radio.
- On a VPN or routed link, TCP may connect successfully while UDP is blocked separately. **First UDP Packet** showing `No` with **Status** showing a connected state is a reliable sign of this split.
- **First UDP Packet** resets on each new connection. Disconnect and reconnect if you want to re-verify delivery after changing network settings.
- Use the **Timeframe** selector to narrow or widen the history shown across all time-series views. The default is 5 minutes.
- The **Rates** view uses a logarithmic scale so that low-bitrate streams (such as Meters) remain visible alongside the higher-bitrate RX total.
- Use the **Search filter** above the navigation tree to quickly find specific view pages when many items are present.
- The dialog uses a custom dark-themed appearance with styled panels, navigation tree, and controls for consistent visual feedback across all platforms.
- The dialog geometry (position and size) is remembered between sessions via the `NetworkDiagnosticsDialogGeometry` setting.

## Troubleshooting

- **First UDP Packet stays "No" after connecting** — UDP is not arriving at the local endpoint. Verify that no firewall is blocking UDP on the port shown in **Local UDP**, and that the radio can route back to your machine's IP. On a VPN connection, confirm the VPN passes UDP in both directions.
- **First UDP Packet shows "Yes" but audio is silent** — UDP is arriving, but a different problem affects playback. Check the **Audio Playback** group in the Details view for underruns or buffer issues, and see the audio diagnostics page.
- **Log viewer is empty or shows no entries** — Confirm that at least one **Filter Categories** checkbox is selected. If all categories are deselected, no entries are displayed. Click **Select All** to restore visibility.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Verify the radio's IP and local bind address](../../features/network-diagnostics/verify-the-radio-s-ip-and-local-bind-address.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Diagnose audio underruns and jitter](../../troubleshooting/networkdiagnostics/diagnose-audio-underruns-and-jitter.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Pick the local network interface used for a manual connection](pick-the-local-network-interface-used-for-a-manual-connection.md)
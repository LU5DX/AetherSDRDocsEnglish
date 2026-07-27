# Network Diagnostics Dialog

Use this page to monitor the live network link between AetherSDR and your FLEX-8600, confirm connection addresses, inspect per-stream data rates, and review filtered log output.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but most fields and graphs will show meaningful values only after a connection attempt has been made.

## Opening the dialog

1. Click `Settings > Network...`.
2. The **Network Diagnostics** dialog opens. It defaults to a navigation tree on the left with a content panel on the right. The default view is **Overview**.

## Layout overview

The dialog uses a two-panel layout with a navigation tree on the left and a content panel on the right. Click any item in the navigation tree to display the corresponding page.

The navigation tree contains the following sections and pages:

- **Radio Connection**
  - Overview
  - Details
- **Network Graphs**
  - Latency
  - Rates
  - Packet Loss
  - Audio
- **Logging**
  - Logs

## Search for a page

1. Locate the search field at the top of the navigation tree, labeled with a magnifying glass icon.
2. Type any part of a page name (for example, "delay" or "rates"). The navigation tree filters to show only matching items.
3. Click a filtered item to open that page.
4. Clear the search field to restore the full navigation tree.

## Page overview

| Page              | What it shows                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Overview**      | Four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer). |
| **Details**       | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.         |
| **Latency**       | Full-width time-series graph of RTT, arrival gap, and jitter in ms.                                                            |
| **Rates**         | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps. |
| **Packet Loss**   | Full-width time-series graph of packet loss % per stream category.                                                             |
| **Audio**         | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. |
| **Logs**          | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name.       |

## Verify the radio's IP and local bind address

1. Open the **Network Diagnostics** dialog as described above.
2. In the navigation tree, click **Details**.
3. Locate the **Network Status** group.
4. Read **Target Radio IP** — this shows the IP address of the radio AetherSDR connected to. If no connection has been made, the field displays `Not connected`.
5. Read **Selected Source** — this shows the local network interface or bind path AetherSDR used to reach the radio.
6. Read **Local TCP** and **Local UDP** to see the exact local endpoints for each protocol.
7. Click **Close** when done.

## Control the chart timeframe

The **Timeframe** combo box in the top-right corner sets how far back all time-series charts display history. It is hidden while the **Logs** page is active.

| Value                 | Behavior | Notes |
|-----------------------|----------|-------|
| 1 minute              |          |       |
| 5 minutes *(default)* |          |       |
| 15 minutes            |          |       |
| 1 hour                |          |       |
| 1 day                 |          |       |
| 1 week                |          |       |

Select a value from the **Timeframe** drop-down. All visible charts update immediately.

## Use the Logs page

1. In the navigation tree, click **Logs**.
2. The **Log path label** at the top of the page shows the full path of the log file being tailed.
3. Use the **Filter Categories (Logs)** checkboxes to show or hide individual log categories. The list includes a **General** category (shown by default) plus every category registered with LogManager.
4. Click **Select All (Logs)** to enable all categories at once.
5. Click **Deselect All (Logs)** to hide all categories at once.
6. The **Live / Paused** toggle button controls auto-scrolling:
   - **Live** — the viewer auto-scrolls to the newest output as log lines arrive.
   - **Paused** — scrolling is stopped so you can read earlier lines. Scroll up at any time to auto-pause.
   - Click **Live** to resume and jump back to the tail.
7. Log lines are syntax-highlighted by log level (DBG, INF, WRN, CRT, FTL) and by category name.

> **Note:** The **Timeframe** selector is hidden while the **Logs** page is active. Navigate to any other page to restore it.

## Inspect per-stream RX audio diagnostics

1. In the navigation tree, click **Audio**.
2. The main graph shows playback buffer fill (ms) and underruns/s over time.
3. Below the graph, a detail area displays per-stream RX audio diagnostics for each active audio stream:
   - **Feed rate** — The rate at which audio data is being fed to the playback buffer.
   - **Deficit** — The current buffer deficit in ms.
   - **Late packets** — Count of packets arriving after their scheduled playback time.
   - **Packet class code** — Classification of the packet quality.
   - **Stream health** — Overall health indicator for the audio stream.
4. Use this information to identify which audio stream is experiencing issues and what type of problem is occurring.

## What each indicator means

| Indicator                               | Meaning                                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------------------|
| **Status**                              | Overall link quality, color-coded from green (Excellent) to red (Poor). States: Excellent, Very Good, Good, Fair, Poor. |
| **Target Radio IP**                     | IP address of the connected radio. Displays `Not connected` if no connection is active. |
| **Selected Source**                     | Local NIC or bind path used to reach the radio.                                         |
| **Local TCP**                           | Local TCP endpoint (address and port).                                                  |
| **Local UDP**                           | Local UDP endpoint (address and port).                                                  |
| **First UDP Packet**                    | Whether the first UDP packet has been received since connect (Yes / No).                |
| **Latency (RTT)**                       | Current round-trip time.                                                                |
| **Max Latency (RTT)**                   | Highest RTT seen since connect.                                                         |
| **Audio / FFT / Waterfall / Meters / DAX rates** | Per-category ingress rate in kbps.                                            |
| **Total RX / Total TX**                 | Aggregate bytes per second in each direction.                                           |
| **Audio / FFT / Waterfall / Meters / DAX drops** | Per-category dropped-packet counts and percentage.                            |
| **RX Buffer Now / Peak**                | Current and peak audio buffer fill in bytes and ms.                                     |
| **Underruns (total / last sec)**        | Audio underrun counters.                                                                |
| **Audio Arrival Gap / Max Arrival Gap** | Inter-packet arrival timing.                                                            |
| **Network Jitter**                      | Smoothed jitter estimate of the audio stream in ms.                                     |
| **Log path label**                      | Full path of the log file being tailed (visible on the Logs page).                       |

## Controls reference

| Control                  | Type           | Default | Behavior                                                                                                                           |
|--------------------------|----------------|---------|------------------------------------------------------------------------------------------------------------------------------------|
| **Timeframe**            | Combo box      | 5 minutes | Selects how far back the time-series charts display history. Hidden when the Logs page is active.                                  |
| **Filter Categories (Logs)** | Checkboxes | —       | Per-category checkboxes filter the log view. Includes a General category plus all registered LogManager categories.               |
| **Select All (Logs)**    | Button         | —       | Shows all log categories in the viewer.                                                                                            |
| **Deselect All (Logs)**  | Button         | —       | Hides all log categories from the viewer.                                                                                          |
| **Live / Paused (Logs)** | Toggle button  | Live    | When Live, the viewer auto-scrolls to newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.        |
| **Close**                | Button         | —       | Closes the dialog.                                                                                                                 |

## Tips

- The dialog refreshes all values once per second. If you have just connected, wait a moment for the fields to populate.
- **Selected Source** is useful when the host has multiple network interfaces. Confirm it shows the interface on the same subnet as the radio, not a VPN or secondary adapter.
- The **Rates** page uses a logarithmic y-axis, which makes it easier to compare high-bandwidth streams (such as total RX at several Mbps) alongside low-bandwidth streams (such as Meters at a few kbps) on the same chart.
- On the **Logs** page, scrolling up automatically switches the toggle to **Paused**. Click **Live** to jump back to the current tail.
- The **Audio** page's per-stream diagnostics help you identify whether audio problems are caused by network issues (late packets, high deficit) or local playback issues (underruns, buffer mismanagement).
- Use the search field at the top of the navigation tree to quickly find any page by name.

## Troubleshooting

- **Target Radio IP shows `Not connected`** — No connection to the radio is active. Use `Settings > Connect to Radio...` to discover and connect to your FLEX-8600, then reopen the dialog.
- **Selected Source shows an unexpected interface** — Your operating system routed the connection through a different NIC than intended. Check your routing table or disable unused network interfaces, then reconnect.
- **Status card shows Poor or Fair** — Check the **Latency** and **Packet Loss** pages for the affected time range. High jitter or sustained packet loss on the Audio stream usually points to network congestion or Wi-Fi interference.
- **Logs page shows no output** — All category checkboxes may be deselected. Click **Select All (Logs)** to restore visibility.
- **Audio stream shows high late packet count** — Check the **Latency** page for jitter spikes and the **Packet Loss** page for Audio stream drops. Consider increasing the audio buffer size in audio settings.
- **Navigation tree search returns no results** — Check your spelling or try a different search term. The search matches against page names only.

## Related

- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
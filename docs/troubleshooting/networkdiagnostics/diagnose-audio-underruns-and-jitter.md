# Diagnose audio underruns and jitter

Use the Network Diagnostics dialog to read live audio buffer health, underrun counts, arrival gap timing, and jitter estimates. This helps you identify whether audio dropouts are caused by a starved buffer, bursty packet delivery, or network jitter.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the audio indicators are only meaningful while a radio is connected and streaming audio.
- Reproduce the audio problem before opening the dialog so the counters and peak values reflect the fault condition.
- The dialog window geometry is saved and restored automatically between sessions.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Use the navigation tree on the left to select the view you need:
   - **Overview** – Health cards and summary time-series charts.
   - **Details** – Scrollable grid of all labeled metrics.
   - **Latency** – RTT, arrival gap, and jitter chart.
   - **Rates** – Per-stream incoming bitrate chart.
   - **Packet Loss** – Per-category packet loss percentage chart.
   - **Audio** – Playback buffer fill and underrun rate chart. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream.
   - **Logs** – Live tail of the AetherSDR log file.
3. On the **Details** view, locate the **Audio Playback** group.
4. Read **RX Buffer Now** to see how many bytes (and milliseconds) of audio are currently held in the playback buffer.
5. Read **RX Buffer Peak** to see the highest buffer fill recorded since the dialog was opened.
6. Read **Underruns (total)** to see the cumulative count of buffer underruns since the audio engine started.
7. Read **Underruns (last sec)** to see how many underruns occurred in the most recent one-second window. A non-zero value here while audio is actively streaming indicates an ongoing problem.
8. Read **Audio Arrival Gap** to see the current inter-packet arrival interval. A value significantly larger than the expected packet period indicates bursty delivery.
9. Read **Max Arrival Gap** to see the worst-case arrival gap recorded since the dialog was opened.
10. Read **Network Jitter** to see the smoothed jitter estimate for the audio stream.
11. If underruns are rising but **RX Buffer Now** stays near zero, the buffer is starving — see the tips below.
12. Click **Close** when finished.

## What each control does

### Navigation and search

| Control                    | Type        | Default   | Behavior                                                                                                                                 |
|----------------------------|-------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Navigation tree**        | Tree widget | –         | Left sidebar listing all diagnostic views (Overview, Details, Latency, Rates, Packet Loss, Audio, Logs). Click an item to switch views. The tree item has a minimum height of 38px and highlights with accent color when selected. |
| **Search**                 | Text input  | –         | Filter search box at the top of the dialog. Focus style shows a bright accent border. Enter text to filter displayed information.        |
| **Timeframe**              | Combo box   | 5 minutes | Selects how far back the time-series charts display history. Options: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week. Shown in the top-right corner of the dialog; hidden when the Logs view is active. |

### Views

| View             | Behavior                                                                                                                                       |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Overview**     | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer). |
| **Details**      | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.                        |
| **Latency**      | Full-width time-series graph of RTT, arrival gap and jitter in ms.                                                                            |
| **Rates**        | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                |
| **Packet Loss**  | Full-width time-series graph of packet loss % per stream category.                                                                            |
| **Audio**        | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. |
| **Logs**         | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name. Timeframe selector is hidden while this view is active. |

### Controls

| Control                    | Type        | Default   | Behavior                                                                                                                                 |
|----------------------------|-------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Filter Categories (Logs)** | Checkboxes | –         | Per-category checkboxes filter the log view. Includes a General (default) category plus all registered LogManager categories.            |
| **Select All (Logs)**      | Push button | –         | Shows all log categories in the viewer.                                                                                                 |
| **Deselect All (Logs)**    | Push button | –         | Hides all log categories from the viewer.                                                                                               |
| **Live / Paused (Logs)**   | Toggle button | Live    | When Live, the viewer auto-scrolls to newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.             |
| **Close**                  | Push button | –         | Closes the dialog.                                                                                                                      |
| **Page Title**             | Label       | –         | Displays the name of the currently selected view in the main content area. Font is 20px bold primary text color.                         |

### Indicators

All indicators refresh once per second.

| Indicator               | Meaning                                                                                                  |
|--------------------------|----------------------------------------------------------------------------------------------------------|
| **Status**              | Overall link quality, color-coded green → red. States: Excellent, Very Good, Good, Fair, Poor.           |
| **Target Radio IP**     | IP of connected radio, or "Not connected".                                                              |
| **Selected Source**     | Local NIC/bind path used for the connection.                                                            |
| **Local TCP**           | Local TCP endpoint.                                                                                     |
| **Local UDP**           | Local UDP endpoint.                                                                                     |
| **First UDP Packet**    | Whether the first UDP packet has been received since connect. States: Yes, No.                          |
| **Latency (RTT)**       | Current round-trip time.                                                                                |
| **Max Latency (RTT)**   | Highest RTT seen since connect.                                                                         |
| **Audio / FFT / Waterfall / Meters / DAX rates** | Per-category ingress rate in kbps.                                                   |
| **Total RX / Total TX** | Aggregate bytes per second in each direction.                                                           |
| **Audio / FFT / Waterfall / Meters / DAX drops** | Per-category dropped-packet counts and percentage.                                   |
| **RX Buffer Now / Peak**| Current and peak audio buffer fill in bytes and ms.                                                      |
| **Underruns (total / last sec)** | Audio underrun counters.                                                                        |
| **Audio Arrival Gap / Max Arrival Gap** | Inter-packet arrival timing.                                                           |
| **Network Jitter**      | Smoothed jitter estimate of audio stream in ms.                                                         |
| **Log path label**      | Shows the full path of the log file being tailed.                                                       |
| **Feed Rate**           | Current audio feed rate for each active stream.                                                         |
| **Deficit**             | Current audio deficit for each active stream.                                                           |
| **Late Packets**        | Count of late packets for each active audio stream.                                                     |
| **Packet Class Code**   | Packet class code for each active audio stream.                                                         |
| **Stream Health**       | Health status for each active audio stream.                                                             |

## Using the Logs view

The Logs view provides a live tail of the AetherSDR log file directly inside the Network Diagnostics dialog.

1. Click **Logs** in the navigation tree. The **Timeframe** selector in the top-right corner is hidden while this view is active.
2. The log path is shown at the top of the view. This is the full path of the file being tailed.
3. Use the **Filter Categories (Logs)** checkboxes to include or exclude specific log categories. The General category is available by default; additional categories appear as LogManager registers them.
4. Click **Select All (Logs)** to enable all categories at once. Click **Deselect All (Logs)** to hide all categories.
5. The viewer is in **Live** mode by default and auto-scrolls to the newest output. Scroll upward to pause auto-scrolling; the button changes to **Paused**. Click **Live** to resume and jump back to the tail.
6. Log entries are syntax-highlighted by log level (debug, info, warning, critical) and category name.

## Understanding chart axes

The time-series charts throughout the dialog use consistent axis scaling:

- **Linear scale**: Y-axis ticks are evenly spaced from minimum to maximum value.
- **Log scale** (Rates view): Y-axis uses logarithmic spacing with a baseline of "0" displayed at the bottom. Values at or below 1 unit are functionally considered zero.
- **Fixed Y-range**: Some charts may use a fixed minimum and maximum Y-range for consistent comparison across different timeframes.

## Tips

- **Underruns rising, buffer near zero:** The audio stream is not arriving fast enough to keep the buffer filled. Check the **Audio** rate in the **Incoming Stream Rates** group and compare it to the expected bitrate. A very low or zero Audio rate means packets are not arriving at all.
- **Zero packet loss but still getting underruns:** The **Packet Loss (Sequence Gaps)** group counts only missing VITA sequence numbers. Packets that arrive late rather than missing will not increment the drop counter but will still cause jitter and underruns. Use **Audio Arrival Gap** and **Network Jitter** to detect this condition.
- **Large Max Arrival Gap with low average gap:** This indicates occasional bursts of delayed packets rather than sustained loss. Isolate the network path to the radio and check for competing traffic.
- **RX Buffer Peak is very low:** The buffer never built up a useful reserve. This makes the stream sensitive to any delivery variation. Check the network path and consider whether other heavy traffic is competing on the same link.
- **Investigating unexpected disconnects or errors:** Open the **Logs** view and enable the relevant LogManager categories. Use **Filter Categories (Logs)** to focus on the category of interest, then reproduce the fault while the viewer is in **Live** mode.
- **Per-stream RX audio diagnostics:** On the **Audio** view, review the feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. This helps identify individual stream issues that may not affect other streams.

## Troubleshooting

- **All audio indicators show zero or no data** — The radio is not streaming audio. Confirm the radio is connected and a receiver slice is active.
- **Underruns (last sec) is non-zero but Underruns (total) is small** — The problem is intermittent. Leave the dialog open and wait for a longer observation period. Watch **Max Arrival Gap** for evidence of periodic bursts.
- **Network Jitter is high but Audio drops show zero** — Packets are arriving late rather than being lost. Jitter directly reduces the effective buffer margin. Check for other UDP traffic competing on the same interface.
- **Logs view shows no output** — Confirm the log file path shown at the top of the view is accessible. If no categories are checked, click **Select All (Logs)** to restore visibility.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
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
   - **Connection Details** – Scrollable grid of all labeled metrics, including the Adaptive Frame-Rate Throttle section.
   - **Latency** – RTT, arrival gap, and jitter chart.
   - **Rates** – Per-stream incoming bitrate chart.
   - **Packet Loss** – Per-category packet loss percentage chart.
   - **Audio** – Playback buffer fill and underrun rate chart. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream.
   - **Logs** – Live tail of the AetherSDR log file.
   - **TCI Clients** – Lists connected TCI clients with a live traffic monitor (available only in TCI-enabled builds).
3. On the **Connection Details** view, locate the **Audio Playback** group.
4. Read **RX Buffer Now** to see how many bytes (and milliseconds) of audio are currently held in the playback buffer.
5. Read **RX Buffer Peak** to see the highest buffer fill recorded since the dialog was opened.
6. Read **Underruns (total)** to see the cumulative count of buffer underruns since the audio engine started.
7. Read **Underruns (last sec)** to see how many underruns occurred in the most recent one-second window. A non-zero value here while audio is actively streaming indicates an ongoing problem.
8. Read **Audio Arrival Gap** to see the current inter-packet arrival interval. A value significantly larger than the expected packet period indicates bursty delivery.
9. Read **Max Arrival Gap** to see the worst-case arrival gap recorded since the dialog was opened.
10. Read **Network Jitter** to see the smoothed jitter estimate for the audio stream.
11. On the **Connection Details** view, locate the **Adaptive Frame-Rate Throttle** section to see the throttle's Current State, Pending Lift, and Sessions This Run values.
12. If underruns are rising but **RX Buffer Now** stays near zero, the buffer is starving — see the tips below.
13. Click **Close** when finished.

## What each control does

### Navigation and search

| Control                    | Type        | Default   | Behavior                                                                                                                                 |
|----------------------------|-------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------|
| **Navigation tree**        | Tree widget | –         | Left sidebar listing all diagnostic views (Overview, Connection Details, Latency, Rates, Packet Loss, Audio, Logs, TCI Clients). Click an item to switch views. The tree item has a minimum height of 38px and highlights with accent color when selected. |
| **Search**                 | Text input  | –         | Filter search box at the top of the dialog. Focus style shows a bright accent border. Enter text to filter displayed information.        |
| **Timeframe**              | Combo box   | 5 minutes | Selects how far back the time-series charts display history. Options: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week. Shown in the top-right corner of the dialog; hidden when the Logs or TCI Clients view is active. |

### Views

| View                  | Behavior                                                                                                                                       |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| **Overview**          | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer). |
| **Connection Details**| Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, Audio Playback, and the Adaptive Frame-Rate Throttle section. Includes a Read-Only Clipboard Copy action to copy the whole diagnostic summary. |
| **Latency**           | Full-width time-series graph of RTT, arrival gap and jitter in ms.                                                                            |
| **Rates**             | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                |
| **Packet Loss**       | Full-width time-series graph of packet loss % per stream category.                                                                            |
| **Audio**             | Full-width time-series graph of playback buffer fill (ms) and underruns/s. Includes per-stream RX audio diagnostics showing feed rate, deficit, late packets, packet class code, and stream health for each active audio stream. |
| **Logs**              | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name. Timeframe selector is hidden while this view is active. |
| **TCI Clients**       | Lists connected TCI clients with a live traffic monitor (Pause/Save log/Clear), answer-command suppression controls, and per-client details. Timeframe selector is hidden on this page. Available only in TCI-enabled builds. |

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
| **Latency (RTT)**       | Current round-trip time. Shows "not measured on this link" when the transport has no round trip to time. |
| **Max Latency (RTT)**   | Highest RTT seen since connect. Shows "not measured on this link" when the transport has no round trip to time. |
| **Audio / FFT / Waterfall / Meters / DAX rates** | Per-category ingress rate in kbps. Shows "n/a" when the transport does not support per-stream category statistics. |
| **Total RX / Total TX** | Aggregate bytes per second in each direction.                                                           |
| **Audio / FFT / Waterfall / Meters / DAX drops** | Per-category dropped-packet counts and percentage. Shows "n/a" when the transport does not support per-stream category statistics. |
| **RX Buffer Now / Peak**| Current and peak audio buffer fill in bytes and ms.                                                      |
| **Underruns (total / last sec)** | Audio underrun counters.                                                                        |
| **Audio Arrival Gap / Max Arrival Gap** | Inter-packet arrival timing. Shows "not measured on this link" when timing data is not available.         |
| **Network Jitter**      | Smoothed jitter estimate of audio stream in ms. Shows "not measured on this link" when timing data is not available. |
| **Log path label**      | Shows the full path of the log file being tailed.                                                       |
| **Feed Rate**           | Current audio feed rate for each active stream.                                                         |
| **Deficit**             | Current audio deficit for each active stream.                                                           |
| **Late Packets**        | Count of late packets for each active audio stream.                                                     |
| **Packet Class Code**   | Packet class code for each active audio stream.                                                         |
| **Stream Health**       | Health status for each active audio stream.                                                             |
| **Adaptive Frame-Rate Throttle: Current State** | Current state of the adaptive throttle.                                                     |
| **Adaptive Frame-Rate Throttle: Pending Lift** | Whether a throttle lift is pending.                                                         |
| **Adaptive Frame-Rate Throttle: Sessions This Run** | Number of throttle sessions since the connection started.                                     |

## Using the Logs view

The Logs view provides a live tail of the AetherSDR log file directly inside the Network Diagnostics dialog.

1. Click **Logs** in the navigation tree. The **Timeframe** selector in the top-right corner is hidden while this view is active.
2. The log path is shown at the top of the view. This is the full path of the file being tailed.
3. Use the **Filter Categories (Logs)** checkboxes to include or exclude specific log categories. The General category is available by default; additional categories appear as LogManager registers them.
4. Click **Select All (Logs)** to enable all categories at once. Click **Deselect All (Logs)** to hide all categories.
5. The viewer is in **Live** mode by default and auto-scrolls to the newest output. Scroll upward to pause auto-scrolling; the button changes to **Paused**. Click **Live** to resume and jump back to the tail.
6. Log entries are syntax-highlighted by log level (debug, info, warning, critical) and category name.

## Using the TCI Clients view

The TCI Clients view lists connected TCI clients and provides a live traffic monitor. This view is only available in builds with TCI support enabled.

1. Click **TCI Clients** in the navigation tree. The **Timeframe** selector in the top-right corner is hidden while this view is active.
2. Review the list of connected TCI clients and their per-client details.
3. Use the traffic monitor controls to **Pause** the live view, **Save log** to disk, or **Clear** the current traffic data.
4. Use the answer-command suppression controls to manage how the radio responds to TCI client commands.

## Understanding chart axes

The time-series charts throughout the dialog use consistent axis scaling:

- **Linear scale**: Y-axis ticks are evenly spaced from minimum to maximum value.
- **Log scale** (Rates view): Y-axis uses logarithmic spacing with a baseline of "0" displayed at the bottom. Values at or below 1 unit are functionally considered zero.
- **Fixed Y-range**: Some charts may use a fixed minimum and maximum Y-range for consistent comparison across different timeframes.
- **Not measured series**: On transports that have no round trip to time (such as a single-stream link), the RTT series is omitted from the Latency chart rather than drawn as a flat 0 ms line.

## Understanding the Adaptive Frame-Rate Throttle

The Adaptive Frame-Rate Throttle reduces panadapter frame rates when latency or packet loss is detected, helping to maintain a stable audio stream under degraded network conditions.

1. Open the **Connection Details** view.
2. Locate the **Adaptive Frame-Rate Throttle** section. This section is hidden until throttle data is available.
3. Read **Current State** to see whether the throttle is active or idle.
4. Read **Pending Lift** to see whether a throttle lift is pending.
5. Read **Sessions This Run** to see how many throttle sessions have occurred since the connection started.

## Understanding "not measured on this link"

In v26.8.4, certain latency and timing indicators show "not measured on this link" when the current transport cannot produce that measurement. This is distinct from a value of "0" or "< 1 ms": it means the measurement does not exist for this link type, not that the value is zero.

- **Latency (RTT)** and **Max Latency (RTT)** show "not measured on this link" when the transport has no round trip to time.
- **Audio Arrival Gap**, **Max Arrival Gap**, and **Network Jitter** show "not measured on this link" until the first delivery-timing window has closed (a backend is considered "reported" from its first tick, one second before its first timing window closes).

## Tips

- **Underruns rising, buffer near zero:** The audio stream is not arriving fast enough to keep the buffer filled. Check the **Audio** rate in the **Incoming Stream Rates** group and compare it to the expected bitrate. A very low or zero Audio rate means packets are not arriving at all.
- **Zero packet loss but still getting
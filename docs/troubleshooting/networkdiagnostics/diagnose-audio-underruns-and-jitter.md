# Diagnose audio underruns and jitter

Use the Network Diagnostics dialog to read live audio buffer health, underrun counts, arrival gap timing, and jitter estimates. This helps you identify whether audio dropouts are caused by a starved buffer, bursty packet delivery, or network jitter.

## Before you start

- AetherSDR must be running. The dialog does not require an active radio connection, but the audio indicators are only meaningful while a radio is connected and streaming audio.
- Reproduce the audio problem before opening the dialog so the counters and peak values reflect the fault condition.
- The dialog window can be toggled between frameless and standard window decoration. This is controlled by the `FramelessWindow` setting in AetherSDR's configuration. When frameless mode is active, a title bar with drag-and-resize handles appears at the top of the dialog.

## Steps

1. Click `Settings > Network...` to open the Network Diagnostics dialog.
2. Locate the **Audio Playback** group in the lower-right area of the dialog.
3. Read **RX Buffer Now** to see how many bytes (and milliseconds) of audio are currently held in the playback buffer.
4. Read **RX Buffer Peak** to see the highest buffer fill recorded since the dialog was opened.
5. Read **Underruns (total)** to see the cumulative count of buffer underruns since the audio engine started.
6. Read **Underruns (last sec)** to see how many underruns occurred in the most recent one-second window. A non-zero value here while audio is actively streaming indicates an ongoing problem.
7. Read **Audio Arrival Gap** to see the current inter-packet arrival interval. A value significantly larger than the expected packet period indicates bursty delivery.
8. Read **Max Arrival Gap** to see the worst-case arrival gap recorded since the dialog was opened.
9. Read **Network Jitter** to see the smoothed jitter estimate for the audio stream.
10. If underruns are rising but **RX Buffer Now** stays near zero, the buffer is starving — see the tips below.
11. Click **Close** when finished.

## What each control does

| Indicator                | Meaning                                                                                                                                                                      | Notes                                                                             |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **RX Buffer Now**        | Current audio buffer fill, shown in bytes and milliseconds.                                                                                                                  |                                                                                   |
| **RX Buffer Peak**       | Highest buffer fill seen since the dialog was opened.                                                                                                                        |                                                                                   |
| **Underruns (total)**    | Cumulative count of audio buffer underruns since the audio engine started.                                                                                                   |                                                                                   |
| **Underruns (last sec)** | Number of underruns that occurred in the last one-second interval.                                                                                                           |                                                                                   |
| **Audio Arrival Gap**    | Time between consecutive incoming audio packet arrivals.                                                                                                                     |                                                                                   |
| **Max Arrival Gap**      | Largest arrival gap recorded since the dialog was opened.                                                                                                                    |                                                                                   |
| **Network Jitter**       | Smoothed estimate of audio stream jitter.                                                                                                                                    |                                                                                   |
| Overview (tab)           | Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series graphs (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer). |                                                                                   |
| Details (tab)            | Scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.                                                       |                                                                                   |
| Latency (tab)            | Full-width time-series graph of RTT, arrival gap and jitter in ms.                                                                                                           |                                                                                   |
| Rates (tab)              | Full-width log-scale time-series graph of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.                                               |                                                                                   |
| Packet Loss (tab)        | Full-width time-series graph of packet loss % per stream category.                                                                                                           |                                                                                   |
| Audio (tab)              | Full-width time-series graph of playback buffer fill (ms) and underruns/s.                                                                                                   |                                                                                   |
| Logs (tab)               | Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name.                                                     | Timeframe selector is hidden while this tab is active.                            |
| Timeframe                | Selects how far back the time-series charts display history. Default is 5 minutes. Valid values: 1 minute, 5 minutes, 15 minutes, 1 hour, 1 day, 1 week.                     | Shown in the top-right corner of the tab bar; hidden when the Logs tab is active. |
| Filter Categories (Logs) | Per-category checkboxes filter the log view. Includes a General (default) category plus all registered LogManager categories.                                                |                                                                                   |
| Select All (Logs)        | Shows all log categories in the viewer.                                                                                                                                      |                                                                                   |
| Deselect All (Logs)      | Hides all log categories from the viewer.                                                                                                                                    |                                                                                   |
| Live / Paused (Logs)     | When Live, the viewer auto-scrolls to newest output. Scrolling up auto-pauses; clicking Live resumes and jumps to the tail.                                                  |                                                                                   |

All indicators refresh once per second.

## Using the Logs tab

The Logs tab provides a live tail of the AetherSDR log file directly inside the Network Diagnostics dialog.

1. Click the **Logs** tab. The **Timeframe** selector in the top-right corner is hidden while this tab is active.
2. The log path is shown at the top of the tab. This is the full path of the file being tailed.
3. Use the **Filter Categories (Logs)** checkboxes to include or exclude specific log categories. The General category is available by default; additional categories appear as LogManager registers them.
4. Click **Select All (Logs)** to enable all categories at once. Click **Deselect All (Logs)** to hide all categories.
5. The viewer is in **Live** mode by default and auto-scrolls to the newest output. Scroll upward to pause auto-scrolling; the button changes to **Paused**. Click **Live** to resume and jump back to the tail.
6. Log entries are syntax-highlighted by log level (debug, info, warning, critical) and category name.

## Tips

- **Underruns rising, buffer near zero:** The audio stream is not arriving fast enough to keep the buffer filled. Check the **Audio** rate in the **Incoming Stream Rates** group and compare it to the expected bitrate. A very low or zero Audio rate means packets are not arriving at all.
- **Zero packet loss but still getting underruns:** The **Packet Loss (Sequence Gaps)** group counts only missing VITA sequence numbers. Packets that arrive late rather than missing will not increment the drop counter but will still cause jitter and underruns. Use **Audio Arrival Gap** and **Network Jitter** to detect this condition.
- **Large Max Arrival Gap with low average gap:** This indicates occasional bursts of delayed packets rather than sustained loss. Isolate the network path to the radio and check for competing traffic.
- **RX Buffer Peak is very low:** The buffer never built up a useful reserve. This makes the stream sensitive to any delivery variation. Check the network path and consider whether other heavy traffic is competing on the same link.
- **Investigating unexpected disconnects or errors:** Open the **Logs** tab and enable the relevant LogManager categories. Use **Filter Categories (Logs)** to focus on the category of interest, then reproduce the fault while the viewer is in **Live** mode.

## Troubleshooting

- **All audio indicators show zero or no data** — The radio is not streaming audio. Confirm the radio is connected and a receiver slice is active.
- **Underruns (last sec) is non-zero but Underruns (total) is small** — The problem is intermittent. Leave the dialog open and wait for a longer observation period. Watch **Max Arrival Gap** for evidence of periodic bursts.
- **Network Jitter is high but Audio drops show zero** — Packets are arriving late rather than being lost. Jitter directly reduces the effective buffer margin. Check for other UDP traffic competing on the same interface.
- **Logs tab shows no output** — Confirm the log file path shown at the top of the tab is accessible. If no categories are checked, click **Select All (Logs)** to restore visibility.
- **Dialog appears with standard window frame** — The `FramelessWindow` setting may be set to `False`. To enable frameless mode, set `FramelessWindow` to `True` in the AetherSDR configuration file. The dialog respects the setting each time it opens.

## Related

- [Network Diagnostics overview](../../features/network-diagnostics/overview.md)
- [Measure RTT and packet drops during audio problems](../../features/network-diagnostics/measure-rtt-and-packet-drops-during-audio-problems.md)
- [Check per-category data rates (audio, FFT, waterfall, meters, DAX)](../../features/network-diagnostics/check-per-category-data-rates-audio-fft-waterfall-meters-dax.md)
# Network Diagnostics

The Network Diagnostics dialog provides a live view of the network link to the radio. It features a multi-tab layout with an overview dashboard, detailed metrics, per-stream performance graphs, and a live log viewer.

## Opening Network Diagnostics

1. Go to `Settings > Network...`.
2. The Network Diagnostics dialog opens.

## Tabs

The dialog contains the following tabs:

- **Overview** – Shows four health cards (Status, Latency, Packet Loss, Audio Buffer) and four time-series charts (Latency and Jitter, Recent Packet Loss, Total Stream Rates, Audio Buffer).
- **Details** – A scrollable grid with labeled values for Network Status, Incoming Stream Rates, Packet Loss, and Audio Playback groups.
- **Latency** – Full-width time-series chart of RTT, arrival gap, and jitter in ms.
- **Rates** – Full-width log-scale time-series chart of per-stream incoming bitrates (RX total, Audio, FFT, Waterfall, Meters, DAX) in kbps.
- **Packet Loss** – Full-width time-series chart of packet loss percentage per stream category.
- **Audio** – Full-width time-series chart of playback buffer fill (ms) and underruns per second.
- **Logs** – Live tail of the AetherSDR log file, filtered by category checkboxes. Syntax-highlighted by log level and category name.

## Timeframe selector

A dropdown at the top-right corner of the tab bar selects how far back the time-series charts display history. The following options are available:

- 1 minute
- 5 minutes (default)
- 15 minutes
- 1 hour
- 1 day
- 1 week

The timeframe selector is hidden when the **Logs** tab is active.

## Pause log scrolling to inspect an older entry

The Logs tab tails the AetherSDR log file in real time. This section explains how to pause that automatic scrolling so you can read an older entry without it jumping away, and how to resume live tailing when you are done.

### Steps

1. Open Network Diagnostics via `Settings > Network...`.
2. Click the **Logs** tab.
3. To pause scrolling, do either of the following:
   - Scroll up in the log viewer. The viewer automatically switches to **Paused**.
   - Click the toggle button, which reads **Live**, to switch it to **Paused**.
4. Read the entry you need. The display stays fixed while the button shows **Paused**.
5. When you are ready to return to the live tail, click the toggle button, which now reads **Paused**, to switch it back to **Live**. The viewer immediately jumps to the newest output and resumes auto-scrolling.

### Logs tab controls

| Control | Default | Behavior |
|---|---|---|
| **Live / Paused** (toggle button) | Live | When set to **Live**, the viewer auto-scrolls to the newest log output. When set to **Paused**, scrolling stops and the display holds its current position. Scrolling up in the viewer automatically switches the button to **Paused**. Clicking the button while it reads **Paused** resumes auto-scrolling and jumps to the tail. |
| **Filter Categories** (checkboxes) | – | Per-category checkboxes filter the log view. Includes a "General" (default) category plus all registered LogManager categories. |
| **Select All** (push button) | – | Shows all log categories in the viewer. |
| **Deselect All** (push button) | – | Hides all log categories from the viewer. |

### Tips

- Scrolling up is the fastest way to pause — you do not need to reach for the toggle button first.
- The log view is syntax-highlighted by log level and category name, which makes it easier to spot the entry you are looking for.
- Category filter checkboxes and the **Select All** and **Deselect All** buttons remain active while paused, so you can narrow the visible entries without resuming live scrolling.

## Indicators

The dialog displays the following indicators:

| Indicator | Meaning |
|---|---|
| Status | Overall link quality, color-coded green → red. States: Excellent, Very Good, Good, Fair, Poor |
| Target Radio IP | IP of connected radio, or "Not connected" |
| Selected Source | Local NIC/bind path used for the connection |
| Local TCP | Local TCP endpoint |
| Local UDP | Local UDP endpoint |
| First UDP Packet | Whether the first UDP packet has been received since connect (Yes/No) |
| Latency (RTT) | Current round-trip time |
| Max Latency (RTT) | Highest RTT seen since connect |
| Audio / FFT / Waterfall / Meters / DAX rates | Per-category ingress rate in kbps |
| Total RX / Total TX | Aggregate bytes per second in each direction |
| Audio / FFT / Waterfall / Meters / DAX drops | Per-category dropped-packet counts and percentage |
| RX Buffer Now / Peak | Current and peak audio buffer fill in bytes and ms |
| Underruns (total / last sec) | Audio underrun counters |
| Audio Arrival Gap / Max Arrival Gap | Inter-packet arrival timing |
| Network Jitter | Smoothed jitter estimate of audio stream in ms |
| Log path label | Full path of the log file being tailed |

## Frameless mode

The Network Diagnostics dialog can appear with or without a title bar, based on the global `FramelessWindow` setting (`Settings > Appearance > Frameless Window`). When frameless mode is enabled, the dialog includes a custom title bar and resize handles. When disabled, the window uses the standard operating system title bar and decorations.

## Closing the dialog

Click **Close** to close the Network Diagnostics dialog.
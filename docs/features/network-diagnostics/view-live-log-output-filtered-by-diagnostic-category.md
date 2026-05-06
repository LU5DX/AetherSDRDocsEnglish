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

| Control | Behavior | Default |
|---|---|---|
| **Logs** (tab) | Live tail of the AetherSDR log file filtered by category checkboxes. Syntax-highlighted by log level and category name. The **Timeframe** selector is hidden while this tab is active. | — |
| **Filter Categories** | Per-category checkboxes. Check a category to include its lines; uncheck to hide them. Includes **General** plus all registered LogManager categories. | — |
| **Select All** | Shows all log categories in the viewer immediately. | — |
| **Deselect All** | Hides all log categories from the viewer immediately. | — |
| **Live / Paused** | When **Live**, the viewer auto-scrolls to the newest output. Scrolling up switches the state to **Paused**. Clicking the toggle when it reads **Paused** resumes auto-scroll and jumps to the tail. | Live |
| **Log path label** | Displays the full filesystem path of the log file being tailed. | — |

## Tips

- The log view refreshes every 500 ms, so there is a short delay between a message being written and it appearing in the viewer.
- Syntax highlighting colors help distinguish log levels at a glance: `INF` lines appear in blue, `WRN` in amber, and `CRT`/`FTL` in red. Category names are shown in bold. Numbers and protocol tokens (such as `UDP`, `TCP`, `RX`, `TX`) are highlighted separately.
- If you want to freeze the display to read a specific entry, scroll up. The viewer switches to **Paused** automatically. Click **Live** to return to the tail.
- Clicking **Deselect All** and then checking a single category is the fastest way to isolate one subsystem's output.

## Related

- [Pause log scrolling to inspect an older entry](pause-log-scrolling-to-inspect-an-older-entry.md)
- [Network Diagnostics overview](overview.md)
- [Measure RTT and packet drops during audio problems](measure-rtt-and-packet-drops-during-audio-problems.md)

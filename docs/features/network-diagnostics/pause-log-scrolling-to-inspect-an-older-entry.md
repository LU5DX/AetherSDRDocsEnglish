# Pause log scrolling to inspect an older entry

The Logs tab in Network Diagnostics tails the AetherSDR log file in real time. This page explains how to pause that automatic scrolling so you can read an older entry without it jumping away, and how to resume live tailing when you are done.

## Before you start

- Open Network Diagnostics via `Settings > Network...`.
- Click the **Logs** tab to make the log viewer visible.

## Steps

1. Go to `Settings > Network...`.
2. Click the **Logs** tab.
3. To pause scrolling, do either of the following:
   - Scroll up in the log viewer. The viewer automatically switches to **Paused**.
   - Click the toggle button, which reads **Live**, to switch it to **Paused**.
4. Read the entry you need. The display stays fixed while the button shows **Paused**.
5. When you are ready to return to the live tail, click the toggle button, which now reads **Paused**, to switch it back to **Live**. The viewer immediately jumps to the newest output and resumes auto-scrolling.

## What each control does

| Control | Default | Behavior |
|---|---|---|
| **Live / Paused** (toggle button) | Live | When set to **Live**, the viewer auto-scrolls to the newest log output. When set to **Paused**, scrolling stops and the display holds its current position. Scrolling up in the viewer automatically switches the button to **Paused**. Clicking the button while it reads **Paused** resumes auto-scrolling and jumps to the tail. |

## Tips

- Scrolling up is the fastest way to pause — you do not need to reach for the toggle button first.
- The log view is syntax-highlighted by log level and category name, which makes it easier to spot the entry you are looking for before the display was paused.
- Category filter checkboxes (**Filter Categories**) and the **Select All** and **Deselect All** buttons remain active while paused, so you can narrow the visible entries without resuming live scrolling.

## Related

- [View live log output filtered by diagnostic category](view-live-log-output-filtered-by-diagnostic-category.md)
- [Network Diagnostics overview](overview.md)

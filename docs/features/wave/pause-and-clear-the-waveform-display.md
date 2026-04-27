# Pause and clear the waveform display

The waveform display can be frozen so you can inspect a transient in detail, or wiped clean to start fresh. Use these gestures to control what the display is showing without affecting the audio stream itself.

## Before you start

- The Waveform applet must be visible. If it is not, click the WAVE tray button in the right sidebar to show it.

## Steps

### Pause and resume

1. Single-click anywhere on the waveform display.
   The display freezes on the current buffer snapshot. A **PAUSED** badge appears in the footer.
2. Single-click the display again to resume live updating. The **PAUSED** badge disappears.

### Clear the buffer

1. Double-click anywhere on the waveform display.
   The ring buffer for the active direction (RX or TX) is cleared and the display resets to empty.

## What each control does

| Interaction | Behavior | Default state |
|---|---|---|
| Single-click on display | Toggles between live and paused. While paused, a snapshot of the buffer is shown and a **PAUSED** badge appears in the footer. | Live |
| Double-click on display | Clears the ring buffer for the active direction (RX or TX). Resets the display to empty. | — |

## Tips

- Pause is direction-aware: the snapshot preserves whichever side (RX or TX) was active at the moment you clicked. The direction tint and the RX/TX label in the header remain visible so you can tell which path you are inspecting.
- Double-clicking clears only the active direction's buffer. If you are in RX mode, the TX buffer is not affected.
- The display shows a 100 ms time window. Pausing is most useful when you need to measure a brief event that would otherwise scroll off before you can examine it.

## Troubleshooting

- **Double-click clears instead of pausing** — This is expected. Qt disambiguates single from double clicks using the system double-click interval. Click once and wait; if the display does not pause, try clicking more slowly.
- **PAUSED badge is not visible** — The badge appears in the footer, to the right of the time scale readout. If the applet is very narrow, the footer text may be truncated. Widen the applet panel or pop it out with `View > Pop Out Applet Panel`.

## Related

- [Waveform applet overview](overview.md)
- [Use the waveform display to monitor TX or RX audio](use-the-waveform-display-to-monitor-tx-or-rx-audio.md)

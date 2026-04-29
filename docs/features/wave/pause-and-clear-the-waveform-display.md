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
   The settings drawer opens or closes. To reset the buffer programmatically, use the `WaveformWidget::clear()` slot or reconnect the audio source.

## What each control does

| Interaction             | Behavior                                                                                                                                                                                         | Default state                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Single-click on display | Toggles between live and paused. While paused, a snapshot of the buffer is shown and a **PAUSED** badge appears in the footer.                                                                   | Live                                                                                                                     |
| Double-click on display | Toggles the settings drawer open or closed. Does not clear the buffer.                                                                                                                           | —                                                                                                                        |
| View                    | Selects the waveform visualization mode: Scope (Graph = min/max + RMS lines), Envelope (peak/RMS filled area), History (horizontal level bars), Bands (frequency band bars via Goertzel filter). | Located in the collapsible settings drawer below the waveform. Persisted as `Graph`, `Envelope`, `History`, or `Bands`. |
| Zoom                    | Scales the amplitude axis; higher values stretch small signals vertically, causing clipping artifacts to appear sooner.                                                                           | Located in the settings drawer. Default 170% (1.7x).                                                                    |
| FPS                     | Controls how often the waveform repaints; lower values reduce CPU load on slow systems.                                                                                                          | Located in the settings drawer.                                                                                          |

## Tips

- Pause is direction-aware: the snapshot preserves whichever side (RX or TX) was active at the moment you clicked. The direction tint and the RX/TX label in the header remain visible so you can tell which path you are inspecting.
- Double-clicking toggles the settings drawer, not the buffer. To clear the buffer, use the `WaveformWidget::clear()` slot or reconnect to reset.
- The display shows a 100 ms time window. Pausing is most useful when you need to measure a brief event that would otherwise scroll off before you can examine it.

## Troubleshooting

- **Double-click opens the settings drawer instead of clearing the buffer** — This is the intended behavior as of v0.9.2.1. Double-click now toggles the settings drawer. To reset the waveform buffer, use the `WaveformWidget::clear()` slot or reconnect the audio source.
- **Single-click is not pausing** — Qt disambiguates single from double clicks using the system double-click interval. Click once and wait; if the display does not pause, try clicking more slowly.
- **PAUSED badge is not visible** — The badge appears in the footer, to the right of the time scale readout. If the applet is very narrow, the footer text may be truncated. Widen the applet panel or pop it out with `View > Pop Out Applet Panel`.

## Related

- [Waveform applet overview](overview.md)
- [Use the waveform display to monitor TX or RX audio](use-the-waveform-display-to-monitor-tx-or-rx-audio.md)
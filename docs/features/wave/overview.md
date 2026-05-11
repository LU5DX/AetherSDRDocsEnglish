# Waveform applet overview

The Waveform applet is an audio oscilloscope that displays the time-domain waveform of the active RX or TX audio path. Use it to spot clipping, dropouts, and audio level problems at a glance without reaching for an external meter.

## How it works

The applet renders a scrolling time window of mono audio. The window duration is adjustable from 240 ms to 10 seconds via a discrete-step slider in the settings drawer. The display is continuously fed samples from the audio engine. Each pixel column shows the min/max envelope of the samples that fall within it, with separate peak and RMS envelope traces drawn over the top.

The header line shows the current direction (RX or TX), RMS level in dBFS, and peak level in dBFS. The footer shows the sample rate, window duration, and time per division.

Two separate ring buffers — one for RX and one for TX — run in parallel. The display draws from whichever buffer matches the current transmit state. When you switch from receive to transmit, the tint changes and the display immediately begins drawing from the TX buffer.

To open or close the applet, click the **WAVE** tray button in row 1 of the right sidebar. The applet is on by default and is inserted immediately after the EQ button on first run after upgrading to v0.9.1.

The applet no longer enforces a fixed height; it resizes vertically with the layout.

## What each control does

| Control                 | Behavior                                                                                                                                                                                         | Notes                                                                                                                   |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Waveform display        | Renders the min/max envelope per pixel column with peak and RMS envelope traces over the configured time window.                                                                                 | No persisted setting key.                                                                                               |
| Single-click on display | Toggles between live and paused. While paused, a snapshot of the buffer is held until you click again.                                                                                           | A **PAUSED** badge appears in the footer. Default state is live.                                                        |
| Double-click on display | Toggles the settings drawer open or closed.                                                                                                                                                      | Does not clear the buffer. To reset the display, use the WaveformWidget::clear() slot or reconnect.                     |
| View                    | Selects the waveform visualization mode: Scope (Graph = min/max + RMS lines), Envelope (peak/RMS filled area), History (horizontal level bars), Bands (frequency band bars via Goertzel filter). | Located in the collapsible settings drawer below the waveform. Persisted as `WaveApplet_ViewMode`.                      |
| Zoom                    | Scales the amplitude axis; higher values stretch small signals vertically, causing clipping artifacts to appear sooner.                                                                          | Located in the settings drawer. Default 170% (1.7x). Persisted as `WaveApplet_ZoomPercent`.                             |
| FPS                     | Controls how often the waveform repaints; lower values reduce CPU load on slow systems.                                                                                                          | Located in the settings drawer. Persisted as `WaveApplet_RefreshRateHz`.                                                |
| Window                  | Sets the time window duration. Discrete steps: 240 ms, 480 ms, 1 s, then 1-second increments to 10 s.                                                                                           | Located in the settings drawer. Persisted as `WaveApplet_TimeWindowMs`. Default 1000 ms (1 s).                          |

### Settings drawer controls

The settings drawer contains the following controls:

- **View** combo box — Selects waveform visualization mode. Options: Scope, Envelope, History, Bands. Persisted as `WaveApplet_ViewMode`.
- **Zoom** slider — Amplitude scaling from 1.0x to 6.0x. Default 1.7x (170%). Persisted as `WaveApplet_ZoomPercent`.
- **FPS** slider — Refresh rate from 5 to 30 Hz. Default 24 Hz. Persisted as `WaveApplet_RefreshRateHz`.
- **Window** slider — Time window duration. Steps: 240 ms, 480 ms, 1 s, 2 s, 3 s, 4 s, 5 s, 6 s, 7 s, 8 s, 9 s, 10 s. Default 1 s. Persisted as `WaveApplet_TimeWindowMs`.

On initial launch after upgrading from a version using `WaveApplet_TimeWindowSec`, your previous window setting is migrated to the nearest available step in the new discrete-step system.

## Indicators

- **Direction tint** — The display uses a cool tint for RX and a warm tint for TX so the active audio path is unambiguous without reading the header label.
- **Clipping highlight** — Any pixel column containing samples at or above the clipping threshold is highlighted in red at the top and bottom edges of the plot. A **CLIP** count also appears in the header, in bold red, showing the number of clipped samples in the current window.
- **PAUSED badge** — Shown in the footer when the display is frozen on a snapshot. No badge means the display is live.
- **No-audio placeholder** — If no samples have arrived within the last second, or the display buffer is empty, a placeholder message replaces the empty trace.

## Tips

- The waveform color and line width follow the `DisplayFftFillColor` and `DisplayFftLineWidth` display settings used elsewhere in AetherSDR. Valid line width range is 1.0 to 3.0 px; default is 2.0.
- Grid lines can be suppressed via `DisplayShowGrid`. When enabled, the display draws major and minor grid lines behind the trace.
- Single-click to pause is particularly useful for catching a transient: click immediately after the event, inspect the frozen waveform, then click again to resume.
- Double-click on the display toggles the settings drawer. To clear the waveform buffer, use the WaveformWidget::clear() slot or reconnect to the audio engine.
- The Window slider provides discrete steps only — it does not allow free-scrolling through millisecond values. Use the closest step that captures the time span you need.

## Related

- [Use the waveform display to monitor TX or RX audio](use-the-waveform-display-to-monitor-tx-or-rx-audio.md)
- [Pause and clear the waveform display](pause-and-clear-the-waveform-display.md)
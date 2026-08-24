# Waveform applet overview

The Waveform applet is an audio oscilloscope that displays the time-domain waveform of the active RX or TX audio path in one of four view modes (Scope, Envelope, History bars, Bands spectrum). Use it to spot clipping, dropouts, and audio level problems at a glance without reaching for an external meter.

## How it works

The applet renders a scrolling time window of mono audio. The window duration is adjustable from 10 ms to 500 ms via a slider in the settings drawer. The display is continuously fed samples from the audio engine. Each pixel column shows the min/max envelope of the samples that fall within it, with separate peak and RMS envelope traces drawn over the top.

The header line shows the current direction (RX or TX), RMS level in dBFS, and peak level in dBFS.

Two separate ring buffers — one for RX and one for TX — run in parallel. The display draws from whichever buffer matches the current transmit state. When you switch from receive to transmit, the tint changes and the display immediately begins drawing from the TX buffer.

To open or close the applet, click the **WAVE** tray button in row 1 of the right sidebar. The applet is on by default and is inserted immediately after the EQ button on first run after upgrading to v0.9.1.

The applet no longer enforces a fixed height; it resizes vertically with the layout.

## What each control does

| Control                 | Behavior                                                                                                                                                                                         | Notes                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Waveform display        | Renders mono float-32 PCM scope samples. Displays min/max waveform, RMS envelope, peak markers, and clipping highlights in the active view mode.                                                 | TX direction tinted differently from RX so the current side is obvious without reading a label. Header readout shows RX/TX, RMS dBFS, and PK dBFS. |
| Single-click on display | Toggles between live and paused. While paused, a snapshot of the buffer is held until you click again.                                                                                           | A **PAUSED** badge appears in the footer. Default state is live.                                                                                   |
| Double-click on display | Toggles the settings drawer open or closed.                                                                                                                                                      | Does not clear the buffer. To reset the display, use the WaveformWidget::clear() slot or reconnect.                                                |
| View                    | Selects the waveform visualization mode: Scope (Graph = min/max + RMS lines), Envelope (peak/RMS filled area), History (horizontal level bars), Bands (frequency band bars via Goertzel filter). | Located in the collapsible settings drawer below the waveform. Persisted as `WaveApplet_ViewMode`.                                                 |
| Zoom                    | Scales the amplitude axis; higher values stretch small signals vertically, causing clipping artifacts to appear sooner.                                                                          | Located in the settings drawer. Default 170% (1.7x). Persisted as `WaveApplet_ZoomPercent`.                                                        |
| FPS                     | Controls how often the waveform repaints; lower values reduce CPU load on slow systems.                                                                                                          | Located in the settings drawer. Range 5–30 Hz. Default 24 Hz. Persisted as `WaveApplet_RefreshRateHz`.                                             |
| Window                  | Controls the time window shown on the waveform display, in milliseconds. Larger values show more history at reduced resolution.                                                                  | Located in the settings drawer. Range 10–500 ms. Default 200 ms. Persisted as `WaveApplet_TimeWindowMs`.                                           |

### Settings drawer controls

The settings drawer contains the following controls:

- **View** combo box — Selects waveform visualization mode. Options: Scope, Envelope, History, Bands. Persisted as `WaveApplet_ViewMode`.
- **Zoom** slider — Amplitude scaling from 1.0x to 6.0x. Default 1.7x (170%). Persisted as `WaveApplet_ZoomPercent`. Changes are saved immediately to settings.
- **FPS** slider — Refresh rate from 5 to 30 Hz. Default 24 Hz. Persisted as `WaveApplet_RefreshRateHz`. Changes are saved immediately to settings.
- **Window** slider — Time window duration from 10 to 500 ms. Default 200 ms. Persisted as `WaveApplet_TimeWindowMs`.

On initial launch after upgrading from a version using `WaveApplet_TimeWindowSec`, your previous window setting is migrated to the nearest available millisecond value.

Slider styles are now theme-aware — the groove, sub-page, and handle colors adapt to the active theme instead of using the fixed `#203040`/`#00b4d8`/`#c8d8e8` palette. Label colors similarly follow the theme's `color.text.primary` and `color.text.secondary` tokens.

### Settings drawer state

The settings drawer remembers whether it was open or closed when you last closed the applet. If you close the applet with the drawer open, it will be open the next time you open the applet. If you close the applet with the drawer closed, it will remain closed on the next launch. The state is persisted as `WaveApplet_DrawerExpanded`.

## Indicators

- **Direction tint** — The display uses a cool tint for RX and a warm tint for TX so the active audio path is unambiguous without reading the header label.
- **Clipping highlight** — Any pixel column containing samples at or above the clipping threshold is highlighted in red at the top and bottom edges of the plot. A **CLIP N** counter also appears in the header, in bold red, showing the number of clipped samples in the current window.
- **PAUSED badge** — Shown in the footer when the display is frozen on a snapshot. No badge means the display is live.
- **No-audio placeholder** — If no samples have arrived within the last second, or the display buffer is empty, a placeholder message replaces the empty trace. For the RX path, the message reads "no RX audio". For the TX path, the message reads "no TX audio".

## Tips

- The waveform color and line width follow the `DisplayFftFillColor` and `DisplayFftLineWidth` display settings used elsewhere in AetherSDR. Valid line width range is 1.0 to 3.0 px; default is 2.0.
- Grid lines can be suppressed via `DisplayShowGrid`. When enabled, the display draws major and minor grid lines behind the trace.
- Single-click to pause is particularly useful for catching a transient: click immediately after the event, inspect the frozen waveform, then click again to resume.
- Double-click on the display toggles the settings drawer. To clear the waveform buffer, use the WaveformWidget::clear() slot or reconnect to the audio engine.
- The click discrimination interval used for starting the pause toggle timer reads from the Radio Setup click discrimination interval setting. This allows you to adjust the double-click timing across all applets without restarting AetherSDR.

## Related

- [Use the waveform display to monitor TX or RX audio](use-the-waveform-display-to-monitor-tx-or-rx-audio.md)
- [Pause and clear the waveform display](pause-and-clear-the-waveform-display.md)
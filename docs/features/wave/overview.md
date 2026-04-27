# Waveform applet overview

The Waveform applet is an audio oscilloscope that displays the time-domain waveform of the active RX or TX audio path. Use it to spot clipping, dropouts, and audio level problems at a glance without reaching for an external meter.

## How it works

The applet renders a scrolling 100 ms time window of mono audio. The display is continuously fed samples from the audio engine. Each pixel column shows the min/max envelope of the samples that fall within it, with separate peak and RMS envelope traces drawn over the top.

The header line shows the current direction (RX or TX), RMS level in dBFS, and peak level in dBFS. The footer shows the sample rate, window duration, and time per division.

Two separate ring buffers — one for RX and one for TX — run in parallel. The display draws from whichever buffer matches the current transmit state. When you switch from receive to transmit, the tint changes and the display immediately begins drawing from the TX buffer.

To open or close the applet, click the **WAVE** tray button in row 1 of the right sidebar. The applet is on by default and is inserted immediately after the EQ button on first run after upgrading to v0.9.1.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Waveform display | Renders the min/max envelope per pixel column with peak and RMS envelope traces over a fixed 100 ms window. | No persisted setting key. |
| Single-click on display | Toggles between live and paused. While paused, a snapshot of the buffer is held until you click again. | A **PAUSED** badge appears in the footer. Default state is live. |
| Double-click on display | Clears the ring buffer for the active direction (RX or TX) and resets the display to empty. | Does not affect the opposite direction's buffer. |

## Indicators

- **Direction tint** — The display uses a cool tint for RX and a warm tint for TX so the active audio path is unambiguous without reading the header label.
- **Clipping highlight** — Any pixel column containing samples at or above the clipping threshold is highlighted in red at the top and bottom edges of the plot. A **CLIP** count also appears in the header, in bold red, showing the number of clipped samples in the current window.
- **PAUSED badge** — Shown in the footer when the display is frozen on a snapshot. No badge means the display is live.
- **No-audio placeholder** — If no samples have arrived within the last second, or the display buffer is empty, a placeholder message replaces the empty trace.

## Tips

- The waveform color and line width follow the `DisplayFftFillColor` and `DisplayFftLineWidth` display settings used elsewhere in AetherSDR. Valid line width range is 1.0 to 3.0 px; default is 2.0.
- Grid lines can be suppressed via `DisplayShowGrid`. When enabled, the display draws major and minor grid lines behind the trace.
- Single-click to pause is particularly useful for catching a transient: click immediately after the event, inspect the frozen waveform, then click again to resume.
- Double-click only clears the buffer for the currently active direction. The opposite direction's buffer is preserved.

## Related

- [Use the waveform display to monitor TX or RX audio](use-the-waveform-display-to-monitor-tx-or-rx-audio.md)
- [Pause and clear the waveform display](pause-and-clear-the-waveform-display.md)

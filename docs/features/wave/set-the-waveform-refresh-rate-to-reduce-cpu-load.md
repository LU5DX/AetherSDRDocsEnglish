# Waveform Applet Configuration Reference

The Waveform applet provides an audio oscilloscope that shows the time-domain waveform of the active TX or RX audio path. It helps operators spot clipping, dropouts, and audio level issues at a glance.

## Overview

The waveform display renders mono float-32 PCM samples received from the audio engine. The TX direction is tinted differently from RX, making the current side obvious without reading a label. The header readout shows RX/TX, RMS dBFS, and PK dBFS.

## Waveform display interactions

| Interaction | Behavior |
|---|---|
| Single-click on display | Toggles pause. A snapshot of the buffer is frozen until clicked again. Useful for inspecting a transient. A "PAUSED" badge appears in the footer while paused. |
| Double-click on display | Toggles the settings drawer open or closed. Does not clear the buffer — use the WaveformWidget::clear() slot or reconnect to reset. |

The single-click discrimination interval is read from the Radio Setup click discrimination setting. If you adjust this value in Radio Setup, it takes effect immediately without an app restart.

## Waveform display indicators

| Indicator | States | Meaning |
|---|---|---|
| Direction tint | RX (cool tint), TX (warm tint) | Visually disambiguates whether the displayed waveform is the receive monitor or the outgoing transmit path. |
| Clipping highlight | No clipping (normal trace), Clipping (red emphasis, CLIP N label) | Columns containing samples at or above ±0.98 full-scale are highlighted; a 'CLIP N' counter appears in the header. |
| PAUSED badge | Live (no badge), Paused (PAUSED badge in footer) | Indicates the display is showing a frozen snapshot and not the live audio stream. |
| No-audio placeholder | Waveform present, 'no RX audio' / 'no TX audio' message | When no scope samples have arrived within 1 second, a placeholder message is shown instead of an empty trace. |

## Lean mode

The waveform applet supports a lean mode that fully disables the scope when the applet is hidden. In lean mode:

- The applet becomes invisible (`setVisible(false)`).
- The `appendScopeSamples` handler short-circuits immediately, discarding all incoming scope data instead of writing it into the sample buffer.
- The 24 Hz software repaint cycle stops entirely.
- The upstream `AudioEngine::{tx,rx}PostChainScopeReady` signal still fires per audio callback, but the applet skips the appended-and-repainted work.

This reduces CPU usage when the waveform display is not visible, because no waveform rendering work is performed at all. To enable lean mode, call `setActive(false)` on the applet. The default state is active (`m_active{true}`).

Use the `isActive()` method to check whether the applet is currently active.

## Settings drawer

The settings drawer can be toggled open or closed by double-clicking the waveform display. Its expanded state is persisted across sessions using the `WaveApplet_DrawerExpanded` setting. When you close the drawer and restart AetherSDR, it remains closed until you double-click the display to reopen it.

## View mode

1. Double-click the waveform display to open the settings drawer.
2. Locate the View combo box at the top of the drawer.
3. Select one of the following modes:

| Mode | Description |
|---|---|
| Scope | Graph = min/max + RMS lines |
| Envelope | Peak/RMS filled area |
| History | Horizontal level bars |
| Bands | Frequency band bars via Goertzel filter |

The setting is persisted as `WaveApplet_ViewMode` with values 'Graph', 'Envelope', 'History', or 'Bands'.

## Zoom slider

1. Double-click the waveform display to open the settings drawer.
2. Locate the Zoom slider.
3. Drag the slider to adjust the amplitude zoom. The current value is shown to the right of the slider in the format `N.Nx`.

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Zoom | 1.7x (170%) | 1.0x–6.0x (100–600) | `WaveApplet_ZoomPercent` |

Higher values stretch small signals vertically, causing clipping artifacts to appear sooner. The slider uses the primary slider style from the current theme.

## FPS slider

1. Double-click the waveform display to open the settings drawer.
2. Locate the FPS slider.
3. Drag the slider to adjust the refresh rate. The current value is shown to the right of the slider in the format `N fps`.

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| FPS | 24 Hz | 5–30 Hz | `WaveApplet_RefreshRateHz` |

Lower values reduce CPU load on slow systems. The setting has no effect on audio capture or level accuracy. The slider uses the primary slider style from the current theme.

## Window slider

1. Double-click the waveform display to open the settings drawer.
2. Locate the Window slider at the bottom of the drawer.
3. Drag the slider to select a time window for the waveform display.

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Window | 1 s | 240 ms, 480 ms, 1 s, 2 s, 3 s, 4 s, 5 s, 6 s, 7 s, 8 s, 9 s, 10 s | `WaveApplet_TimeWindowMs` |

The slider uses discrete steps. The first three positions are sub-second (240 ms, 480 ms, 1 s), then 1-second increments from 1 to 10 seconds. The current value is shown to the right of the slider. The slider uses the primary slider style from the current theme.

Setting a shorter window allows you to see fine details in the waveform. Setting a longer window shows the overall trend and makes it easier to spot infrequent events.

**Migration note:** If you previously set a time window using the older `WaveApplet_TimeWindowSec` setting, it is automatically converted to the nearest available discrete step on first use. The old key is then removed from settings.

## Tips

- A value of 5–10 fps is sufficient for monitoring average levels and spotting clipping. Use higher values only when you need to track fast transients visually.
- The FPS slider uses a single step of 5 and a page step of 10, so pressing the arrow keys or Page Up/Page Down on the slider moves it in those increments.
- The zoom, FPS, and window settings are independent — changing one does not affect the others.
- Use the pause feature (single-click the display) to freeze the waveform for close inspection of a transient or anomaly.
- When the waveform applet is hidden, it enters lean mode and stops all waveform rendering work, reducing CPU usage.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
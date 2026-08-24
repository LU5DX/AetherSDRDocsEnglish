# Waveform Applet Configuration Reference

The Waveform applet provides an audio oscilloscope that shows the time-domain waveform of the active TX or RX audio path in one of four view modes (Scope, Envelope, History bars, Bands spectrum). It helps operators spot clipping, dropouts, and audio level issues at a glance. The TX path is tinted differently from RX so the current direction is unambiguous.

## Overview

The waveform display renders mono float-32 PCM samples received from the audio engine. The TX direction is tinted differently from RX, making the current side obvious without reading a label. The header readout shows RX/TX, RMS dBFS, and PK dBFS.

Waveform rendering uses QPainter with incremental reduction via WaveformScopeModel: repaints merge pre-folded bins instead of rescanning the raw window, so paint cost no longer scales with the time window.

## Waveform display interactions

| Interaction | Behavior | Notes |
|---|---|---|
| Single-click on display | Toggles pause. A snapshot of the buffer is frozen until clicked again. Useful for inspecting a transient. A "PAUSED" badge appears in the footer while paused. | The single-click discrimination interval is read from the Radio Setup click discrimination setting. If you adjust this value in Radio Setup, it takes effect immediately without an app restart. |
| Double-click on display | Toggles the settings drawer open or closed. Does not clear the buffer — use the WaveformWidget::clear() slot or reconnect to reset. | |

## Waveform display indicators

| Indicator | States | Meaning |
|---|---|---|
| Direction tint | RX (cool tint), TX (warm tint) | Visually disambiguates whether the displayed waveform is the receive monitor or the outgoing transmit path. |
| Clipping highlight | No clipping (normal trace), Clipping (red emphasis, CLIP N label) | Columns containing samples at or above ±0.98 full-scale are highlighted; a 'CLIP N' counter appears in the header. |
| PAUSED badge | Live (no badge), Paused (PAUSED badge in footer) | Indicates the display is showing a frozen snapshot and not the live audio stream. |
| No-audio placeholder | Waveform present, 'no RX audio' / 'no TX audio' message | When no scope samples have arrived within 1 second, a placeholder message is shown instead of an empty trace. |

## Settings drawer

The settings drawer can be toggled open or closed by double-clicking the waveform display. Its expanded state is persisted across sessions using the `WaveApplet_DrawerExpanded` setting. When you close the drawer and restart AetherSDR, it remains closed until you double-click the display to reopen it.

## View mode

1. Double-click the waveform display to open the settings drawer.
2. Locate the View combo box at the top of the drawer. The combo box has object name `waveViewCombo` and accessible name "WAVE view mode".
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
2. Locate the Zoom slider. The slider has object name `waveZoomSlider` and accessible name "WAVE zoom".
3. Drag the slider to adjust the amplitude zoom. The current value is shown to the right of the slider in the format `N.Nx`.

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Zoom | 1.7x (170%) | 1.0x–6.0x (100–600) | `WaveApplet_ZoomPercent` |

Higher values stretch small signals vertically, causing clipping artifacts to appear sooner. The slider uses the primary slider style from the current theme.

## FPS slider

1. Double-click the waveform display to open the settings drawer.
2. Locate the FPS slider. The slider has object name `waveFpsSlider` and accessible name "WAVE FPS".
3. Drag the slider to adjust the refresh rate. The current value is shown to the right of the slider in the format `N fps`.

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| FPS | 24 Hz | 5–30 Hz | `WaveApplet_RefreshRateHz` |

Lower values reduce CPU load on slow systems. The default of 24 fps provides a smooth scope response with a moderate load on the CPU. Users who previously saved an explicit FPS value keep their existing setting — the default is only applied when the setting key is absent.

The setting has no effect on audio capture or level accuracy. The slider uses the primary slider style from the current theme.

## Window slider

1. Double-click the waveform display to open the settings drawer.
2. Locate the Window slider at the bottom of the drawer. The slider has object name `waveWindowSlider` and accessible name "WAVE window".
3. Drag the slider to select a time window for the waveform display.

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Window | 200 ms | 10–500 ms | `WaveApplet_TimeWindowMs` |

The slider uses discrete steps from the window steps array. The current value is shown to the right of the slider. The slider uses the primary slider style from the current theme.

Setting a shorter window allows you to see fine details in the waveform. Setting a longer window shows more history at reduced resolution.

**Migration note:** If you previously set a time window using the older `WaveApplet_TimeWindowSec` setting, it is automatically converted to the nearest available discrete step on first use. The old key is then removed from settings.

## Tips

- A value of 5–10 fps is sufficient for monitoring average levels and spotting clipping. Use higher values only when you need to track fast transients visually.
- The FPS slider uses a single step of 5 and a page step of 10, so pressing the arrow keys or Page Up/Page Down on the slider moves it in those increments.
- The zoom, FPS, and window settings are independent — changing one does not affect the others.
- Use the pause feature (single-click the display) to freeze the waveform for close inspection of a transient or anomaly.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
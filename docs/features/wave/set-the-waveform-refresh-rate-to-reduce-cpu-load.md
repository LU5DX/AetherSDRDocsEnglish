# Set the waveform refresh rate to reduce CPU load

The Waveform applet repaints at up to 30 frames per second by default. On slower systems, lowering the frame rate reduces CPU usage with no effect on the audio data being monitored.

## Before you start

- The WAVE applet must be visible in the applet panel. If it is not, click the WAVE tray button in the right sidebar to show it.
- The settings drawer must be open. If you see only the waveform display, double-click the display to open the drawer.

## Steps

1. Double-click the waveform display to open the settings drawer.
2. Locate the FPS row at the bottom of the drawer.
3. Drag the FPS slider left to decrease the frame rate or right to increase it. The current value is shown to the right of the slider in the format `N fps`.
4. Release the slider. The new rate takes effect immediately and is saved automatically to `WaveApplet_RefreshRateHz`.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| FPS | 24 Hz | 5–30 Hz | `WaveApplet_RefreshRateHz` |

Lower values reduce how often the waveform repaints. Higher values give smoother motion. The setting has no effect on audio capture or level accuracy.

## Tips

- A value of 5–10 fps is sufficient for monitoring average levels and spotting clipping. Use higher values only when you need to track fast transients visually.
- The FPS slider uses a single step of 5 and a page step of 10, so pressing the arrow keys or Page Up/Page Down on the slider moves it in those increments.
- Reducing FPS does not affect the other settings in the drawer. View mode (`WaveApplet_ViewMode`) and zoom (`WaveApplet_ZoomPercent`) remain independent.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)

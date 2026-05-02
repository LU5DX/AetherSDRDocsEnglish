# Adjust waveform amplitude zoom

The Zoom slider in the Waveform applet scales the amplitude axis of the waveform display. Increasing zoom stretches small signals vertically so they are easier to read; decreasing it prevents clipping artifacts from obscuring the trace on loud signals.

## Before you start

- The Waveform applet must be visible. If it is not, click the WAVE tray button in the right sidebar to show it.
- The settings drawer must be open. If only the waveform trace is visible with no controls below it, double-click the waveform display to open the drawer.

## Steps

1. Double-click the waveform display to open the settings drawer if it is not already open.
2. Locate the Zoom row in the settings drawer.
3. Drag the Zoom slider left to decrease zoom or right to increase zoom. The readout to the right of the slider updates immediately, showing the current value as a multiplier (for example, `1.7x`).
4. Release the slider. The new value is saved automatically to `WaveApplet_ZoomPercent`.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Zoom | 170 (1.7x) | 100–600 (displayed as 1.0x–6.0x) | `WaveApplet_ZoomPercent` |

The slider value is an integer percentage. The waveform display divides it by 100 to produce the multiplier shown in the readout. A value of 100 means no zoom (1.0x); 600 is maximum zoom (6.0x).

## Tips

- At high zoom levels, signals near full scale will produce clipping highlights (red column emphasis and a CLIP N counter in the header). If you see frequent clipping indicators after raising zoom, reduce the value until the trace fits within the display without hitting the edges.
- The zoom setting applies equally to RX and TX paths. The direction tint (cool for RX, warm for TX) still distinguishes which path is active regardless of zoom level.
- To inspect a transient at a higher zoom without missing it in real time, pause the display first by single-clicking the waveform, then adjust zoom while the snapshot is frozen.

## Troubleshooting

- **The settings drawer is not visible** — Double-click the waveform display to toggle it open. The drawer is below the waveform trace.
- **The Zoom slider snaps back after dragging** — This can happen if no audio is arriving and the display is showing the no-audio placeholder. The slider value is still saved; it takes effect as soon as audio resumes.
- **Zoom resets after restarting AetherSDR** — Verify the value is being persisted. If the application closed abnormally, the `WaveApplet_ZoomPercent` setting may not have been written. Set the slider to the desired value after a clean launch.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Pause the waveform to inspect a transient](pause-the-waveform-to-inspect-a-transient.md)
- [Switch the waveform view mode (Scope, Envelope, History, Bands)](switch-the-waveform-view-mode-scope-envelope-history-bands.md)
- [Set the waveform refresh rate to reduce CPU load](set-the-waveform-refresh-rate-to-reduce-cpu-load.md)

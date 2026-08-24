# Adjust waveform amplitude zoom and time window

The Zoom slider in the Waveform applet scales the amplitude axis of the waveform display. Increasing zoom stretches small signals vertically so they are easier to read; decreasing it prevents clipping artifacts from obscuring the trace on loud signals. The Window slider controls the time window shown in the waveform display.

## Before you start

- The Waveform applet must be visible. If it is not, click the WAVE tray button in the right sidebar to show it.
- The settings drawer must be open. If only the waveform trace is visible with no controls below it, double-click the waveform display to open the drawer. The drawer state is persisted across sessions.

## Steps

1. Double-click the waveform display to open the settings drawer if it is not already open.
2. Locate the Zoom row or the Window row in the settings drawer.
3. Adjust the desired slider:
   - Drag the **Zoom** slider left to decrease zoom or right to increase zoom. The readout to the right of the slider updates immediately, showing the current value as a multiplier (for example, `1.7x`).
   - Drag the **Window** slider left to decrease the time window or right to increase it. The readout to the right of the slider updates immediately, showing the current value in milliseconds (for example, `200 ms`).
4. Release the slider. The new value is saved automatically to `WaveApplet_ZoomPercent` or `WaveApplet_TimeWindowMs`. The drawer expanded/collapsed state is also saved automatically to `WaveApplet_DrawerExpanded`.

## What each control does

| Control | Default    | Valid range     |
|---------|------------|-----------------|
| Zoom    | 170 (1.7x) | 100–600 (displayed as 1.0x–6.0x) |
| Window  | 200 ms     | 10–500 ms (continuous)           |

The Zoom slider value is an integer percentage. The waveform display divides it by 100 to produce the multiplier shown in the readout. A value of 100 means no zoom (1.0x); 600 is maximum zoom (6.0x).

The Window slider is a continuous range from 10 ms to 500 ms, giving you full control over the time window. Smaller values (around 10–50 ms) provide fine detail in fast waveforms; larger values (up to 500 ms) show more history at reduced resolution.

## The settings drawer state

The settings drawer (which contains the View, Zoom, Window, and FPS controls) remembers whether it was open or closed when you last used the applet. When you reopen the Waveform applet, the drawer restores to its previous state. If you always want the drawer open, leave it open before closing the applet or restarting AetherSDR.

## Tips

- At high zoom levels, signals near full scale will produce clipping highlights (red column emphasis and a CLIP N counter in the header). If you see frequent clipping indicators after raising zoom, reduce the value until the trace fits within the display without hitting the edges.
- The zoom and window settings apply equally to RX and TX paths. The direction tint (cool for RX, warm for TX) still distinguishes which path is active regardless of zoom level.
- To inspect a transient at higher zoom without missing it in real time, pause the display first by single-clicking the waveform, then adjust zoom while the snapshot is frozen.
- Use a shorter window (around 50 ms) to see fine details in fast waveforms. Use a longer window (up to 500 ms) to see overall level changes over time.
- The click discrimination interval used to distinguish single-click from double-click respects the value you set in Radio Setup → Interaction Settings. Changes to that setting take effect immediately without restarting AetherSDR.

## Troubleshooting

- **The settings drawer is not visible** — Double-click the waveform display to toggle it open. The drawer is below the waveform trace.
- **The Zoom slider snaps back after dragging** — This can happen if no audio is arriving and the display is showing the no-audio placeholder. The slider value is still saved; it takes effect as soon as audio resumes.
- **Zoom resets after restarting AetherSDR** — Verify the value is being persisted. If the application closed abnormally, the `WaveApplet_ZoomPercent` setting may not have been written. Set the slider to the desired value after a clean launch.
- **Window setting changed unexpectedly after update** — If upgrading from a previous version that used the `WaveApplet_TimeWindowSec` setting (1–20 s linear), the value is automatically migrated to the nearest value in `WaveApplet_TimeWindowMs`. Verify the setting and adjust if needed.
- **The no-audio placeholder message changed** — When no RX audio is arriving, the display now shows "Enable PC Audio" instead of "no RX audio". This indicates you need to enable PC audio in the radio settings or audio configuration. For TX, the message still shows "no TX audio".

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Pause the waveform to inspect a transient](pause-the-waveform-to-inspect-a-transient.md)
- [Switch the waveform view mode (Scope, Envelope, History, Bands)](switch-the-waveform-view-mode-scope-envelope-history-bands.md)
- [Set the waveform refresh rate to reduce CPU load](set-the-waveform-refresh-rate-to-reduce-cpu-load.md)
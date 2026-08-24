# Switch the waveform view mode (Scope, Envelope, History, Bands)

The Waveform applet offers four visualization modes for the active audio path. Switching modes lets you choose the representation that best suits your monitoring task — for example, Bands to spot frequency imbalance in a TX signal, or Scope for a traditional time-domain trace.

## Before you start

- The WAVE applet must be visible in the applet panel. If it is not, click the WAVE tray button in the right sidebar to show it.
- The settings drawer must be open. If you see only the waveform display with no controls beneath it, double-click the waveform display to open the drawer.

## Steps

1. Double-click the waveform display to open the settings drawer if it is not already open.
2. In the settings drawer, locate the **View:** label on the first row.
3. Click the combo box to the right of **View:**. The combo box has an accessible name of "WAVE view mode".
4. Select one of the four options: **Scope**, **Envelope**, **History**, or **Bands**.

The display updates immediately. The selection is saved to `WaveApplet_ViewMode` and restored on the next launch.

## What each control does

| Control             | Default | Valid values                                                                                                          |
|---------------------|---------|-----------------------------------------------------------------------------------------------------------------------|
| **View:** combo box | Scope   | Scope, Envelope, History, Bands                                                                                       |
| **Window:** slider  | 200 ms  | 10–500 ms                                                                                                             |
| **Zoom:** slider    | 1.7x    | 1.0x – 6.0x (100–600)                                                                                                 |
| **FPS:** slider     | 24 fps  | 5–30 Hz                                                                                                               |

## Settings drawer controls

All controls are located in the collapsible settings drawer below the waveform display. Each control has an accessible name for screen reader compatibility:

| Control                 | Accessible name    | Setting key                          | Behavior                                                         |
|-------------------------|--------------------|--------------------------------------|------------------------------------------------------------------|
| **View:** combo box     | WAVE view mode     | `WaveApplet_ViewMode`                | Persisted as 'Graph', 'Envelope', 'History', or 'Bands'          |
| **Zoom:** slider        | WAVE zoom          | `WaveApplet_ZoomPercent`             | Scales amplitude axis; default 170 (1.7x)                        |
| **FPS:** slider         | WAVE FPS           | `WaveApplet_RefreshRateHz`           | Controls repaint rate; default 24 fps, range 5–30 Hz             |
| **Window:** slider      | WAVE window        | `WaveApplet_TimeWindowMs`            | Time window shown; default 200 ms, range 10–500 ms               |

**Note:** The legacy `WaveApplet_TimeWindowSec` key is migrated to `WaveApplet_TimeWindowMs` on first run. The drawer collapsed state is persisted across application restarts using `WaveApplet_DrawerExpanded`.

## Tips

- **Bands** mode uses a Goertzel filter to derive frequency band bars. It is useful for checking whether TX audio energy is distributed across the expected frequency range.
- **History** mode displays horizontal level bars accumulated over time, which makes it easier to see sustained level trends than a momentary trace.
- If the display shows a **"no RX audio"** or **"no TX audio"** message, no scope samples have arrived within the last second. For the RX path, enable PC Audio in the radio settings. For the TX path, verify that the microphone or line input is active. The view mode setting is still applied and will take effect as soon as audio resumes.
- Single-clicking the waveform display toggles pause. If the display appears frozen, click it once to resume live updates. A **PAUSED** badge in the footer confirms the paused state.
- The settings drawer state (open or closed) is persisted. If you close the drawer and restart AetherSDR, it stays closed. Double-click the waveform to reopen it.
- The TX audio path is tinted with a warm color and the RX path with a cool color, so you can identify the active direction at a glance without reading a label. The header readout shows RX/TX, RMS dBFS, and PK dBFS.
- When clipping occurs (samples at or above ±0.98 full-scale), the affected columns are highlighted in red and a **CLIP N** counter appears in the header.

## Troubleshooting

- **The View: combo box is not visible** — The settings drawer is closed. Double-click the waveform display to toggle it open.
- **The selected mode does not persist after restart** — Confirm AetherSDR has write access to its settings storage. If the issue repeats, check that no other AetherSDR instance is running simultaneously and overwriting `WaveApplet_ViewMode` on exit.
- **The display shows a placeholder message instead of a waveform** — No scope samples have arrived within the last second. Verify the audio source is active. For the RX path, ensure PC Audio is enabled in the radio settings. For the TX path, confirm the microphone or line input is active.
- **The waveform display appears frozen** — The display may be paused. Single-click the waveform to resume live updates. A **PAUSED** badge in the footer confirms the paused state.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
- [Pause the waveform to inspect a transient](pause-the-waveform-to-inspect-a-transient.md)
- [Set the waveform refresh rate to reduce CPU load](set-the-waveform-refresh-rate-to-reduce-cpu-load.md)
- Set the waveform time window
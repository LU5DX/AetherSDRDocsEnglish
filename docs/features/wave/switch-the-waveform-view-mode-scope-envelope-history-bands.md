# Switch the waveform view mode (Scope, Envelope, History, Bands)

The Waveform applet offers four visualization modes for the active audio path. Switching modes lets you choose the representation that best suits your monitoring task — for example, Bands to spot frequency imbalance in a TX signal, or Scope for a traditional time-domain trace.

## Before you start

- The WAVE applet must be visible in the applet panel. If it is not, click the WAVE tray button in the right sidebar to show it.
- The settings drawer must be open. If you see only the waveform display with no controls beneath it, double-click the waveform display to open the drawer.

## Steps

1. Double-click the waveform display to open the settings drawer if it is not already open.
2. In the settings drawer, locate the **View:** label on the first row.
3. Click the combo box to the right of **View:**.
4. Select one of the four options: **Scope**, **Envelope**, **History**, or **Bands**.

The display updates immediately. The selection is saved to `WaveApplet_ViewMode` and restored on the next launch.

## What each control does

| Control | Default | Valid values | Persisted key | Behavior |
|---------|---------|--------------|---------------|----------|
| **View:** combo box | Scope | Scope, Envelope, History, Bands | `WaveApplet_ViewMode` | Selects the visualization mode. Scope shows min/max and RMS lines. Envelope shows a peak/RMS filled area. History shows horizontal level bars. Bands shows frequency band bars. |
| **Zoom:** slider | 1.7x | 1.0x – 6.0x (100–600) | `WaveApplet_ZoomPercent` | Scales the amplitude axis. Higher values stretch small signals vertically. |
| **FPS:** slider | 24 fps | 5–30 Hz | `WaveApplet_RefreshRateHz` | Controls repaint frequency. Lower values reduce CPU load. |

## Tips

- **Bands** mode uses a Goertzel filter to derive frequency band bars. It is useful for checking whether TX audio energy is distributed across the expected frequency range.
- **History** mode displays horizontal level bars accumulated over time, which makes it easier to see sustained level trends than a momentary trace.
- If the display shows a "no RX audio" or "no TX audio" message, no scope samples have arrived within the last second. The view mode setting is still applied and will take effect as soon as audio resumes.
- Single-clicking the waveform display toggles pause. If the display appears frozen, click it once to resume live updates. A **PAUSED** badge in the footer confirms the paused state.

## Troubleshooting

- **The View: combo box is not visible** — The settings drawer is closed. Double-click the waveform display to toggle it open.
- **The selected mode does not persist after restart** — Confirm AetherSDR has write access to its settings storage. If the issue repeats, check that no other AetherSDR instance is running simultaneously and overwriting `WaveApplet_ViewMode` on exit.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
- [Pause the waveform to inspect a transient](pause-the-waveform-to-inspect-a-transient.md)
- [Set the waveform refresh rate to reduce CPU load](set-the-waveform-refresh-rate-to-reduce-cpu-load.md)

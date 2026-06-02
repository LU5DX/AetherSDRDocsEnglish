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
| **Window:** slider | 1 s | Discrete steps: 240 ms, 480 ms, 1 s, then 1-second increments to 10 s | `WaveApplet_TimeWindowMs` | Sets the time window displayed on the waveform. Shorter windows (240 ms, 480 ms) provide detail on fast transients; longer windows (up to 10 s) give a broader view of audio dynamics. |
| **Zoom:** slider | 1.7x | 1.0x – 6.0x (100–600) | `WaveApplet_ZoomPercent` | Scales the amplitude axis. Higher values stretch small signals vertically. |
| **FPS:** slider | 24 fps | 5–30 Hz | `WaveApplet_RefreshRateHz` | Controls repaint frequency. Lower values reduce CPU load. |

## Tips

- **Bands** mode uses a Goertzel filter to derive frequency band bars. It is useful for checking whether TX audio energy is distributed across the expected frequency range.
- **History** mode displays horizontal level bars accumulated over time, which makes it easier to see sustained level trends than a momentary trace.
- If the display shows a **"Enable PC Audio"** message (for the RX path) or a **"no TX audio"** message, no scope samples have arrived within the last second. For the RX path, enable PC Audio in the radio settings. For the TX path, verify that the microphone or line input is active. The view mode setting is still applied and will take effect as soon as audio resumes.
- Single-clicking the waveform display toggles pause. If the display appears frozen, click it once to resume live updates. A **PAUSED** badge in the footer confirms the paused state.
- The settings drawer state (open or closed) is persisted. If you close the drawer and restart AetherSDR, it stays closed. Double-click the waveform to reopen it.
- The **Window:** slider uses discrete steps with deliberate stops, not a continuous range. Each notch on the slider corresponds to one of the available time windows: 240 ms, 480 ms, 1 s, 2 s, 3 s, 4 s, 5 s, 6 s, 7 s, 8 s, 9 s, 10 s. Slider appearance adapts to the active theme.
- The **Zoom:** and **FPS:** sliders use theme-aware styling. Their handle and track colors match the current theme selection to provide consistent visual feedback across light and dark themes.

## Troubleshooting

- **The View: combo box is not visible** — The settings drawer is closed. Double-click the waveform display to toggle it open.
- **The selected mode does not persist after restart** — Confirm AetherSDR has write access to its settings storage. If the issue repeats, check that no other AetherSDR instance is running simultaneously and overwriting `WaveApplet_ViewMode` on exit.
- **The Window: slider seems to have limited positions** — This is by design. The slider provides 12 discrete time window steps rather than a continuous range, so you can quickly select a standard window length without fine-tuning.
- **The display shows "Enable PC Audio" instead of "no RX audio"** — This message indicates that PC Audio must be enabled in the radio settings for the RX path. Navigate to Radio > Audio and enable PC Audio.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
- [Pause the waveform to inspect a transient](pause-the-waveform-to-inspect-a-transient.md)
- [Set the waveform refresh rate to reduce CPU load](set-the-waveform-refresh-rate-to-reduce-cpu-load.md)
- Set the waveform time window
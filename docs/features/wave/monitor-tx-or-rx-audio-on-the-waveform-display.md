# Monitor TX or RX audio on the waveform display

The Waveform applet displays a live time-domain view of the active TX or RX audio path. Use it to spot clipping, dropouts, and audio level problems without leaving the main window.

## Before you start

- AetherSDR must be running. A radio connection is not required — the applet displays audio from the local audio engine.
- The applet panel must be visible. If it is hidden, enable it via `View > Applet Panel`.

## Steps

1. Locate the WAVE tray button in the right sidebar's top row of tray buttons.
2. Click WAVE to show the Waveform applet. Click it again to hide it.
3. Watch the waveform display. The trace is tinted cool when monitoring RX audio and warm when monitoring TX audio — no label reading required.
4. Check the header readout for the current direction (RX or TX), RMS level in dBFS, and peak level in dBFS.
5. If no audio has arrived within one second, the display shows a placeholder message instead of an empty trace. For the RX path, the message reads **"no RX audio"**. For the TX path, it reads **"no TX audio"**.
6. To open the settings drawer, double-click anywhere on the waveform display. Double-click again to close it. The drawer's open/closed state is remembered across app restarts.
7. In the settings drawer, use the View combo box to choose a visualization: **Scope**, **Envelope**, **History**, or **Bands**. The default is **Scope**.
8. Use the Zoom slider to scale the amplitude axis. The default is 1.7x (range 1.0x–6.0x). Drag right to stretch small signals; at high zoom values, clipping artifacts appear sooner.
9. Use the FPS slider to set how often the display repaints (range 5–30 Hz, default 24). Lower values reduce CPU load.
10. Use the Window slider to set the time window displayed. Slider stops at discrete steps: 240 ms, 480 ms, 1 s, then 1-second increments to 10 s. The default is 1 s.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| View | Scope | Scope, Envelope, History, Bands | `WaveApplet_ViewMode` | Selects the visualization mode. Scope shows min/max waveform and RMS lines. Envelope shows a peak/RMS filled area. History shows horizontal level bars. Bands shows frequency band bars. |
| Zoom | 1.7x (170) | 1.0x–6.0x (100–600) | `WaveApplet_ZoomPercent` | Scales the amplitude axis vertically. |
| FPS | 24 | 5–30 Hz | `WaveApplet_RefreshRateHz` | Controls repaint frequency. |
| Window | 1 s | 240 ms, 480 ms, 1 s, 2 s, 3 s, 4 s, 5 s, 6 s, 7 s, 8 s, 9 s, 10 s | `WaveApplet_TimeWindowMs` | Sets the time window displayed in discrete stepped intervals. |
| Click on display | Live | Live / Paused | — | Toggles pause. A PAUSED badge appears in the footer while the display is frozen. The click discrimination interval respects the value set in `Radio Setup > Audio > Click Discrimination Interval (ms)`. |
| Double-click on display | — | — | — | Toggles the settings drawer open or closed. |
| Settings drawer | Expanded | Expanded / Collapsed | `WaveApplet_DrawerExpanded` | Remembers the drawer's open/closed state across app restarts. |

## Tips

- When clipping occurs, affected columns are highlighted and a CLIP N counter appears in the header. Reduce your audio drive level or lower the Zoom value to bring the signal back within range.
- Click once on the waveform to freeze a snapshot when you notice a transient. Click again to resume the live view.
- The settings drawer remembers whether it was open or closed when you last used it, and restores that state on next launch.
- The click discrimination interval used for single-click versus double-click detection is read from the Radio Setup at click time, so changes to `Settings > Radio Setup... > Audio > Click Discrimination Interval (ms)` take effect without restarting AetherSDR.
- The Window slider uses discrete steps rather than continuous adjustment. Each notch provides a specific time window value. The first three steps (240 ms, 480 ms, 1 s) give sub-second detail; the remaining steps increase in 1-second increments up to 10 s.

## Troubleshooting

- **The display shows "no RX audio"** — No RX scope samples have arrived in the last second. Ensure that PC Audio is enabled in the radio's audio configuration. Verify the correct audio device is selected in `Settings > Radio Setup...`.
- **The display shows "no TX audio"** — No TX scope samples have arrived in the last second. Verify that audio is flowing through the transmit path.
- **The WAVE tray button is missing** — The applet panel may be hidden. Enable it via `View > Applet Panel`. If the panel is visible but WAVE is absent, use `View > Reset Applet Order` to restore the default applet layout.
- **Single-click and double-click are not reliably distinguished** — Adjust the click discrimination interval in `Settings > Radio Setup... > Audio > Click Discrimination Interval (ms)`. A longer interval makes single-clicks easier, a shorter interval makes double-clicks easier.

## Related

- [Waveform overview](overview.md)
- [Pause the waveform to inspect a transient](pause-the-waveform-to-inspect-a-transient.md)
- [Switch the waveform view mode (Scope, Envelope, History, Bands)](switch-the-waveform-view-mode-scope-envelope-history-bands.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
- [Set the waveform refresh rate to reduce CPU load](set-the-waveform-refresh-rate-to-reduce-cpu-load.md)
- Adjust the waveform time window
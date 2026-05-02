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
5. If no audio has arrived within one second, the display shows a "no RX audio" or "no TX audio" placeholder instead of an empty trace.
6. To open the settings drawer, double-click anywhere on the waveform display. Double-click again to close it.
7. In the settings drawer, use the View combo box to choose a visualization: **Scope**, **Envelope**, **History**, or **Bands**. The default is **Scope**.
8. Use the Zoom slider to scale the amplitude axis. The default is 1.7x (range 1.0x–6.0x). Drag right to stretch small signals; at high zoom values, clipping artifacts appear sooner.
9. Use the FPS slider to set how often the display repaints (range 5–30 Hz, default 24). Lower values reduce CPU load.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| View | Scope | Scope, Envelope, History, Bands | `WaveApplet_ViewMode` | Selects the visualization mode. Scope shows min/max waveform and RMS lines. Envelope shows a peak/RMS filled area. History shows horizontal level bars. Bands shows frequency band bars. |
| Zoom | 1.7x (170) | 1.0x–6.0x (100–600) | `WaveApplet_ZoomPercent` | Scales the amplitude axis vertically. |
| FPS | 24 | 5–30 Hz | `WaveApplet_RefreshRateHz` | Controls repaint frequency. |
| Click on display | Live | Live / Paused | — | Toggles pause. A PAUSED badge appears in the footer while the display is frozen. |
| Double-click on display | — | — | — | Toggles the settings drawer open or closed. |

## Tips

- When clipping occurs, affected columns are highlighted and a CLIP N counter appears in the header. Reduce your audio drive level or lower the Zoom value to bring the signal back within range.
- Click once on the waveform to freeze a snapshot when you notice a transient. Click again to resume the live view.
- The settings drawer opens in the expanded state each time you launch AetherSDR.

## Troubleshooting

- **The display shows "no RX audio" or "no TX audio"** — No scope samples have arrived in the last second. Verify that audio is flowing through the relevant path and that the correct audio device is selected in `Settings > Radio Setup...`.
- **The WAVE tray button is missing** — The applet panel may be hidden. Enable it via `View > Applet Panel`. If the panel is visible but WAVE is absent, use `View > Reset Applet Order` to restore the default applet layout.

## Related

- [Waveform overview](overview.md)
- [Pause the waveform to inspect a transient](pause-the-waveform-to-inspect-a-transient.md)
- [Switch the waveform view mode (Scope, Envelope, History, Bands)](switch-the-waveform-view-mode-scope-envelope-history-bands.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
- [Set the waveform refresh rate to reduce CPU load](set-the-waveform-refresh-rate-to-reduce-cpu-load.md)

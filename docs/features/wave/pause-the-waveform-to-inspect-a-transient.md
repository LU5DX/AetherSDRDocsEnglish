# Pause the waveform to inspect a transient

Single-clicking the waveform display freezes a snapshot of the current audio buffer so you can examine a transient, clipping event, or dropout without the trace continuing to scroll.

## Before you start

- The Waveform applet must be visible. If it is not, click the WAVE tray button in the right sidebar to open it.
- Audio must be flowing (RX or TX) so there is something worth freezing. If no samples have arrived within 1 second, the display shows a placeholder message instead of a trace.
  - For RX audio, the placeholder reads "no RX audio".
  - For TX audio, the placeholder reads "no TX audio".

## Steps

1. Watch the waveform display for the transient you want to examine.
2. Single-click anywhere on the waveform display at the moment the event appears.
3. Confirm the display is frozen: a **PAUSED** badge appears in the footer of the waveform display.
4. Examine the frozen trace. The header continues to show the RX/TX direction, RMS dBFS, and PK dBFS values that were captured at the moment of the click.
5. Single-click the waveform display again to resume live updates. The **PAUSED** badge disappears.

## What each control does

| Control | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|
| Click on display | Toggles pause: freezes a buffer snapshot on first click; resumes live display on second click. The click discrimination interval is read from Radio Setup at click time, so changes to that setting take effect immediately without restarting the application. | Live | Live / Paused | — |
| View | Selects the visualization mode shown while paused. | Scope | Scope, Envelope, History, Bands | `WaveApplet_ViewMode` |
| Zoom | Scales the amplitude axis. Higher values stretch small signals vertically, making subtle transients easier to see while paused. | 1.7x (170) | 100–600 (1.0x–6.0x) | `WaveApplet_ZoomPercent` |
| FPS | Controls repaint rate while live. Has no effect while paused. | 24 | 5–30 Hz | `WaveApplet_RefreshRateHz` |
| Settings drawer state | Persists the expanded/collapsed state of the settings drawer across application restarts. Toggle by double-clicking the waveform display or opening/closing the drawer manually. | Expanded (True) | Expanded / Collapsed | `WaveApplet_DrawerExpanded` |

## Tips

- The click is disambiguated from a double-click by a short interval. If the display does not freeze on your first click, click once and wait rather than clicking rapidly.
- The click discrimination interval is read from the **Radio Setup** dialog at the moment you click. If you adjust that setting, it applies immediately without restarting AetherSDR.
- Double-clicking opens or closes the settings drawer instead of pausing. If you accidentally open the drawer, double-click again to close it, then single-click to pause.
- Increasing Zoom before pausing can make low-level transients more visible in the frozen frame.
- The TX path is tinted differently from the RX path, so you can confirm which audio direction the frozen snapshot represents without reading the header.
- If no RX audio samples have arrived within 1 second, the placeholder message reads "no RX audio". For TX audio, the placeholder reads "no TX audio".
- The settings drawer state (expanded or collapsed) is saved when you close it and restored the next time you open the Waveform applet.

## Troubleshooting

- **Click does not pause the display** — Make sure you are clicking once on the waveform area itself, not on the settings drawer below it. A rapid second click will immediately resume the display; click once and pause before clicking again.
- **PAUSED badge appears but the trace is blank** — The buffer was empty at the moment you clicked. This happens when no audio has arrived within the last second. Resume live mode, wait for audio to appear, then click again.
- **Display resumes on its own** — Pausing only freezes the visual display; a reconnect or audio engine reset clears the buffer and restores the live view.
- **Placeholder message shows "no RX audio"** — This indicates no RX audio samples have been received. Enable PC Audio in the radio settings to receive audio from the radio.
- **Settings drawer does not remember its state** — The drawer state is saved when you close it. If AetherSDR crashes before the save completes, the state may revert to expanded on next launch.
- **Waveform applet is hidden and does not respond** — The applet may be in lean mode, which fully disables the scope. Click the WAVE tray button to show the applet and enable it. In lean mode, the scope feed is dropped and the applet is hidden to conserve resources.

## Related

- [Waveform overview](overview.md)
- [Monitor TX or RX audio on the waveform display](monitor-tx-or-rx-audio-on-the-waveform-display.md)
- [Adjust waveform amplitude zoom](adjust-waveform-amplitude-zoom.md)
- [Switch the waveform view mode (Scope, Envelope, History, Bands)](switch-the-waveform-view-mode-scope-envelope-history-bands.md)
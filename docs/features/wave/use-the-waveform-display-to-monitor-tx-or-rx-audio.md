# Use the waveform display to monitor TX or RX audio

The Waveform applet shows a time-domain oscilloscope view of the active TX or RX audio path. Use it to spot clipping, dropouts, and audio level problems at a glance without interrupting operation.

## Before you start

- The Waveform applet must be visible. If it is not, click the WAVE tray button in the right sidebar to show it.
- Audio must be flowing through AetherSDR (transmitting or receiving) for the display to show a trace.

## Steps

1. Locate the Waveform applet in the right sidebar applet panel. It appears by default after the EQ button.
2. Observe the direction tint: a cool tint means the display is showing RX audio; a warm tint means TX audio. The direction also appears in the header readout (for example, `RX  RMS -24.3 dBFS  PK -18.1 dBFS`).
3. Watch the trace for clipping. Pixel columns containing clipped samples are highlighted in red, and a `CLIP` counter appears in the top-right corner of the display.
4. Check the header readout for RMS and peak levels in dBFS.
5. Check the footer for the current sample rate, the 100 ms time window, and the milliseconds-per-division scale.
6. If no audio has arrived recently, the display shows a "No audio" placeholder instead of a trace.

## What each control does

| Control | Behavior | Default | Notes |
|---|---|---|---|
| Waveform display | Renders the min/max envelope per pixel column with peak and RMS envelope curves. Time window is fixed at 100 ms. | Live | Shows RX or TX depending on the active direction. |
| Click on display | Toggles pause. The display freezes on a snapshot of the buffer until clicked again. | Live | A `PAUSED` badge appears in the footer while paused. |
| Double-click on display | Clears the ring buffer for the active direction (RX or TX). Resets the display to empty. | — | Does not affect the other direction's buffer. |
| Direction tint | Cool tint = RX audio. Warm tint = TX audio. | — | Changes automatically when the radio switches between transmit and receive. |
| Clipping highlight | Columns containing samples at or above 0.98 full scale are drawn in red. A `CLIP N` count appears in the header. | No clipping | No action required; highlight appears automatically. |
| PAUSED badge | Shown in the footer when the display is frozen. | Not shown (live) | Click the display once to resume. |
| No-audio placeholder | Replaces the trace when no samples have arrived for more than 1 second. | — | Disappears as soon as audio resumes. |

## Tips

- The header readout always labels the source (`RX` or `TX`) so you do not need to rely on the tint alone when working in low-light conditions.
- The tooltip on the display reads "Click to pause/resume waveform capture" as a quick reminder of the click behavior.
- A radio connection is not required for the Waveform applet to open, but live audio data requires an active audio path.

## Troubleshooting

- **Display shows "No audio" message** — No scope samples have arrived in the last 1 second. Confirm audio is routed correctly and the radio is actively receiving or transmitting.
- **Trace is frozen and not updating** — The display is paused. Click the display once to resume. The `PAUSED` badge in the footer confirms this state.
- **WAVE tray button is not visible** — Open `View > Applet Panel` to confirm the applet panel is shown, or use `View > Reset Applet Order` to restore the default applet layout.

## Related

- [Waveform applet overview](overview.md)
- [Pause and clear the waveform display](pause-and-clear-the-waveform-display.md)

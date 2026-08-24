# Open the mini-pan narrow scope

Open the Mini-Pan, a small narrow-band scope centred on the active VFO's receive passband, so you can watch a distinct slice of spectrum independent of the main panadapter.

## Before you start

- Connect to your FLEX-8600 radio.
- Ensure the applet panel is visible (it is shown by default, and also available in Minimal Mode).

## Steps

1. In the applet panel, click the Mini-Pan tile.
2. The Mini-Pan scope opens, showing the active VFO's receive passband with a hairline on the carrier frequency.
3. To close the scope, click the close button on its title bar (the scope hides; it consumes no radio resources when hidden).

The Mini-Pan floats over other applications by default. You can also dock it, make it always-on-top, or close it using the controls on its title bar.

## What each control does

| Control | Behavior | Default / Range | Setting key |
| --- | --- | --- | --- |
| Mini-Pan tile | Opens and closes the scope. | — | — |
| Scope (right-click) | Opens a menu to choose the span. | ±5 kHz (10 kHz total span) | `MiniPan` |
| VFO readout | Shows the followed VFO frequency, drawn inside the trace on the same row as the span labels. | — | — |
| Title bar controls | Float, dock, always-on-top, close. Handled by the standard container title bar. | — | — |

The scope's dBm range is fixed at -130 to -40. The frequency readout and hairline are centred on the passband centre, not the carrier.

## Tips

- The scope is centred on the passband centre rather than the carrier, so on SSB the received signal appears in the middle of the view.
- The scope mirrors the main panadapter's FFT Line/Fill settings, so it will match the appearance of your main spectrum.
- The Mini-Pan is a view only — it creates no panadapter or slice, so opening it costs the radio nothing.

## Troubleshooting

- **The Mini-Pan tile is not visible** — The applet panel may be hidden. Check the View menu for applet panel settings, or enter Minimal Mode where the applet panel is shown.
- **The scope shows a placeholder `—.———` readout** — No valid VFO frequency is available. Verify you are connected to a radio and a valid slice is active.

## Related

- [Mini-Pan overview](overview.md)
- [Change the mini-pan span with a right-click (5 or 10 kHz)](change-the-mini-pan-span-with-a-right-click-5-or-10-khz.md)

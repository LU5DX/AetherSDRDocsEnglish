# Output Level Meter overview

The Output Level Meter is a vertical dB meter that shows the smoothed post-processing peak level of an audio stage. It gives you a continuous visual and numeric read of how close the output signal is to clipping, so you can set drive and output levels without guessing.

## How it works

The meter receives peak level updates from the audio engine and applies fast-attack / slow-release ballistics before displaying the result. When the incoming level rises, the smoothing factor is 0.6 (fast attack), so the bar reacts quickly to peaks. When the level falls, the smoothing factor is 0.08 (slow release), so the bar decays gradually. This matching ballistic behavior is shared with the EQ output fader meter, so all meters in AetherSDR feel visually consistent.

The meter is visible inside the Tube applet's frameless editor, to the right of the saturation curve. Open it by double-clicking the TUBE stage in the chain widget. The same ballistics are also used by the EQ editor's Output Fader meter.

No settings are persisted for this widget. It has no interactive controls; all elements are read-only indicators.

### Numeric readout throttling

The numeric dB readout below the bar updates at 10 Hz (100 ms intervals) even though the level bar animates on every paint event. This keeps the digits stable and readable while the bar continues to show smooth level changes. The readout displays `-inf` when the smoothed peak level is below approximately −59.5 dB, and re-formats to a signed dB value with one decimal place otherwise.

## What each control does

| Element | Description | Range / Values |
|---|---|---|
| Header label | Identifies what the meter is measuring. The Tube applet sets this to `OUT`. An empty string hides the header. | Any short string; default `OUT` |
| Level bar | Gradient-filled vertical bar showing the smoothed peak level. Fills from the bottom up, proportional to the current dB value. | −60 dB (bottom) to 0 dB (top) |
| dB scale ticks | Static reference grid to the left of the bar with labeled tick marks. | 0, −6, −12, −20, −40 dB |
| Numeric readout | Displays the smoothed peak as a signed dB value to one decimal place, centered below the bar. Updates at 10 Hz. Shows `-inf` when the level is below approximately −59.5 dB. | `-inf` or a value in the form `+/-XX.X dB` |

### Level bar color

The fill color changes with level to give an immediate sense of headroom:

| Color | Level range | Meaning |
|---|---|---|
| Green | −60 dB to −12 dB | Normal operating level |
| Lime | −12 dB to −6 dB | Moderate level |
| Amber | −6 dB to −3 dB | Approaching clipping |
| Red | Above −3 dB | 3 dB or less from clipping |

## Tips

- Watch for amber or red on the level bar while adjusting the Tube applet's Drive or Output knobs. Red means you have 3 dB or less of headroom before clipping.
- The slow-release ballistics (alpha 0.08) mean the bar holds elevated readings briefly after a peak. This is intentional — it lets you catch transients that would otherwise disappear before you notice them.
- The numeric readout may appear to "lag" behind the level bar by up to 100 ms. This is normal — the bar animates smoothly while the digits update at a fixed 10 Hz rate for readability.

## Related

- [Read the output level meter on the Tube applet](read-the-output-level-meter-on-the-tube-applet.md)
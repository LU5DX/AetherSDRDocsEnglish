# Read the output level meter on the Tube applet

The Output Level Meter inside the Tube applet shows the smoothed peak signal level after the tube saturation stage. Use it to confirm your output is loud enough to be useful and to catch levels that are close to clipping.

## Before you start

- The Tube applet must be visible. It appears as "Aetherial Mic-PreAmp" (TX) or "Aetherial Dynamic Tube" (RX) inside the Aetherial Audio (TXDSP) parent container. If the applet is hidden, enable the Tube stage via the CHAIN widget on the matching side.
- No radio connection is required to read the meter.

## Steps

1. Locate the Tube applet for the side you want to monitor — "Aetherial Mic-PreAmp" for TX or "Aetherial Dynamic Tube" for RX.
2. Double-click the TUBE stage in the CHAIN widget to open the frameless editor titled "Aetherial Tube — TX" or "Aetherial Tube — RX".
3. Find the vertical meter to the right of the saturation curve. Its header label reads **OUT**.
4. Pass audio through the stage (transmit, or receive a signal). The colored bar rises and falls with the smoothed peak output level.
5. Read the exact level from the numeric readout below the bar. The value is displayed as a signed dB figure to one decimal place (for example, `−4.3 dB`). Below approximately −59.5 dB the readout shows `-inf`.

## What each control does

| Element | What it shows | Range | Notes |
|---|---|---|---|
| **OUT** (header label) | Identifies the meter as the post-saturation output | — | Static label; set by the Tube applet. |
| Level bar | Smoothed peak fill, color-coded by level | −60 dB (bottom) to 0 dB (top) | Fast attack (alpha = 0.6), slow release (alpha = 0.08). |
| dB scale ticks | Static reference lines at 0, −6, −12, −20, and −40 dB | — | Tick lines extend from the label column onto the bar. |
| Numeric readout | Smoothed peak as a signed dB value | `-inf` or a signed value to one decimal place | Shows `-inf` below approximately −59.5 dB. |

### Color meaning

| Bar color | Level range | Meaning |
|---|---|---|
| Green | −60 to −12 dB | Well clear of clipping. |
| Lime | −12 to −6 dB | Approaching moderate levels. |
| Amber | −6 to −3 dB | Getting close to clipping; watch the Output knob. |
| Red | Above −3 dB | Within 3 dB of clipping. Reduce Drive or Output. |

## Tips

- The meter uses the same fast-attack / slow-release ballistics as the meter in the EQ output fader, so brief transient peaks are caught quickly but the bar does not drop instantly — brief excursions into red may represent short peaks even if the bar lingers.
- If the bar sits in the red regularly, reduce the Output knob (range −24.0 to 12.0 dB, default 0.0 dB) to bring the post-saturation level down without changing the saturation character.
- If the bar barely moves off the bottom, increase Drive (range 0.0 to 24.0 dB, default 0.0 dB) to push more signal into the tube stage and raise the output reading.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)

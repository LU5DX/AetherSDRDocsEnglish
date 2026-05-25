# Read the output level meter on the Tube applet

The Output Level Meter in the Tube applet shows the smoothed post-saturation peak level of your audio signal. Use it to confirm that the Tube stage is not clipping its output and to judge how much headroom remains after drive and output gain are applied.

## Before you start

- The Tube applet must be present in the applet panel.
- The Tube editor must be open. If it is not open, double-click the TUBE stage in the chain widget to open it.

## Steps

1. Double-click the TUBE stage in the chain widget to open the Tube editor.
2. Locate the vertical meter on the right side of the editor, to the right of the saturation curve. The header label reads **OUT**.
3. Feed audio through the radio. The level bar rises and falls as signal passes through the Tube stage.
4. Read the color of the fill to judge headroom at a glance (see color meanings below).
5. Read the numeric value in the readout below the bar for a precise signed dB figure. The numeric readout updates at 10 Hz to keep digits readable while the bar animates every paint.

## What each control does

| Element | What it shows | Range | Notes |
|---|---|---|---|
| Header label | Identifies the meter | Reads **OUT** | Confirms this meter shows the post-saturation output level. |
| Level bar | Smoothed peak fill | −60 dB (bottom) to 0 dB (top) | Uses fast-attack (alpha = 0.6) / slow-release (alpha = 0.08) ballistics. Gradient fill: green (low) → lime → amber → red (top, above −3 dB). |
| dB scale ticks | Static reference grid | 0, −6, −12, −20, −40 dB labelled | Tick lines extend onto the bar so absolute level is readable at a glance. |
| Numeric readout | Smoothed peak as a signed dB value | `-inf` or a signed value to one decimal place, e.g. `+0.0 dB` | Displays `-inf` when the signal is below approximately −59.5 dB. Updated at 10 Hz for readability. |

### Level bar color meanings

| Color | Approximate level | Meaning |
|---|---|---|
| Green | −60 dB to −12 dB | Plenty of headroom. |
| Lime | −12 dB to −6 dB | Moderate level; normal operating range for most signals. |
| Amber | −6 dB to −3 dB | Approaching clipping; consider reducing Drive or Output. |
| Red | Above −3 dB | 3 dB or less from clipping. Reduce Drive or Output to bring the level down. |

## Tips

- The meter ballistics match those of the EQ Output Fader meter, so the visual feel is consistent if you use both applets side by side.
- If the bar stays red during normal speech peaks, reduce the **Output** knob (range −24 dB to +12 dB, default 0.0 dB) or reduce the **Drive** knob (range 0 dB to 24 dB, default 0.0 dB) until amber or lower is typical for your signal peaks.
- The slow-release ballistics (alpha = 0.08) mean the bar descends gradually after a peak, making it easier to catch transient overloads visually.
- The numeric readout refreshes at 10 Hz rather than on every paint frame. This prevents the digits from flickering or becoming unreadable during fast level changes while the bar continues to animate smoothly.

## Related

- [Output Level Meter overview](overview.md)
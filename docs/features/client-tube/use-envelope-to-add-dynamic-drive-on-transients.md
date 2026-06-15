# Use Envelope to add dynamic drive on transients

The Envelope knob connects an envelope follower to the tube drive, so the amount of saturation changes in real time with the input signal level. Use it on TX to add harmonic grit on mic transients, or on RX to make received audio feel more present on peaks.

## Before you start

- The Tube stage must be enabled for the side you want to adjust (TX or RX). If the applet is not visible, enable the stage via the CHAIN widget first.
- Set Drive to a level where the transfer curve already shows some bend. Envelope modulates that drive; if Drive is at 0 dB the effect will be subtle.
- When a Tube stage is bypassed, the entire applet tile dims to approximately 55 % opacity. This visual cue matches the dim effect used on the EQ curve and confirms the DSP stage is inactive.

## Steps

1. Double-click the TUBE stage in the CHAIN widget on the TX or RX side to open the floating editor titled "Aetherial Tube — TX" or "Aetherial Tube — RX".
2. Locate the Envelope knob in the right column of the editor.
3. Turn Envelope clockwise (positive) to increase drive on transients — the tube gets hotter as input levels rise. Turn it counter-clockwise (negative) to reduce drive on transients, compressing harmonics dynamically. Default is 0 %.
4. Adjust Attack to set how quickly the envelope follower responds when levels rise. Lower values (toward 0.1 ms) react faster; higher values (toward 30.0 ms) smooth out short spikes.
5. Adjust Release to set how quickly the follower recovers after levels drop. Lower values (toward 10.0 ms) recover faster; higher values (toward 500.0 ms) let the effect hang longer.
6. Watch the live input ball on the transfer curve — with Envelope active, the ball will move further along the curve on peaks than on quiet passages, confirming the follower is working.

## What each control does

| Control  | Default   | Valid range      |
|----------|-----------|------------------|
| Envelope | 0 %       | -1.0 to +1.0     |
| Attack   | 5.00 ms   | 0.1 to 30.0 ms   |
| Release  | 35.00 ms  | 10.0 to 500.0 ms |
| RN2      | unchecked | —                |
## Bypass dimming

When a Tube stage is bypassed, AetherSDR applies a `QGraphicsOpacityEffect` to the applet tile and renders it at 55 % opacity. The tile returns to full opacity as soon as the stage is re-enabled. This behavior applies to both the TX and RX tiles and requires no configuration.

## Inline value editing

Each knob supports direct numeric entry for precise adjustment. Click the displayed value below any knob to activate an inline edit field. The field appears in a dark inset box with a cyan border when focused.

- Type a numeric value and press **Enter** to commit. The value is clamped to the knob's valid range.
- Click elsewhere on the interface or press **Tab** to commit the value on focus-out.
- Press **Escape** to cancel editing and revert to the previous value.
- In locales that use a comma as decimal separator (e.g., "12,5"), the editor accepts the locale's format.
- The editor also accepts values with trailing unit text (e.g., "5.00 ms" or "−6 dB") by stripping non-numeric characters before parsing.
- Invalid input silently reverts to the last valid value.

## Tips

- After setting a positive Envelope value, check the OUT meter in the editor. Peaks may be louder than the static Drive setting alone would produce; use the Output knob to compensate.
- For natural-sounding TX mic grit, start with Envelope around +30 %, Attack at 5 ms, and Release at 50–80 ms, then adjust to taste.
- Negative Envelope values behave like a dynamic saturation reducer — useful on RX to tame harsh peaks without removing tube character from quieter passages.
- The Dry/Wet knob blends the fully processed signal (including envelope-modulated saturation) with the dry signal, so you can use high Envelope values without fully committing to the effect.
- Use inline value editing to set exact Attack, Release, or Envelope values rather than approximate knob positions.
- If a tile appears dimmed and controls are unresponsive, the stage is bypassed. Re-enable it via the CHAIN widget; the tile will return to full brightness.
- The applet tile now uses theme-aware colors through the `color.knob.*` namespace. Knob background, foreground arc, handle, label text, and value text all respect the current theme settings rather than using hardcoded colors.
- The transfer curve in the curve widget also uses theme-aware colors: background (`color.background.0`), frame and grid (`color.background.1`), axis (`color.background.1`), curve (`color.accent.dim`), ball glow (`color.accent.warning`), and ball core (`color.text.primary`).

## Troubleshooting

- **Envelope knob has no audible effect** — Drive is likely at or near 0 dB. Set Drive to a value where the transfer curve visibly bends, then re-test Envelope.
- **Effect sounds erratic or pumping** — Attack or Release values are too short for the program material. Increase Release toward 100 ms or more; increase Attack above 10 ms to ignore short transients.
- **Output level spikes on transients** — Positive Envelope adds gain on peaks. Reduce Output to compensate, or reduce Envelope depth.
- **Applet tile appears dim** — The Tube stage is bypassed. Enable the stage via the CHAIN widget to restore full opacity and DSP processing.
- **Inline editor does not accept typed value** — Ensure the value falls within the knob's valid range. Values outside the range are silently clamped. Check that you are using the locale-appropriate decimal separator.
- **Knob colors look wrong** — Verify you are using a compatible theme. The knob components now read from `color.knob.background`, `color.knob.foreground`, `color.knob.handle`, `color.text.secondary`, and `color.text.primary` in the theme definition.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Tune Attack and Release for natural-sounding envelope following](tune-attack-and-release-for-natural-sounding-envelope-following.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Dry/Wet](parallel-blend-saturation-with-dry-wet.md)
- [Monitor output clipping with the level meter in the editor](monitor-output-clipping-with-the-level-meter-in-the-editor.md)
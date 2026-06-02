# Brighten or darken the saturated signal with Tone

Use the Tone knob to tilt the spectral character of the saturated signal — negative values make it darker and warmer, positive values make it brighter and more present. Tone works on both the TX side (Aetherial Mic-PreAmp) and the RX side (Aetherial Dynamic Tube) independently.

## Before you start

- The tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- The Aetherial Mic-PreAmp (TX) or Aetherial Dynamic Tube (RX) sub-container must be visible in the Applet Panel. Double-click the TUBE stage in the CHAIN widget to open the floating editor, or locate the sub-container directly in the panel.

## Steps

1. Locate the five-knob row at the bottom of the Aetherial Mic-PreAmp (TX) or Aetherial Dynamic Tube (RX) applet.
2. Find the knob labeled **Tone** — it is the second knob from the left, between Drive and Bias.
3. Turn the **Tone** knob left (toward −1.00) to darken the saturated signal, or right (toward +1.00) to brighten it.
4. Read the current value from the label beneath the knob. The label displays two decimal places (e.g. `−0.50` or `0.75`).
5. To reset Tone to its default, double-click the **Tone** knob.
6. To type a precise value directly, click the value display below the Tone knob. A small text entry field appears. Type the desired value and press **Enter** or click elsewhere to commit. The value is clamped to the valid range automatically. Press **Escape** to cancel the edit and revert to the previous value.

## What each control does

| Control   | Default                                                                                                                                                                             | Valid range                                                                                                                                                                                               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tone (TX) | 0.00                                                                                                                                                                                | −1.0 to 1.0                                                                                                                                                                                               |
| Tone (RX) | 0.00                                                                                                                                                                                | −1.0 to 1.0                                                                                                                                                                                               |
| Drive     | 0.00 dB                                                                                                                                                                             | 0.0 to 24.0 dB                                                                                                                                                                                            |
| Bias      | 0 %                                                                                                                                                                                 | 0.0 to 1.0                                                                                                                                                                                                |
| Output    | 0.00 dB                                                                                                                                                                             | −24.0 to 12.0 dB                                                                                                                                                                                          |
| Dry/Wet   | 100 %                                                                                                                                                                               | 0.0 to 1.0                                                                                                                                                                                                |
| Envelope  | 0 %                                                                                                                                                                                 | −1.0 to 1.0                                                                                                                                                                                               |
| Attack    | 5.00 ms                                                                                                                                                                             | 0.1 to 30.0 ms                                                                                                                                                                                            |
| Release   | 35.00 ms                                                                                                                                                                            | 10.0 to 500.0 ms                                                                                                                                                                                          |
| RN2       | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. | Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. |

## Output level meter

The floating editor (titled **Aetherial Tube — TX** or **Aetherial Tube — RX**) includes an **OUT** level meter in the far-right column. This meter shows the post-saturation peak level and uses fast-attack / slow-release ballistics.

| Level range | Meter color |
|---|---|
| −60 to −12 dB | Green |
| −12 to −6 dB | Lime |
| −6 to −3 dB | Amber |
| Above −3 dB | Red |

The meter is only visible in the floating editor. It does not appear on the docked applet tile in the Applet Panel.

## Bypass dimming

When the tube stage is bypassed, the entire docked applet tile renders at reduced opacity (approximately 55 % of full brightness). This matches the dim effect used on the EQ curve widget when that stage is bypassed. The opacity returns to full as soon as the stage is re-enabled. The floating editor is not affected by this dimming.

## Tips

- Tone interacts with Drive: a high Drive value produces more saturation harmonics, so Tone adjustments become more audible as Drive increases. Dial in Drive first, then use Tone to shape the result.
- If you have the floating editor open alongside the applet, both reflect the same value. Changes made in one sync to the other within approximately 33 ms.
- A Tone value of 0.00 leaves the spectral balance of the saturated signal unchanged.
- Watch the **OUT** meter in the floating editor to catch post-saturation clipping. If the meter reaches red, reduce the **Output** knob or lower **Drive**.
- The inline value editor supports locale-aware number parsing. Enter `12,5` in a comma-decimal locale, or strip units like `12.5 ms` and the editor will parse the numeric portion.

## Troubleshooting

- **Tone knob has no audible effect** — the tube stage may be bypassed. Confirm the stage is active in the CHAIN widget on the matching side. Also check that Mix is above 0 %; a fully dry signal (Mix at 0 %) passes through the tube model but blends none of the wet output.
- **Knob position does not match what you expect after reloading** — the value is saved automatically each time the knob changes. If `ClientTubeTxTone` or `ClientTubeRxTone` is missing or corrupted in your settings file, the value reverts to the default of 0.00.
- **OUT meter is not visible** — the meter only appears in the floating editor. Double-click the TUBE stage in the CHAIN widget to open it.
- **Applet tile appears dimmed** — the tube stage is bypassed. Enable the stage in the CHAIN widget to restore full opacity.
- **Inline editor shows a red border and won't accept input** — the editor only appears when you click the value display. If you do not see the editor, ensure you are clicking directly on the numeric value text below the knob, not on the knob itself. The editor reverts to a label-like appearance when not focused.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Parallel-blend saturation with Dry/Wet](parallel-blend-saturation-with-mix.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
- [Modulate the tube curve with Envelope](modulate-the-tube-curve-with-envelope.md)
- Type exact values with the value popup editor
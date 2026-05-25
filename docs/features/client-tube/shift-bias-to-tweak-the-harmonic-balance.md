# Shift Bias to tweak the harmonic balance

The Bias knob moves the operating point on the tube transfer curve, changing the balance of even and odd harmonics the saturator produces. Use it to fine-tune the character of the saturation after you have set Drive.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- Drive should already be set high enough that the transfer curve is visibly bent. See [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md).
- Open the floating editor by double-clicking the TUBE stage in the CHAIN widget on the TX or RX side. The editor is titled "Aetherial Tube — TX" or "Aetherial Tube — RX".

## Steps

1. Locate the Bias knob in the centre row of the editor, to the right of the A / B / C model selector.
2. Turn Bias from its default of 0 % toward higher values (up to 100 %) to shift the operating point and increase asymmetric saturation.
3. Watch the transfer curve: the curve shifts its bend point as you turn the knob. The live input ball tracks the new operating region in real time.
4. Stop when the harmonic balance sounds correct for your use case.
5. If the overall level changes noticeably, adjust the Output knob to compensate. See [Compensate level changes with Output](compensate-level-changes-with-output.md).

## What each control does

| Control   | Default                                                                                                                                                                             | Valid range                                                                                                                                                                                               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bias (TX) | 0 %                                                                                                                                                                                 | 0 % to 100 % (internal 0.0 to 1.0)                                                                                                                                                                        |
| Bias (RX) | 0 %                                                                                                                                                                                 | 0 % to 100 % (internal 0.0 to 1.0)                                                                                                                                                                        |
| RN2       | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. | Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. |

The Bias knob uses a linear mapping. The displayed value is a percentage. Internally the setting is stored as a value from 0.0 to 1.0 in `ClientTubeTxBias` (TX side) or `ClientTubeRxBias` (RX side).
## Inline value editing

The single- and three-knob compact views and all knob-based editors now support inline value editing.

1. Click the numeric value displayed below any knob. A text entry field replaces the value label.
2. Type the desired value directly. You may include units (e.g., "5.00 ms", "-6 dB", "12.5") or just the number.
3. Press Enter to commit the value. The knob immediately moves to the new setting.
4. The field automatically accepts locale-aware number formats (comma decimal separators for locales where that is standard).
5. If you type an invalid value, the knob reverts to its previous setting.

**Note:** The inline editor is available on all ClientCompKnob instances across the application: Drive, Tone, Bias, Output, Dry/Wet, Envelope, Attack, Release, and any other knob-based control that displays its numeric value.

## Tips

- Bias interacts with the selected tube character. Try each of A, B, and C to hear how the same Bias value produces different harmonic results with different models.
- The Bias knob is also present in the docked applet tile (the compact five-knob row beneath the transfer curve), so you can make quick adjustments without opening the full editor.
- Changes made in the docked tile and the floating editor stay in sync; a 30 Hz timer keeps both views updated.
- To enter Bias values with the inline editor, click the percentage display (e.g., "0 %") beneath the knob and type a number between 0 and 100.

## Bypass dim

When the Tube stage is bypassed, the entire docked applet tile renders at reduced opacity (approximately 55 % of full brightness). This matches the dim effect used on the EQ curve and gives a clear at-a-glance indication that the stage is inactive. The tile returns to full opacity as soon as the stage is re-enabled.

## Troubleshooting

- **Bias knob has no audible effect** — Drive may be at or near 0.00 dB. Bias only shifts the operating point meaningfully when the curve is already bent. Increase Drive first.
- **Level changes when Bias is adjusted** — This is expected. The asymmetry introduced by Bias can raise or lower the apparent output. Trim the Output knob to compensate.
- **Docked tile appears dimmed** — The Tube stage is bypassed. Re-enable it on the TX or RX side. See [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md).
- **Inline editor does not accept typed value** — Ensure you are typing a plain number or a number with optional decimal point and sign. Commas are allowed only in locales where they serve as decimal separators.

## Related

- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Select a tube character (Model A, B, or C) to change harmonic flavour](select-a-tube-character-model-a-b-or-c-to-change-harmonic-flavour.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Monitor output clipping with the level meter in the editor](monitor-output-clipping-with-the-level-meter-in-the-editor.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
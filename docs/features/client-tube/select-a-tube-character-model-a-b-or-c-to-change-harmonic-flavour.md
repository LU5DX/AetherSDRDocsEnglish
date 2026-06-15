# Select a tube character (Model A, B, or C) to change harmonic flavour

The tube character selector chooses which of three distinct saturation curves the tube stage uses, directly shaping the harmonic content added to your TX or RX audio. Switch models to compare flavours without changing any other parameter.

## Before you start

- The Tube stage must be enabled on the side you want to adjust (TX or RX). If the stage is bypassed, the model selection still persists but you will not hear a difference until you enable it. When the stage is bypassed, the entire docked applet tile dims to approximately 55 % opacity as a visual indicator; it returns to full opacity when the stage is re-enabled.
- Open the floating editor for the relevant side: double-click the TUBE stage in the CHAIN widget on the TX or RX side to open the "Aetherial Tube — TX" or "Aetherial Tube — RX" editor. The model selector is only available in the floating editor, not in the docked applet tile.

## Steps

1. Double-click the TUBE stage in the CHAIN widget on the TX or RX side. The frameless editor titled "Aetherial Tube — TX" or "Aetherial Tube — RX" opens.
2. Locate the three toggle buttons labelled **A**, **B**, and **C** in the centre row of the editor, between the Tone knob and the Bias knob.
3. Click **A**, **B**, or **C** to select a tube character. The selected button turns amber. Only one model can be active at a time.
4. Watch the transfer curve: the curve shape updates immediately to reflect the selected character. The live input ball continues to ride the new curve.

## What each control does

| Control      | Default                                                                                                                                                                             | Valid values                                                                                                                                                                                              |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **A**        | Checked (active)                                                                                                                                                                    | Selected / not selected                                                                                                                                                                                   |
| **B**        | Unchecked                                                                                                                                                                           | Selected / not selected                                                                                                                                                                                   |
| **C**        | Unchecked                                                                                                                                                                           | Selected / not selected                                                                                                                                                                                   |
| **Drive**    | 0.00 dB                                                                                                                                                                             | 0.0 to 24.0 dB                                                                                                                                                                                            |
| **Tone**     | 0.00                                                                                                                                                                                | -1.0 to 1.0                                                                                                                                                                                               |
| **Bias**     | 0 %                                                                                                                                                                                 | 0.0 to 1.0                                                                                                                                                                                                |
| **Output**   | 0.00 dB                                                                                                                                                                             | -24.0 to 12.0 dB                                                                                                                                                                                          |
| **Dry/Wet**  | 100 %                                                                                                                                                                               | 0.0 to 1.0                                                                                                                                                                                                |
| **Envelope** | 0 %                                                                                                                                                                                 | -1.0 to 1.0                                                                                                                                                                                               |
| **Attack**   | 5.00 ms                                                                                                                                                                             | 0.1 to 30.0 ms                                                                                                                                                                                            |
| **Release**  | 35.00 ms                                                                                                                                                                            | 10.0 to 500.0 ms                                                                                                                                                                                          |
| **RN2**      | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. | Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. |
| RN2          | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. | Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. |

A, B, and C are mutually exclusive. Selecting one deselects the others. The same setting key (`ClientTubeTxModel` for TX, `ClientTubeRxModel` for RX) stores the choice for its respective side; TX and RX selections are fully independent.
## Indicators

| Indicator | Purpose                                                                                                                         |
|-----------|---------------------------------------------------------------------------------------------------------------------------------|
| Transfer curve | Compact-mode ClientTubeCurveWidget. Draws the currently-configured tube transfer curve with a live ball at the input. Colors are theme-aware via the ThemeManager color keys. |
| Live input ball | Dot moves along the transfer curve at the current input level, visualising the saturation regime. Ball glow uses `color.accent.warning`, core uses `color.text.primary`. |
| Output level meter | ClientLevelMeter widget (far right of the editor) showing post-saturation peak level with fast-attack / slow-release ballistics. Labelled 'OUT'. Only visible in the floating editor, not the docked applet tile. Colour zones: green (-60 to -12 dB), lime (-12 to -6 dB), amber (-6 to -3 dB), red (above -3 dB). |

## Bypass dim behaviour

When the tube stage is bypassed, the docked applet tile renders at reduced opacity (approximately 55 %). This matches the dim effect used on the EQ curve elsewhere in the chain. The tile returns to full opacity as soon as the stage is re-enabled. The dim is applied to the entire tile, including the transfer curve and all knobs. It is a visual indicator only and does not affect the persisted settings.

## Knob inline value editing

All knob controls in the Aetherial Tube floating editor support inline value editing. Click a knob's displayed value text to open a small text entry field overlaid on the control. Type a numeric value and press Enter, or click elsewhere, to commit the value. The entered value is clamped to the knob's valid range. Press Escape to cancel editing and revert to the previous value.

When the text entry field is focused, it shows a dark background with a cyan border to indicate edit mode. When not focused, it appears identical to the painted value text.

## Theme-aware knob colours

All knob components (background ring, value arc, pointer, label, and value text) now read from the ThemeManager's dedicated `color.knob.*` namespace. The per-applet container override (e.g. `applet/tube`) allows the tube knobs to respect the current theme. Knob label text uses `color.text.secondary`, value text uses `color.text.primary`.

## Tips

- The transfer curve display updates in real time when you switch models. Use this together with the live input ball to see how heavily your current Drive and Bias settings are bending the new curve before committing.
- The TX and RX sides maintain independent model selections. Changing the model in "Aetherial Tube — TX" has no effect on "Aetherial Tube — RX" and vice versa.
- After switching models, the harmonic mix may change noticeably at high Drive or Bias settings. If the level changes, adjust the Output knob to compensate.
- Use inline value editing for precise numeric entry rather than dragging knobs. This is especially useful for setting exact values for Bias, Drive, Output, and Envelope parameters.
- If the docked tile appears dimmed, the tube stage is currently bypassed. Re-enable it before evaluating how a model change sounds.
- The tube curve widget colours are fully theme-aware: background uses `color.background.0`, frame uses `color.background.1`, curve uses `color.accent.dim`.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Shift Bias to tweak the harmonic balance](shift-bias-to-tweak-the-harmonic-balance.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
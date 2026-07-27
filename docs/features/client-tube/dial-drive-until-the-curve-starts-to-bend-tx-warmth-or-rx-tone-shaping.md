# Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)

Use the Drive knob to push signal into the tube stage and produce harmonic saturation. Watching the transfer curve bend as you increase Drive tells you exactly when and how much saturation is happening.

## Before you start

- The Tube stage must be enabled on the side you want to shape (TX or RX). Enable it through the CHAIN widget or by opening the floating editor for that side.
- The "Aetherial Mic-PreAmp" (TX) or "Aetherial Dynamic Tube" (RX) sub-container must be visible inside the Aetherial Audio (TXDSP) parent container in the applet panel.

## Steps

1. Locate the correct sub-container in the applet panel: "Aetherial Mic-PreAmp" for TX signal shaping, or "Aetherial Dynamic Tube" for RX tone shaping.
2. Look at the transfer curve display at the top of the applet. At Drive 0.0 dB the curve is a straight diagonal line — no saturation.
3. Turn the Drive knob clockwise. Watch the transfer curve: the shoulders begin to compress and bend as Drive increases. The live input ball moves along the curve and shows which part of the curve your current signal level is hitting.
4. Stop increasing Drive when the curve shows the amount of bend you want. Subtle warmth appears with light bend; heavier saturation comes from pushing Drive further toward 24.0 dB.
5. If the saturated output is noticeably louder or quieter than the dry signal, trim the Output knob to compensate. The floating editor's OUT meter (far right column) shows the post-saturation peak level and helps you judge the trim.

## What each control does

| Control  | Default   | Valid range                        |
|----------|-----------|------------------------------------|
| Drive    | 0.00 dB   | 0.0 – 24.0 dB                      |
| Tone     | 0.00      | −1.0 – 1.0                         |
| Bias     | 0 %       | 0 – 100 %                          |
| Output   | 0.00 dB   | −24.0 – 12.0 dB                    |
| Dry/Wet  | 100 %     | 0 – 100 %                          |
| Envelope | 0 %       | −100 – 100 %                       |
| Attack   | 5.00 ms   | 0.1 – 30.0 ms                      |
| Release  | 35.00 ms  | 10.0 – 500.0 ms                    |
| RN2      | unchecked | TX-only toggle (hidden in RX mode) |

**Transfer curve** — Indicator. Compact-mode ClientTubeCurveWidget. Draws the currently-configured tube transfer curve with a live ball at the input. The shape changes as you adjust Drive, Bias, and model selection. The live input ball rides the curve at the current signal level, showing the active saturation regime. No persisted key.

**Drive** — Linear mapping. Pushes more signal into the tube stage. Higher values cause the transfer curve to bend more sharply, producing stronger harmonic content. Label 'X.XX dB'. Left column of the editor.

**Tone** — Linear mapping. Negative values darken the saturated signal; positive values brighten it. Label 'X.XX'. Centre row of the editor, left of the Model selector.

**Model A / B / C** — Toggle buttons. Selects the tube character model. Exclusive selection — only one model active at a time. Defaults to Model A (checked). Amber when checked. Backing value stored as integer 0/1/2 in `ClientTubeTxModel` / `ClientTubeRxModel`.

**Bias** — Linear mapping. Shifts the operating point on the transfer curve, changing the balance of even and odd harmonics. Label displayed as percentage. Centre row of the editor, right of the Model selector. Setting key `ClientTubeTxBias` (not `ClientTubeTxBiasAmount`) / `ClientTubeRxBias`.

**Output** — Linear mapping. Post-tube make-up or trim gain. Use this to match the saturated level to the dry level. Label 'X.XX dB'. Left column of the editor. Setting key `ClientTubeTxOutputDb` (not `ClientTubeTxOutputGainDb`) / `ClientTubeRxOutputDb`.

**Dry/Wet** — Linear mapping. Dry/wet blend. At 100 % only the saturated signal passes. Reducing Dry/Wet blends in the original dry signal for parallel saturation. Label displayed as percentage. Left column of the editor (top knob).

**Envelope** — Linear mapping (−1.0 to +1.0). Dynamic envelope follower modulation. Positive values increase drive on transients (the tube gets hotter on loud peaks); negative values reduce it, compressing harmonics dynamically. Label displayed as percentage (signed). Right column of the editor. Setting key `ClientTubeTxEnvelope` / `ClientTubeRxEnvelope`.

**Attack** — Exponential mapping (0.1 × 300^n). Sets how quickly the envelope follower responds to rising levels when Envelope ≠ 0. Label shows 'X.XX ms' below 10 ms, 'X.X ms' above. Right column of the editor.

**Release** — Exponential mapping (10 × 50^n). Sets how quickly the envelope follower recovers after levels drop when Envelope ≠ 0. Label shows 'X.XX ms' below 100 ms, 'X.X ms' above. Right column of the editor.

**RN2** — TX-only toggle button (hidden in RX mode). Default unchecked. Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate, compressor, or saturator. Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine.

**Output level meter** — Indicator. ClientLevelMeter widget (far right of the editor) showing post-saturation peak level with fast-attack / slow-release ballistics. Labelled 'OUT'. Only visible in the floating editor ("Aetherial Tube — TX" or "— RX"), not the docked applet tile. Colour zones: green (−60 to −12 dB), lime (−12 to −6 dB), amber (−6 to −3 dB), red (above −3 dB). No persisted key.

**Value edit mode** — Click any knob's displayed value to enter edit mode. The value text transforms into an inline text field with a subtle dark background and cyan border. Type a numeric value (supports locale-aware formats like "12,5" and unit-stripped input like "3.5 ms" or "−6 dB") and press Enter or click elsewhere to commit. The value is clamped to the knob's valid range. Press Escape or leave the field with invalid input to revert silently.

## Tips

- Start with Drive at 0.0 dB and increase slowly. The transfer curve is the most direct visual guide to how much saturation you are adding.
- The TX and RX sides are fully independent. Adjustments to the TX tube do not affect the RX tube and vice versa.
- The floating editor (opened by double-clicking the TUBE stage in the CHAIN widget) and the docked applet knobs stay in sync — changes in one are reflected in the other within approximately 30 ms.
- If you want to hear the effect without committing to it, reduce Dry/Wet toward 0 % to blend back to dry while keeping your Drive setting in place.
- Use the OUT meter in the floating editor to confirm that the post-saturation level is where you expect it before closing the editor.
- To dial in an exact value, click the knob's displayed value to enter inline edit mode rather than dragging the knob.
- The applet tile and floating editor use per-applet container colour overrides defined in the theme's `color.knob.*` namespace (background, foreground, handle) and `color.text.*` for label/value text. Theme customisation affects knob appearance in this applet independently of other applet types.
- Enable RN2 on the TX side in voice modes (SSB, AM, FM) to suppress background noise before the saturation stage. The RN2 toggle is located below the output level meter in the floating editor. Digital modes bypass RN2 automatically.

## Troubleshooting

- **Transfer curve does not bend when Drive is increased** — The Tube stage may not be enabled for that side. Enable it through the CHAIN widget. The applet is hidden until the stage is active.
- **Knobs in the applet do not match the floating editor** — The applet syncs from the engine on a polling timer. Wait a moment; they should align within about 30 ms. If they remain out of sync, the audio engine may not be connected — check that the radio connection is active.
- **OUT meter is not visible** — The output level meter only appears in the floating editor, not in the docked applet tile. Open the floating editor by double-clicking the TUBE stage in the CHAIN widget.
- **Docked applet tile looks faded or dimmed** — When the Tube stage is bypassed, the entire docked tile is rendered at reduced opacity. This is expected behaviour and matches the dim effect applied to the EQ curve when that stage is bypassed. Re-enable the Tube stage through the CHAIN widget to restore full opacity.
- **Inline value edit shows wrong value after applying** — If the value was typed with unsupported characters, the knob reverts to its last valid setting. Ensure you enter only numbers and, optionally, a decimal separator.
- **RN2 toggle is not visible** — RN2 is TX only and only appears in the floating editor for the TX side ("Aetherial Tube — TX"). It is hidden in the RX floating editor and in the docked applet tile. If you are in a digital mode (RADE, DAX, RTTY, FT8, FDV, CW), RN2 is bypassed and the toggle may be hidden regardless of side.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- Use Envelope for dynamic tube response
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
- Enable RNNoise noise suppression on TX (RN2)
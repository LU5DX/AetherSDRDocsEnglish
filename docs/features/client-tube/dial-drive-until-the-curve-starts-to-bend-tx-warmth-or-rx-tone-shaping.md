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

| Control  | Default                                                                                                                                                                             | Valid range                                                                                                                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Drive    | 0.00 dB                                                                                                                                                                             | 0.0 – 24.0 dB                                                                                                                                                                                             |
| Tone     | 0.00                                                                                                                                                                                | −1.0 – 1.0                                                                                                                                                                                                |
| Bias     | 0 %                                                                                                                                                                                 | 0 – 100 %                                                                                                                                                                                                 |
| Output   | 0.00 dB                                                                                                                                                                             | −24.0 – 12.0 dB                                                                                                                                                                                           |
| Dry/Wet  | 100 %                                                                                                                                                                               | 0 – 100 %                                                                                                                                                                                                 |
| Envelope | 0 %                                                                                                                                                                                 | −100 – 100 %                                                                                                                                                                                              |
| Attack   | 5.00 ms                                                                                                                                                                             | 0.1 – 30.0 ms                                                                                                                                                                                             |
| Release  | 35.00 ms                                                                                                                                                                            | 10.0 – 500.0 ms                                                                                                                                                                                           |
| RN2      | TX-only toggle (hidden in RX mode). Enables RNNoise neural denoiser on the mic input before the DSP chain. Suppresses background noise before it reaches gate/compressor/saturator. | Located in the floating StripTubePanel below the output level meter, TX side only. Voice modes only — digital modes (RADE, DAX, RTTY, FT8, FDV, CW) bypass this stage. Setting persisted via AudioEngine. |

**Transfer curve** — Indicator. Draws the tube transfer curve in real time. The shape changes as you adjust Drive, Bias, and model selection. The live input ball rides the curve at the current signal level, showing the active saturation regime. No persisted key.

**Drive** — Pushes more signal into the tube stage. Higher values cause the transfer curve to bend more sharply, producing stronger harmonic content.

**Tone** — Negative values darken the saturated signal; positive values brighten it.

**Model A / B / C** — Toggle buttons. Selects the tube character model. Exclusive selection — only one model active at a time. Defaults to Model A (checked). Backing value stored as integer 0/1/2 in `ClientTubeTxModel` / `ClientTubeRxModel`.

**Bias** — Shifts the operating point on the transfer curve, changing the balance of even and odd harmonics.

**Output** — Post-tube make-up or trim gain. Use this to match the saturated level to the dry level.

**Dry/Wet** — Dry/wet blend. At 100 % only the saturated signal passes. Reducing Dry/Wet blends in the original dry signal for parallel saturation.

**Envelope** — Dynamic envelope follower modulation. Positive values increase drive on transients (the tube gets hotter on loud peaks); negative values reduce it, compressing harmonics dynamically. Label displayed as percentage (signed).

**Attack** — Sets how quickly the envelope follower responds to rising levels when Envelope ≠ 0. Exponential mapping (0.1 × 300^n). Label shows 'X.XX ms' below 10 ms, 'X.X ms' above.

**Release** — Sets how quickly the envelope follower recovers after levels drop when Envelope ≠ 0. Exponential mapping (10 × 50^n). Label shows 'X.XX ms' below 100 ms, 'X.X ms' above.

**Output level meter** — Indicator. Visible only in the floating editor ("Aetherial Tube — TX" or "— RX"), in the far-right column labelled OUT. Shows post-saturation peak level with fast-attack / slow-release ballistics. Colour zones: green (−60 to −12 dB), lime (−12 to −6 dB), amber (−6 to −3 dB), red (above −3 dB). No persisted key.

**Value edit mode** — Click any knob's displayed value to enter edit mode. The value text transforms into an inline text field with a subtle dark background and cyan border. Type a numeric value (supports locale-aware formats like "12,5" and unit-stripped input like "3.5 ms" or "−6 dB") and press Enter or click elsewhere to commit. The value is clamped to the knob's valid range. Press Escape or leave the field with invalid input to revert silently.
## Tips

- Start with Drive at 0.0 dB and increase slowly. The transfer curve is the most direct visual guide to how much saturation you are adding.
- The TX and RX sides are fully independent. Adjustments to the TX tube do not affect the RX tube and vice versa.
- The floating editor (opened by double-clicking the TUBE stage in the CHAIN widget) and the docked applet knobs stay in sync — changes in one are reflected in the other within approximately 30 ms.
- If you want to hear the effect without committing to it, reduce Dry/Wet toward 0 % to blend back to dry while keeping your Drive setting in place.
- Use the OUT meter in the floating editor to confirm that the post-saturation level is where you expect it before closing the editor.
- To dial in an exact value, click the knob's displayed value to enter inline edit mode rather than dragging the knob.

## Troubleshooting

- **Transfer curve does not bend when Drive is increased** — The Tube stage may not be enabled for that side. Enable it through the CHAIN widget. The applet is hidden until the stage is active.
- **Knobs in the applet do not match the floating editor** — The applet syncs from the engine on a polling timer. Wait a moment; they should align within about 30 ms. If they remain out of sync, the audio engine may not be connected — check that the radio connection is active.
- **OUT meter is not visible** — The output level meter only appears in the floating editor, not in the docked applet tile. Open the floating editor by double-clicking the TUBE stage in the CHAIN widget.
- **Docked applet tile looks faded or dimmed** — When the Tube stage is bypassed, the entire docked tile is rendered at reduced opacity. This is expected behaviour and matches the dim effect applied to the EQ curve when that stage is bypassed. Re-enable the Tube stage through the CHAIN widget to restore full opacity.
- **Inline value edit shows wrong value after applying** — If the value was typed with unsupported characters, the knob reverts to its last valid setting. Ensure you enter only numbers and, optionally, a decimal separator.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- Use Envelope for dynamic tube response
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)
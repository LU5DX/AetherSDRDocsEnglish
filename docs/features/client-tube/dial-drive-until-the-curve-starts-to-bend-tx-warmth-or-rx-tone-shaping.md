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
5. If the saturated output is noticeably louder or quieter than the dry signal, trim the Output knob to compensate.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|
| Drive | 0.0 dB | 0.0 – 24.0 dB | `ClientTubeTxDriveDb` / `ClientTubeRxDriveDb` |
| Tone | 0.00 | −1.0 – 1.0 | `ClientTubeTxTone` / `ClientTubeRxTone` |
| Bias | 0 % | 0 – 100 % | `ClientTubeTxBiasAmount` / `ClientTubeRxBiasAmount` |
| Output | 0.0 dB | −24.0 – 12.0 dB | `ClientTubeTxOutputGainDb` / `ClientTubeRxOutputGainDb` |
| Mix | 100 % | 0 – 100 % | `ClientTubeTxDryWet` / `ClientTubeRxDryWet` |

**Transfer curve** — Indicator. Draws the tube transfer curve in real time. The shape changes as you adjust Drive, Bias, and model selection. The live input ball rides the curve at the current signal level, showing the active saturation regime. No persisted key.

**Drive** — Pushes more signal into the tube stage. Higher values cause the transfer curve to bend more sharply, producing stronger harmonic content.

**Tone** — Negative values darken the saturated signal; positive values brighten it.

**Bias** — Shifts the operating point on the transfer curve, changing the balance of even and odd harmonics.

**Output** — Post-tube make-up or trim gain. Use this to match the saturated level to the dry level.

**Mix** — Dry/wet blend. At 100 % only the saturated signal passes. Reducing Mix blends in the original dry signal for parallel saturation.

## Tips

- Start with Drive at 0.0 dB and increase slowly. The transfer curve is the most direct visual guide to how much saturation you are adding.
- The TX and RX sides are fully independent. Adjustments to the TX tube do not affect the RX tube and vice versa.
- The floating editor (opened by double-clicking the TUBE stage in the CHAIN widget) and the docked applet knobs stay in sync — changes in one are reflected in the other within approximately 30 ms.
- If you want to hear the effect without committing to it, reduce Mix toward 0 % to blend back to dry while keeping your Drive setting in place.

## Troubleshooting

- **Transfer curve does not bend when Drive is increased** — The Tube stage may not be enabled for that side. Enable it through the CHAIN widget. The applet is hidden until the stage is active.
- **Knobs in the applet do not match the floating editor** — The applet syncs from the engine on a polling timer. Wait a moment; they should align within about 30 ms. If they remain out of sync, the audio engine may not be connected — check that the radio connection is active.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from either chain](bypass-the-tube-from-either-chain.md)

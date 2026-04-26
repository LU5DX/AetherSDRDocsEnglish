# Tube Saturator overview

The Tube Saturator is a TX-side audio processing stage that shapes your transmitted signal through a bias-swept tube model, adding harmonic richness and saturation. Use it to give your audio more presence and character before it reaches the radio.

## Before you start

- The Tube Saturator applet is hidden until the Tube stage is enabled. Enable it via the CHAIN widget in the PooDoo Audio (TXDSP) container, or by double-clicking the Tube stage in the CHAIN widget to open the floating editor.
- The applet appears as the `TUBE` sub-container inside the PooDoo Audio (TXDSP) parent container.

## How it works

The Tube Saturator processes the TX audio signal through a nonlinear transfer curve that models tube saturation behavior. The shape of the curve changes in real time as you adjust Drive, Bias, and the active tube model.

The applet displays a compact transfer curve graph. A live input ball rides along the curve, showing where the current signal level sits in the saturation regime — fully linear near the center, increasingly saturated toward the edges. The ball position updates at approximately 30 Hz and smooths slightly to avoid jarring jumps.

The five knobs control how hard the signal is pushed into the tube (Drive), the tonal character of the result (Tone), the asymmetry of the operating point (Bias), the post-saturation output level (Output), and the blend between the original dry signal and the saturated signal (Mix). All settings are persisted and kept in sync between the applet and the floating editor.

Bypass is handled from the CHAIN widget, not from within the applet itself.

## What each control does

| Control | Default | Range | Persisted setting | Description |
|---|---|---|---|---|
| Transfer curve | — | — | — | Displays the current tube transfer curve. Bends and shifts as Drive, Bias, and model change. |
| Live input ball | — | — | — | Dot moves along the transfer curve at the current input level, showing the active saturation regime. |
| Drive | 0.0 dB | 0.0 to 24.0 dB | `ClientTubeTxDriveDb` | Pushes more signal into the tube stage. Higher values bend the curve more aggressively. |
| Tone | 0.00 | -1.0 to 1.0 | `ClientTubeTxTone` | Negative values darken the saturated signal; positive values brighten it. |
| Bias | 0 % | 0 % to 100 % | `ClientTubeTxBiasAmount` | Shifts the operating point on the transfer curve, changing the balance of even and odd harmonics. |
| Output | 0.0 dB | -24.0 to 12.0 dB | `ClientTubeTxOutputGainDb` | Post-tube make-up or trim gain. Use this to compensate for level changes introduced by saturation. |
| Mix | 100 % | 0 % to 100 % | `ClientTubeTxDryWet` | Blends the dry (unprocessed) and saturated signals. 100 % passes only the saturated signal. |

The enabled state of the Tube stage is persisted as `ClientTubeTxEnabled` and is controlled from the CHAIN widget.

## Tips

- Start with Drive at 0.0 dB and raise it slowly until the transfer curve visibly bends. That bend is where saturation begins.
- Use Mix below 100 % to blend in only a portion of the saturated signal, which can add warmth without obvious coloration.
- Raising Bias shifts the curve asymmetrically, which introduces more even-order harmonics and changes the character of the saturation.
- If saturation raises your perceived level, pull Output down to compensate before adjusting other settings.
- Changes made in the floating editor are reflected in the applet knobs automatically, and vice versa.

## Related

- [Dial Drive until the curve starts to bend](dial-drive-until-the-curve-starts-to-bend.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)

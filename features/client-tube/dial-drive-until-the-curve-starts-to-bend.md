# Dial Drive until the curve starts to bend

Drive controls how hard the signal is pushed into the tube model. Increasing it causes the transfer curve to visibly bend away from a straight diagonal, which is the point at which harmonic saturation begins.

## Before you start

- The Tube Saturator stage must be enabled. If the TUBE sub-container is not visible, enable the stage via the CHAIN widget or double-click the Tube stage in the CHAIN widget to open the floating Tube editor.
- Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container so the transfer curve and knobs are visible.

## Steps

1. Look at the transfer curve display at the top of the TUBE applet. At Drive 0.0 dB the curve is a nearly straight diagonal line.
2. Turn the Drive knob clockwise. The knob label updates in real time and shows the value as `X.X dB`.
3. Watch the curve. As Drive increases, the shoulders of the curve begin to flatten and bend. Stop when the bend reaches the amount of saturation you want.
4. Speak into the microphone (or key a tone). The live input ball rides along the curve, showing where your signal is operating on the transfer function. Aim to keep the ball in the bent region during typical peaks.
5. If the overall level has changed noticeably, use the Output knob to compensate. See [Compensate level changes with Output](compensate-level-changes-with-output.md).

## What each control does

| Control | Default | Valid range | Persisted setting | Behavior |
|---|---|---|---|---|
| Drive | 0.0 dB | 0.0 – 24.0 dB | `ClientTubeTxDriveDb` | Pushes more signal into the tube stage. Higher values produce more curve bend and more harmonic content. |
| Transfer curve | — | — | — | Draws the current tube transfer curve. Updates immediately as Drive, Bias, or model changes. |
| Live input ball | — | — | — | Dot moves along the transfer curve at the smoothed current input level, showing the active saturation regime. |

## Tips

- The ball is smoothed with a short time constant, so brief transients will not move it to the extreme edges. Judge the operating region by watching the ball during sustained speech or tone, not instantaneous peaks.
- Drive interacts with Bias: once you have the curve bend you want, adjust Bias to shift the harmonic mix without changing the overall amount of bending. See [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md).
- If you open the floating Tube editor at the same time, both views stay in sync. Changes made in either place are reflected in the other within approximately 33 ms.

## Troubleshooting

- **The transfer curve does not bend no matter how high Drive is set** — confirm the Tube stage is enabled. A disabled stage shows the applet but does not process audio, so the curve may not respond as expected. Use the CHAIN widget to verify the stage is active. See [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md).
- **The live input ball does not move** — the ball requires an active audio engine and a live signal. Confirm the radio is connected and audio is flowing to the TX DSP chain.
- **Knob position does not match the value shown in the floating editor** — the applet syncs every 33 ms. If values appear momentarily out of step, wait one sync cycle or move either knob slightly to force an update.

## Related

- [Tube Saturator overview](overview.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)

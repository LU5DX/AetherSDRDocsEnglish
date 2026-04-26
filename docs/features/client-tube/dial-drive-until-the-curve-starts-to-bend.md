# Dial Drive until the curve starts to bend

Drive controls how hard the signal is pushed into the tube stage. Increasing it causes the transfer curve to visibly bend away from a straight line — the point where harmonic saturation begins.

## Before you start

- The Tube Saturator stage must be enabled. If the TUBE sub-container is hidden, enable the stage via the CHAIN widget or double-click the Tube stage in the CHAIN widget to open the floating Tube editor.
- Open the TUBE sub-container inside the PooDoo Audio (TXDSP) parent container. You should see the transfer curve and the five knobs below it.

## Steps

1. Locate the transfer curve at the top of the TUBE applet. At Drive 0.0 dB the curve is nearly a straight diagonal line.
2. Watch the live input ball — it moves along the curve at the current input level, showing where your signal sits on the transfer characteristic.
3. Turn the Drive knob slowly clockwise. The transfer curve begins to bend at the top and bottom as Drive increases, indicating the onset of saturation.
4. Stop when the bend is visible at the level where the live input ball rides. This is the saturation regime for your current signal level.
5. If the output level has risen noticeably, compensate using the Output knob. See [Compensate level changes with Output](compensate-level-changes-with-output.md).

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Drive | 0.0 dB | 0.0 – 24.0 dB | `ClientTubeTxDriveDb` | Pushes more signal into the tube stage. Higher values bend the curve further from linear. |
| Transfer curve | — | — | — | Draws the currently-configured tube transfer curve. Updates in real time as Drive changes. |
| Live input ball | — | — | — | Dot that rides the curve at the current input level, visualising the saturation regime. |

## Tips

- Start with Drive below 6 dB and increase slowly. The bend becomes apparent well before the maximum of 24.0 dB; heavy Drive values produce strong harmonic distortion.
- The curve shape also depends on Bias and the tube model selected in the floating editor. If the curve bends asymmetrically, Bias is non-zero — see [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md).
- Changes made in the floating Tube editor are reflected on the applet knobs within approximately 33 ms and vice versa, so you can use either to dial Drive.

## Troubleshooting

- **The transfer curve is not visible** — The TUBE sub-container is visible only when the Tube stage is enabled. Enable the stage from the CHAIN widget, then return to the TUBE applet.
- **The live input ball is stuck at the left edge** — No signal is passing through the TX chain. Verify you are transmitting or feeding audio into the TX path.
- **Turning Drive produces no audible change** — Check that Mix is above 0 %. At 0 % the fully dry signal bypasses the tube entirely. See [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md).

## Related

- [Tube Saturator overview](overview.md)
- [Shift Bias to tweak the even / odd harmonic balance](shift-bias-to-tweak-the-even-odd-harmonic-balance.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)
- [Brighten or darken the saturated signal with Tone](brighten-or-darken-the-saturated-signal-with-tone.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Bypass the tube from the chain](bypass-the-tube-from-the-chain.md)

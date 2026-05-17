# Set Floor to avoid unnatural silence between words

A fully closed gate produces complete silence, which can sound unnatural during pauses in speech. The Floor knob limits how deep the gate can cut, so background audio is reduced rather than eliminated entirely.

## Before you start

- The TX Gate or RX gate stage must be enabled in the CHAIN widget. The ClientGateApplet is hidden until the Gate stage is active.
- Open the **Aetherial TX Gate** sub-container (TX side) inside the Aetherial Audio (TXDSP) parent container, or open the floating editor by double-clicking the GATE stage in the CHAIN widget.

## Steps

1. Locate the **Floor** knob in the five-knob row at the bottom of the **Aetherial TX Gate** applet.
2. Turn **Floor** clockwise to raise the floor (less attenuation, less silence) or counter-clockwise to lower it (more attenuation, deeper cut).
3. Watch the **Gain-reduction bar** while pausing speech. The amber fill should stop growing before it reaches the floor you set — the bar will not extend beyond the Floor value.
4. Speak normally and pause. Confirm that pauses sound like reduced background rather than dead silence.

**Inline value editing:** Click any knob's displayed value to type a precise number directly. The field shows a subtle cyan border when focused. Press Enter or click elsewhere to commit the value; press Escape to cancel and revert to the previous value. Wheel-scrolling continues to work while the editor is focused.

## What each control does

| Control                | Default                                                                                                                                                                                                     | Valid range                                                                                                                                                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Floor                  | -15.0 dB                                                                                                                                                                                                    | -80.0 to 0.0 dB                                                                                                                                                                                                                                                     |
| Thresh                 | -40.0 dB                                                                                                                                                                                                    | -80.0 to 0.0 dB                                                                                                                                                                                                                                                     |
| Ratio                  | 2.0                                                                                                                                                                                                         | 1.0 to 10.0                                                                                                                                                                                                                                                         |
| Return                 | 2.0 dB                                                                                                                                                                                                      | 0.0 to 20.0 dB                                                                                                                                                                                                                                                      |
| Release                | 100 ms                                                                                                                                                                                                      | 5 to 2000 ms                                                                                                                                                                                                                                                         |
| Gain-reduction bar     | —                                                                                                                                                                                                           | 0 to 40 dB GR                                                                                                                                                                                                                                                       |
| Transfer curve         | —                                                                                                                                                                                                           | —                                                                                                                                                                                                                                                                    |

For the RX side, the equivalent persisted key is `ClientGateRxFloorDb`. The Floor knob in the **Aetherial AGC-G** applet works identically.

## Tips

- The default Floor of -15.0 dB is marked by the tick on the gain-reduction bar. If attenuation at that value still sounds abrupt, try raising Floor to -10.0 dB or -6.0 dB.
- Floor only caps the attenuation ceiling — it does not change when or how fast the gate opens or closes. If the gate is opening and closing too sharply, also adjust **Release**. See [Tune release for natural open/close](tune-release-for-natural-open-close.md).
- If the gate chatters — opening and closing rapidly on signals near the threshold — increase **Return** to widen the hysteresis deadband. The cyan band on the transfer curve grows wider as Return increases, making the sticky zone easy to judge visually.
- Setting Floor to 0.0 dB disables all attenuation, effectively bypassing the gate's effect without disabling it in the chain.
- When the Gate stage is disabled in the CHAIN widget, the entire applet tile dims to roughly half opacity. This matches the dim effect used on the EQ curve and provides a quick visual indication that the stage is bypassed without requiring you to check the CHAIN widget directly.
- The **Transfer curve** indicator shows the expander's static transfer curve with a live ball at the current input level. A soft-cyan vertical hysteresis band appears between (Thresh minus Return) and Thresh when Return is greater than 0 dB, making the gate's sticky zone visible.
- Use inline value editing to set controls with decimal precision — for example, type `2.5` for Ratio to get a 2.5:1 expansion ratio, or `12.5` for Return to set exactly 12.5 dB of hysteresis.

## Troubleshooting

- **The gain-reduction bar fills all the way regardless of Floor** — confirm you are adjusting the Floor knob on the correct side (TX or RX). The TX and RX applets have fully independent state and separate persisted keys.
- **Pauses still sound completely silent** — Floor may be set lower than -40.0 dB on the scale, or Ratio is very high (approaching 10:1), making the gate behave like a hard cut. Raise Floor toward -15.0 dB and consider lowering Ratio. See [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md).
- **Gate chatters near the threshold** — Use the **Return** knob to add hysteresis. Increase Return until the gate stays open through brief dips in the input level.
- **The applet tile looks faded or dim** — the Gate stage is bypassed in the CHAIN widget. The reduced opacity (approximately 55%) is intentional. Enable the Gate stage in the CHAIN widget to restore full brightness and DSP processing.
- **Inline editor shows unexpected decimal places** — the display adapts to the control's label format. For example, Return shows two decimal places (X.XX dB), while Floor shows one (X.X dB). Typed values are parsed using your system locale, so `12,5` works in comma-decimal regions.

## Related

- [Tune release for natural open/close](tune-release-for-natural-open-close.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
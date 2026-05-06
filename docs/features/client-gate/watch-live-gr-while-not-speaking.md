# Watch live GR while not speaking

The gain-reduction meter and transfer curve update in real time even when you are not transmitting. Watching them while the room is quiet tells you how deep the gate is cutting at any given moment, so you can judge whether your threshold and floor settings are appropriate before you key up.

## Before you start

- The Gate stage must be enabled on the side you want to observe. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the applet is not visible.
- The "Aetherial TX Gate" or "Aetherial AGC-T" sub-container must be open inside the Aetherial Audio (TXDSP) parent container.

## Steps

1. Open the applet panel if it is not already visible: `View > Applet Panel`.
2. Locate the "Aetherial TX Gate" sub-container (TX side) or "Aetherial AGC-T" sub-container (RX side).
3. Stay silent — do not speak or key the radio.
4. Watch the amber Gain-reduction bar. While input stays below the Thresh level, the bar fills from the right, showing the depth of attenuation being applied.
5. Watch the input ball on the Transfer curve. The ball sits in the lower-left region of the curve when the gate is closed (input below threshold) and moves up and to the right when the gate opens.
6. Note how far the bar fills. If it reaches or exceeds the -15 dB tick mark, the gate is applying at least 15 dB of attenuation — the default Floor value.

## Bypass dimming

When the gate stage is bypassed, the entire applet tile renders at reduced opacity (approximately 55% of full brightness). This matches the dim effect used on the EQ curve and gives an at-a-glance indication that the stage is not processing audio. The applet returns to full brightness as soon as the stage is re-enabled.

## What each control does

| Control                | Kind                                                                                                                                                                                                        | Default                                                                                                                                                                                                                                                             |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Transfer curve         | Indicator                                                                                                                                                                                                   | —                                                                                                                                                                                                                                                                   |
| Input ball             | Indicator                                                                                                                                                                                                   | —                                                                                                                                                                                                                                                                   |
| Hysteresis band        | Indicator                                                                                                                                                                                                   | —                                                                                                                                                                                                                                                                   |
| Gain-reduction bar     | Meter                                                                                                                                                                                                       | —                                                                                                                                                                                                                                                                   |
| Thresh                 | Knob                                                                                                                                                                                                        | -40.0 dB                                                                                                                                                                                                                                                            |
| Ratio                  | Knob                                                                                                                                                                                                        | 2.0                                                                                                                                                                                                                                                                 |
| Return                 | Knob                                                                                                                                                                                                        | 2.0 dB                                                                                                                                                                                                                                                              |
| Release                | Knob                                                                                                                                                                                                        | 100 ms                                                                                                                                                                                                                                                              |
| Floor                  | Knob                                                                                                                                                                                                        | -15.0 dB                                                                                                                                                                                                                                                            |
| Flip (Expander / Gate) | Unchecked = downward-expander (gentle, ratio-based). Checked = Gate (hard cut). Snaps ratio and floor to preset pairs when toggled; other knobs stay put. Label updates live between 'Expander' and 'Gate'. | Editor-only control (floating ClientGateEditor). Colour: unchecked = green (Expander), checked = amber (Gate). Tooltip: 'Flip between downward Expander (gentle) and Gate (hard) modes. Snaps ratio + floor to preset pairs; other knobs stay where you left them.' |
| Peek (lookahead)       | Sets a pre-read delay so the gate can open fractionally before a transient arrives, avoiding clipped attack edges. 'Off' disables the delay line entirely.                                                  | Editor-only control. Higher values increase latency on the TX path. 1 and 1.5 ms match Ableton's preset options; 3 and 5 ms added for very fast transients.                                                                                                         |
| Attack                 | Exponential mapping (0.1 * 1000^n). Sets how quickly the gate opens after input rises above Thresh.                                                                                                         | Editor-only control. Label 'X.XX ms' below 10 ms, 'X.X ms' above.                                                                                                                                                                                                   |
| Hold                   | Linear mapping (n * 500). After the input drops below Thresh − Return the gate stays open for this long before it begins closing, preventing flutter on rhythmic material.                                  | Editor-only control. Label 'X.X ms'.                                                                                                                                                                                                                                |

**Gain-reduction bar:** Horizontal amber strip, right-filled. Scale maxes at 40 dB. A tick at -15 dB marks the default Floor value. Empty means no attenuation; full right-fill means the gate is cutting at the maximum depth set by Floor.

**Transfer curve / Input ball:** The static curve shows the expander's input-to-output relationship. The live ball tracks the current input level, moving below or above the threshold knee in real time.

**Hysteresis band:** A soft-cyan vertical band drawn on the transfer curve between (Thresh − Return) and Thresh. It makes the gate's sticky zone visible: the gate opens when the input rises above Thresh and does not close again until the input falls below Thresh − Return. The band is absent when Return is set to 0.

**Return knob:** Sets the hysteresis deadband width in dB. Increasing Return prevents the gate from chattering when the input hovers near the threshold. The label displays in the format X.XX dB.

## Tips

- The meter updates approximately every 33 ms, so the bar tracks gain reduction closely enough to catch brief noise events.
- Knob changes made in the floating Gate editor are reflected in the applet within the same 33 ms poll cycle, so you can leave the applet visible as a live meter while tuning in the editor.
- A bar that never fully empties while you are silent means the gate is always attenuating — the input never rises above Thresh even when you stop speaking. This is normal and expected behavior for a noise gate at rest.
- If the gate chatters — opens and closes rapidly while you are speaking near the threshold — increase Return to widen the hysteresis deadband. The cyan band on the transfer curve grows wider as you do so, giving you a visual indication of how much deadband is in effect.
- If the applet tile appears dimmed, the gate stage is bypassed and no processing is active. Re-enable the stage to restore full brightness and resume attenuation.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune return / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
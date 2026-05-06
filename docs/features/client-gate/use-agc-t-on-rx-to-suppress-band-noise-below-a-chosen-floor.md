# Use AGC-T on RX to Suppress Band Noise Below a Chosen Floor

The Aetherial AGC-T (RX) applet applies a client-side downward expander to your received audio. Use it to reduce persistent band noise, QRM, or hiss between signals by attenuating audio that falls below a level you set.

## Before you start

- The Aetherial AGC-T (RX) applet is hidden until the Gate stage is enabled on the RX side. Enable it via the CHAIN widget or the floating Gate editor for the RX side first.
- The applet lives inside the Aetherial Audio (TXDSP) parent container in the Applet Panel. Open the Applet Panel if it is not visible: `View > Applet Panel`.

## Steps

1. In the Applet Panel, locate the **Aetherial AGC-T** sub-container under the Aetherial Audio (TXDSP) parent container.
2. Enable the Gate stage for the RX side using the CHAIN widget (single-click the Gate stage) or double-click the Gate stage in the CHAIN widget to open the floating **Aetherial Gate — RX** editor.
3. Watch the **Transfer curve** — the live ball moves with your incoming audio level. Note where the ball sits during band noise versus during a signal.
4. Turn the **Thresh** knob to set the level below which the gate begins attenuating. Set it just above the noise floor and below the weakest signal you want to hear. Default: -40.0 dB; range: -80.0 to 0.0 dB. This value is saved as `ClientGateRxThresholdDb`.
5. Turn the **Ratio** knob to control how aggressively audio below the threshold is cut. At 2.0:1 (default) the gate acts as a soft expander; at 10.0:1 it cuts very hard. Range: 1.0 to 10.0. Saved as `ClientGateRxRatio`.
6. Turn the **Return** knob to set the hysteresis deadband. The gate opens when input rises above Thresh and does not close again until input drops below Thresh minus the Return value. This prevents rapid chatter near the threshold. Default: 2.0 dB; range: 0.0 to 20.0 dB. Saved as `ClientGateRxReturnDb`. A soft-cyan vertical band appears on the **Transfer curve** between Thresh − Return and Thresh to make this sticky zone visible.
7. Turn the **Floor** knob to set the maximum attenuation the gate is allowed to apply. The default -15.0 dB leaves a faint residual noise rather than cutting to silence. Range: -80.0 to 0.0 dB. Saved as `ClientGateRxFloorDb`.
8. Turn the **Release** knob to control how quickly the gate closes after the input drops below Thresh minus the Return value. Default: 100 ms; range: 5 to 2000 ms. Saved as `ClientGateRxReleaseMs`. A longer release sounds more natural; a shorter release closes more tightly between signals.
9. Observe the **Gain-reduction bar** while band noise is present with no signal. The amber strip fills from the right as gain reduction is applied. The tick mark at -15 dB indicates the default Floor position. Adjust Thresh and Floor until the bar stays filled during noise and empties promptly when a signal appears.
10. When the Gate stage is bypassed, the entire applet tile dims to approximately 55 % opacity. This visual cue confirms the stage is inactive; the knob settings are preserved and take effect again as soon as you re-enable the stage.

## What each control does

| Control                | Default                                                                                                                                                                                                     | Valid range                                                                                                                                                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Thresh                 | -40.0 dB                                                                                                                                                                                                    | -80.0 to 0.0 dB                                                                                                                                                                                                                                                     |
| Ratio                  | 2.0                                                                                                                                                                                                         | 1.0 to 10.0                                                                                                                                                                                                                                                         |
| Return                 | 2.0 dB                                                                                                                                                                                                      | 0.0 to 20.0 dB                                                                                                                                                                                                                                                      |
| Release                | 100 ms                                                                                                                                                                                                      | 5 to 2000 ms                                                                                                                                                                                                                                                        |
| Floor                  | -15.0 dB                                                                                                                                                                                                    | -80.0 to 0.0 dB                                                                                                                                                                                                                                                     |
| Transfer curve         | —                                                                                                                                                                                                           | —                                                                                                                                                                                                                                                                   |
| Gain-reduction bar     | —                                                                                                                                                                                                           | 0 to 40 dB GR                                                                                                                                                                                                                                                       |
| Flip (Expander / Gate) | Unchecked = downward-expander (gentle, ratio-based). Checked = Gate (hard cut). Snaps ratio and floor to preset pairs when toggled; other knobs stay put. Label updates live between 'Expander' and 'Gate'. | Editor-only control (floating ClientGateEditor). Colour: unchecked = green (Expander), checked = amber (Gate). Tooltip: 'Flip between downward Expander (gentle) and Gate (hard) modes. Snaps ratio + floor to preset pairs; other knobs stay where you left them.' |
| Peek (lookahead)       | Sets a pre-read delay so the gate can open fractionally before a transient arrives, avoiding clipped attack edges. 'Off' disables the delay line entirely.                                                  | Editor-only control. Higher values increase latency on the TX path. 1 and 1.5 ms match Ableton's preset options; 3 and 5 ms added for very fast transients.                                                                                                         |
| Attack                 | Exponential mapping (0.1 * 1000^n). Sets how quickly the gate opens after input rises above Thresh.                                                                                                         | Editor-only control. Label 'X.XX ms' below 10 ms, 'X.X ms' above.                                                                                                                                                                                                  |
| Hold                   | Linear mapping (n * 500). After the input drops below Thresh − Return the gate stays open for this long before it begins closing, preventing flutter on rhythmic material.                                  | Editor-only control. Label 'X.X ms'.                                                                                                                                                                                                                                |

## Tips

- Start with Thresh at -40.0 dB and raise it slowly until the gain-reduction bar fills solidly during band noise but opens cleanly when a signal appears.
- Set Floor to -15.0 dB initially. Reduce it (more negative) only if the residual noise is still distracting. Avoid very low Floor values, as they can make the audio sound unnatural between signals.
- Use the **Return** knob to eliminate gate chatter on signals that hover near the threshold. Increase Return until the gate holds open cleanly through brief pauses, then test that it still closes during longer silences.
- The soft-cyan band on the **Transfer curve** gives immediate visual feedback as you adjust Return — a wider band means a larger hysteresis deadband.
- Changes made in the floating **Aetherial Gate — RX** editor and in the applet tile stay synchronized — the tile polls the engine approximately every 33 ms and updates its knobs to match.
- The AGC-T operates entirely client-side and requires no radio connection to configure.
- When the Gate stage is bypassed, the applet tile renders at reduced opacity (approximately 55 %). This matches the dim behaviour of the EQ curve when its stage is bypassed and makes it easy to see at a glance which processing stages are active.

## Troubleshooting

- **The Aetherial AGC-T applet is not visible in the Applet Panel** — The Gate stage on the RX side has not been enabled. Enable it via the CHAIN widget for the RX side. The applet is hidden until the stage is active.
- **The gain-reduction bar shows no activity even during band noise** — Thresh is set too low. The noise floor is not reaching the threshold. Raise Thresh toward 0 dB until the bar shows amber fill during noise.
- **Signals are being cut along with the noise** — Thresh is set too high. Lower Thresh so that only the noise floor triggers attenuation and desired signals open the gate.
- **The gate sounds abrupt or choppy between signals** — Increase the Release value to allow the gate to close more gradually after each signal.
- **The gate chatters rapidly near the threshold** — Increase the Return value to widen the hysteresis deadband so the gate does not reopen and reclose on signal edges near Thresh.
- **The applet tile appears dimmed and the gate is not processing audio** — The Gate stage is bypassed. The reduced-opacity tile is intentional. Re-enable the stage via the CHAIN widget to restore full processing and full opacity.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune return / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
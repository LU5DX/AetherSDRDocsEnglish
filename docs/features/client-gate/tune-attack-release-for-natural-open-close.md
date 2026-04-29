# Tune Return / Release for Natural Open/Close

Adjust the Return and Release knobs to control the gate's hysteresis deadband and how quickly it closes when audio falls below threshold. Correct settings prevent rapid chatter near the threshold and abrupt cut-offs between words.

## Before you start

- The Gate stage must be enabled on the side you want to tune (TX or RX). See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the stage is not yet active.
- Open the "Aetherial TX Gate" or "Aetherial AGC-T" sub-container inside the Aetherial Audio (TXDSP) parent container, or double-click the GATE stage in the CHAIN widget to open the floating editor for that side.
- Have audio playing or speak into the microphone so the gain-reduction bar moves while you adjust.

## Steps

1. Locate the knob row at the bottom of the applet. Find the knob labeled **Return** (third knob from the left on TX; same position on RX).
2. Turn **Return** toward the right (higher values) to widen the hysteresis deadband — the gate opens when input rises above Thresh and will not close again until input drops below Thresh − Return. Turn it left (toward 0.0 dB) to reduce the deadband so the gate closes sooner after the signal drops. The default is 2.0 dB. Valid range is 0.0 to 20.0 dB.
3. Watch the transfer curve. A soft-cyan vertical band appears between (Thresh − Return) and Thresh, showing the sticky zone. A wider band means the gate stays open across a larger signal range before closing.
4. Watch the live input ball on the transfer curve. When your signal level hovers near the threshold, the ball should sit inside the cyan band without causing the gate to chatter open and closed.
5. Locate the knob labeled **Release** (fourth knob from the left).
6. Turn **Release** toward the right (higher values) to make the gate close more slowly after audio falls below Thresh − Return — this softens the tail between words. Turn it left to close faster and cut background noise more aggressively. The default is 100 ms. Valid range is 5 to 2000 ms.
7. Speak a phrase with natural pauses and watch the gain-reduction bar. The amber fill should grow smoothly during silence and retract cleanly when speech resumes, with no pumping or sudden jumps.
8. If the gate snaps shut mid-word, increase **Release**. If background noise bleeds through between sentences, decrease **Release**.
9. If the gate chatters rapidly open and closed on signals near the threshold, increase **Return** to widen the deadband.

## What each control does

| Knob                   | Default                                                                                                                                                                                                     | Valid range                                                                                                                                                                                                                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Return                 | 2.0 dB                                                                                                                                                                                                      | 0.0 – 20.0 dB                                                                                                                                                                                                                                                       |
| Release                | 100 ms                                                                                                                                                                                                      | 5 – 2000 ms                                                                                                                                                                                                                                                         |
| Flip (Expander / Gate) | Unchecked = downward-expander (gentle, ratio-based). Checked = Gate (hard cut). Snaps ratio and floor to preset pairs when toggled; other knobs stay put. Label updates live between 'Expander' and 'Gate'. | Editor-only control (floating ClientGateEditor). Colour: unchecked = green (Expander), checked = amber (Gate). Tooltip: 'Flip between downward Expander (gentle) and Gate (hard) modes. Snaps ratio + floor to preset pairs; other knobs stay where you left them.' |
| Peek (lookahead)       | Sets a pre-read delay so the gate can open fractionally before a transient arrives, avoiding clipped attack edges. 'Off' disables the delay line entirely.                                                  | Editor-only control. Higher values increase latency on the TX path. 1 and 1.5 ms match Ableton's preset options; 3 and 5 ms added for very fast transients.                                                                                                         |
| Attack                 | Exponential mapping (0.1 * 1000^n). Sets how quickly the gate opens after input rises above Thresh.                                                                                                         | Editor-only control. Label 'X.XX ms' below 10 ms, 'X.X ms' above.                                                                                                                                                                                                   |
| Hold                   | Linear mapping (n * 500). After the input drops below Thresh − Return the gate stays open for this long before it begins closing, preventing flutter on rhythmic material.                                  | Editor-only control. Label 'X.X ms'.                                                                                                                                                                                                                                |
## Tips

- The gain-reduction bar maxes at 40 dB and the tick mark at the −15 dB position corresponds to the default Floor value. Use this tick as a visual reference: if the amber fill rarely reaches the tick, your Floor setting is the governing limit, not the ratio or timing.
- Changes made in the docked applet knobs and the floating editor are kept in sync automatically. You do not need to reopen either view after adjusting one.
- For SSB voice, a Release of 150–300 ms typically avoids the gate closing during brief inter-word pauses. For CW audio tones, a much shorter Release (10–30 ms) gives a cleaner result.
- If the cyan hysteresis band disappears, Return is set to 0.0 dB and the gate has no deadband. Any signal that dips below Thresh will immediately start the closing sequence.

## Troubleshooting

- **Gate chatters or flutters between open and closed** — Release is too short, or Return is too narrow. Increase **Return** so the gate stays open across small signal fluctuations near the threshold, or increase **Release** to slow the closing time.
- **Gate stays open too long after speech ends** — Return is too wide or Release is too long. Reduce **Return** so the gate closes sooner after the signal drops, or turn **Release** left to shorten the tail.
- **Background noise audible between words** — Release is too long. Turn **Release** left to shorten the tail. Also verify that **Floor** is set to a sufficiently negative value to attenuate noise while closed.
- **Knob position does not match what was set in the floating editor** — The applet syncs from the engine approximately every 33 ms. Wait one moment; the knob position will update to reflect the current engine value.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
# Tune Attack / Release for Natural Open/Close

Adjust the Attack and Release knobs to control how quickly the gate opens when you speak and how quickly it closes when you stop. Correct timing prevents clipped syllable starts and abrupt cut-offs between words.

## Before you start

- The Gate stage must be enabled on the side you want to tune (TX or RX). See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the stage is not yet active.
- Open the "Aetherial TX Gate" or "Aetherial AGC-T" sub-container inside the Aetherial Audio (TXDSP) parent container, or double-click the GATE stage in the CHAIN widget to open the floating editor for that side.
- Have audio playing or speak into the microphone so the gain-reduction bar moves while you adjust.

## Steps

1. Locate the knob row at the bottom of the applet. Find the knob labeled **Attack** (third knob from the left on TX; same position on RX).
2. Turn **Attack** toward the left (lower values) to make the gate open faster on loud transients; turn it right (higher values) to slow the opening and smooth abrupt entries. The default is 0.5 ms. Valid range is 0.1 to 100.0 ms.
3. Watch the transfer curve's live input ball. When you start speaking, the ball should move above the threshold and the gain-reduction bar should clear promptly without a clipped leading edge.
4. Locate the knob labeled **Release** (fourth knob from the left).
5. Turn **Release** toward the right (higher values) to make the gate close more slowly after audio falls below threshold — this softens the tail between words. Turn it left to close faster and cut background noise more aggressively. The default is 100 ms. Valid range is 5 to 2000 ms.
6. Speak a phrase with natural pauses and watch the gain-reduction bar. The amber fill should grow smoothly during silence and retract cleanly when speech resumes, with no pumping or sudden jumps.
7. If the gate snaps shut mid-word, increase **Release**. If background noise bleeds through between sentences, decrease **Release**.
8. If the first syllable of each word is attenuated, decrease **Attack**. If the gate chatters open on breath noise before speech, increase **Attack**.

## What each control does

| Knob | Default | Valid range | Persisted key (TX / RX) | Behavior |
|---|---|---|---|---|
| Attack | 0.5 ms | 0.1 – 100.0 ms | `ClientGateTxAttackMs` / `ClientGateRxAttackMs` | Sets how quickly the gate opens when input rises above threshold. Uses exponential mapping. |
| Release | 100 ms | 5 – 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` | Sets how quickly the gate closes after input falls below threshold. Uses exponential mapping. |

## Tips

- The gain-reduction bar maxes at 40 dB and the tick mark at the −15 dB position corresponds to the default Floor value. Use this tick as a visual reference: if the amber fill rarely reaches the tick, your Floor setting is the governing limit, not the ratio or timing.
- Changes made in the docked applet knobs and the floating editor are kept in sync automatically. You do not need to reopen either view after adjusting one.
- For SSB voice, a Release of 150–300 ms typically avoids the gate closing during brief inter-word pauses. For CW audio tones, a much shorter Release (10–30 ms) gives a cleaner result.

## Troubleshooting

- **First syllable of each word is cut off** — Attack is too slow. Turn the **Attack** knob left toward 0.1 ms so the gate opens before the transient passes.
- **Gate chatters or flutters between open and closed** — Release is too short, or Thresh is set near the signal level. Increase **Release** or lower **Thresh** slightly so the gate does not re-trigger on breath and room noise.
- **Background noise audible between words** — Release is too long. Turn **Release** left to shorten the tail. Also verify that **Floor** is set to a sufficiently negative value to attenuate noise while closed.
- **Knob position does not match what was set in the floating editor** — The applet syncs from the engine approximately every 33 ms. Wait one moment; the knob position will update to reflect the current engine value.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)

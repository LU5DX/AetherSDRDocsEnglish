# Tune Attack / Release for Natural Open/Close

Attack and Release control how quickly the gate opens when your voice crosses the threshold and how quickly it closes when it falls back below. Getting these right eliminates the clipped first syllable (Attack too slow) and the abrupt chop after each word (Release too fast) that make gating sound unnatural.

## Before you start

- The gate must be enabled on the side you want to adjust (TX or RX). See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) to confirm the gate stage is active.
- Open the Aetherial TX Gate (TX side) or Aetherial AGC-T (RX side) sub-container inside the Aetherial Audio (TXDSP) parent container in the applet panel. If the sub-container is not visible, double-click the GATE stage in the CHAIN widget on the matching side to open the floating gate editor.

## Steps

1. Locate the **Attack** knob in the five-knob row at the bottom of the applet.
2. Turn **Attack** left to open faster (minimum 0.1 ms) or right to open slower (maximum 100.0 ms). The default is 0.50 ms. For most voice work, values between 0.5 ms and 5 ms avoid clipping the leading edge of consonants.
3. Speak normally and watch the transfer curve's input ball and the amber gain-reduction bar. If the bar shows a brief spike of gain reduction at the very start of each word, Attack is too slow — turn it left.
4. Locate the **Release** knob in the same row.
5. Turn **Release** left to close faster (minimum 5 ms) or right to close slower (maximum 2000 ms). The default is 100 ms. For natural speech, values between 80 ms and 400 ms let the gate trail off rather than cut abruptly.
6. Pause speaking and watch the gain-reduction bar. If the bar fills rapidly and the signal cuts off unnaturally between words, increase Release (turn right). If background noise bleeds back in during pauses, decrease Release (turn left).
7. Repeat steps 2–6 until pauses sound natural and the gate opens cleanly on the first syllable.

## What each control does

| Control | Default | Valid range | Persisted setting (TX / RX) |
|---|---|---|---|
| **Attack** | 0.50 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` / `ClientGateRxAttackMs` |
| **Release** | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` |

Attack uses exponential knob mapping (0.1 × 1000^n). Release uses exponential knob mapping (5 × 400^n). Both knobs save immediately; changes persist across restarts and are shared between the applet knobs and the floating editor.

The gain-reduction bar shows 0 to 40 dB of attenuation as an amber right-filled strip. A tick mark at −15 dB corresponds to the default **Floor** value. Use this bar as a live guide: a clean release will show the bar growing smoothly during pauses rather than snapping to full scale.

## Tips

- Attack and Release interact with **Thresh** and **Ratio**. A harder ratio (higher value) makes timing errors more audible — consider dialing ratio back toward 2.0:1 while tuning attack/release, then tighten ratio once timing feels right.
- Knob changes made in the floating gate editor and in the applet tile stay in sync automatically; you do not need to close the editor to see updated values in the applet.
- The input ball on the transfer curve moves to show whether the gate is currently open (ball above threshold line) or closed (ball below). Watch it during natural speech to confirm the gate is tracking correctly.

## Troubleshooting

- **First syllable of each word is clipped or quiet** — Attack is too slow. Turn the **Attack** knob left toward 0.1 ms until the gate opens before the syllable is lost.
- **Gate closes too quickly, chopping the end of words** — Release is too short. Turn the **Release** knob right. Start around 150–200 ms for voice.
- **Background noise audible between words** — Release is too long, or **Thresh** is set below the noise floor. Shorten Release and/or raise Thresh. See [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md).
- **Knob value in the applet does not match the floating editor** — Wait one meter tick (approximately 33 ms); the applet syncs knob positions from the engine on each tick and will update automatically.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)

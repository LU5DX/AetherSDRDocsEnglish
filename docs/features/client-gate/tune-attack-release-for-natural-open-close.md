# Tune Attack / Release for Natural Open/Close

Adjust how quickly the noise gate opens when you start speaking and closes when you stop. Correct attack and release times prevent clipping the first syllable of a word and avoid an abrupt, unnatural chop between words.

## Before you start

- The Gate stage must be enabled. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the stage is currently bypassed.
- Open the GATE applet: locate the GATE sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel. If it is not visible, double-click the Gate stage in the CHAIN widget to open the floating Gate editor, or right-click the GATE sub-container titlebar and choose to show it.
- Have a microphone connected and audio passing so the transfer curve's input ball and the Gain-reduction bar react in real time while you adjust.

## Steps

1. Watch the Gain-reduction bar while speaking normally. The amber strip should fill briefly on loud audio and drain between words. If the gate is cutting the front of each word, the Attack is too slow; if it snaps shut mid-breath with an audible click, the Release is too fast.
2. To fix clipped word starts, turn the **Attack** knob left (lower value). The default is 0.50 ms. For most voice work, values between 0.1 ms and 2.0 ms open fast enough to preserve consonants.
3. To fix an abrupt or chattering close, turn the **Release** knob right (higher value). The default is 100 ms. A value of 150–300 ms allows the gate to hold open across natural pauses without snapping shut between syllables.
4. Speak a sentence and observe the input ball on the transfer curve. The ball should cross the threshold line cleanly as each word begins, with no visible stall at the threshold.
5. Watch the Gain-reduction bar drain smoothly after each word. If the amber strip lingers too long or causes a pumping effect, reduce Release toward 50–100 ms.
6. Repeat steps 2–5 until open and close feel transparent during normal speech.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Attack** | 0.50 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` | Sets how quickly the gate opens when input rises above the threshold. Exponential knob scale. Label shows `X.XX ms` below 10 ms, `X.X ms` above. |
| **Release** | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | Sets how quickly the gate closes after input falls below the threshold. Exponential knob scale. Label shows `X.X ms` below 100 ms, `X ms` above. |
| **Gain-reduction bar** | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Shows depth of attenuation while the gate is closed. The tick mark at −15 dB corresponds to the default Floor value. |
| **Transfer curve** | — | — | — | Plots the static transfer curve with a live input ball. Ball position shows whether the gate is currently above or below threshold. |

## Tips

- Attack and Release use exponential knob scaling, so small movements near the low end of the range produce larger changes in milliseconds than the same movement near the high end. Make small adjustments and re-test after each one.
- If the gate chatters rapidly — opening and closing multiple times per word — increase Release first. If that alone is not enough, also raise the **Thresh** knob slightly so borderline-level audio does not repeatedly cross the threshold boundary.
- The Gain-reduction bar and input ball update approximately every 33 ms. Watch both while speaking a passage that represents your worst-case noise situation, not just isolated words.
- Changes take effect immediately and are saved automatically. No separate save step is required.

## Troubleshooting

- **First consonant of each word is cut off** — Attack is too slow. Lower Attack toward 0.1 ms.
- **Gate closes audibly between syllables within a single word** — Release is too short. Raise Release to 150 ms or higher and re-test.
- **Gate chatters open and closed rapidly** — The input level is hovering near the threshold. Increase Release to at least 200 ms, or raise Thresh slightly so marginal levels do not trigger the gate. See [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md).
- **Gain-reduction bar never moves** — The Gate stage may be bypassed or disabled. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- **Knob values do not match what is shown in the floating Gate editor** — The applet syncs from the engine approximately every 33 ms. Wait one moment; values should reconcile automatically.

## Related

- [Noise Gate / Expander overview](overview.md)
- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)

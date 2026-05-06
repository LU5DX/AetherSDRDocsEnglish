# Tune Release for Natural Gate Close

The Release knob controls how quickly the gate closes after audio drops below the threshold. Setting it correctly prevents the gate from cutting off word endings too abruptly or leaving the gate open so long that background noise bleeds through between words.

## Before you start

- The gate stage must be enabled on the TX or RX side. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the gate is currently bypassed. When the gate stage is bypassed, the entire applet tile dims to approximately 55% opacity — this is normal and indicates the DSP stage is inactive.
- Open the Aetherial TX Gate or Aetherial AGC-T applet so the knobs are visible. The applet appears inside the Aetherial Audio (TXDSP) parent container once the gate stage is active.

## Steps

1. Locate the **Release** knob in the five-knob row at the bottom of the applet. It is the fourth knob from the left, between **Return** and **Floor**.
2. Turn **Release** clockwise to increase the release time (slower close) or counter-clockwise to decrease it (faster close). The knob label updates live, showing the current value in milliseconds — formatted as `X.X ms` below 100 ms and `X ms` at 100 ms and above.
3. Speak or pass audio through the gate while watching the gain-reduction bar. After audio drops below the threshold, observe how quickly the amber strip rises to full attenuation. Adjust **Release** until the gate closes smoothly without clipping word endings.
4. If the gate closes so slowly that noise is audible between words, reduce **Release**. If word endings are cut off, increase **Release**.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|
| **Release** | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` |

The knob uses an exponential mapping (5 × 400^n), so small movements at the low end of the range produce finer timing adjustments, while the upper range covers long, gradual fade-outs. Release begins only after the input has fallen below Thresh − Return; the **Return** value therefore affects when the release phase starts.

## Tips

- 100 ms (the default) suits most voice TX work. Increase toward 200–400 ms if consonants at the end of words are being clipped. Decrease toward 20–50 ms if background noise is audible in the gaps between words.
- Release interacts with **Return**: a larger Return deadband delays the start of the release phase. If the gate seems to hang open, check **Return** before shortening **Release** further.
- The gain-reduction bar updates approximately every 33 ms. Watch it in real time while adjusting **Release** to confirm the close speed before transmitting.
- Changes take effect immediately and are saved automatically. No radio connection is required to adjust this setting.
- If the applet tile appears dimmed, the gate stage is bypassed and no processing is occurring. Re-enable the stage before making adjustments. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).

## Related

- [Set Return to prevent gate chatter near threshold](set-return-to-prevent-gate-chatter-near-threshold.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
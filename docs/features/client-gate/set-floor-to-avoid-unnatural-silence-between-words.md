# Set Floor to avoid unnatural silence between words

The Floor knob limits how deeply the gate can attenuate your audio. Without a floor, a hard gate cuts completely to silence between words, which sounds unnatural on voice. Setting a moderate floor lets a small amount of audio through while the gate is closed, preserving the feel of a live transmission.

## Before you start

- The Gate stage must be enabled. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) to confirm the stage is active.
- Open the GATE applet: it is the sub-container labeled GATE inside the PooDoo Audio (TXDSP) parent container. If it is not visible, double-click the Gate stage in the CHAIN widget to open the floating Gate editor, or right-click the GATE sub-container titlebar and select the appropriate option.

## Steps

1. Locate the Floor knob in the five-knob row at the bottom of the GATE applet. It is the rightmost knob, labeled "Floor".
2. Watch the Gain-reduction bar while you pause speaking. The amber fill shows how much attenuation the gate is currently applying. The tick mark at the -15 dB position marks the default floor.
3. Turn the Floor knob clockwise (toward 0 dB) to reduce the maximum attenuation, allowing more audio through when the gate is closed.
4. Turn the Floor knob counter-clockwise (toward -80 dB) to increase the maximum attenuation, cutting more deeply between words.
5. Speak normally and pause deliberately. Adjust until the transitions between words sound natural rather than abruptly silent or unnaturally quiet.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Floor | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate is allowed to apply. Higher (closer to 0 dB) values let more audio through when the gate is closed. Lower values cut more deeply. |
| Gain-reduction bar | — | 0 to 40 dB GR | — | Horizontal amber strip, right-filled. Shows the depth of attenuation while the gate is closed. The tick at -15 dB marks the default floor position. |

## Tips

- The default Floor of -15.0 dB is intentionally moderate. It keeps a faint residual signal present between words, which most listeners find more natural than complete silence.
- If you are using a low Ratio (soft expander behavior), the gate may never reach the Floor even at full attenuation — the Floor only caps the maximum, it does not set a target.
- The transfer curve in the GATE applet updates to reflect your Floor setting. Watch the curve's lower plateau while adjusting to see the effect visually alongside the live input ball.
- Changes are saved immediately. The Floor value persists across restarts via `ClientGateTxFloorDb`.

## Troubleshooting

- **Audio cuts to complete silence between words despite a high Floor value** — Confirm the gate stage is not bypassed. Check the Gain-reduction bar: if it shows full amber fill reaching the right edge, the gate is applying maximum attenuation. Raise Floor (closer to 0 dB) and monitor the bar to confirm it limits the fill.
- **Floor knob has no audible effect** — The gate may not be triggering. If the input ball on the transfer curve stays above threshold, the gate is open and Floor is not being applied. Lower Thresh so the gate actually closes between words.

## Related

- [Noise Gate / Expander overview](overview.md)
- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)

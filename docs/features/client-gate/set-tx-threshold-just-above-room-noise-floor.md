# Set TX threshold just above room noise floor

Setting Thresh correctly tells the TX gate where your room's background noise ends and your voice begins. A threshold just above the noise floor keeps mic hiss and ambient sound silent between transmissions while letting your voice through cleanly.

## Before you start

- The TX gate stage must be enabled in the CHAIN widget on the TX side. If it is not enabled, the applet is hidden and knob changes have no effect. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- Open the "Aetherial TX Gate" sub-container inside the Aetherial Audio (TXDSP) parent container, or double-click the GATE stage in the CHAIN widget to open the floating "Aetherial Gate — TX" editor.

## Steps

1. Put on your headphones and set the room to its normal ambient conditions — fan running, computer noise present, whatever is typical when you operate.
2. Do not speak. Watch the live input ball on the Transfer curve. The ball shows where your room noise sits on the input axis.
3. Watch the Gain-reduction bar. If the bar shows no amber fill while you are silent, Thresh is already below your noise floor and the gate is not closing — raise Thresh.
4. Turn the Thresh knob slowly clockwise until the amber Gain-reduction bar begins to fill consistently while you are silent. This is the noise floor.
5. Back Thresh off by 2–3 dB so the gate closes firmly on noise without clipping the leading edge of your voice. The input ball should sit clearly below the threshold line when you are silent.
6. Speak at normal volume. Confirm the Gain-reduction bar drops to zero (no fill) immediately when you start talking, indicating the gate has opened.
7. Return to silence. Confirm the amber fill returns promptly. If the gate is slow to close, reduce Release. See [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md).

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate starts attenuating. Set this just above the room noise floor. |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` | Higher values produce a harder cut; lower values produce a softer downward expansion. |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` | How quickly the gate opens when input rises above Thresh. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | How quickly the gate closes after input falls below Thresh. |
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate may apply. Prevents complete silence between words. |

The Transfer curve plots the static input/output relationship and shows a live input ball at the current signal level. The Gain-reduction bar is an amber horizontal strip, right-filled, scaled 0 to 40 dB; a tick marks the −15 dB default Floor position.

## Tips

- Set Thresh during your worst-case noise condition (loudest fan, most background activity). A threshold calibrated to a quiet room will let noise through when conditions change.
- If the gate chops the start of words, lower Attack or reduce Thresh by 1–2 dB so the gate opens faster or triggers earlier.
- The Gain-reduction bar and the input ball update live at approximately 30 Hz, so short noise bursts will be visible even if brief.
- Changes to any knob are saved immediately and survive a restart. You do not need to confirm or apply separately.

## Troubleshooting

- **The applet is not visible** — The GATE stage is not enabled. Single-click the GATE stage in the CHAIN widget to enable it, or double-click to open the floating editor and enable it there.
- **The Gain-reduction bar never fills while silent** — Thresh is set below the noise floor. Raise Thresh until consistent amber fill appears during silence.
- **The gate chops the beginning of words** — Thresh is too close to your voice level, or Attack is too slow. Lower Thresh slightly or reduce the Attack value.
- **The gate does not close between words** — Thresh is too low for the current noise floor. Raise Thresh until the bar fills reliably during pauses.

## Related

- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)

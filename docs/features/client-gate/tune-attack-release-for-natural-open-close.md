# Tune Attack / Release for Natural Open/Close

Adjust how quickly the noise gate opens when you start speaking and closes when you stop. Correct attack and release times prevent the gate from clipping the front edge of words or leaving an audible chop at the end of each transmission.

## Before you start

- The GATE applet must be visible in the applet panel. It appears as a sub-container inside the PooDoo Audio (TXDSP) parent container. If it is hidden, enable the Gate stage via the CHAIN widget or double-click the Gate stage in the CHAIN widget to open the floating Gate editor.
- The gate must be enabled. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the gate is currently bypassed.
- Set a working threshold before tuning timing. See [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md).

## Steps

1. Open the GATE applet inside the PooDoo Audio (TXDSP) container. The five knobs — Thresh, Ratio, Attack, Release, Floor — appear in a row below the transfer curve and gain-reduction bar.
2. Key the mic and speak normally while watching the Gain-reduction bar. The amber strip collapses to the left as the gate opens and fills to the right as it closes.
3. Turn the Attack knob while speaking. Lower values open the gate faster; raise the value if the gate opens too abruptly and causes audible pumping on loud signals. The label shows the current value in milliseconds (for example, `0.50 ms`).
4. Pause between words and watch the Gain-reduction bar refill. Turn the Release knob to control how quickly the gate closes after your voice drops below threshold. Shorter values close the gate quickly; longer values let the tail of each word decay naturally before attenuation begins.
5. Repeat steps 3 and 4 until speech passes through cleanly with no clipped consonants on opening and no abrupt chop on closing.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` | Sets how quickly the gate opens when input rises above threshold. Mapped exponentially: turning from minimum to maximum covers 0.1 ms through 100.0 ms. |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` | Sets how quickly the gate closes after input falls below threshold. Mapped exponentially: turning from minimum to maximum covers 5 ms through 2000 ms. |
| Thresh | -40.0 dB | -80.0 to 0.0 dB | `ClientGateTxThresholdDb` | Level below which the gate begins attenuating. Affects when the Attack and Release timing is triggered. |
| Floor | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` | Maximum attenuation the gate applies when closed. Does not affect timing, but limits how deep the gate cuts during the release phase. |

## Tips

- Start with Attack at the default (0.5 ms) and adjust Release first. Release has the greater effect on perceived naturalness.
- If the front of words sounds cut off, increase Attack slightly (try 2–5 ms) so the gate has time to open before the transient arrives.
- If you hear the gate chatter — rapidly opening and closing — increase Release to smooth out brief pauses within a word.
- The live ball on the transfer curve shows whether the gate is currently above or below threshold. Watch it track your speech to confirm timing changes are taking effect.
- Attack and Release knobs sync bidirectionally with the floating Gate editor. Changes made in either view are reflected immediately in the other.

## Troubleshooting

- **Front consonants are cut off** — Attack is too fast relative to the signal rise time, or Thresh is set too high. Lower Thresh slightly or increase Attack (try 2–10 ms) to allow the gate to open before the transient.
- **Gate closes abruptly mid-word during normal pauses** — Release is too short. Increase Release toward 200–500 ms to let short gaps pass without closing.
- **Gate does not close between words** — Release may be very long, or Thresh is set below the room noise floor. Check Thresh first (see [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)), then reduce Release.
- **Gain-reduction bar does not move** — The gate may be bypassed or the audio engine is not connected. Confirm the Gate stage is active in the CHAIN widget.

## Related

- [Set threshold just above room noise floor](set-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)

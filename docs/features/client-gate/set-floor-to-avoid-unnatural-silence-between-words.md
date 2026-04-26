# Set Floor to avoid unnatural silence between words

The **Floor** knob sets the maximum attenuation the gate is allowed to apply when it closes. Raising Floor above its default keeps a small amount of audio passing during pauses, which prevents the unnatural dead silence that a hard cut produces between words or phrases.

## Before you start

- The TX gate must be enabled. The "Aetherial TX Gate" sub-container is hidden until the Gate stage is active — see [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- Open the "Aetherial TX Gate" sub-container inside the Aetherial Audio (TXDSP) parent container, or double-click the GATE stage in the CHAIN widget to open the floating "Aetherial Gate — TX" editor.

## Steps

1. Locate the **Floor** knob — the rightmost of the five knobs below the transfer curve.
2. Turn **Floor** clockwise (toward 0 dB) to reduce the depth of attenuation. The gate will cut audio only as far as the Floor value when it closes.
3. Watch the Gain-reduction bar while you pause speaking. The amber fill should stop growing at the point that corresponds to your Floor setting. A tick mark on the bar indicates −15.0 dB, which is the default.
4. Speak a sentence, then pause. Adjust **Floor** until pauses sound natural — present but quiet, not silent.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|
| Floor | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` / `ClientGateRxFloorDb` |
| Thresh | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` / `ClientGateRxThresholdDb` |
| Ratio | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` / `ClientGateRxRatio` |
| Attack | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` / `ClientGateRxAttackMs` |
| Release | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` |
| Gain-reduction bar | — | 0 to 40 dB GR displayed | — |

Floor controls the maximum attenuation applied when the gate is closed. At −80.0 dB the gate can cut almost completely; at 0 dB the gate applies no attenuation at all, effectively bypassing the gain-reduction action.

The Gain-reduction bar fills amber from the right. The tick at −15 dB marks the default Floor position. When Floor is set shallower than −15 dB, the amber fill will stop before the tick during normal pauses.

## Tips

- A Floor value between −20.0 dB and −10.0 dB is a practical starting range for most microphones. Start at the default −15.0 dB and adjust by ear.
- If room noise is audible during pauses even with Floor raised, lower **Thresh** so the gate closes only on genuine silence, then bring Floor back up to control the residual level. See [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md).
- The same Floor knob and `ClientGateRxFloorDb` setting exist on the RX side ("Aetherial AGC-T"). Adjusting Floor there controls how much band noise is allowed through during quiet periods on receive. See [Use AGC-T on RX to suppress band noise below a chosen floor](use-agc-t-on-rx-to-suppress-band-noise-below-a-chosen-floor.md).
- Changes take effect immediately and are saved automatically. No Apply or OK button is required.

## Troubleshooting

- **Pauses still sound completely silent after raising Floor** — confirm the gate is not also being overridden by a very high Ratio. A Ratio near 10:1 acts as a hard gate regardless of Floor. Lower Ratio toward 2.0:1 for softer behavior. See [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md).
- **The Floor knob has no effect** — the gate stage may be bypassed. Check the CHAIN widget and re-enable the Gate stage if it is greyed out. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- **Gain-reduction bar fills all the way during pauses despite a raised Floor** — the bar displays raw gain-reduction signal from the engine; if Floor is set but the bar still reads maximum, verify that the correct side (TX vs. RX) is being adjusted.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)
- [Use AGC-T on RX to suppress band noise below a chosen floor](use-agc-t-on-rx-to-suppress-band-noise-below-a-chosen-floor.md)

# Watch live GR while not speaking

The gain-reduction meter and transfer curve update in real time even when you are not transmitting. Watching them while the room is quiet tells you how deep the gate is cutting at any given moment, so you can judge whether your threshold and floor settings are appropriate before you key up.

## Before you start

- The Gate stage must be enabled on the side you want to observe. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the applet is not visible.
- The "Aetherial TX Gate" or "Aetherial AGC-T" sub-container must be open inside the Aetherial Audio (TXDSP) parent container.

## Steps

1. Open the applet panel if it is not already visible: `View > Applet Panel`.
2. Locate the "Aetherial TX Gate" sub-container (TX side) or "Aetherial AGC-T" sub-container (RX side).
3. Stay silent — do not speak or key the radio.
4. Watch the amber Gain-reduction bar. While input stays below the Thresh level, the bar fills from the right, showing the depth of attenuation being applied.
5. Watch the input ball on the Transfer curve. The ball sits in the lower-left region of the curve when the gate is closed (input below threshold) and moves up and to the right when the gate opens.
6. Note how far the bar fills. If it reaches or exceeds the -15 dB tick mark, the gate is applying at least 15 dB of attenuation — the default Floor value.

## What each control does

| Control | Kind | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|---|
| Transfer curve | Indicator | — | — | — |
| Input ball | Indicator | — | Below threshold / above threshold | — |
| Gain-reduction bar | Meter | — | 0 to 40 dB GR | — |
| Thresh | Knob | -40.0 dB | -80.0 to 0.0 dB | `ClientGateTxThresholdDb` / `ClientGateRxThresholdDb` |
| Ratio | Knob | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` / `ClientGateRxRatio` |
| Attack | Knob | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` / `ClientGateRxAttackMs` |
| Release | Knob | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` |
| Floor | Knob | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` / `ClientGateRxFloorDb` |

**Gain-reduction bar:** Horizontal amber strip, right-filled. Scale maxes at 40 dB. A tick at -15 dB marks the default Floor value. Empty means no attenuation; full right-fill means the gate is cutting at the maximum depth set by Floor.

**Transfer curve / Input ball:** The static curve shows the expander's input-to-output relationship. The live ball tracks the current input level, moving below or above the threshold knee in real time.

## Tips

- The meter updates approximately every 33 ms, so the bar tracks gain reduction closely enough to catch brief noise events.
- Knob changes made in the floating Gate editor are reflected in the applet within the same 33 ms poll cycle, so you can leave the applet visible as a live meter while tuning in the editor.
- A bar that never fully empties while you are silent means the gate is always attenuating — the input never rises above Thresh even when you stop speaking. This is normal and expected behavior for a noise gate at rest.

## Related

- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)

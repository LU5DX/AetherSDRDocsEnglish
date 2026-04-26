# Watch Live GR While Not Speaking

Use this page to read the gain-reduction (GR) display on the ClientGateApplet while the gate is idle — that is, while no audio is crossing the threshold. This lets you confirm that the gate is closing correctly and judge how much attenuation it is applying between words or during band noise.

## Before you start

- The Gate stage must be enabled on at least one side (TX or RX). The applet is hidden until the Gate stage is enabled via the CHAIN widget or the floating editor. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md) if the applet is not visible.
- AetherSDR must be connected to audio (a radio connection is not required for the display to animate, but audio must be flowing for the GR meter to show meaningful readings).

## Steps

1. Locate the **Aetherial TX Gate** sub-container (TX side) or the **Aetherial AGC-T** sub-container (RX side) inside the Aetherial Audio (TXDSP) parent container in the applet panel.
2. Stop speaking, or wait for a quiet moment on the band.
3. Watch the **Gain-reduction bar** — the horizontal amber strip at the top of the applet, just below the transfer curve. When the gate is closed, the strip fills from the right toward the left in amber.
4. Watch the **Input ball** on the transfer curve. When the ball sits below the threshold point on the curve, the gate is closed and the amber fill on the **Gain-reduction bar** shows the depth of attenuation being applied.
5. Note the tick mark on the **Gain-reduction bar**. The tick at −15 dB marks the soft-expander default floor. If the amber fill reaches or passes that tick, the gate is attenuating at or beyond the default Floor value.

## What each control does

| Control | Kind | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|---|
| Transfer curve | Indicator | — | — | — |
| Gain-reduction bar | Meter | — | 0 to 40 dB GR | — |
| Input ball | Indicator | — | Below / above threshold | — |
| Thresh | Knob | −40.0 dB | −80.0 to 0.0 dB | `ClientGateTxThresholdDb` / `ClientGateRxThresholdDb` |
| Ratio | Knob | 2.0:1 | 1.0 to 10.0 | `ClientGateTxRatio` / `ClientGateRxRatio` |
| Attack | Knob | 0.5 ms | 0.1 to 100.0 ms | `ClientGateTxAttackMs` / `ClientGateRxAttackMs` |
| Release | Knob | 100 ms | 5 to 2000 ms | `ClientGateTxReleaseMs` / `ClientGateRxReleaseMs` |
| Floor | Knob | −15.0 dB | −80.0 to 0.0 dB | `ClientGateTxFloorDb` / `ClientGateRxFloorDb` |

The **Gain-reduction bar** scale maxes at 40 dB. The tick at −15 dB corresponds to the default Floor value.

## Tips

- The meter updates approximately every 33 ms. Fast transients may not be fully visible, but steady-state attenuation during silence reads accurately.
- If you have the floating editor open at the same time, the knob values in both views stay in sync automatically. You can adjust Thresh or Floor in the editor and watch the **Gain-reduction bar** in the applet respond without switching windows.
- To see how deeply the gate cuts, temporarily lower Thresh far below your noise floor — the amber fill should reach near full scale. Restore Thresh when done.

## Troubleshooting

- **Gain-reduction bar stays empty even when not speaking** — The gate may not be enabled, or the Thresh knob is set lower than your noise floor so the gate never closes. Raise Thresh until it sits just above the noise floor. See [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md).
- **Amber fill reaches full scale and audio sounds cut off** — The Floor knob is set too low (large negative value), applying more attenuation than intended. Raise Floor toward −15.0 dB. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).
- **Applet is not visible** — The Gate stage is not enabled. Enable it via the CHAIN widget on the matching TX or RX side. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Choose gate vs soft-expander behaviour via ratio](choose-gate-vs-soft-expander-behaviour-via-ratio.md)
- [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md)

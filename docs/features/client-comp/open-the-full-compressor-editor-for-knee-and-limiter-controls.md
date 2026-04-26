# Open the Full Compressor Editor for Knee and Limiter Controls

The applet tile exposes five knobs — Thresh, Ratio, Attack, Release, and Makeup — but the knee width and limiter controls are only available in the floating editor. This page explains how to open that editor for either the TX or RX compressor.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel.
- The COMP stage must exist in the CHAIN widget for the side you want to edit (TX or RX).

## Steps

1. Locate the CHAIN widget for the side you want to edit — TX or RX.
2. Double-click the COMP stage in the CHAIN widget.
   - For the TX side, this opens the floating editor titled **Aetherial Compressor — TX**.
   - For the RX side, this opens the floating editor titled **Aetherial Compressor — RX**.
3. Use the controls in the floating editor to adjust knee and limiter settings. The editor contains all controls from the applet tile plus the knee and limiter sections not available in the tile.

## What each control does

The floating editor includes the five knobs shared with the applet tile plus two additional sections: knee and limiter. All values are persisted per side.

### TX side

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Thresh | -18.0 dB | -60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` |
| Makeup | 0.0 dB | -12.0 to 24.0 dB | `ClientCompTxMakeupDb` |
| Knee | — | — | `ClientCompTxKneeDb` |
| Limiter enabled | — | — | `ClientCompTxLimEnabled` |
| Limiter ceiling | — | — | `ClientCompTxLimCeilingDb` |

### RX side

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Thresh | -18.0 dB | -60.0 to 0.0 dB | `ClientCompRxThresholdDb` |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompRxRatio` |
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompRxAttackMs` |
| Release | 200 ms | 5 to 2000 ms | `ClientCompRxReleaseMs` |
| Makeup | 0.0 dB | -12.0 to 24.0 dB | `ClientCompRxMakeupDb` |
| Knee | — | — | `ClientCompRxKneeDb` |
| Limiter enabled | — | — | `ClientCompRxLimEnabled` |
| Limiter ceiling | — | — | `ClientCompRxLimCeilingDb` |

Defaults and valid ranges for Knee and Limiter ceiling are not specified in the available documentation; see the floating editor for current values.

## Tips

- Changes made in the floating editor are reflected immediately in the applet tile's transfer curve and gain-reduction bar.
- The TX and RX editors are fully independent. Opening one does not affect the other.
- The floating editor is frameless. Drag its title bar to reposition it.

## Troubleshooting

- **Double-clicking COMP in the CHAIN widget does nothing** — The COMP stage may be bypassed or the audio engine may not be connected. Check that the stage is active and that AetherSDR has an audio engine running.
- **Knee and limiter controls are not visible** — You may be looking at the applet tile rather than the floating editor. The tile does not expose knee or limiter controls. Double-click the COMP stage in the CHAIN widget to open the full editor.

## Related

- [Aetherial Compressor (TX) / Aetherial AGC-C (RX) overview](overview.md)
- [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md)
- [Adjust compressor threshold (TX or RX side)](adjust-compressor-threshold-tx-or-rx-side.md)
- [Watch live gain reduction while speaking or listening](watch-live-gain-reduction-while-speaking-or-listening.md)

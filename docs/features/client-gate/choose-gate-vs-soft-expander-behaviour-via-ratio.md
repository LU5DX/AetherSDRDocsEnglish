# Choose gate vs soft-expander behaviour via ratio

The Ratio knob controls how aggressively the gate attenuates audio below the threshold. Setting a low ratio produces a soft downward expander that gently reduces quiet audio; setting a high ratio produces a hard gate that cuts it sharply. Choosing the right ratio lets you match the gate's character to your noise situation and operating style.

## Before you start

- The gate stage must be enabled on the side you want to adjust (TX or RX). If the applet is not visible, enable the gate via the CHAIN widget or double-click the GATE stage to open the floating editor.
- Open the **Aetherial TX Gate** sub-container (TX) or the **Aetherial AGC-T** sub-container (RX) inside the Aetherial Audio (TXDSP) parent container in the Applet Panel.

## Steps

1. Locate the **Ratio** knob in the five-knob row at the bottom of the applet.
2. To set soft-expander behaviour, turn **Ratio** toward a low value (for example, 2.0:1). Audio below the threshold is reduced gradually.
3. To set hard-gate behaviour, turn **Ratio** toward a high value (for example, 8.0:1 or higher). Audio below the threshold is cut sharply.
4. Watch the gain-reduction bar while audio passes through. A soft-expander setting produces a shallower, more gradual amber fill; a hard-gate setting produces a deep, abrupt fill when the gate closes.
5. If the hard-gate cut is too severe between words, adjust **Floor** to limit the maximum attenuation. See [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md).

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) | Behaviour |
|---|---|---|---|---|
| **Ratio** | 2.0 | 1.0 to 10.0 | `ClientGateTxRatio` / `ClientGateRxRatio` | Displayed as X.X:1. Lower values expand softly; higher values gate hard. |
| **Thresh** | -40.0 dB | -80.0 to 0.0 dB | `ClientGateTxThresholdDb` / `ClientGateRxThresholdDb` | Level below which attenuation begins. |
| **Floor** | -15.0 dB | -80.0 to 0.0 dB | `ClientGateTxFloorDb` / `ClientGateRxFloorDb` | Maximum attenuation the gate is allowed to apply, regardless of ratio. |
| **Gain-reduction bar** | — | 0 to 40 dB GR | — | Amber strip, right-filled. The tick at -15 dB marks the default Floor value. |
| Transfer curve | — | — | — | Shows the static transfer curve with a live ball at the current input level. |

## Tips

- A ratio of 2.0:1 (the default) is a conservative starting point suitable for most TX use. Raise it only if low-level noise is still audible when you are not speaking.
- At ratios above approximately 8.0:1 the gate behaves almost like an on/off switch. Pair this with a carefully set **Thresh** to avoid clipping the leading edge of words.
- The transfer curve updates in real time as you move **Ratio**. Use the live input ball to confirm the curve shape matches your intent before transmitting.
- Changes to **Ratio** take effect immediately and are saved automatically. No Apply or Save button is required.

## Troubleshooting

- **Ratio knob has no effect on the sound** — Confirm the gate stage is enabled. A bypassed gate passes audio unmodified regardless of knob settings. See [Bypass the gate from the chain](bypass-the-gate-from-the-chain.md).
- **Hard-gate ratio cuts too deep and creates unnatural silences** — Lower **Floor** toward 0 dB to reduce the maximum attenuation, or reduce **Ratio** toward the soft-expander range.
- **Soft-expander ratio does not suppress noise enough** — Raise **Ratio** or lower **Thresh** so attenuation begins at a higher input level.

## Related

- [Aetherial TX Gate / Aetherial AGC-T (RX) overview](overview.md)
- [Set TX threshold just above room noise floor](set-tx-threshold-just-above-room-noise-floor.md)
- [Set Floor to avoid unnatural silence between words](set-floor-to-avoid-unnatural-silence-between-words.md)
- [Tune attack / release for natural open/close](tune-attack-release-for-natural-open-close.md)
- [Watch live GR while not speaking](watch-live-gr-while-not-speaking.md)

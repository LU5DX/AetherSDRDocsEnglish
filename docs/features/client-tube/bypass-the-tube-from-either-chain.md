# Bypass the tube from either chain

The CHAIN widget lets you disable the tube stage on the TX or RX path without touching any of the knob settings. Use this to A/B the effect or to take the tube out of the signal path entirely.

## Before you start

- AetherSDR must be running with an audio engine loaded (a radio connection is not required for the tube stage itself).
- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel. If it is not, check `View > Applet Panel`.
- Locate the CHAIN widget inside the Aetherial Audio (TXDSP) container. It contains separate TX and RX signal-chain stage selectors.

## Steps

1. In the applet panel, find the CHAIN widget inside the **Aetherial Audio (TXDSP)** container.
2. Identify the **TUBE** stage on the side you want to bypass — TX (labeled **Aetherial Mic-PreAmp**) or RX (labeled **Aetherial Dynamic Tube**).
3. Single-click the **TUBE** stage in the CHAIN widget to toggle bypass on that side.
   - When the stage is active, the tube applet is visible and processing.
   - When bypassed, the tube applet is hidden and the stage passes signal through unprocessed.
4. To re-enable, single-click the **TUBE** stage again.

Alternatively, open the floating editor for either side by double-clicking the **TUBE** stage in the CHAIN widget (title: **Aetherial Tube — TX** or **Aetherial Tube — RX**). Bypass is controlled from the CHAIN widget, not from inside the editor.

## What each control does

| Setting key | What it controls | Default | Valid range |
|---|---|---|---|
| `ClientTubeTxEnabled` | Whether the TX tube stage is active | — | Enabled / bypassed |
| `ClientTubeRxEnabled` | Whether the RX tube stage is active | — | Enabled / bypassed |
| `ClientTubeTxDriveDb` | TX Drive — signal level into the tube | 0.0 dB | 0.0 – 24.0 dB |
| `ClientTubeRxDriveDb` | RX Drive — signal level into the tube | 0.0 dB | 0.0 – 24.0 dB |
| `ClientTubeTxTone` | TX Tone — darkens (negative) or brightens (positive) | 0.00 | −1.0 to 1.0 |
| `ClientTubeRxTone` | RX Tone | 0.00 | −1.0 to 1.0 |
| `ClientTubeTxBiasAmount` | TX Bias — operating point on the transfer curve | 0 % | 0 – 100 % |
| `ClientTubeRxBiasAmount` | RX Bias | 0 % | 0 – 100 % |
| `ClientTubeTxOutputGainDb` | TX Output — post-tube make-up gain | 0.0 dB | −24.0 to 12.0 dB |
| `ClientTubeRxOutputGainDb` | RX Output | 0.0 dB | −24.0 to 12.0 dB |
| `ClientTubeTxDryWet` | TX Mix — dry/wet blend (100 % = fully saturated) | 100 % | 0 – 100 % |
| `ClientTubeRxDryWet` | RX Mix | 100 % | 0 – 100 % |

## Tips

- Bypassing the tube stage preserves all knob values (`Drive`, `Tone`, `Bias`, `Output`, `Mix`). Re-enabling restores the same settings.
- The transfer curve and live input ball in the applet are only visible when the tube stage is active. They disappear when bypassed because the applet itself is hidden.
- The TX and RX sides are fully independent. You can bypass one without affecting the other.
- A 30 Hz sync timer keeps the applet knobs consistent with any changes made in the floating editor. If you change settings in the editor while the stage is active, the applet will reflect them within one polling cycle.

## Troubleshooting

- **Single-clicking the TUBE stage has no effect** — Confirm you are clicking the correct side's TUBE stage (TX vs. RX). The two chains are separate and clicking one does not affect the other.
- **The tube applet is not visible after enabling** — The applet is hidden until the tube stage is enabled via the CHAIN widget. If it still does not appear after enabling, check that the **Aetherial Audio (TXDSP)** parent container is expanded in the applet panel.

## Related

- [Aetherial Mic-PreAmp (TX) / Aetherial Dynamic Tube (RX) overview](overview.md)
- [Dial Drive until the curve starts to bend (TX warmth or RX tone shaping)](dial-drive-until-the-curve-starts-to-bend-tx-warmth-or-rx-tone-shaping.md)
- [Parallel-blend saturation with Mix](parallel-blend-saturation-with-mix.md)
- [Compensate level changes with Output](compensate-level-changes-with-output.md)

# Pick Aphex (Even) vs Behringer (Odd) character

Choose between two harmonic-enhancement algorithms in the PUDU exciter: Even mode (Aphex-lineage) for a warmer, asymmetric character, or Odd mode (Behringer-lineage) for a brighter, symmetric sound. The choice applies independently to the TX and RX chains.

## Before you start

- The PUDU stage must be visible in the Aetherial Audio chain. If the applet is hidden, enable the PUDU stage via the CHAIN widget on the TX or RX side, or double-click the PUDU stage in the CHAIN widget to open the floating editor.
- Decide whether you are adjusting the transmit path ("Aetherial TX Voice Processor — TX") or the receive path ("Aetherial Voice Processor — RX"). The two sides are fully independent.
- On TX, the panel opens with the title "Aetherial Voice Processor — TX". On RX, the panel opens with the title "Aetherial Voice Processor — RX". Use the correct panel for the chain you want to adjust.

## Steps

1. Open the PUDU exciter panel: double-click the PUDU stage in the CHAIN widget on the TX or RX side. The floating editor appears with the correct title for that chain.
2. Find the two mode buttons directly below the PooDoo logo: `Even` and `Odd`.
3. Click `Even` to select Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer, with Big Bottom LF saturation. The button highlights in amber when active.
4. Click `Odd` to select Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter, with a feed-forward bass compressor.
5. Close the panel. To adjust the other chain, double-click its PUDU stage in the CHAIN widget to open its independent panel.

The selection is saved immediately to `ClientPuduTxMode` (TX) or `ClientPuduRxMode` (RX).

## What each control does

| Control | Behavior | Default | Valid values | Setting key |
|---|---|---|---|---|
| `Even` | Selects Aphex-lineage asymmetric shaping. Exclusive with `Odd`. | — | Selected / unselected | `ClientPuduTxMode` / `ClientPuduRxMode` |
| `Odd` | Selects Behringer-lineage symmetric tanh shaping. Exclusive with `Even`. | — | Selected / unselected | `ClientPuduTxMode` / `ClientPuduRxMode` |

Only one of `Even` or `Odd` can be active at a time. Selecting one deselects the other.

## Tips

- Even mode suits voice signals where warmth and low-end body are the goal. Odd mode suits situations where added presence and brightness are preferred.
- The PooDoo logo pulses with the processed (wet) signal RMS, so you can see the exciter reacting as you switch modes without monitoring audio.
- When the PUDU stage is bypassed, the entire applet tile dims to approximately 55% opacity, matching the dim effect applied to the EQ curve. This is a visual indicator only and does not affect your settings.
- All six Body and Clarity knobs remain active regardless of which mode is selected; their effect on the signal changes character depending on the mode chosen.

## Related

- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Add air with Doo Air](add-air-with-doo-harmonics.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)
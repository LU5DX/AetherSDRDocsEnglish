# Pick Aphex (Even) vs Behringer (Odd) character

The PUDU Exciter offers two harmonic shaping algorithms. Switching between them changes the tonal character of both the Poo (low-frequency) and Doo (high-frequency) processors simultaneously. Choose Even for a warmer, Aphex-lineage sound; choose Odd for a brighter, Behringer-lineage sound.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. If the PUDU sub-container is not visible, enable the stage via the CHAIN widget or double-click the PUDU (Enh) stage in the CHAIN widget to open the floating PUDU editor.
- The PUDU applet is inside the PooDoo Audio (TXDSP) parent container in the applet panel.

## Steps

1. Locate the two buttons labelled **Even** and **Odd** near the top of the PUDU applet, below the PooDoo logo.
2. Click **Even** to select Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer, with Big Bottom LF saturation.
3. Click **Odd** to select Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter, with a feed-forward bass compressor.

The selected button highlights in amber. The change takes effect immediately and is saved to `ClientPuduTxMode`.

## What each control does

| Control | Behavior | Persisted key |
|---------|----------|---------------|
| **Even** | Selects Aphex-lineage asymmetric shaping. Produces predominantly even harmonics with Big Bottom LF saturation. Exclusive with **Odd**. | `ClientPuduTxMode` |
| **Odd** | Selects Behringer-lineage symmetric tanh shaping. Produces pure odd harmonics with a feed-forward bass compressor. Exclusive with **Even**. | `ClientPuduTxMode` |

## Tips

- Even mode tends to suit voice and warm instruments; Odd mode tends to suit signals that need more presence and edge.
- Switching modes does not reset any of the Poo or Doo knobs, so you can audition both characters with the same drive and mix settings and compare directly.
- The PooDoo logo pulses with the processed signal level — watch it while toggling modes to confirm the exciter is active.

## Related

- [PUDU Exciter overview](overview.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md)

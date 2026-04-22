# Pick Aphex (Even) vs Behringer (Odd) character

The PUDU exciter offers two distinct harmonic flavors. Use Even for Aphex-style warmth with Big Bottom low-frequency saturation, or Odd for Behringer-style brightness with a feed-forward bass compressor.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. The PUDU applet is hidden until the stage is active. See [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md) if the applet is not visible.
- Open the PUDU applet: locate the PUDU sub-container inside the PooDoo Audio (TXDSP) parent container, or double-click the PUDU (Enh) stage in the CHAIN widget to open the floating editor.

## Steps

1. Locate the mode toggle row at the top of the PUDU applet, directly below the PooDoo logo.
2. Click "Even" to select Aphex-lineage asymmetric shaping — predominantly even harmonics, warmer tone, with Big Bottom LF saturation. The button highlights in amber when selected.
3. Click "Odd" to select Behringer-lineage symmetric tanh shaping — pure odd harmonics, brighter presence, with a feed-forward bass compressor instead of LF saturation.

The selection takes effect immediately and is saved to `ClientPuduTxMode`.

## What each control does

| Control | Behavior | Default | Setting key |
|---------|----------|---------|-------------|
| Even | Selects Aphex-lineage asymmetric shaping. Predominantly even harmonics, warmer character, with Big Bottom LF saturation. Exclusive with Odd. | — | `ClientPuduTxMode` |
| Odd | Selects Behringer-lineage symmetric tanh shaping. Pure odd harmonics, brighter character, with a feed-forward bass compressor. Exclusive with Even. | — | `ClientPuduTxMode` |

## Tips

- Even mode suits voices that need warmth and weight in the low mids. Odd mode suits voices that are already full in the low end and need presence or cut.
- The Poo group (Drive, Tune, Mix) shapes the low-frequency processor; its behavior differs subtly between the two modes because the underlying saturation algorithm changes. After switching modes, check your Poo / Drive setting — what was appropriate in Even may be too aggressive in Odd.
- The PooDoo logo pulses brighter as the processed (wet) signal increases. Use it as a quick visual check that the exciter is active after switching modes.

## Related

- [PUDU Exciter overview](overview.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Bypass PUDU from the chain](bypass-pudu-from-the-chain.md)

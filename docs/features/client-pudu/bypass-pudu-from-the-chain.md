# Bypass PUDU from the chain

Temporarily remove the PUDU exciter from the TX DSP chain without changing any of its settings. Use this when you want to compare your audio with and without PUDU processing, or when you need to transmit without the effect active.

## Before you start

- The PUDU stage must already be present in the CHAIN widget inside the PooDoo Audio (TXDSP) container.
- No radio connection is required to bypass or re-enable the stage.

## Steps

1. Locate the CHAIN widget in the PooDoo Audio (TXDSP) container.
2. Single-click the **PUDU (Enh)** stage in the CHAIN widget.

A single click toggles the PUDU stage between active and bypassed. The stage remains in the chain but audio passes through it unprocessed while it is bypassed. The `ClientPuduTxEnabled` setting is updated immediately and persisted.

To re-enable PUDU, single-click the **PUDU (Enh)** stage again.

## Tips

- Bypassing via the CHAIN widget does not reset any knob values. All settings for Poo Drive, Poo Tune, Poo Mix, Doo Tune, Doo Air, and Doo Mix are preserved.
- Double-clicking the **PUDU (Enh)** stage in the CHAIN widget opens the floating PUDU editor instead of toggling bypass. Use a single click to bypass.
- The PooDoo logo inside the PUDU applet pulses with the processed signal RMS when PUDU is active and stops pulsing when bypassed.

## Related

- [PUDU Exciter overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)

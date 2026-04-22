# Bypass PUDU from the chain

The PUDU exciter is enabled and disabled from the CHAIN widget, not from inside the PUDU Exciter applet itself. Use this page to temporarily remove PUDU from the TX DSP chain without changing any of its settings.

## Before you start

- The PooDoo Audio (TXDSP) parent container must be visible in the applet panel.
- The PUDU (Enh) stage must be present in the CHAIN widget.

## Steps

1. Locate the CHAIN widget inside the PooDoo Audio (TXDSP) container.
2. Find the **PUDU (Enh)** stage block in the chain.
3. Single-click the **PUDU (Enh)** stage to toggle it off. The stage is now bypassed and audio passes through the chain without PUDU processing.
4. Single-click the **PUDU (Enh)** stage again to re-enable it.

When PUDU is bypassed, the PUDU sub-container remains hidden. The persisted setting `ClientPuduTxEnabled` is updated immediately. All knob values (`ClientPuduTxPooDriveDb`, `ClientPuduTxPooTuneHz`, `ClientPuduTxPooMix`, `ClientPuduTxDooTuneHz`, `ClientPuduTxDooHarmonicsDb`, `ClientPuduTxDooMix`) and the selected mode (`ClientPuduTxMode`) are preserved.

## Tips

- Bypassing from the CHAIN widget is non-destructive. Re-enabling restores all knob positions exactly as you left them.
- To open the PUDU Exciter controls without enabling the stage, double-click the **PUDU (Enh)** stage in the CHAIN widget to open the floating editor.

## Related

- [PUDU Exciter overview](overview.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)

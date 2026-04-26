# Bypass the de-esser from the chain

Remove the Aetherial De-Esser from your TX audio path without changing any of its settings. Bypassing is useful when you want to compare treated and untreated audio, or temporarily disable de-essing for a particular session.

## Before you start

- AetherSDR must be open and the Aetherial Audio (TXDSP) processing chain must be visible.
- The DESS stage must already exist in the CHAIN widget. If the de-esser has never been enabled, the DESS stage may not be present — see [Aetherial De-Esser overview](overview.md).

## Steps

1. Locate the CHAIN widget in the Aetherial Audio (TXDSP) container.
2. Find the **DESS** stage in the chain.
3. Single-click the **DESS** stage to toggle bypass on or off.

When bypassed, the stage is visually marked as inactive and the de-esser is removed from the TX audio path. Single-clicking again re-enables it. The `ClientDeEssTxEnabled` setting is updated immediately.

## Tips

- Bypassing does not reset any knob values. Freq, Q, Thresh, and Amount all retain their current settings when you re-enable the stage.
- To open the full editor for detailed adjustments, double-click the **DESS** stage rather than single-clicking.

## Related

- [Aetherial De-Esser overview](overview.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)

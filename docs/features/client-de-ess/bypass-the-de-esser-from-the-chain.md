# Bypass the de-esser from the chain

Remove the Aetherial De-Esser from your TX or RX audio path without changing any of its settings. Bypassing is useful when you want to compare treated and untreated audio, or temporarily disable de-essing for a particular session.

## Before you start

- AetherSDR must be open and the Aetherial Audio (TXDSP or RXDSP) processing chain must be visible.
- The DESS stage must already exist in the CHAIN widget. If the de-esser has never been enabled, the DESS stage may not be present — see [Aetherial De-Esser overview](overview.md).
- The de-esser is available on both TX and RX audio paths. Each path has its own independent instance of the Aetherial De-Esser.

## Steps for TX de-esser bypass

1. Locate the CHAIN widget in the Aetherial Audio (TXDSP) container.
2. Find the **DESS** stage in the chain.
3. Single-click the **DESS** stage to toggle bypass on or off.

## Steps for RX de-esser bypass

1. Locate the CHAIN widget in the Aetherial Audio (RXDSP) container.
2. Find the **DESS** stage in the chain.
3. Single-click the **DESS** stage to toggle bypass on or off.

When bypassed, the entire de-esser tile renders at reduced opacity (55 % of normal). Single-clicking again re-enables it and restores the tile to full opacity. The `ClientDeEssTxEnabled` and `ClientDeEssRxEnabled` settings are updated immediately.

## Opening the de-esser settings panel

The de-esser settings panel has two instances:
- **TX instance**: "Aetherial De-Esser — TX" (accessible from the Aetherial Audio Channel Strip's TX path)
- **RX instance**: "Aetherial De-Esser — RX" (accessible from the Aetherial Audio Channel Strip's RX path)

To open the appropriate instance:
1. Open the Aetherial Audio Channel Strip.
2. Click the **DESS** stage to open the de-esser settings panel for that path (TX or RX).
3. The panel title bar shows either "Aetherial De-Esser — TX" or "Aetherial De-Esser — RX" depending on which path you accessed.

## De-esser controls

The Aetherial De-Esser panel contains the following controls:

| Label | Kind | Default | Valid Range | Setting Key | Notes |
|---|---|---|---|---|---|
| Sidechain response curve | indicator | — | — | — | Draws the bandpass filter response with a live ball at the current centre frequency. |
| Gain-reduction bar | meter | — | 0 to 24 dB GR | — | Horizontal soft-red strip, right-filled. Scale maxes at 24 dB; a tick marks the -6 dB typical amount. Refreshed ~30 Hz. |
| Freq | knob | 6000 Hz | 1000 to 12000 Hz | `ClientDeEssTxFrequencyHz` or `ClientDeEssRxFrequencyHz` | Logarithmic mapping. Sets the centre frequency of the sibilance band. |
| Q | knob | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` or `ClientDeEssRxQ` | Linear mapping. Sets the bandwidth of the sibilance band — higher Q = narrower. |
| Thresh | knob | -30.0 dB | -60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` or `ClientDeEssRxThresholdDb` | Level above which the de-esser starts attenuating the band. |
| Amount | knob | -6.0 dB | -24.0 to 0.0 dB | `ClientDeEssTxAmountDb` or `ClientDeEssRxAmountDb` | Maximum attenuation applied at peak sibilance. Values are negative (or zero) because they represent reduction. |
| Attack | knob | 1.0 ms | 0.1 to 30.0 ms | `ClientDeEssTxAttackMs` or `ClientDeEssRxAttackMs` | Sets how quickly the de-esser responds once sibilance crosses the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). |
| Release | knob | 100 ms | 10.0 to 500.0 ms | `ClientDeEssTxReleaseMs` or `ClientDeEssRxReleaseMs` | Sets how quickly gain returns after sibilance drops below the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). |

## Tips

- Bypassing does not reset any knob values. Freq, Q, Thresh, and Amount all retain their current settings when you re-enable the stage.
- The TX and RX de-esser instances are independent. Changing settings on one does not affect the other.
- The sidechain response curve and gain-reduction meter reflect the currently active instance (TX or RX) in the panel title bar.

## Related

- [Aetherial De-Esser overview](overview.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
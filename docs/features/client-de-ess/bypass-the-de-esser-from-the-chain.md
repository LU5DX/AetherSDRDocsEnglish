# Aetherial De-Esser

The Aetherial De-Esser tames harsh 'S' and 'T' sibilance by ducking a narrow band when it exceeds a sidechain threshold. It shows the sidechain bandpass response, a 24 dB gain-reduction meter, and six tuning knobs (Freq, Q, Thresh, Amount, Attack, Release).

**Applet instances:**
- **TX instance**: "Aetherial De-Esser" (shown in the docked Applet Panel)
- **RX instance**: "Aetherial De-Esser — RX" (reachable through the Aetherial Audio Channel Strip)

## Before you start

- AetherSDR must be open and the Aetherial Audio (TXDSP or RXDSP) processing chain must be visible.
- The DESS stage must already exist in the CHAIN widget. If the de-esser has never been enabled, the DESS stage may not be present.
- The de-esser is available on both TX and RX audio paths. Each path has its own independent instance of the Aetherial De-Esser.

## Bypass the de-esser from the chain

Remove the Aetherial De-Esser from your TX or RX audio path without changing any of its settings. Bypassing is useful when you want to compare treated and untreated audio, or temporarily disable de-essing for a particular session.

### Steps for TX de-esser bypass

1. Locate the CHAIN widget in the Aetherial Audio (TXDSP) container.
2. Find the **DESS** stage in the chain.
3. Single-click the **DESS** stage to toggle bypass on or off.

### Steps for RX de-esser bypass

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
| Sidechain response curve | indicator | — | — | — | Compact-mode ClientDeEssCurveWidget. Draws the bandpass filter response with a live ball at the current centre frequency. Frequency axis labels are rendered as QStaticText for improved performance. |
| Gain-reduction bar | meter | — | 0 to 24 dB GR | — | Horizontal soft-red strip, right-filled. Scale maxes at 24 dB; a tick marks the -6 dB typical amount. Refreshed ~30 Hz from `ClientDeEss::gainReductionDb()`. |
| Freq | knob | 6000 Hz | 1000 to 12000 Hz | `ClientDeEssTxFrequencyHz` or `ClientDeEssRxFrequencyHz` | Logarithmic mapping (1000 * 12^n). Sets the centre frequency of the sibilance band. Label '6.0 kHz' above 1 kHz, 'N Hz' below. |
| Q | knob | 2.00 | 0.5 to 5.0 | `ClientDeEssTxQ` or `ClientDeEssRxQ` | Linear mapping. Sets the bandwidth of the sibilance band — higher Q = narrower. Label 'X.XX'. |
| Thresh | knob | -30.0 dB | -60.0 to 0.0 dB | `ClientDeEssTxThresholdDb` or `ClientDeEssRxThresholdDb` | Linear mapping. Level above which the de-esser starts attenuating the band. |
| Amount | knob | -6.0 dB | -24.0 to 0.0 dB | `ClientDeEssTxAmountDb` or `ClientDeEssRxAmountDb` | Linear mapping. Maximum attenuation applied at peak sibilance. Values are negative (or zero) because they represent reduction. |
| Attack | knob | 1.0 ms | 0.1 to 30.0 ms | `ClientDeEssTxAttackMs` or `ClientDeEssRxAttackMs` | Exponential mapping (0.1 * 300^n). Sets how quickly the de-esser responds once sibilance crosses the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob. |
| Release | knob | 100 ms | 10.0 to 500.0 ms | `ClientDeEssTxReleaseMs` or `ClientDeEssRxReleaseMs` | Exponential mapping (10 * 50^n). Sets how quickly gain returns after sibilance drops below the threshold. Present in the Channel Strip StripDeEssPanel (RX and TX). The docked ClientDeEssApplet omits this knob. |

## Indicators

| Label | States | Meaning |
|---|---|---|
| Centre-frequency ball | resting on curve peak | Marks the currently-tuned sibilance centre frequency on the response curve. |
| Gain-reduction strip | empty, soft-red fill | Current attenuation applied to the sibilance band. |

## Tips

- Bypassing does not reset any knob values. Freq, Q, Thresh, and Amount all retain their current settings when you re-enable the stage.
- The TX and RX de-esser instances are independent. Changing settings on one does not affect the other.
- The sidechain response curve and gain-reduction meter reflect the currently active instance (TX or RX) in the panel title bar.
- Frequency axis labels on the sidechain response curve use cached QStaticText for improved rendering performance.

## Related

- [Aetherial De-Esser overview](overview.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
- [Set threshold just below the loudest 'S' peaks](set-threshold-just-below-the-loudest-s-peaks.md)
- [Dial Amount for the most transparent de-essing](dial-amount-for-the-most-transparent-de-essing.md)
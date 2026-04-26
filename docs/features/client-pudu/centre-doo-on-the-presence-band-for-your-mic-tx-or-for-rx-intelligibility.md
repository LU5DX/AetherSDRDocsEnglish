# Centre Doo on the presence band for your mic (TX) or for RX intelligibility

The **Doo / Tune** knob sets the centre frequency of the high-frequency excitement band. Moving it lets you target the specific presence or intelligibility region that matters most — the upper-midrange bite of your microphone on TX, or the speech-clarity band on RX.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget for the side you want to adjust (TX or RX). See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- Open the relevant applet: **Aetherial TX Poodoo™** for transmit, **Aetherial RX Poodoo™** for receive. Both are inside the Aetherial Audio (TXDSP) parent container. You can also double-click the PUDU stage in the CHAIN widget to open the matching frameless editor (titled **Aetherial Poodoo™ — TX** or **Aetherial Poodoo™ — RX**).

## Steps

1. Locate the **Doo** group — the right-hand bracket of the six-knob row.
2. Find the first knob under the **Doo** bracket, labelled **Tune**.
3. Turn **Doo / Tune** to the frequency that covers the presence range you want to enhance.
   - For a typical microphone TX presence peak, try the 3 kHz – 6 kHz range.
   - For RX speech intelligibility, try 2 kHz – 4 kHz.
   - The knob displays its value as **X.X kHz** at 1000 Hz and above.
4. Monitor the PooDoo logo — its pulse brightness reflects the processed wet-signal level and gives a real-time indication that the Doo section is active.
5. Adjust **Doo / Air** and **Doo / Mix** to taste after setting the centre frequency. See [Add air with Doo Harmonics](add-air-with-doo-harmonics.md) and [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md).

## What each control does

| Control | Default | Valid range | Persisted setting | Behavior |
|---|---|---|---|---|
| **Doo / Tune** (TX) | 5000 Hz | 1000 – 10000 Hz | `ClientPuduTxDooTuneHz` | Logarithmic mapping. Centres the high-frequency excitement band on TX. Displayed as X.X kHz above 1 kHz. |
| **Doo / Tune** (RX) | 5000 Hz | 1000 – 10000 Hz | `ClientPuduRxDooTuneHz` | Logarithmic mapping. Centres the high-frequency excitement band on RX. |
| **Doo / Air** (TX) | 6.0 dB | 0.0 – 24.0 dB | `ClientPuduTxDooHarmonicsDb` | Amount of harmonics added at the Doo band. |
| **Doo / Air** (RX) | 6.0 dB | 0.0 – 24.0 dB | `ClientPuduRxDooHarmonicsDb` | Amount of harmonics added at the Doo band. |
| **Doo / Mix** (TX) | 30 % | 0 – 100 % | `ClientPuduTxDooMix` | Blends the excited high band with the dry signal. |
| **Doo / Mix** (RX) | 30 % | 0 – 100 % | `ClientPuduRxDooMix` | Blends the excited high band with the dry signal. |

## Tips

- **Doo / Tune** uses logarithmic mapping, so the upper half of the knob travel covers a wider frequency span than the lower half. Make small adjustments when working above 5 kHz.
- TX and RX instances are fully independent. Setting a Doo frequency on TX has no effect on RX.
- The **Even** mode (Aphex-lineage) adds asymmetric harmonics at the Doo band — warmer character. **Odd** mode (Behringer-lineage) adds symmetric odd harmonics — brighter and more forward. The best Doo / Tune point may differ between modes. See [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md).

## Related

- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)
- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)

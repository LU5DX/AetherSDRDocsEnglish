# Centre Clarity on the presence band for your mic (TX) or for RX intelligibility

The **Doo / Tune** knob sets the centre frequency of the high-frequency excitement band. Moving it lets you target the specific presence or intelligibility region that matters most — the upper-midrange bite of your microphone on TX, or the speech-clarity band on RX.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget for the side you want to adjust (TX or RX). See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md). When the stage is bypassed, the entire applet tile dims to approximately 55 % opacity as a visual reminder that DSP is inactive.
- Open the relevant applet: **Aetherial TX Voice Processor** for transmit, **Aetherial RX Poodoo™** for receive. Both are inside the Aetherial Audio (TXDSP) parent container. You can also double-click the PUDU stage in the CHAIN widget to open the matching frameless editor (titled **Aetherial Poodoo™ — TX** or **Aetherial Poodoo™ — RX**).

## Steps

1. Locate the **Clarity** group — the right-hand bracket of the six-knob row.
2. Find the first knob under the **Clarity** bracket, labelled **Tune**.
3. Turn **Doo / Tune** to the frequency that covers the presence range you want to enhance.
   - For a typical microphone TX presence peak, try the 3 kHz – 6 kHz range.
   - For RX speech intelligibility, try 2 kHz – 4 kHz.
   - The knob displays its value as **X.X kHz** at 1000 Hz and above.
4. Monitor the AetherVoice logo — its pulse brightness reflects the processed wet-signal level and gives a real-time indication that the Clarity section is active.
5. Optionally, click the value text of any knob to enter a precise value using the inline editor. Type the desired number and press Enter, or click elsewhere to commit. The value is automatically clamped to the valid range.
6. Adjust **Doo / Air** and **Doo / Mix** to taste after setting the centre frequency. See [Add air with Doo Harmonics](add-air-with-doo-harmonics.md) and [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md).

## What each control does

| Control             | Default                                                                                      | Valid range                               |
|---------------------|----------------------------------------------------------------------------------------------|-------------------------------------------|
| **Doo / Tune** (TX) | 5000 Hz                                                                                      | 1000 – 10000 Hz                           |
| **Doo / Tune** (RX) | 5000 Hz                                                                                      | 1000 – 10000 Hz                           |
| **Doo / Air** (TX)  | 6.0 dB                                                                                       | 0.0 – 24.0 dB                             |
| **Doo / Air** (RX)  | 6.0 dB                                                                                       | 0.0 – 24.0 dB                             |
| **Doo / Mix** (TX)  | 30 %                                                                                         | 0 – 100 %                                 |
| **Doo / Mix** (RX)  | 30 %                                                                                         | 0 – 100 %                                 |
| AetherVoice logo    | Animated branded logo that pulses with the wet-signal RMS. Displays 'AetherVoice™' wordmark. | PooDooLogo widget — 40 px minimum height. |
| Clarity group label | Bracket label for the three high-frequency processor knobs (Tune, Air, Mix).                 | —                                         |

## Tips

- **Doo / Tune** uses logarithmic mapping, so the upper half of the knob travel covers a wider frequency span than the lower half. Make small adjustments when working above 5 kHz.
- TX and RX instances are fully independent. Setting a Doo frequency on TX has no effect on RX.
- The **Even** mode (Aphex-lineage) adds asymmetric harmonics at the Clarity band — warmer character. **Odd** mode (Behringer-lineage) adds symmetric odd harmonics — brighter and more forward. The best Doo / Tune point may differ between modes. See [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md).
- If the applet tile appears dimmed, the PUDU stage is bypassed. Re-enable it in the CHAIN widget before making adjustments.
- Use the inline editor to type exact frequencies. Click the displayed value to activate the editor, type a number, and press Enter. Locale-aware parsing accepts both dot and comma decimal separators. Invalid entries revert silently to the previous value.

## Related

- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)
# Add air with Doo Harmonics

Use the Doo / Air knob to add harmonic excitement and presence to the high-frequency band. This raises perceived "air" on TX to make your signal cut through, or on RX to improve intelligibility of incoming audio.

## Before you start

- The PUDU stage must be enabled in the audio chain. If it is not visible, enable it via the CHAIN widget on the matching TX or RX side.
- Open the Aetherial TX Poodoo™ or Aetherial RX Poodoo™ applet in the Applet Panel, or double-click the PUDU stage in the CHAIN widget to open the floating editor titled "Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX".

## Steps

1. Locate the **Doo** group — the three knobs on the right side of the applet, under the "Doo" bracket label.
2. Turn the **Air** knob to set the amount of harmonic content added at the high-frequency band. The value is shown in dB below the knob.
3. Watch the PooDoo logo pulse increase as the wet-signal level rises. Use this as a rough indicator of how much processing is being applied.
4. If the result is too aggressive, reduce **Air** or lower **Doo / Mix** to blend the effect back with the dry signal.

Settings are saved automatically. The value persists in `ClientPuduTxDooHarmonicsDb` (TX) or `ClientPuduRxDooHarmonicsDb` (RX).

## What each control does

| Control | Default | Valid range | Persisted setting (TX / RX) | Behavior |
|---|---|---|---|---|
| Doo / Air | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxDooHarmonicsDb` / `ClientPuduRxDooHarmonicsDb` | Sets the amount of harmonics added at the Doo frequency band. Linear mapping. |
| Doo / Tune | 5000 Hz | 1000 to 10000 Hz | `ClientPuduTxDooTuneHz` / `ClientPuduRxDooTuneHz` | Centres the high-frequency excitement band. Logarithmic mapping. Displayed as X.X kHz above 1 kHz, X Hz below. |
| Doo / Mix | 30 % | 0 to 100 % | `ClientPuduTxDooMix` / `ClientPuduRxDooMix` | Blends the excited highs back with the dry signal. Linear mapping. |

## Tips

- Start with **Air** at 6.0 dB (default) and **Doo / Mix** at 30 % (default), then increase **Air** gradually while listening to the effect on program material.
- The **Doo / Tune** knob centres the band where harmonics are added. Set it to match your mic's presence peak on TX, or to the intelligibility range of incoming audio on RX. See [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md) for that procedure.
- Even mode (Aphex-lineage) produces warmer even harmonics; Odd mode (Behringer-lineage) produces brighter odd harmonics. The character of **Air** differs between the two. See [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md).

## Troubleshooting

- **Air knob has no audible effect** — The PUDU stage may be bypassed. Check that the stage is enabled in the CHAIN widget. See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- **Effect sounds harsh at moderate Air values** — Lower **Doo / Mix** to reduce the wet blend rather than cutting **Air** entirely. See [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md).

## Related

- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)
- [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md)
- [Blend the Doo excitement with Mix](blend-the-doo-excitement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)

# Blend the Doo excitement with Mix

Use the Doo / Mix knob to control how much of the Doo high-frequency excitement is blended back into the dry signal. Setting Mix too high can introduce harshness; setting it too low means the Doo processing has little audible effect.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget for the relevant side (TX or RX). See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- Open the Poodoo editor by double-clicking the PUDU stage in the CHAIN widget. The editor is titled "Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX" depending on which side you are working on.

## Steps

1. Locate the **Doo** group — the three knobs on the right side of the knob row, under the "Doo" bracket label.
2. Identify the third knob in the Doo group, labelled **Mix**.
3. Turn the **Mix** knob to blend the excited high-frequency signal with the dry signal. The value is displayed as a percentage directly on the knob.
4. Release the knob. The setting is saved automatically.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Doo / Mix (TX) | 30 % | 0 % to 100 % | `ClientPuduTxDooMix` |
| Doo / Mix (RX) | 30 % | 0 % to 100 % | `ClientPuduRxDooMix` |

The knob maps linearly. At 0 % the Doo processor is mixed out entirely and has no effect on the signal. At 100 % only the processed signal passes through — no dry signal is blended in. The TX and RX sides hold fully independent Mix values.

## Tips

- Start with the default of 30 % and increase gradually while listening to the effect on presence or intelligibility.
- The PooDoo logo pulses with the wet-signal RMS. A faster, stronger pulse as you raise Mix confirms the Doo stage is contributing to the output.
- If you have not yet positioned the Doo band on the right frequency, set Mix to 0 % temporarily while adjusting Doo / Tune, then bring Mix back up. See [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md).

## Related

- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)
- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)

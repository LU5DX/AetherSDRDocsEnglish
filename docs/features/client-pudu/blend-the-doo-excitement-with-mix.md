# Blend the Doo excitement with Mix

Use the Doo / Mix knob to control how much of the Doo high-frequency excitement is blended back into the dry signal. Setting Mix too high can introduce harshness; setting it too low means the Doo processing has little audible effect.

## Before you start

- The PUDU stage must be enabled in the CHAIN widget for the relevant side (TX or RX). See [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md).
- Open the Poodoo editor by double-clicking the PUDU stage in the CHAIN widget. The editor is titled "Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX" depending on which side you are working on.
- When the PUDU stage is bypassed, the entire applet tile dims to approximately 55 % opacity. This is a visual indicator only — your knob settings are preserved. Re-enable the stage to restore full opacity and active processing.

## Steps

1. Locate the **Clarity** group — the three knobs on the right side of the knob row, under the "Clarity" bracket label.
2. Identify the third knob in the Clarity group, labelled **Mix**.
3. Turn the **Mix** knob to blend the excited high-frequency signal with the dry signal. The value is displayed as a percentage directly on the knob.
4. To type a precise value instead of turning the knob, click the knob's value text. A small text editor appears in place of the value display. Type the desired number and press **Enter** or click elsewhere to commit the value. The knob adjusts automatically and clamps to the valid range. Press **Escape** during editing to cancel and revert to the previous value.

   *Note: The inline editor accepts locale-aware number formats (e.g., "12,5" in comma-decimal locales) and strips non-numeric characters automatically if parsing fails.*

5. Release the knob or commit the typed value. The setting is saved automatically.

## What each control does

| Control          | Default                                                                                      | Valid range                               |
|------------------|----------------------------------------------------------------------------------------------|-------------------------------------------|
| Doo / Mix (TX)   | 30 %                                                                                         | 0 % to 100 %                              |
| Doo / Mix (RX)   | 30 %                                                                                         | 0 % to 100 %                              |
| AetherVoice logo | Animated branded logo that pulses with the wet-signal RMS. Displays 'AetherVoice™' wordmark. | PooDooLogo widget — 40 px minimum height. |

The knob maps linearly. At 0 % the Doo processor is mixed out entirely and has no effect on the signal. At 100 % only the processed signal passes through — no dry signal is blended in. The TX and RX sides hold fully independent Mix values.

## Tips

- Start with the default of 30 % and increase gradually while listening to the effect on presence or intelligibility.
- The PooDoo logo pulses with the wet-signal RMS. A faster, stronger pulse as you raise Mix confirms the Doo stage is contributing to the output.
- If you have not yet positioned the Doo band on the right frequency, set Mix to 0 % temporarily while adjusting Doo / Tune, then bring Mix back up. See [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md).
- To enter a specific percentage precisely, click the knob's value display to open the inline editor, type the number (e.g., "42" for 42 %), and press Enter. The knob snaps to that value.

## Related

- [Add air with Doo Harmonics](add-air-with-doo-harmonics.md)
- [Centre Doo on the presence band for your mic (TX) or for RX intelligibility](centre-doo-on-the-presence-band-for-your-mic-tx-or-for-rx-intelligibility.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Bypass PUDU from either chain](bypass-pudu-from-either-chain.md)
- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
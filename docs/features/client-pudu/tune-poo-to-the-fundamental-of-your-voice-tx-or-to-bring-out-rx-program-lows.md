# Tune Body to the fundamental of your voice (TX) or to bring out RX program lows

The **Body / Tune** knob sets the centre frequency of the low-frequency saturation band. On TX, aim it at the fundamental of your voice to add body and warmth at the right pitch. On RX, move it toward the dominant low-frequency content of the incoming audio to bring out program lows.

## Before you start

- The PUDU stage must be enabled in the Aetherial Audio chain. If the Poodoo applet is not visible, enable the PUDU stage via the CHAIN widget on the TX or RX side.
- Decide whether you are adjusting the TX chain ("Aetherial TX Poodoo™") or the RX chain ("Aetherial RX Poodoo™") — they have fully independent settings.

## Steps

1. Open the PUDU editor for the side you want to adjust: double-click the PUDU stage in the CHAIN widget. The frameless editor titled "Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX" opens.
2. Locate the **Body** group — the three knobs under the "Body" bracket label on the left half of the knob row.
3. Turn the **Tune** knob (the centre knob in the Body group) to the target frequency.
   - For TX: start near your voice fundamental. A typical male voice fundamental is 85–180 Hz; a typical female voice fundamental is 165–255 Hz. The default is 100 Hz.
   - For RX: sweep toward the dominant low-frequency program content you want to emphasise.
4. Monitor the AetherVoice™ logo — its brightness pulses with the processed signal RMS, giving real-time feedback as you dial in the frequency.
5. Adjust **Body / Mix** to blend the result to taste. Settings are saved automatically.

## What each control does

| Control | Default | Valid range | Persisted key (TX / RX) |
|---|---|---|---|
| **Body / Tune** | 100 Hz | 50 to 160 Hz | `ClientPuduTxPooTuneHz` / `ClientPuduRxPooTuneHz` |
| **Body / Drive** | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxPooDriveDb` / `ClientPuduRxPooDriveDb` |
| **Body / Mix** | 30 % | 0 to 100 % | `ClientPuduTxPooMix` / `ClientPuduRxPooMix` |

The **Body / Tune** knob uses linear mapping across its 50–160 Hz range. The display reads in whole hertz (for example, "100 Hz").

## Tips

- The Body band is intentionally narrow. If you hear little effect after tuning, raise **Body / Drive** first, then re-sweep **Body / Tune** until you hear the saturation engage.
- In **Even** mode the Body stage uses Big Bottom LF saturation; in **Odd** mode it uses a feed-forward bass compressor. The optimal tune frequency may differ slightly between modes — re-check after switching.
- Keep **Body / Mix** below 50 % on TX to avoid muddying the transmitted signal. Start at the 30 % default and increase only if the enhancement is inaudible.
- When the PUDU stage is bypassed, the entire applet tile dims to approximately 55 % opacity. This is a visual indicator only — no settings are lost.

## Troubleshooting

- **Turning Body / Tune has no audible effect** — confirm the PUDU stage is enabled (the CHAIN widget controls bypass). Also check that **Body / Drive** is above 0.0 dB and **Body / Mix** is above 0 %; both at their minimums will silence the Body band regardless of the Tune setting.
- **The Body group knobs are not visible** — the PUDU applet is hidden until the PUDU stage is enabled via the CHAIN widget or the floating editor.

## Related

- [Aetherial TX Poodoo / Aetherial RX Poodoo overview](overview.md)
- [Dial Body Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Blend the Body enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
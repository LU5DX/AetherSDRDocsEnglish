# Tune Body to the fundamental of your voice (TX) or to bring out RX program lows

The **Body / Tune** knob sets the centre frequency of the low-frequency saturation band. On TX, aim it at the fundamental of your voice to add body and warmth at the right pitch. On RX, move it toward the dominant low-frequency content of the incoming audio to bring out program lows.

## Before you start

- The PUDU stage must be enabled in the Aetherial Audio chain. If the Poodoo applet is not visible, enable the PUDU stage via the CHAIN widget on the TX or RX side.
- Decide whether you are adjusting the TX chain ("Aetherial TX Voice Processor") or the RX chain ("Aetherial RX Poodoo™") — they have fully independent settings.

## Steps

1. Open the PUDU editor for the side you want to adjust: double-click the PUDU stage in the CHAIN widget. The frameless editor titled "Aetherial Poodoo™ — TX" or "Aetherial Poodoo™ — RX" opens.
2. Locate the **Body** group — the three knobs under the "Body" bracket label on the left half of the knob row.
3. Turn the **Drive** knob (the first knob in the Body group) to set the drive level for the low-frequency processor.
4. Turn the **Tune** knob (the centre knob in the Body group) to the target frequency.
   - For TX: start near your voice fundamental. A typical male voice fundamental is 85–180 Hz; a typical female voice fundamental is 165–255 Hz. The default is 100 Hz.
   - For RX: sweep toward the dominant low-frequency program content you want to emphasise.
5. Turn the **Mix** knob (the third knob in the Body group) to blend the result to taste. Settings are saved automatically.
6. Monitor the AetherVoice logo — its brightness pulses with the processed signal RMS, giving real-time feedback as you dial in the frequency.
7. You can type a value directly into any knob's value display: click the displayed value, type a number, and press Enter or click away to confirm. The editor accepts locale-aware decimal formats (for example, "12,5" in comma-decimal locales) and strips trailing unit text.

## What each control does

| Control (Body group) | Default    | Valid range     | Notes                                         |
|----------------------|------------|-----------------|-----------------------------------------------|
| **Drive**            | 6.0 dB     | 0.0 to 24.0 dB  | Drives the low-frequency saturator/compressor |
| **Tune**             | 100 Hz     | 50 to 160 Hz    | Linear mapping; centres the LF focus band     |
| **Mix**              | 30 %       | 0.0 to 1.0      | Blends enhanced low band with dry signal      |

| Control (Clarity group) | Default    | Valid range       | Notes                                           |
|-------------------------|------------|-------------------|-------------------------------------------------|
| **Tune**                | 5000 Hz    | 1000 to 10000 Hz  | Logarithmic mapping; centres HF excitation band |
| **Air**                 | 6.0 dB     | 0.0 to 24.0 dB    | Amount of harmonics/air added at the high band  |
| **Mix**                 | 30 %       | 0.0 to 1.0        | Blends excited highs with dry signal            |

| Control             | Default | Valid range | Behavior                                                   |
|---------------------|---------|-------------|------------------------------------------------------------|
| **Even**            | —       | —           | Radio button; selects Aphex-lineage asymmetric shaping     |
| **Odd**             | —       | —           | Radio button; selects Behringer-lineage symmetric shaping  |
| AetherVoice logo    | —       | —           | Animated branded logo that pulses with wet-signal RMS      |

The **Body / Tune** knob uses linear mapping across its 50–160 Hz range. The display reads in whole hertz (for example, "100 Hz").

The **Clarity / Tune** knob uses logarithmic mapping (1000 * 10^n). The display reads in kilohertz above 1 kHz (for example, "5.0 kHz") or in hertz below.

## Tips

- The Body band is intentionally narrow. If you hear little effect after tuning, raise **Drive** first, then re-sweep **Tune** until you hear the saturation engage.
- In **Even** mode the Body stage uses Big Bottom LF saturation; in **Odd** mode it uses a feed-forward bass compressor. The optimal tune frequency may differ slightly between modes — re-check after switching.
- Keep **Mix** below 50 % on TX to avoid muddying the transmitted signal. Start at the 30 % default and increase only if the enhancement is inaudible.
- The Clarity **Air** control adds presence and sparkle. Raise it cautiously on TX to avoid harshness.
- Use the inline editor on any knob to type exact values. Click the displayed value, enter the number, and press Enter.
- When the PUDU stage is bypassed, the entire applet tile dims to approximately 55 % opacity. This is a visual indicator only — no settings are lost.
- In v26.6.1, knob colours are now sourced from the theme. The PUDU applet uses a dedicated themed container (`applet/pudu`) that can override knob ring, arc, and pointer colours independently. If you have created a custom theme, ensure the `color.knob.*` and `color.text.*` keys are defined for the PUDU container; otherwise, default theme colours apply.
- In v26.7.4, the PUDU editor no longer uses a dedicated style for its buttons. All editor buttons now follow the global theme styling consistently.

## Troubleshooting

- **Turning Tune has no audible effect** — confirm the PUDU stage is enabled (the CHAIN widget controls bypass). Also check that **Drive** is above 0.0 dB and **Mix** is above 0 %; both at their minimums will silence the Body band regardless of the Tune setting.
- **The body group knobs are not visible** — the PUDU applet is hidden until the PUDU stage is enabled via the CHAIN widget or the floating editor.
- **Typed values are not accepted** — ensure you are using a locale-appropriate decimal separator. The editor accepts numbers and strips trailing unit text (for example, "100 Hz" becomes 100).
- **Knob colours appear incorrect** — the new themed rendering in v26.6.1 reads colours from `color.knob.background`, `color.knob.foreground`, and `color.knob.handle` in the theme. If these keys are missing or misconfigured, knob visuals may fall back unexpectedly. Contact your theme developer or reset to the default theme.

## Related

- [Aetherial TX Voice Processor / Aetherial RX Poodoo overview](overview.md)
- Dial Drive for LF thickness
- Blend the Body enhancement with Mix
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- Add presence with Clarity Air
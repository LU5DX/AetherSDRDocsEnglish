# Tune Poo to the fundamental of your voice

The **Poo / Tune** knob sets the centre frequency of the PUDU exciter's low-frequency processing band. Matching it to the fundamental of your voice ensures the Poo stage works where your microphone and vocal character actually sit, rather than above or below it.

## Before you start

- The PUDU exciter must be enabled and visible. It appears in the "PUDU" sub-container inside the PooDoo Audio (TXDSP) parent container. If it is hidden, enable the PUDU stage via the CHAIN widget or double-click the PUDU (Enh) stage in the CHAIN widget to open the floating PUDU editor.
- Know the approximate fundamental frequency of your voice. For most male voices this is roughly 85–180 Hz; for most female voices roughly 165–255 Hz. The **Poo / Tune** range covers 50 to 160 Hz, so it is most useful for deeper fundamentals or for targeting the low-frequency body of the voice rather than the fundamental pitch itself.

## Steps

1. Open the PUDU sub-container inside the PooDoo Audio (TXDSP) parent container.
2. Locate the **Poo** group — the three knobs beneath the "Poo" bracket label.
3. Transmit in your normal operating mode and speak into the microphone at your typical operating level.
4. Turn the **Poo / Tune** knob while listening to the processed signal. Rotate toward lower values to focus the band on a deeper fundamental; rotate toward higher values to raise it.
5. Stop adjusting when the low-end enhancement sounds centred on your voice rather than muddy or thin.

## What each control does

| Control | Default | Valid range | Persisted key |
|---|---|---|---|
| Poo / Tune | 100 Hz | 50 to 160 Hz | `ClientPuduTxPooTuneHz` |
| Poo / Drive | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxPooDriveDb` |
| Poo / Mix | 30 % | 0 to 100 % | `ClientPuduTxPooMix` |

**Poo / Tune** centres the low-frequency focus band using a linear mapping across 50–160 Hz. The knob label reads the current value as "X Hz".

**Poo / Drive** and **Poo / Mix** are companion controls. Drive determines how hard the saturator or compressor is pushed at the tuned frequency; Mix blends the processed low band back with the dry signal. See [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md) and [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md).

## Tips

- The PooDoo logo pulses brighter as the wet-signal RMS rises. Use this as a rough visual indicator that the Poo stage is working — if the logo barely reacts during speech, **Poo / Drive** may be set too low or **Poo / Mix** near zero.
- If the processed audio sounds boomy or indistinct, the tune frequency is likely below your voice's actual fundamental. Increase **Poo / Tune** in small steps until the enhancement tracks your voice.
- The **Even** mode uses Big Bottom-style LF saturation; **Odd** mode uses a feed-forward bass compressor. The character of the Poo band differs between modes, so re-check the Tune setting after switching. See [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md).
- The upper limit of **Poo / Tune** is 160 Hz. If your voice fundamental sits above that range, focus the Poo section on the sub-fundamental body of your voice and use the **Doo** section for presence. See [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md).

## Related

- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)
- [Centre Doo on the presence band for your mic](centre-doo-on-the-presence-band-for-your-mic.md)

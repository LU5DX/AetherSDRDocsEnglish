# Tune Poo to the fundamental of your voice

The **Poo / Tune** knob centres the low-frequency processing band on the frequency you choose. Setting it to the fundamental of your voice focuses the Poo saturator or compressor where your voice actually has energy, rather than above or below it.

## Before you start

- The PUDU stage must be enabled in the PooDoo Audio chain. If the PUDU sub-container is not visible, enable the stage via the CHAIN widget or double-click the PUDU (Enh) stage in the CHAIN widget to open the floating editor.
- You need a rough idea of your voice's fundamental frequency. Most male voices sit between 85 and 180 Hz; most female voices between 165 and 255 Hz. A starting point of 100 Hz (the default) works for many baritone and bass voices.

## Steps

1. Open the PUDU sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Locate the **Poo** group — the three knobs under the bracket labelled **Poo**.
3. Turn the **Poo / Tune** knob to match your voice's fundamental. The knob displays its value as a whole number in Hz (for example, `100 Hz`).
4. Key the radio and listen to your monitor audio or watch the PooDoo logo pulse. Increase or decrease **Poo / Tune** until the low-end thickening centres on your voice rather than sounding muddy (too low) or thin (too high).
5. Fine-tune **Poo / Drive** and **Poo / Mix** to taste once the frequency is set.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Poo / Tune | 100 Hz | 50 to 160 Hz | `ClientPuduTxPooTuneHz` | Linear mapping. Centres the low-frequency focus band. |
| Poo / Drive | 6.0 dB | 0.0 to 24.0 dB | `ClientPuduTxPooDriveDb` | Drives the low-frequency saturator or compressor harder. |
| Poo / Mix | 30 % | 0 to 100 % | `ClientPuduTxPooMix` | Blends the enhanced low band back with the dry signal. |

## Tips

- The **Poo / Tune** range is 50 to 160 Hz. If your voice fundamental falls above 160 Hz, set **Poo / Tune** to its maximum and rely more on the **Doo** group for presence instead.
- In **Even** mode the Poo section uses Big Bottom-style LF saturation; in **Odd** mode it uses a feed-forward bass compressor. The same **Poo / Tune** frequency applies in both modes, but the character differs — re-check the setting if you switch modes.
- The PooDoo logo brightens with processed signal RMS. If the logo barely pulses when you transmit, **Poo / Mix** may be very low or the stage may be bypassed.

## Troubleshooting

- **Poo / Tune knob has no audible effect** — Confirm the PUDU stage is not bypassed in the CHAIN widget. Also check that **Poo / Mix** is above 0 %; at 0 % the processed low band is fully removed from the output.
- **Low end sounds muddy regardless of Tune position** — **Poo / Drive** may be set too high. Reduce it and re-evaluate the frequency.
- **Poo / Tune control is not visible** — The PUDU sub-container is hidden until the PUDU stage is enabled. Enable it via the CHAIN widget.

## Related

- [PUDU Exciter overview](overview.md)
- [Dial Poo Drive for LF thickness](dial-poo-drive-for-lf-thickness.md)
- [Blend the Poo enhancement with Mix](blend-the-poo-enhancement-with-mix.md)
- [Pick Aphex (Even) vs Behringer (Odd) character](pick-aphex-even-vs-behringer-odd-character.md)

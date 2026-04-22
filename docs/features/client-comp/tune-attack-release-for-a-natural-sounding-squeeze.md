# Tune Attack / Release for a Natural-Sounding Squeeze

Adjust the Attack and Release knobs to control how quickly the compressor responds to and recovers from loud voice peaks. Getting these timing values right prevents the compressor from sounding abrupt or pumping between syllables.

## Before you start

- The Compressor stage must be enabled (bypass off). If the COMPRESSOR tile is hidden, enable the stage via the CHAIN widget first. See [Bypass the compressor from the chain](bypass-the-compressor-from-the-chain.md).
- The COMPRESSOR sub-container must be visible inside the PooDoo Audio (TXDSP) parent container.
- Have a microphone active so you can speak while watching the gain-reduction bar respond in real time.

## Steps

1. Locate the COMPRESSOR sub-container in the applet panel.
2. Find the **Attack** knob in the five-knob row at the bottom of the tile.
3. Turn **Attack** while speaking at a normal level. Watch the gain-reduction bar: a shorter attack time causes the bar to fill quickly after each word onset; a longer attack lets the initial transient through before clamping.
4. Find the **Release** knob, immediately to the right of **Attack**.
5. Turn **Release** while speaking. A shorter release time causes the compressor to recover quickly between words; too short produces an audible pumping effect. A longer release holds the gain reduction steady across syllables, which can sound dull on fast speech.
6. Repeat steps 3–5 until the gain-reduction bar rises and falls smoothly with your speech rhythm and the audio sounds natural.

## What each control does

| Knob | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Attack | 20.0 ms | 0.1 to 300.0 ms | `ClientCompTxAttackMs` | How quickly the compressor clamps down after the input crosses the threshold. Uses exponential knob mapping. Labels show one decimal place below 10 ms, whole milliseconds above. |
| Release | 200 ms | 5 to 2000 ms | `ClientCompTxReleaseMs` | How quickly the gain returns after the input drops back below the threshold. Uses exponential knob mapping. Label shows whole milliseconds. |

The other knobs in the same row are:

| Knob | Default | Valid range | Persisted key |
|---|---|---|---|
| Thresh | -18.0 dB | -60.0 to 0.0 dB | `ClientCompTxThresholdDb` |
| Ratio | 3.0 | 1.0 to 20.0 | `ClientCompTxRatio` |
| Makeup | 0.0 dB | -12.0 to 24.0 dB | `ClientCompTxMakeupDb` |

The **Gain-reduction bar** is the horizontal amber strip above the knob row. It fills from the right, with a tick mark at 6 dB. Maximum indicated reduction is 20 dB. Use it to verify that Attack and Release are producing the response shape you want while you speak.

## Tips

- Start with a longer Attack (40–80 ms) to preserve consonant punch, then shorten it only if peaks are clipping through before compression engages.
- If the gain-reduction bar is surging up and down rapidly between words, increase Release until the motion becomes smoother.
- The envelope ball on the transfer curve moves along the curve in real time. Watching it alongside the gain-reduction bar gives a second view of how quickly gain is being applied and released.
- Knee and limiter settings (stored as `ClientCompTxKneeDb`, `ClientCompTxLimEnabled`, `ClientCompTxLimCeilingDb`) are not accessible from the applet knobs. Open the full editor if you need to adjust those. See [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md).

## Troubleshooting

- **Gain-reduction bar does not move when you speak** — The compressor stage may be bypassed, or the threshold is set too high for your mic level. Confirm the stage is enabled and check the Thresh knob. See [Adjust compressor threshold](adjust-compressor-threshold.md).
- **Audio sounds like it is pumping or breathing** — Release is too short. Turn the **Release** knob clockwise to increase the recovery time.
- **Loud word onsets are still distorting** — Attack is too long, allowing peaks through before compression engages. Turn the **Attack** knob counter-clockwise to reduce the attack time.

## Related

- [Watch live gain reduction while speaking](watch-live-gain-reduction-while-speaking.md)
- [Adjust compressor threshold](adjust-compressor-threshold.md)
- [Set compression ratio for voice](set-compression-ratio-for-voice.md)
- [Apply make-up gain after compression](apply-make-up-gain-after-compression.md)
- [Open the full Compressor editor for knee and limiter controls](open-the-full-compressor-editor-for-knee-and-limiter-controls.md)

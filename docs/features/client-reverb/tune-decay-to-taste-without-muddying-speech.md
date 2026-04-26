# Tune decay to taste without muddying speech

The Decay knob controls how long the reverb tail rings after each syllable. Setting it too high smears speech; this page shows how to find a value that adds presence without washing out intelligibility.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget. The "Aetherial FreeVerb" sub-container is hidden until the stage is active.
- Open the reverb controls: either locate the "Aetherial FreeVerb" sub-container inside the Aetherial Audio (TXDSP) parent container in the applet panel, or double-click the VERB stage in the CHAIN widget to open the floating editor titled "Aetherial FreeVerb — TX".

## Steps

1. Locate the **Decay** knob. It displays a value in the format `X.XX s`.
2. Turn **Decay** down toward `0.30 s` and transmit a voice sample. At this extreme the tail is barely audible.
3. Slowly increase **Decay** while speaking or monitoring a recording. Stop when the tail becomes audible between syllables.
4. Back off slightly until syllables no longer blur into one another. For most voice work, values in the range `0.5 s` to `1.5 s` keep speech clear.
5. If the tail still sounds muddy, increase **Damp** to roll off high-frequency energy in the tail, which often reduces the perception of smear without shortening Decay further.
6. Verify that **Mix** is not set too high. A Mix of `10 %` to `15 %` is typical for voice; excess wet signal amplifies the effect of any Decay value.

## What each control does

| Label | Default | Range | Persisted key | Behavior |
|-------|---------|-------|---------------|----------|
| Decay | 1.20 s | 0.3 to 5.0 s | `ClientReverbTxDecayS` | Sets the reverb tail length. Uses exponential mapping across its range (~16.7× from minimum to maximum). |
| Damp | 50 % | 0.0 to 1.0 (displayed as %) | `ClientReverbTxDamping` | Higher values cause high frequencies to decay faster in the tail, reducing brightness and perceived smear. |
| Mix | 15 % | 0.0 to 1.0 (displayed as %) | `ClientReverbTxMix` | Dry/wet balance. A high Mix value amplifies the audible impact of every other parameter. |

## Tips

- Because Decay uses an exponential mapping, the knob is much more sensitive at the low end of its travel. Make small adjustments when working below `1.0 s`.
- The applet knobs and the floating "Aetherial FreeVerb — TX" editor stay in sync at approximately 30 Hz. Adjustments made in one are immediately reflected in the other.
- Double-click the **Decay** knob to reset it to the default of `1.20 s`.

## Troubleshooting

- **Speech sounds washed out even at short Decay values** — Check **Mix**. If Mix is above `30 %`, the wet signal dominates regardless of tail length. Reduce Mix to `10–15 %` first, then re-evaluate Decay.
- **Decay knob has no audible effect** — The Reverb stage may not be enabled. Confirm the VERB stage is active in the CHAIN widget. The applet is hidden and the processor is bypassed when the stage is off.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

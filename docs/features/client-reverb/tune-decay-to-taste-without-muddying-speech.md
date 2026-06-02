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

| Label                | Default                                                                                                                                                                                                                                     | Range                                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Size                 | 50 %                                                                                                                                                                                                                                        | 0.0 to 1.0 (displayed as %)                                                                                 |
| Decay                | 1.20 s                                                                                                                                                                                                                                      | 0.3 to 5.0 s                                                                                                |
| Damp                 | 50 %                                                                                                                                                                                                                                        | 0.0 to 1.0 (displayed as %)                                                                                 |
| Pre                  | 20 ms                                                                                                                                                                                                                                       | 0 to 100 ms                                                                                                 |
| Mix                  | 15 %                                                                                                                                                                                                                                        | 0.0 to 1.0 (displayed as %)                                                                                 |
| Reverb visualisation | ReverbVizBox — live visualisation showing the dry sine packet (cyan), first-order reflections (yellow), and reverberant tail (magenta). All five knob values feed the rendering so the display follows knob edits in real time. 90 px tall. | Replaces the curve widget used by other DSP applets. Rendering algorithm matches StripReverbPanel::GridBox. |

## Live visualisation

The applet panel and the floating "Aetherial FreeVerb — TX" editor both display a compact waveform diagram (90 px tall) that updates in real time as you move any knob. The diagram uses three colour-coded layers:

- **Cyan** — the dry signal packet, gradient-faded toward the right. Its amplitude decreases as Mix increases.
- **Yellow** — first-order reflections. Spacing and count respond to Size; amplitude per reflection decreases with higher Damp values.
- **Magenta** — the reverberant tail. Its horizontal length reflects Decay, its high-frequency roll-off reflects Damp, and its overall amplitude reflects Mix.

The visualisation is for orientation only; it does not represent a precise impulse-response measurement. Use your ears to make final adjustments.

## Editing knob values directly

Starting in v26.5.2.1, any knob in the "Aetherial FreeVerb — TX" can be edited by typing a numeric value instead of turning the knob.

1. Click the numeric value displayed below a knob. The value becomes an editable text field with a cyan border.
2. Type the desired value. You can include units or extra characters — the editor strips them automatically. For example, `1.5` or `1.5 s` both set Decay to `1.50 s`.
3. Press Enter or click outside the editor to commit the value. The knob updates and the editor reverts to a label appearance.
4. Press Escape to cancel the edit and restore the previous value.

Inline editing respects locale — in regions that use a comma as decimal separator (such as `1,5`), the editor parses it correctly.

## Knob colours follow the current theme

Starting in v26.6.1, knob component colours are drawn from the active theme rather than hard-coded. The "Aetherial FreeVerb — TX" applet uses the `applet/reverb` container namespace, which may define custom knob foreground, background, and handle colours. If you apply a custom theme that changes the `color.knob.*` tokens, all knobs in this applet update their ring arc, background ring, handle pointer, label, and value text to match. The default appearance remains unchanged for the built-in theme.

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
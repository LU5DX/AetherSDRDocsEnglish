# Set room size for a small or large-hall feel

The Size knob controls the modelled room size in the TX reverb, letting you dial in anything from a tight booth to a large hall. Use this page to locate the control and set it to taste.

## Before you start

- The REVERB sub-container must be visible in the PooDoo Audio (TXDSP) parent container. It is hidden until the Reverb stage is enabled via the CHAIN widget or the floating Reverb editor.
- No radio connection is required to adjust reverb settings.

## Steps

1. Locate the **REVERB** sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. If the sub-container is not visible, enable the Reverb stage by clicking it in the CHAIN widget, or double-click the Reverb stage in the CHAIN widget to open the floating Reverb editor and enable it there.
3. Find the **Size** knob — the leftmost of the five knobs in the compact row.
4. Drag the **Size** knob upward for a larger room or downward for a smaller room. The label shows the current value as a percentage (for example, `50 %`).
   - For a small-room feel, set **Size** toward `0 %`.
   - For a large-hall feel, set **Size** toward `100 %`.
5. Adjust the remaining knobs to complement the room size (see Related below).

## What each control does

| Knob | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| Size | 50 % | 0 % to 100 % | `ClientReverbTxSize` | Sets the modelled room size. Linear mapping. |
| Decay | 1.20 s | 0.3 to 5.0 s | `ClientReverbTxDecayS` | Sets the reverb tail length. Exponential mapping. |
| Damp | 50 % | 0 % to 100 % | `ClientReverbTxDamping` | Higher values damp high frequencies faster in the tail. Linear mapping. |
| Pre | 20 ms | 0 to 100 ms | `ClientReverbTxPreDelayMs` | Pre-delay between the dry signal and the first reflections. Linear mapping. |
| Mix | 15 % | 0 % to 100 % | `ClientReverbTxMix` | Dry/wet balance. Linear mapping. |

## Tips

- When you increase Size substantially, consider increasing Decay as well — a larger modelled room naturally sustains reflections longer.
- Hold Shift while dragging any knob for finer adjustment (one-quarter the normal drag sensitivity).
- Double-click the Reverb stage in the CHAIN widget to open the floating Reverb editor, which gives you the same knobs in a larger, easier-to-grab format.
- Right-click the **REVERB** sub-container titlebar to float, pop-out, or hide the applet.

## Related

- [Reverb overview](overview.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Offset reflections from the dry signal with Pre](offset-reflections-from-the-dry-signal-with-pre.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

# Dial in a subtle Mix — 10-15 % is typical for voice

The Mix knob controls the dry/wet balance of the reverb effect on your transmitted audio. Keeping Mix low — between 10 % and 15 % — adds a sense of space without making your voice sound processed or hollow.

## Before you start

- The REVERB sub-container must be visible in the PooDoo Audio (TXDSP) parent container. It is hidden until the Reverb stage is enabled via the CHAIN widget or the floating editor.
- Enable the Reverb stage before adjusting Mix, or the effect will not be heard even if Mix is set above zero.

## Steps

1. Locate the REVERB sub-container inside the PooDoo Audio (TXDSP) panel.
2. Find the Mix knob — the rightmost knob in the five-knob row.
3. Turn Mix to your target value. The label updates live, showing the current percentage (for example, `15 %`).
4. Transmit a test signal and listen to the monitor output. Adjust Mix up or down until the reverb tail is audible but not dominant.

To reset Mix to its default, double-click the Mix knob. The default is 15 %.

## What each control does

| Control | Default | Range | Persisted key | Behavior |
|---------|---------|-------|---------------|----------|
| Mix | 15 % | 0 % to 100 % | `ClientReverbTxMix` | Sets the dry/wet balance. Higher values increase the proportion of reverberated signal relative to the dry signal. Mapped linearly. |

## Tips

- 10–15 % is a practical starting point for SSB voice. At these levels the tail adds warmth without calling attention to itself on the receiving end.
- Raising Mix above 30 % makes the reverb effect audible to most listeners and may reduce intelligibility in poor band conditions.
- Hold Shift while dragging the Mix knob for finer adjustment (drag sensitivity is reduced to one quarter of normal).
- Scroll the mouse wheel over the Mix knob to step in 1 % increments.

## Troubleshooting

- **Mix is set above 0 % but no reverb is audible** — The Reverb stage may not be enabled in the CHAIN widget. Enable the stage, then re-check Mix.
- **Knob position does not change after editing** — The floating Reverb editor and the REVERB applet sync at 30 Hz. Changes made in one are reflected in the other within one refresh cycle. If they appear out of sync, wait a moment or reopen the applet.

## Related

- [Reverb overview](overview.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)

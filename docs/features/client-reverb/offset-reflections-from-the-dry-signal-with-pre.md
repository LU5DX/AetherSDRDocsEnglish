# Offset reflections from the dry signal with Pre

Use the Pre knob to insert a gap between the dry signal and the first reverb reflections. Increasing Pre makes the reverb tail feel more detached from the voice, which can improve clarity on speech without reducing the overall room effect.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget or the floating Reverb editor. The REVERB sub-container is hidden until the stage is active.
- Open the REVERB sub-container inside the PooDoo Audio (TXDSP) parent container, or double-click the Reverb stage in the CHAIN widget to open the floating Reverb editor.

## Steps

1. Locate the five-knob row in the REVERB sub-container or floating Reverb editor.
2. Find the knob labeled **Pre**.
3. Click and drag the Pre knob upward to increase the pre-delay, or downward to decrease it. Hold Shift while dragging for finer control.
4. Read the current value from the label below the knob, displayed as `X ms`.
5. Release when the label shows the pre-delay you want.

To reset Pre to its default, double-click the knob.

## What each control does

| Control | Default | Valid range | Persisted setting | Behavior |
|---------|---------|-------------|-------------------|----------|
| Pre | 20 ms | 0 to 100 ms | `ClientReverbTxPreDelayMs` | Linear mapping. Sets the delay between the dry signal and the first reverb reflections. Higher values push the tail further behind the voice. |

## Tips

- A Pre value of 0 ms causes reflections to begin immediately, blending closely with the dry voice. Values of 20–40 ms give a more natural room feel on voice.
- The mouse scroll wheel adjusts Pre in 1 % steps of the full range (approximately 1 ms per notch). Shift-drag slows movement to one quarter speed for precise placement.
- Pre works alongside Mix. If the tail sounds like it is swamping the voice, reduce Mix rather than pulling Pre all the way down.

## Related

- [Reverb overview](overview.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

# Tune decay to taste without muddying speech

The Decay knob controls how long the reverb tail rings after each sound. This page explains how to set it to a value that adds presence without smearing speech intelligibility.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget. The REVERB sub-container is hidden until the stage is active.
- Open the REVERB sub-container inside the PooDoo Audio (TXDSP) parent container, or double-click the Reverb stage in the CHAIN widget to open the floating Reverb editor.

## Steps

1. Locate the **Decay** knob in the five-knob REVERB row.
2. Drag the knob upward to increase decay time or downward to decrease it. Hold Shift while dragging for finer control.
3. Watch the label below the knob — it displays the current value in seconds, formatted as `X.XX s`.
4. For voice, start near the default of 1.20 s and reduce toward 0.3 s if consonants begin to blur together.
5. If you want a longer tail for effect, increase toward 2.0–3.0 s, then check intelligibility on a recording or monitor.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---------|---------|-------------|---------------|----------|
| Decay | 1.20 s | 0.3 to 5.0 s | `ClientReverbTxDecayS` | Sets the reverb tail length. Uses exponential mapping across the knob travel (~16.7× range from minimum to maximum). |
| Damp | 50 % | 0.0 to 1.0 | `ClientReverbTxDamping` | Higher values damp high frequencies faster in the tail, softening the character of longer decays. |
| Mix | 15 % | 0.0 to 1.0 | `ClientReverbTxMix` | Dry/wet balance. A lower Mix reduces how much the tail contributes to the transmitted signal. |

## Tips

- Short decay times (0.3–0.8 s) work best for conversational SSB — the tail is audible but clears before the next syllable.
- If a longer Decay still sounds intelligible but feels harsh, raise **Damp** to soften high-frequency energy in the tail without shortening it.
- Reducing **Mix** is an alternative to shortening Decay — the tail length stays the same but sits lower in the overall signal.
- The knob uses exponential mapping, so the first half of the knob travel covers 0.3 to roughly 1.2 s. Most usable voice settings live in the lower half of the knob range.

## Troubleshooting

- **Decay changes have no audible effect** — confirm that the Reverb stage is enabled and that **Mix** (`ClientReverbTxMix`) is above 0 %. A Mix of 0 % passes only dry signal regardless of Decay.
- **Tail does not clear between words** — reduce Decay toward 0.3 s, or raise **Damp** to accelerate high-frequency decay. Also verify that **Pre** (`ClientReverbTxPreDelayMs`) is not set so high that reflections persist into the next word.

## Related

- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Offset reflections from the dry signal with Pre](offset-reflections-from-the-dry-signal-with-pre.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

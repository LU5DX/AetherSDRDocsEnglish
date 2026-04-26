# Reduce the high-end sparkle of the tail with Damp

The **Damp** knob controls how quickly high frequencies fade within the reverb tail. Raising it removes the bright, airy shimmer that can make voice reverb sound unnatural on air.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget. If it is not, the Aetherial FreeVerb applet is hidden and Damp has no effect.
- The Aetherial FreeVerb applet or its floating editor must be visible. See [Aetherial FreeVerb overview](overview.md) if you have not opened it yet.

## Steps

1. Open the Aetherial FreeVerb editor by double-clicking the VERB stage in the CHAIN widget. The frameless window titled "Aetherial FreeVerb — TX" opens.
2. Locate the **Damp** knob — third knob from the left in the five-knob row.
3. Turn **Damp** clockwise to increase damping. Higher values cause high frequencies to decay faster, reducing brightness in the tail.
4. Turn **Damp** counter-clockwise to let high frequencies persist longer, producing a brighter, more open tail.
5. Release the knob. The value is saved immediately to `ClientReverbTxDamping`.

## What each control does

| Control | Default | Range | Persisted key | Behavior |
|---------|---------|-------|---------------|----------|
| Damp | 50 % | 0 % – 100 % | `ClientReverbTxDamping` | Higher values damp high frequencies faster in the reverb tail. Linear mapping. |

## Tips

- A value around 50–70 % suits most voice work. It softens the tail without making the reverb sound muffled.
- If the tail sounds dull or indistinct, lower **Damp** toward 20–30 % to let more high-frequency content through.
- **Damp** interacts with **Decay**: a long decay with low damping produces a bright, lingering tail that can mask speech. Raise **Damp** if you also raise Decay.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

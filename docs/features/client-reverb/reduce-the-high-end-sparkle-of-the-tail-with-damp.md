# Reduce the high-end sparkle of the tail with Damp

The Damp knob controls how quickly high frequencies fade in the reverb tail. Raising it removes the bright, airy quality from longer decays — useful when reverb sounds too metallic or harsh on voice.

## Before you start

- The Reverb applet must be visible. It is hidden until the Reverb stage is enabled via the CHAIN widget or the floating Reverb editor. See [Bypass reverb from the chain](bypass-reverb-from-the-chain.md) if you need to enable the stage first.
- The TXDSP parent container (PooDoo Audio) must be open in the applet panel so the REVERB sub-container is accessible.

## Steps

1. Locate the **REVERB** sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Find the **Damp** knob — the third knob in the five-knob row (Size, Decay, Damp, Pre, Mix).
3. Drag the **Damp** knob upward to increase damping. The label shows the current value as a percentage.
4. Transmit and listen. Higher values cause high frequencies in the tail to decay faster, producing a warmer, darker reverb.
5. Adjust until the tail blends naturally with your voice without sounding dull.

## What each control does

| Control | Default | Valid range | Persisted setting | Behavior |
|---------|---------|-------------|-------------------|----------|
| Damp | 50 % | 0 % to 100 % | `ClientReverbTxDamping` | Linear. Higher values damp high frequencies faster in the reverb tail. 0 % leaves the tail unfiltered; 100 % heavily suppresses high-frequency content throughout the tail. |

## Tips

- Start at the default of 50 % and raise in small increments. For most voice work, values in the 50–70 % range remove harshness without making the tail sound muddy.
- If the tail still sounds too bright after raising Damp, also shorten Decay. The two work together: a long decay at low Damp produces the most high-frequency energy over time.
- Double-click the **Damp** knob to reset it to its default value of 50 %.

## Related

- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Set room size for a small or large-hall feel](set-room-size-for-a-small-or-large-hall-feel.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

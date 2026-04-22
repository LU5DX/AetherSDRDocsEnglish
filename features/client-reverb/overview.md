# Reverb overview

The Reverb applet adds a Freeverb-based reverb tail to your transmitted audio. Use it to add subtle room or hall ambience to voice transmissions before the signal leaves the client.

## Before you start

- The Reverb stage must be enabled via the CHAIN widget or the floating Reverb editor before the applet appears. The applet is hidden until the stage is active.
- Reverb is a client-side TX effect. It processes audio on your computer, not on the radio.

## How it works

The Reverb applet appears as a sub-container labeled **REVERB** inside the PooDoo Audio (TXDSP) parent container. It presents a compact row of five knobs — **Size**, **Decay**, **Damp**, **Pre**, and **Mix** — that together shape the character of the reverb tail applied to your outgoing audio.

Knob values are synchronized with the floating Reverb editor at approximately 30 Hz. Changes made in either the applet or the floating editor are reflected in both places immediately.

To open the floating Reverb editor, double-click the Reverb stage in the CHAIN widget. To float, pop out, or hide the **REVERB** sub-container, right-click its titlebar.

No radio connection is required to adjust Reverb settings.

## What each control does

| Knob | Default | Valid range | Persisted setting | Behavior |
|------|---------|-------------|-------------------|----------|
| **Size** | 50 % | 0 – 100 % | `ClientReverbTxSize` | Sets the modelled room size. Linear mapping. |
| **Decay** | 1.20 s | 0.3 – 5.0 s | `ClientReverbTxDecayS` | Sets the reverb tail length. Exponential mapping; small increases at the low end have more effect than the same movement at the high end. |
| **Damp** | 50 % | 0 – 100 % | `ClientReverbTxDamping` | Controls how quickly high frequencies fade in the tail. Higher values damp high frequencies faster, producing a warmer, darker reverb. Linear mapping. |
| **Pre** | 20 ms | 0 – 100 ms | `ClientReverbTxPreDelayMs` | Sets the pre-delay between the dry signal and the first reflections. Linear mapping. |
| **Mix** | 15 % | 0 – 100 % | `ClientReverbTxMix` | Sets the dry/wet balance. Linear mapping. |

The enabled/disabled state of the reverb stage is persisted in `ClientReverbTxEnabled`.

## Tips

- A Mix of 10–15 % is typical for voice. Higher values become noticeable quickly and can muddy speech intelligibility.
- Short Decay values (0.3–0.8 s) with a small Size produce a tight room effect. Longer Decay values with a large Size approximate a hall.
- Increasing Damp can help tame harshness in the reverb tail without reducing Mix.

## Related

- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Offset reflections from the dry signal with Pre](offset-reflections-from-the-dry-signal-with-pre.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Set room size for a small or large-hall feel](set-room-size-for-a-small-or-large-hall-feel.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)

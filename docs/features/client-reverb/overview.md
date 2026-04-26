# Aetherial FreeVerb Overview

Aetherial FreeVerb adds a Freeverb-based reverb tail to your transmitted audio, giving your voice a sense of room or hall ambience. It applies to the TX path only — there is no RX counterpart.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget inside the Aetherial Audio (TXDSP) applet. The "Aetherial FreeVerb" sub-container and its controls remain hidden until the stage is enabled.
- A radio connection is not required to adjust reverb settings.

## How it works

Aetherial FreeVerb inserts a Freeverb reverb processor into the client-side TX audio chain, after any upstream DSP stages. When the VERB stage is active, the five knobs — Size, Decay, Damp, Pre, and Mix — shape the character and level of the reverb tail added to your transmitted voice.

The controls appear in two places that stay synchronized at approximately 30 Hz:

- **The "Aetherial FreeVerb" sub-container** — a compact five-knob row embedded inside the Aetherial Audio (TXDSP) parent container in the applet panel.
- **The floating editor titled "Aetherial FreeVerb — TX"** — a larger version of the same controls, opened by double-clicking the VERB stage in the CHAIN widget. You can also right-click the "Aetherial FreeVerb" sub-container titlebar to float, pop-out, or hide it.

Turning any knob in either view immediately updates the other. Settings are persisted automatically when you change a knob.

## What each control does

| Knob | Default | Valid range | Behavior | Setting key |
|------|---------|-------------|----------|-------------|
| Size | 50 % | 0–100 % | Sets the modelled room size. Linear mapping. | `ClientReverbTxSize` |
| Decay | 1.20 s | 0.3–5.0 s | Sets the reverb tail length. Exponential mapping — the knob travels from 0.3 s to 5.0 s with finer control at shorter values. | `ClientReverbTxDecayS` |
| Damp | 50 % | 0–100 % | Higher values damp high frequencies faster in the tail, producing a warmer, less bright reverb. Linear mapping. | `ClientReverbTxDamping` |
| Pre | 20 ms | 0–100 ms | Sets the pre-delay between the dry signal and the first reflections. Linear mapping. | `ClientReverbTxPreDelayMs` |
| Mix | 15 % | 0–100 % | Sets the dry/wet balance. 0 % is fully dry; 100 % is fully wet. Linear mapping. | `ClientReverbTxMix` |

The enabled/disabled state of the stage is persisted as `ClientReverbTxEnabled`.

## Tips

- For voice, a Mix of 10–15 % is typical. The default of 15 % is a reasonable starting point.
- High Decay values (above 3 s) can muddy speech. Start at the default 1.20 s and increase only if the room effect sounds too short.
- Raising Damp reduces high-frequency sparkle in the tail, which can help reverb sit behind speech rather than on top of it.
- The floating editor ("Aetherial FreeVerb — TX") provides larger knobs for precise adjustment. Its position and size are saved automatically between sessions.

## Related

- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Set room size for a small or large-hall feel](set-room-size-for-a-small-or-large-hall-feel.md)
- [Offset reflections from the dry signal with Pre](offset-reflections-from-the-dry-signal-with-pre.md)

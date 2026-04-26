# Set room size for a small or large-hall feel

The Size knob controls the modelled room dimensions in the Aetherial FreeVerb TX reverb. Turning it up shifts the character from a tight booth toward a large hall.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget. If the "Aetherial FreeVerb" sub-container is not visible in the Aetherial Audio (TXDSP) panel, enable the VERB stage first.
- A radio connection is not required to adjust reverb parameters.

## Steps

1. Open the reverb controls using one of these two methods:
   - In the Aetherial Audio (TXDSP) panel, locate the "Aetherial FreeVerb" sub-container and adjust the Size knob directly in the compact row.
   - Double-click the VERB stage in the CHAIN widget to open the floating "Aetherial FreeVerb — TX" editor.
2. Turn the Size knob left for a smaller, tighter room character; turn it right for a larger, more spacious hall feel.
3. The knob label updates in real time and shows the current value as a percentage (for example, `50 %`).

## What each control does

| Label | Default | Range | Setting key | Behavior |
|-------|---------|-------|-------------|----------|
| Size | 50 % | 0 % to 100 % | `ClientReverbTxSize` | Sets the modelled room size. Linear mapping. |
| Decay | 1.20 s | 0.3 to 5.0 s | `ClientReverbTxDecayS` | Sets the reverb tail length. Exponential mapping. |
| Damp | 50 % | 0 % to 100 % | `ClientReverbTxDamping` | Higher values damp high frequencies faster in the tail. Linear mapping. |
| Pre | 20 ms | 0 to 100 ms | `ClientReverbTxPreDelayMs` | Pre-delay between the dry signal and the first reflections. Linear mapping. |
| Mix | 15 % | 0 % to 100 % | `ClientReverbTxMix` | Dry/wet balance. Linear mapping. |

## Tips

- Size and Decay interact closely. A large Size with a short Decay sounds unnatural; if you increase Size significantly, consider raising Decay to match.
- Both the compact applet knob and the floating "Aetherial FreeVerb — TX" editor control the same underlying parameters and stay in sync automatically.
- Double-clicking a knob resets it to its default value.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

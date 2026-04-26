# Offset reflections from the dry signal with Pre

The Pre knob adds a gap between the dry signal and the onset of the reverb tail. Use it to keep your voice distinct and upfront while still letting the reverb bloom behind it.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget. The applet is hidden until the stage is active.
- Open the Aetherial FreeVerb applet or the floating editor. To open the editor, double-click the VERB stage in the CHAIN widget; the window is titled "Aetherial FreeVerb — TX".

## Steps

1. Locate the Pre knob in the five-knob row (Size, Decay, Damp, **Pre**, Mix).
2. Turn Pre clockwise to increase the delay between the dry signal and the first reflections, or counter-clockwise to reduce it.
3. Monitor the label beneath the knob; it reads in milliseconds (for example, `20 ms`).
4. Stop when the reverb tail feels separated from your voice without sounding disconnected.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---------|---------|-------------|---------------|----------|
| Pre | 20 ms | 0 to 100 ms | `ClientReverbTxPreDelayMs` | Linear mapping. Sets the time between the dry signal and the first reverb reflections. |

## Tips

- A Pre value of 0 ms causes reflections to start immediately, which can blur transients. Values in the 15–30 ms range are common for voice to preserve intelligibility.
- Pre interacts with Decay: a short Pre with a long Decay can make the tail appear to start before you expect it. Increase Pre if the reverb seems to swallow the leading edge of words.
- Both the compact applet knob (labeled Pre) and the floating editor knob (labeled PreDly) control the same `ClientReverbTxPreDelayMs` setting and stay in sync.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)

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

## Live visualisation

Starting in v0.9.7, the Aetherial FreeVerb applet includes a real-time reverb diagram displayed above the knob row. The visualisation is a compact 90-pixel-tall panel with a dark background and grid lines. It updates immediately whenever you move any of the five knobs.

The diagram shows three overlaid waveform layers:

- **Cyan — dry signal.** A sine packet representing the unprocessed audio. Its amplitude decreases as Mix is raised, reflecting the shift toward the wet signal.
- **Yellow — first-order reflections.** A series of short sine bursts that begin after the pre-delay gap. Their spacing widens as Size increases, and their amplitude decays faster as Damp increases.
- **Magenta — reverberant tail.** An exponentially decaying oscillation that starts at the same offset as the reflections. Its horizontal extent grows with Decay, and higher Damp values cause the tail amplitude to collapse more quickly.

The position at which the yellow and magenta layers begin shifts rightward as you increase Pre, directly showing the gap between the dry signal and the first reflections.

No configuration is required. The visualisation is always visible when the applet is open and the Reverb stage is active.

## Tips

- A Pre value of 0 ms causes reflections to start immediately, which can blur transients. Values in the 15–30 ms range are common for voice to preserve intelligibility.
- Pre interacts with Decay: a short Pre with a long Decay can make the tail appear to start before you expect it. Increase Pre if the reverb seems to swallow the leading edge of words.
- Both the compact applet knob (labeled Pre) and the floating editor knob control the same `ClientReverbTxPreDelayMs` setting and stay in sync.
- Use the live visualisation to confirm that the yellow reflection bursts begin clearly to the right of the cyan dry packet. If the two layers appear to overlap, increase Pre.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
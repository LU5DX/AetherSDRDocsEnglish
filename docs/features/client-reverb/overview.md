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

### Live reverb visualisation

The floating editor includes a compact live visualisation (90 px tall) that updates in real time as you turn the knobs. It depicts three signal components against a dark grid background:

- **Cyan** — the dry signal packet, gradient-faded toward the right.
- **Yellow** — first-order reflections, spaced and damped according to the current Size and Damp values.
- **Magenta** — the reverberant tail, whose length and decay envelope track the Decay and Damp knobs.

The Pre knob shifts the point at which reflections and the tail begin relative to the dry signal. The Mix knob scales the amplitude of both the wet components and the fade of the dry packet. The visualisation matches the layout used by the strip-side reverb panel, so the two views read consistently.

### Inline value editing

Each knob in the Aetherial FreeVerb sub-container and floating editor supports inline value editing. Click a knob's value label to enter edit mode — a subtle cyan border indicates the editor is active. Type a new value using the same units shown in the knob label (for example, "2.50" for Decay, "75" for Size), then press Enter or click elsewhere to commit. The value is automatically clamped to the knob's valid range. Press Escape to cancel the edit and revert to the previous value.

Mouse wheel scrolling continues to work while the editor has focus, so you can fine-tune by scrolling after typing an approximate value.

### Knob color theming

Knob component colors (background ring, value arc, handle/label text) are sourced from the theme system. The applet container uses its own color namespace (`applet/reverb`) so that per-applet color overrides — for example, amber knob foreground in certain themes — are respected at render time. Container-specific colors can be adjusted via the active theme without affecting other knob types in the application.

## What each control does

| Knob                 | Default    | Valid range | Setting key               |
|----------------------|------------|-------------|---------------------------|
| Size                 | 50 %       | 0–100 %     | `ClientReverbTxSize`      |
| Decay                | 1.20 s     | 0.3–5.0 s   | `ClientReverbTxDecayS`    |
| Damp                 | 50 %       | 0–100 %     | `ClientReverbTxDamping`   |
| Pre                  | 20 ms      | 0–100 ms    | `ClientReverbTxPreDelayMs`|
| Mix                  | 15 %       | 0–100 %     | `ClientReverbTxMix`       |

| Indicator               | Behavior                                                                 |
|-------------------------|--------------------------------------------------------------------------|
| Reverb visualisation    | ReverbVizBox — live visualisation showing the dry sine packet (cyan), first-order reflections (yellow), and reverberant tail (magenta). All five knob values feed the rendering so the display follows knob edits in real time. 90 px tall. Replaces the curve widget used by other DSP applets. Rendering algorithm matches StripReverbPanel::GridBox. |

The enabled/disabled state of the stage is persisted as `ClientReverbTxEnabled`.

- **Size** — Sets the modelled room size. Linear mapping from 0 to 100 %. Larger values simulate a larger space.
- **Decay** — Sets the reverb tail length. Exponential mapping from 0.3 to 5.0 s. Higher values produce a longer, more sustained tail.
- **Damp** — Controls how quickly high frequencies decay in the tail. Linear mapping from 0 to 100 %. Higher values damp high frequencies faster, producing a warmer, darker tail.
- **Pre** — Pre-delay between the dry signal and the first reflections. Linear mapping from 0 to 100 ms.
- **Mix** — Dry/wet balance. Linear mapping from 0 to 100 %. Controls the level of the reverb effect relative to the dry signal.

## Tips

- For voice, a Mix of 10–15 % is typical. The default of 15 % is a reasonable starting point.
- High Decay values (above 3 s) can muddy speech. Start at the default 1.20 s and increase only if the room effect sounds too short.
- Raising Damp reduces high-frequency sparkle in the tail, which can help reverb sit behind speech rather than on top of it.
- The floating editor ("Aetherial FreeVerb — TX") provides larger knobs and the live visualisation for precise adjustment. Its position and size are saved automatically between sessions.
- Use the live visualisation to get a rough sense of tail length and reflection density before transmitting. The magenta tail length gives a visual approximation of how Decay and Damp interact.
- Use inline value editing to enter exact values quickly — click the knob value label, type the number, and press Enter. This is especially useful for Decay and Pre where you may want precise times.

## Related

- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Set room size for a small or large-hall feel](set-room-size-for-a-small-or-large-hall-feel.md)
- [Offset reflections from the dry signal with Pre](offset-reflections-from-the-dry-signal-with-pre.md)
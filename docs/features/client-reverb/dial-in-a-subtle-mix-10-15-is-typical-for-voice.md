# Dial in a subtle Mix — 10-15 % is typical for voice

The Mix knob controls the dry/wet balance of the Aetherial FreeVerb reverb on your transmitted audio. Keeping Mix in the 10–15 % range adds a light sense of space without making your voice sound processed or distant.

## Before you start

- The Reverb stage must be enabled in the CHAIN widget. The "Aetherial FreeVerb" sub-container is hidden until the stage is active.
- You can adjust Mix from either the compact applet row inside the Aetherial Audio (TXDSP) container or from the floating "Aetherial FreeVerb — TX" editor.

## Steps

1. Open the floating editor by double-clicking the VERB stage in the CHAIN widget. The editor titled "Aetherial FreeVerb — TX" appears.
2. Locate the Mix knob — the rightmost of the five knobs in the editor row.
3. Turn Mix to your target value. The knob label updates in real time, displayed as a percentage (for example, `15 %`). You can also click the value text and type a numeric value directly — press Enter or click elsewhere to commit.
4. For voice, set Mix between 10 % and 15 %. Lower values blend in less reverb tail; higher values make the effect more prominent.
5. Close the editor or leave it open. The value is saved immediately.

## What each control does

| Label                | Default | Valid range | Notes |
|----------------------|---------|-------------|-------|
| Mix                  | 15 % | 0–100 % (0.0 to 1.0) | Linear mapping. Dry / wet balance. |
| Size                 | 50 % | 0–100 % (0.0 to 1.0) | Linear mapping. Sets the modelled room size. |
| Decay                | 1.20 s | 0.3 to 5.0 s | Exponential mapping (0.3 * (5.0/0.3)^n, ~16.7x). Sets the reverb tail length. |
| Damp                 | 50 % | 0–100 % (0.0 to 1.0) | Linear mapping. Higher values damp high frequencies faster in the tail. |
| Pre                  | 20 ms | 0 to 100 ms | Linear mapping. Pre-delay between the dry signal and the first reflections. |
| Reverb visualisation | ReverbVizBox — live visualisation showing the dry sine packet (cyan), first-order reflections (yellow), and reverberant tail (magenta). All five knob values feed the rendering so the display follows knob edits in real time. 90 px tall. | Replaces the curve widget used by other DSP applets. Rendering algorithm matches StripReverbPanel::GridBox. |

## Inline value editing

v26.5.2.1 adds inline value editing to all knob controls in the "Aetherial FreeVerb — TX" editor. Click the numeric value displayed below a knob to open a text input field. Type a new value and press Enter, or click anywhere outside the editor, to commit the change. The value is clamped to the knob's valid range automatically.

To cancel an edit, press the Escape key before committing. The knob reverts to its previous value.

## Live visualisation

v0.9.7 adds a small reverb visualisation inside the "Aetherial FreeVerb — TX" editor. It appears as a 90-pixel-tall waveform display above the knob row and updates in real time as you turn any knob.

The display uses three colour-coded layers:

| Colour | What it represents |
|--------|--------------------|
| Cyan | Dry signal — a sine packet that fades toward the right as Mix increases. |
| Yellow | First-order reflections — short bursts whose spacing widens with Size and whose amplitude falls off with Damp. |
| Magenta | Reverberant tail — an exponentially decaying oscillation whose length tracks Decay and whose onset position tracks Pre. |

The visualisation is read-only. It does not add or remove any processing; it reflects the current knob values only. The layout algorithm matches the reverb panel on the strip side, so the two views read consistently when both are open at the same time.

## Tips

- The default Mix value is 15 %, which is already within the typical voice range. If you reset the knob to default, it returns to 15 %.
- Both the compact applet knob and the floating editor knob stay in sync. Changes made in one are reflected in the other within approximately 33 ms.
- Mix at 0 % passes only dry signal; the reverb stage is still active but inaudible. To remove it from the processing chain entirely, see [Bypass reverb from the chain](bypass-reverb-from-the-chain.md).
- Use the live visualisation to get a quick read on how Decay and Damp interact: a long, bright tail in the display corresponds to a long, high-frequency-rich reverb in the transmitted audio.
- Inline editing supports both dot-decimal and comma-decimal number formats. For example, entering `1,5` and `1.5` both produce the same value on systems configured for European decimal notation.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Reduce the high-end sparkle of the tail with Damp](reduce-the-high-end-sparkle-of-the-tail-with-damp.md)
- [Offset reflections from the dry signal with Pre](offset-reflections-from-the-dry-signal-with-pre.md)
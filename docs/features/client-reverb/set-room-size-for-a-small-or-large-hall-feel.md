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
4. To type an exact value, click the value label below the knob. The label transforms into an inline text editor with a cyan border. Type the desired number and press Enter. The value is clamped to the valid range. Clicking elsewhere (focus-out) also commits the edit.

## Live visualisation

The "Aetherial FreeVerb — TX" editor includes a compact waveform display (90 px tall) that updates in real time as you adjust any of the five knobs. It shows three overlaid signal layers:

- **Cyan** — the dry sine packet. Its amplitude decreases as Mix is raised.
- **Yellow** — first-order reflections. Spacing and count reflect the Size and Damp settings.
- **Magenta** — the reverberant tail. Length tracks Decay; damping of high frequencies tracks Damp; onset position tracks Pre-delay.

The display uses a dark background with a subtle grid. No interaction is required; it updates automatically whenever a knob value changes.

## What each control does

| Label                | Default | Range | Behavior | Notes |
|----------------------|---------|-------|----------|-------|
| Size                 | 50 %    | 0 % to 100 % | Linear mapping. Sets the modelled room size. | Label displayed as percentage. |
| Decay                | 1.20 s  | 0.3 to 5.0 s | Exponential mapping (0.3 * (5.0/0.3)^n, ~16.7x). Sets the reverb tail length. | Label 'X.XX s'. |
| Damp                 | 50 %    | 0 % to 100 % | Linear mapping. Higher values damp high frequencies faster in the tail. | Label displayed as percentage. |
| Pre                  | 20 ms   | 0 to 100 ms | Linear mapping. Pre-delay between the dry signal and the first reflections. | Label 'X ms'. |
| Mix                  | 15 %    | 0 % to 100 % | Linear mapping. Dry / wet balance. | Label displayed as percentage. |
| Reverb visualisation | ReverbVizBox — live visualisation showing the dry sine packet (cyan), first-order reflections (yellow), and reverberant tail (magenta). All five knob values feed the rendering so the display follows knob edits in real time. 90 px tall. | Always visible | Replaces the curve widget used by other DSP applets. Rendering algorithm matches StripReverbPanel::GridBox. | Background grid with crosshairs at centre for spatial reference. |

## Visualisation indicators

| Indicator | States | Meaning |
|-----------|--------|---------|
| Dry sine packet | Visible, cyan, gradient-faded | Dry signal visualised as a sine packet. Cyan, with a horizontal gradient fading to transparent rightward. |
| First-order reflections | Visible, yellow pulses | Early reflections shown as yellow decaying sine bursts, spacing and amplitude driven by Size and Damping values. |
| Reverberant tail | Visible, magenta, exponentially decaying | Reverb tail drawn as a magenta sine wave with exponential decay, length determined by Decay and Damping. |
| Background grid | Always visible | Thin dashed-grid background with crosshairs at centre for spatial reference. |

## Inline value editing

Every knob supports direct numeric entry:

1. Click the value label below the knob. The label transforms into a text editor with a dark background and cyan border.
2. Type the desired value. Locale-aware parsing supports both decimal point and comma formats (for example, `0.5` or `0,5`). Extra non-numeric characters are automatically stripped.
3. Press Enter to commit, or click elsewhere to apply the value. The value is clamped to the knob's valid range.
4. To cancel without changing the value, press Escape.
5. While the editor is focused, mouse wheel events still adjust the knob normally.

## Tips

- Size and Decay interact closely. A large Size with a short Decay sounds unnatural; if you increase Size significantly, consider raising Decay to match.
- The live visualisation in the floating editor gives immediate feedback on how Size, Decay, Damp, Pre-delay, and Mix interact before you transmit.
- Both the compact applet knob and the floating "Aetherial FreeVerb — TX" editor control the same underlying parameters and stay in sync automatically.
- Double-clicking a knob resets it to its default value.
- Use inline editing for precise numeric values rather than relying on knob rotation alone.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
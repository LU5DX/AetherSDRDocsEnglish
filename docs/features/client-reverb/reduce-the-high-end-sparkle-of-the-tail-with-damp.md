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

| Control              | Default | Range      | Setting key               | Notes                                                                                            |
|----------------------|---------|------------|---------------------------|--------------------------------------------------------------------------------------------------|
| Size                 | 50 %    | 0 % – 100 % | `ClientReverbTxSize`      | Linear mapping. Sets the modelled room size. Label displayed as percentage.                      |
| Decay                | 1.20 s  | 0.3 – 5.0 s | `ClientReverbTxDecayS`    | Exponential mapping (0.3 * (5.0/0.3)^n, ~16.7x). Label 'X.XX s'.                                |
| Damp                 | 50 %    | 0 % – 100 % | `ClientReverbTxDamping`   | Linear mapping. Higher values damp high frequencies faster in the tail. Label displayed as percentage. |
| Pre                  | 20 ms   | 0 – 100 ms  | `ClientReverbTxPreDelayMs`| Linear mapping. Pre-delay between the dry signal and the first reflections. Label 'X ms'.         |
| Mix                  | 15 %    | 0 % – 100 % | `ClientReverbTxMix`       | Linear mapping. Dry / wet balance. Label displayed as percentage.                                |
| Reverb visualisation | —       | —           | —                         | ReverbVizBox — live visualisation showing the dry sine packet (cyan), first-order reflections (yellow), and reverberant tail (magenta). 90 px tall. |

## Live visualisation

The Aetherial FreeVerb editor displays a compact real-time diagram (90 px tall) above the knob row. It updates immediately as you adjust any knob and shows three overlaid elements:

| Element | Colour | What it represents |
|---------|--------|--------------------|
| Dry sine packet | Cyan, gradient-faded to the right | The unprocessed signal passing through |
| First-order reflections | Yellow | Early reflections; spacing set by Size, amplitude by Mix and Damp |
| Reverberant tail | Magenta | The full reverb tail; length set by Decay, brightness by Damp |

The visualisation is purely informational. It does not affect audio processing.

### How Damp appears in the visualisation

- Raising **Damp** causes the magenta tail to decay more steeply and reduces the amplitude of successive yellow reflection bursts.
- Lowering **Damp** produces a flatter magenta decay curve and more even yellow reflection amplitudes.

## Themes and knob colours

The Aetherial FreeVerb applet uses a dedicated theme container (`applet/reverb`) for its knob components. This enables per-applet colour overrides. The following knob colours are drawn from the theme system:

| Theme key | Purpose |
|-----------|---------|
| `color.knob.background` | Background ring of the knob |
| `color.knob.foreground` | Value arc showing current setting |
| `color.knob.handle` | Pointer line from centre to arc |
| `color.text.secondary` | Label text below the knob |
| `color.text.primary` | Value text displayed in the knob centre |

If you change themes, knob colours update automatically. Custom theme files can assign distinct colours to the `applet/reverb` container to make the reverb knobs visually distinct from other DSP knobs.

## Tips

- A value around 50–70 % suits most voice work. It softens the tail without making the reverb sound muffled.
- If the tail sounds dull or indistinct, lower **Damp** toward 20–30 % to let more high-frequency content through.
- **Damp** interacts with **Decay**: a long decay with low damping produces a bright, lingering tail that can mask speech. Raise **Damp** if you also raise Decay.
- Use the live visualisation to confirm the interaction between **Damp** and **Decay** before transmitting.

## Related

- [Aetherial FreeVerb overview](overview.md)
- [Tune decay to taste without muddying speech](tune-decay-to-taste-without-muddying-speech.md)
- [Dial in a subtle Mix — 10-15 % is typical for voice](dial-in-a-subtle-mix-10-15-is-typical-for-voice.md)
- [Bypass reverb from the chain](bypass-reverb-from-the-chain.md)
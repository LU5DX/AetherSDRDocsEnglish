# Select the de-esser slope sharpness (12/24/36/48 dB/oct)

Choose how aggressively the de-esser's sidechain filter attenuates frequencies outside the sibilant band. Higher slope values produce a sharper cutoff, reducing collateral attenuation on mid-range frequencies.

## Before you start

- The de-esser must be enabled in the audio chain (single-click DESS in the CHAIN widget).
- Open the De-Ess editor by double-clicking DESS in the CHAIN widget, or open the Aetherial Audio Channel Strip and double-click DESS in the RX chain for the RX De-Ess editor.

## Steps

1. In the De-Ess editor (titled "Aetherial De-Esser — TX" or "Aetherial De-Esser — RX"), locate the **Slope** push button in the left column, bottom area.
2. Click the **Slope** push button. Each click cycles to the next value: 12 dB/oct → 24 dB/oct → 36 dB/oct → 48 dB/oct, then wraps back.
3. The button label updates to show the current slope, e.g. "24 dB/oct".
4. Speak a sibilant phrase (e.g. "Sally sells sea shells") and listen for the most natural sound with minimal attenuation on non-sibilant parts of your voice.

## What each control does

| Control | Label                 | Description                                                                                                  |
|---------|-----------------------|--------------------------------------------------------------------------------------------------------------|
| Slope   | **Slope** push button | Cycles the sidechain bandpass cascade count. Each stage adds 12 dB/oct of rolloff outside the sibilant band. |

## Tips

- Start with **24 dB/oct** (2 stages) — this provides a good balance between sharp cutoff and smooth sound.
- For heavy sibilance that triggers on many words, try **12 dB/oct** — the gentler slope preserves more natural timbre.
- For extreme "S" sounds on an otherwise clear voice, **48 dB/oct** can target only the harshest sibilant band with minimal mid-band impact.

## Gain-reduction meter smoothing (v26.6.3 – v26.7.4)

Beginning in v26.6.3, the gain-reduction meter uses an improved smoothing algorithm. The meter animation timer now stops when the gain-reduction value has settled, reducing unnecessary repaints. The meter redraws only when the smoothed value or a pending repaint flag indicates a visual change is needed. This optimization applies to both the docked Aetherial De-Esser applet and the Aetherial De-Esser — RX instance accessible through the Aetherial Audio Channel Strip.

Beginning in v26.7.4, the meter repaints every animation tick regardless of whether the value has settled or the smoothed indicator needs repainting. This ensures the sidechain response curve and gain-reduction bar remain visually responsive at all times, even when the gain-reduction value has fully settled. The edit-style push button used in earlier versions has been removed; the Slope button now uses the standard applet button style.

## Color theming (v26.6.1)

Beginning in v26.6.1, the De-Ess editor and its internal widgets (the sidechain response curve, knobs, and gain-reduction meter) read colors from the theme engine. The editor container registers under the `applet/deess` container key, so theme authors can assign distinct colors to the De-Ess editor panel. Curve colors (axis labels, grid lines, bandpass curve, threshold line, and centre-frequency ball) use the same theme namespace as other Aetherial applets. Knob components (arc, background ring, pointer, and labels) read from `color.knob.*`.

## Related

- [Aetherial De-Esser overview](overview.md)
- [Narrow or widen the sidechain band with Q](narrow-or-widen-the-sidechain-band-with-q.md)
- [Sweep Freq to locate peak sibilance](sweep-freq-to-locate-peak-sibilance.md)
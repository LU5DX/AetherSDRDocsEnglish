# Overlay a reference mic or intelligibility curve as a visual EQ target

This page shows you how to display a reference frequency-response curve—such as the AT&T 1959 intelligibility target or the response of a famous SSB microphone—on the EQ canvas while you tune bands. The curve is a visual guide only; it does not affect EQ math.

## Before you start

- Open the Aetherial Parametric EQ editor by double-clicking the EQ stage in the CHAIN widget (TX or RX side).
- The editor window is titled "Aetherial Parametric EQ — TX" or "— RX" depending on which side you opened.

## Steps

1. In the floating editor's header strip, locate the **Ref:** combo box.
2. Click the **Ref:** combo box and select one of the following:
   - **Off** (default) — no reference curve
   - **AT&T 1959** — Bell Labs intelligibility target, +5 dB at 2.5 kHz
   - **Heil DX** — aggressive presence boost for SSB contests
   - **Astatic D-104** — classic lollipop mic, sharp peak at 3 kHz
   - **Shure 444** — broadcast-style desk mic, gentler boost
   - **Heil HC-5** — modern dynamic SSB element
3. The selected curve appears as a thin amber line on the EQ canvas.
4. Adjust your EQ bands to match the reference curve, or use it as a rough shape for your target response.
5. To remove the overlay, select **Off** from the **Ref:** combo box.

## What each control does

| Control | Default | Valid range | Persisted setting key | Behavior |
|---|---|---|---|---|
| **Ref:** combo | Off | Off \| AT&T 1959 \| Heil DX \| Astatic D-104 \| Shure 444 \| Heil HC-5 | `ClientEqReferenceCurve` | Overlays a reference target curve on the EQ canvas as a thin amber line. Shared between RX and TX editors. |
| **Smoothing:** combo | Off (1/96) | Off (1/96) \| 1/24 \| 1/12 \| 1/6 \| 1/3 | `ClientEqSmoothingFraction` | Applies fractional-octave power-averaging to the analyzer trace for display. Does not affect EQ math. Shared between RX and TX editors. |

## Tips

- The reference curve is display-only—it never changes the audio path, so feel free to experiment with different presets.
- The selection persists globally; choosing a curve in the TX editor also affects the RX editor's display.
- Combine the reference curve with **Peak Hold** to compare your band shaping against a sustained look at the audio actually passing through.

## Related

- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Smooth the analyzer display for easier reading with the Smoothing combo](smooth-the-analyzer-display-for-easier-reading-with-the-smoothing-combo.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)

# Parametric EQ (Client) overview

The Parametric EQ (Client) feature provides a client-side parametric equalizer for both the receive and transmit audio paths. Use it to shape the frequency response of audio passing through AetherSDR without touching the radio's own DSP chain.

## Before you start

- AetherSDR must be running. A radio connection is not required to configure the EQ, but a live audio path is needed for the analyzer overlay to show signal.
- The EQ applet is hidden by default. Enable the EQ stage from the CHAIN widget or the floating editor to make the applet visible.

## How it works

AetherSDR runs one EQ instance for the receive path and one for the transmit path. Each instance is independent: it has its own set of bands, its own enabled/bypassed state, and its own persisted settings.

The **CEQ** sub-container sits inside the PooDoo Audio (TXDSP) parent container in the applet panel. It displays a compact curve and analyzer area (110 px tall) for whichever path it is bound to. There is one applet tile per path — the RX-bound tile shows the RX EQ; the TX-bound tile shows the TX EQ. Neither tile contains an internal path selector; the chain widget's tab determines which side you are editing.

Actual band editing — adding, removing, and tuning bands — happens in the floating **ClientEqEditor** window, not in the applet tile itself. Open it by double-clicking the EQ stage in the CHAIN widget. The applet tile is a read-only view: it shows the current state of the path but does not accept clicks to move or edit bands.

The curve area renders two layers simultaneously:

- **Summed EQ response** — the cumulative frequency response of all enabled bands for the bound path. When no bands are configured, the area displays "(no bands — add one in the editor)". When no EQ is connected, it displays "(no EQ connected)".
- **Live FFT analyzer overlay** — a real-time FFT of the audio passing through the bound path, drawn as a filled cyan gradient. The vertical scale runs from −70 dB at the bottom to 0 dB at the top. The horizontal scale is logarithmic from 20 Hz to 20 kHz.

The frequency grid draws vertical lines at 20, 50, 100, 200, 500, 1k, 2k, 5k, 10k, and 20k Hz. Horizontal dB reference lines appear at ±6 dB and ±12 dB, with a brighter line at 0 dB.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| RX tab | Tab | Checked | Binds the curve widget to the RX EQ instance. Mutually exclusive with TX. | — |
| TX tab | Tab | Unchecked | Binds the curve widget to the TX EQ instance. Mutually exclusive with RX. | — |
| Analyzer / curve area | Indicator (view-only) | — | Displays the summed EQ response and live FFT analyzer overlay for the selected path. Editing happens in the floating ClientEqEditor. | — |
| `ClientEqRxEnabled` | Persisted setting | — | Stores the enabled/bypassed state of the RX EQ. | `ClientEqRxEnabled` |
| `ClientEqTxEnabled` | Persisted setting | — | Stores the enabled/bypassed state of the TX EQ. | `ClientEqTxEnabled` |
| `ClientEqRxBands` | Persisted setting | — | Stores the band configuration for the RX EQ. | `ClientEqRxBands` |
| `ClientEqTxBands` | Persisted setting | — | Stores the band configuration for the TX EQ. | `ClientEqTxBands` |

## Tips

- Right-click the **CEQ** sub-container titlebar to float, pop out, or hide the applet tile if you need more screen space.
- The summed EQ response is computed from analog-prototype transfer functions across the full 20 Hz–20 kHz range. The curve is an ideal reference; the audio path uses the equivalent digital biquads.
- Band colors follow a fixed palette (gray, amber, yellow, green, teal, blue, purple, gray). With more than 8 bands, colors wrap rather than repeat from gray.

## Related

- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [See the live spectrum of the selected path](see-the-live-spectrum-of-the-selected-path.md)
- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)

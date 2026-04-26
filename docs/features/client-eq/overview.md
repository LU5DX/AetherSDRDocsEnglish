# Aetherial Parametric EQ (TX / RX) Overview

The Aetherial Parametric EQ is a client-side parametric equalizer that processes audio independently on the transmit and receive paths. Use it to shape your transmitted signal or your received audio without touching any radio-side DSP settings.

## Before you start

- AetherSDR must be running. A radio connection is not required for configuration, but the live FFT analyzer only shows signal when audio is flowing.
- The EQ tiles ("Aetherial TX EQ" and "Aetherial RX EQ") are hidden until the matching EQ stage is enabled via the CHAIN widget or the floating editor. Enable the EQ stage first if you do not see the tiles.

## How it works

AetherSDR instantiates two separate EQ copies: one bound permanently to the TX path ("Aetherial TX EQ") and one bound permanently to the RX path ("Aetherial RX EQ"). Each lives inside the Aetherial Audio (TXDSP) parent container. There is no in-tile selector for switching between paths — each tile is locked to its side at construction.

**Applet tiles (docked view)**

Each tile contains a single read-only analyzer and curve area. The tile shows the summed EQ response for its path and a live FFT analyzer overlay. You cannot edit bands directly in the tile; all band editing happens in the floating editor.

**Floating editor**

Double-clicking the EQ stage in the CHAIN widget opens the frameless floating editor, titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX" depending on which side you opened. A single editor window is reused for both sides; its title updates to reflect the active path.

The floating editor contains:

- An interaction hint strip at the top describing drag gestures.
- A filter family selector (see table below).
- An icon row, an editable canvas, and a parameter row for adding, removing, and tuning bands.
- An output fader on the right with a level meter and dB readout.

The FFT analyzer in the editor runs at 25 Hz while the editor is visible and stops when it is closed.

**Bypass**

Bypassing an EQ stage is done from the CHAIN widget, not from inside the tile or the floating editor.

## What each control does

### Applet tile controls

| Control | Description | Persisted setting |
|---|---|---|
| Analyzer / curve area | Read-only display, 110 px tall. Shows the summed EQ response curve and a live FFT analyzer overlay for this tile's path. | — |

### Floating editor controls

| Control | Default | Valid values | Persisted setting |
|---|---|---|---|
| Filter family | Butterworth | Butterworth, Chebyshev, Bessel, Elliptic | `ClientEqTxBands` / `ClientEqRxBands` (saved with band data) |
| Output fader | — | Linear gain, shown as dB | `ClientEqTxBands` / `ClientEqRxBands` |
| RX EQ enabled | — | On / bypassed | `ClientEqRxEnabled` |
| TX EQ enabled | — | On / bypassed | `ClientEqTxEnabled` |
| Band definitions (RX) | — | Added/removed interactively in the canvas | `ClientEqRxBands` |
| Band definitions (TX) | — | Added/removed interactively in the canvas | `ClientEqTxBands` |

**Filter family options**

| Option | Behavior |
|---|---|
| Butterworth | Maximally flat passband |
| Chebyshev | Steeper transition, 1 dB passband ripple |
| Bessel | Linear phase, gentler rolloff |
| Elliptic | Steepest transition, ripple in both bands |

The filter family selector applies to HP/LP cascade math. Shelves and peaks use their native second-order topology regardless of this setting.

**Summed EQ response indicator**

Shows the cumulative frequency response of all enabled bands for the tile's path. Displays as flat when no bands are active or all bands are at 0 dB gain, and shaped when bands are contributing to the response.

**Live analyzer overlay**

Displays a real-time FFT of audio passing through the tile's path. Idle when no audio is flowing; running when audio is present.

## Tips

- Right-click the "Aetherial TX EQ" or "Aetherial RX EQ" sub-container titlebar to float, pop out, or hide the tile.
- In the floating editor canvas: drag a peak or shelf band to adjust frequency and gain; hold Shift while dragging to adjust Q. Drag an HP or LP band to adjust frequency and Q. Click a band icon to cycle through filter types.
- The output fader in the floating editor controls master gain for that EQ path after all bands are summed.

## Troubleshooting

- **The "Aetherial TX EQ" or "Aetherial RX EQ" tile is not visible** — The tile is hidden until the matching EQ stage is enabled. Enable the stage from the CHAIN widget or from the floating editor.
- **The live FFT analyzer shows nothing** — Audio must be flowing through the path for the analyzer to display signal. Confirm the radio is connected and audio routing is active for that path.
- **The floating editor title does not match the side you want to edit** — The editor is shared between both paths. Open the editor by double-clicking the correct EQ stage (TX or RX) in the CHAIN widget to switch it to that side.

## Related

- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)

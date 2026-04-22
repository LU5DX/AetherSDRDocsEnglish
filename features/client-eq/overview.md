# Parametric EQ (Client) overview

The Parametric EQ (Client) applet applies a client-side parametric equalizer to your receive and transmit audio paths independently. Use it to shape audio before it reaches your speakers or microphone chain, without touching the radio's own DSP.

## Before you start

- The applet is housed inside the PooDoo Audio (TXDSP) parent container as the "CEQ" sub-container. It is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor.
- No radio connection is required to configure the EQ.

## How it works

The applet presents a compact view of one audio path at a time — either RX or TX. The **RX** and **TX** tabs at the top of the applet select which path is displayed. Switching tabs rebinds the curve area to that path's EQ instance; it does not bypass or alter either path.

The main area of the applet is the analyzer and curve display. It is 110 pixels tall and shows two layers at once:

- **Summed EQ response** — the combined frequency response of all enabled bands for the selected path. The curve is flat when no bands are active or all are bypassed, and shaped when one or more bands are contributing gain or cut.
- **Live FFT analyzer overlay** — a real-time spectrum of audio flowing through the selected path. This overlay is idle when no audio is present and running when audio is active.

The curve area is view-only. To add, remove, or tune bands, open the floating editor by double-clicking the EQ stage in the CHAIN widget.

Bypass (enabling and disabling the EQ stage entirely) is controlled from the CHAIN widget, not from within the applet itself.

## What each control does

| Control | Kind | Default | Behavior | Persisted setting |
|---|---|---|---|---|
| **RX** | Tab | Checked | Selects the receive path; binds the curve area to the RX EQ instance. Mutually exclusive with TX. | — |
| **TX** | Tab | Unchecked | Selects the transmit path; binds the curve area to the TX EQ instance. Mutually exclusive with RX. | — |
| Analyzer / curve area | Indicator | — | Displays the summed EQ response and live FFT analyzer overlay for the selected path. View-only. | — |
| RX enabled state | — | — | Whether the RX EQ stage is active or bypassed. Controlled via the CHAIN widget. | `ClientEqRxEnabled` |
| TX enabled state | — | — | Whether the TX EQ stage is active or bypassed. Controlled via the CHAIN widget. | `ClientEqTxEnabled` |
| RX band configuration | — | — | Frequency, gain, Q, and type for each band on the RX path. Edited in the floating editor. | `ClientEqRxBands` |
| TX band configuration | — | — | Frequency, gain, Q, and type for each band on the TX path. Edited in the floating editor. | `ClientEqTxBands` |

## Tips

- The curve area vertical range is ±18 dB. Horizontal gridlines appear at ±6 dB and ±12 dB; the 0 dB reference line is drawn slightly brighter.
- Frequency gridlines are placed at 20, 50, 100, 200, 500, 1k, 2k, 5k, 10k, and 20k Hz.
- The RX and TX paths are independent. Switching the tab to check one path does not affect what the other path is doing.
- Right-click the "CEQ" sub-container titlebar to float, pop out, or hide the applet if you need more screen space.

## Related

- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [See the live spectrum of the selected path](see-the-live-spectrum-of-the-selected-path.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)

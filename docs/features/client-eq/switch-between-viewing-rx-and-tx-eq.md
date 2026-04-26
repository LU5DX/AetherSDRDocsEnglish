# Switch between viewing RX and TX EQ

The ClientEqApplet shows one EQ path at a time — either the receive path or the transmit path. This page explains how to switch which path the curve widget displays.

## Before you start

- The CEQ sub-container must be visible inside the PooDoo Audio (TXDSP) parent container. It is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor.
- The applet panel must be open (`View > Applet Panel`).

## Steps

1. Locate the **CEQ** tile in the applet panel.
2. Click the **RX** tab to display the receive-path EQ curve and analyzer.
3. Click the **TX** tab to display the transmit-path EQ curve and analyzer.

The curve widget immediately rebinds to the selected path. The summed EQ response and the live FFT analyzer overlay both update to reflect that path.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| **RX** | Tab | Checked | Binds the curve widget to the RX EQ instance. Mutually exclusive with TX. | — |
| **TX** | Tab | Unchecked | Binds the curve widget to the TX EQ instance. Mutually exclusive with RX. | — |
| Analyzer / curve area | Indicator | — | 110 px tall. Shows the summed EQ response for the selected path overlaid with a live FFT analyzer. View-only. | — |

The enabled state and band configuration for each path are persisted separately: `ClientEqRxEnabled`, `ClientEqTxEnabled`, `ClientEqRxBands`, and `ClientEqTxBands`.

## Tips

- Switching tabs does not affect processing. Both RX and TX EQ paths continue to run regardless of which one is displayed.
- Editing bands requires opening the floating editor. Double-click the EQ stage in the CHAIN widget to open it. The curve area in the applet is view-only.

## Related

- [Parametric EQ (Client) overview](overview.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [See the live spectrum of the selected path](see-the-live-spectrum-of-the-selected-path.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)

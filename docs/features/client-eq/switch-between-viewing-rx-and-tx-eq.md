# Switch between viewing RX and TX EQ

The ClientEqApplet shows the EQ curve and live analyzer for one audio path at a time. Use the RX and TX tabs to choose which path — receive or transmit — is displayed in the curve area.

## Before you start

- The ClientEqApplet (labeled "CEQ") must be visible in the applet panel. It is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor.

## Steps

1. Locate the "CEQ" sub-container in the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Click **RX** to display the receive-path EQ curve and analyzer. This tab is checked by default.
3. Click **TX** to display the transmit-path EQ curve and analyzer.

The curve area updates immediately to show the summed EQ response and live FFT overlay for the selected path. Only one tab can be active at a time.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| **RX** | Tab | Checked | Selects the receive path; binds the curve area to the RX EQ instance. | — |
| **TX** | Tab | Unchecked | Selects the transmit path; binds the curve area to the TX EQ instance. | — |
| Analyzer / curve area | Indicator (view-only) | — | 110 px tall. Shows a frequency grid, the summed EQ response for the selected path, and a live FFT analyzer overlay. Editing is done in the floating editor, not here. | — |

Persisted settings that store each path's state: `ClientEqRxEnabled`, `ClientEqTxEnabled`, `ClientEqRxBands`, `ClientEqTxBands`.

## Tips

- Switching tabs does not affect whether either path's EQ is enabled or bypassed — it only changes which path is shown.
- To edit bands on the currently displayed path, open the floating editor. See [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md).

## Related

- [Parametric EQ (Client) overview](overview.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [See the live spectrum of the selected path](see-the-live-spectrum-of-the-selected-path.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)

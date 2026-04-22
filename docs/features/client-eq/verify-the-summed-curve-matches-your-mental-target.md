# Verify the summed curve matches your mental target

Use the ClientEqApplet's analyzer/curve area to confirm that the combined effect of all your EQ bands produces the frequency response shape you intended, for either the RX or TX path.

## Before you start

- The CEQ applet must be visible. It is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor.
- At least one band must be configured in the floating editor so the summed EQ response is non-flat.

## Steps

1. Locate the CEQ sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Click the **RX** tab to inspect the receive-path EQ, or click the **TX** tab to inspect the transmit-path EQ.
3. Look at the analyzer/curve area — the 110 px tall display that fills the lower portion of the applet.
4. Read the summed EQ response line. It shows the cumulative frequency response of all enabled bands for the selected path, drawn over a frequency grid spanning 20 Hz to 20 kHz and a vertical range of ±18 dB.
5. Compare the curve shape against your intended target. Horizontal dB gridlines appear at 0, ±6, and ±12 dB as reference markers. Frequency gridlines appear at 20, 50, 100, 200, 500, 1k, 2k, 5k, 10k, and 20k Hz.
6. If the curve does not match your target, double-click the EQ stage in the CHAIN widget to open the floating editor and adjust your bands. Return to the applet to re-verify after each change.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| RX | Tab | Checked | Binds the analyzer/curve area to the receive-path EQ. | — |
| TX | Tab | Unchecked | Binds the analyzer/curve area to the transmit-path EQ. | — |
| Analyzer/curve area | Indicator (view-only) | — | Displays the summed EQ response for the selected path overlaid with a live FFT analyzer. Frequency axis: 20 Hz–20 kHz (log). Vertical axis: ±18 dB. | — |

Persisted settings that affect what the curve reflects:

| Setting key | What it controls |
|---|---|
| `ClientEqRxEnabled` | Whether the RX EQ stage is active |
| `ClientEqTxEnabled` | Whether the TX EQ stage is active |
| `ClientEqRxBands` | Saved band parameters for the RX path |
| `ClientEqTxBands` | Saved band parameters for the TX path |

## Tips

- The analyzer/curve area is view-only. All editing — adding, removing, and tuning bands — happens in the floating ClientEqEditor, not in the applet.
- The live FFT analyzer overlay shows audio actually flowing through the selected path post-EQ. If the overlay is idle, no audio is passing through that path at the moment.
- The 0 dB reference line is drawn slightly brighter than the other dB gridlines, making it easy to spot boost and cut symmetry at a glance.
- Right-click the CEQ sub-container titlebar to float or pop out the applet if you want to position it alongside the floating editor.

## Troubleshooting

- **The analyzer/curve area is not visible** — The CEQ applet hides itself until the EQ stage is enabled. Enable the EQ stage from the CHAIN widget or the floating editor, then check that the applet panel is visible via `View > Applet Panel`.
- **The summed response line is flat** — No bands are enabled for the selected path, or all bands have 0 dB gain. Open the floating editor to confirm band settings are saved under `ClientEqRxBands` or `ClientEqTxBands` for the path you are viewing.
- **The curve shows a shape but bypassing the EQ stage sounds identical** — `ClientEqRxEnabled` or `ClientEqTxEnabled` may be off. Verify the EQ stage is not bypassed in the CHAIN widget.

## Related

- [Parametric EQ (Client) overview](overview.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [See the live spectrum of the selected path](see-the-live-spectrum-of-the-selected-path.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)

# See the live spectrum of the selected path

The analyzer / curve area in the ClientEq applet shows a real-time FFT of audio passing through the selected RX or TX path, overlaid with the summed EQ response. Use this to watch how your EQ is affecting live audio without opening the floating editor.

## Before you start

- The CEQ applet must be visible. It is hidden until the EQ stage is enabled via the CHAIN widget or the floating editor. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md) if the applet is not showing.
- Audio must be flowing through the path you want to observe for the live FFT overlay to be active rather than idle.

## Steps

1. Locate the CEQ sub-container inside the PooDoo Audio (TXDSP) parent container in the applet panel.
2. Click the **RX** tab to view the receive path, or click the **TX** tab to view the transmit path.
3. Observe the analyzer / curve area. The live FFT overlay appears as a filled gradient behind the summed EQ response curve. The horizontal axis runs from 20 Hz to 20 kHz on a logarithmic scale. The vertical axis spans ±18 dB; the FFT overlay scales from −70 dB at the bottom to 0 dB at the top.
4. Watch the overlay update in real time as audio passes through the selected path.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| **RX** | Tab | Checked | Binds the analyzer / curve area to the receive-path EQ. Mutually exclusive with TX. | — |
| **TX** | Tab | Unchecked | Binds the analyzer / curve area to the transmit-path EQ. Mutually exclusive with RX. | — |
| Analyzer / curve area | Indicator | — | 110 px tall. Displays the frequency grid, the summed EQ response for the selected path, and the live FFT overlay. View-only. | — |

## Tips

- The analyzer / curve area is view-only. To add, remove, or tune bands, open the floating editor by double-clicking the EQ stage in the CHAIN widget.
- Right-click the CEQ sub-container titlebar to float or pop out the applet if you want the analyzer visible alongside other windows.
- The summed EQ response curve is drawn on top of the FFT overlay, so you can directly compare the EQ shape against the live spectrum.

## Related

- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)
- [Open the floating editor to add / remove / tune bands](open-the-floating-editor-to-add-remove-tune-bands.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)

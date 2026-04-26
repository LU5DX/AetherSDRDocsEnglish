# Open the floating editor to add / remove / tune bands

The floating ClientEqEditor is where you add, remove, and tune EQ bands for the RX and TX paths. The compact applet in the panel shows the result; editing always happens in this separate window.

## Before you start

- The CEQ applet must be visible in the applet panel. It is hidden until the EQ stage is enabled via the CHAIN widget.
- Locate the EQ stage tile in the CHAIN widget for the path you want to edit (RX or TX).

## Steps

1. Find the EQ stage in the CHAIN widget for the path you want to shape (RX chain for receive, TX chain for transmit).
2. Double-click the EQ stage in the CHAIN widget.
3. The ClientEqEditor floating window opens. Add, remove, or tune bands there.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| RX | Tab | Checked | Binds the curve widget to the RX EQ instance. | — |
| TX | Tab | Unchecked | Binds the curve widget to the TX EQ instance. | — |
| Analyzer / curve area | Indicator | — | Displays the summed EQ response and a live FFT overlay for the selected path. View-only; editing requires the floating editor. | — |
| RX enabled state | — | — | Whether the RX EQ stage is active. | `ClientEqRxEnabled` |
| TX enabled state | — | — | Whether the TX EQ stage is active. | `ClientEqTxEnabled` |
| RX band configuration | — | — | Stored band parameters for the RX path. | `ClientEqRxBands` |
| TX band configuration | — | — | Stored band parameters for the TX path. | `ClientEqTxBands` |

## Tips

- The curve area is 110 px tall and shows a ±18 dB vertical range. If all bands are removed, the applet displays "(no bands — add one in the editor)" as a reminder that the floating editor is the only place to add bands.
- Each path has its own applet tile. Double-click the EQ stage in the RX chain to edit RX bands; double-click the one in the TX chain to edit TX bands. There is no internal RX/TX selector inside the applet itself.
- You can also right-click the CEQ sub-container titlebar for options to float, pop-out, or hide the applet tile.

## Related

- [Parametric EQ (Client) overview](overview.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Switch between viewing RX and TX EQ](switch-between-viewing-rx-and-tx-eq.md)
- [Verify the summed curve matches your mental target](verify-the-summed-curve-matches-your-mental-target.md)

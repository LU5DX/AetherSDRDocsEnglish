# Bypass the EQ stage from the chain

Use this page to bypass the client-side parametric EQ on the TX or RX path without removing your band settings. Bypass is useful for A/B comparisons or for temporarily disabling the EQ while keeping your curve intact.

## Before you start

- The Aetherial Audio (TXDSP) parent container must be visible in the applet panel.
- The EQ stage you want to bypass must already be enabled and present in the CHAIN widget; if neither TX nor RX EQ stage appears in the chain, see [Aetherial Parametric EQ (TX / RX) overview](overview.md).

## Steps

1. Locate the CHAIN widget for the path you want to bypass — TX or RX.
2. Single-click the EQ stage tile in the CHAIN widget for that path.

   Clicking the EQ stage toggles bypass on that path. When bypass is engaged, the stage is excluded from the processing chain. Your band settings (`ClientEqTxBands` or `ClientEqRxBands`) are preserved and the stage can be re-enabled by clicking again.

3. Repeat for the other path if needed — TX and RX bypass states are independent.

## What each control does

| Control | Path | Persisted setting | Effect when bypassed |
|---|---|---|---|
| EQ stage tile (TX) in CHAIN widget | TX | `ClientEqTxEnabled` | Removes the TX EQ from the audio chain; TX bands are retained. |
| EQ stage tile (RX) in CHAIN widget | RX | `ClientEqRxEnabled` | Removes the RX EQ from the audio chain; RX bands are retained. |

## Tips

- The "Aetherial TX EQ" and "Aetherial RX EQ" sub-container applets are hidden when the matching EQ stage is disabled. If the applet disappears after bypassing, this is expected.
- Band configuration stored in `ClientEqTxBands` and `ClientEqRxBands` is not affected by toggling bypass. Re-enabling the stage restores your curve exactly.
- To compare your EQ curve against a flat response, click the stage tile rapidly to toggle bypass on and off.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)

# Bypass the EQ stage from the chain

This page explains how to bypass the client-side parametric EQ for either the TX or RX audio path. Bypassing removes the EQ from the signal chain without deleting your band settings.

## Before you start

- AetherSDR must be open. A radio connection is not required to bypass the EQ.
- The EQ stage must already be present in the CHAIN widget for the path you want to bypass (TX or RX).

## Steps

1. Locate the CHAIN widget for the path you want to bypass — either the TX chain or the RX chain.
2. Single-click the EQ stage in the CHAIN widget for that path.

The EQ stage is now bypassed for that path. The `ClientEqTxEnabled` or `ClientEqRxEnabled` setting is updated immediately and persisted across restarts.

To re-engage the EQ, single-click the EQ stage in the CHAIN widget again.

## What each control does

| Control | Path | Persisted key | Behavior |
|---|---|---|---|
| EQ stage (TX chain) | TX | `ClientEqTxEnabled` | Single-click toggles bypass on or off for the TX EQ. Bypassed = EQ removed from signal chain; bands and settings are preserved. |
| EQ stage (RX chain) | RX | `ClientEqRxEnabled` | Single-click toggles bypass on or off for the RX EQ. Bypassed = EQ removed from signal chain; bands and settings are preserved. |

Band data is stored separately in `ClientEqTxBands` and `ClientEqRxBands` and is not affected by bypass.

## Tips

- The bypass state is per-path. Bypassing the TX EQ does not affect the RX EQ, and vice versa.
- The "Aetherial TX EQ" and "Aetherial RX EQ" applet tiles are hidden when their matching EQ stage is not enabled. If a tile disappears after bypassing, this is expected behavior.
- The floating editor ("Aetherial Parametric EQ — TX" or "— RX") can still be opened via double-click on the CHAIN widget stage even when bypassed, so you can continue editing bands without re-engaging the EQ.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)

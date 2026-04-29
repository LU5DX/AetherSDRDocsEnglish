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

| Control | Path | Persisted key |
|---|---|---|
| EQ stage (TX chain) | TX | `ClientEqTxEnabled` |
| EQ stage (RX chain) | RX | `ClientEqRxEnabled` |
| Output Fader | Vertical combined fader + level meter on the right edge of the floating editor. Drag to set post-EQ master gain; scroll wheel adjusts in 0.5 dB steps; double-click resets to 0 dB. The level bar behind the handle shows the smoothed post-EQ peak in real time with the same green-amber-red gradient as the Tube level meter. | Persisted separately per path: `ClientEqTxMasterGain` / `ClientEqRxMasterGain`. Tooltip: 'Output gain (dB). Drag to set, wheel for fine step, double-click to reset to 0 dB.' Gain range is linear 0.0 to ~4.0; the scale labels run from -40 to 0 dB. Located in the floating editor only — not in the docked applet tile. |
| Peak Hold | Located in the floating editor header strip only. When checked, the per-bin peak-hold trace in the analyzer stops decaying — every frequency's highest observed level is held until the button is toggled off. Button background turns amber when checked. | None (not persisted). |
| Filter family | Located in the floating editor header strip. Selects the HP/LP cascade mathematics: Butterworth (maximally flat passband), Chebyshev (steeper rolloff with 1 dB passband ripple), Bessel (linear phase / gentler rolloff), or Elliptic (steepest transition with ripple in both bands). Applies only to HP and LP filter types; peak and shelf bands use their own fixed 2nd-order topology regardless. Default: Butterworth. | Persisted separately per path: `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`. |
| Reset | Located in the floating editor header strip. Resets all bands to the default 10-band template, restores the default band count, and resets the Filter family to Butterworth. Saves immediately. Tooltip: 'Reset all bands to default values'. | Affects `ClientEqTxBands` / `ClientEqRxBands` and `ClientEqTxFilterFamily` / `ClientEqRxFilterFamily`. |

Band data is stored separately in `ClientEqTxBands` and `ClientEqRxBands` and is not affected by bypass.

## Tips

- The bypass state is per-path. Bypassing the TX EQ does not affect the RX EQ, and vice versa.
- The "Aetherial TX EQ" and "Aetherial RX EQ" applet tiles are hidden when their matching EQ stage is not enabled. If a tile disappears after bypassing, this is expected behavior.
- The floating editor ("Aetherial Parametric EQ — TX" or "— RX") can still be opened via double-click on the CHAIN widget stage even when bypassed, so you can continue editing bands without re-engaging the EQ.
- The peak-hold trace in the analyzer decays at approximately 10 dB/sec during normal operation. Enable **Peak Hold** in the floating editor to freeze the trace at its highest observed level per frequency bin — useful for identifying resonances while tuning bands.
- Clicking **Reset** in the floating editor is permanent and takes effect immediately. There is no undo. The reset also sets the Filter family back to Butterworth for that path.

## Related

- [Aetherial Parametric EQ (TX / RX) overview](overview.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Inspect the TX EQ curve and live spectrum](inspect-the-tx-eq-curve-and-live-spectrum.md)
- [Inspect the RX EQ curve and live spectrum](inspect-the-rx-eq-curve-and-live-spectrum.md)
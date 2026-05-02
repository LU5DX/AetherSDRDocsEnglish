# Adjust post-EQ output gain with the Output Fader

The Output Fader sets a master gain applied after all EQ bands on either the TX or RX path. Use it to compensate for overall level changes introduced by your EQ curve without touching individual band gains.

## Before you start

- The floating editor (titled "Aetherial Parametric EQ — TX" or "Aetherial Parametric EQ — RX") must be open. The Output Fader is not present in the docked applet tile.
- The matching EQ stage must be enabled. See [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md) if the stage is currently bypassed.

## Steps

1. Open the floating editor for the path you want to adjust. Double-click the EQ stage in the CHAIN widget on the TX or RX side.
2. Locate the Output Fader on the right edge of the editor window. It is a vertical combined fader and level meter.
3. Drag the fader handle up or down to set the post-EQ master gain. The valid range is -36.0 to +12.0 dB.
4. To make a fine adjustment, hover over the fader and scroll the mouse wheel. Each scroll step moves the gain by 0.5 dB.
5. To return the gain to the default, double-click the fader handle. This resets the value to 0 dB.

## What each control does

| Control | Default | Valid range | Persisted setting |
|---|---|---|---|
| Output Fader (TX path) | 0 dB | -36.0 to +12.0 dB | `ClientEqTxMasterGain` |
| Output Fader (RX path) | 0 dB | -36.0 to +12.0 dB | `ClientEqRxMasterGain` |

The level bar behind the fader handle shows the smoothed post-EQ peak level in real time, using the same green-amber-red gradient as the Tube level meter. This is a display indicator only; it does not respond to dragging.

## Tips

- Use the live level bar on the Output Fader to confirm that your EQ changes have not pushed the output into the red before transmitting or routing audio further.
- The TX and RX Output Faders are independent. Adjusting one path does not affect the other.
- The gain value is persisted immediately. If you close and reopen the editor, the fader returns to the last saved position.

## Troubleshooting

- **Output Fader is not visible** — The fader is only present in the floating editor, not in the docked "Aetherial TX EQ" or "Aetherial RX EQ" applet tile. Open the floating editor by double-clicking the EQ stage in the CHAIN widget.
- **Double-click does not reset the fader** — Ensure you are double-clicking directly on the fader handle, not on the level bar area behind it.

## Related

- [Monitor post-EQ peak level on the Output Fader meter](monitor-post-eq-peak-level-on-the-output-fader-meter.md)
- [Open the frameless editor to add / remove / tune bands on either side](open-the-frameless-editor-to-add-remove-tune-bands-on-either-side.md)
- [Bypass the EQ stage from the chain](bypass-the-eq-stage-from-the-chain.md)
- [Aetherial Parametric EQ (TX / RX) overview](overview.md)

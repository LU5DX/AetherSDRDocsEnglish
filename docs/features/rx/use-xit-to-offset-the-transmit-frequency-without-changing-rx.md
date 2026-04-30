# Use XIT to offset the transmit frequency without changing RX

XIT (Transmit Incremental Tuning) lets you shift your transmit frequency by a fixed number of hertz while your receive frequency stays on the VFO. This is useful when working split, compensating for a TX offset requested by the other station, or matching a net frequency without retuning the panadapter.

## Before you start

- AetherSDR must be connected to the radio. XIT controls are only active when a radio connection is present.
- Open the RX Controls applet. If it is not visible, click the RX tray button on the right sidebar.
- Select the slice you want to adjust using the slice tabs (A..H) at the top of the applet.

## Steps

1. In the RX Controls applet, scroll down to the RIT/XIT section.
2. Click XIT to enable Transmit Incremental Tuning. The button lights when active.
3. Adjust the XIT offset using one of these methods:
   - Click the **<** or **>** buttons flanking the XIT offset spinbox to step in 10 Hz increments.
   - Hover over the XIT offset spinbox and scroll the mouse wheel to step in 10 Hz increments.
4. To return the TX offset to zero without disabling XIT, click XIT 0.
5. To turn XIT off, click XIT again so the button is no longer lit.

## What each control does

| Control    | What it does                                                                                   | Default |
|------------|------------------------------------------------------------------------------------------------|---------|
| XIT        | Toggles Transmit Incremental Tuning on or off.                                                 | Off     |
| XIT offset | Sets the TX frequency offset in hertz. Adjusted with the **<** / **>** buttons or mouse wheel. | +0 Hz   |
| XIT 0      | Resets the XIT offset to +0 Hz without turning XIT off.                                        | —       |

## Tips

- RIT and XIT are independent. You can run both simultaneously: RIT shifts your receive frequency, XIT shifts your transmit frequency, and the VFO readout stays unchanged.
- If you need the TX offset to persist across a session, set the XIT offset before transmitting; it remains set until you click XIT 0 or disable XIT.
- To zero the offset quickly before a transmission, click XIT 0 rather than toggling XIT off and back on.

## Troubleshooting

- **XIT controls are greyed out** — The radio is not connected. Use `Settings > Connect to Radio...` to establish a connection, then try again.
- **TX frequency is not shifting as expected** — Confirm the correct slice is selected using the slice tabs (A..H). XIT acts only on the currently bound slice.

## Slice tab and badge colors (v0.9.3)

Starting in v0.9.3, the slice tab buttons (A..H) and the slice badge in the top-left of the applet are colored by the SliceColorManager. Each slice has its own color that persists across sessions. The same color is reflected in the VFO widgets and meter strips for that slice. Colors are not configurable from within the RX Controls applet itself; they are managed centrally by SliceColorManager and apply consistently across all widgets that reference a given slice.

## NT mode behavior

The NT mode is treated as a digital mode by the RX Controls applet. Specifically:

- NT follows the same filter width presets and step sizes as DIGU and DIGL.
- The filter width label calculates bandwidth the same way as DIGU (using the high-edge value).
- The SQL button and squelch level slider are disabled when NT is active, because audio is routed via DAX and squelch is not meaningful. If squelch was on when you switched to NT, it is turned off automatically and the previous state is saved for restoration when you leave NT mode.

## Related

- [Use RIT to offset the receive frequency for a drifting station](use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)
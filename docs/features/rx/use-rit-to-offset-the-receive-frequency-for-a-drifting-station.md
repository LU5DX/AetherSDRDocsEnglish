# Use RIT to offset the receive frequency for a drifting station

RIT (Receive Incremental Tuning) shifts the receive frequency by a small amount without moving the transmit frequency or the VFO readout. Use it when a station drifts slightly off your dial frequency and you want to track them without retuning the whole slice.

## Before you start

- AetherSDR must be connected to the radio. RIT controls are inactive without a radio connection.
- Open the RX Controls applet. Click the RX tray button on the right sidebar if the applet is not visible.
- Select the slice you want to adjust using the slice tabs (A..H) at the top of the applet, if more than one slice is active.

## Steps

1. In the RX Controls applet, locate the RIT row near the bottom of the applet.
2. Click RIT to enable Receive Incremental Tuning. The button lights when active.
3. Use the `<` and `>` buttons beside the RIT offset spinbox, or scroll the mousewheel over the spinbox, to adjust the offset. Each step moves the receive frequency by 10 Hz. The spinbox displays the current offset (default: `+0 Hz`).
4. Continue adjusting until the drifting station is centred in the passband.
5. To return to zero offset without disabling RIT, click RIT 0. The offset resets to `+0 Hz`.
6. To turn off RIT entirely, click RIT again. The receive frequency returns to the VFO frequency.

## What each control does

| Control    | Kind          | Default |
|------------|---------------|---------|
| RIT        | Toggle button | Off     |
| RIT offset | Spinbox       | `+0 Hz` |
| RIT 0      | Push button   | —       |
## Tips

- RIT affects only the receive frequency. Your transmit frequency stays on the VFO. If you also need to offset your transmit frequency, use XIT instead of or alongside RIT.
- The 10 Hz minimum step suits SSB and CW work. For a station drifting slowly, a few presses of `>` or a short mousewheel scroll is usually enough.
- Clicking RIT 0 before turning RIT off is good practice. It means RIT is already zeroed if you re-enable it later.

## Slice tab and badge colours (v0.9.3)

From v0.9.3, the slice tab buttons (A..H) and the Slice badge in the top-left corner of the applet both take their colour from the SliceColorManager singleton rather than a fixed colour table. This means:

- Per-slice colours are customisable and persist across sessions.
- The same colour is reflected in the slice tab buttons, the Slice badge, VFO widgets, and meter strips wherever the slice is displayed.
- No action is required on your part; the colours update automatically when a slice is connected or its colour is changed.

## Slice tab behaviour on reconnect (v0.9.5.1)

From v0.9.5.1, the slice tab row is rebuilt correctly whenever the number of available slices changes across a disconnect and reconnect cycle. Specifically:

- When the radio reports a different slice count on reconnect, the existing tab buttons are torn down completely before new ones are created. The static Slice badge is restored and visible while no tabs are present.
- Click signal handlers are connected only once per applet lifetime, regardless of how many times the radio connects or reconnects. This prevents duplicate events from firing when a slice tab is clicked after a reconnect.

No action is required on your part. If you reconnect to a radio with a different slice configuration, the tab row updates automatically.

## NT mode behaviour

From v0.9.3, the NT mode is treated as a digital mode throughout the RX Controls applet:

- **Filter width presets** apply the digital (DIG) preset list to NT slices, the same as DIGU and DIGL.
- **Filter width display** calculates the NT filter width using the upper edge (hi), consistent with DIGU and FDV handling.
- **Squelch** is disabled for NT slices. Because audio is routed via DAX in digital modes, the squelch control is not meaningful. The SQL button and squelch level slider are greyed out when NT is the active mode. If squelch was on when you switched to NT, it is turned off automatically and restored when you leave NT.

## Filter width presets (v0.9.5.1)

From v0.9.5.1, filter preset entries can store either a plain width value or an explicit lo:hi passband pair. This matches the storage format used by VfoWidget (#2259). The behaviour from your perspective is:

- Presets you saved in earlier versions (plain width values) continue to load and work without any changes.
- When a preset is saved from a custom passband position, both the low and high filter edges are stored. When that preset is recalled, the passband is restored to exactly the same position, not just the same width.
- The `FilterPresets` setting in AppSettings uses the format `lo:hi` for passband-aware entries and a plain integer for width-only entries. Multiple entries are comma-separated, for example: `300:3000,100:2900,2700`.
- At most six presets are shown in the RX Controls applet regardless of how many are stored.

Right-click a filter preset button to save the current filter width (and passband position, if applicable) as that preset. Click a preset button to apply it.

## Related

- [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
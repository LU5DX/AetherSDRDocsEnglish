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

## Slice badge text format (v26.5.2.1)

From v26.5.2.1, the slice badge label uses rich text format so the slice letter may be rendered as HTML. This allows special colour or style characters if needed. The badge still displays the letter of the currently bound slice (A..H).

## Slice tab behaviour on reconnect (v0.9.5.1)

From v0.9.5.1, the slice tab row is rebuilt correctly whenever the number of available slices changes across a disconnect and reconnect cycle. Specifically:

- When the radio reports a different slice count on reconnect, the existing tab buttons are torn down completely before new ones are created. The static Slice badge is restored and visible while no tabs are present.
- Click signal handlers are connected only once per applet lifetime, regardless of how many times the radio connects or reconnects. This prevents duplicate events from firing when a slice tab is clicked after a reconnect.

No action is required on your part. If you reconnect to a radio with a different slice configuration, the tab row updates automatically.

## RADE mode behaviour

When you select RADE from the mode combo, the slice is placed into RADE (Rapid Automatic Detection and Excitation) mode. Note that RADE is a client-side only mode — the radio echoes back the real mode (DIGL/DIGU) immediately after selection. When you switch from RADE to another mode, no RADE deactivation signal is emitted because the slice's mode is never `"RADE"` on the radio side. This prevents spurious deactivations when changing modes.

## NT mode behaviour

From v0.9.3, the NT mode is treated as a digital mode throughout the RX Controls applet:

- **Filter width presets** apply the digital (DIG) preset list to NT slices, the same as DIGU and DIGL.
- **Filter width display** calculates the NT filter width using the upper edge (hi), consistent with DIGU and FDV handling.
- **Squelch** is disabled for NT slices. Because audio is routed via DAX in digital modes, the squelch control is not meaningful. The SQL button and squelch level slider are greyed out when NT is the active mode. If squelch was on when you switched to NT, it is turned off automatically and restored when you leave NT.

## RTTY mode squelch behaviour (v26.5.1)

From v26.5.1, RTTY mode is added to the list of modes that automatically disable squelch. When you switch to RTTY mode:

- The **SQL** button and **Squelch level** slider are disabled.
- If squelch was on, it is turned off automatically and the saved state is restored when you leave RTTY.

This prevents squelch from notching out FSK characters and breaking decoding (#2504).

## Manual squelch level persistence (v26.5.2.1)

From v26.5.2.1, the manual squelch threshold you set with the squelch level slider is saved and restored across sessions. When auto-squelch mode is active, the radio may change the squelch level internally — the client now remembers your last manual preference so it is preserved when you return to manual squelch control. The setting is stored in `LastManualSquelchLevel` with a default of 20.

## RX antenna menu (v26.5.2.1)

From v26.5.2.1, the RX antenna menu is populated from the slice's dedicated `rxAntennaList()` when available, falling back to the general `ant_list` from the panadapter status. This ensures you see only antennas valid for the current slice. Menu items display the antenna name with tooltip and status tip showing the raw antenna identifier. Selecting an item calls `setRxAntenna()` with the antenna data string rather than the menu label text.

## TX antenna menu (v26.5.2.1)

From v26.5.2.1, the TX antenna menu uses a refined filtering algorithm. A fallback function `likelyTxAntennaFallbackToken()` accepts antenna tokens that start with `ANT`, `TX`, or are exactly `XVTR`. Ports starting with `RX` are excluded. Menu items display the antenna name with tooltip and status tip. Selecting an item calls `setTxAntenna()` with the antenna data string.

## Filter width presets (v0.9.5.1)

From v0.9.5.1, filter preset entries can store either a plain width value or an explicit lo:hi passband pair. This matches the storage format used by VfoWidget (#2259). The behaviour from your perspective is:

- Presets you saved in earlier versions (plain width values) continue to load and work without any changes.
- When a preset is saved from a custom passband position, both the low and high filter edges are stored. When that preset is recalled, the passband is restored to exactly the same position, not just the same width.
- The `FilterPresets` setting in AppSettings uses the format `lo:hi` for passband-aware entries and a plain integer for width-only entries. Multiple entries are comma-separated, for example: `300:3000,100:2900,2700`.
- At most six presets are shown in the RX Controls applet regardless of how many are stored.

Right-click a filter preset button to save the current filter width (and passband position, if applicable) as that preset. Click a preset button to apply it.

## Filter width stepping (v0.9.8)

From v0.9.8, the `stepFilterWidth()` method walks the per-mode preset list to find the next narrower or wider filter preset. This means the widen/narrow shortcuts (if available) produce mode-correct edge geometry for all modes (LSB, CWL, DIGL, RTTY, AM, CW, USB) rather than applying a simple fixed offset. The filter width readout, shared with the VFO panel via `RxApplet::formatFilterWidth()`, uses mode-aware logic so SSB and digital modes display the correct labelled width.

If you have widen or narrow keyboard shortcuts bound to `stepFilterWidth()`:

- Pressing the widen shortcut selects the next wider preset in the current mode's filter preset list that is wider than the current width.
- Pressing the narrow shortcut selects the next narrower preset.
- If no wider/narrower preset exists, the key press is ignored.

No action is required on your part; the stepping behaviour updates automatically in v0.9.8.

## Mute button behaviour (v26.5.3)

From v26.5.3, the mute button uses a click-discrimination system:

- **Single-click** mutes or unmutes only the current slice. The action is deferred by the platform double-click interval (approximately 400 ms) so a double-click can override it.
- **Double-click** mutes or unmutes all slices owned by this client, emitted via the `muteAllToggled` signal.
- The visual icon (🔊/🔇) updates only when the radio acknowledges the mute state change via `SliceModel::audioMuteChanged`. This follows the Radio-Authoritative Settings Policy (#2489) — the radio is the source of truth for audio mute.
- Mute state is NOT saved or restored on reconnect.

## Frequency entry parser (v26.5.3)

From v26.5.3, frequency entry uses a dedicated `FrequencyEntryParser` for text normalisation and validation:

- When you type a frequency in MHz and press Enter, the parser normalises the text by stripping any dots after the first decimal point. For example, `14.200.000` becomes `14.200000`.
- The parser detects whether you entered an explicit MHz value (contains a decimal point) or a raw number. If you enter a value above 54.0 MHz as an explicit MHz entry (e.g., `144.0`), the XVTR frequency limit of 50000.0 MHz applies, allowing VHF/UHF operation without requiring an XVTR antenna.
- If you enter a value above 54.0 MHz without a decimal point, the system divides the value by 1000 (treating kHz as Hz) or by 1e6 (treating Hz as MHz) as appropriate.
- On any valid entry (0.001 to maxMhz), the signal `directEntryCommitted(freqMhz, QStringLiteral("rx-direct-entry"))` is emitted to recenter the panadapter.

## AF gain and pan slider labels (v26.5.3)

From v26.5.3, the AF gain and pan sliders display percentage and positional labels:

- **AF gain slider**: Displays the current value as a percentage (e.g., `70%`) using `percentText()`.
- **Pan slider**: Displays `C` at centre (50), `Lx` for left offset (e.g., `L20` for 30% from centre), and `Rx` for right offset (e.g., `R30` for 80% from centre) using `panText()`. The label updates as you drag the slider.

## RADE mode switching fix (v26.5.3)

From v26.5.3, when switching out of RADE mode via the mode combo, the applet emits `radeActivated(false)` only if the slice was actually in RADE mode. This prevents stale deactivate signals when changing modes on a non-RADE slice (#2376).

## Related

- [Use XIT to offset the transmit frequency without changing RX](use-xit-to-offset-the-transmit-frequency-without-changing-rx.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
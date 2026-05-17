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

## Slice badge text format (v26.5.2.1)

Starting in v26.5.2.1, the slice badge label supports rich text (HTML) rendering. This allows the slice letter to be formatted with HTML tags when necessary, such as for accessibility or special display requirements. The badge continues to display the single letter of the currently bound slice (A through H) with its slice-identity color. No action is required from you.

## Slice tab behavior on reconnect (v0.9.5.1)

In v0.9.5.1, the slice tab row is rebuilt correctly when the number of available slices changes, such as after a disconnect and reconnect or after the radio reports a different slice count.

Previously, the tab buttons were created only once and never replaced. Now, if the radio reports a different maximum slice count from the one already displayed, the existing buttons are torn down first — removing them from the layout and restoring the static slice badge — before the new set is built. This prevents stale tab buttons from appearing after reconnection.

The click handler that emits `sliceActivationRequested` is connected only once per applet instance, regardless of how many times the tab row is rebuilt. This prevents duplicate signal handlers from accumulating across reconnects.

No action is required from you. The tab row updates automatically when the radio connection changes.

## Antenna menu behavior (v26.5.2.1)

In v26.5.2.1, the RX and TX antenna menus were improved for better accuracy and reliability:

- **RX antenna menu** now uses the slice's dedicated `rxAntennaList()` when available, rather than the global panadapter antenna list. This ensures the menu shows only antennas valid for the current slice. If the slice does not provide a dedicated RX antenna list, the global antenna list is used as a fallback.
- **TX antenna menu** explicitly filters antennas to only those suitable for transmission. The applet uses a dedicated method (`txAntennaOptions()`) that identifies TX-capable antennas by checking if the antenna token starts with "ANT", "TX", or equals "XVTR". Antennas starting with "RX" are excluded from TX options.
- **Menu items** now display tooltips and status tips showing the raw antenna identifier string. The menu action's data field, rather than its display text, is used when setting the antenna on the slice. This prevents display formatting from interfering with the actual antenna selection.

No action is required from you. The antenna menus now show only appropriate antennas for each function.

## Manual squelch level persistence (v26.5.2.1)

Starting in v26.5.2.1, the manual squelch threshold level is saved and restored across sessions. When you adjust the squelch level slider manually, the value is stored client-side in the AetherSDR settings file under `LastManualSquelchLevel`.

This is necessary because the radio's auto-squelch mode can overwrite the `squelchLevel` property on the slice, so the radio cannot be relied upon to preserve the operator's manual preference. By persisting the manual level in AetherSDR, the applet can restore your preferred squelch threshold when you exit auto mode or restart the application.

The stored value is clamped to the valid range (0-100) on load. Default value is 20.

No action is required from you. Your manual squelch preference is now remembered between sessions.

## Filter preset storage format (v0.9.5.1)

In v0.9.5.1, filter presets saved by the `FilterPresets` setting can store either a plain bandwidth width value or an explicit low-edge/high-edge pair. This matches the format used by the VFO widget.

- **Width-only format** — a single integer in hertz, for example `2700`. The applet centers the passband symmetrically around the carrier using the mode's default edges.
- **Lo:Hi format** — two integers separated by a colon, for example `300:3000`. The applet sets the filter low edge to 300 Hz and the high edge to 3000 Hz exactly. The displayed width label shows the computed difference (2700 Hz in this example).

Both formats can appear in the same comma-separated `FilterPresets` value for a given mode. Entries that are malformed, have a high edge equal to or below the low edge, or are zero or negative are silently skipped.

This change affects how custom filter presets are saved and loaded but does not change how you interact with the filter preset buttons. Right-click a preset button to save the current passband to that slot; click it to apply the preset. The lo:hi format is written automatically when you save a preset whose low edge differs from the mode default.

## Filter width step behavior (v0.9.8)

In v0.9.8, the `stepFilterWidth()` method walks the per-mode filter preset list to widen or narrow the passband. This ensures that keyboard shortcuts or other controls that step through filter widths produce mode-correct edge geometry.

When you use a widen/narrow action (such as from the Widen/Narrow buttons in the VFO panel), the applet searches the per-mode filter preset list for the preset closest to the current filter width. It then applies the next wider or narrower preset from that list. If the current width exactly matches a preset, the next preset in the chosen direction is applied directly.

This behavior applies to all modes: LSB, CWL, DIGL, RTTY, AM, CW, and USB. FM-family modes (FM, NFM, DFM) do not have filter presets and ignore the step action.

No configuration is needed. The step behavior uses the same `FilterPresets` setting that you can customize with right-click save.

## Filter width label format (v0.9.8)

In v0.9.8, the filter width readout (shared with the VFO panel via `RxApplet::formatFilterWidth`) uses mode-aware logic so SSB and digital modes display the correct labelled width. This ensures consistent readouts between the RX Controls applet and the VFO panel, as referenced in issue #2197. No action is required from you.

## NT mode behavior

The NT mode is treated as a digital mode by the RX Controls applet. Specifically:

- NT follows the same filter width presets and step sizes as DIGU and DIGL.
- The filter width label calculates bandwidth the same way as DIGU (using the high-edge value).
- The SQL button and squelch level slider are disabled when NT is active, because audio is routed via DAX and squelch is not meaningful. If squelch was on when you switched to NT, it is turned off automatically and the previous state is saved for restoration when you leave NT mode.

## Squelch behavior in RTTY and digital modes (v26.5.1)

Starting in v26.5.1, the squelch controls (SQL button and squelch level slider) are also disabled in RTTY mode, in addition to the existing digital modes (DIGU, DIGL) and NT mode. This change ensures that squelch does not notch out FSK characters, which would otherwise break decoding.

When you switch to RTTY mode:
- The SQL button and squelch level slider are automatically disabled.
- If squelch was on when you switched to RTTY, it is turned off automatically and the previous state is saved for restoration when you leave RTTY or digital mode.
- CW modes (CW, CWL) continue to have squelch disabled as before, with squelch state managed by the radio itself.

## RADE mode safety (v26.5.2.1)

In v26.5.2.1, the RADE (RADE) mode deactivation logic was updated to reflect that "RADE" is a client-side only mode. The radio itself does not understand RADE as a distinct mode — when RADE is active, the radio echoes back the underlying real mode (DIGL or DIGU) immediately.

Previously, the applet checked `m_slice->mode() == "RADE"` before emitting a deactivation signal. Because the radio immediately reports the real mode after setting RADE, this condition could never be true.
- Switching between non-RADE modes on a slice that was never in RADE.
- RADE was activated externally (via the VFO widget combo, profile load on startup, or `MainWindow::activateRADE`).
- The slice is rebound to a different slice via `setSlice()`.

No action is required from you. The RADE mode deactivation behavior now correctly aligns with the client-side-only nature of the mode.

## Audio mute state on reconnect (v0.9.10)

In v0.9.10, the mute button state (🔊 / 🔇) is NOT saved or restored when the radio connection is lost and re-established. The radio is the source of truth for audio mute state, per the Radio-Authoritative Settings Policy (#2489). After you disconnect and reconnect, the mute button reflects the actual mute state reported by the radio, which may be different from what it was before the disconnect.

## Related

- [Use RIT to offset the receive frequency for a drifting station](use-rit-to-offset-the-receive-frequency-for-a-drifting-station.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)
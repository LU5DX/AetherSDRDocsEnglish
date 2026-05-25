# Change mode (USB, LSB, CW, AM, FM, etc.)

This page explains how to select a receive mode for a slice. Changing the mode reshapes the filter presets and tuning step sizes to suit the new modulation.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- If you have more than one slice, select the correct slice first using the A..H tab row at the top of the RX Controls applet.

## Steps

1. If the RX Controls applet is not visible, click the **RX** tray button on the right sidebar to show it.
2. If your radio has more than one slice active, click the appropriate slice tab (**A** through **H**) to bind the applet to the slice you want to change.
3. Click the **Mode combo** drop-down. The current mode is shown (default: **USB**).
4. Select the desired mode from the list:
   - **USB**, **LSB**, **CW**, **AM**, **SAM**, **FM**, **NFM**, **DFM**, **DIGU**, **DIGL**, **RTTY**
   - (RADE appears only in builds with RADE support enabled.)
5. The slice switches to the selected mode. The filter width presets and tuning step sizes update automatically to suit the new mode.

## What each control does

| Control                    | Default          | Valid values                                                                                                                                                                                          |
|----------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mode combo**             | USB              | USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY (+ RADE if available)                                                                                                                           |
| **Filter width presets**   | Mode-dependent   | USB/LSB: 1800/2100/2400/2700/2900/3300 Hz; CW: 50/100/250/400 Hz; AM/SAM: 5600–14000 Hz; DIGU/DIGL: 100–2000 Hz; RTTY: 250–1000 Hz                                                                    |
| **STEP**                   | 100 Hz (index 2) | Per-mode list (e.g. SSB: 1, 10, 50, 100, 500, 1000, 2000, 3000 Hz; CW: 1, 5, 10, 50, 100, 200, 400 Hz; FM family: 50–12500 Hz)                                                                        |
| **Filter passband widget** | —                | Drag lo/hi edges                                                                                                                                                                                      |
| **SQL**                    | Off              | Toggle button to enable squelch. Auto-disabled in RTTY, DIGU, DIGL, NT, CW, and CWL modes. In RTTY and digital modes, squelch is also turned off automatically to prevent gating FSK signals (#2504). |
| **Squelch level**          | 20               | Slider (0-100) to set squelch threshold. Disabled in RTTY, DIGU, DIGL, NT, CW, and CWL modes.                                                                                                         |
| **RX antenna**             | ANT1             | Combo box listing available receive antennas. Populated from the radio's `ant_list` or the slice's `rxAntennaList()` when available.                                                                  |
| **TX antenna**             | ANT1             | Combo box listing TX-capable antennas. RX-only antenna ports (prefix 'RX') are filtered out. Uses `txAntennaOptions()` for the list.                                                                  |
| **🔊 / 🔇 (mute)**        | 🔊 (unmuted)     | Push button. Single-click mutes/unmutes this slice. Double-click mutes/unmutes all owned slices. Icon flips when the radio acknowledges the change.                                                    |
| **AF gain**                | 70               | Slider (0-100) for slice audio output gain.                                                                                                                                                           |
| **L / R pan**              | 50 (centre)      | Slider (0-100) for stereo pan position. Double-click resets to centre.                                                                                                                                |
## Tips

- FM, NFM, and DFM modes do not show filter width preset buttons. The filter is fixed for those modes.
- After switching to FM or NFM, the CTCSS tone and repeater offset controls (**Tone mode**, **Offset**, **−**, **Simplex**, **+**, **REV**) become visible. See [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md) for details.
- After switching to CW, the **QSK** indicator in the header becomes relevant. Its state is controlled from the CW applet, not from RX Controls.
- AGC mode controls are hidden when an FM family mode is active.
- Filter presets are now stored in a `lo:hi` format (e.g. `300:3000`) as well as the older plain-width format. Both formats are read correctly. If you have saved custom presets from an earlier version, they continue to work without any action on your part.
- The `stepFilterWidth()` method walks the per-mode preset list so widen/narrow shortcuts produce mode-correct edge geometry. This ensures that when you widen or narrow the filter using keyboard shortcuts, the filter stays within the appropriate preset boundaries for the current mode.
- When switching to RTTY or digital modes (DIGU, DIGL), the squelch is automatically disabled and turned off. This prevents the squelch from notching out FSK characters and breaking decoding (#2504).
- The manual squelch level is persisted across sessions. The last user-chosen value is stored in the `LastManualSquelchLevel` setting and restored on launch. This preserves the operator's manual preference across mode cycles, as auto mode may otherwise clobber the slice's `squelchLevel` with algorithm-suggested values (#2606).
- The slice badge now supports rich text formatting (HTML) for the slice letter (#2606).

## Mute button behaviour (v26.5.3)

The mute button (🔊 / 🔇) operates as a push button, not a toggle button. The behaviour follows the **Radio-Authoritative Settings Policy (#2489)** — mute state is NOT saved or restored on reconnect; the radio is the source of truth for audio mute.

**Single-click:** Mutes or unmutes the current slice. The action is deferred by the platform double-click interval (typically ~400 ms) so a double-click can override it. The icon updates only when the radio acknowledges the change via `SliceModel::audioMuteChanged`.

**Double-click:** Mutes or unmutes all owned slices. The double-click handler is implemented in the `eventFilter` method and cancels the single-click timer, preventing the single-click action from firing.

When a double-click sequence occurs, the second press does not emit a `clicked()` signal — the eventFilter returns true on `MouseButtonDblClick`, so `QAbstractButton::mouseDoubleClickEvent` is never called. This ensures clean single-click vs double-click discrimination.

## Slice tab behaviour (v0.9.5.1)

When the radio reports a change in the number of available slices, the A..H tab row is now rebuilt correctly instead of being skipped. The previous behaviour kept the old buttons if any were already present; v0.9.5.1 tears down and recreates the buttons whenever the slice count changes (`clearSliceButtons()`, #2254). On disconnect the tab row is hidden and the static **Slice badge** is restored automatically.

Signal connections for slice button clicks are also guarded so that reconnecting to the radio does not attach duplicate handlers.

## Filter width formatting (v0.9.8)

The filter width readout in the RX Controls applet now uses mode-specific logic to display the correct labelled width. This readout is shared with the VFO panel for consistent formatting (#2197). The `formatFilterWidth()` static method applies mode-aware rules so that SSB and digital modes display the expected bandwidth label (e.g., "2.7K" for 2700 Hz USB, "500" for 500 Hz CW).

## Antenna selection behaviour

The RX and TX antenna combo boxes now use `rxAntennaList()` and `txAntennaOptions()` respectively to populate their menus. The radio's `ant_list` is used as a fallback when slice-specific antenna lists are not available.

The antenna menu items now include tooltips and status tips showing the raw antenna identifier, and the menu label is generated by `antennaMenuLabel()` for consistent display. The selected antenna is sent via `setData()` rather than `text()` to ensure the correct identifier is used.

The `likelyTxAntennaFallbackToken()` helper determines if an antenna token is suitable for TX by checking if it starts with "ANT", "TX", or equals "XVTR". RX-only ports (prefix "RX") are excluded.

## Frequency entry behaviour (v26.5.3)

The frequency editor now uses `FrequencyEntryParser::normalizedMhzText()` to clean the entered text before conversion to a double. This ensures consistent handling of thousands separators and decimal points across locales.

**XVTR-aware entry:** The maximum frequency range is now determined by two conditions:
- If the slice is on an XVTR antenna (antenna name starts with "XVT" or frequency > 54.0 MHz)
- OR if the user enters an explicit MHz value above 54.0 MHz

When either condition is true, the frequency editor accepts up to 50000.0 MHz. This allows direct entry of VHF/UHF frequencies (e.g., 144.6 MHz) even when not currently on an XVTR antenna.

The 3-digit-band convenience (e.g., "1446" → 144.6 MHz for 2m) applies only to XVTR slices and is skipped for entries that already appear to be explicit MHz values above 54.0 MHz.

When a valid frequency is committed, the applet emits `directEntryCommitted(freqMhz, "rx-direct-entry")` instead of calling `slice->tuneAndRecenter()` directly.

## Troubleshooting

- **Mode combo is missing or grayed out** — The applet is not connected to the radio. Check the connection via `Settings > Connect to Radio...`.
- **Filter preset buttons disappeared after changing mode** — This is expected when switching to FM, NFM, or DFM. Those modes do not use filter presets.
- **Slice tabs show the wrong number of buttons after reconnecting** — This was a known issue fixed in v0.9.5.1 (#2254). Update to the current release if you see stale tab buttons.
- **Squelch level resets unexpectedly** — The manual squelch level is now persisted client-side across sessions (#2606). If squelch appears to reset, check whether auto mode is overriding the slice's squelch level, as the radio may not preserve the manual value.
- **Mute button does not respond to single-click** — This may occur if your platform double-click interval is very short. The single-click action is deferred by this interval; try clicking more deliberately. Verify that the radio acknowledges the mute state change.
- **Frequency entry rejected for VHF/UHF frequencies** — Ensure you enter the frequency in MHz with a decimal point (e.g., "144.600"). Entering "144600" will be interpreted as 144.600 MHz (division by 1000) because it exceeds 54.0 MHz.

## Related

- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Work an FM repeater with CTCSS tone and +/- offset](work-an-fm-repeater-with-ctcss-tone-and-offset.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
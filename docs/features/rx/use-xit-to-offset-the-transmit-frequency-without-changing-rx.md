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

---

## RX Controls Applet — Full Reference

The RX Controls applet provides per-slice receive controls for the currently bound slice. It is displayed as a panel in the right sidebar when the RX tray button is clicked.

### Slice tabs (A..H)

The slice tab row at the top of the applet lets you select which slice the applet is bound to. Each slice has its own color that persists across sessions. The same color is reflected in the VFO widgets and meter strips for that slice.

- Click a tab button (A..H) to bind the applet to that slice.
- The tab row is hidden if the radio supports only one slice.
- On reconnect, the tab row is rebuilt correctly when the number of available slices changes. The click handler that emits `sliceActivationRequested` is connected only once per applet instance, regardless of how many times the tab row is rebuilt.
- Slice button click connections are guarded against duplicate signal handlers across reconnects. `clearSliceButtons()` tears down all generated tab buttons and restores the static slice badge on disconnect.

### Slice badge

The slice badge in the top-left of the applet displays the letter of the currently bound slice (A through H) with its slice-identity color. The badge supports rich text (HTML) rendering for accessibility or special display requirements.

### 🔓 / 🔒 (Tune lock)

Toggles tune-lock on the slice. When locked, the slice ignores frequency changes.

### ANT1 (RX antenna)

Opens a menu listing available receive antennas. The menu uses the slice's dedicated `rxAntennaList()` when available, falling back to the global panadapter antenna list. Blue-coloured label.

### ANT1 (TX antenna)

Opens a menu listing TX-capable antennas. RX-only antenna ports (prefix "RX") are filtered out. Red-coloured label.

### 2.7K (filter width)

Displays the current slice filter bandwidth. The readout is shared with the VFO panel and uses mode-aware logic so SSB and digital modes display the correct labelled width. The `stepFilterWidth()` method walks the per-mode filter preset list to widen or narrow the passband, producing mode-correct edge geometry.

### QSK

Lights amber when CW break-in (QSK) is active. Read-only; controlled via the CW applet Breakin button.

### TX (badge)

Click to set this slice as the TX slice.

### Mode combo

Selects the slice mode from the available options: USB, LSB, CW, AM, SAM, FM, NFM, DFM, DIGU, DIGL, RTTY. If the build has RADE support, RADE is also available.

When switching modes:
- Switching to RTTY or digital modes (DIGU, DIGL) auto-disables squelch, which would otherwise notch out FSK characters and break decoding.
- When switching out of RADE mode, the applet emits a deactivate signal only if the slice was actually in RADE mode, preventing stale deactivate signals when changing modes on a non-RADE slice.
- Selecting any real radio mode automatically tears down the WFM software demodulator overlay if it was running on this slice (see WFM button section).

### WFM button

A toggle button labelled "WFM" appears immediately after the mode combo box. It enables or disables the software FM demodulator, which uses DAX IQ audio routed through the Hi-Fi cable. This is not a radio mode but a client-side overlay.

- Click to toggle the WFM demodulator on or off.
- When active, the button is highlighted with a green background.
- Tooltip: "Software FM demodulator via DAX IQ → Hi-Fi Cable"
- Selecting any mode from the mode combo box automatically deactivates WFM on that slice.
- The WFM state is synchronized across reconnects: if the radio connection drops and re-establishes, the button reflects the previously active WFM state.

### Frequency label

Displays the current VFO frequency with dotted grouping. Click to switch into edit mode.

### Frequency edit

Enter a frequency in MHz and press Enter to tune and recenter. Supports kHz/Hz auto-scaling. The input is normalized so that only the first dot is kept as the decimal separator; any additional dots are removed. Escape cancels the entry, restores the previous frequency, and dismisses the editor. XVTR-aware: accepts up to 450 MHz when the slice is on an XVTR antenna. The text field is now a `FreqLineEdit` widget with a "MHz" hint label instead of placeholder text.

### STEP

Cycles through per-mode step sizes using < / > buttons or mousewheel. Step list depends on slice mode. The `stepSizeChangedByUser` signal is emitted alongside `stepSizeChanged` to distinguish user-initiated step changes from programmatic ones.

### Filter width presets

Click to apply a preset filter width. Right-click to save the current width as a preset. Buttons are hidden for FM/NFM/DFM modes. Presets are per-mode.

The `stepFilterWidth()` method walks the per-mode filter preset list to widen or narrow the passband, producing mode-correct edge geometry.

Saved filter presets can store either a plain bandwidth width value or an explicit low-edge/high-edge pair (e.g., `300:3000`).

### Filter passband widget

Drag the lo/hi edges to adjust the filter passband.

### Tone mode (FM)

Selects CTCSS tone mode on FM/NFM/DFM. Visible only in FM family modes.

### CTCSS tone value

Selects the CTCSS tone frequency sent with transmit. Enabled only when Tone mode is CTCSS TX.

### Offset (FM)

Sets the FM repeater offset frequency in MHz.

### −, Simplex, + (offset direction)

Sets the repeater offset direction to down, simplex, or up.

### REV

Inverts the TX offset sign to work a reversed repeater pair.

### 🔊 / 🔇 (mute)

Single-click mutes/unmutes this slice. Double-click mutes/unmutes all owned slices. The action is deferred by the platform double-click interval so a double-click can override a single-click.

Mute state is NOT saved or restored on reconnect — the radio is the source of truth for audio mute state. The mute icon updates only when the radio acknowledges the mute state change.

### AF gain

Adjusts the slice audio output gain (0-100).

### L / R pan

Pans slice audio between left (0) and right (100) channels. Double-click resets to 50 (centre). The slider fill anchors from the centre outward so the operator can see the neutral position at a glance. A small centre-mark dot is painted on the groove.

### SQL

Enables squelch at the current slider level. Disabled (and auto-turned off) in RTTY and digital modes (DIGU, DIGL) where squelch would notch out FSK characters.

### Squelch level

Adjusts the squelch threshold (0-100). Takes effect only when SQL is on. Disabled in RTTY and digital modes.

The manual squelch threshold level is saved and restored across sessions under `LastManualSquelchLevel`. This preserves your preferred squelch threshold when you exit auto mode or restart the application.

### AGC mode

Sets the slice AGC mode (Off, Slow, Med, Fast). Hidden in FM family modes.

### AGC threshold

Sets the AGC threshold (or AGC off-level when AGC mode is Off). Tooltip reflects which value is being adjusted. Additionally, the tooltip now advertises the right-click calibration feature: "Right-click to calibrate against the noise floor."

Right-click on the AGC threshold slider to open a context menu with the option "Calibrate AGC-T against noise floor…" Selecting this emits a `calibrateAgcTRequested` signal for the current slice, which opens the AGC-T noise calibration panel. This feature helps you set the AGC threshold based on the actual noise floor rather than an arbitrary value.

### AGC-T calibration context menu

The AGC threshold slider has a right-click context menu that provides access to the noise calibration panel:

1. Right-click the AGC threshold slider.
2. Select "Calibrate AGC-T against noise floor…" from the context menu.
3. The calibration panel opens, allowing you to set the AGC threshold based on the measured noise floor.

This feature helps you set the AGC threshold more precisely for your operating environment. The context menu is only available when a slice is bound to the applet.

### RIT

Toggles Receive Incremental Tuning on/off.

### RIT 0

Zeroes the RIT offset.

### RIT offset

Adjusts the RIT offset by 10 Hz steps using < / > buttons or mousewheel.

### XIT

Toggles Transmit Incremental Tuning on/off.

### XIT 0

Zeroes the XIT offset.

### XIT offset

Adjusts the XIT offset by 10 Hz steps using < / > buttons or mousewheel.

---

## NT mode behavior

The NT mode is treated as a digital mode by the RX Controls applet. Specifically:

- NT follows the same filter width presets and step sizes as DIGU and DIGL.
- The filter width label calculates bandwidth the same way as DIGU (using the high-edge value).
- The SQL button and squelch level slider are disabled when NT is active, because audio is routed via DAX and squelch is not meaningful. If squelch was on when you switched to NT, it is turned off automatically and the previous state is saved for restoration when you leave NT mode.

## Squelch behavior in RTTY and digital modes

Starting in v26.5.1, the squelch controls (SQL button and squelch level slider) are also disabled in RTTY mode, in addition to the existing digital modes (DIGU, DIGL) and NT mode. This change ensures that squelch does not notch out FSK characters, which would otherwise break decoding.

When you switch to RTTY mode:
- The SQL button and squelch level slider are automatically disabled.
- If squelch was on when you switched to RTTY, it is turned off automatically and the previous state is saved for restoration when you leave RTTY or digital mode.
- CW modes (CW, CWL) continue to have squelch disabled as before, with squelch state managed by the radio itself.

## RADE mode safety

In v26.5.2.1, the RADE mode deactivation logic was updated to reflect that "RADE" is a client-side only mode. The radio itself does not understand RADE as a distinct mode — when RADE is active, the radio echoes back the underlying real mode (DIGL or DIGU) immediately.

The applet emits `radeActivated(false)` only if the slice was actually in RADE mode when the mode combo selection changed, preventing stale deactivate signals when changing modes on a non-RADE slice.

This fix addresses the following scenarios:
- Switching between non-RADE modes on a slice that was never in RADE.
- RADE was activated externally (via the VFO widget combo, profile load on startup, or `MainWindow::activateRADE`).

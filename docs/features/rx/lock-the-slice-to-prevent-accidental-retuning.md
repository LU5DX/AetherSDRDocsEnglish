# Lock the slice to prevent accidental retuning

The tune-lock feature prevents a slice from responding to frequency changes. Use it when you want to monitor a fixed frequency without the risk of nudging the VFO by clicking the panadapter or scrolling the mouse wheel.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

## Steps

1. In the RX Controls applet, identify the header row containing the slice badge, lock button, and antenna selectors.
2. If you have more than one slice, click the appropriate slice tab (A through H) to select the slice you want to lock.
3. Click the 🔓 button in the header row. The icon changes to 🔒 and turns blue, confirming the slice is locked.
4. To unlock, click 🔒 again. The icon returns to 🔓 and the slice resumes responding to frequency changes.

## What each control does

| Control | Default      | Behavior                                                                                                                |
|---------|--------------|-------------------------------------------------------------------------------------------------------------------------|
| 🔓 / 🔒   | 🔓 (unlocked) | Toggles tune-lock on the active slice. When locked (🔒), the slice ignores all frequency changes. Click again to unlock. |
## Tips

- The lock state applies per slice. You can lock slice A while slice B remains freely tunable.
- The lock button is always visible in the header row regardless of the current mode.
- From v0.9.3, the slice tab buttons and the slice badge both use per-slice colors managed by SliceColorManager. Colors are customizable per slice and persist across sessions. The same color is reflected in the slice tab buttons, the slice badge, VFO widgets, and meter strips.

## Slice tab behavior on reconnect (v0.9.5.1)

When the radio disconnects or the number of available slices changes, AetherSDR now tears down all generated slice tab buttons and restores the static slice badge automatically (`clearSliceButtons()`, #2254). On reconnect, the tab row is rebuilt to match the new slice count. If the count has not changed, the existing buttons are reused without a rebuild.

Signal connections between the slice button group and the `sliceActivationRequested` handler are guarded so that reconnecting to the radio does not accumulate duplicate signal handlers.

## Filter preset storage format (v0.9.5.1)

Filter presets saved for a given mode (setting key `FilterPresets`) now support two storage formats:

- **Width only** — a plain integer representing the filter bandwidth in Hz (for example, `2700`). This is the legacy format and continues to work.
- **Lo:Hi** — a colon-separated pair of low-edge and high-edge offsets in Hz (for example, `-1400:1300`). This format preserves an asymmetric passband exactly as you set it by dragging the filter passband widget edges.

When you right-click a filter preset button to save the current width, AetherSDR writes the `lo:hi` form when the passband is asymmetric (#2259). Presets saved in the old width-only format are read and applied as centred passbands, exactly as before.

Up to six presets are stored and displayed per mode in the RX Controls applet. Buttons are hidden for FM, NFM, and DFM modes.

## Step filter width (v0.9.8)

The filter width preset system now supports a `stepFilterWidth()` method that walks the per-mode preset list. This enables widen/narrow shortcuts that produce mode-correct edge geometry for all modes (LSB, CWL, DIGL, RTTY, AM, CW, USB).

When you apply a widen or narrow operation:

- AetherSDR finds the closest matching preset width to the current filter passband.
- It then selects the next wider or narrower preset from the per-mode list.
- The preset is applied through `applyFilterPreset()`, which uses the correct edge offsets for the current mode.

This ensures that widening or narrowing a filter always stays within the mode-appropriate preset values and produces the correct passband geometry.

## Filter width formatting (v0.9.8)

The `formatFilterWidth()` method is now a public static function, shared with the VFO panel (`VfoWidget`). This ensures both the RX Controls applet and the VFO panel display identical filter width readouts. The method uses mode-aware logic so SSB and digital modes display the correct labelled width (#2197).

## NT and RTTY mode squelch behavior (v26.5.1)

Squelch is disabled in NT mode, RTTY mode, and the existing digital modes (`DIGU`, `DIGL`). This prevents squelch from gating weak FSK signals and notching out characters, which would break decoding (#2504). If squelch was active when you switched into RTTY or a digital mode, AetherSDR turns it off automatically and saves the state so it can be restored when you leave the mode. The squelch button and slider remain disabled while the mode is active.

## RADE mode activation (v26.5.1)

When you select RADE mode from the mode combo box, the slice mode is set immediately on the slice before issuing the `radeActivated` signal. When switching away from RADE mode to any other mode, the `radeActivated(false)` deactivation is only emitted if the slice was actually in RADE mode prior to the switch. This defense-in-depth logic prevents spurious deactivation signals in the following scenarios:

- Swapping between non-RADE modes (e.g., USB to LSB) on a slice that was never in RADE — no deactivate signal is sent.
- Rebinding a slice via `setSlice()` — the current mode is always read from the bound slice, not from a leftover flag.
- Externally activated RADE (via VFO combo, profile load on startup, or `MainWindow::activateRADE`) — the slice's mode is `"RADE"` regardless of how it got there, so the deactivate is correctly sent.

## NT mode

Version 0.9.3 adds the `NT` mode alongside the existing digital modes (`DIGU`, `DIGL`). It behaves identically to other digital modes in the following ways:

- **Filter presets** — NT shares the DIG filter preset set (100–2000 Hz). The filter width label updates accordingly.
- **Filter width calculation** — The filter width display measures the high-edge offset, the same as USB and DIGU.
- **Squelch** — The SQL button and squelch slider are disabled in NT mode. Because audio is routed via DAX in digital modes, squelch is not meaningful. If squelch was active when you switched into NT mode, AetherSDR turns it off automatically and restores it when you leave NT mode.

## Related

- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
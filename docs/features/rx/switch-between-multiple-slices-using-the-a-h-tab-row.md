# Switch between multiple slices using the A..H tab row

The FLEX-8600 supports up to eight simultaneous receive slices. The A..H tab row at the top of the RX Controls applet lets you switch which slice the applet is bound to, so you can view and adjust each slice's mode, frequency, filter, and other settings independently.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The RX Controls applet requires an active radio connection.
- The radio must have more than one slice active. The tab row is hidden when only one slice exists.
- The RX Controls applet must be visible. If it is not, click the RX tray button on the right sidebar to show it.

## Steps

1. Look at the top of the RX Controls applet for the horizontal row of lettered tabs (A, B, C, and so on, up to H).
2. Click the tab letter that corresponds to the slice you want to inspect or control.
3. Confirm the switch: the **Slice badge** in the header row updates to show the letter of the newly selected slice, coloured by its slice identity.
4. All controls below the tab row — mode, frequency, filter, AGC, AF gain, and others — now reflect and control the selected slice.

## What each control does

| Control           | Behavior                                                                       | Notes                                                                                                                                                                                                                                                       |
|-------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Slice tabs (A..H) | Selects which slice the RX applet is bound to; emits sliceActivationRequested. | Row hidden if maxSlices <= 1. clearSliceButtons() tears down all generated tab buttons and restores the static slice badge on disconnect (v0.9.5.1, #2254). Slice button click connections are guarded against duplicate signal handlers across reconnects. |
| Slice badge       | Displays the letter of the currently bound slice.                              | Coloured by slice identity.                                                                                                                                                                                                                                 |
## NT mode behavior

v0.9.3 adds `NT` as a recognized digital mode alongside `DIGU` and `DIGL`. The following behaviors apply to NT mode:

- **Filter width presets** use the same preset list as DIGU and DIGL (100–2000 Hz range).
- **Filter width display** calculates bandwidth from the high edge, matching the USB/DIGU/FDV convention.
- **Squelch** is disabled when NT mode is active. Audio is routed via DAX, so the squelch control is not meaningful. If squelch was on when you switched to NT, AetherSDR saves its state and turns it off automatically. Switching away from NT restores the previous squelch state.

## Filter preset storage format

Starting in v0.9.5.1, filter presets saved under the `FilterPresets` setting key can store either a plain width value or a fully specified passband as a `lo:hi` pair (#2259). This matches the format used by VfoWidget.

- A plain entry such as `2700` records only the filter width. When applied, AetherSDR centres the passband around the current carrier point.
- A `lo:hi` entry such as `-1400:1300` records both edges. When applied, AetherSDR restores the exact passband position as well as the width.

Right-clicking a **Filter width presets** button saves the current passband in `lo:hi` format so that both edges are preserved on reload. Older plain-width entries saved by earlier versions remain valid and are read without error.

## Tips

- The tab row is hidden entirely when the radio reports a maximum slice count of 1. If you do not see any tabs, only one slice is configured on the radio.
- If the number of active slices changes while AetherSDR is connected, the tab row is rebuilt automatically. The previous set of buttons is torn down by `clearSliceButtons()` before the new buttons are created, preventing stale click handlers from accumulating across reconnects.
- Each slice retains its own mode, frequency, filter presets, AGC settings, and antenna selection. Switching tabs does not alter any slice's settings; it only changes which slice the applet displays.
- Filter width presets are saved per mode via the `FilterPresets` setting. Presets you save on slice A in USB mode apply to USB mode on all slices.

## Related

- [RX Controls overview](overview.md)
- [Understanding slices and VFOs](../../getting-started/concepts/understanding-slices.md)
- [Tune the radio to a frequency (type MHz in the readout)](tune-the-radio-to-a-frequency-type-mhz-in-the-readout.md)
- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Pick a filter width preset for the current mode](pick-a-filter-width-preset-for-the-current-mode.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-01 -->
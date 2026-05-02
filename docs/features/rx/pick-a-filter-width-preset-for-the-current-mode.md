# Pick a filter width preset for the current mode

Use the filter width preset buttons in the RX Controls applet to quickly apply a standard passband width for the active mode. Presets are saved per mode in `FilterPresets`.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Select the slice you want to adjust using the slice tabs (A..H) if more than one slice is active.
- Set the slice mode first. Preset values differ by mode, and presets are not shown for FM, NFM, or DFM modes.

## Steps

1. Open the RX Controls applet. If it is not visible, click the RX tray button on the right sidebar.
2. If the slice tab row is visible, click the tab (A through H) for the slice you want to adjust.
3. Confirm the mode shown in the Mode combo is correct. Filter presets change when the mode changes.
4. Click any of the filter width preset buttons to apply that bandwidth immediately. The current filter width shown in the filter width label (for example, `2.7K`) updates to reflect the applied preset.
5. To save the current filter passband as a preset, right-click any filter width preset button and choose to save the current width. The value is stored in `FilterPresets`.

## What each control does

| Control                | Behavior                                                                                                                                                                | Default presets by mode |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| Filter width presets   | Click to apply a preset bandwidth to the current slice. Right-click to save the current filter width as a preset. Hidden in FM, NFM, and DFM modes.                     | See table below         |
| Filter width label     | Read-only indicator showing the current filter bandwidth (for example, `2.7K`, `500`, `6.0K`). Updates when a preset is applied or when the passband edges are dragged. | —                       |
| Filter passband widget | Drag the low or high edge to set a custom passband. Use presets for standard widths.                                                                                    | —                       |
| Mode                   | Preset widths (Hz)                                                                                                                                                      |                         |
| ---                    | ---                                                                                                                                                                     |                         |
| USB, LSB               | 1800, 2100, 2400, 2700, 2900, 3300                                                                                                                                      |                         |
| AM, SAM                | 5600, 6000, 8000, 10000, 12000, 14000                                                                                                                                   |                         |
| CW                     | 50, 100, 250, 400                                                                                                                                                       |                         |
| DIGU, DIGL, NT         | 100, 300, 600, 1000, 1500, 2000                                                                                                                                         |                         |
| RTTY                   | 250, 300, 350, 400, 500, 1000                                                                                                                                           |                         |
| FM, NFM, DFM           | No presets (buttons hidden)                                                                                                                                             |                         |

## Filter preset storage format (v0.9.5.1)

Starting in v0.9.5.1, filter presets stored in `FilterPresets` can represent either a plain bandwidth or a fully specified passband with explicit low and high edge offsets. Both formats are accepted when loading saved presets.

- **Width-only format** — A single integer representing bandwidth in Hz (for example, `2700`). When applied, the radio positions the passband symmetrically around the carrier according to the mode's default offset rules.
- **Lo:Hi format** — Two integers separated by a colon representing the low and high passband edge offsets in Hz (for example, `300:3000`). The width is derived as `hi − lo`. The `hi` value must be greater than the `lo` value or the entry is ignored.

Entries in either format may appear in the same saved preset list for a given mode. The list is comma-separated. Up to six entries are loaded for the RX Controls applet (matching the maximum number of preset buttons displayed).

If a saved preset list is changed externally or a reconnect causes the radio to report a different slice count, the preset buttons are rebuilt automatically to reflect the stored values.

## Noise reduction and DSP filter button visibility

The following table summarises which noise-reduction and DSP filter buttons are visible based on radio series and mode.

| Button | 6000-series | 8000-series (extended DSP) | Hidden when |
|--------|-------------|---------------------------|-------------|
| NR     | Yes         | Yes                       | FM mode     |
| NR2    | Yes         | Yes                       | FM mode     |
| NB     | Yes         | Yes                       | FM mode     |
| NRL    | Yes         | Yes                       | FM mode     |
| NRS    | No          | Yes                       | FM mode     |
| RNN    | No          | Yes                       | CW or FM mode |
| NRF    | No          | Yes                       | FM mode     |

Prior to V0.9.4, the NRL button was only shown on 8000-series radios (extended DSP). Starting in V0.9.4, NRL is also available on 6000-series radios. NRS, RNN, and NRF remain 8000-series only.

## Slice tab and badge colors (v0.9.3)

Starting in v0.9.3, slice tab buttons and the slice badge use per-slice colors managed by the `SliceColorManager` singleton rather than a fixed color table. The active border, background highlight on the tab buttons, and the badge background all reflect the color assigned to that slice. Colors persist across sessions and are also reflected in VFO widgets and meter strips. No action is required; the colors update automatically when a slice is connected.

## Slice tab behavior on reconnect (v0.9.5.1)

When AetherSDR disconnects from the radio and reconnects, or when the number of available slices changes, the slice tab row is rebuilt correctly. Specifically:

- If the number of slices reported by the radio differs from the number of tab buttons currently shown, `clearSliceButtons()` tears down all existing tab buttons and the row is reconstructed from scratch.
- While the tab row is torn down, the static slice badge is restored so the applet continues to show which slice is bound.
- Signal connections from the tab buttons to the slice activation handler are established only once per applet instance, preventing duplicate handlers from accumulating across reconnects.

No user action is required. If the slice count changes (for example, after a disconnect and reconnect cycle), the tab row updates automatically.

## Tips

- If you need a width that does not match any preset, drag the edges of the filter passband widget to set an arbitrary value, then right-click a preset button to save that width for future use.
- When saving a preset by right-clicking a preset button, the passband is stored in lo:hi format if the current passband edges have been set explicitly, or in width-only format otherwise. Both formats are loaded correctly on all subsequent sessions.
- Presets are per mode. Switching modes reshapes the filter and displays the preset buttons for the new mode.
- NT mode uses the same filter presets and squelch behavior as DIGU and DIGL. Squelch is disabled in NT mode and squelch off is sent to the radio automatically if squelch was previously enabled.

## Troubleshooting

- **Preset buttons are not visible** — The active mode is FM, NFM, or DFM. These modes do not expose filter presets. Change the mode using the Mode combo to a mode that supports presets (for example, USB or CW).
- **Right-click on a preset button does nothing visible** — Confirm the slice is connected to the radio. The RX applet requires an active radio connection to save preset values.
- **NRL button is not visible on a 6000-series radio** — Confirm you are running V0.9.4 or later. Earlier versions restricted NRL to 8000-series radios only.
- **Squelch controls are greyed out** — The active mode is DIGU, DIGL, NT, CW, or CWL. Squelch is disabled in these modes. In digital modes (including NT) squelch is turned off automatically; in CW modes the radio manages squelch state directly.
- **Slice tab row is blank after reconnecting** — This could occur on versions prior to v0.9.5.1. Upgrade to v0.9.5.1 or later. The tab row is now rebuilt automatically when the slice count changes on reconnect.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-01 -->
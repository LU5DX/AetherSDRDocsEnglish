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

| Control | Behavior | Default presets by mode | Persisted key |
|---|---|---|---|
| Filter width presets | Click to apply a preset bandwidth to the current slice. Right-click to save the current filter width as a preset. Hidden in FM, NFM, and DFM modes. | See table below | `FilterPresets` |
| Filter width label | Read-only indicator showing the current filter bandwidth (for example, `2.7K`, `500`, `6.0K`). Updates when a preset is applied or when the passband edges are dragged. | — | — |
| Filter passband widget | Drag the low or high edge to set a custom passband. Use presets for standard widths. | — | — |

**Default preset values by mode:**

| Mode | Preset widths (Hz) |
|---|---|
| USB, LSB | 1800, 2100, 2400, 2700, 2900, 3300 |
| AM, SAM | 5600, 6000, 8000, 10000, 12000, 14000 |
| CW | 50, 100, 250, 400 |
| DIGU, DIGL | 100, 300, 600, 1000, 1500, 2000 |
| RTTY | 250, 300, 350, 400, 500, 1000 |
| FM, NFM, DFM | No presets (buttons hidden) |

## Tips

- If you need a width that does not match any preset, drag the edges of the filter passband widget to set an arbitrary value, then right-click a preset button to save that width for future use.
- Presets are per mode. Switching modes reshapes the filter and displays the preset buttons for the new mode.

## Troubleshooting

- **Preset buttons are not visible** — The active mode is FM, NFM, or DFM. These modes do not expose filter presets. Change the mode using the Mode combo to a mode that supports presets (for example, USB or CW).
- **Right-click on a preset button does nothing visible** — Confirm the slice is connected to the radio. The RX applet requires an active radio connection to save preset values.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)

# Pick a filter width preset for the current mode

Filter width presets let you apply a standard bandwidth to the active slice with a single click, or save your own preferred width as a preset. Presets are specific to the current mode.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- The slice you want to adjust must be selected. If you have multiple slices, use the slice tabs (A..H) at the top of the RX Controls applet to select the correct one.
- Filter width presets are not available in FM, NFM, or DFM modes. Switch to a different mode if the preset buttons are not visible.

## Steps

### Apply a preset

1. Open the RX Controls applet. If it is not visible, click the **RX** tray button on the right sidebar.
2. If using multiple slices, click the correct slice tab (A..H) to bind the applet to that slice.
3. In the filter preset row, click the button showing the width you want. The current filter width indicator (e.g. **2.7K**) updates immediately.

### Save a custom preset

1. Set the filter passband to the width you want to save by dragging the lo/hi edges of the filter passband widget.
2. Right-click any filter width preset button.
3. Select the option to save the current width to that preset position. The button label updates to reflect the new value. The custom value is persisted in `FilterPresets`.

## What each control does

| Control | Behavior | Default presets by mode | Setting key |
|---|---|---|---|
| Filter width presets | Click to apply that width to the slice filter. Right-click to overwrite the preset with the current filter width. Hidden in FM/NFM/DFM modes. Presets are per-mode. | See table below | `FilterPresets` |
| Filter width indicator (**2.7K**) | Read-only display showing the current filter bandwidth in kHz or Hz. Updates when a preset is applied or the passband edges are dragged. | — | — |
| Filter passband widget | Drag the lo or hi edge to set a custom filter width. | — | — |

**Default preset values by mode:**

| Mode | Preset widths |
|---|---|
| USB, LSB | 1800 / 2100 / 2400 / 2700 / 2900 / 3300 Hz |
| AM, SAM | 5600 / 6000 / 8000 / 10000 / 12000 / 14000 Hz |
| CW | 50 / 100 / 250 / 400 Hz |
| DIGU, DIGL | 100 / 300 / 600 / 1000 / 1500 / 2000 Hz |
| RTTY | 250 / 300 / 350 / 400 / 500 / 1000 Hz |
| FM, NFM, DFM | No presets (buttons hidden) |

## Tips

- When you change mode (e.g. from USB to CW), the preset buttons repopulate with the widths for the new mode. Any custom presets you saved are stored per mode in `FilterPresets`.
- For fine control beyond what the presets offer, drag the edges of the filter passband widget directly. Right-click a preset button afterward to save that width for future use.

## Troubleshooting

- **Preset buttons are not visible** — The active slice is in FM, NFM, or DFM mode. Filter presets are not available for FM family modes. Switch to a different mode to see the preset buttons.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)
- [RX Controls overview](overview.md)

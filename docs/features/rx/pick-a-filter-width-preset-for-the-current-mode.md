# Pick a filter width preset for the current mode

Filter width presets let you apply a standard bandwidth to the active slice with a single click, matched to the current mode. Use them to quickly switch between wide and narrow filter widths without dragging the passband edges manually.

## Before you start

- AetherSDR must be connected to a Flex radio.
- The RX applet must be open. If it is not visible, click the RX tray button on the right sidebar to show it.
- Select the slice you want to adjust using the slice tabs (A..H) at the top of the RX applet.

## Steps

1. Check the **Mode combo** to confirm the slice is set to the mode you want. Filter presets are per-mode; changing mode after step 2 will reshape the presets.
2. Locate the row of filter width preset buttons in the RX applet. The current filter width is shown in the **2.7K** indicator in the header row.
3. Click the preset button for the bandwidth you want. The **2.7K** indicator updates immediately to reflect the applied width.
4. To save the current filter width as a preset, right-click any preset button and choose to save the current width into that slot. The value is persisted under `FilterPresets`.

## What each control does

| Control | Behavior | Valid values | Persisted key |
|---|---|---|---|
| Filter width presets | Click to apply a preset filter width to the active slice. Right-click to save the current width as a preset. | See ranges below by mode. | `FilterPresets` |
| **2.7K** (filter width indicator) | Displays the current filter bandwidth in kHz or Hz. Updates when a preset is applied or the passband is dragged. | Read-only. | — |
| Filter passband widget | Drag the low or high edge to set a custom filter width outside the presets. | — | — |

### Preset values by mode

| Mode | Available preset widths |
|---|---|
| USB, LSB | 1800, 2100, 2400, 2700, 2900, 3300 Hz |
| AM, SAM | 5600, 6000, 8000, 10000, 12000, 14000 Hz |
| CW | 50, 100, 250, 400 Hz |
| DIGU, DIGL | 100, 300, 600, 1000, 1500, 2000 Hz |
| RTTY | 250, 300, 350, 400, 500, 1000 Hz |
| FM, NFM, DFM | No preset buttons shown. |

## Tips

- Preset buttons are hidden entirely when the slice is in FM, NFM, or DFM mode. Switch to a non-FM mode to see them.
- To fine-tune beyond the presets, drag the lo or hi edge of the Filter passband widget directly.
- The `FilterPresets` setting is saved per mode, so customising CW presets does not affect SSB presets.

## Troubleshooting

- **No preset buttons are visible** — The slice is in FM, NFM, or DFM mode. Filter presets are not available for FM-family modes. Change mode using the **Mode combo** to see presets.
- **Clicking a preset has no effect** — Confirm the slice is not tune-locked. A closed padlock icon (🔒) in the header row means the slice ignores changes. Click the lock icon to unlock it.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [Lock the slice to prevent accidental retuning](lock-the-slice-to-prevent-accidental-retuning.md)
- [RX Controls overview](overview.md)

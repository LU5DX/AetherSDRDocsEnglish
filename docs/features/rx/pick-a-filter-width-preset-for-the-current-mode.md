# Pick a filter width preset for the current mode

Filter width presets let you switch the receive passband to a standard width in one click. Presets are grouped by mode, so the buttons shown change when you change mode. The selected width is reflected immediately in the filter width indicator and the filter passband widget.

## Before you start

- AetherSDR must be connected to the radio. The RX Controls applet requires an active radio connection.
- Select the slice you want to adjust using the slice tabs (A..H) at the top of the RX Controls applet.
- Set the mode you want to work in using the Mode combo, because presets are mode-specific.

## Steps

1. If the RX Controls applet is not visible, click the **RX** tray button on the right sidebar to show it.
2. Confirm the correct slice is active by checking the slice badge (A/B/C/D/E/F/G/H) in the applet header. Click the appropriate slice tab if not.
3. Confirm the correct mode is set in the **Mode combo**. Preset buttons are not shown for FM, NFM, or DFM modes.
4. Locate the filter width preset buttons below the Mode combo. Each button shows a width value (for example, **1800**, **2700**, or **3300** for USB/LSB).
5. Click the preset button for the width you want. The **2.7K** filter width indicator in the header updates to reflect the new width, and the filter passband widget adjusts to match.
6. To save the current filter width as a custom preset, right-click any preset button and follow the prompt to store the current width in that slot. The value is persisted in `FilterPresets`.

## What each control does

| Control | Description | Valid values | Persisted key |
|---|---|---|---|
| Filter width presets | Buttons that apply a standard passband width for the current mode. Not shown for FM/NFM/DFM. | USB/LSB: 1800, 2100, 2400, 2700, 2900, 3300 Hz; AM/SAM: 5600, 6000, 8000, 10000, 12000, 14000 Hz; CW: 50, 100, 250, 400 Hz; DIGU/DIGL: 100, 300, 600, 1000, 1500, 2000 Hz; RTTY: 250, 300, 350, 400, 500, 1000 Hz | `FilterPresets` |
| Filter width indicator | Read-only label in the applet header showing the current filter width (e.g. **2.7K**). | Updates on preset selection or manual passband drag. | — |
| Filter passband widget | Drag the lo/hi edges to set a width not covered by a preset. | Drag handles on lo and hi filter edges. | — |

## Tips

- Right-clicking a preset button lets you overwrite that slot with the current passband width, so you can tailor presets to your operating habits without losing the other slots.
- After applying a preset, you can fine-tune the edges by dragging the lo or hi handle in the filter passband widget. The width indicator updates in real time.
- FM, NFM, and DFM modes do not show preset buttons. The radio manages the passband automatically in those modes.

## Related

- [Change mode (USB, LSB, CW, AM, FM, etc.)](change-mode-usb-lsb-cw-am-fm-etc.md)
- [RX Controls overview](overview.md)
- [Switch between multiple slices using the A..H tab row](switch-between-multiple-slices-using-the-a-h-tab-row.md)

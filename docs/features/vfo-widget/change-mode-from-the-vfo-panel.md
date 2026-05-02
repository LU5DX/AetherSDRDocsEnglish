# Change mode from the VFO panel

Use the VFO panel's Mode tab to switch the demodulation mode for any slice — for example, from USB to CW or FM — without leaving the spectrum view.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel must be open. If it is not visible, click the VFO marker flag on the spectrum display for the slice you want to change.

## Steps

1. Click the VFO marker flag on the spectrum display for the target slice. The VFO panel opens, anchored to the left of the marker.
2. Click the **Mode** tab inside the VFO panel.
3. Click the **Mode combo** and select the desired mode from the list.

## What each control does

| Control | Default | Valid values | Persisted setting |
|---|---|---|---|
| Mode combo | USB | USB, LSB, CW, CWL, AM, SAM, DIGU, DIGL, FM, NFM, DFM, RTTY | — |
| Filter preset buttons | — | Saved filter width presets | `FilterPresets` |

**Mode combo** — sets the demodulation mode for the slice. Selecting a new mode takes effect immediately on the radio.

**Filter preset buttons** — appear on the same Mode tab. Each button applies a saved filter width. Right-click a button to save the current filter width into that slot. Presets are persisted in `FilterPresets`.

## Tips

- Changing mode may alter the active filter passband. Check the filter width label in the header row after switching modes, and apply a filter preset if needed.
- The filter width label in the VFO panel header shows the current bandwidth. Click it to cycle through the filter preset buttons on the Mode tab.

## Related

- [Apply a filter width preset from the VFO panel](apply-a-filter-width-preset-from-the-vfo-panel.md)
- [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)
- [VFO Panel overview](overview.md)

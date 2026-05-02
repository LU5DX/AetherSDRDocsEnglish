# Change the VFO Marker Line Thickness

Use the marker thickness button to control how prominent the VFO marker line appears on the spectrum display, or to hide it entirely. The setting is saved per slice.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel must be open for the slice you want to adjust. If it is not visible, click the VFO marker flag for that slice on the spectrum display.

## Steps

1. Open the VFO panel for the target slice by clicking its VFO marker flag on the spectrum display.
2. Locate the **Marker thickness button** in the VFO panel.
3. Click the button to cycle through the available values: **Off**, **1 px**, and **3 px**.
4. Stop clicking when the desired thickness is shown. The marker on the spectrum display updates immediately.

## What each control does

| Control | Default | Valid values | Persisted setting |
|---|---|---|---|
| Marker thickness button | 1 px | Off, 1 px, 3 px | `Slice{N}_MarkerWidth` |

Each click advances to the next value in the cycle: **Off** → **1 px** → **3 px** → **Off**. The setting is persisted per slice, so slice 1 and slice 2 can have different thicknesses.

## Tips

- Setting the marker to **Off** hides the vertical line entirely. The VFO panel and flag remain visible and functional.
- If you run multiple slices on the same panadapter, increasing one marker to **3 px** can help distinguish it from adjacent slices.

## Related

- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)

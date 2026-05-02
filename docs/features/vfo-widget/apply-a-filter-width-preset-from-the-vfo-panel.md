# Apply a filter width preset from the VFO panel

Filter preset buttons let you switch the receive filter width for a slice with a single click. Use them to move quickly between common bandwidths — for example, between a wide 3 kHz SSB filter and a narrow 500 Hz CW filter — without leaving the spectrum view.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to a frequency-only strip, click anywhere on it to expand it first.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens, anchored to the left of the marker.
2. Click the **Mode** tab inside the VFO panel.
3. Click the filter preset button that corresponds to the bandwidth you want. The radio immediately applies that filter width to the slice.

To save the current filter width into a preset slot:

1. Set the filter to the bandwidth you want to save (see [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)).
2. Right-click the preset button slot you want to overwrite.
3. The current filter width is saved into that slot.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Filter preset buttons (Mode tab) | Each button applies a saved filter width preset to the slice. Left-click to apply; right-click to save the current filter width into that slot. Custom low and high filter edges can be stored per slot via right-click. | — | `FilterPresets` |
| Filter width label | Displays the current filter bandwidth. Click to cycle through the filter preset buttons in the Mode tab. | — | — |

## Tips

- The filter width label in the VFO panel header shows the active bandwidth at all times. Click it directly to cycle through the preset buttons without switching to the Mode tab first.
- Preset slots are shared across all slices and modes. Overwriting a slot affects every slice that uses it.
- Filter edge lines on the spectrum panadapter reflect the active filter width. If the lines are hidden, enable them with the Filter edges button in the VFO panel. See [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md).

## Related

- [Set a custom filter edge from the VFO panel](set-a-custom-filter-edge-from-the-vfo-panel.md)
- [Change mode from the VFO panel](change-mode-from-the-vfo-panel.md)
- [Hide or show filter edge lines on the spectrum](hide-or-show-filter-edge-lines-on-the-spectrum.md)
- [VFO Panel overview](overview.md)

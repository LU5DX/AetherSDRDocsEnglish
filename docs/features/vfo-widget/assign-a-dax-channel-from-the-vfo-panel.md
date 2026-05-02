# Assign a DAX channel from the VFO panel

DAX (Digital Audio Exchange) routes a slice's received audio to a named audio channel on your computer. Use this procedure to assign or change the DAX channel for any slice directly from its VFO panel.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The DAX audio bridge must be running. If it is not, enable it via `Settings > Autostart DAX with AetherSDR` and restart AetherSDR, or start it manually.
- The VFO panel for the target slice must be open and expanded. If it is collapsed to the frequency-only strip, click anywhere on it to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to configure. The VFO panel opens, anchored to the left of the marker.
2. Click the **DAX** tab inside the VFO panel.
3. Click the **DAX channel combo** and select a channel from the drop-down list.
4. To disable DAX routing for this slice, select **Off**.

## What each control does

| Control | Default | Valid values | Persisted setting key |
|---|---|---|---|
| DAX channel combo | Off | Off, 1–8 | — |

The DAX channel combo assigns a DAX audio channel to the current slice. Selecting a numbered channel routes the slice's received audio to that DAX channel. Selecting **Off** removes the assignment. This setting reflects live radio state and is not persisted locally by AetherSDR.

## Tips

- Each DAX channel can be assigned to only one slice at a time. If you assign a channel that is already in use by another slice, the radio will move the assignment.
- If the VFO panel would be clipped by the window edge, it flips to the right side of the marker automatically.

## Troubleshooting

- **DAX channel combo has no effect / audio does not appear on the host** — Confirm the DAX audio bridge is running. Check `Settings > Autostart DAX with AetherSDR`. On macOS and PipeWire systems, the bridge must be active for DAX channels to appear as audio devices.
- **DAX tab is not visible** — The VFO panel may be collapsed. Click the collapsed strip to expand it, then select the DAX tab.

## Related

- [VFO Panel overview](overview.md)
- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)

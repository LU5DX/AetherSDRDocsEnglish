# Hide or show filter edge lines on the spectrum

The VFO panel gives you a per-slice toggle to hide or show the vertical lines that mark the edges of the receive filter passband on the spectrum display. Hiding them reduces visual clutter when you want a cleaner panadapter view.

## Before you start

- AetherSDR must be connected to the radio.
- The slice you want to adjust must have a VFO marker visible on the spectrum display.

## Steps

1. Click the VFO marker flag on the spectrum display for the target slice. The VFO panel opens anchored to the marker.
2. Locate the **Filter edges button** in the VFO panel.
3. Click **Filter edges button** to toggle the filter edge lines off. Click it again to restore them.

The state is saved immediately. When you reopen AetherSDR, the setting is restored to whichever state you left it in for that slice.

## What each control does

| Control | Default | Persisted setting |
|---|---|---|
| **Filter edges button** | Shown (edges visible) | `Slice{N}_FilterEdgesHidden` |

`{N}` is the slice number. Each slice stores its own value independently.

## Tips

- The setting is per-slice. Hiding filter edges on slice 0 does not affect slice 1 or any other slice.
- If you have collapsed the VFO panel to frequency-only view, expand it first by clicking the collapsed strip to access the **Filter edges button**.

## Related

- [Change the VFO marker line thickness](change-the-vfo-marker-line-thickness.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)

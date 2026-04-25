# Turn Spots on or off

DX spots appear as overlays on the panadapter, showing callsigns and frequencies from your configured spot sources. This page explains how to enable or disable the spot overlay and the related memory overlay using the master toggles in Spot Settings.

## Before you start

- Open a panadapter. The Spot Settings dialog is accessed from the panadapter context menu.
- Spots will only appear if you have at least one spot source configured. See `Settings > SpotHub...` to configure DX cluster or other sources.

## Steps

1. Right-click anywhere on the panadapter to open the context menu.
2. Select the spot overlay option to open the **Spot Settings** dialog.
3. Locate the **Spots:** row. Click the toggle button to switch between **Enabled** and **Disabled**.
4. To also show memory channels as panadapter overlays, locate the **Memories:** row and click its toggle button to switch between **Enabled** and **Disabled**.
5. Close the dialog. The change takes effect immediately.

## What each control does

| Label | Kind | Default | Persisted key | Behavior |
|---|---|---|---|---|
| **Spots:** | Toggle button | Enabled | `IsSpotsEnabled` | Master toggle for the DX spot overlay on the panadapter. |
| **Memories:** | Toggle button | Disabled | `IsMemoriesShownOnPanadapter` | Toggles memory channel overlays on the panadapter. |

## Tips

- The **Total Spots:** indicator at the bottom of the dialog shows how many live spots are currently tracked, which is useful for confirming that your spot sources are delivering data even when the overlay is disabled.
- Disabling **Spots:** hides the overlay without disconnecting your spot sources or clearing the spot cache.

## Related

- [Spot Settings overview](overview.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)

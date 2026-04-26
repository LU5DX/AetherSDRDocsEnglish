# Turn spots on or off

DX spots from your configured cluster sources can be shown or hidden on the panadapter at any time. Use the master spot toggle to enable or disable the entire spot overlay without changing any other settings.

## Before you start

- Open a panadapter. The Spot Settings dialog is accessed from the panadapter context menu.
- Ensure at least one spot source is configured in `Settings > SpotHub...` if you want spots to appear after enabling.

## Steps

1. Right-click anywhere on the panadapter to open the context menu.
2. Select the spot overlay option to open the **Spot Settings** dialog.
3. Locate the **Spots:** row.
4. Click the toggle button to switch between **Enabled** and **Disabled**.

The change takes effect immediately. The button label updates to reflect the current state, and `IsSpotsEnabled` is saved.

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **Spots:** toggle | Enabled | Master toggle. Hides or shows all DX spots on the panadapter. | `IsSpotsEnabled` |
| **Memories:** toggle | Disabled | Shows radio memory channels as spot-like markers on the panadapter. | `IsMemoriesShownOnPanadapter` |
| **Levels:** slider | 3 | Number of vertical stacking rows used when spots overlap. Range: 1–10. | `SpotsStackLevels` |
| **Position:** slider | 50 | Vertical position of the spot band on the panadapter, as a percentage from top. Range: 0–100. | `SpotsPosition` |
| **Font Size:** slider | 16 | Text size for spot labels. Range: 8–32 pt. | `SpotsFontSize` |
| **Spot Lifetime:** slider | 30 min | How long a spot remains visible before expiring. Steps run from 10 sec through 24 hrs. | `SpotsLifetime` |
| **Override Colors:** toggle | Disabled | Forces all spot labels to use a single text color instead of cluster-assigned colors. | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker | `#FFFF00` | Opens a color picker to select the override text color. Active only when **Override Colors:** is Enabled. | `SpotsOverrideColor` |
| **Override Background: Enabled** toggle | Enabled | Draws a solid background behind each spot label. | `IsSpotsOverrideBackgroundColorsEnabled` |
| **Override Background: Auto** toggle | Enabled | Automatically chooses a background color to contrast with the text color. | `IsSpotsOverrideToAutoBackgroundColorEnabled` |
| Spot background color picker | `#000000` | Opens a color picker to select a manual background color. Used when Auto is Disabled. | `SpotsOverrideBgColor` |
| **Background Opacity:** slider | 48 | Alpha value for the spot background. Range: 0–100. | `SpotsOverrideBgOpacity` |
| **Clear All Spots** | — | Removes all spots currently displayed on the panadapter. Does not affect settings. | — |

## Tips

- The **Total Spots:** indicator in the dialog shows how many spots are currently tracked, even when the **Spots:** toggle is Disabled.
- Disabling **Spots:** does not clear the internal spot list. Re-enabling restores all spots that have not yet expired.
- If you want spots hidden only temporarily, toggle **Spots:** off rather than disconnecting your cluster source in `Settings > SpotHub...`.

## Troubleshooting

- **Spots toggle is Enabled but no spots appear on the panadapter** — No spots have been received yet, or all received spots fall outside the current panadapter frequency range. Check your cluster connection at `Settings > SpotHub...`. The **Total Spots:** count will be zero if no data has arrived.
- **Spots reappear after restart even though you disabled them** — The `IsSpotsEnabled` setting is saved immediately when you toggle. If spots appear, the toggle may have been re-enabled by another session or profile load.

## Related

- [Spot Settings overview](overview.md)
- [Overlay memory channels on the panadapter](overlay-memory-channels-on-the-panadapter.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)
- [Clear every spot from the panadapter](clear-every-spot-from-the-panadapter.md)

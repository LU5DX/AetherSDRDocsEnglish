# Enlarge or shrink the spot font

Use this page to make spot callsign text larger or smaller on the panadapter. Adjusting the font size helps when spots are hard to read at a distance or when they overlap other display elements.

## Before you start

- AetherSDR must be running. A radio connection is not required to change this setting.
- The Spot Settings dialog must be accessible from the panadapter. If spots are not visible, confirm that the `IsSpotsEnabled` toggle is set to Enabled — see [Turn spots on or off](turn-spots-on-or-off.md).

## Steps

1. Right-click anywhere on the panadapter to open the context menu.
2. Select the spots overlay option to open the **Spot Settings** dialog.
3. Locate the **Font Size:** row.
4. Drag the slider left to decrease the font size or right to increase it. The current value in points is shown to the right of the slider.
5. Release the slider. The change takes effect immediately and is saved automatically.

## What each control does

| Control                          | Description                                                                                                                                                                                                                                                                                              | Default                        |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| **Spots:**                       | Master toggle for DX spot display. Click to toggle between enabled and disabled states. The button text updates to "Enabled" when spots are on and "Disabled" when spots are off. Stored in `IsSpotsEnabled`.                                                                                            | Enabled                        |
| **Memories:**                    | Toggles memory channel overlays on panadapter. Click to toggle between enabled and disabled states. The button text updates to "Enabled" when memories are on and "Disabled" when memories are off. Stored in `IsMemorySpotsEnabled`.                                                                    | Disabled                       |
| **Kiwi DX:**                     | Overlays KiwiSDR Community DX database spots (beacons, utilities, time signals) on the band plan strip. Click to toggle between enabled and disabled states. The button text updates to "Enabled" when Kiwi DX spots are on and "Disabled" when they are off. Stored in `ShowKiwiDxSpots`. New in v26.8.4. | Disabled                       |
| **Levels:**                      | Vertical stacking rows for spots. Range 1-10. Stored in `SpotsMaxLevel`.                                                                                                                                                                                                                                 | 3                              |
| **Position:**                    | Vertical position on panadapter as a percentage. Range 0-100. Stored in `SpotsStartingHeightPercentage`.                                                                                                                                                                                                 | 50                             |
| **Font Size:**                   | Sets the text size of spot callsigns and labels rendered on the panadapter. Range is 8–32 points. Stored in `SpotFontSize`.                                                                                                                                                                              | 16                             |
| **Spot Lifetime:**               | How long spots remain before fading. Non-linear scale from 10 seconds to 24 hours. Stored in seconds in `DxClusterSpotLifetimeSec`.                                                                                                                                                                      | 60 minutes                     |
| **Override Colors:**             | Forces a single text color for all spots. Click to toggle between enabled and disabled states. The button text updates to "Enabled" when override is on and "Disabled" when override is off. Stored in `IsSpotsOverrideColorsEnabled`.                                                                   | Disabled                       |
| **Spot text color picker**       | Opens a color dialog to pick text color. Stored in `SpotsOverrideColor`.                                                                                                                                                                                                                                 | #FFFF00                        |
| **Override Background: Enabled** | Draws a background under spot text. Click to toggle between enabled and disabled states. The button text updates to "Enabled" when background is on and "Disabled" when background is off. Stored in `IsSpotsOverrideBackgroundColorsEnabled`.                                                           | Enabled                        |
| **Override Background: Auto**    | Auto-picks background color for contrast. Stored in `IsSpotsOverrideToAutoBackgroundColorEnabled`.                                                                                                                                                                                                       | Enabled                        |
| **Spot background color picker** | Opens a color dialog for background color. Stored in `SpotsOverrideBgColor`.                                                                                                                                                                                                                             | #000000                        |
| **Background Opacity:**          | Alpha of spot background (0 = transparent, 100 = opaque). Stored in `SpotsBackgroundOpacity`.                                                                                                                                                                                                            | 48                             |
| **Spot Lines:**                  | Draws vertical lines from the spectrum baseline up to each spot label. Click to toggle between enabled and disabled states. The button text updates to "Enabled" when lines are on and "Disabled" when lines are off. Disable during contests to reduce visual clutter. Stored in `IsSpotsLinesEnabled`. | Enabled                        |
| **Clear All Spots**              | Clears all spots from the panadapter.                                                                                                                                                                                                                                                                    | N/A                            |

## Indicators

| Indicator | Description |
|---|---|
| **Total Spots:** | Shows count of live spots currently tracked. |

## Tips

- A font size of 16 is the default. Values toward 8 reduce clutter when many spots are visible; values toward 32 help when viewing the panadapter from a distance.
- Font size applies to all spots simultaneously. There is no per-spot size override.
- Enabling **Kiwi DX:** adds spots for beacons, utilities, and time signals from the KiwiSDR Community DX database to the band plan strip. This can be useful for monitoring propagation beacons, but may add clutter on busy bands.
- Disabling **Spot Lines:** can significantly reduce visual clutter during contests when a large number of spots are active.
- The Spot Settings dialog now respects the current theme. If you have a custom theme applied, the dialog title and Total Spots label will use your theme's text colors.
- Toggle buttons (Spots, Memories, Kiwi DX, Override Colors, Override Background: Enabled, Spot Lines) now display "Enabled" when the feature is active and "Disabled" when the feature is inactive. Check the button text to determine the current state.

## Related

- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
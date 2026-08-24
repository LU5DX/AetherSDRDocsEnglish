# Spot Settings Dialog

The **Spot Settings** dialog provides quick, stand-alone control over how DX spots and memory channel overlays render on the panadapter. You can adjust visibility, density, vertical position, text size, lifetime, spot lines, and color overrides.

## Opening the Spot Settings dialog

- Right-click anywhere on the spots overlay on the panadapter.
- Select **Spot Settings** from the context menu.

## Before you start

- The **Spots:** toggle master-switches all spot display. If it shows "Disabled", click it to enable spots first.

## What the controls do

| Control                          | Default                                                                                                 | Range                              |
|----------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------|
| **Spots:**                       | Enabled                                                                                                 | On/Off                             |
| **Memories:**                    | Disabled                                                                                                | On/Off                             |
| **Kiwi DX:**                     | Disabled                                                                                                | On/Off                             |
| **Levels:**                      | 3                                                                                                       | 1–10                               |
| **Position:**                    | 50                                                                                                      | 0–100 (% from top)                 |
| **Font Size:**                   | 16                                                                                                      | 8–32 points                        |
| **Spot Lifetime:**               | 10 min                                                                                                  | 10 sec – 24 hrs (non-linear steps) |
| **Override Colors:**             | Disabled                                                                                                | On/Off                             |
| Spot text color picker           | `#FFFF00`                                                                                               | (color)                            |
| **Override Background: Enabled** | Enabled                                                                                                 | On/Off                             |
| **Override Background: Auto**    | Enabled                                                                                                 | On/Off                             |
| Spot background color picker     | `#000000`                                                                                               | (color)                            |
| **Background Opacity:**          | 48                                                                                                      | 0–100 (0 = transparent)            |
| **Spot Lines:**                  | Enabled                                                                                                 | On/Off                             |
| **Clear All Spots**              | –                                                                                                       | –                                  |

## Kiwi DX spots

**Kiwi DX:** overlays spots from the KiwiSDR Community DX database on the band plan strip. These include beacons, utility stations, and time signal stations that are not typically reported by amateur DX cluster sources.

To enable Kiwi DX spots:

1. In the Spot Settings dialog, locate the **Kiwi DX:** row.
2. Click the toggle button so it reads **Enabled**. This persists as `ShowKiwiDxSpots`.
3. The Kiwi DX spots appear on the band plan strip immediately.

To disable Kiwi DX spots, click the toggle again so it reads **Disabled**.

## Indicator

| Indicator | Meaning |
|---|---|
| **Total Spots:** | Live count of DX spots currently tracked on the panadapter. |

## Toggle buttons display state

Each toggle button in the Spot Settings dialog updates its label to reflect the current enabled or disabled state. When a toggle is enabled the button reads **Enabled**; when disabled it reads **Disabled**. This applies to the following controls:

- **Spots:**
- **Memories:**
- **Kiwi DX:**
- **Override Colors:**
- **Override Background: Enabled**
- **Spot Lines:**

## Spot Lines

**Spot Lines:** draws a vertical line from the spectrum baseline up to each spot label. It is enabled by default.

To hide spot lines, click the toggle so it reads **Disabled**. This sets `IsSpotsLinesEnabled` to `False`. Disabling spot lines is useful during contests where many closely spaced spots create visual clutter on the panadapter.

To restore spot lines, click the toggle again so it reads **Enabled**.

## Force a single spot text color

Override the per-spot colors assigned by your DX cluster source and render all spot labels in one chosen color instead. Useful when the default colors clash with your panadapter theme or are hard to read.

1. In the Spot Settings dialog, locate the **Override Colors:** row.
2. Click the toggle button so it reads **Enabled**. This persists as `IsSpotsOverrideColorsEnabled`.
3. Click the color swatch button immediately to the right of **Enabled**. A color picker dialog opens.
4. Select the color you want for all spot text labels, then click **OK**.
5. The swatch updates to show your chosen color. All spots on the panadapter immediately render in that color. The chosen value is persisted as `SpotsOverrideColor`.

To revert to per-spot colors, click the **Override Colors:** toggle again so it reads **Disabled**.

## Tips

- The color picker only takes effect while **Override Colors:** reads **Enabled**. You can pre-select a color while the toggle is still Disabled; it will apply the next time you enable the override.
- If spot text is still hard to read after setting the color, adjust the background contrast using the **Override Background:** controls — see [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md) and [Adjust spot background opacity](adjust-spot-background-opacity.md).
- During contests, disabling **Spot Lines:** while keeping spots enabled reduces clutter without losing frequency labels.
- Kiwi DX spots complement amateur DX cluster spots. You can run both sources simultaneously by enabling **Spots:** and **Kiwi DX:** together.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
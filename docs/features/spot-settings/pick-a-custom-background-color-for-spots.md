# Pick a custom background color for spots

Set a specific background color that appears behind spot labels on the panadapter. Use this when the automatic color contrast is not suitable for your display or operating conditions.

## Before you start

- Open the Spot Settings dialog by right-clicking the spots overlay on a panadapter.
- Confirm that "Override Background: Enabled" button shows "Enabled". The background color picker has no effect when the background is disabled.
- Disable "Override Background: Auto" if you want your chosen color to take effect. When "Auto" is active, AetherSDR selects the background color automatically and ignores the manual color picker.

## Steps

1. Right-click the spots overlay on the panadapter and open Spot Settings.
2. Locate the **Override Background:** row.
3. If the "Enabled" button shows "Disabled", click it so it shows "Enabled". This persists to `IsSpotsOverrideBackgroundColorsEnabled`.
4. If the "Auto" button shows "Enabled", click it so it shows "Disabled". This persists to `IsSpotsOverrideToAutoBackgroundColorEnabled`. While "Auto" is active, the manual color picker is overridden.
5. Click the small color swatch button to the right of "Auto". This opens the system color dialog titled "Spot Background Color".
6. Select your desired color and confirm the selection.
7. The swatch updates immediately and the panadapter background behind spot labels changes to the chosen color. The value is persisted to `SpotsOverrideBgColor`.

## What each control does

| Label                        | Kind                                                                                                    | Default                        |
|------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------|
| Spots:                       | Toggle button                                                                                           | Enabled                        |
| Memories:                    | Toggle button                                                                                           | Disabled                       |
| Kiwi DX:                     | Toggle button                                                                                           | Disabled                       |
| Levels:                      | Slider (1–10)                                                                                           | 3                              |
| Position:                    | Slider (0–100)                                                                                          | 50                             |
| Font Size:                   | Slider (8–32)                                                                                           | 16                             |
| Spot Lifetime:               | Slider (non-linear steps, 10 sec – 24 hrs)                                                              | (varies)                       |
| Override Colors:             | Toggle button                                                                                           | Disabled                       |
| Spot text color picker       | Push button (swatch)                                                                                    | `#FFFF00`                      |
| Override Background: Enabled | Toggle button                                                                                           | Enabled                        |
| Override Background: Auto    | Toggle button                                                                                           | Enabled                        |
| Spot background color picker | Push button (swatch)                                                                                    | `#000000`                      |
| Background Opacity:          | Slider (0–100)                                                                                          | 48                             |
| Spot Lines:                  | Toggle button                                                                                           | Enabled                        |
| Clear All Spots              | Push button                                                                                             | —                              |

## Indicators

| Label | Meaning |
|---|---|
| Total Spots: | Shows count of live spots currently tracked. |

## Tips

- **Kiwi DX:** defaults to "Disabled". Enable it to overlay KiwiSDR Community DX database spots (beacons, utilities, time signals) on the band plan strip. The setting persists to `ShowKiwiDxSpots`. This control was added in v26.8.4.
- Setting opacity to 0 makes the background fully transparent regardless of the color chosen. If the background disappears after picking a color, check the "Background Opacity:" slider.
- "Override Background: Auto" defaults to "Enabled", so a freshly opened dialog will ignore any manual color until you disable "Auto".
- "Spot Lines:" defaults to "Enabled". If vertical lines from the spectrum baseline to spot labels are adding clutter during a contest, click the toggle so it shows "Disabled". This persists to `IsSpotsLinesEnabled`.

## Troubleshooting

- **Color picker has no visible effect on the panadapter** — Confirm "Override Background: Enabled" shows "Enabled" and "Override Background: Auto" shows "Disabled". Both conditions must be met for a manual background color to display.
- **Background is invisible despite correct toggle states** — Check the "Background Opacity:" slider. If it is at 0, the background is fully transparent. See [Adjust spot background opacity](adjust-spot-background-opacity.md).
- **Kiwi DX spots do not appear** — Confirm "Kiwi DX:" shows "Enabled". The toggle persists to `ShowKiwiDxSpots`. This control was added in v26.8.4; if you are running an earlier version, the setting is not available.
- **Spot lines are not visible** — Confirm "Spot Lines:" shows "Enabled". The toggle persists to `IsSpotsLinesEnabled`. This control was added in v0.9.7; if you are running an earlier version, the setting is not available.

## Related

- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Force a single spot text color](force-a-single-spot-text-color.md)
- [Turn spots on or off](turn-spots-on-or-off.md)
- [Spot Settings overview](overview.md)
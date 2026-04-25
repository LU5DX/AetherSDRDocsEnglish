# Force a single spot text color

By default, AetherSDR colors each DX spot according to its source or mode. This page explains how to override that behavior and display all spot text in one color of your choosing.

## Before you start

- The Spot Settings dialog must be open. Right-click the spots overlay on the panadapter to open it.
- Spots must be active. If the `IsSpotsEnabled` toggle reads "Disabled", enable it first (see [Turn spots on or off](turn-spots-on-or-off.md)).

## Steps

1. Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter.
2. Locate the **Override Colors:** row.
3. Click the toggle button so it reads **Enabled**. This activates the single-color override and persists `IsSpotsOverrideColorsEnabled`.
4. Click the small color swatch button immediately to the right of the **Enabled** toggle. A color picker dialog opens titled "Spot Text Color".
5. Select your desired color and confirm. The swatch updates to reflect your choice, and the color is saved to `SpotsOverrideColor`.

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **Override Colors:** toggle | Disabled | When Enabled, all spot text is rendered in a single color instead of per-source colors. | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker (swatch button) | `#FFFF00` | Opens the color picker dialog. The selected color is applied to all spot text when Override Colors is Enabled. | `SpotsOverrideColor` |

## Tips

- The color swatch reflects the currently saved color even when **Override Colors:** is Disabled. You can pre-select a color before enabling the override.
- The default text color is `#FFFF00` (yellow). If you want to return to the default, open the color picker and enter that value manually.

## Troubleshooting

- **Spots still show multiple colors after enabling Override Colors** — Confirm the toggle reads **Enabled** (not **Disabled**). If it reads Disabled, click it once to toggle it on.
- **Color picker closes but swatch does not change** — You likely dismissed the dialog without confirming a color. Open the picker again and select a color, then click OK.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)

# Force a single spot text color

By default, AetherSDR renders each DX spot in a color determined by its source or mode. Enabling color override forces every spot label to display in one color you choose, making the panadapter easier to read at a glance.

## Before you start

- Spots must be enabled. If the `IsSpotsEnabled` toggle shows "Disabled", enable it first — see [Turn spots on or off](turn-spots-on-or-off.md).
- Open the Spot Settings dialog by right-clicking the spots overlay on the panadapter and selecting the spot settings option from the context menu.

## Steps

1. In the Spot Settings dialog, locate the **Override Colors:** row.
2. Click the toggle button so it reads "Enabled". The setting `IsSpotsOverrideColorsEnabled` is saved immediately.
3. Click the small color swatch button to the right of the toggle. A color picker dialog opens titled "Spot Text Color".
4. Select your desired color and confirm. The swatch updates to reflect your choice and the color is saved to `SpotsOverrideColor`.

To revert to per-spot colors, click the **Override Colors:** toggle again so it reads "Disabled".

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **Override Colors:** toggle | Disabled | When "Enabled", replaces all spot text colors with the single color set by the color picker. When "Disabled", each spot uses its own source-assigned color. | `IsSpotsOverrideColorsEnabled` |
| Spot text color picker (swatch button) | `#FFFF00` (yellow) | Opens the "Spot Text Color" picker. The chosen color applies to all spot labels when **Override Colors:** is "Enabled". | `SpotsOverrideColor` |

## Tips

- The color picker only takes effect when **Override Colors:** is "Enabled". You can pre-select a color while the toggle is "Disabled" and enable it later.
- Yellow (`#FFFF00`) is the default override color. It contrasts well against the default dark panadapter background at the default background opacity of 48.

## Troubleshooting

- **Spots still appear in multiple colors after enabling Override Colors:** — Confirm the toggle reads "Enabled" (green state), not "Disabled". Clicking the toggle cycles its state and saves immediately; no Apply button is required.
- **Color picker closes but the swatch does not update** — The picker was dismissed with Cancel or the window was closed without selecting a color. Click the swatch button again and confirm a color selection.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Pick a custom background color for spots](pick-a-custom-background-color-for-spots.md)
- [Adjust spot background opacity](adjust-spot-background-opacity.md)
- [Enlarge or shrink the spot font](enlarge-or-shrink-the-spot-font.md)

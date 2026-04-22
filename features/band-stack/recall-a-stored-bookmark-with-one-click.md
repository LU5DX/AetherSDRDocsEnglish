# Recall a stored bookmark with one click

The Band Stack panel shows your saved frequency bookmarks beside each panadapter. Clicking a bookmark instantly tunes the panadapter to that frequency, restoring the stored mode, filter, antenna, and other slice settings.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Band Stack panel is only visible when a radio is connected.
- At least one bookmark must already exist. If the panel is empty, save a bookmark first using the `+` button.

## Steps

1. Locate the Band Stack panel — the narrow vertical strip of colored buttons immediately alongside the panadapter.
2. Find the bookmark button showing the frequency you want. Each button displays the frequency in MHz (for example, `14.225`). Hover over a button to see a tooltip showing the full frequency, mode, and antenna.
3. Click the bookmark button. The panadapter tunes to the stored frequency and the associated slice settings are restored.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| Bookmark buttons | Click to recall the stored frequency, mode, filter, antenna, AGC, audio, and noise-reduction settings. Color reflects the band-plan segment for that frequency. Right-click to delete. | `BandStack_<serial>` |
| `+` | Adds a new bookmark at the active slice's current frequency. | `BandStack_<serial>` |

## Tips

- Button color indicates the band-plan segment for the stored frequency. Use color to visually group bookmarks before clicking.
- If you have more bookmarks than fit in the visible panel, scroll the panel vertically to reveal additional buttons.

## Troubleshooting

- **The Band Stack panel is not visible** — The panel only appears when a radio is connected. Check your connection via `Settings > Connect to Radio...`.
- **No bookmark buttons appear** — No bookmarks have been saved for this radio yet. Use `+` to add the first one.

## Related

- [Band Stack overview](overview.md)
- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

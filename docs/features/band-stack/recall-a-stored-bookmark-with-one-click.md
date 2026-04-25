# Recall a stored bookmark with one click

The Band Stack panel lets you jump the panadapter directly to any saved frequency by clicking its bookmark button. Use this when you want to return to a frequency you bookmarked earlier without retyping it.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Band Stack panel is only visible when a radio is connected.
- At least one bookmark must already exist in the panel. If the panel is empty, add a bookmark first.

## Steps

1. Locate the Band Stack panel — the narrow vertical strip alongside the panadapter in the main window.
2. Find the bookmark button showing the frequency you want. Each button displays the frequency in MHz (for example, `14.225`). Hover over a button to see a tooltip with the full frequency, mode, and antenna.
3. Click the bookmark button. The panadapter tunes to the stored frequency immediately.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| Bookmark buttons | Click to tune the panadapter to the stored frequency. Color reflects the band-plan segment for that frequency. | `BandStack_<serial>` |
| `+` | Adds a new bookmark at the active slice's current frequency. | `BandStack_<serial>` |
| × | Clears all bookmarks. | `BandStack_<serial>` |
| ⚙ | Opens band stack options: Group by band, Auto-expiry (Off, 5 min, 15 min, 30 min, 60 min), Auto-save dwell (Off, 10 sec, 30 sec, 60 sec). | `BandStack_<serial>` |

## Tips

- If you have many bookmarks, enable **Group by band** via the ⚙ menu. Bookmarks are then sorted under band headers, making a specific frequency easier to find by sight.
- Each bookmark button's color comes from the band plan segment for that frequency, so you can identify the band at a glance without reading the label.

## Troubleshooting

- **The Band Stack panel is not visible** — the panel appears only when a radio is connected. Check your connection via `Settings > Connect to Radio...`.
- **No bookmark buttons appear** — no bookmarks have been saved for this radio yet. Click `+` to save the current frequency, or see [Bookmark the current frequency](bookmark-the-current-frequency.md).

## Related

- [Band Stack overview](overview.md)
- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

# Bookmark the current frequency

Save the active slice's frequency to the Band Stack so you can return to it later with a single click.

## Before you start

- AetherSDR must be connected to a radio. The Band Stack panel is only visible when a radio connection is active.
- Tune the active slice to the frequency you want to bookmark.

## Steps

1. Locate the Band Stack panel — the narrow vertical strip alongside the panadapter.
2. Click `+` at the bottom of the Band Stack panel.

A new bookmark button appears in the list, labeled with the frequency in MHz and colored to match the band-plan segment for that frequency. The bookmark is saved immediately to `BandStack_<serial>`, where `<serial>` is your radio's serial number.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| `+` | Adds a bookmark at the active slice's current frequency. | Saved to `BandStack_<serial>`. |
| Bookmark buttons | Click to recall the stored frequency; right-click to delete. | Color reflects the band-plan segment for that frequency. Tooltip shows full frequency in MHz, mode, and RX antenna. |
| ⚙ | Opens band stack options. | Options include "Group by band" and auto-expiry intervals: Off, 5 min, 15 min, 30 min, 60 min. |
| × | Clears all bookmarks. | Tooltip reads "Clear all bookmarks". |

## Tips

- If "Group by band" is enabled (via the ⚙ menu), the new bookmark appears under its band heading rather than at the bottom of a flat list.
- The bookmark button tooltip shows the full six-decimal frequency, mode, and RX antenna — hover over a button to confirm what was captured.

## Troubleshooting

- **The `+` button is not visible** — The Band Stack panel only appears when a radio is connected. Verify the connection via `Settings > Connect to Radio...`.
- **The bookmark appears in an unexpected position** — "Group by band" is on. The ⚙ menu shows whether grouping is active; uncheck it to restore insertion-order display.

## Related

- [Band Stack overview](overview.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

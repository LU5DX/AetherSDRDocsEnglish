# Recall a stored bookmark with one click

The Band Stack panel lets you jump the panadapter to any saved frequency in a single click. Use this when you want to return quickly to a frequency you have already bookmarked without retyping it.

## Before you start

- AetherSDR must be connected to a radio. The Band Stack panel is only visible when a radio is connected.
- At least one bookmark must already be saved. If the panel is empty, see [Bookmark the current frequency](bookmark-the-current-frequency.md) first.

## Steps

1. Locate the Band Stack panel — the narrow vertical strip of colored buttons sitting alongside the panadapter in the main window.
2. Find the bookmark button showing the frequency you want. Each button displays the frequency in MHz (three decimal places). Hover over a button to see a tooltip with the full frequency, mode, and antenna.
3. Click the bookmark button. The panadapter tunes immediately to the stored frequency.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Bookmark buttons | Click to tune the panadapter to the stored frequency. Right-click to open a context menu with a **Remove** option. | Button color reflects the band-plan segment for that frequency. |
| `+` | Adds a new bookmark at the active slice's current frequency. | — |
| ⚙ (gear) | Opens the Band Stack options menu. Contains **Group by band** toggle and **Auto-expiry** settings (Off, 5 min, 15 min, 30 min, 60 min). | — |
| × | Removes all bookmarks at once. Tooltip reads "Clear all bookmarks". | — |

Bookmarks are persisted in `BandStack_<serial>`, where `<serial>` is your radio's serial number.

## Tips

- If you have many bookmarks, scroll the panel vertically to find the one you want. The panel has a scrollable area; horizontal scrolling is disabled.
- Enable **Group by band** from the ⚙ menu to sort bookmarks by band rather than insertion order. This makes it easier to find a frequency when you have bookmarks across multiple bands.

## Troubleshooting

- **The Band Stack panel is not visible** — The panel only appears when a radio is connected. Check your connection via `Settings > Connect to Radio...`.
- **Clicking a bookmark button does nothing** — Ensure the radio is still connected. If the connection dropped, reconnect and try again.

## Related

- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)
- [Band Stack overview](overview.md)

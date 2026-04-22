# Bookmark the current frequency

Save the active slice's frequency, mode, and filter settings as a bookmark in the Band Stack panel so you can return to it with a single click later.

## Before you start

- AetherSDR must be connected to a radio. The Band Stack panel is only visible when a radio is connected.
- Tune the active slice to the frequency you want to bookmark.

## Steps

1. Locate the Band Stack panel — the narrow vertical strip of colored buttons to the side of the panadapter.
2. Click `+` at the bottom of the Band Stack panel.

A new bookmark button appears in the panel showing the frequency in MHz. Its color reflects the band-plan segment for that frequency.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| `+` | Adds a bookmark at the active slice's current frequency. | `BandStack_<serial>` |
| Bookmark buttons | Click to recall the stored frequency. Right-click to delete. Color reflects the band-plan segment for that frequency. | `BandStack_<serial>` |

## Tips

- Bookmarks are saved per radio serial number. If you connect a different radio, its bookmark list is separate.
- Hovering over a bookmark button shows the full frequency in MHz, the mode, and the RX antenna stored with it.
- If you have many bookmarks, the panel scrolls vertically. The `+` button stays fixed at the bottom.

## Troubleshooting

- **The `+` button is not visible** — The Band Stack panel only appears when a radio is connected. Check your connection via `Settings > Connect to Radio...`.
- **The new bookmark appears with a grey color** — Grey indicates the frequency does not match any segment in the active band plan. Check your band plan region under `View > Band Plan`.

## Related

- [Band Stack overview](overview.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

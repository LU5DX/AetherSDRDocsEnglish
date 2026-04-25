# Bookmark the current frequency

Save the active slice's frequency to the Band Stack panel so you can return to it with a single click.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Band Stack panel is only visible when a radio is connected.
- Tune the active slice to the frequency you want to save.

## Steps

1. Locate the Band Stack panel — the narrow vertical strip of colored buttons that sits alongside the panadapter.
2. Click `+` at the bottom of the Band Stack panel.

The new bookmark appears immediately as a color-coded button showing the frequency in MHz. The button color reflects the band-plan segment for that frequency. Bookmarks are saved automatically to `BandStack_<serial>`, where `<serial>` is your radio's serial number.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| `+` | Adds a bookmark at the active slice's current frequency. | One click; no confirmation dialog. |
| Bookmark buttons | Click to recall the stored frequency; right-click to delete. | Color matches the band-plan segment. |
| ⚙ (gear button) | Opens Band Stack options menu. | See options below. |
| × button | Clears all bookmarks. | Tooltip: "Clear all bookmarks". |

### Gear menu options

| Option | Values | Behavior |
|---|---|---|
| Group by band | On / Off | Arranges bookmarks under band headers instead of insertion order. |
| Auto-expiry | Off, 5 min, 15 min, 30 min, 60 min | Automatically removes bookmarks older than the selected age. |
| Auto-save dwell | Off, 10 sec, 30 sec, 60 sec | Automatically bookmarks a frequency after the slice dwells on it for the chosen duration. |

## Tips

- Pair **Auto-save dwell** with **Auto-expiry** to maintain a self-pruning rolling history of recently visited frequencies without any manual bookmarking.
- Hover over a bookmark button to see the full frequency in MHz, the mode, and the RX antenna stored with it.

## Related

- [Band Stack overview](overview.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

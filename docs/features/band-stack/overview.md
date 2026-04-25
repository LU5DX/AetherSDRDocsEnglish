# Band Stack overview

The Band Stack is a vertical strip of frequency bookmarks that sits alongside each panadapter. Use it to save frequencies you want to return to, recall them with a single click, and visually survey what you have stored across the bands.

## How it works

The Band Stack panel appears automatically beside each panadapter whenever a radio is connected — there is nothing to open or enable. Each radio's bookmarks are stored independently under the `BandStack_<serial>` setting key, where `<serial>` is the serial number of the connected FLEX-8600.

Bookmarks are displayed as buttons showing the stored frequency in MHz. Each button's color reflects the band-plan segment that frequency falls in, making it easy to distinguish HF bands at a glance. You can scroll the list if you have more bookmarks than fit in the panel height.

When "Group by band" is enabled, bookmarks are sorted under labeled band headers (for example, 40m or 20m) rather than shown in the order you added them. Right-clicking a band header when grouped gives you the option to clear all bookmarks in that band at once.

## What each control does

| Control | Description | Notes |
|---|---|---|
| Bookmark buttons | Click to tune the panadapter to the stored frequency. Right-click and choose "Remove" to delete a single bookmark. | Color matches the band-plan segment for that frequency. Tooltip shows full frequency in MHz, mode, and RX antenna. |
| + | Adds a new bookmark at the active slice's current frequency. | — |
| × | Clears all bookmarks. | Tooltip reads "Clear all bookmarks". |
| ⚙ (gear) | Opens the band stack options menu. | See options below. |

### Gear menu options

| Option | Description | Valid values |
|---|---|---|
| Group by band | When checked, bookmarks are sorted under band headers. When unchecked, bookmarks appear in insertion order. | On / Off |
| Auto-expiry | Automatically removes bookmarks older than the chosen age. | Off, 5 min, 15 min, 30 min, 60 min |
| Auto-save dwell | Automatically saves a bookmark after the active slice has rested on a frequency for the chosen duration. | Off, 10 sec, 30 sec, 60 sec |

## Tips

- Pair Auto-save dwell with Auto-expiry to maintain a self-pruning rolling history of frequencies you have visited, without manual bookmarking.
- When "Group by band" is on, right-click a band header to clear all bookmarks for that band without affecting the others.

## Related

- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

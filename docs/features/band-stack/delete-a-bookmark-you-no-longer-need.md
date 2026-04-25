# Delete a bookmark you no longer need

Remove a frequency bookmark from the Band Stack when it is no longer useful. Deleted bookmarks are removed from the persisted `BandStack_<serial>` settings for the connected radio.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Band Stack panel is only visible when a radio is connected.
- Locate the Band Stack panel, the narrow vertical strip of colored frequency buttons that sits alongside the panadapter.

## Steps

1. Find the bookmark button you want to delete in the Band Stack panel.
2. Right-click the bookmark button.
3. Click **Remove** in the context menu that appears.

The bookmark disappears immediately from the panel and is removed from the stored settings.

## What each control does

| Control | Behavior |
|---|---|
| Bookmark buttons | Left-click recalls the stored frequency. Right-click opens a context menu with the **Remove** option. |
| **+** | Adds a new bookmark at the active slice's current frequency. |
| **×** | Clears all bookmarks for the connected radio. |

The bookmark list is persisted under `BandStack_<serial>`, where `<serial>` is the serial number of the connected FLEX-8600.

## Tips

- If you want to remove every bookmark at once, click **×** at the bottom of the Band Stack panel instead of deleting entries one at a time.
- If "Group by band" is enabled (via the ⚙ menu), bookmarks are sorted by band rather than insertion order. Right-click still works the same way regardless of the current grouping.
- To avoid accumulating bookmarks you rarely revisit, consider enabling **Auto-expiry** in the ⚙ menu. Options are Off, 5 min, 15 min, 30 min, and 60 min.

## Related

- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

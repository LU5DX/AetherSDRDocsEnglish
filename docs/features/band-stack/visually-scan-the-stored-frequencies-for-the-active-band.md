# Visually scan the stored frequencies for the active band

The Band Stack panel shows all your bookmarked frequencies as a vertical strip of color-coded buttons beside the panadapter. Glancing at it lets you see at a glance which frequencies you have stored, what band segments they fall in, and how many bookmarks exist — without tuning to any of them.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Band Stack panel is only visible when a radio is connected.
- At least one bookmark must already be saved. If the panel is empty, see [Bookmark the current frequency](bookmark-the-current-frequency.md).

## Steps

1. Look at the narrow vertical strip immediately beside the panadapter. This is the Band Stack panel.
2. Read the frequency labels on the bookmark buttons. Each button displays the stored frequency in MHz to three decimal places (for example, `14.225`).
3. Hover over any bookmark button to see its full detail: frequency to six decimal places, mode, and RX antenna, shown in a tooltip.
4. To group bookmarks by band for easier scanning, click the ⚙ button at the bottom of the panel, then click **Group by band**. The panel redraws with band-name headers separating each group. Bookmarks that do not fall within a defined band appear under an **Other** header.
5. To return to insertion-order display, click ⚙ again and click **Group by band** to uncheck it.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Bookmark buttons | Display a stored frequency; click to recall, right-click to open a menu with **Remove**. | Button color reflects the band-plan segment for that frequency. Tooltip shows full frequency, mode, and RX antenna. |
| + | Adds a new bookmark at the active slice's current frequency. | — |
| × | Requests deletion of all bookmarks. | Tooltip reads "Clear all bookmarks". |
| ⚙ | Opens the band stack options menu. | See options below. |
| **Group by band** (⚙ menu) | Toggles grouped vs. insertion-order display. When checked, band-name headers appear and bookmarks are sorted by band. | Default: unchecked. |
| **Auto-expiry** (⚙ menu) | Automatically removes bookmarks older than the chosen age: Off, 5 min, 15 min, 30 min, or 60 min. | Default: Off. |
| **Auto-save dwell** (⚙ menu) | Automatically saves a bookmark after the VFO dwells on a frequency for the chosen time: Off, 10 sec, 30 sec, or 60 sec. | Default: Off. Pair with Auto-expiry for a self-pruning rolling history. |

Bookmark data is persisted in `BandStack_<serial>`, where `<serial>` is your radio's serial number.

## Tips

- Button colors come from the active band plan. Buttons for frequencies in different segments (CW, phone, digital) appear in different colors, making segment distribution visible at a glance without reading each label.
- When **Group by band** is on, you can right-click a band-name header to clear all bookmarks in that band only, using the **Clear \<band name\>** menu item.
- If the bookmark list is long, the panel scrolls vertically. The scrollbar appears on the right edge of the panel; the + , ×, and ⚙ buttons remain pinned at the bottom.

## Related

- [Band Stack overview](overview.md)
- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)

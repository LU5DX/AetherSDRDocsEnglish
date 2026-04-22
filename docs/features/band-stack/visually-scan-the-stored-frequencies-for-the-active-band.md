# Visually scan the stored frequencies for the active band

The Band Stack panel shows all your bookmarked frequencies as a vertical strip of color-coded buttons alongside the panadapter. Glancing at the panel lets you see at a glance which frequencies you have stored and which band-plan segment each one falls in, without tuning to any of them.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The Band Stack panel is only visible when a radio is connected.
- At least one bookmark must already be stored for the active radio. If the panel is empty, see [Bookmark the current frequency](bookmark-the-current-frequency.md).

## Steps

1. Look at the narrow vertical strip (80 px wide) that sits alongside the panadapter in the main window. This is the Band Stack panel.
2. Read the frequency labels on the bookmark buttons. Each button displays the stored frequency in MHz to three decimal places (for example, `14.225`).
3. Hover over any bookmark button to see a tooltip showing the full frequency to six decimal places, the stored mode, and the RX antenna.
4. Note the background color of each button. The color reflects the band-plan segment that contains that frequency. Buttons for frequencies outside any defined band-plan segment appear in dark grey.
5. If there are more bookmarks than fit in the visible area, scroll the panel vertically to reveal additional buttons. The panel scrolls; no horizontal scrolling is available.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| Bookmark buttons | Each button shows a stored frequency. Color reflects the band-plan segment for that frequency. Click to recall; right-click to delete. | `BandStack_<serial>` |
| + | Adds a new bookmark at the active slice's current frequency. | `BandStack_<serial>` |

## Tips

- Tooltip text includes the mode and RX antenna stored with each bookmark, so you can distinguish two bookmarks at the same frequency saved with different modes or antennas without recalling either one.
- Bookmark data is stored per radio serial number. If you connect a different radio, its own separate list of bookmarks appears.

## Related

- [Band Stack overview](overview.md)
- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)

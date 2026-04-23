# Visually scan the stored frequencies for the active band

The Band Stack panel shows all your saved frequency bookmarks as a vertical strip beside the panadapter. This page explains how to read the panel at a glance — understanding the color coding, layout order, and grouping options — so you can find a stored frequency quickly without scrolling through a long list.

## Before you start

- AetherSDR must be connected to your Flex radio. The Band Stack panel is only visible when a radio connection is active.
- You need at least one bookmark already saved. If the panel is empty, see [Bookmark the current frequency](bookmark-the-current-frequency.md).

## Steps

1. Look at the Band Stack panel — the narrow vertical strip immediately beside the panadapter in the main window.
2. Read each bookmark button. The button label shows the frequency in MHz to three decimal places (for example, `14.225`). Hover over any button to see a tooltip with the full frequency to six decimal places, mode, and receive antenna.
3. Note the button color. Each bookmark's background color reflects the band-plan segment that contains that frequency, matching the same color scheme used on the panadapter's band plan overlay.
4. To switch the panel from insertion order to band-grouped order, click the ⚙ button at the bottom of the panel. In the menu that appears, click **Group by band**. The panel rebuilds with labeled band headers separating each group. Bookmarks that do not fall within a known band appear under an **Other** header at the bottom.
5. To return to flat insertion order, click ⚙ again and click **Group by band** to uncheck it.
6. Scroll the bookmark list up or down if there are more bookmarks than fit in the visible area. The horizontal scrollbar is hidden; only vertical scrolling is available.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Bookmark buttons | Display stored frequency in MHz (3 decimal places). Click to recall; right-click for a **Remove** option. | Color matches the band-plan segment for that frequency. |
| ⚙ (gear button) | Opens a menu with layout and expiry options. | Located in the bottom row of the panel. |
| **Group by band** (menu item) | Toggles between flat insertion order and band-grouped layout with band-name headers. | When grouped, right-clicking a band header shows a **Clear \<band\>** option. |
| **Auto-expiry** (menu items) | Sets how long bookmarks are retained before automatic removal. Options: **Off**, **5 min**, **15 min**, **30 min**, **60 min**. Default: **Off**. | Applies to all bookmarks for the connected radio. |
| × (clear all button) | Removes all bookmarks at once. | Located in the bottom row beside + and ⚙. |
| + | Saves the active slice's current frequency as a new bookmark. | Located in the bottom row. |

Bookmarks are persisted under the key `BandStack_<serial>`, where `<serial>` is your radio's serial number.

## Tips

- When **Group by band** is on, bookmarks within each band appear in the order they were saved. Scanning a single band is easier because its bookmarks are contiguous and labeled with the band name.
- If you operate on many bands, enabling **Group by band** avoids having to remember which frequency belongs to which band — the headers make it immediately visible.
- The tooltip on each bookmark includes the mode and receive antenna that were active when the bookmark was saved, giving you more context without needing to recall the frequency.

## Related

- [Band Stack overview](overview.md)
- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)

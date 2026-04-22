# Band Stack overview

The Band Stack is a vertical strip of frequency bookmarks that sits alongside each panadapter. Use it to save frequencies you return to often, then recall them with a single click.

## Before you start

- A FLEX-8600 radio must be connected. The Band Stack panel is not visible when no radio is connected.

## How it works

The Band Stack panel appears as a narrow strip to the side of each panadapter in the main window. It is always visible when a radio is connected and requires no manual setup to display.

Each bookmark button shows a frequency in MHz, rounded to three decimal places. The button's color reflects the band-plan segment that contains that frequency — for example, phone, CW, or data portions of a band are each shown in the color defined by your active band plan. Frequencies that fall outside any defined band-plan segment appear in a neutral dark grey.

Bookmarks are stored per radio, identified by serial number, using the `BandStack_<serial>` setting. The file is saved automatically whenever you add or remove a bookmark. If you connect a different radio, its own set of bookmarks loads independently.

The panel scrolls vertically if you have more bookmarks than fit in the visible area. A thin scrollbar appears on the right edge of the panel when needed.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Bookmark buttons | Click to tune the panadapter to the stored frequency. Right-click to open a context menu with a **Remove** option. | Button color reflects the band-plan segment for that frequency. Tooltip shows full frequency in MHz, mode, and RX antenna. |
| **+** | Adds a new bookmark at the active slice's current frequency. | Located at the bottom of the panel. Stores frequency, mode, filter edges, antennas, AGC settings, audio gain, and noise-reduction state. |

## Tips

- Each radio's bookmarks are stored separately. Connecting a second FLEX-8600 loads that radio's own bookmark list without affecting the first.
- Bookmark button tooltips show the full six-decimal-place frequency, the mode, and the RX antenna. Hover over a button to confirm what it will recall before clicking.
- If you reorganize your band plan regions, existing bookmark colors update to match the new plan on the next load.

## Related

- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

# Band Stack overview

The Band Stack is a vertical strip of frequency bookmarks that sits beside each panadapter. Use it to save, recall, and manage tuning positions without leaving the panadapter view.

## How it works

The Band Stack panel appears automatically alongside each panadapter when a radio is connected. It requires no separate step to open.

Each bookmark is displayed as a button labeled with the stored frequency in MHz. Button colors reflect the band-plan segment for that frequency, making it easy to see at a glance which band a bookmark belongs to. Bookmarks are saved per radio serial number under the `BandStack_<serial>` setting, so each radio you connect maintains its own independent list.

The panel is scrollable when the bookmark list grows longer than the visible area. A row of three buttons at the bottom of the panel controls the list:

| Control | What it does |
|---|---|
| Bookmark buttons | Click to recall the stored frequency on the active panadapter. Right-click to open a context menu with a "Remove" option. Tooltip shows full frequency in MHz, mode, and RX antenna. |
| `+` | Adds a new bookmark at the active slice's current frequency. |
| `×` | Clears all bookmarks in the list. |
| ⚙ (gear) | Opens the band stack options menu (see below). |

### Band stack options menu

Clicking the gear button opens a menu with two categories of settings:

**Group by band** — A checkable option. When enabled, bookmarks are sorted into band sections with a labeled header for each band (for example, "40m", "20m"). Right-clicking a band header offers an option to clear all bookmarks within that band's frequency range. When disabled, bookmarks appear in insertion order.

**Auto-expiry** — Sets how long bookmarks are retained before being removed automatically. Options are:

| Option | Retention |
|---|---|
| Off | Bookmarks are never expired automatically |
| 5 min | Removed after 5 minutes |
| 15 min | Removed after 15 minutes |
| 30 min | Removed after 30 minutes |
| 60 min | Removed after 60 minutes |

Only one auto-expiry option is active at a time.

## Related

- [Bookmark the current frequency](bookmark-the-current-frequency.md)
- [Recall a stored bookmark with one click](recall-a-stored-bookmark-with-one-click.md)
- [Delete a bookmark you no longer need](delete-a-bookmark-you-no-longer-need.md)
- [Visually scan the stored frequencies for the active band](visually-scan-the-stored-frequencies-for-the-active-band.md)

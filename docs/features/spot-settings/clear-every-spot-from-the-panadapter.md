# Clear every spot from the panadapter

Use this page to instantly remove all DX spots currently displayed on the panadapter. This is useful when the spot list has become cluttered or stale and you want a clean view without changing any other spot settings.

## Before you start

- AetherSDR must be running.
- The Spot Settings dialog must be accessible from the panadapter context menu or Spots overlay.

## Steps

1. Right-click on the panadapter (or the Spots overlay) to open the context menu.
2. Select the option that opens the **Spot Settings** dialog.
3. Click **Clear All Spots**.

All spots are immediately removed from the panadapter. No settings are changed — spots will continue to appear as new ones arrive from your configured sources.

## Tips

- **Clear All Spots** removes only the currently displayed spots. It does not affect `IsSpotsEnabled` or any other persisted setting. New spots from your DX cluster or other sources will populate the panadapter again as they arrive.
- The **Total Spots:** indicator in the Spot Settings dialog shows how many live spots are currently tracked. After clicking **Clear All Spots**, this count resets.
- To stop new spots from appearing entirely, use the **Spots:** toggle instead. See [Turn spots on or off](turn-spots-on-or-off.md).

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Change spot density and vertical position](change-spot-density-and-vertical-position.md)

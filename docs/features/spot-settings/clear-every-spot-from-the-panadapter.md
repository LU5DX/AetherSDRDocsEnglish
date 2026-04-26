# Clear every spot from the panadapter

This page explains how to remove all currently displayed DX spots from the panadapter in a single action. Use this when the spot display has become cluttered or you want a clean slate without waiting for spots to expire.

## Before you start

- AetherSDR must be running.
- The panadapter must be visible.
- Spots must have been received from a configured source; if no spots are loaded, the button has no effect.

## Steps

1. Right-click anywhere on the panadapter to open the context menu, then select the option that opens the Spot Settings dialog.
2. In the **Spot Settings** dialog, click **Clear All Spots**.

All spots are immediately removed from the panadapter. The **Total Spots:** indicator resets to zero. New spots will appear again as they arrive from your configured spot sources.

## Tips

- Clearing spots does not disable spot display. The `IsSpotsEnabled` setting is unchanged; new incoming spots will continue to appear after the clear.
- If you want to stop spots from appearing entirely rather than just clearing the current set, use the **Spots:** toggle to switch it to Disabled. See [Turn spots on or off](turn-spots-on-or-off.md).
- The **Total Spots:** indicator at the bottom of the Spot Settings dialog shows how many spots are currently tracked. Check it before and after clicking **Clear All Spots** to confirm the clear succeeded.

## Troubleshooting

- **Spots reappear immediately after clearing** — Your spot source is actively pushing new spots. This is normal behavior. To pause spot intake, disable the spot source in `Settings > SpotHub...` or toggle **Spots:** to Disabled.

## Related

- [Turn spots on or off](turn-spots-on-or-off.md)
- [Shorten or lengthen spot lifetime](shorten-or-lengthen-spot-lifetime.md)
- [Spot Settings overview](overview.md)

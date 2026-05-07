# Enable passive spots mode

When multiple AetherSDR clients share the same radio, each client sending spot-add commands can cause duplicates on the panadapter. Passive spots mode lets you receive and display spots without sending any spot commands to the radio.

## Before you start

- Open SpotHub: **Settings > SpotHub...**
- Confirm that spot display is active: the **Spots:** toggle on the **Display** tab must show **Enabled**.

## Steps

1. In SpotHub, click the **Display** tab.
2. Click the **Passive Spots:** toggle button until it shows **Enabled**.

The setting is saved automatically. AetherSDR will continue receiving and rendering spots from all configured sources but will not issue spot-add commands to the radio.

## What each control does

| Control | Behavior |
|---|---|
| **Spots:** | Master toggle for the spot overlay on the panadapter. Must be Enabled for any spots to appear. Default: Enabled. |
| **Passive Spots:** | Receive and render radio spots without sending spot-add commands to the radio. Default: Disabled. |

## Tips

- Enable passive spots mode on every secondary client that shares the radio. Leave it disabled on the single primary client that should own spot commands.
- Passive spots mode has no effect on which spot sources are active — all connected sources (DX Cluster, RBN, WSJT-X, etc.) continue feeding spots to the display.

## Related

- [Configure spot display](configure-spot-display.md)
- [Connect to a DX cluster](connect-to-dx-cluster.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->

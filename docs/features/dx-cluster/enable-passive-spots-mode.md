# Enable passive spots mode

Passive spots mode lets AetherSDR receive and render DX spots on the panadapter without sending spot-add commands to the radio — useful when multiple clients share the same radio to avoid duplicate spot commands.

## Before you start

- Confirm that spot display is active: open **Settings > SpotHub...**, go to the **Display** tab, and verify **Spots:** is set to **Enabled**.

## Steps

1. Open **Settings > SpotHub...** and select the **Display** tab.
2. Click **Passive Spots:** to toggle it from **Disabled** to **Enabled**.

## What each control does

| Control | Behavior |
|---|---|
| **Spots:** | Master toggle for the spot overlay on the panadapter. Must be Enabled for spots to appear regardless of passive mode. |
| **Passive Spots:** | When Enabled, receives and renders spots without sending spot-add commands to the radio. Default: Disabled. |

## Tips

- Enable passive spots mode on every secondary client that shares the same radio. Leave it disabled on the one client responsible for submitting spots to avoid duplication.
- Passive spots mode has no effect on which spot sources (DX Cluster, RBN, WSJT-X, etc.) are connected — those sources continue to operate normally on each client.

## Related

- [SpotHub overview](spothub-overview.md)
- [Enable spots on the panadapter](enable-spots.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->

# Enable Autostart for TCI with AetherSDR

This page explains how to configure AetherSDR to start the TCI server automatically each time the application launches, so you do not need to enable TCI manually after every restart.

## Before you start

- AetherSDR must be built with WebSocket support (`HAVE_WEBSOCKETS`). If the menu item is absent, your build does not include TCI.
- You should be familiar with how TCI client software connects to AetherSDR's TCI server.

## Steps

1. Click `Settings` in the menu bar.
2. Click `Autostart TCI with AetherSDR`.

The menu item is a checkable toggle. A check mark next to the label means autostart is enabled. Clicking it again removes the check mark and disables autostart.

## What each control does

| Control | Description | Default | Persisted key |
|---|---|---|---|
| `Autostart TCI with AetherSDR` | When checked, AetherSDR starts the TCI server immediately on launch without requiring manual activation. | Off | `AutoStartTCI` |

## Tips

- If you only run TCI clients some of the time, leave autostart off and start the TCI server manually when needed to avoid unnecessary resource use.
- The setting is saved immediately when you toggle the menu item. No restart of AetherSDR is required for future launches to respect the new value.

## Related

- [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md)
- [Enable autostart for DAX with AetherSDR](enable-autostart-for-dax-with-aethersdr.md)
- [Enable autostart for rigctld with AetherSDR](enable-autostart-for-rigctld-with-aethersdr.md)
- [Getting Started](getting-started.md)

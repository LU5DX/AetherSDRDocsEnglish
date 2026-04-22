# Enable autostart for DAX with AetherSDR

This page explains how to configure AetherSDR to start the DAX audio bridge automatically each time the application launches. Use this setting if you want DAX audio routing available immediately without enabling it manually after each start.

## Before you start

- AetherSDR must be installed and able to connect to your FLEX-8600.
- DAX audio bridge is supported on macOS and PipeWire-based Linux systems. This setting has no effect on other platforms.

## Steps

1. In the menu bar, click `Settings`.
2. Click `Autostart DAX with AetherSDR`.

The menu item is checkable. When checked, AetherSDR starts the DAX audio bridge each time the application launches. Click it again to uncheck and disable autostart.

## What each control does

| Control | Description | Default | Setting key |
|---|---|---|---|
| `Autostart DAX with AetherSDR` | Checkable menu item. When checked, the DAX audio bridge starts automatically on application launch (macOS and PipeWire only). | Unchecked | `AutoStartDAX` |

## Tips

- The `AutoStartDAX` setting is persisted between sessions. You only need to set it once.
- If you run AetherSDR on multiple platforms, note that this setting is active only on macOS and PipeWire-based Linux. On other systems the option may appear but has no effect.

## Related

- [Enable autostart for TCI with AetherSDR](enable-autostart-for-tci-with-aethersdr.md)
- [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md)
- [Enable autostart for rigctld with AetherSDR](enable-autostart-for-rigctld-with-aethersdr.md)

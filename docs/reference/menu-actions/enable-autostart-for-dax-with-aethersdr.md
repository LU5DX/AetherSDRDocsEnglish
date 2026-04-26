# Enable autostart for DAX with AetherSDR

This page explains how to configure AetherSDR to start the DAX audio bridge automatically each time the application launches. Use this if you want DAX audio routing available immediately without enabling it manually each session.

## Before you start

- AetherSDR must be installed and able to connect to a FLEX-8600 radio.
- DAX audio bridge support requires macOS or a Linux system with PipeWire.

## Steps

1. Click `Settings` in the menu bar.
2. Click `Autostart DAX with AetherSDR`.

The menu item is a checkmark toggle. When checked, AetherSDR will start the DAX audio bridge automatically on each launch. Click the item again to disable autostart.

## What each control does

| Control | Description | Persisted key |
|---|---|---|
| `Autostart DAX with AetherSDR` | Checkable menu item. When checked, AetherSDR starts the DAX audio bridge on launch. Applies on macOS and PipeWire-based Linux systems. | `AutoStartDAX` |

## Troubleshooting

- **The menu item has no effect on Windows** — DAX autostart is supported on macOS and PipeWire-based Linux only. On other platforms, configure DAX audio routing through your system audio settings.
- **DAX audio bridge does not start despite the item being checked** — Verify that PipeWire is running on your Linux system, or that your macOS audio subsystem is available at login. Uncheck and recheck `Autostart DAX with AetherSDR` to reset the setting.

## Related

- [Enable autostart for TCI with AetherSDR](enable-autostart-for-tci-with-aethersdr.md)
- [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md)
- [Enable autostart for rigctld with AetherSDR](enable-autostart-for-rigctld-with-aethersdr.md)
- [Getting Started](getting-started.md)

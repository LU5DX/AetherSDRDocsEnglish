# Enable Autostart for TCI with AetherSDR

This page explains how to configure AetherSDR to start its TCI server automatically each time the application launches. Use this if you run third-party logging or contest software that connects to AetherSDR over TCI.

## Before you start

- AetherSDR must be built with WebSockets support. If `Settings > Autostart TCI with AetherSDR` does not appear in the menu, your build does not include this feature.
- Connect to your FLEX-8600 before enabling autostart if you want to verify TCI is working after the change.

## Steps

1. Click `Settings` in the menu bar.
2. Click `Autostart TCI with AetherSDR`.

The item is a checkable menu entry. A checkmark indicates the setting is on. Clicking it toggles the checkmark and immediately persists the change to `AutoStartTCI`.

3. Restart AetherSDR to confirm the TCI server starts on launch.

## What each control does

| Control | Description | Default | Persisted key |
|---|---|---|---|
| `Autostart TCI with AetherSDR` | When checked, AetherSDR starts the TCI server each time it launches without requiring manual intervention. | Off | `AutoStartTCI` |

## Related

- [Enable autostart for CAT with AetherSDR](enable-autostart-for-cat-with-aethersdr.md)
- [Enable autostart for DAX with AetherSDR](enable-autostart-for-dax-with-aethersdr.md)
- [Enable autostart for rigctld with AetherSDR](enable-autostart-for-rigctld-with-aethersdr.md)
- [Getting Started](getting-started.md)

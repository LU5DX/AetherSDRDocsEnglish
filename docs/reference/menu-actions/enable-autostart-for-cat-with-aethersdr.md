# Enable Autostart for CAT with AetherSDR

This page explains how to enable automatic startup of virtual serial ports for CAT control when AetherSDR launches. Use this if you want CAT-capable logging or contest software to connect to AetherSDR immediately on startup without manually enabling CAT each session.

## Before you start

- CAT autostart creates virtual serial ports and is supported on Linux and macOS only. Windows users should see an alternative CAT method such as rigctld.
- Confirm that your third-party software is configured to connect to the virtual serial port that AetherSDR will create.

## Steps

1. Click `Settings` in the menu bar.
2. Click `Autostart CAT with AetherSDR`.

The menu item is checkable. A check mark next to the label means CAT autostart is enabled. Clicking it again removes the check mark and disables autostart. The setting persists across sessions under the key `AutoStartCAT`.

## What each control does

| Control | Description | Default | Persisted key |
|---|---|---|---|
| `Autostart CAT with AetherSDR` | When checked, AetherSDR creates virtual serial ports for CAT control each time it starts. Supported on Linux and macOS. | Off (unchecked) | `AutoStartCAT` |

## Troubleshooting

- **The menu item is present but CAT does not start on Windows** — Virtual serial port CAT autostart is not supported on Windows. Use `Autostart rigctld with AetherSDR` as an alternative CAT interface on that platform.
- **Third-party software reports the serial port is unavailable** — Verify the software is configured to use the correct virtual port and that no other process has the port open. Uncheck and recheck `Autostart CAT with AetherSDR` to force re-creation of the virtual ports, then restart AetherSDR.

## Related

- [Enable autostart for rigctld with AetherSDR](enable-autostart-for-rigctld-with-aethersdr.md)
- [Enable autostart for TCI with AetherSDR](enable-autostart-for-tci-with-aethersdr.md)
- [Enable autostart for DAX with AetherSDR](enable-autostart-for-dax-with-aethersdr.md)
- [USB Cables](usb-cables.md)

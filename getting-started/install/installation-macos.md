# Install AetherSDR on macOS

This page walks you through installing AetherSDR on macOS so you can connect to your FLEX-8600 radio.

## Before you start

- Your Mac must be connected to the same local network as your FLEX-8600.
- Confirm your FLEX-8600 is running firmware 4.1.5.
- You must have sufficient permissions to install applications on your Mac (administrator account or equivalent).

## Steps

1. Download the latest AetherSDR macOS disk image (`.dmg`) from the official AetherSDR distribution site.
2. Open the downloaded `.dmg` file. A Finder window appears showing the AetherSDR application bundle.
3. Drag the AetherSDR icon into your **Applications** folder.
4. Eject the disk image.
5. Open **Applications** and double-click **AetherSDR** to launch it.
6. If macOS displays a security prompt stating the app is from an unidentified developer, open **System Settings > Privacy & Security**, scroll to the blocked app notice, and click **Open Anyway**.
7. Once AetherSDR opens, go to `Settings > Connect to Radio...` to discover and connect to your FLEX-8600.

## Tips

- AetherSDR supports `Autostart DAX with AetherSDR` on macOS (requires PipeWire or compatible audio backend). Enable it via `Settings > Autostart DAX with AetherSDR` if you want the DAX audio bridge to start automatically at launch.
- Virtual serial ports for CAT control are available on macOS. Enable automatic startup via `Settings > Autostart CAT with AetherSDR` (persisted as `AutoStartCAT`).

## Related

- [Install AetherSDR on Linux](installation-linux.md)
- [Install AetherSDR on Windows](installation-windows.md)

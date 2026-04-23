# Install AetherSDR on Linux

This page walks you through installing AetherSDR on a Linux system so you can connect to your Flex radio.

## Before you start

- Confirm your Linux distribution and architecture are supported by the AetherSDR package you have obtained.
- Ensure you have sufficient privileges to install software (either `root` access or `sudo`).
- Verify your system has Qt6 runtime libraries available if you are installing from a pre-built binary rather than a distribution package.
- Have your network connection active — AetherSDR discovers radios over the local network at first launch.

## Steps

1. Download the AetherSDR package for Linux from the official distribution source.
2. Open a terminal in the directory containing the downloaded file.
3. Install the package using your distribution's package manager. For example, on a Debian or Ubuntu system:
   ```
   sudo apt install ./aethersdr_<version>_amd64.deb
   ```
   On an RPM-based system:
   ```
   sudo rpm -i aethersdr-<version>.x86_64.rpm
   ```
4. Once installation completes, launch AetherSDR from your application menu or by running:
   ```
   aethersdr
   ```
5. On first launch, go to `Settings > Connect to Radio...` to discover and connect to your Flex radio.

## Tips

- If you plan to use CAT control from third-party logging software, enable `Settings > Autostart CAT with AetherSDR` after connecting. This feature creates virtual serial ports and is available on Linux.
- If you use rigctld-compatible software, enable `Settings > Autostart rigctld with AetherSDR` to have AetherSDR spawn the rigctld CAT server automatically on each launch.
- If DAX audio bridging via PipeWire is required, enable `Settings > Autostart DAX with AetherSDR`.

## Troubleshooting

- **AetherSDR does not start after installation** — Confirm that Qt6 runtime libraries are installed on your system. Your distribution's package manager should pull these in automatically from the package dependencies; if not, install the Qt6 base libraries manually.
- **No radios found in `Settings > Connect to Radio...`** — Confirm the Flex radio is powered on and connected to the same local network segment. Check that no firewall rules are blocking UDP discovery traffic.
- **Virtual serial ports for CAT are not created** — Confirm `Settings > Autostart CAT with AetherSDR` is enabled. This feature requires the appropriate kernel modules for virtual serial ports to be loaded on your system.

## Related

- [Install AetherSDR on Windows](installation-windows.md)
- [Install AetherSDR on macOS](installation-macos.md)

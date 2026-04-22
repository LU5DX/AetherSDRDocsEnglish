# Install AetherSDR on Windows

This page walks you through downloading and installing AetherSDR on Windows so you can connect to your FLEX-8600 radio.

## Before you start

- Your Windows user account must have permission to run installers.
- Your FLEX-8600 must be on the same network as your Windows machine.
- Close any other SmartSDR-compatible clients before running AetherSDR for the first time.

## Steps

1. Download the latest AetherSDR Windows installer from the official AetherSDR distribution site.
2. Double-click the downloaded installer file to launch it.
3. Follow the on-screen prompts, accepting the default installation directory unless you have a reason to change it.
4. When the installer finishes, click Finish to close it.
5. Launch AetherSDR from the Start menu or the desktop shortcut created by the installer.
6. When AetherSDR opens, go to `Settings > Connect to Radio...` to discover and connect to your FLEX-8600.

## Troubleshooting

- **AetherSDR does not start after installation** — Verify that your system meets the minimum Qt6 runtime requirements. If a missing DLL error appears, re-run the installer and choose the option to install runtime dependencies, or install the Visual C++ Redistributable for the version bundled with AetherSDR.
- **Radio not found in Connect to Radio...** — Confirm the FLEX-8600 and the Windows machine are on the same subnet and that Windows Firewall is not blocking AetherSDR's network access. Add a firewall exception for AetherSDR if needed.

## Related

- [Install AetherSDR on Linux](installation-linux.md)
- [Install AetherSDR on macOS](installation-macos.md)

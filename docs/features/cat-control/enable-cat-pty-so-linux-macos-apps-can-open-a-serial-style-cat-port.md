# Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port

CAT PTY creates four virtual serial port symlinks that logging and contest software can open as if they were physical serial devices. Use this feature on Linux or macOS when your external application expects a serial port path rather than a TCP connection.

## Before you start

- AetherSDR must be connected to the radio. The CAT Control applet requires an active radio connection.
- The PTY feature is available on Linux and macOS only.
- Open the CAT Control applet by clicking the **CAT** tray button on the right sidebar. The applet is hidden by default.

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet.
2. Click **Enable TTY**.

   The button turns green when active. AetherSDR creates four symlinks:

   ```
   /tmp/AetherSDR-CAT-A
   /tmp/AetherSDR-CAT-B
   /tmp/AetherSDR-CAT-C
   /tmp/AetherSDR-CAT-D
   ```

3. In your external application, set the serial port path to the symlink for the channel you want to control — for example, `/tmp/AetherSDR-CAT-A` for channel A.
4. Each channel row in the applet updates to show the active PTY path once the symlink is running.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Enable TTY** | Off | On / Off | — | Starts or stops all four PTY symlinks under `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. |
| **Enable TCP** | Off | On / Off | — | Starts or stops all four rigctld TCP servers. Toggling also persists the base port to `CatTcpPort`. |
| **Base** | `4532` | 1024–65535 | `CatTcpPort` | Base TCP port for the TCP servers. Values outside the valid range snap back to `4532`. Does not affect PTY paths. |
| A/B/C/D channel rows | `(stopped)` | — | — | Each row shows a colour-coded channel badge, the TCP server status, and the PTY symlink path for that channel. |

## Tips

- Each channel (A, B, C, D) maps to one radio slice. Point your logging software at the symlink that corresponds to the slice you want it to control.
- To have AetherSDR start the PTY symlinks automatically at launch, enable `Settings > Autostart CAT with AetherSDR`.
- You can run **Enable TTY** and **Enable TCP** independently. Enabling one does not require enabling the other.

## Troubleshooting

- **Enable TTY has no effect or symlinks do not appear** — PTY support requires Linux or macOS. The feature is not available on Windows.
- **External application cannot open the port** — Confirm the application is using the full path, for example `/tmp/AetherSDR-CAT-A`. Check that **Enable TTY** is still active (button should be green) and that AetherSDR remains connected to the radio.
- **Symlink path shown in the row does not match `/tmp/AetherSDR-CAT-A`** — The path shown updates to the actual PTY device path once the symlink is running. Use whatever path is displayed in the channel row, not the placeholder.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [CAT Control overview](overview.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

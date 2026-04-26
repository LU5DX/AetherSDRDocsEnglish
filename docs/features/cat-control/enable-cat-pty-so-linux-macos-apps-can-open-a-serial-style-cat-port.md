# Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port

The CAT PTY feature creates four virtual serial port symlinks under `/tmp/` that logging and contest software on Linux and macOS can open as if they were physical serial ports. Use this when your application expects a serial device path rather than a TCP connection.

## Before you start

- AetherSDR must be connected to the radio. The CAT Control applet requires an active radio connection.
- PTY symlinks are only created on Linux and macOS. This feature is not available on Windows.
- The CAT tray button must be visible in the right sidebar. If it is not visible, see [CAT Control overview](overview.md).

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet.
2. Click **Enable TTY** to start the PTY servers.
3. Check the per-channel rows. When each PTY is running, the path column updates from `/tmp/AetherSDR-CAT-A` (or B, C, D) to the active symlink path assigned by the system.
4. In your logging or contest application, set the serial port to the path shown in the relevant channel row — for example `/tmp/AetherSDR-CAT-A` for channel A.

## What each control does

| Control | Kind | Default | Range | Persisted key | Behavior |
|---|---|---|---|---|---|
| **Enable TTY** | Toggle button | Off | On / Off | — | Starts or stops all four PTY symlinks under `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. |
| **Base** | Text field | `4532` | 1024–65535 | `CatTcpPort` | Base TCP port used by the TCP servers. Does not affect PTY paths. Out-of-range values snap back to `4532`. |
| A / B / C / D rows | Indicator | `(stopped)` | — | — | Each row shows a colour-coded channel badge, the TCP server status, and the current PTY symlink path. |

## Tips

- Each of the four channels (A–D) maps to one radio slice. Open the path for the channel that corresponds to the slice you want to control.
- You can run **Enable TTY** and **Enable TCP** at the same time. They operate independently.
- To start the PTY servers automatically every time AetherSDR launches, use `Settings > Autostart CAT with AetherSDR`.

## Troubleshooting

- **The PTY path does not appear or stays grey after clicking Enable TTY** — confirm the radio is connected. The CAT Control applet requires an active radio connection before PTY servers can start.
- **The symlink path shown is not `/tmp/AetherSDR-CAT-A`** — the system may have assigned a different slave device path. Use the exact path shown in the channel row, not a hardcoded value.
- **Enable TTY has no effect on Windows** — PTY symlinks are a Linux/macOS feature. Use **Enable TCP** and a TCP-to-serial bridge utility instead.

## Related

- [CAT Control overview](overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Change the base TCP port](change-the-base-tcp-port.md)

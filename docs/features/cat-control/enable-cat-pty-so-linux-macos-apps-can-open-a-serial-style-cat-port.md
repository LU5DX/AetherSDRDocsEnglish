# Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port

The CAT PTY feature creates virtual serial port symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`, one per channel. Use this when your logging or digital-mode software expects to open a serial device rather than a TCP socket for CAT control.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The CAT Control applet requires an active radio connection.
- PTY symlinks are only created on Linux and macOS. This feature is not available on Windows.
- The CAT Control applet is hidden by default. You must reveal it before you can use it.

## Steps

1. Click the **CAT** tray button on the right sidebar to show the CAT Control applet.
2. Click **Enable TTY**.

The button highlights green when active. Each channel row immediately shows its symlink path. The path for each channel updates from the static placeholder to the live path once the PTY is running.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable TTY** | Starts or stops PTY symlinks for all four channels (A–D). | Off | — | — |
| **Enable TCP** | Starts or stops the rigctld TCP servers. Independent of PTY. | Off | — | — |
| **Base** | Base TCP port for the rigctld servers. Channels bind to Base, Base+1, Base+2, Base+3. Does not affect PTY paths. | `4532` | 1024–65535 | `CatTcpPort` |
| A/B/C/D rows | Show each channel's badge, TCP server status, and current PTY symlink path. Read-only indicators. | `(stopped)` | — | — |

The PTY symlink paths are fixed as `/tmp/AetherSDR-CAT-A`, `/tmp/AetherSDR-CAT-B`, `/tmp/AetherSDR-CAT-C`, and `/tmp/AetherSDR-CAT-D`. Each maps to the corresponding slice (channel A = slice 0, B = slice 1, and so on).

## Tips

- Open your external application to the symlink path shown in the channel row, for example `/tmp/AetherSDR-CAT-A`. Treat it exactly as you would a hardware serial port.
- PTY and TCP can run simultaneously. If your software supports both, you can enable **Enable TTY** and **Enable TCP** at the same time without conflict.
- To start PTY symlinks automatically every time AetherSDR launches, use `Settings > Autostart CAT with AetherSDR`.

## Troubleshooting

- **The Enable TTY button is present but symlinks never appear** — Confirm you are running Linux or macOS. PTY creation is not supported on Windows.
- **External software cannot open the symlink** — Check that AetherSDR is connected to the radio. The CAT Control applet requires an active radio connection; PTYs may not function while the radio is disconnected.
- **The channel row still shows the placeholder path after clicking Enable TTY** — The PTY may have failed to start. Try clicking **Enable TTY** again to toggle it off and back on.

## Related

- [CAT Control overview](overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Change the base TCP port](change-the-base-tcp-port.md)

# Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port

The CAT PTY feature creates four virtual serial port symlinks under `/tmp/` that logging and contest software can open as if they were physical serial devices. Use this when your software expects a serial port path rather than a TCP connection.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The CAT Control applet requires an active radio connection.
- PTY symlinks are available on Linux and macOS only. This feature is not available on Windows.
- The CAT Control applet is hidden by default. You must make it visible before you can use it.

## Steps

1. Click the **CAT** tray button on the right sidebar to show the CAT Control applet.
2. Click **Enable TTY**.

The button highlights green when active. The four channel rows (A, B, C, D) update to show the active symlink paths under `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`.

3. In your external application, open the serial port path shown in the relevant channel row — for example, `/tmp/AetherSDR-CAT-A` for channel A.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| **Enable TTY** | Starts or stops all four PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. | Off | — | — |
| **Enable TCP** | Starts or stops all four rigctld TCP servers on Base through Base+3. | Off | — | — |
| **Base** | Base TCP port. Channels bind to port, port+1, port+2, port+3. PTY channels A–D correspond to the same channel numbering. | 4532 | 1024–65535 | `CatTcpPort` |
| A/B/C/D channel rows | Each row shows the channel badge, TCP server status, and current PTY symlink path. | (stopped) | — | — |

## Tips

- Each channel (A, B, C, D) maps to one radio slice. Point channel A at your primary slice and use channels B–D for additional slices if needed.
- The PTY path shown in each channel row updates to the actual running symlink path once **Enable TTY** is active. If the row still shows `/tmp/AetherSDR-CAT-A`, the PTY has not started successfully.
- You can enable **Enable TTY** and **Enable TCP** simultaneously to serve both serial-style and network-connected applications at the same time.
- To start the PTY symlinks automatically each time AetherSDR launches, use `Settings > Autostart CAT with AetherSDR`.
- Out-of-range values entered in **Base** snap back to 4532 automatically.

## Troubleshooting

- **Channel row still shows `(stopped)` after clicking Enable TTY** — Confirm you are running on Linux or macOS. PTY symlinks are not available on Windows. Also confirm the radio connection is active; the applet requires a connected radio.
- **External application cannot open `/tmp/AetherSDR-CAT-A`** — Confirm **Enable TTY** is active (button shows green). Check that no other process holds an exclusive lock on the symlink. Verify the path shown in the channel row matches what your application is configured to open.
- **PTY path in the channel row does not update** — The symlink may have failed to create. Check that `/tmp/` is writable by your user account.

## Related

- [CAT Control overview](overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Change the base TCP port](change-the-base-tcp-port.md)

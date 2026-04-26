# CAT Control overview

The CAT Control applet lets external logging and contest software control the FLEX-8600 by exposing up to four independent rigctld-compatible interfaces — one per slice. Each channel can be reached over TCP, or on Linux and macOS via a PTY symlink that appears to software as a serial port.

## Before you start

- AetherSDR must be connected to a radio. The CAT applet requires an active radio connection.
- Know which port your logging software expects. The default base port is 4532.

## How it works

The CAT Control applet runs up to four rigctld-compatible servers, one for each slice channel (A, B, C, D). When TCP is enabled, each channel listens on a consecutive port starting at the value in `CatTcpPort`: channel A on the base port, B on base+1, C on base+2, D on base+3. When TTY is enabled on Linux or macOS, each channel also creates a PTY symlink under `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D` that software can open as a virtual serial device.

The applet is hidden by default. Click the **CAT** tray button on the right sidebar to show it. Each channel row shows a colour-coded badge (A/B/C/D matching the slice colour), the current TCP server status, and the PTY path. The TCP status updates in real time as clients connect and disconnect.

Autostart behaviour is controlled separately via `Settings > Autostart rigctld with AetherSDR` (TCP) and `Settings > Autostart CAT with AetherSDR` (TTY).

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| **Enable TCP** | Toggle button | Off | — | — | Starts or stops all four rigctld TCP servers on ports Base through Base+3. Also persists the current base port to `CatTcpPort`. |
| **Enable TTY** | Toggle button | Off | — | — | Starts or stops all four PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Linux and macOS only. |
| **Base** | Text field | 4532 | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels bind to Base, Base+1, Base+2, Base+3. Values outside the valid range snap back to 4532. If the servers are running when you change this value, they restart immediately on the new ports. |
| **A/B/C/D channel rows** | Indicator | (stopped) | — | — | Each row shows the channel badge, TCP status (e.g. `:4532 (1 client)`), and PTY path. The badge and active status text are colour-coded to match the slice. |

## Tips

- If logging software cannot connect, check that **Enable TCP** is on and that no firewall is blocking the port. The channel row will show `(stopped)` if the server is not running, or a port and client count when it is.
- Each channel maps to a slice (A=slice 0, B=slice 1, and so on). Run multiple channels if you want separate programs controlling separate slices simultaneously.
- Changing the **Base** port while servers are running restarts them automatically — connected clients will be dropped and must reconnect.

## Troubleshooting

- **Channel row always shows `(stopped)` after clicking Enable TCP** — the port may already be in use by another application. Change the **Base** value to a free port range and try again.
- **PTY symlinks do not appear** — Enable TTY is only functional on Linux and macOS. The control has no effect on Windows.
- **Logging software loses connection after a port change** — changing **Base** restarts all servers. Reconnect the logging software to the new port.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

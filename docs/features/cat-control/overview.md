# CAT Control overview

CAT Control lets external logging and contest software command the FLEX-8600 through rigctld-compatible interfaces. AetherSDR runs up to four independent servers — one per slice (A, B, C, D) — over TCP, virtual serial ports (PTY), or both simultaneously.

## Before you start

- A FLEX-8600 must be connected. The CAT Control applet requires an active radio connection.
- The CAT applet is hidden by default. Click the CAT tray button on the right sidebar to show it.

## How it works

Each of the four channels (A, B, C, D) maps to one radio slice. When TCP is enabled, each channel listens on its own port starting at the base port: channel A on `Base`, B on `Base+1`, C on `Base+2`, D on `Base+3`. When TTY is enabled on Linux or macOS, each channel creates a PTY symlink that logging software can open as a serial device.

External programs connect to whichever channel controls the slice they want to operate. Multiple clients can connect to the same channel simultaneously; the per-channel status row shows the current client count.

AetherSDR can start the TCP servers and PTY links automatically at launch via `Settings > Autostart rigctld with AetherSDR` and `Settings > Autostart CAT with AetherSDR`.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| Enable TCP | Toggle button | Off | — | — | Starts or stops all four rigctld TCP servers on ports Base through Base+3. Also writes the current base port to `CatTcpPort`. |
| Enable TTY | Toggle button | Off | — | — | Starts or stops all four PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Available on Linux and macOS only. |
| Base | Text field | 4532 | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Values outside the valid range snap back to 4532. If TCP servers are running when you change this value, they restart on the new ports immediately. |
| A / B / C / D channel rows | Indicator | (stopped) | — | — | Each row shows a colour-coded slice badge, the TCP status (for example `:4532 (1 client)` or `(stopped)`), and the PTY symlink path for that channel. |

## Tips

- If a port is already in use by another application, the server for that channel will fail to start. Change `Base` to a free port range and click Enable TCP again.
- The PTY symlink paths (`/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`) are fixed until the PTY starts; once running, the actual path reported by the system appears in the channel row.
- You can run TCP and TTY at the same time on the same channel.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

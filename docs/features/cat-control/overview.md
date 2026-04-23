# CAT Control overview

The CAT Control applet runs up to four rigctld-compatible servers — one per radio slice — so external logging and contest software can control the Flex radio using standard CAT commands. Each channel (A, B, C, D) can be reached over TCP, and on Linux and macOS, also through a virtual serial port (PTY).

## Before you start

- AetherSDR must be connected to a Flex radio. The CAT applet requires an active radio connection.
- The CAT tray button must be visible in the right sidebar. If the applet panel is hidden, enable it via `View > Applet Panel`.

## How it works

Clicking the CAT tray button in the right sidebar opens the CAT Control applet. The applet manages four independent channels, A through D, each mapped to one radio slice. You can start TCP servers, PTY symlinks, or both simultaneously.

**TCP servers** listen on consecutive ports starting at the base port. With the default base of `4532`, channel A binds to port 4532, B to 4533, C to 4534, and D to 4535. Any rigctld-compatible software — N1MM+, Log4OM, WSJT-X, and others — can connect to the appropriate port and control the corresponding slice.

**PTY symlinks** (Linux and macOS only) create virtual serial ports at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Applications that expect a serial device rather than a TCP socket can open these paths directly.

The two transport types are independent. You can enable one, both, or neither.

Autostart options in the `Settings` menu let AetherSDR bring up the TCP servers or PTY links automatically each time it launches, without manual intervention.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| Enable TCP | Toggle button | Off | — | — | Starts or stops all four rigctld TCP servers on Base, Base+1, Base+2, Base+3. Also persists the current base port to `CatTcpPort`. |
| Enable TTY | Toggle button | Off | — | — | Starts or stops all four PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Linux and macOS only. |
| Base | Text field | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Out-of-range values snap back to `4532`. If TCP servers are already running, they restart immediately on the new ports. |
| A / B / C / D channel rows | Indicator | `(stopped)` | — | — | Each row shows a colour-coded channel badge, the TCP status for that channel, and the PTY path. TCP status shows `(stopped)` when the server is not running, or `:<port> (N client(s))` when it is. |

## Tips

- If you change the value in Base while TCP servers are running, AetherSDR restarts all four servers on the new ports automatically. You do not need to toggle Enable TCP off and on.
- To check how many external programs are currently connected to each channel, look at the per-channel TCP status in the A/B/C/D rows. The count updates in real time as clients connect and disconnect.
- To avoid manually starting CAT servers every session, use `Settings > Autostart CAT with AetherSDR` or `Settings > Autostart rigctld with AetherSDR`.

## Troubleshooting

- **Enable TCP has no effect / servers do not start** — AetherSDR must be connected to a radio before the CAT applet can start servers. Verify the radio connection, then try Enable TCP again.
- **Port field snaps back to 4532** — The value entered is outside the valid range of 1024–65535. Enter a value within that range.
- **Enable TTY is missing or does nothing** — PTY symlinks are only available on Linux and macOS. On Windows, the Enable TTY button has no effect.
- **External software cannot connect** — Confirm the base port matches what your logging software expects, and that no firewall is blocking the port. Each channel occupies one port: Base through Base+3.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

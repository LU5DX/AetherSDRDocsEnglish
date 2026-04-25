# CAT Control overview

CAT Control lets external logging and contest software — such as N1MM+, Log4OM, and WSJT-X — command the FLEX-8600 by presenting up to four independent rigctld-compatible interfaces, one per radio slice. Each interface is available as a TCP server, a PTY serial symlink (Linux and macOS only), or both simultaneously.

## Before you start

- AetherSDR must be connected to the radio. CAT Control requires an active radio connection.
- Open the CAT Control applet by clicking the CAT tray button on the right sidebar. The applet is hidden by default.

## How it works

AetherSDR runs up to four rigctld-compatible servers in parallel, labelled channels A, B, C, and D. Each channel maps to one radio slice (slice 0–3). External software connects to a channel and issues standard rigctld commands to read or set frequency, mode, and other parameters on that slice.

**TCP servers** bind to consecutive ports starting from the base port. With the default base port of 4532, channel A binds to port 4532, B to 4533, C to 4534, and D to 4535. Any software that can target a rigctld TCP socket can connect to the appropriate port.

**PTY symlinks** (Linux and macOS only) appear as virtual serial devices under `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Software that expects a serial port path can open these symlinks directly.

TCP and PTY modes are independent. You can run one, both, or neither on any given session. Both modes can be configured to start automatically when AetherSDR launches via `Settings > Autostart rigctld with AetherSDR` and `Settings > Autostart CAT with AetherSDR`.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| Enable TCP | Toggle button | Off | — | — | Starts or stops all four rigctld TCP servers on Base through Base+3. Also persists the current base port to `CatTcpPort`. |
| Enable TTY | Toggle button | Off | — | — | Starts or stops all four PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Linux and macOS only. |
| Base | Text field | 4532 | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels bind to Base, Base+1, Base+2, Base+3. Values outside the valid range snap back to 4532. If TCP servers are already running, they restart immediately on the new ports. |
| A / B / C / D channel rows | Indicator | (stopped) | — | — | Each row shows a colour-coded channel badge, the TCP status for that channel, and the PTY path. TCP status reads `(stopped)` when the server is not running, or `:<port> (N client(s))` when listening. |

## Tips

- If you change the base port while Enable TCP is active, the servers restart automatically on the new ports — you do not need to toggle Enable TCP off and back on.
- The channel badge colours match the slice colours used elsewhere in AetherSDR, making it straightforward to identify which channel corresponds to which slice.
- To check how many external clients are currently connected to each channel, read the TCP status label in each channel row. It updates live as clients connect and disconnect.

## Troubleshooting

- **Enable TCP stays off after clicking it** — Confirm AetherSDR is connected to the radio. CAT Control requires an active radio connection.
- **Port binding fails silently** — Another process on the system may already be using that port. Change Base to an unused port in the range 1024–65535 and click Enable TCP again.
- **Enable TTY has no effect** — PTY symlinks are only available on Linux and macOS. The control has no function on Windows.
- **External software cannot connect** — Verify the software is pointed at the correct port (Base + channel offset 0–3) and that a local firewall is not blocking the connection.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

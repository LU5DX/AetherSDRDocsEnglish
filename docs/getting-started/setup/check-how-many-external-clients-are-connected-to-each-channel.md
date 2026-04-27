# Check how many external clients are connected to each channel

The CAT Control applet shows a live client count for each of the four rigctld TCP channels (A–D). Use this to confirm that your logging or contest software has successfully connected to the right channel.

## Before you start

- The radio must be connected. The CAT Control applet requires an active radio connection.
- Enable TCP must be active. If the servers are not running, all channels show `(stopped)` and no clients can connect. See [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md).

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet.
2. Read the TCP status label on each channel row (A, B, C, D).

Each row displays one of the following states:

| Display | Meaning |
|---|---|
| `(stopped)` | The TCP server for that channel is not running. |
| `:<port> (0 clients)` | Server is running; no external client is connected. |
| `:<port> (1 client)` | One external client is connected on that port. |
| `:<port> (N clients)` | N external clients are connected on that port. |

The port shown is the base port for channel A, base+1 for B, base+2 for C, and base+3 for D. The default base port is `4532` (persisted as `CatTcpPort`).

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Enable TCP** | Off | On / Off | — | Starts or stops all four rigctld TCP servers. Also saves the current base port to `CatTcpPort`. |
| **Enable TTY** | Off | On / Off | — | Starts or stops all four PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. |
| **Base** | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels bind to base, base+1, base+2, base+3. Values outside the valid range snap back to `4532`. If servers are running, they restart on the new ports immediately. |
| A/B/C/D channel rows | `(stopped)` | — | — | Each row shows the slice colour badge, TCP status with client count, and PTY path. Updates live as clients connect or disconnect. |

## Tips

- The TCP status label changes colour when a client is connected: it adopts the slice colour for that channel, making it easier to spot at a glance which channels are in use.
- If you change the value in **Base** while the servers are running, all four servers restart automatically on the new ports. Any connected clients will be dropped and must reconnect.

## Troubleshooting

- **All rows show `(stopped)` even though Enable TCP is on** — The radio connection may have been lost. Check that AetherSDR is connected to the FLEX-8600, then toggle **Enable TCP** off and on again.
- **Client count stays at 0 after starting your logging software** — Confirm the software is pointing at the correct port. Channel A uses the base port (`4532` by default), B uses base+1, and so on. Check the value in the **Base** field and compare it to what your software is configured to connect to.
- **Server fails to start on the selected port** — Another application may already be listening on that port. Change the **Base** value to a free port range and click **Enable TCP** again.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](../../features/cat-control/enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [See how many TCI clients are connected](see-how-many-tci-clients-are-connected.md)

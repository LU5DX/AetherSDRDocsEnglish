# Check how many external clients are connected to each channel

The CAT Control applet shows a live client count for each of the four rigctld TCP channels (A–D). Use this to confirm that your logging or contest software has successfully connected to the right channel.

## Before you start

- AetherSDR must be connected to the radio. The CAT applet requires an active radio connection.
- The TCP servers must be running. Click "Enable TCP" in the CAT applet if you have not already done so. See [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md).

## Steps

1. Click the "CAT" tray button on the right sidebar to open the CAT Control applet.
2. Read the TCP status label on each channel row (A, B, C, D).

That is all. The status updates automatically whenever a client connects or disconnects.

## What each control does

| Control | What it shows | States |
|---|---|---|
| A / B / C / D channel rows | Per-channel server state and connected client count | `(stopped)` when the server is not running; `:<port> (1 client)` or `:<port> (N clients)` when the server is running |
| "Enable TCP" | Starts or stops all four rigctld TCP servers | Off by default; channels bind to `Base`, `Base+1`, `Base+2`, `Base+3` |
| "Base" field | Base TCP port for all four servers | Default: `4532`; valid range: 1024–65535; persisted as `CatTcpPort`; out-of-range values snap back to `4532` |

When a channel has no clients connected, its status label shows the port number in a dim colour. When one or more clients are connected, the label changes to the channel's slice colour and reads `:<port> (N client)` or `:<port> (N clients)`.

## Tips

- Each channel maps to one slice (A = slice 0, B = slice 1, C = slice 2, D = slice 3). If your software connects to the wrong port, it will control the wrong slice.
- The client count reflects TCP connections, not authenticated sessions. A count of 1 normally means one external application is connected.

## Troubleshooting

- **All rows show `(stopped)` even though "Enable TCP" is checked** — The server may have failed to bind the port. Another application may already be using the base port. Change the value in the "Base" field to a different port number and press Enter. AetherSDR will restart the servers on the new ports.
- **Client count stays at 0 after starting your logging software** — Confirm the software is configured to connect to `localhost` (or the correct host) on the expected port (`CatTcpPort` + channel offset). Verify "Enable TCP" is active (the button appears highlighted when on).

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [CAT Control overview](../../features/cat-control/overview.md)
- [See how many TCI clients are connected](see-how-many-tci-clients-are-connected.md)

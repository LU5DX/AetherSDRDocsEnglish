# Check how many external clients are connected to each channel

The CAT Control applet shows a live TCP status indicator for each of the four channels (A–D). Use this to confirm that logging or contest software has successfully connected to the correct rigctld port.

## Before you start

- AetherSDR must be connected to a radio. The CAT Control applet requires an active radio connection.
- TCP servers must be running (Enable TCP must be active). Channels show `(stopped)` until the servers are started.

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet.
2. Look at the channel rows labeled **A**, **B**, **C**, and **D**.
3. Read the TCP status indicator to the right of each channel badge:
   - `(stopped)` — the TCP server for that channel is not running.
   - `:<port> (0 clients)` — the server is listening but no external software is connected.
   - `:<port> (1 client)` — one external client is connected.
   - `:<port> (N clients)` — N clients are connected.

The status updates automatically as clients connect and disconnect. No refresh action is required.

## What each control does

| Control | Description | Default | Range | Setting key |
|---|---|---|---|---|
| Enable TCP | Starts or stops all four rigctld TCP servers on ports Base through Base+3. | Off | — | — |
| Base | Base TCP port. Channel A binds to this port; B, C, D bind to Base+1, Base+2, Base+3. Out-of-range values snap back to 4532. | 4532 | 1024–65535 | `CatTcpPort` |
| A/B/C/D rows | Per-channel indicators showing TCP status and PTY path. | (stopped) | — | — |

## Tips

- The port number shown in the status indicator (for example, `:4532`) confirms which port that channel is listening on. Cross-check this against the port configured in your logging software.
- Channel badge colors match the slice colors used elsewhere in AetherSDR, making it straightforward to match a channel row to a specific receiver slice.

## Troubleshooting

- **All rows show `(stopped)`** — Enable TCP has not been activated. Click **Enable TCP** in the CAT Control applet to start the servers.
- **Status shows `0 clients` but your logging software should be connected** — Confirm the software is pointed at the correct port. Channel A uses the base port (default `4532`); B uses base+1, C uses base+2, D uses base+3. Check that no firewall is blocking the port.
- **Enable TCP is active but a specific channel still shows `(stopped)`** — The port for that channel may already be in use by another application. Change the value in **Base** to a free port range and re-enable.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [CAT Control overview](../../features/cat-control/overview.md)
- [See how many TCI clients are connected](see-how-many-tci-clients-are-connected.md)

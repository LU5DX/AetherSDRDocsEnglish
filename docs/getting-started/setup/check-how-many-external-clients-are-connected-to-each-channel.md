# Check how many external clients are connected to each channel

The CAT Control applet shows a live client count for each of the four rigctld TCP channels. Use this to confirm that logging or contest software has successfully connected to the correct channel.

## Before you start

- AetherSDR must be connected to the radio. The CAT applet requires an active radio connection.
- TCP servers must be running. Click "Enable TCP" in the CAT applet if you have not already done so. See [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md).

## Steps

1. Click the CAT tray button on the right sidebar to open the CAT Control applet.
2. Look at the four channel rows labeled **A**, **B**, **C**, and **D**.
3. Read the TCP status field next to each channel badge:
   - `(stopped)` — the TCP server for that channel is not running.
   - `:<port> (0 clients)` — the server is listening but no external software is connected.
   - `:<port> (1 client)` — one external client is connected.
   - `:<port> (N clients)` — N clients are connected.

The status updates automatically whenever a client connects or disconnects. No manual refresh is needed.

## What each control does

| Control | Kind | Default | Notes |
|---|---|---|---|
| Channel rows (A / B / C / D) | Indicator | `(stopped)` | Each row shows a color-coded channel badge, the TCP status and client count, and the PTY path. The status field color changes to match the slice color when one or more clients are connected. |
| Enable TCP | Toggle button | Off | Starts or stops all four rigctld TCP servers. Ports bind at Base, Base+1, Base+2, Base+3. |
| Base | Text field | `4532` | Base TCP port. Valid range: 1024–65535. Values outside this range snap back to `4532`. Persisted as `CatTcpPort`. |

## Tips

- The TCP status label color shifts to the slice color when at least one client is active, making it easy to spot active channels at a glance.
- Channels A through D correspond to slices 0 through 3. Make sure your external software targets the correct port for the slice it should control.

## Troubleshooting

- **All rows show `(stopped)` even though Enable TCP is on** — The base port may be in use by another application. Change the value in the Base field to a free port in the range 1024–65535 and press Enter. The servers will restart automatically.
- **Client count does not increase after connecting external software** — Confirm the software is targeting the correct port number for the intended channel (Base for A, Base+1 for B, Base+2 for C, Base+3 for D). Verify that Enable TCP is active (button appears highlighted in green when on).

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](../../features/cat-control/enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Change the base TCP port](../../features/cat-control/change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](../../features/cat-control/autostart-cat-servers-with-aethersdr.md)
- [See how many TCI clients are connected](see-how-many-tci-clients-are-connected.md)

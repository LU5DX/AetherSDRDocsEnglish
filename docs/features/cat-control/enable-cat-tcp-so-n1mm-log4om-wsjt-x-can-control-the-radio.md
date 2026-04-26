# Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio

The CAT Control applet runs up to four rigctld-compatible TCP servers, one per slice channel (A–D), so external logging and contest software can control the radio over a network connection. Use this page to start those servers and point your software at the correct port.

## Before you start

- AetherSDR must be connected to the radio. The CAT Control applet requires an active radio connection.
- Know which TCP port your logging software expects. The default base port is `4532`.
- If another application is already listening on port 4532 (for example, a standalone rigctld instance), choose a different base port before enabling.

## Steps

1. Click the **CAT** tray button on the right sidebar to open the CAT Control applet. The applet is hidden by default.
2. Check the **Base** field. The default value is `4532`. If you need a different port, click the field, type a new value (1024–65535), and press Enter. The value is saved to `CatTcpPort`. If you enter an out-of-range value, it snaps back to `4532`.
3. Click **Enable TCP**. The button highlights green when active. All four rigctld TCP servers start immediately, binding to Base, Base+1, Base+2, and Base+3.
4. Confirm the channel rows update. Each row (A, B, C, D) shows a status such as `:4532 (0 clients)` when the server is running and waiting for a connection.
5. In your logging or contest software (N1MM, Log4OM, WSJT-X, or similar), configure the CAT interface as **Hamlib NET rigctl** and set the host to `localhost` and the port to the channel port you want to control:
   - Channel A: Base port (default `4532`)
   - Channel B: Base+1 (default `4533`)
   - Channel C: Base+2 (default `4534`)
   - Channel D: Base+3 (default `4535`)
6. Connect from the external software. The corresponding channel row updates to show the client count, for example `:4532 (1 client)`.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| **Enable TCP** | Toggle button | Off | On / Off | — | Starts or stops all four rigctld TCP servers on Base through Base+3. Also persists the current base port to `CatTcpPort`. |
| **Enable TTY** | Toggle button | Off | On / Off | — | Starts or stops PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Not required for TCP-based software. |
| **Base** | Text field | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels bind to Base, Base+1, Base+2, Base+3. If servers are running when you change this value, they restart on the new ports automatically. |
| **A / B / C / D rows** | Indicator | `(stopped)` | — | — | Shows the server state and connected client count for each channel. Displays `(stopped)` when the server is off, or `:<port> (N clients)` when running. |

## Tips

- Each channel maps to one slice. If you only use one slice, only channel A needs a client connected.
- If you change the **Base** port while **Enable TCP** is already on, the servers restart automatically on the new ports. You do not need to toggle **Enable TCP** off and on again.
- To start the TCP servers automatically every time AetherSDR launches, use `Settings > Autostart rigctld with AetherSDR`.

## Troubleshooting

- **Channel row stays at `(stopped)` after clicking Enable TCP** — Another process may already be listening on that port. Click **Enable TCP** to stop the servers, change **Base** to an unused port, then click **Enable TCP** again.
- **External software connects but cannot control the radio** — Confirm AetherSDR is connected to the FLEX-8600. The CAT Control applet requires an active radio connection. Check the connection status and reconnect if necessary.
- **Port field snaps back to 4532 after I type a value** — The value you entered was outside the valid range of 1024–65535. Enter a value within that range.

## Related

- [CAT Control overview](overview.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

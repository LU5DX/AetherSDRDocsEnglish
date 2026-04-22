# Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio

The CAT Control applet runs up to four rigctld-compatible TCP servers, one per slice channel (A–D). Enable TCP so external logging and contest software can connect to AetherSDR and control the radio over the network.

## Before you start

- AetherSDR must be connected to the radio. The CAT Control applet requires an active radio connection.
- Decide which base port to use. The default is `4532`. Channels A–D bind to Base, Base+1, Base+2, and Base+3 respectively.
- Make sure no other application (including a standalone rigctld instance) is already listening on those ports.

## Steps

1. Click the **CAT** tray button on the right sidebar. The CAT Control applet appears.
2. Check the **Base** field. The default value is `4532`. If you need a different port, click the field, type a new value (1024–65535), and press Enter. Values outside that range snap back to `4532`.
3. Click **Enable TCP**. The button highlights green and all four rigctld TCP servers start.
4. Confirm the channel rows update. Each row that has a server running shows a port and client count, for example `:4532 (0 clients)`. Rows not yet connected by any client show the port dimmed; rows with an active client show the port in the channel's slice color.
5. In your logging or contest software (N1MM, Log4OM, WSJT-X, etc.), configure the CAT interface as **rigctld**, host `localhost` (or the AetherSDR machine's IP address), and port matching the channel you want to control:

   | Channel | Default port |
   |---------|-------------|
   | A       | 4532        |
   | B       | 4533        |
   | C       | 4534        |
   | D       | 4535        |

6. Connect from the external software. The channel row's client count increments to confirm the connection, for example `:4532 (1 client)`.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| **Enable TCP** | Toggle button | Off | On / Off | — | Starts or stops all four rigctld TCP servers on Base through Base+3. When toggled on, also persists the current base port to `CatTcpPort`. |
| **Enable TTY** | Toggle button | Off | On / Off | — | Starts or stops PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Not required for TCP-only software. |
| **Base** | Text field | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channel A binds to this port; B, C, D bind to Base+1, Base+2, Base+3. If TCP is already running when you change this value, all servers restart on the new ports automatically. |
| **A / B / C / D rows** | Indicator | `(stopped)` | — | — | Each row shows the channel badge, current TCP status and connected client count, and the PTY path. |

## Tips

- Each channel maps to one radio slice. If you only use one slice, connect your software to channel A (port `4532` by default) and ignore the other channels.
- If you change the base port while **Enable TCP** is active, the servers restart automatically on the new ports. You do not need to toggle TCP off and back on.
- To start the TCP servers automatically every time AetherSDR launches, use `Settings > Autostart CAT with AetherSDR`.

## Troubleshooting

- **Channel row stays at `(stopped)` after clicking Enable TCP** — Another process may already be listening on that port. Stop the conflicting process, or change **Base** to a free port range and click **Enable TCP** again.
- **External software connects but reports wrong frequency or mode** — Verify the software is pointing to the correct channel port for the slice you want to control. Each channel controls only its assigned slice.
- **Enable TCP has no effect and the button does not stay highlighted** — AetherSDR must be connected to the radio before the CAT servers can start. Connect to the radio first, then click **Enable TCP**.

## Related

- [CAT Control overview](overview.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

# Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio

The CAT Control applet runs up to four rigctld-compatible TCP servers, one per slice channel (A–D). Enabling TCP lets external logging and contest software such as N1MM+, Log4OM, and WSJT-X connect to the radio over a standard network port.

## Before you start

- AetherSDR must be connected to the radio. The CAT applet requires an active radio connection.
- Decide which base port to use. The default is `4532`. Channels A, B, C, and D bind to base, base+1, base+2, and base+3 respectively.
- Make sure no other application (including a standalone rigctld instance) is already listening on those ports.

## Steps

1. Click the **CAT** tray button on the right sidebar. The CAT Control applet appears.
2. Check the value in the **Base** field. The default is `4532`. Change it if needed — valid values are 1024–65535. Press Enter or Tab to confirm; out-of-range values snap back to `4532`.
3. Click **Enable TCP**. The button highlights green when active.
4. Look at the channel rows. Each row that is now serving shows its port and client count, for example `:4532 (0 clients)`. Rows that are not serving show `(stopped)`.
5. In your logging or digital-mode software, configure the CAT/rig-control connection to use `localhost` (or the AetherSDR machine's IP address) and the port for the channel you want to control: base port for channel A, base+1 for channel B, and so on. Select **Hamlib NET rigctl** or **rigctld** as the rig type if your software offers that option.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| **Enable TCP** | Off | — | — | Starts or stops all four rigctld TCP servers. Toggling on also saves the current base port to `CatTcpPort`. |
| **Base** | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channel A uses this port; B, C, and D use base+1, base+2, base+3. If the servers are already running, they restart on the new ports immediately after you confirm the value. |
| **A/B/C/D rows** | `(stopped)` | — | — | Indicators only. Show each channel's current TCP status and connected client count. |

## Tips

- Each channel maps to one slice. If you only use one slice, only channel A needs to be connected by your software; the other servers run but sit idle.
- If you change the **Base** port while **Enable TCP** is already on, the servers restart automatically on the new ports. You do not need to toggle **Enable TCP** off and on again.
- To start the TCP servers every time AetherSDR launches, use `Settings > Autostart rigctld with AetherSDR`.

## Troubleshooting

- **Enable TCP turns on but the row still shows `(stopped)`** — Another process is likely occupying that port. Stop the conflicting process or choose a different base port, then toggle **Enable TCP** off and on again.
- **Software connects but the radio does not respond to commands** — Confirm the software is set to **Hamlib NET rigctl** (not a hardware serial rig type) and that the port number matches the channel row for the slice you intend to control.
- **Port numbers are wrong after restart** — AetherSDR saves the base port to `CatTcpPort` when you confirm the value or toggle **Enable TCP**. If the field was not confirmed before closing, the saved value may differ from what was displayed. Re-enter and confirm the base port.

## Related

- [CAT Control overview](overview.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

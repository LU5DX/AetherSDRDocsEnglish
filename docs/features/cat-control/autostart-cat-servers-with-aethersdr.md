# Autostart CAT servers with AetherSDR

Configure AetherSDR to start its CAT TCP servers or PTY serial links automatically each time the application launches, so your logging or contest software connects without manual intervention.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio before CAT servers can operate. Autostart will queue the servers to start on the next launch when a radio connection is established.
- Decide whether you need TCP servers (for network-connected logging software such as N1MM, Log4OM, or WSJT-X), PTY serial links (for Linux/macOS apps that expect a serial port), or both.
- The CAT Control applet is hidden by default. Click the **CAT** tray button on the right sidebar to show it.

## Steps

### Autostart TCP servers

1. Open the **CAT** applet by clicking the **CAT** tray button on the right sidebar.
2. Click `Settings > Autostart rigctld with AetherSDR` to check that menu item.
3. The **Enable TCP** button in the applet will be checked automatically on the next launch.

### Autostart PTY serial links (Linux/macOS only)

1. Open the **CAT** applet by clicking the **CAT** tray button on the right sidebar.
2. Click `Settings > Autostart CAT with AetherSDR` to check that menu item.
3. The **Enable TTY** button in the applet will be checked automatically on the next launch.

### Verify autostart is active now

1. Restart AetherSDR and reconnect to the radio.
2. Open the **CAT** applet.
3. Confirm **Enable TCP** and/or **Enable TTY** appear checked (highlighted green).
4. Check that each channel row (A, B, C, D) shows a port status such as `:4532 (0 clients)` rather than `(stopped)`.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| `Settings > Autostart rigctld with AetherSDR` | Menu checkbox | unchecked | — | `AutoStartRigctld` | When checked, enables all four rigctld TCP servers on launch. |
| `Settings > Autostart CAT with AetherSDR` | Menu checkbox | unchecked | — | `AutoStartCAT` | When checked, creates PTY symlinks `/tmp/AetherSDR-CAT-A` through `-D` on launch. Linux/macOS only. |
| **Enable TCP** | Toggle button | off | — | — | Starts or stops all four rigctld TCP servers immediately. Also persists the current base port to `CatTcpPort`. |
| **Enable TTY** | Toggle button | off | — | — | Starts or stops all four PTY symlinks immediately. |
| **Base** | Text field | `4532` | 1024–65535 | `CatTcpPort` | Base TCP port. Channels A–D bind to port, port+1, port+2, port+3. Out-of-range values snap back to `4532`. If TCP servers are running, they restart immediately on the new port. |

## Tips

- Enabling autostart via the `Settings` menu sets the persisted preference. Toggling **Enable TCP** or **Enable TTY** in the applet panel changes the current session state and also updates the same persisted value, so either method survives a restart.
- If you change the **Base** port while **Enable TCP** is checked, all four servers restart on the new ports immediately without requiring a restart of AetherSDR.

## Troubleshooting

- **Channel rows still show `(stopped)` after autostart** — The radio was not connected when AetherSDR launched. Connect to the radio, then manually click **Enable TCP** or **Enable TTY** to start the servers for the current session. They will autostart correctly on subsequent launches once the radio is connected.
- **Enable TTY is missing or has no effect on Windows** — PTY serial links are a Linux/macOS feature. Use TCP (via **Enable TCP**) on Windows instead.
- **Port conflicts: server fails to start on a channel** — Another application is already using one of the four ports in the range Base through Base+3. Change **Base** to a different value, such as `4536`, then re-enable TCP.

## Related

- [CAT Control overview](overview.md)
- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

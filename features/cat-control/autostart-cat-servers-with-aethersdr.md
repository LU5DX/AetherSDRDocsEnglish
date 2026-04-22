# Autostart CAT servers with AetherSDR

Configure AetherSDR to start the CAT TCP servers and TTY ports automatically each time it launches, so external logging and contest software connects without manual intervention.

## Before you start

- AetherSDR must be connected to the radio before the CAT applet is functional. Autostart launches the servers on startup, but they require a radio connection to operate.
- Decide whether you need TCP, TTY (PTY), or both. TTY is available on Linux and macOS only.
- Confirm your base port (`CatTcpPort`, default `4532`) is set correctly before enabling autostart. See [Change the base TCP port](change-the-base-tcp-port.md).

## Steps

1. Click `Settings` in the menu bar.
2. To autostart the TCP servers, click `Autostart CAT with AetherSDR`. A checkmark appears next to the item when enabled.
3. Restart AetherSDR. On the next launch, AetherSDR starts all four rigctld TCP servers on ports `Base` through `Base+3` automatically, as if you had clicked `Enable TCP` manually.

To verify the servers started, open the CAT applet:

4. Click the `CAT` tray button on the right sidebar. The CAT Control applet opens.
5. Check each channel row (A, B, C, D). A running server shows `:<port> (0 clients)` or `:<port> (N clients)` rather than `(stopped)`.

## What each control does

| Control | Kind | Default | Behavior | Setting key |
|---|---|---|---|---|
| `Enable TCP` | Toggle button | Off | Starts or stops all four rigctld TCP servers on `Base`, `Base+1`, `Base+2`, `Base+3`. | — |
| `Enable TTY` | Toggle button | Off | Starts or stops all four PTY symlinks at `/tmp/AetherSDR-CAT-A` through `/tmp/AetherSDR-CAT-D`. Linux/macOS only. | — |
| `Base` | Text field | `4532` | Sets the base TCP port. Valid range: 1024–65535. Out-of-range values snap back to `4532`. Restarts running servers when changed. | `CatTcpPort` |
| A/B/C/D channel rows | Indicator | `(stopped)` | Shows TCP status and PTY path per channel. TCP status displays port and connected client count when running. | — |

## Tips

- `Settings > Autostart CAT with AetherSDR` controls TCP autostart. This is separate from `Settings > Autostart rigctld with AetherSDR`, which is a different CAT server mechanism.
- Autostart only starts the servers; it does not open the CAT applet panel automatically. Open it manually with the `CAT` tray button when you need to check status.
- If you change the base port in the `Base` field while servers are running, all four servers restart immediately on the new ports without requiring you to toggle `Enable TCP` off and on.

## Troubleshooting

- **Channel rows still show `(stopped)` after autostart** — The radio connection was not established before AetherSDR attempted to start the servers. Check that the radio is reachable and reconnect. Then click `Enable TCP` manually in the CAT applet to start the servers.
- **`Autostart CAT with AetherSDR` menu item is missing or greyed out** — This item controls PTY-based CAT on Linux and macOS. Verify you are running a supported platform build.
- **Port conflict on startup** — Another application is already using one of the four ports. Change `Base` to an unused port range before enabling autostart.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Enable CAT PTY so Linux/macOS apps can open a serial-style CAT port](enable-cat-pty-so-linux-macos-apps-can-open-a-serial-style-cat-port.md)
- [Change the base TCP port](change-the-base-tcp-port.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

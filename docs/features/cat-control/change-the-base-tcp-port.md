# Change the base TCP port

The CAT Control applet runs up to four rigctld-compatible TCP servers on consecutive ports starting from a configurable base. Change the base port when the default conflicts with another application on your system.

## Before you start

- AetherSDR must be connected to the radio. The CAT applet requires an active radio connection.
- Open the CAT Control applet by clicking the CAT tray button on the right sidebar if it is not already visible.

## Steps

1. In the CAT Control applet, locate the `Base:` label and its text field at the bottom of the applet.
2. Click the `Base:` field and type the new port number. Valid range: 1024–65535. Default: `4532`.
3. Press Enter or Tab to confirm. If the value is outside the valid range, it snaps back to `4532`.
4. The new base port is saved immediately to `CatTcpPort`.
5. If `Enable TCP` is currently active, all four servers restart automatically on the new ports (base, base+1, base+2, base+3). No further action is needed.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| `Base:` | Text field | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels A, B, C, D bind to base, base+1, base+2, base+3. Out-of-range values snap to `4532`. If `Enable TCP` is on, servers restart with the new port immediately. |
| `Enable TCP` | Toggle button | Off | — | — | Starts or stops all four rigctld TCP servers. Also persists the current base port to `CatTcpPort` when toggled. |
| A/B/C/D rows | Indicator | `(stopped)` | — | — | Shows per-channel TCP status as `:<port> (N clients)` when a server is running, or `(stopped)` when it is not. |

## Tips

- Choose a base port that leaves the next three consecutive ports free. For example, a base of `4532` uses `4532`, `4533`, `4534`, and `4535`.
- If you change the port while `Enable TCP` is off, the servers will start on the new port the next time you click `Enable TCP`.

## Troubleshooting

- **Servers do not restart after changing the port** — Confirm you pressed Enter or Tab to finish editing the `Base:` field. Clicking away without committing the edit may not apply the change.
- **Port field snaps back to 4532** — The value entered was outside the 1024–65535 range. Enter a value within that range.
- **Server fails to start on the new port** — Another application may already be using that port or one of the three consecutive ports. Choose a different base port.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

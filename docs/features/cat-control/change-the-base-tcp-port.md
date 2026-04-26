# Change the base TCP port

Change the port number that the CAT Control applet uses as the starting point for its four rigctld TCP servers. Each channel binds to consecutive ports starting at the base: Base, Base+1, Base+2, Base+3.

## Before you start

- AetherSDR must be connected to the radio. The CAT Control applet requires an active radio connection.
- Open the CAT Control applet by clicking the `CAT` tray button on the right sidebar if it is not already visible.

## Steps

1. Locate the `Base:` field in the bottom row of the CAT Control applet.
2. Click the `Base:` field and type the new port number. Valid values are 1024–65535. The default is `4532`.
3. Press Enter or Tab to confirm. If the value is outside the valid range, it resets to `4532` automatically.
4. AetherSDR saves the new value to `CatTcpPort` immediately.
5. If `Enable TCP` is currently active, all four servers stop and restart on the new ports automatically. No further action is needed.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|
| `Base:` | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels A, B, C, D bind to Base, Base+1, Base+2, Base+3. Out-of-range values snap back to `4532`. If `Enable TCP` is on, servers restart with the new port immediately. |
| `Enable TCP` | Off | On/Off | — | Starts or stops all four rigctld TCP servers. Also persists the current base port to `CatTcpPort` when toggled. |
| A/B/C/D rows | `(stopped)` | — | — | Each row shows the channel letter, TCP status (e.g. `:4532 (1 client)`), and PTY path. |

## Tips

- If you change the port while `Enable TCP` is off, the new port takes effect the next time you click `Enable TCP`.
- External software (N1MM, Log4OM, WSJT-X) must be reconfigured to use the new port numbers after any change.
- Channel A uses the base port exactly; channel D uses Base+3. Plan around this if other applications occupy nearby ports.

## Troubleshooting

- **Server does not start after changing the port** — Another application may already be listening on that port or an adjacent port (Base through Base+3). Choose a different base port and try again.
- **Field resets to 4532** — The value entered was outside the 1024–65535 range. Enter a value within the valid range.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

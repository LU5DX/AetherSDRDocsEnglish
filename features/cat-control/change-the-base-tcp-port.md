# Change the base TCP port

The CAT Control applet binds four rigctld-compatible TCP servers to consecutive ports starting at the base port. Change the base port when the default conflicts with another application or when your logging software requires a specific port number.

## Before you start

- The CAT Control applet must be visible. If it is not, click the **CAT** tray button on the right sidebar to show it.
- A radio connection is required.

## Steps

1. In the **Base** field, select the current value and type your desired port number. Valid range: 1024–65535. Default: `4532`.
2. Press Enter or click elsewhere to confirm. If the value is outside the valid range, it snaps back to `4532`.
3. The new value is saved immediately to `CatTcpPort`.
4. If **Enable TCP** is currently active, all four servers stop and restart automatically on the new ports (base, base+1, base+2, base+3). No further action is required.

## What each control does

| Control | Kind | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| **Base** | Text field | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels A, B, C, D bind to base, base+1, base+2, base+3 respectively. Out-of-range values snap back to `4532`. If TCP servers are running, they restart with the new port immediately. |
| **Enable TCP** | Toggle button | Off | — | — | Starts or stops all four rigctld TCP servers. Also persists the current base port to `CatTcpPort` when toggled. |
| A/B/C/D channel rows | Indicator | `(stopped)` | — | — | Shows each channel's TCP status and port number once the servers are running. |

## Tips

- Channels always occupy four consecutive ports. If your base port is `4532`, the four servers listen on `4532`, `4533`, `4534`, and `4535`. Make sure all four ports are free before starting.
- The port change is written to `CatTcpPort` both when you finish editing the **Base** field and when you toggle **Enable TCP**. You do not need to toggle the servers off and on to save the value.

## Troubleshooting

- **Server does not restart after changing the port** — Confirm the new value was accepted by checking that the channel rows show the updated port numbers. If the field reverted to `4532`, the value you entered was outside the 1024–65535 range.
- **Channel row still shows the old port after editing** — The servers only restart automatically if **Enable TCP** was already checked when you pressed Enter. If TCP was off, the new base port takes effect the next time you enable TCP.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

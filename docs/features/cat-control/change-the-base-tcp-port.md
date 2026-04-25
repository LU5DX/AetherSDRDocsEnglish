# Change the base TCP port

Change the port number that the CAT Control applet uses as the starting point for its four rigctld TCP servers. You need to do this when port 4532 conflicts with another application on your system.

## Before you start

- AetherSDR must be connected to the radio. The CAT Control applet requires an active radio connection.
- Open the CAT Control applet by clicking the **CAT** tray button on the right sidebar if it is not already visible.

## Steps

1. Locate the **Base:** field in the top-right area of the CAT Control applet.
2. Click the **Base:** field and type the new port number. Valid range is 1024–65535. The default is `4532`.
3. Press Enter or click away from the field to confirm.
   - If you enter a value outside 1024–65535, the field snaps back to `4532`.
   - The new value is saved to `CatTcpPort` immediately.
   - If **Enable TCP** is currently active, all four servers stop and restart on the new ports automatically. No manual restart is required.

## What each control does

| Control | Default | Valid range | Persisted key | Behavior |
|---------|---------|-------------|---------------|----------|
| **Base:** | `4532` | 1024–65535 | `CatTcpPort` | Sets the base TCP port. Channels A, B, C, and D bind to Base, Base+1, Base+2, and Base+3 respectively. Out-of-range values snap back to `4532`. If **Enable TCP** is on, servers restart immediately with the new ports. |

## Tips

- Choose a base port that leaves the next three ports free. For example, if you set **Base:** to `4532`, the four servers occupy ports 4532, 4533, 4534, and 4535.
- After changing the port, update the port number in any external logging or contest software (N1MM, Log4OM, WSJT-X) to match.
- The channel status rows (A/B/C/D) update to show the new port numbers as soon as the servers restart.

## Troubleshooting

- **Field snaps back to 4532 after I type a new value** — The value you entered was outside the valid range of 1024–65535. Enter a number within that range.
- **Servers do not restart on the new port after changing Base:** — Check that **Enable TCP** is on. If TCP is disabled, the new port is saved but servers do not start until you click **Enable TCP**.
- **Server fails to start on the new port** — Another application may already be listening on that port or one of the three ports above it. Choose a different base port and try again.

## Related

- [Enable CAT TCP so N1MM, Log4OM, WSJT-X can control the radio](enable-cat-tcp-so-n1mm-log4om-wsjt-x-can-control-the-radio.md)
- [Autostart CAT servers with AetherSDR](autostart-cat-servers-with-aethersdr.md)
- [Check how many external clients are connected to each channel](../../getting-started/setup/check-how-many-external-clients-are-connected-to-each-channel.md)

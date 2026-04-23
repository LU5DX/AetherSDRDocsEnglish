# Swap Radios That Share the AG (Antennas in Use by the Other Port Are Locked Out)

When two radios share one Antenna Genius, each radio connects to a separate port (Port A or Port B). Any antenna already selected on one port is locked out — its button is dimmed — on the other port. This page explains how to reassign antennas between ports so neither radio is blocked.

## Before you start

- The Antenna Genius applet must be visible. If the AG tray button is absent, connect to your device first — see [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md) or [Manually connect to an AG over a remote network](../../getting-started/setup/manually-connect-to-an-ag-over-a-remote-network.md).
- The status label must read "Connected — \<name\> v\<version\>". Do not attempt antenna changes while disconnected.
- Your AG device must report two radio ports. If it reports only one, the Port B section is hidden and this procedure does not apply.

## Steps

1. Click the AG tray button on the right sidebar to open the Antenna Genius applet.
2. Look at the Port A antenna buttons and the Port B antenna buttons. Buttons that are dimmed on one port are already selected on the other port and cannot be chosen until released.
3. To free a locked-out antenna, click its currently lit button on the port that holds it. Clicking a selected antenna button a second time deselects it (sets that port to no antenna). The button returns to its unlit state.
4. Once the antenna is deselected on the port that held it, its button becomes active on the other port.
5. Click the now-available antenna button on the port you want to assign it to. The button lights up and the antenna name appears in the port's antenna indicator at the top of that port's section.
6. Confirm the assignment: the antenna indicator next to "Port A" or "Port B" shows the antenna name. If the antenna supports TX on the current band the button is blue; if RX-only on the current band it is amber.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Port A antenna buttons | Click to select an antenna on Port A; click again to deselect. | Dimmed if the antenna is already selected on Port B. Blue = TX+RX permitted; amber = RX only; dim = no permission on current band. |
| Port B antenna buttons | Click to select an antenna on Port B; click again to deselect. | Dimmed if the antenna is already selected on Port A. Port B section is hidden if the device reports only one radio port. |
| Port A AUTO | Toggle. Enables band-follow on Port A so the AG tracks band changes automatically. | Disable AUTO before manually reassigning antennas on Port A if you need explicit control. |
| Port B AUTO | Toggle. Enables band-follow on Port B. | Same caveat as Port A AUTO. |
| Status label | Shows current connection state: "Connected — \<name\> v\<version\>", "Disconnected", "Error: \<msg\>", etc. | Antenna buttons are non-functional when not connected. |
| Port A antenna indicator | Displays the selected antenna name; turns red during TX, orange when TX is routed to an alternate antenna or inhibit is asserted. | Shows "—" when no antenna is selected. |
| Port B antenna indicator | Same as Port A antenna indicator, for Port B. | Shows "—" when no antenna is selected. |

## Tips

- Deselect before reassigning: you must release the antenna from its current port before the button becomes available on the other port. There is no drag-and-drop swap — the release step is required.
- If both radios are in AUTO mode, the AG will follow each radio's band independently. In that case, manual lockout resolution may be overridden immediately by the next band change. Disable AUTO on the relevant port before making manual changes.

## Troubleshooting

- **An antenna button remains dimmed even after I clicked the other port's button to deselect it** — confirm the deselect took effect by checking that the antenna indicator for the other port now shows "—". If the indicator still shows the antenna name, the click may not have registered; click the lit button on the other port once more.
- **Port B section is not visible** — the connected AG device reports only one radio port. Port B sharing is not available on single-port devices.
- **Status label shows "Disconnected" or "Error: \<msg\>"** — antenna buttons cannot be changed while disconnected. Reconnect using Connect or by re-entering the IP in Manual IP and pressing Enter. Invalid addresses produce a red "Invalid IP address" status. The last-used manual IP is stored in `AG_ManualIp` and restored on next launch.

## Related

- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Auto-discover an Antenna Genius on the LAN](auto-discover-an-antenna-genius-on-the-lan.md)

# Swap Radios That Share the AG (Antennas in Use by the Other Port Are Locked Out)

When two radios share a single Antenna Genius, each antenna can only be assigned to one port at a time. This page explains how to reassign antennas between Port A and Port B without conflict, and how to read the lockout indicators before you transmit.

## Before you start

- The Antenna Genius applet must be open and showing "Connected — \<name\> v\<version\>" in the status label.
- The AG device must report two radio ports. The Port B section is hidden when the device reports only one port.
- Identify which antennas each radio is currently using by reading the Port A antenna and Port B antenna indicators at the top of each port section.

## Steps

1. Click the "AG" tray button on the right sidebar to open the Antenna Genius applet.
2. Look at the Port A and Port B antenna indicator labels. An antenna button that appears dim or disabled on one port is already selected on the other port and cannot be selected.
3. To free an antenna that is locked out, go to the port that currently holds it and click its active (checked) antenna button to deselect it. The button toggles off and the antenna selection returns to none (antenna 0).
4. The locked-out button on the other port becomes available immediately. Click it to assign that antenna to the new port.
5. If Port A AUTO or Port B AUTO is enabled, the AG follows band changes automatically and may re-select antennas on its own. If you need stable manual assignment, click "AUTO" on the relevant port to disable AUTO mode before swapping.
6. Confirm the swap by reading both antenna indicator labels. The antenna name should now appear on the intended port.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| Port A antenna buttons | Click to select an antenna on Port A; click again to deselect (returns to antenna 0). | Dim when the antenna is already selected on Port B. Blue = TX+RX allowed; amber = RX only; dim = no permission on the current band. |
| Port B antenna buttons | Click to select an antenna on Port B; click again to deselect. | Dim when the antenna is already selected on Port A. Port B section is hidden if the device reports only one radio port. |
| Port A AUTO | Toggle. Enables band-follow on Port A. | Disable before manually swapping if you need the assignment to stay fixed. |
| Port B AUTO | Toggle. Enables band-follow on Port B. | Disable before manually swapping if you need the assignment to stay fixed. |
| Port A antenna indicator | Shows the selected antenna name. Turns red while transmitting; orange when TX is routed to an alternate antenna or inhibit is asserted. | Displays "—" when no antenna is selected. |
| Port B antenna indicator | Same as Port A antenna indicator, for Port B. | Displays "—" when no antenna is selected. |

## Tips

- Deselect the antenna on its current port first. The button on the other port will not become clickable until the antenna is released.
- Amber-coloured buttons indicate RX-only permission on the current band. Selecting an amber antenna for a port that intends to transmit will route TX to a separate alternate antenna; confirm your setup before keying up.
- AUTO mode on either port can override a manual antenna selection when the radio changes bands. If both ports share a limited antenna set, leaving AUTO on for both ports simultaneously may cause conflicts on band changes.

## Troubleshooting

- **An antenna button stays dim after deselecting it on the other port** — Verify the deselection took effect: the antenna indicator for the port you cleared should show "—". If it still shows an antenna name, click the button once more to toggle it off.
- **Port B section is not visible** — The connected AG device is reporting only one radio port. Port B controls are hidden in this case and two-radio antenna sharing is not available on this device.

## Related

- [Select an antenna for Port A or Port B](select-an-antenna-for-port-a-or-port-b.md)
- [Spot which antennas cannot TX on the current band (amber or dim)](spot-which-antennas-cannot-tx-on-the-current-band-amber-or-dim.md)
- [Enable AUTO mode so the AG follows radio band changes](enable-auto-mode-so-the-ag-follows-radio-band-changes.md)
- [Antenna Genius overview](overview.md)

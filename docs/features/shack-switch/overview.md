# ShackSwitch overview

The ShackSwitch applet lets you control a ShackSwitch antenna switch directly from AetherSDR. Use it to assign antennas to one or two input ports, configure a dummy load for transmit protection, and open the device's web interface — all without leaving the application.

## Before you start

- A ShackSwitch device must be present on your LAN or added through the Peripherals tab in `Settings > Radio Setup...`. AetherSDR discovers ShackSwitch devices automatically via the AG UDP protocol.
- The applet panel must be visible. If it is not, check `View > Applet Panel`.

## How it works

AetherSDR listens on the LAN for a device that identifies itself as a ShackSwitch. When one is found, the ShackSwitch applet appears automatically in the Applet Panel. Toggle its visibility using the ShackSwitch tray button on the right sidebar.

The applet presents every antenna the device reports as a row in a list. Each row has an [A] button and, on dual-port devices, a [B] button. Clicking [A] or [B] routes that antenna to the corresponding input port. The INPUT A card (highlighted in cyan) and INPUT B card (highlighted in orange) always show the current band and antenna name for each port.

If both ports are assigned to the same antenna, the affected [A] and [B] buttons blink amber to signal the conflict. When a dummy load is configured, Port B is automatically routed to the dummy load instead of the selected antenna while that condition applies; the intended row's [B] button blinks amber and the dummy load row's [B] button blinks orange to indicate the automatic rerouting.

On single-port (R4) devices, the INPUT B card and the B column are hidden entirely.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| Status label | Shows the connected device IP address and firmware version, or a disconnected message. | — |
| INPUT A card | Displays the band and antenna name currently assigned to Port A. Highlighted in cyan. Shows — when no antenna is selected. | — |
| INPUT B card | Displays the band and antenna name currently assigned to Port B. Highlighted in orange. Shows — when no antenna is selected. Hidden on single-port (R4) devices. | — |
| [A] button (per antenna row) | Selects that antenna for Input A. Click again to deselect. Blinks amber when Port A and Port B are both assigned to the same antenna. | — |
| [B] button (per antenna row) | Selects that antenna for Input B. Click again to deselect. Blinks amber on conflict. Blinks orange on the dummy load row when Port B is auto-routed there. | — |
| Dummy load selector | Opens a menu to assign one antenna as the dummy load, or clear the assignment. When set, Port B is automatically routed to that antenna to protect the transmit path. Stored as an integer antenna ID; -1 means no dummy load is configured. | `SS_DummyLoadAnt` |
| Settings ⚙ | Opens the ShackSwitch device web configuration interface in the system browser. Uses the live device IP when connected, falls back to `SS_ManualIp`. Port comes from the device beacon, `SS_WebPort`, or defaults to 5000. | `SS_ManualIp`, `SS_WebPort` |

`SS_ControlPort` sets the UDP control port used to communicate with the device.

## Related

- [Select an antenna for ShackSwitch Input A](select-an-antenna-for-shackswitch-input-a.md)
- [Select an antenna for ShackSwitch Input B](select-an-antenna-for-shackswitch-input-b.md)
- [Configure a dummy load antenna to protect the transmit path](configure-a-dummy-load-antenna-to-protect-the-transmit-path.md)
- [Resolve an Input A and Input B antenna conflict](resolve-an-input-a-and-input-b-antenna-conflict.md)
- [Open the ShackSwitch web configuration interface](open-the-shackswitch-web-configuration-interface.md)

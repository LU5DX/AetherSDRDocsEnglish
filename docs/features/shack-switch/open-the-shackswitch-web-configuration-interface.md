# Open the ShackSwitch web configuration interface

The ShackSwitch device includes a built-in web interface for firmware-level configuration. This page explains how to open that interface from within AetherSDR using the "Settings ⚙" button in the ShackSwitch applet.

## Before you start

- The ShackSwitch applet must be visible in the Applet Panel. It appears automatically when a ShackSwitch device is discovered on the LAN, or after connecting via the Peripherals tab in Radio Setup.
- If the device is not currently connected, AetherSDR falls back to the IP address stored in `SS_ManualIp`. Set that value before proceeding if you intend to open the web interface while disconnected.
- Your system browser must be able to reach the ShackSwitch device on the network.

## Steps

1. Locate the ShackSwitch applet in the Applet Panel on the right side of the main window. If it is not visible, click the SS tray button on the right sidebar to show it.
2. Click "Settings ⚙" at the bottom of the applet.
3. AetherSDR constructs a URL from the device IP and web port, then opens it in your system browser.

## What each control does

| Control | Behavior | Persisted setting |
|---|---|---|
| "Settings ⚙" button | Opens the ShackSwitch device web configuration interface in the system browser. Uses the live peer address when connected; falls back to `SS_ManualIp` when disconnected. Port is taken from the device beacon's webPort when that value is above 1024, otherwise from `SS_WebPort`, with a final fallback of 5000. | — |
| `SS_ManualIp` | IP address used when no live device connection is present. | `SS_ManualIp` |
| `SS_WebPort` | Web interface port used when the beacon does not advertise a valid port (above 1024). Default: `5000`. | `SS_WebPort` |
| `SS_DummyLoadAnt` | Stores the antenna ID configured as the dummy load. Set to `-1` when no dummy load is configured. | `SS_DummyLoadAnt` |

## Antenna row controls

Each antenna in the ShackSwitch appears in its own row with the following controls:

| Control | Behavior | Notes |
|---|---|---|
| [A] button (per antenna row) | Selects this antenna for Input A. Deselects if already selected. | Blinks amber when Port A and Port B are both assigned to the same antenna (conflict). |
| [B] button (per antenna row) | Selects this antenna for Input B. Deselects if already selected. | Blinks amber when conflicting. When a dummy load is configured and B is auto-routed there, the intended row B button blinks amber and the dummy load row blinks orange. |
| Dummy load selector | Selects or deselects an antenna as the dummy load. When configured, Port B is automatically routed to the dummy load to protect the antenna when transmitting. | Stored as integer antenna ID. `-1` means no dummy load configured. |

## Status indicators

| Indicator | Display | Meaning |
|---|---|---|
| Status label | Shows the connected device IP address and firmware version, or a disconnected message. | Indicates connection state. |
| INPUT A card | Displays the current band and antenna name selected on Port A. Highlighted in cyan. | Shows `—` when no antenna is selected. |
| INPUT B card | Displays the current band and antenna name selected on Port B. Highlighted in orange. | Hidden on single-port (R4) devices. Shows `—` when no antenna is selected. |

## Tips

- If the device is connected, AetherSDR uses the live peer address automatically. You do not need to set `SS_ManualIp` for normal connected operation.
- The beacon webPort is only trusted when it is above 1024. If the device firmware broadcasts port 80 as a placeholder, AetherSDR ignores it and uses `SS_WebPort` or the default of 5000 instead.
- To open the web interface while the radio is offline, set `SS_ManualIp` to the device's static IP address in advance.
- When a dummy load is configured, AetherSDR automatically routes Input B to the dummy load to protect your main antenna during transmit.

## Troubleshooting

- **Browser opens but the page does not load** — The device may be on a different subnet or behind a firewall. Confirm the IP shown in the ShackSwitch applet's status label is reachable from your machine. Check that the port (default `5000`) is not blocked.
- **Nothing happens when clicking "Settings ⚙"** — AetherSDR will not open a URL if no IP address is available. Either connect to the device so the live address is used, or set `SS_ManualIp` to the device's IP address.
- **Wrong port is used** — If the device serves its web interface on a non-default port and the beacon is not advertising it correctly, set `SS_WebPort` to the correct port number.
- **No antennas appear in the applet** — The device may not have finished discovering its antennas. Wait a few seconds for the beacon to broadcast the antenna list.

## Related

- [ShackSwitch overview](overview.md)
- [Select an antenna for ShackSwitch Input A](select-an-antenna-for-shackswitch-input-a.md)
- [Configure a dummy load antenna to protect the transmit path](configure-a-dummy-load-antenna-to-protect-the-transmit-path.md)
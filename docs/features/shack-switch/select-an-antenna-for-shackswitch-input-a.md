# Select an antenna for ShackSwitch Input A

Use the ShackSwitch applet to route a specific antenna to Input A on your ShackSwitch device. This controls which antenna your radio's Port A uses for receive and transmit.

## Before you start

- A ShackSwitch device must be discovered on the LAN or connected via the Peripherals tab in Radio Setup. The applet appears automatically when a device is found.
- The ShackSwitch applet must be visible in the Applet Panel. If it is not visible, click the SS tray button on the right sidebar to show it.

## Steps

1. Open the Applet Panel. If the ShackSwitch applet is not visible, click the SS tray button on the right sidebar.
2. Locate the antenna list in the applet. Each antenna appears as a row with an antenna name and one or two buttons labeled `[A]` and `[B]`.
3. Find the row for the antenna you want to assign to Input A.
4. Click the `[A]` button in that row.
5. Confirm the selection: the INPUT A card at the top of the applet updates to show the antenna name you selected.

To deselect the current Input A antenna without choosing another, click the active `[A]` button again. The INPUT A card will return to showing —.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| Status label | Shows the connected device IP address and firmware version, or a disconnected message. | — |
| INPUT A card | Displays the current band and antenna name assigned to Port A. Highlighted in cyan. | — |
| INPUT B card | Displays the current band and antenna name assigned to Port B. Highlighted in orange. Hidden on single-port (R4) devices. | — |
| `[A]` button (per antenna row) | Selects that antenna for Input A. Click again to deselect. Blinks amber when Port A and Port B are both assigned to the same antenna (conflict). | — |
| `[B]` button (per antenna row) | Selects that antenna for Input B. Click again to deselect. Blinks amber when conflicting. When a dummy load is configured and B is auto-routed there, the intended row B button blinks amber and the dummy load row blinks orange. | — |
| Dummy load selector | Designates one antenna as a dummy load. When set, Port B is automatically routed to the dummy load to protect the antenna during transmit. | `SS_DummyLoadAnt` |
| Settings ⚙ | Opens the ShackSwitch device web configuration interface in the system browser. Uses the live peer address when connected, falls back to `SS_ManualIp`. Port is taken from `SS_WebPort`, the beacon webPort, or defaults to 5000. | `SS_ManualIp`, `SS_WebPort` |

## Tips

- The `[A]` button highlights in cyan when active, matching the cyan color of the INPUT A card. An unselected `[A]` button is shown in a muted style.
- On single-port (R4) devices, the INPUT B card and `[B]` buttons are hidden. Only Input A selection is available.
- The applet background uses themed styling from the active AetherSDR theme for consistency with other applets.

## Troubleshooting

- **The `[A]` button blinks amber after selection** — Both Input A and Input B are now assigned to the same antenna. This is a conflict. See [Resolve an Input A and Input B antenna conflict](resolve-an-input-a-and-input-b-antenna-conflict.md) to resolve it.
- **The antenna list is empty** — The applet has not yet received antenna data from the device. Check that the ShackSwitch is reachable on the LAN and that the status label shows a connected IP address rather than a disconnected message.
- **The INPUT A card still shows — after clicking `[A]`** — The device may not have confirmed the selection yet. Verify the status label shows a connected device. If the device is disconnected, the command cannot be sent.

## Related

- [ShackSwitch overview](overview.md)
- [Select an antenna for ShackSwitch Input B](select-an-antenna-for-shackswitch-input-b.md)
- [Resolve an Input A and Input B antenna conflict](resolve-an-input-a-and-input-b-antenna-conflict.md)
- [Configure a dummy load antenna to protect the transmit path](configure-a-dummy-load-antenna-to-protect-the-transmit-path.md)
- [Open the ShackSwitch web configuration interface](open-the-shackswitch-web-configuration-interface.md)
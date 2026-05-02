# Select an antenna for ShackSwitch Input B

Use the ShackSwitch applet to assign an antenna to Input B. Input B is the second port on multi-port ShackSwitch devices and is not available on single-port (R4) models.

## Before you start

- A ShackSwitch device must be discovered on the LAN or connected via the Peripherals tab in Radio Setup. The applet appears automatically when a device is active.
- The ShackSwitch applet must be visible in the Applet Panel. If it is not visible, click the SS tray button on the right sidebar.
- Confirm the INPUT B card is shown in the applet. If it is hidden, your device is a single-port (R4) model and Input B is not available.

## Steps

1. Open the Applet Panel and locate the ShackSwitch applet.
2. Find the antenna row you want to assign to Input B. Antenna names are listed under the ANTENNA column.
3. Click the **[B]** button on that antenna row. The button highlights in orange to confirm the selection.
4. Confirm the INPUT B card at the top of the applet updates to show the selected antenna name.

To deselect the current Input B antenna, click its active **[B]** button again.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| INPUT B card | Displays the current band and antenna name assigned to Port B. Hidden on single-port (R4) devices. | — |
| **[B]** button (per antenna row) | Selects this antenna for Input B. Click again to deselect. Blinks amber when Port A and Port B are both assigned to the same antenna. | — |
| Dummy load selector | Opens a menu to designate one antenna as a dummy load. When configured, Port B is automatically routed to the dummy load to protect the antenna during transmit. | `SS_DummyLoadAnt` |

## Tips

- If the **[B]** button blinks amber after you select an antenna, both inputs are now assigned to the same antenna. See [Resolve an Input A and Input B antenna conflict](resolve-an-input-a-and-input-b-antenna-conflict.md).
- If a dummy load is configured and Port B is auto-routed there, the **[B]** button on your intended antenna row blinks amber and the dummy load row's **[B]** button blinks orange. To override this behavior, remove the dummy load assignment using the Dummy load selector.

## Troubleshooting

- **The INPUT B card and [B] buttons are not visible** — Your ShackSwitch device is a single-port (R4) model. Input B is not available on that hardware.
- **Clicking [B] has no effect** — The applet status label shows "Not connected". The ShackSwitch device is not reachable. Verify the device is powered and on the same network segment. Check `SS_ManualIp` and `SS_ControlPort` in Radio Setup if auto-discovery is not working.

## Related

- [Select an antenna for ShackSwitch Input A](select-an-antenna-for-shackswitch-input-a.md)
- [Resolve an Input A and Input B antenna conflict](resolve-an-input-a-and-input-b-antenna-conflict.md)
- [Configure a dummy load antenna to protect the transmit path](configure-a-dummy-load-antenna-to-protect-the-transmit-path.md)
- [Open the ShackSwitch web configuration interface](open-the-shackswitch-web-configuration-interface.md)

# Configure a dummy load antenna to protect the transmit path

Use the dummy load selector to designate one antenna port as a dummy load. When configured, Port B is automatically routed to that port to protect your antenna from unintended transmission.

## Before you start

- A ShackSwitch device must be discovered on the LAN or connected via the Peripherals tab in Radio Setup. The ShackSwitch applet appears automatically when a device is active.
- The ShackSwitch applet must be visible. If it is not, click the SS tray button on the right sidebar.
- At least one antenna must be present in the antenna list before a dummy load can be assigned.

## Steps

1. Open the ShackSwitch applet in the Applet Panel.
2. Click the "Dummy Load: None" button near the bottom of the applet. A menu appears listing None and all available antenna names.
3. Click the antenna name you want to designate as the dummy load. A checkmark appears next to the selected antenna and the button label updates to show the chosen antenna name.
4. To remove the dummy load assignment, click the button again and select None.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Dummy load selector button | Opens a menu to assign or clear the dummy load antenna. When an antenna is assigned, Port B is automatically routed to it. The button label reflects the current assignment. | None | `SS_DummyLoadAnt` |

`SS_DummyLoadAnt` stores the integer antenna ID of the assigned dummy load. A value of `-1` means no dummy load is configured.

## Tips

- When a dummy load is configured and Port B is auto-routed to it, the [B] button on the intended antenna row blinks amber and the dummy load row's [B] button blinks orange. This gives you a visible indication that B has been parked on the dummy load rather than the antenna you selected.
- The dummy load assignment persists across sessions via `SS_DummyLoadAnt`. You do not need to reconfigure it each time you connect.

## Troubleshooting

- **The antenna list in the menu is empty** — The ShackSwitch device has not yet reported any antenna ports. Confirm the device is connected and the status label shows a valid IP address and firmware version rather than a disconnected message.
- **Port B is not routing to the dummy load** — Verify `SS_DummyLoadAnt` is set to a valid antenna ID (not `-1`) by checking that the dummy load selector button shows an antenna name rather than "Dummy Load: None".

## Related

- [ShackSwitch overview](overview.md)
- [Select an antenna for ShackSwitch Input B](select-an-antenna-for-shackswitch-input-b.md)
- [Resolve an Input A and Input B antenna conflict](resolve-an-input-a-and-input-b-antenna-conflict.md)

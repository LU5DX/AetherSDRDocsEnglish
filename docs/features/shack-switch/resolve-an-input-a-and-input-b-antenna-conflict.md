# Resolve an Input A and Input B antenna conflict

A conflict occurs when both Input A and Input B are assigned to the same antenna. AetherSDR signals the conflict visually so you can reassign one input before transmitting.

## Before you start

- AetherSDR has discovered a ShackSwitch device and the ShackSwitch applet is visible in the Applet Panel.
- The ShackSwitch device has at least two antenna ports available (the INPUT B card is not shown on single-port R4 devices, so a conflict is not possible on those).

## Steps

1. Look at the antenna rows in the ShackSwitch applet. When a conflict exists, the `[A]` button and the `[B]` button on the same antenna row both blink amber.
2. Decide which input to move. Either click the `[A]` button on a different antenna row to reassign Input A, or click the `[B]` button on a different antenna row to reassign Input B.
3. Confirm the blinking stops. The INPUT A card and INPUT B card should each show a different antenna name, and neither button blinks.

## What each control does

| Control | Behavior | Setting key |
|---|---|---|
| `[A]` button (per antenna row) | Selects that antenna for Input A. Clicking an already-selected antenna deselects it. Blinks amber when Input A and Input B are both assigned to the same antenna. | — |
| `[B]` button (per antenna row) | Selects that antenna for Input B. Clicking an already-selected antenna deselects it. Blinks amber when conflicting. When a dummy load is configured and Input B is auto-routed there, the intended row `[B]` button blinks amber and the dummy load row `[B]` button blinks orange. | — |
| INPUT A card | Shows the current band and antenna name assigned to Port A. Displays — when no antenna is selected. | — |
| INPUT B card | Shows the current band and antenna name assigned to Port B. Displays — when no antenna is selected. Hidden on single-port R4 devices. | — |
| Dummy load selector | Assigns an antenna as the dummy load. When configured, Port B is automatically routed to the dummy load, which can cause the amber blink on the intended antenna row. | `SS_DummyLoadAnt` |

## Tips

- If the conflict reappears immediately after you reassign an input, check whether a dummy load is configured. When `SS_DummyLoadAnt` is set, Port B is automatically routed to the dummy load antenna. If that antenna is the same one assigned to Input A, the conflict will persist until you either change the Input A selection or reconfigure the dummy load.
- Clicking an already-active `[A]` or `[B]` button deselects that input entirely, leaving the corresponding card showing —. This is a valid way to clear one side of the conflict if you intend to leave that input unassigned.

## Troubleshooting

- **Buttons keep blinking after reassignment** — A dummy load may be auto-routing Input B back to the conflicting antenna. Open the Dummy load selector and check which antenna is set. Select a different antenna or choose None to clear it.
- **INPUT B card is not visible** — The connected device is a single-port R4 ShackSwitch. Input B is not available on this device; a two-input conflict cannot occur.

## Related

- [Configure a dummy load antenna to protect the transmit path](configure-a-dummy-load-antenna-to-protect-the-transmit-path.md)
- [Select an antenna for ShackSwitch Input A](select-an-antenna-for-shackswitch-input-a.md)
- [Select an antenna for ShackSwitch Input B](select-an-antenna-for-shackswitch-input-b.md)
- [ShackSwitch overview](overview.md)

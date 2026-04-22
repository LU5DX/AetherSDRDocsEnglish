# Assign a USB cable as CAT, BCD, bit or PTT

The USB Cables tab lets you assign a physical USB serial adapter connected to your FLEX-8600 to one of four cable types: CAT, BCD, bit, or PTT. Use this to control external equipment such as amplifiers, antenna switches, or logging software via the radio's USB ports.

## Before you start

- AetherSDR must be connected to the radio. The USB Cables tab requires an active radio connection.
- The USB serial adapter must be physically plugged into the FLEX-8600 before opening this dialog. Cables appear in the list only when detected by the radio.

## Steps

1. Open `Settings > USB Cables...`. This opens the Radio Setup dialog directly on the **USB Cables** tab. Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Locate your cable in the **Cables list**. The **Status** column shows **Plugged** or **Unplugged** for each detected cable.
3. Select the cable you want to configure by clicking its row in the list.
4. Set **Name:** to a label that identifies this cable in your station.
5. Set **Enabled** to the active state to put the cable into service.
6. Set **Speed**, **Data Bits**, **Parity**, **Stop Bits**, and **Flow** to match the baud rate and framing expected by the connected equipment.
7. Set **Source** to the slice or radio source that drives the cable's output.
8. If the cable type is BCD, set **BCD Type** and **Auto Report** as required by your equipment.
9. If the cable type is bit, configure **Bit Configuration (0-7)** and **Polarity** for each bit line.
10. If the cable type is PTT, set **Polarity** to match the active-high or active-low requirement of the connected device.
11. Close the dialog. Settings are applied to the radio immediately when each control is changed.

## What each control does

| Control | Description |
|---|---|
| **Cables list / Status** | Lists all USB serial adapters the radio has detected, with **Plugged** or **Unplugged** status for each. |
| **Name:** | User-assigned label for this cable entry. |
| **Enabled** | Activates the cable. The cable carries no signal while disabled. |
| **Speed** | Serial baud rate for the cable. |
| **Data Bits** | Number of data bits per character. |
| **Parity** | Parity scheme (None, Even, Odd, etc.). |
| **Stop Bits** | Number of stop bits. |
| **Flow** | Hardware or software flow control selection. |
| **Source** | The radio slice or signal source routed to this cable. |
| **Auto Report** | When enabled, the radio pushes state changes to the cable without polling. |
| **BCD Type** | Selects the BCD encoding format. Applies to BCD cable types only. |
| **Polarity** | Inverts the active state of the output line. Applies to bit and PTT cable types. |
| **Bit Configuration (0-7)** | Assigns a function to each of the eight bit lines on the cable. Applies to bit cable types only. |

## Troubleshooting

- **Cable does not appear in the list** — The radio has not detected the USB adapter. Check that the adapter is plugged into the FLEX-8600 (not the host PC) and that the **Status** column shows **Plugged**. If status remains **Unplugged**, try unplugging and re-inserting the adapter, then close and reopen the dialog.
- **Cable is listed but produces no output** — Confirm that **Enabled** is active for that cable. Also verify that **Speed**, **Parity**, and **Stop Bits** match the requirements of the connected equipment.
- **PTT line stays asserted or never asserts** — Check the **Polarity** setting. Toggling **Polarity** inverts the active level.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)

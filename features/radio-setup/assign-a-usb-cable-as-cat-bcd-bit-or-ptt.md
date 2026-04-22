# Assign a USB cable as CAT, BCD, bit or PTT

Use this page to configure a USB serial adapter connected to your FLEX-8600 as a CAT control cable, BCD band-decoder output, individual bit output, or PTT line. Each connected adapter appears in the USB Cables tab where you set its type and serial parameters.

## Before you start

- AetherSDR must be connected to the radio. The USB Cables tab is only available while connected.
- The USB serial adapter must be physically plugged in to the radio's USB port before opening the dialog, so the radio can detect it.

## Steps

1. Open `Settings > USB Cables...`. The Radio Setup dialog opens directly on the **USB Cables** tab. Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Locate your cable in the **Cables list**. Each detected adapter is listed with its current **Status** shown as Plugged or Unplugged.
3. Select the cable entry you want to configure.
4. Set **Name:** to a descriptive label for the cable.
5. Set **Enabled** to the desired state for this cable.
6. Set **Speed**, **Data Bits**, **Parity**, **Stop Bits**, and **Flow** to match the serial parameters required by the connected device.
7. Set **Source** to define what drives the cable's output.
8. If the cable type is BCD, set **BCD Type** and **Polarity** as required by your band decoder.
9. If the cable type is bit, use **Bit Configuration (0-7)** to assign the function of each output bit.
10. If the cable type is PTT, confirm **Polarity** matches your amplifier or accessory input.
11. Enable **Auto Report** if the connected device expects the radio to send updates automatically.

## What each control does

| Control | Description |
|---|---|
| Cables list / Status | Lists all USB adapters detected by the radio. Status shows Plugged or Unplugged for each entry. |
| Name: | User-assigned label for this cable entry. |
| Enabled | Activates or deactivates the cable assignment. |
| Speed | Serial baud rate for this cable. |
| Data Bits | Number of data bits per serial frame. |
| Parity | Parity setting for the serial connection. |
| Stop Bits | Number of stop bits per serial frame. |
| Flow | Flow control mode. |
| Source | Selects what radio event or data drives this cable's output. |
| Auto Report | When active, the radio sends updates to the cable automatically rather than on demand. |
| BCD Type | Selects the BCD encoding scheme (applies to BCD cable type). |
| Polarity | Inverts the active logic level on the output (applies to BCD and PTT cable types). |
| Bit Configuration (0-7) | Assigns a function to each of the eight output bits (applies to bit cable type). |

## Tips

- You can also reach the USB Cables tab by going to `Settings > Radio Setup...` and selecting **USB Cables** from the tab bar.
- If a cable shows Unplugged, plug it in to the radio's USB port and reopen the dialog or wait for the status to refresh.
- CAT cables allow external logging and contest software to control the radio's VFO and mode over a virtual serial connection.

## Troubleshooting

- **Cable does not appear in the Cables list** — The adapter must be plugged in to the radio hardware, not the PC. Confirm the adapter is connected to the FLEX-8600's USB port, then reopen the dialog.
- **Status shows Unplugged despite cable being connected** — Reconnect the USB adapter to the radio and allow a moment for the radio firmware to detect it before reopening the dialog.
- **BCD or bit outputs are inverted** — Toggle **Polarity** for that cable entry.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)

# Assign a USB cable as CAT, BCD, bit or PTT

The USB Cables tab lets you assign physical USB serial adapters connected to the FLEX-8600 to a specific cable type — CAT, BCD, bit, or PTT — and configure per-cable serial parameters. Use this when you need the radio to drive external equipment such as amplifiers, band decoders, or logging software through a USB serial port.

## Before you start

- AetherSDR must be connected to the radio. The USB Cables tab is only available while a radio connection is active.
- The USB cable must already be physically plugged into the FLEX-8600's USB port. Cables that are not detected appear with an "Unplugged" status in the list.

## Steps

1. Open `Settings > USB Cables...`. This opens the Radio Setup dialog directly on the USB Cables tab. Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Review the **Cables list / Status** indicator. Each detected USB cable is listed with its type and a Plugged or Unplugged status.
3. Select the cable you want to configure from the list.
4. Set **Name:** to a descriptive label for the cable.
5. Set **Enabled** to enable the cable.
6. Set **Speed**, **Data Bits**, **Parity**, **Stop Bits**, and **Flow** to match the serial parameters required by your external equipment.
7. Set **Source** to the signal source this cable should follow.
8. For BCD cables, set **BCD Type** and configure **Polarity** as needed.
9. For bit cables, configure **Bit Configuration (0-7)** and **Polarity**.
10. For CAT cables, set **Auto Report** to control whether the radio sends unsolicited frequency updates.
11. For PTT cables, set **Polarity** to match your equipment's keying sense.
12. Close the dialog. Settings are applied to the radio immediately.

## What each control does

| Control | Description |
|---|---|
| **Cables list / Status** | Lists all detected USB cables by type. Shows Plugged or Unplugged for each. |
| **Name:** | User-assigned label for the cable. |
| **Enabled** | Activates the cable. |
| **Speed** | Serial baud rate for this cable. |
| **Data Bits** | Number of data bits per frame. |
| **Parity** | Parity setting for the serial link. |
| **Stop Bits** | Number of stop bits per frame. |
| **Flow** | Hardware or software flow control selection. |
| **Source** | Selects which radio signal or slice drives the output on this cable. |
| **Auto Report** | When enabled, the radio sends frequency and mode updates automatically (CAT cables). |
| **BCD Type** | Selects the BCD encoding format (BCD cables only). |
| **Polarity** | Inverts the active logic level on the cable output. |
| **Bit Configuration (0-7)** | Maps individual output bits to radio states (bit cables only). |

## Tips

- You can reach the same tab via `Settings > Radio Setup...` and then clicking **USB Cables** if you need to switch to another tab (such as TX or Peripherals) in the same session without reopening the dialog.
- The Plugged or Unplugged status in **Cables list / Status** updates dynamically. If a cable is not listed, check the physical USB connection to the radio, then reopen the tab.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)
- [Connect TGXL, PGXL or Antenna Genius by IP](../../getting-started/setup/connect-tgxl-pgxl-or-antenna-genius-by-ip.md)

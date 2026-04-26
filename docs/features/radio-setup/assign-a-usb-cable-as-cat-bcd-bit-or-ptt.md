# Assign a USB cable as CAT, BCD, bit or PTT

The USB Cables tab in Radio Setup lets you assign physical USB serial adapters connected to the FLEX-8600 to specific functions: CAT control, BCD band data, individual bit outputs, or PTT. Use this page to configure which cable does what and to set its serial parameters.

## Before you start

- AetherSDR must be connected to the radio. The USB Cables tab is not accessible without an active radio connection.
- The USB serial adapter must be physically plugged into the FLEX-8600 before you open the tab. Unplugged cables appear with an Unplugged status.

## Steps

1. Open `Settings > USB Cables...`. This opens the Radio Setup dialog directly on the **USB Cables** tab. Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Locate your cable in the **Cables list**. Each detected adapter is listed with its current **Status** shown as Plugged or Unplugged.
3. Select the cable entry you want to configure.
4. Set **Name:** to a descriptive label for the cable.
5. Set the cable type using the appropriate field. The available types are CAT, BCD, bit, and PTT. Select the type that matches your intended use.
6. Set **Enabled** to enable the cable once configuration is complete.
7. For CAT and BCD cables, configure the serial line parameters: **Speed**, **Data Bits**, **Parity**, **Stop Bits**, and **Flow**.
8. Set **Source** to select what drives the cable output.
9. For CAT cables, set **Auto Report** as needed.
10. For BCD cables, set **BCD Type** and **Polarity**.
11. For bit cables, configure **Bit Configuration (0–7)** and **Polarity** for each bit position.
12. Close the dialog. Settings are applied to the radio immediately when each control is changed.

## What each control does

| Control | Description |
|---|---|
| **Cables list / Status** | Lists all detected USB cables and shows Plugged or Unplugged for each. |
| **Name:** | User-assigned label for the cable. |
| **Enabled** | Activates or deactivates the cable. |
| **Speed** | Serial baud rate for the cable. |
| **Data Bits** | Number of data bits per serial frame. |
| **Parity** | Parity setting for the serial connection. |
| **Stop Bits** | Number of stop bits per serial frame. |
| **Flow** | Flow control mode. |
| **Source** | Selects what signal or data source drives this cable's output. |
| **Auto Report** | Controls whether the radio automatically sends updates over the CAT cable. |
| **BCD Type** | Selects the BCD encoding format (BCD cables only). |
| **Polarity** | Sets active-high or active-low polarity for BCD and bit cables. |
| **Bit Configuration (0–7)** | Assigns a function to each of the eight bit outputs (bit cables only). |

## Tips

- If a cable you expect to see is not listed, check that it is physically plugged into the radio and that the radio firmware recognizes it. Reopening the USB Cables tab after plugging in the cable may be necessary to refresh the list.
- Configuring a cable as PTT requires no serial parameters — only **Enabled**, **Source**, and **Polarity** apply.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)

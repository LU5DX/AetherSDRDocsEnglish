# Assign a USB cable as CAT, BCD, bit or PTT

The USB Cables tab in Radio Setup lets you assign physical USB serial adapters connected to the FLEX-8600 to specific control roles: CAT, BCD, bit, or PTT. Use this page when you want an external device or amplifier controller to communicate with the radio over a USB serial cable.

## Before you start

- Connect the USB serial adapter to the FLEX-8600 before opening the dialog. The radio must detect the cable for it to appear in the list.
- AetherSDR must be connected to the radio.

## Steps

1. Open `Settings > USB Cables...`.
   The Radio Setup dialog opens with the **USB Cables** tab already selected.
   Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Locate your cable in the **Cables list / Status** indicator. Each detected cable is listed with its type and a **Plugged** or **Unplugged** status.
3. Select the cable you want to configure by clicking it in the list.
4. Set the cable's role and serial parameters using the controls that appear for the selected cable:
   - **Name:** — identifies the cable.
   - **Enabled** — enables or disables this cable assignment.
   - **Speed** — serial baud rate.
   - **Data Bits** — number of data bits.
   - **Parity** — parity setting.
   - **Stop Bits** — number of stop bits.
   - **Flow** — flow control method.
   - **Source** — the radio source this cable tracks.
   - **Auto Report** — controls automatic state reporting.
   - **BCD Type** — applies when the cable type is BCD; sets the BCD encoding variant.
   - **Polarity** — signal polarity (normal or inverted).
   - **Bit Configuration (0-7)** — applies when the cable type is bit; assigns individual bit functions.
5. Close the dialog when finished. Settings are applied to the radio immediately as you make changes.

## What each control does

| Control | Description |
|---|---|
| **Cables list / Status** | Read-only list of detected USB cables and their current **Plugged** or **Unplugged** state. |
| **Name:** | Label identifying the cable. |
| **Enabled** | Activates or deactivates this cable's assignment on the radio. |
| **Speed** | Serial port baud rate for the cable. |
| **Data Bits** | Word length for the serial link. |
| **Parity** | Parity checking mode for the serial link. |
| **Stop Bits** | Number of stop bits for the serial link. |
| **Flow** | Hardware or software flow control selection. |
| **Source** | Which radio slice or signal source this cable reports. |
| **Auto Report** | Whether the radio automatically sends state updates over this cable. |
| **BCD Type** | BCD encoding variant; active only for BCD-type cables. |
| **Polarity** | Sets the logic polarity of the output signal. |
| **Bit Configuration (0-7)** | Assigns a function to each of the eight bit outputs; active only for bit-type cables. |

## Troubleshooting

- **Cable does not appear in the list** — The radio enumerates cables at connection time. Unplug and replug the USB adapter, then close and reopen `Settings > USB Cables...` to refresh the list. Confirm the adapter is connected to the radio's USB port, not to the host PC.
- **Status shows Unplugged** — The cable is configured but currently not physically present. Reconnect the adapter to the radio.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)

# Assign a USB cable as CAT, BCD, bit or PTT

Use this page to configure the USB serial adapters connected to your FLEX-8600 and assign each one a role — CAT control, BCD band data, individual bit output, or PTT — along with its serial parameters and behavior options.

## Before you start

- Connect the USB serial adapter(s) to the computer running AetherSDR before opening the dialog.
- AetherSDR must be connected to the radio. The USB Cables tab is not available without an active radio connection.

## Steps

1. Open `Settings > USB Cables...`. This opens the Radio Setup dialog directly on the USB Cables tab. Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Locate the cables list on the left side of the tab. Each detected USB cable appears with its name and a **Plugged** or **Unplugged** status indicator.
3. Select the cable you want to configure by clicking it in the list.
4. Set the cable type using the **Name:** field and the associated type selector. Choose from CAT, BCD, bit, or PTT depending on the role this cable should serve.
5. Set **Enabled** to enable the cable. The cable will not function until it is enabled.
6. Configure the serial parameters for the cable:
   - **Speed** — baud rate for the serial connection.
   - **Data Bits** — number of data bits.
   - **Parity** — parity setting.
   - **Stop Bits** — number of stop bits.
   - **Flow** — flow control method.
7. Configure the behavioral options relevant to the cable type:
   - **Source** — selects what drives the cable output.
   - **Auto Report** — controls whether state changes are reported automatically.
   - **BCD Type** — selects the BCD encoding format (BCD cables only).
   - **Polarity** — sets active-high or active-low logic.
   - **Bit Configuration (0–7)** — assigns functions to individual output bits (bit cables only).
8. Repeat steps 3–7 for any additional cables.
9. Click **Close** to dismiss the dialog. Settings take effect immediately when each cable is enabled; no separate Apply step is required.

## What each control does

| Control | Description |
|---|---|
| **Cables list / Status** | Lists all detected USB serial adapters with **Plugged** or **Unplugged** status. Select a cable here to edit its settings. |
| **Name:** | User-visible label for the cable. |
| **Enabled** | Activates the cable. The cable is inactive until enabled. |
| **Speed** | Serial baud rate. |
| **Data Bits** | Number of serial data bits. |
| **Parity** | Serial parity: None, Even, Odd, etc. |
| **Stop Bits** | Number of stop bits. |
| **Flow** | Flow control method (None, Hardware, Software). |
| **Source** | Selects the radio signal source that drives the cable output. |
| **Auto Report** | When active, the radio reports state changes to the cable automatically. |
| **BCD Type** | Selects the BCD band-data encoding format. Applies to BCD-type cables only. |
| **Polarity** | Sets whether the output logic is active-high or active-low. |
| **Bit Configuration (0–7)** | Maps individual output pins to specific functions. Applies to bit-type cables only. |

## Tips

- If a cable shows **Unplugged**, check the physical USB connection and reopen the dialog. The list reflects the state at the time the tab was built.
- Assign only one PTT cable at a time if you want predictable transmit keying behavior.
- BCD and bit cables share many of the same serial parameters; configure **Speed**, **Data Bits**, **Parity**, **Stop Bits**, and **Flow** to match the expectations of the external device receiving the data.

## Troubleshooting

- **Cable shows Unplugged even though it is connected** — The USB adapter may not have been present when the tab loaded. Close Radio Setup, ensure the adapter is recognized by the OS, then reopen `Settings > USB Cables...`.
- **Enabled toggle has no effect** — Confirm the radio is connected. The USB Cables tab requires an active radio connection; controls do not send commands without it.
- **BCD or bit outputs are inverted** — Check the **Polarity** setting for the cable and toggle it to match your external device's logic levels.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)

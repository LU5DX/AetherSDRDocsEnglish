# Configure FlexControl Serial Port Pin Functions

This page explains how to select and configure the serial port used by a FlexControl device, set line parameters, and assign functions to the DTR and RTS output pins. You need this if you are connecting a FlexControl knob or a serial-controlled accessory to AetherSDR.

## Before you start

- The radio must be connected. The Serial tab is only available when AetherSDR has an active radio connection.
- The Serial tab is only present in builds that include serial port support. If you do not see it, your build does not include this feature.
- Know the device path of your serial port (for example, `/dev/ttyUSB0` on Linux or `COM3` on Windows).

## Steps

1. Open `Settings > FlexControl...`. This opens the Radio Setup dialog directly on the Serial tab. Alternatively, open `Settings > Radio Setup...` and click the **Serial** tab.
2. In the **Port** combo box, select your serial port from the list. If your port does not appear, click **Refresh** to rescan. To enter a path manually, type it into the **Path** field.
3. Set the line parameters using the **Baud**, **Data**, **Parity**, and **Stop** combo boxes to match your device.
4. For each of the **DTR** and **RTS** output pins, set the desired **Function** using its combo box, then set the **Polarity** using the adjacent combo box.
5. If your paddle connections are reversed, check **Paddle Swap (swap dit/dah)**.
6. To have AetherSDR open this port every time it starts, check **Auto-open serial port on startup**.
7. To detect a connected FlexControl tuning knob, click **Detect**. To release the knob, click **Close**.
8. To have AetherSDR detect the FlexControl knob automatically at launch, check **Auto-detect on startup**.
9. To reverse the tuning direction of the knob, check **Invert tuning direction**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Port** | Combo box | Selects the serial device from detected ports. |
| **Refresh** | Button | Rescans for available serial ports and repopulates the **Port** list. |
| **Path** | Field | Displays or overrides the device path for the selected port. |
| **Baud** | Combo box | Sets the baud rate for the serial connection. |
| **Data** | Combo box | Sets the number of data bits. |
| **Parity** | Combo box | Sets the parity mode. |
| **Stop** | Combo box | Sets the number of stop bits. |
| **DTR: Function** | Combo box | Assigns the logical function driven on the DTR pin. |
| **DTR: Polarity** | Combo box | Sets active-high or active-low polarity for DTR. |
| **RTS: Function** | Combo box | Assigns the logical function driven on the RTS pin. |
| **RTS: Polarity** | Combo box | Sets active-high or active-low polarity for RTS. |
| **Paddle Swap (swap dit/dah)** | Checkbox | Swaps the dit and dah inputs from the paddle. |
| **Auto-open serial port on startup** | Checkbox | Reopens the configured port each time AetherSDR launches. |
| **Detect** | Button | Attempts to detect a FlexControl tuning knob on the selected port. |
| **Close** | Button | Releases the FlexControl knob connection. |
| **Auto-detect on startup** | Checkbox | Automatically runs knob detection when AetherSDR starts. |
| **Invert tuning direction** | Checkbox | Reverses the direction of the FlexControl tuning knob. |

## Tips

- Use **Refresh** any time you plug in a USB serial adapter after the dialog is already open, so the new device appears in the **Port** list.
- If you use the FlexControl knob, enable **Auto-detect on startup** together with **Auto-open serial port on startup** so everything is ready without manual steps after each launch.

## Troubleshooting

- **Serial tab is not visible** — Your AetherSDR build does not include serial port support (`HAVE_SERIALPORT` was not enabled at build time). Obtain a build that includes this feature.
- **Port does not appear in the list** — Click **Refresh**. On Linux, confirm your user account has permission to access the device (typically by membership in the `dialout` group). On Windows, verify the device appears in Device Manager.
- **FlexControl knob not detected** — Confirm the correct port is selected and the port is open. Click **Detect** again. If the knob was connected after the dialog opened, click **Refresh** first.

## Related

- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)

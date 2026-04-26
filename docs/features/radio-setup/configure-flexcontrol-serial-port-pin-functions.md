# Configure FlexControl Serial Port Pin Functions

This page explains how to select a serial port for the FlexControl knob and assign signal functions to its hardware pins. You would do this to use a FlexControl tuning knob with AetherSDR over a serial connection, or to control PTT and keying lines through the serial port's DTR and RTS pins.

## Before you start

- The radio must be connected. The Serial tab is only available when AetherSDR is connected to a FLEX-8600.
- The serial port support must be compiled into your AetherSDR build (`HAVE_SERIALPORT`). If you do not see `Settings > FlexControl...` in the menu, your build does not include serial port support.
- The serial device must be physically attached and visible to the operating system before you open the dialog.

## Steps

1. Click `Settings > FlexControl...`. This opens the Radio Setup dialog directly on the Serial tab. Alternatively, open `Settings > Radio Setup...` and click the **Serial** tab.
2. In the **Port** combo box, select your serial device from the list. If the device does not appear, click **Refresh** to rescan. You can also type a path directly into the **Path** field.
3. Set the serial line parameters using the **Baud**, **Data**, **Parity**, and **Stop** combo boxes to match your hardware.
4. For each output pin you want to configure, locate the **DTR** or **RTS** row and set the **Function** combo box to the desired signal function, then set the **Polarity** combo box to the appropriate polarity.
5. If you are using a paddle with this serial port and need to swap dit and dah, check **Paddle Swap (swap dit/dah)**.
6. To have AetherSDR reopen this port automatically every time it starts, check **Auto-open serial port on startup**.
7. To detect an attached FlexControl tuning knob, click **Detect** in the FlexControl Tuning Knob section. To release the port, click **Close**.
8. To have the FlexControl knob detected automatically at startup, check **Auto-detect on startup**. To reverse the tuning direction, check **Invert tuning direction**.
9. Click **Close** in the dialog button bar when finished.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Port** | Combo box | Selects the serial device from the list of detected ports. |
| **Refresh** | Button | Rescans for available serial ports and updates the **Port** list. |
| **Path** | Field | Displays or overrides the path to the selected serial device. |
| **Baud** | Combo box | Sets the baud rate for the serial connection. |
| **Data** | Combo box | Sets the number of data bits. |
| **Parity** | Combo box | Sets the parity mode. |
| **Stop** | Combo box | Sets the number of stop bits. |
| **DTR: Function** | Combo box | Assigns the signal function carried by the DTR pin. |
| **DTR: Polarity** | Combo box | Sets active-high or active-low polarity for DTR. |
| **RTS: Function** | Combo box | Assigns the signal function carried by the RTS pin. |
| **RTS: Polarity** | Combo box | Sets active-high or active-low polarity for RTS. |
| **Paddle Swap (swap dit/dah)** | Checkbox | Swaps dit and dah inputs for the connected paddle. |
| **Auto-open serial port on startup** | Checkbox | Reopens this serial port automatically when AetherSDR launches. |
| **Detect** | Button | Detects an attached FlexControl tuning knob on the configured port. |
| **Close** | Button | Releases the FlexControl knob connection. |
| **Auto-detect on startup** | Checkbox | Automatically detects the FlexControl knob when AetherSDR starts. |
| **Invert tuning direction** | Checkbox | Reverses the direction of frequency change when turning the FlexControl knob. |

## Troubleshooting

- **The Serial tab does not appear in Radio Setup** — Your AetherSDR build does not include serial port support (`HAVE_SERIALPORT`). You also will not see `Settings > FlexControl...` in the menu. Obtain a build that includes this feature.
- **Your device does not appear in the Port list** — Click **Refresh**. If it still does not appear, confirm the device is plugged in and the OS has assigned it a port. On Linux, verify your user account has permission to access the device (typically membership in the `dialout` group).
- **Detect reports no FlexControl knob** — Confirm the baud rate and serial parameters match the FlexControl hardware requirements and that the correct port is selected before clicking **Detect**.

## Related

- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)

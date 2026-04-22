# Configure FlexControl Serial Port Pin Functions

This page explains how to assign functions to the DTR and RTS output pins — and configure the CTS and DSR input pins — on the serial port used by the FlexControl hardware interface. Use this when you need AetherSDR to drive PTT, keying, or other signals through a serial port's control lines.

## Before you start

- AetherSDR must be built with serial port support (`HAVE_SERIALPORT`). If the Serial tab is absent from Radio Setup, your build does not include this feature.
- The radio must be connected. Radio Setup requires an active radio connection.
- Know the device path of your serial port (for example, `/dev/ttyUSB0` on Linux or `COM3` on Windows).

## Steps

1. Open `Settings > FlexControl...`. This opens the Radio Setup dialog directly on the Serial tab. Alternatively, open `Settings > Radio Setup...` and click the **Serial** tab.
2. In the **Port** combo box, select your serial device from the list. Click **Refresh** to rescan if the port does not appear. You can also type the path directly into the **Path** field.
3. Set the serial line parameters using the **Baud**, **Data**, **Parity**, and **Stop** combo boxes to match your hardware.
4. Under the DTR row, set the **Function** combo box to the desired signal function for the DTR pin, then set the **Polarity** combo box to the correct polarity.
5. Under the RTS row, set the **Function** combo box to the desired signal function for the RTS pin, then set the **Polarity** combo box to the correct polarity.
6. If your paddle wiring reverses dit and dah, check **Paddle Swap (swap dit/dah)**.
7. If you want the port to open automatically every time AetherSDR starts, check **Auto-open serial port on startup**.
8. In the **FlexControl Tuning Knob** section, click **Detect** to detect the FlexControl knob on the selected port, or **Close** to release it.
9. If you want the FlexControl knob to be detected automatically at startup, check **Auto-detect on startup**. To reverse the tuning direction of the knob, check **Invert tuning direction**.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Port** / **Refresh** / **Path** | Combo box | Selects the serial device. Refresh rescans available ports. Path allows direct text entry. |
| **Baud** / **Data** / **Parity** / **Stop** | Combo boxes | Set the serial line parameters to match the connected hardware. |
| **DTR: Function** / **Polarity** | Combo boxes | Assigns the signal function and active polarity for the DTR output pin. |
| **RTS: Function** / **Polarity** | Combo boxes | Assigns the signal function and active polarity for the RTS output pin. |
| **Paddle Swap (swap dit/dah)** | Checkbox | Swaps dit and dah on the paddle input. |
| **Auto-open serial port on startup** | Checkbox | Reopens the configured serial port automatically when AetherSDR launches. |
| **FlexControl Tuning Knob: Detect** | Button | Attempts to detect a FlexControl knob on the currently selected port. |
| **FlexControl Tuning Knob: Close** | Button | Releases the FlexControl knob connection. |
| **Auto-detect on startup** | Checkbox | Automatically detects the FlexControl knob when AetherSDR starts. |
| **Invert tuning direction** | Checkbox | Reverses the direction of frequency tuning from the FlexControl knob. |

## Troubleshooting

- **Serial tab is missing from Radio Setup** — AetherSDR was not built with `HAVE_SERIALPORT`. Use a build that includes serial port support.
- **Port does not appear in the Port list** — Click **Refresh** to rescan. Confirm the device is physically connected and that your user account has permission to access the port (on Linux, this typically means membership in the `dialout` or `tty` group).
- **FlexControl knob is not detected** — Confirm the correct port is selected, then click **Detect** again. Check that no other application has the port open.

## Related

- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)
- [Radio Setup overview](overview.md)

# Configure FlexControl serial port pin functions

This page explains how to assign functions to the DTR and RTS output pins on a FlexControl serial port connection. Use these settings to drive external devices such as a CW keyer or PTT line from the serial port's control signals.

## Before you start

- AetherSDR must be built with serial port support (`HAVE_SERIALPORT`). If the Serial tab is not visible in Radio Setup, your build does not include this feature.
- The radio must be connected. Radio Setup requires an active radio connection.
- Know the device path of your serial port (for example, `/dev/ttyUSB0` on Linux or `COM3` on Windows).

## Steps

1. Open `Settings > FlexControl...`. This opens the Radio Setup dialog directly on the Serial tab. Alternatively, open `Settings > Radio Setup...` and click the **Serial** tab.
2. In the **Port** combo box, select your serial port device. Click **Refresh** if your port does not appear in the list, or type the path directly into the **Path** field.
3. Set **Baud**, **Data**, **Parity**, and **Stop** to match the device connected to the serial port.
4. Under the **DTR** row, open the **Function** combo box and select the function you want DTR to perform. Then set the **Polarity** combo box for that pin.
5. Under the **RTS** row, open the **Function** combo box and select the function you want RTS to perform. Then set the **Polarity** combo box for that pin.
6. If you are using a paddle and need to swap dit and dah, check **Paddle Swap (swap dit/dah)**.
7. To have AetherSDR open this serial port automatically each time it launches, check **Auto-open serial port on startup**.
8. If a FlexControl tuning knob is attached, click **Detect** to identify it. Click **Close** to release it. To detect the knob automatically at launch, check **Auto-detect on startup**. To reverse the tuning direction, check **Invert tuning direction**.

## What each control does

| Control | Kind | Behavior | Default | Valid range / notes |
|---|---|---|---|---|
| Port / Refresh / Path | Combo box | Selects or manually enters the serial device path. **Refresh** rescans available ports. | — | System-dependent |
| Baud / Data / Parity / Stop | Combo boxes | Serial line parameters. Must match the attached device. | — | — |
| DTR: Function | Combo box | Assigns the function driven on the DTR output pin. | — | Options populated from device capabilities |
| DTR: Polarity | Combo box | Sets active-high or active-low logic for DTR. | — | — |
| RTS: Function | Combo box | Assigns the function driven on the RTS output pin. | — | Options populated from device capabilities |
| RTS: Polarity | Combo box | Sets active-high or active-low logic for RTS. | — | — |
| Paddle Swap (swap dit/dah) | Checkbox | Swaps the dit and dah inputs for a connected paddle. | Unchecked | — |
| Auto-open serial port on startup | Checkbox | Reopens the configured port automatically when AetherSDR launches. | Unchecked | — |
| FlexControl Tuning Knob: Detect | Push button | Detects a FlexControl knob on the selected port. | — | — |
| FlexControl Tuning Knob: Close | Push button | Releases the FlexControl knob. | — | — |
| Auto-detect on startup | Checkbox | Detects the FlexControl knob automatically at launch. | — | — |
| Invert tuning direction | Checkbox | Reverses the direction of tuning knob rotation. | — | — |

## Troubleshooting

- **Serial tab is missing** — Your AetherSDR build does not include `HAVE_SERIALPORT`. Install or obtain a build that includes serial port support.
- **Port does not appear in the list** — Click **Refresh**. Confirm the device is plugged in and that your OS user account has permission to access the serial port (on Linux, the user typically needs to be in the `dialout` group).
- **Pin functions have no effect** — Confirm the **Polarity** setting matches what the attached device expects. Some devices require active-low logic.

## Related

- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)

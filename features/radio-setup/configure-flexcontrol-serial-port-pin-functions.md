# Configure FlexControl Serial Port Pin Functions

This page explains how to select a serial port for the FlexControl hardware interface and assign functions and polarity to the DTR and RTS output pins. Use these settings when connecting a FlexControl knob or a paddle via a serial adapter.

## Before you start

- AetherSDR must be built with serial port support. The Serial tab is only present when `HAVE_SERIALPORT` is enabled. If you do not see a Serial tab in Radio Setup, your build does not include this feature.
- A radio connection must be active. Radio Setup requires a connected radio.
- Know which serial device path corresponds to your FlexControl or serial adapter (for example, `/dev/ttyUSB0` on Linux).

## Steps

1. Open `Settings > FlexControl...`. This opens the Radio Setup dialog directly on the Serial tab. Alternatively, open `Settings > Radio Setup...` and click the Serial tab.
2. In the Port section, click the Port combo box and select your serial device from the list. If the device does not appear, click Refresh to rescan. To type a path directly, edit the Path field.
3. Set the serial line parameters using the Baud, Data, Parity, and Stop combo boxes to match your device.
4. Under the DTR row, open the Function combo box and select the function you want to assign to the DTR pin. Open the Polarity combo box and select the polarity.
5. Under the RTS row, open the Function combo box and select the function for the RTS pin. Open the Polarity combo box and select the polarity.
6. If you are connecting a CW paddle and need to swap dit and dah, check Paddle Swap (swap dit/dah).
7. To have AetherSDR open this port automatically each time it starts, check Auto-open serial port on startup.
8. In the FlexControl Tuning Knob section, click Detect to confirm the knob is recognized. Click Close to release it.
9. To have AetherSDR detect the tuning knob automatically at startup, check Auto-detect on startup. To reverse the tuning direction, check Invert tuning direction.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| Port / Refresh / Path | Combo box | Selects or manually specifies the serial device. Refresh rescans available ports. |
| Baud / Data / Parity / Stop | Combo boxes | Sets the serial line parameters to match the connected device. |
| DTR: Function / Polarity | Combo boxes | Assigns a signal function and active polarity to the DTR output pin. |
| RTS: Function / Polarity | Combo boxes | Assigns a signal function and active polarity to the RTS output pin. |
| Paddle Swap (swap dit/dah) | Checkbox | Reverses the dit and dah inputs from the connected paddle. |
| Auto-open serial port on startup | Checkbox | Reopens the configured port each time AetherSDR launches. |
| FlexControl Tuning Knob: Detect / Close | Buttons | Detect initiates recognition of the FlexControl knob. Close releases the connection to it. |
| Auto-detect on startup | Checkbox | Automatically detects the FlexControl knob when AetherSDR starts. |
| Invert tuning direction | Checkbox | Reverses the direction of the tuning knob. |

## Tips

- If you opened Radio Setup via `Settings > Radio Setup...` and the Serial tab is not visible, your AetherSDR build does not include `HAVE_SERIALPORT` support.
- On Linux, serial device paths are typically `/dev/ttyUSB0` or `/dev/ttyS0`. Your user account may need to be a member of the `dialout` group to access these devices.

## Troubleshooting

- **Serial tab is missing from Radio Setup** — The tab is only compiled in when `HAVE_SERIALPORT` is enabled. Use a build that includes serial port support.
- **Port list is empty** — No serial devices were found. Connect the device, then click Refresh to rescan.
- **FlexControl knob is not detected after clicking Detect** — Verify the correct port and baud rate are selected and that the device is physically connected. Click Refresh on the port list and try again.

## Related

- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)
- [Radio Setup overview](overview.md)

# Configure FlexControl Serial Port Pin Functions

Use this page to assign a function and polarity to the DTR and RTS output pins on the serial port connected to your FlexControl or other serial-attached device. This lets AetherSDR drive external hardware — such as PTT lines or keyer inputs — through the serial port's control signals.

## Before you start

- The radio must be connected. The Serial tab requires an active radio connection.
- The Serial tab is only present when AetherSDR was built with serial port support (`HAVE_SERIALPORT`). If you do not see a Serial tab or a `Settings > FlexControl...` menu item, your build does not include this feature.
- Know the device path of your serial port (for example, `/dev/ttyUSB0` on Linux or `COM3` on Windows).

## Steps

1. Open `Settings > FlexControl...` — this jumps directly to the Serial tab of Radio Setup. Alternatively, open `Settings > Radio Setup...` and click the **Serial** tab.
2. In the **Port** combo box, select your serial device from the list. Click **Refresh** to rescan if your device is not shown, or type the path directly into the **Path** field.
3. Set the serial line parameters using the **Baud**, **Data**, **Parity**, and **Stop** combo boxes to match your device's requirements.
4. For the **DTR** pin, select the desired function from the **DTR** function combo box, then select the active polarity from the adjacent **Polarity** combo box.
5. For the **RTS** pin, repeat the same two selections — function and polarity — using the **RTS** function and **Polarity** combo boxes.
6. If your paddle connections are reversed, check **Paddle Swap (swap dit/dah)**.
7. To have AetherSDR open this port automatically each time it starts, check **Auto-open serial port on startup**.
8. If you are connecting a FlexControl tuning knob, click **Detect** under **FlexControl Tuning Knob** to identify the device. Click **Close** to release it.
9. To have AetherSDR detect the FlexControl knob automatically on startup, check **Auto-detect on startup**. To reverse the tuning direction, check **Invert tuning direction**.

## What each control does

| Control | What it does | Default | Valid range / values |
|---|---|---|---|
| **Port** | Selects or enters the serial device path. | — | System serial ports |
| **Refresh** | Rescans for available serial ports. | — | — |
| **Path** | Editable field showing the selected port path. | — | Any valid device path |
| **Baud** | Serial baud rate. | — | Per combo box options |
| **Data** | Number of data bits. | — | Per combo box options |
| **Parity** | Parity setting. | — | Per combo box options |
| **Stop** | Number of stop bits. | — | Per combo box options |
| **DTR: Function** | Assigns a signal function to the DTR output pin. | — | Per combo box options |
| **DTR: Polarity** | Sets active-high or active-low polarity for DTR. | — | Per combo box options |
| **RTS: Function** | Assigns a signal function to the RTS output pin. | — | Per combo box options |
| **RTS: Polarity** | Sets active-high or active-low polarity for RTS. | — | Per combo box options |
| **Paddle Swap (swap dit/dah)** | Reverses dit and dah paddle inputs. | Unchecked | Checked / Unchecked |
| **Auto-open serial port on startup** | Reopens the configured port when AetherSDR launches. | Unchecked | Checked / Unchecked |
| **FlexControl Tuning Knob: Detect** | Detects a connected FlexControl knob. | — | — |
| **FlexControl Tuning Knob: Close** | Releases the FlexControl knob connection. | — | — |
| **Auto-detect on startup** | Automatically detects the FlexControl knob at launch. | Unchecked | Checked / Unchecked |
| **Invert tuning direction** | Reverses the direction of FlexControl tuning. | Unchecked | Checked / Unchecked |

## Frequency calibration changes in v0.9.2.1

The **RX** tab frequency calibration section has been revised. Previously, the **Cal Frequency (MHz)** field and **Start** button were only shown when no GPSDO was detected. Starting in v0.9.2.1, those controls are always visible regardless of whether a GPSDO is installed.

The status message at the top of the calibration group changes depending on hardware:

- GPSDO installed — shown in green: *GPSDO installed. Manual frequency offset calibration available.*
- No GPSDO — shown in amber: *Manual frequency offset calibration available.*

The **Start** button now provides inline status feedback next to the button. While a calibration is in progress the button is disabled and its label changes to **Busy**. The status label shows the current stage (for example, *Starting…*) and updates as the calibration proceeds. The button is re-enabled when the calibration completes or fails.

Before starting calibration, AetherSDR now resets the stored frequency error to zero (`radio set freq_error_ppb=0`) before sending `radio pll_start`. If the **Cal Frequency (MHz)** field is empty when you click **Start**, the status label shows *Enter cal frequency* in amber and the calibration does not start.

### Updated RX tab calibration controls

| Control | What it does | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. | Now always shown, with or without GPSDO. |
| **Start** | Starts the frequency calibration sweep. | Disabled and labelled **Busy** while active. Validates that a cal frequency has been entered before proceeding. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion. | Reset to 0 automatically when **Start** is clicked. |

## Tips

- If you open Radio Setup through `Settings > Radio Setup...` rather than `Settings > FlexControl...`, the Serial tab appears at the far right of the tab bar. Scroll or widen the dialog if the tab is not visible.
- The Serial tab is built lazily — it is not constructed until you first click it, so there is a brief pause the first time you select it.
- On the RX tab, if you have a GPSDO installed you can still run a manual calibration. Enter the reference frequency in **Cal Frequency (MHz)** and click **Start**.

## Troubleshooting

- **Serial tab is missing** — AetherSDR was built without `HAVE_SERIALPORT`. The `Settings > FlexControl...` menu item will also be absent. Use a build that includes serial port support.
- **Port does not appear in the list** — Click **Refresh** to rescan. On Linux, confirm your user account has read/write permission on the device node (typically the `dialout` or `uucp` group).
- **FlexControl knob is not detected** — Confirm the correct port is selected and the baud rate matches the FlexControl device. Click **Detect** again after verifying the connection.
- **Start button stays disabled after a calibration attempt** — Check that the **Cal Frequency (MHz)** field contains a valid frequency. An empty field prevents the calibration from starting and the button will not re-enable until you dismiss and reopen the dialog or the previous calibration completes.

## Related

- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)
- [Select iambic mode A or B for the radio keyer](select-iambic-mode-a-or-b-for-the-radio-keyer.md)
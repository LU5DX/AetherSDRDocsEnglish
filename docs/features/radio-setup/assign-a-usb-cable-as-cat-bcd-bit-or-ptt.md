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

| Control | Description | Notes |
|---|---|---|
| **Cables list / Status** | Lists all detected USB serial adapters with **Plugged** or **Unplugged** status. Select a cable here to edit its settings. | |
| **Name:** | User-visible label for the cable. | |
| **Enabled** | Activates the cable. The cable is inactive until enabled. | |
| **Speed** | Serial baud rate. | |
| **Data Bits** | Number of serial data bits. | |
| **Parity** | Serial parity: None, Even, Odd, etc. | |
| **Stop Bits** | Number of stop bits. | |
| **Flow** | Flow control method (None, Hardware, Software). | |
| **Source** | Selects the radio signal source that drives the cable output. | |
| **Auto Report** | When active, the radio reports state changes to the cable automatically. | |
| **BCD Type** | Selects the BCD band-data encoding format. Applies to BCD-type cables only. | |
| **Polarity** | Sets whether the output logic is active-high or active-low. | |
| **Bit Configuration (0–7)** | Maps individual output pins to specific functions. Applies to bit-type cables only. | |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. | Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. | |
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. | Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. | Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. | Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | |

## RX tab — frequency calibration (v0.9.2.1)

The **RX** tab now shows the frequency calibration controls regardless of whether a GPSDO is installed. In previous releases, the calibration fields were hidden when a GPSDO was detected.

- If a GPSDO is installed, a green status line reads "GPSDO installed. Manual frequency offset calibration available."
- If no GPSDO is installed, a yellow status line reads "Manual frequency offset calibration available."

In both cases the **Cal Frequency (MHz):**, **Start**, and **Freq Offset (ppb):** controls are always visible.

### Calibration procedure

1. Open `Settings > Radio Setup...` and click the **RX** tab.
2. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
3. Click **Start**. The button changes to **Busy** and is disabled while calibration runs. A status label to the right of the button shows progress text.
   - "Starting…" appears immediately.
   - The radio receives `radio set cal_freq=<value>` followed by `radio set freq_error_ppb=0`, then `radio pll_start` to begin the sweep.
   - If you leave the **Cal Frequency (MHz):** field empty and click **Start**, the status label shows "Enter cal frequency" in amber and the calibration does not start.
4. Wait for the status label to indicate completion. The **Start** button re-enables automatically.
5. Confirm or adjust the result using **Freq Offset (ppb):**.

### RX tab controls

| Control | Description | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for calibration, entered in MHz to six decimal places. | Sent to the radio as `radio set cal_freq=<value>`. |
| **Start** | Begins the calibration sweep. Disabled and labelled **Busy** while a calibration is in progress. | Resets `freq_error_ppb` to 0 before starting. Requires a non-empty cal frequency. |
| **Freq Offset (ppb):** | Manual frequency offset correction in parts per billion. | |
| **10 MHz Reference Source:** | Selects the oscillator reference: Auto, TCXO, GPSDO, or External. Available options depend on installed hardware. | Lock status (Locked / Unlocked) is shown alongside the selector and updates live. |

## Tips

- If a cable shows **Unplugged**, check the physical USB connection and reopen the dialog. The list reflects the state at the time the tab was built.
- Assign only one PTT cable at a time if you want predictable transmit keying behavior.
- BCD and bit cables share many of the same serial parameters; configure **Speed**, **Data Bits**, **Parity**, **Stop Bits**, and **Flow** to match the expectations of the external device receiving the data.
- When running frequency calibration, ensure the reference signal is stable and at the exact frequency entered before clicking **Start**. Clicking **Start** with an unstable or absent reference will produce an inaccurate offset correction.

## Troubleshooting

- **Cable shows Unplugged even though it is connected** — The USB adapter may not have been present when the tab loaded. Close Radio Setup, ensure the adapter is recognized by the OS, then reopen `Settings > USB Cables...`.
- **Enabled toggle has no effect** — Confirm the radio is connected. The USB Cables tab requires an active radio connection; controls do not send commands without it.
- **BCD or bit outputs are inverted** — Check the **Polarity** setting for the cable and toggle it to match your external device's logic levels.
- **Start button stays disabled after calibration** — If the connection to the radio drops during a calibration sweep, the button may remain in the Busy state. Close and reopen Radio Setup to reset the dialog.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)
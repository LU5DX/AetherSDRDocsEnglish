# Set per-band TX max power and tune mode

Use this page to cap transmit power on a per-band basis and choose how the Tune function behaves. These settings are stored on the radio and apply regardless of which client connects.

## Before you start

- AetherSDR must be connected to the radio. The TX tab is not accessible without an active connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. Click **TX Band Settings** to open the dedicated per-band power and tune dialog.
4. In the per-band table, locate the band you want to configure.
5. Adjust the power limit for that band as needed. The valid range for **Max Power:** is 0–100 %.
6. To change tune behavior, select the desired option from the **Tune Mode:** combo box.
7. Close the dialog when done. Settings are applied immediately to the radio.

## What each control does

| Control                                               | Kind          | Valid range / options                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TX Band Settings**                                  | Button        | —                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Max Power:**                                        | Spin box      | 0–100 %                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Tune Mode:**                                        | Combo box     | See radio firmware options                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Show TX in Waterfall:**                             | Toggle button | Enabled / Disabled                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **TX Follows Active Slice / Active Slice Follows TX** | Button pair   | Mutually exclusive                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TX Follows Active Slice                               | Button        | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation.                                                                                                                                                                                                                                                                                                                     |
| Active Slice Follows TX                               | Button        | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice.                                                                                                                                                                                                                                                                                                                       |
| Voice / CW / Digital filter sharpness sliders         | Slider        | 0–3. Sets filter sharpness (0 = lowest latency, 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`.                                                                                                                                                                                                                                                                    |
| Auto (Voice / CW / Digital)                           | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`.                                                                                                                                                                                                                                                                                    |
| Connect / Disconnect (TGXL)                           | Button        | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL)                           | Button        | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`.                                                                                                                                                                                                                                                                                                     |
| Connect / Disconnect (Antenna Genius)                 | Button        | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`.                                                                                                                                                                                                                                                                                                                      |

## Frequency calibration (RX tab)

The **RX** tab contains controls for manual frequency offset calibration and 10 MHz reference source selection. In v0.9.2.1 the calibration controls are always shown regardless of whether a GPSDO is installed. When a GPSDO is present, the status label reads "GPSDO installed. Manual frequency offset calibration available." (green). When no GPSDO is present, the label reads "Manual frequency offset calibration available." (amber).

### How to run a frequency calibration

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
4. Click **Start**.
   - The button label changes to **Busy** and becomes disabled while calibration runs.
   - The status field to the right of the button shows progress text ("Starting…" then live state).
   - Before starting, AetherSDR resets the frequency error to zero (`radio set freq_error_ppb=0`) and then issues `radio pll_start`.
   - If you leave **Cal Frequency (MHz):** empty and click **Start**, the status field shows "Enter cal frequency" and the calibration does not proceed.
5. When calibration completes, the button re-enables and the status field shows the result.
6. If you need to set an offset manually, enter a value in **Freq Offset (ppb):**.

### Calibration controls

| Control                    | Kind      | Notes                                                                                                       |
|----------------------------|-----------|-------------------------------------------------------------------------------------------------------------|
| **Cal Frequency (MHz):**   | Spin box  | Frequency used for calibration. Must not be empty before clicking **Start**.                                |
| **Start**                  | Button    | Begins calibration. Resets `freq_error_ppb` to 0, then issues `radio pll_start`. Disabled while busy.      |
| **Freq Offset (ppb):**     | Spin box  | Manual frequency offset in parts per billion.                                                               |
| **10 MHz Reference Source:** | Combo box | Auto / TCXO / GPSDO / External. Options shown depend on installed hardware. Lock status updates live.     |

## Tips

- **TX Band Settings** is also accessible directly from `Settings > TX Band Settings...` without opening Radio Setup first.
- The **Max Power:** spin box on the TX tab sets a radio-level cap. Per-band limits set inside **TX Band Settings** operate on top of this cap.
- When running frequency calibration, ensure no other station is transmitting on the reference frequency before clicking **Start**.

## Related

- [Radio Setup overview](overview.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
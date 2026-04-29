# Select iambic mode A or B for the radio keyer

Choose between Curtis iambic mode A and mode B for the FLEX-8600's built-in keyer. The setting applies to both the radio hardware keyer and AetherSDR's local software keyer, which mirrors the radio's state for low-latency sidetone.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW tab is unavailable when no radio is connected.
- A paddle must be wired to the radio's key jack for the iambic keyer to function.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Phone/CW** tab.
3. Confirm that **Iambic:** is set to **Enabled**. If it reads **Disabled**, click it once to enable the iambic keyer.
4. Click **A** or **B** to select the desired Curtis iambic mode.

## What each control does

| Control                                       | Kind                                                                                                                                                                    | Default                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Iambic:**                                   | Toggle button                                                                                                                                                           | —                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Iambic Mode: A / B**                        | Push button (mutually exclusive pair)                                                                                                                                   | A                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Swap:**                                     | Toggle button                                                                                                                                                           | —                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TX Follows Active Slice                       | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'.                                                                                         | Disabled automatically during Split operation.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Active Slice Follows TX                       | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'.                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Voice / CW / Digital filter sharpness sliders | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled.                                                               | Commands sent as 'radio filter_sharpness \<mode> level=\<N>'.                                                                                                                                                                                                                                                                                                                                                                                   |
| Auto (Voice / CW / Digital)                   | Enables automatic filter-level selection for that mode; disables the manual sharpness slider.                                                                           | Commands sent as 'radio filter_sharpness \<mode> auto_level=1'.                                                                                                                                                                                                                                                                                                                                                                                 |
| Connect / Disconnect (TGXL)                   | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to TGXL_ManualIp and TGXL_ManualPort on connect so AetherSDR auto-reconnects on startup. | Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL (TgxlConnection::requestAutotune()) instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If IP field is empty and radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL)                   | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to PGXL_ManualIp and PGXL_ManualPort.                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Connect / Disconnect (Antenna Genius)         | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to AG_ManualIp and AG_ManualPort.                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Frequency calibration (RX tab)

In v0.9.2.1 the RX tab frequency calibration controls are available regardless of whether a GPSDO is installed. Previously, the **Cal Frequency (MHz):**, **Start**, and **Freq Offset (ppb):** controls were hidden when a GPSDO was detected. The status label at the top of the group now reads:

- **GPSDO installed. Manual frequency offset calibration available.** (green) — GPSDO present.
- **Manual frequency offset calibration available.** (amber) — no GPSDO.

### Using frequency calibration

1. Click `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
4. Click **Start**.
   - The button label changes to **Busy** and becomes disabled while calibration is in progress.
   - A status label beside the button reports progress (Starting… and subsequent states).
   - AetherSDR resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`) before starting the sweep.
5. When calibration completes the button re-enables and the status label updates with the result.
6. If the **Cal Frequency (MHz):** field is empty when you click **Start**, the status label shows **Enter cal frequency** and calibration does not begin.

### Calibration controls

| Control                 | Kind    | Default | Behavior                                                                                               |
|-------------------------|---------|---------|--------------------------------------------------------------------------------------------------------|
| **Cal Frequency (MHz):** | Spinbox | —       | Frequency used for calibration. Must not be empty before clicking Start.                               |
| **Start**               | Button  | —       | Resets frequency error to 0 ppb, then starts the calibration sweep. Disabled and labelled Busy during an active calibration. |
| **Freq Offset (ppb):**  | Spinbox | —       | Manual frequency offset in parts per billion. Applied directly without running a sweep.                |

## Tips

- Mode A (Curtis A) releases the last element when both paddles are released mid-squeeze. Mode B (Curtis B) completes the last element before stopping. Choose based on your sending style.
- The local software keyer mirrors whichever mode you select here, providing sub-5 ms sidetone response independent of network latency.
- When a GPSDO is installed, the frequency error correction the GPSDO provides is independent of the manual calibration controls. You can still use manual calibration to verify or trim the offset.

## Related

- [Radio Setup overview](overview.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)
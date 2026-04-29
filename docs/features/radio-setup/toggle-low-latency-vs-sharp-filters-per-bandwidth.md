# Toggle low-latency vs sharp filters per bandwidth

The Filters tab in Radio Setup lets you choose between low-latency and sharp DSP filters for each receive bandwidth, and optionally force low-latency filters when using digital modes.

## Before you start

- AetherSDR must be connected to the radio. The Filters tab is only available when a radio connection is active.
- Open Radio Setup via `Settings > Radio Setup...`.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Filters** tab.
3. Click the **Low Latency / Sharp Filters** toggle button to switch between the two filter families for the current bandwidth. The button reflects the active selection.
4. To force low-latency filters whenever a digital mode (DIGU or DIGL) is active, check **Use Low Latency Filters for Digital Modes**.
5. Close the dialog. Settings take effect immediately.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Low Latency / Sharp Filters** | Toggle button | Switches the filter-family preference between low-latency and sharp filters for the selected bandwidth. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | When checked, overrides the per-bandwidth filter choice and uses low-latency filters whenever a DIGU or DIGL slice is active. |
| Voice / CW / Digital filter sharpness sliders | Slider | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode. The slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| Auto (Voice / CW / Digital) | Toggle button | Enables automatic filter-level selection for that mode and disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| TX Follows Active Slice | Push button | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | Switches the active slice when TX moves externally (for example WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. |
| Connect / Disconnect (TGXL) | Push button | Opens or closes a direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Push button | Opens or closes a direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Connect / Disconnect (Antenna Genius) | Push button | Opens or closes a connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |

## Frequency calibration (RX tab)

In v0.9.2.1 the frequency calibration controls on the **RX** tab are available regardless of whether a GPSDO is installed. Previously, the Cal Frequency and Start controls were hidden when a GPSDO was detected.

- When a GPSDO is installed, the status label reads "GPSDO installed. Manual frequency offset calibration available." in green.
- When no GPSDO is installed, the status label reads "Manual frequency offset calibration available." in amber.

### Calibration procedure

1. Click `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz)**.
4. Click **Start**. AetherSDR resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`), sets the calibration frequency, and starts the PLL calibration sweep. The status field beside the Start button updates as the calibration progresses.
5. While calibration is running, the **Start** button is disabled and shows "Busy". It re-enables when calibration completes or fails.
6. Adjust **Freq Offset (ppb)** manually if needed after calibration completes.

### Calibration controls

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz)** | Spinbox | Frequency used for calibration. Must not be empty before clicking Start. |
| **Start** | Push button | Resets the frequency error to 0 ppb, applies the calibration frequency, and starts the PLL calibration sweep. Disabled and labelled "Busy" while a calibration is in progress. |
| **Freq Offset (ppb)** | Spinbox | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source** | Combo box | Selects oscillator reference: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

## Tips

- Low-latency filters reduce processing delay, which benefits real-time digital mode decoding and CW. Sharp filters provide steeper skirt selectivity, which is more useful for crowded SSB conditions.
- The **Use Low Latency Filters for Digital Modes** checkbox applies across all bandwidths, so you do not need to toggle the per-bandwidth setting each time you switch to a digital mode.
- If **Start** does not become active after entering a calibration frequency, check that the Cal Frequency field is not empty.

## Related

- [Radio Setup overview](overview.md)
- [Select iambic mode A or B for the radio keyer](select-iambic-mode-a-or-b-for-the-radio-keyer.md)
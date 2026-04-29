# Check Radio Serial, Hardware Version, Region and Options

The Radio tab in Radio Setup shows identifying information reported directly by the radio — serial number, hardware version, regulatory region, and licensed options. Use this page to verify what hardware and options your radio has before troubleshooting or contacting support.

## Before you start

- AetherSDR must be connected to the radio. The Radio tab fields are populated from live radio data.

## Steps

1. Click `Settings > Radio Setup...`.
2. The dialog opens on the **Radio** tab by default.
3. Read the values in the **Radio Information** group:
   - **Radio SN** — the chassis serial number.
   - **HW Version** — the hardware version string reported by the radio.
   - **Region** — the radio's regulatory region (defaults to `USA` if the radio does not report one).
   - **Options** — the licensed options active on this radio (for example, `GPS`, `PGXL`).

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Radio SN | Indicator (read-only) | Chassis serial number as reported by the radio. |
| HW Version | Indicator (read-only) | Hardware version string prefixed with `v`. |
| Region | Indicator (read-only) | Regulatory region. Displays `USA` if the radio reports none. |
| Options | Indicator (read-only) | Licensed radio options. |
| TX Follows Active Slice | Push button | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. |
| Voice / CW / Digital filter sharpness sliders | Slider | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| Auto (Voice / CW / Digital) | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| Connect / Disconnect (TGXL) | Push button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Push button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Connect / Disconnect (Antenna Genius) | Push button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |

All four Radio Information fields are read-only. No persisted settings keys are associated with them.

## RX tab — frequency calibration

In v0.9.2.1 the calibration controls in the **RX** tab are always visible regardless of whether a GPSDO is installed. Previously, the Cal Frequency, Start, and Freq Offset fields were hidden when a GPSDO was detected. The status banner at the top of the group now reads:

- **GPSDO installed** — "GPSDO installed. Manual frequency offset calibration available." (green text)
- **No GPSDO** — "Manual frequency offset calibration available." (amber text)

The following controls are now available in both configurations:

| Label | Kind | Behavior |
|---|---|---|
| Cal Frequency (MHz): | Spinbox | Frequency used for calibration. Enter the known reference frequency before clicking Start. |
| Start | Push button | Starts the frequency calibration sequence. The button is disabled and its label changes to **Busy** while calibration is in progress. Before triggering the PLL sweep, AetherSDR resets the radio's frequency error to zero (`radio set freq_error_ppb=0`) and then issues `radio pll_start`. If the Cal Frequency field is empty, the button shows a warning and takes no action. |
| Freq Offset (ppb): | Spinbox | Manual frequency offset in parts per billion, applied after calibration completes or set directly for manual correction. |

A status label appears to the right of the Start button and updates throughout the calibration sequence:

| State | Text | Color |
|---|---|---|
| Idle | *(empty)* | — |
| Cal frequency not entered | "Enter cal frequency" | Amber |
| Sequence started | "Starting…" | Grey-blue |
| In progress | Updated as PLL state is reported by the radio | Grey-blue |

The Start button is re-enabled and its label reverts to **Start** when the calibration sequence completes or fails.

## Tips

- If **Radio SN** is blank, the radio has not yet sent its chassis serial. Disconnect and reconnect to the radio.
- **Options** reflects what the radio itself reports. If you have recently purchased a license upgrade, power-cycle the radio and reconnect so it fetches the updated options.
- When running calibration, ensure the reference signal is present at the antenna input and that **Cal Frequency (MHz)** exactly matches the reference transmitter's frequency before clicking **Start**.

## Related

- [Radio Setup overview](overview.md)
- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
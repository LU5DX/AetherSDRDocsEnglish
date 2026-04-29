# Upload a New Firmware .ssdr to the Radio

This page explains how to load a firmware image file onto your FLEX-8600 using the Radio Setup dialog. You would do this to update the radio to a specific firmware version without using the automatic update check.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) will not populate correctly without a live connection.
- Obtain the `.ssdr` firmware file from FlexRadio and note where it is saved on your computer.
- Do not transmit during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Browse .ssdr...** to open a file chooser.
4. Navigate to the `.ssdr` file on your computer, select it, and confirm.
5. Click **Upload Firmware**.
6. Watch the progress bar and status text below the button. Wait until the status indicates the upload is complete before doing anything else.
7. Reboot the radio as directed by the firmware release notes to apply the new firmware.

## What each control does

| Control                                       | Kind                                                                                                                                                                    | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Check for Update**                          | Button                                                                                                                                                                  | Queries for available firmware updates automatically. Use this instead of **Browse .ssdr...** if you want AetherSDR to find the update for you.                                                                                                                                                                                                                                                                                                 |
| **Browse .ssdr...**                           | Button                                                                                                                                                                  | Opens a file dialog to select a local `.ssdr` firmware image.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Upload Firmware**                           | Button                                                                                                                                                                  | Starts the upload using the file selected with **Browse .ssdr...**. A progress bar and status text appear below and update as the transfer proceeds.                                                                                                                                                                                                                                                                                            |
| TX Follows Active Slice                       | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'.                                                                                         | Disabled automatically during Split operation.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Active Slice Follows TX                       | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'.                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Voice / CW / Digital filter sharpness sliders | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled.                                                               | Commands sent as 'radio filter_sharpness <mode> level=<N>'.                                                                                                                                                                                                                                                                                                                                                                                     |
| Auto (Voice / CW / Digital)                   | Enables automatic filter-level selection for that mode; disables the manual sharpness slider.                                                                           | Commands sent as 'radio filter_sharpness <mode> auto_level=1'.                                                                                                                                                                                                                                                                                                                                                                                  |
| Connect / Disconnect (TGXL)                   | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to TGXL_ManualIp and TGXL_ManualPort on connect so AetherSDR auto-reconnects on startup. | Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL (TgxlConnection::requestAutotune()) instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If IP field is empty and radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL)                   | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to PGXL_ManualIp and PGXL_ManualPort.                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Connect / Disconnect (Antenna Genius)         | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to AG_ManualIp and AG_ManualPort.                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## Frequency calibration (RX tab)

The RX tab shows calibration controls regardless of whether a GPSDO is installed. The status label at the top of the tab changes wording and color depending on the hardware present:

- **GPSDO installed** — label reads "GPSDO installed. Manual frequency offset calibration available." in green. You can still run a manual calibration if needed.
- **No GPSDO** — label reads "Manual frequency offset calibration available." in amber.

In both cases the **Cal Frequency (MHz)** field and the **Start** button are always visible and active. Prior to v0.9.2.1, the calibration controls were hidden when a GPSDO was detected.

### Using the Start button

The **Start** button now provides inline status feedback directly in the RX tab rather than relying solely on the radio's response. When you click **Start**:

1. AetherSDR validates that the **Cal Frequency (MHz)** field is not empty. If it is empty, the status label shows "Enter cal frequency" in amber and the calibration does not proceed.
2. The button text changes to **Busy** and the button is disabled until the calibration command sequence completes.
3. AetherSDR sends `radio set cal_freq=<value>` followed by `radio set freq_error_ppb=0` to reset any prior offset, then issues `radio pll_start` to begin the calibration sweep.
4. The inline status label beside the button updates as the calibration progresses.
5. When the sequence finishes (or fails), the button re-enables and reverts to **Start**.

The calibration activity is logged to the protocol log at debug level, including the cal frequency value, the ppb reset, and an internal run identifier that helps correlate log entries when multiple calibration attempts are made in the same session.

### Cal frequency controls

| Control                | Kind    | Behavior                                                                                          |
|------------------------|---------|---------------------------------------------------------------------------------------------------|
| **Cal Frequency (MHz)** | Field   | Enter the known reference frequency in MHz (six decimal places). Sent as `radio set cal_freq=<value>` when you leave the field or click **Start**. |
| **Start**              | Button  | Resets the frequency error to 0 ppb, then starts the calibration sweep. Disabled and labeled **Busy** while a sweep is running. |
| **Freq Offset (ppb)**  | Spinbox | Manual frequency offset in parts per billion. Adjust after calibration if fine-trimming is needed. |

## Tips

- If you only want to check whether a newer version exists rather than uploading a specific file, use **Check for Update** instead of the manual browse-and-upload workflow.
- The firmware status area is empty until an upload begins. If you see no progress bar after clicking **Upload Firmware**, confirm that a file was selected with **Browse .ssdr...** first.
- If **Start** shows "Enter cal frequency" in amber, type a frequency value in the **Cal Frequency (MHz)** field before clicking **Start** again.
- Even with a GPSDO installed, you can run a manual calibration pass if you need to verify or override the automatic correction.

## Troubleshooting

- **Upload Firmware does nothing** — No `.ssdr` file has been selected. Click **Browse .ssdr...** first, select the file, then click **Upload Firmware**.
- **Radio tab controls are unpopulated or grayed out** — AetherSDR is not connected to the radio. Establish a connection via `Settings > Connect to Radio...` before opening Radio Setup.
- **Start button stays labeled Busy** — The radio did not respond to the `radio pll_start` command. Check the protocol log for the relevant run identifier, verify the radio is connected and not transmitting, then try again.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
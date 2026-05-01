# Upload a New Firmware File to the Radio

This page explains how to load a firmware image onto your FLEX-8600 using the Radio Setup dialog. You would do this to update the radio to a specific firmware version without using the automatic update check.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) will not populate correctly without a live connection.
- Download the SmartSDR installer from flexradio.com and note where it is saved on your computer. AetherSDR accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file.
- Do not transmit during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Select Installer...** to open a file chooser.
4. Navigate to the installer or firmware file on your computer, select it, and confirm. AetherSDR auto-detects the format from the file header and extracts the `.ssdr` if needed. A status message appears while the firmware is being prepared.
5. When the status indicates the firmware is ready, click **Upload Firmware**.
6. Watch the progress bar and status text below the button. Wait until the status indicates the upload is complete before doing anything else.
7. Reboot the radio as directed by the firmware release notes to apply the new firmware.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Check for Update** | Button | Queries for available firmware updates. If an update is found, the status area shows the available version and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it. |
| **Select Installer...** | Button | Opens a file dialog that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. A status message is shown while the file is being prepared. Renamed from **Browse .ssdr...** in v0.9.3. |
| **Upload Firmware** | Button | Starts the upload using the file staged by **Select Installer...**. A progress bar and status text appear below and update as the transfer proceeds. |
| TX Follows Active Slice | Button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| Active Slice Follows TX | Button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| Voice / CW / Digital filter sharpness sliders | Slider | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| Auto (Voice / CW / Digital) | Toggle | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| Connect / Disconnect (TGXL) | Button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has already discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Connect / Disconnect (Antenna Genius) | Button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows a Connected status only when the connected device is a genuine Antenna Genius (not a ShackSwitch). |
| Connect / Disconnect (ShackSwitch) | Button | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the 'ShackSwitch' field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from Connected status if Antenna Genius (non-ShackSwitch) is the connected device. |
| ⚙ Web UI (ShackSwitch) | Button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. |
| APD (tab) | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| ANT1 / ANT2 / XVTA / XVTB sampler combos (APD) | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. |
| Equalizer Reset (APD) | Button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| Themes (tab) | Tab | UI customization tab — currently hosts the Slice Colors section. |
| Use Aether defaults / Custom colors | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. |
| Slice A–H color buttons | Button | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. |
| Reset All to Defaults (Themes) | Button | Resets all custom slice colors to the built-in AetherSDR palette. |

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

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz)** | Field | Enter the known reference frequency in MHz (six decimal places). Sent as `radio set cal_freq=<value>` when you leave the field or click **Start**. |
| **Start** | Button | Resets the frequency error to 0 ppb, then starts the calibration sweep. Disabled and labeled **Busy** while a sweep is running. |
| **Freq Offset (ppb)** | Spinbox | Manual frequency offset in parts per billion. Adjust after calibration if fine-trimming is needed. |

## Tips

- If you only want to check whether a newer version exists rather than uploading a specific file, use **Check for Update** first. The status area will tell you the available version and direct you to download the installer from flexradio.com.
- **Select Installer...** accepts `.msi`, `.exe`, and `.ssdr` files. You do not need to extract a `.ssdr` from an installer manually — AetherSDR handles that automatically.
- The firmware status area is empty until a file is staged or an upload begins. If you see no progress bar after clicking **Upload Firmware**, confirm that a file was successfully staged with **Select Installer...** first.
- If **Start** shows "Enter cal frequency" in amber, type a frequency value in the **Cal Frequency (MHz)** field before clicking **Start** again.
- Even with a GPSDO installed, you can run a manual calibration pass if you need to verify or override the automatic correction.
- To open the ShackSwitch web interface, click **⚙ Web UI** in the ShackSwitch row of the Peripherals tab. If the device has not yet been connected, enter its IP address in the `SS_ManualIp` field first.

## Troubleshooting

- **Upload Firmware does nothing** — No firmware file has been staged. Click **Select Installer...**, select the `.msi`, `.exe`, or `.ssdr` file, wait for the status message to confirm the file is ready, then click **Upload Firmware**.
- **Radio tab controls are unpopulated or grayed out** — AetherSDR is not connected to the radio. Establish a connection via `Settings > Connect to Radio...` before opening Radio Setup.
- **Start button stays labeled Busy** — The radio did not respond to the `radio pll_start` command. Check the protocol log for the relevant run identifier, verify the radio is connected and not transmitting, then try again.
- **APD tab is not visible** — The connected radio does not report `apd configurable=1`. The APD tab is only available on FLEX-8x00 series radios running SmartSDR 4.2.18 or later firmware.
- **⚙ Web UI opens the wrong address or does nothing** — Verify that `SS_ManualIp` contains the correct IP for the ShackSwitch. If the beacon advertises a `webPort` of 1024 or below, AetherSDR falls back to `SS_WebPort` or port 5000. Set `SS_WebPort` in settings if your device uses a non-default web port.
- **Antenna Genius row shows no Connected
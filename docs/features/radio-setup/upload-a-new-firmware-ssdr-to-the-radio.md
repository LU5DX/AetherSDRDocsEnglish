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

### 10 MHz Reference Source

The **10 MHz Reference Source:** combo box selects the oscillator reference used by the radio. In v0.9.7 the combo and its status label were updated with the following behavior:

- The combo is populated dynamically based on hardware reported by the radio. **Auto** is always present. **TCXO** appears when the radio reports `tcxoPresent` or when the current setting or active state is TCXO. **GPSDO** appears when `gpsdoPresent` is reported or the current setting or state is GPSDO. **External 10 MHz** appears when `extPresent` is reported, when oscillator status has been received from the radio, or when the current setting or state is External.
- The value `ext` reported by the radio is normalized to `external` internally before display, so the combo always shows **External 10 MHz** rather than a raw `ext` string.
- The status label beside the combo reflects both the configured setting and the radio's active oscillator state:
  - When **Auto** is selected and the radio has resolved to a specific source, the label reads, for example, `Auto -> GPSDO`.
  - When a specific source is selected but the radio is actively using a different one, the label reads, for example, `TCXO -> GPSDO`.
  - Otherwise the label shows the active source name only.
  - The label appends **Locked** (green) or **Unlocked** (red) to reflect lock state. If the active source is External and the radio reports no external signal is present, the label also appends **(not detected)**.
  - While the radio has not yet reported oscillator status, the label reads `Waiting for oscillator status` in blue-grey.

| Control | Kind | Behavior |
|---|---|---|
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference source. Options shown depend on hardware installed and live radio state. Sends `radio oscillator <value>` when changed. Valid values: `auto`, `tcxo`, `gpsdo`, `external`. |
| Oscillator status label | Indicator | Shows the resolved source, lock state, and (for External) whether a signal is detected. Updates live as the radio reports changes. |

## Tips

- If you only want to check whether a newer version exists rather than uploading a specific file, use **Check for Update** first. The status area will tell you the available version and direct you to download the installer from flexradio.com.
- **Select Installer...** accepts `.msi`, `.exe`, and `.ssdr` files. You do not need to extract
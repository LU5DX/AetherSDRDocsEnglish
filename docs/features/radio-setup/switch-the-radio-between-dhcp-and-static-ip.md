# Switch the Radio Between DHCP and Static IP

Use this page to change how the FLEX-8600 obtains its network address — either automatically via DHCP or with a fixed static IP, subnet mask, and gateway you specify.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available when a radio connection is active.
- If you are switching to static IP, have the IP address, subnet mask, and gateway values ready before you begin.
- Changing the network configuration will cause the radio to move to a new address. You will need to reconnect after applying.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Network** tab.
3. Note the current **IP Address**, **Mask**, and **MAC Address** shown as read-only indicators.
4. Click the **DHCP / Static** toggle button to switch modes. The button reflects the current mode; clicking it switches to the other.
5. If you selected static mode, fill in the **IP Address:**, **Mask:**, and **Gateway:** text fields with the values for your network.
6. Click **Apply** to push the network configuration to the radio.
7. Reconnect to the radio at its new address using `Settings > Connect to Radio...`.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicators (read-only) | Displays the radio's current network addresses. |
| **DHCP / Static** | Toggle button | Switches the radio between DHCP and static IP modes. |
| **IP Address:** | Text field | Static IP address to assign to the radio. Active only in static mode. |
| **Mask:** | Text field | Subnet mask for the static configuration. Active only in static mode. |
| **Gateway:** | Text field | Default gateway for the static configuration. Active only in static mode. |
| **Apply** | Push button | Sends the network configuration to the radio. |
| **TX Follows Active Slice** | Push button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| **Voice / CW / Digital filter sharpness sliders** | Sliders (0–3) | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Push button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Push button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Push button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |
| **Select Installer...** | Push button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v0.9.3. |
| **APD (tab)** | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. |
| **Equalizer Reset (APD)** | Push button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| **Themes (tab)** | Tab | UI customization tab — currently hosts the Slice Colors section. |
| **Use Aether defaults / Custom colors** | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. |
| **Slice A–H color buttons** | Push buttons | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. |
| **Reset All to Defaults (Themes)** | Push button | Resets all custom slice colors to the built-in AetherSDR palette. |

## Firmware update (Radio tab)

The **Radio** tab includes controls to check for firmware updates and stage a firmware file for upload.

### How to update firmware in v0.9.3

1. Click **Check for Update**. AetherSDR queries the FlexRadio update server. If an update is available, the status label shows the version number and instructs you to download the SmartSDR installer from flexradio.com.
2. Download the SmartSDR installer from flexradio.com (`.msi` for v4.2+, `.exe` for older releases).
3. Click **Select Installer...** to open the file picker. Select the installer you downloaded, or a pre-extracted `.ssdr` file if you already have one. The stager detects the file format automatically and extracts the firmware without external tools. The status label updates to show preparation progress.
4. When staging is complete, click **Upload Firmware** to transfer the firmware to the radio. A progress bar and status label track the upload.

> **Note:** In v0.9.3 the button formerly labeled **Browse .ssdr...** was renamed to **Select Installer...** and the file picker now accepts `.msi`, `.exe`, and `.ssdr` files. The **Check for Update** button no longer switches to a download button when an update is found; you download the installer manually from flexradio.com and stage it locally.

### Firmware tab controls

| Control | Kind | Behavior |
|---|---|---|
| **Radio SN** | Indicator (read-only) | Chassis serial number. |
| **Model** | Indicator (read-only) | Radio model. |
| **HW Version** | Indicator (read-only) | Hardware version string. |
| **Region** | Indicator (read-only) | Radio regulatory region. |
| **Options** | Indicator (read-only) | Shows licensed radio options. |
| **FlexControl** | Indicator (read-only) | Detected state of FlexControl hardware. |
| **multiFLEX** | Indicator (read-only) | multiFLEX enabled state. |
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field (`StationName`) | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if left empty. Sent to the radio as `client station <name>`. |
| **License Info** | Indicator (read-only) | Displays subscription, expiration, Radio ID, and licensed version from the radio. |
| **Remote On** | Push button | Enables remote wake / remote-on. |
| **Check for Update** | Push button | Queries the FlexRadio update server for available firmware. If an update is available, the status label shows the version and directs you to download the installer manually. |
| **Select Installer...** | Push button | Opens a file picker accepting `.msi`, `.exe`, or `.ssdr` files. The stager auto-detects the format and extracts the firmware. |
| **Upload Firmware** | Push button | Starts the firmware upload to the radio with a progress bar and status label. |

## Frequency calibration (RX tab)

The **RX** tab provides manual frequency offset calibration and 10 MHz reference source selection. In v0.9.2.1 the calibration controls are always shown regardless of whether a GPSDO is installed. A status label at the top of the group indicates the GPSDO state:

- **GPSDO installed** — label shown in green: *GPSDO installed. Manual frequency offset calibration available.*
- **No GPSDO** — label shown in amber: *Manual frequency offset calibration available.*

### Calibration controls

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz):** | Spinbox / text field | Frequency used for calibration. Must not be empty before starting. |
| **Start** | Push button | Starts the frequency calibration sequence. Sets `cal_freq`, resets `freq_error_ppb` to 0, then triggers the radio PLL calibration. The button is disabled and shows **Busy** while calibration is running. A status label beside the button reports progress (Starting… / running / result). |
| **Freq Offset (ppb):** | Spinbox | Manual frequency offset in parts per billion. Set to 0 automatically at the start of a calibration run. |
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference source: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. Live lock status (Locked / Unlocked) is displayed alongside the combo. |

### How calibration works in v0.9.2.1

1. Enter the known reference frequency in **Cal Frequency (MHz):**.
2. Click **Start**. AetherSDR sends `radio set cal_freq=<value>` and `radio set freq_error_ppb=0` to the radio, then issues `radio pll_start` to begin the sweep.
3. The **Start** button is disabled and labeled **Busy** until the sequence completes or fails.
4. The status label beside the button updates in real time. When calibration finishes the button re-enables and the label shows the result.

If the **Cal Frequency (MHz):** field is empty when you click **Start**, the status label shows *Enter cal frequency* in amber and calibration does not start.

> **Note:** Prior to v0.9.2.1, the calibration controls were hidden when a GPSDO was detected. They are now always available.

## Tips

- The **IP Address / Mask / MAC Address** indicators show what the radio is currently using. Record
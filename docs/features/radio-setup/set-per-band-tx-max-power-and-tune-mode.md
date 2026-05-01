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

| Control | Kind | Valid range / options |
|---|---|---|
| **TX Band Settings** | Button | — |
| **Max Power:** | Spin box | 0–100 % |
| **Tune Mode:** | Combo box | See radio firmware options |
| **Show TX in Waterfall:** | Toggle button | Enabled / Disabled |
| **TX Follows Active Slice** | Button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| Voice / CW / Digital filter sharpness sliders | Slider | 0–3. Sets filter sharpness (0 = lowest latency, 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| Auto (Voice / CW / Digital) | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows a Connected status only when the connected device is an Antenna Genius (non-ShackSwitch). If a ShackSwitch is the connected device, this row is hidden from Connected status. |
| **Connect / Disconnect (ShackSwitch)** | Button | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon. Auto-discovery via UDP also works without manually entering an IP. Row shows Connected status only when the connected device is a ShackSwitch. |
| **⚙ Web UI (ShackSwitch)** | Button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. |
| **Select Installer...** | Button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v0.9.3. |
| **APD** (tab) | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| ANT1 / ANT2 / XVTA / XVTB sampler combos (APD) | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. Default: INTERNAL. |
| **Equalizer Reset (APD)** | Button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| **Themes** (tab) | Tab | UI customization tab — currently hosts the Slice Colors section. |
| Use Aether defaults / Custom colors | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. |
| Slice A–H color buttons | Button | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. |
| **Reset All to Defaults (Themes)** | Button | Resets all custom slice colors to the built-in AetherSDR palette. |

## Connecting peripheral devices (Peripherals tab)

The **Peripherals** tab provides manual IP connection for external devices including the TGXL, PGXL, Antenna Genius, and ShackSwitch. Each device has its own row with **Connect** / **Disconnect** buttons and a status indicator.

### ShackSwitch

The ShackSwitch row behaves as follows:

- Enter the ShackSwitch IP address and click **Connect**. AetherSDR saves the address to `SS_ManualIp` and port to `SS_ControlPort` and connects using the AG UDP/TCP protocol on port 9007.
- If the radio has already discovered the ShackSwitch via UDP beacon, the IP field may be pre-filled.
- The row shows a Connected status only when the connected device is identified as a ShackSwitch. If a standard Antenna Genius is connected instead, the ShackSwitch row does not show Connected, and the Antenna Genius row does.
- Click **⚙ Web UI** to open the ShackSwitch's local web interface in your system browser. AetherSDR determines the port as follows:
  1. Uses the `webPort` advertised in the beacon if it is greater than 1024.
  2. Falls back to the value stored in `SS_WebPort`.
  3. Falls back to port 5000.

## Firmware update (Radio tab)

The **Radio** tab contains controls for checking for firmware updates and uploading firmware to the radio.

### How to update firmware

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, the status label shows the available version and instructs you to download the SmartSDR installer from flexradio.com.
   - If the firmware is already current, the status label shows "Firmware is up to date."
4. Download the SmartSDR installer from flexradio.com if one is available.
5. Click **Select Installer...**.
   - The file picker accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` file.
   - The firmware stager detects the file format automatically and extracts the `.ssdr` without requiring external tools.
   - While the stager prepares the firmware, the progress bar is shown and the status label reads "Preparing firmware from \<filename\>...".
6. Once staging completes, click **Upload Firmware** to transfer the firmware to the radio. Progress and result are shown in the status label.

### Firmware update controls

| Control | Kind | Notes |
|---|---|---|
| **Check for Update** | Button | Queries for available firmware updates. Enables or updates the status label with the result. |
| **Select Installer...** | Button | Opens a file picker. Accepts `.msi`, `.exe`, or `.ssdr`. Stager auto-detects format. Previously labelled **Browse .ssdr...** (changed in v0.9.3). |
| **Upload Firmware** | Button | Starts the firmware upload. Progress bar and status label update throughout. |

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

| Control | Kind | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Spin box | Frequency used for calibration. Must not be empty before clicking **Start**. |
| **Start** | Button | Begins calibration. Resets `freq_error_ppb` to 0, then issues `radio pll_start`. Disabled while busy. |
| **Freq Offset (ppb):** | Spin box | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Combo box | Auto / TCXO / GPSDO / External. Options shown depend on installed hardware. Lock status updates live. |

## Tips

- **TX Band Settings** is also accessible directly from `Settings > TX Band Settings...` without opening Radio Setup first.
- The **Max Power:** spin box on the TX tab sets a radio-level cap. Per-band limits set inside **TX Band Settings** operate on top of this cap.
- When running frequency calibration, ensure no other station is transmitting on the reference frequency before clicking **Start**.
- When **Check for Update** reports an available firmware version,
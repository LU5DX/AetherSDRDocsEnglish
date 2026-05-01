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
| Connect / Disconnect (Antenna Genius) | Push button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows "Connected" only when the connected device is a non-ShackSwitch Antenna Genius. If a ShackSwitch is the connected device, this row's status is hidden. |
| Connect / Disconnect (ShackSwitch) | Push button | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. The row shows "Connected" only when the connected device is identified as a ShackSwitch; the row is hidden from "Connected" status if a non-ShackSwitch Antenna Genius is the connected device. |
| ⚙ Web UI (ShackSwitch) | Push button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. The button reads the IP from `SS_ManualIp` or, if empty, from the live peer address when the connected device is a ShackSwitch. |
| Select Installer... | Push button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v0.9.3. |
| APD (tab) | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| ANT1 / ANT2 / XVTA / XVTB sampler combos (APD) | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. |
| Equalizer Reset (APD) | Push button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| Themes (tab) | Tab | UI customization tab — currently hosts the Slice Colors section. |
| Use Aether defaults / Custom colors | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. |
| Slice A–H color buttons | Push button | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. |
| Reset All to Defaults (Themes) | Push button | Resets all custom slice colors to the built-in AetherSDR palette. |

All four Radio Information fields are read-only. No persisted settings keys are associated with them.

## Firmware tab — selecting an installer or firmware file (v0.9.3)

In v0.9.3 the **Browse .ssdr...** button was renamed **Select Installer...**. The button now accepts the full SmartSDR installer package in addition to a pre-extracted `.ssdr` file, so you no longer need to extract the firmware manually before uploading.

**To stage firmware for upload:**

1. Click **Check for Update**. If an update is available, the status label instructs you to download the SmartSDR installer from flexradio.com.
2. Download the installer from flexradio.com (`.msi` for SmartSDR 4.2 and later, `.exe` for older releases).
3. Click **Select Installer...** and choose the downloaded file, or choose a pre-extracted `.ssdr` file if you have one.
4. AetherSDR reads the first 8 bytes of the file to detect whether it is an MSI package, a self-extracting EXE, or a raw `.ssdr`. The `.ssdr` payload is extracted automatically without external tools. Progress is shown in the progress bar and status label.
5. When staging completes, click **Upload Firmware** to transfer the firmware to the radio.

> **Note:** In versions before v0.9.3, clicking **Check for Update** when an update was available converted the button into a **Download vX.Y.Z** button that downloaded and staged the firmware automatically. That behavior has been removed. You must download the installer from flexradio.com yourself and then use **Select Installer...** to stage it.

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

## Peripherals tab — ShackSwitch web interface (v0.9.4)

In v0.9.4 the Peripherals tab adds a dedicated **⚙ Web UI** button next to the ShackSwitch row. Click it to open the ShackSwitch device's built-in configuration web page in your system browser.

The button determines the URL as follows:

1. If the ShackSwitch is currently connected and its discovery beacon advertises a `webPort` greater than 1024, that port is used.
2. Otherwise the stored `SS_WebPort` setting is used.
3. If neither is available, port 5000 is used as a fallback.

The IP address is taken from `SS_ManualIp`. If that field is empty and the connected device is a ShackSwitch, the live peer address is used instead. The button takes no action if no IP address can be determined.

Also in v0.9.4, the **Connect / Disconnect (Antenna Genius)** row now hides its "Connected" status when a ShackSwitch is the device actually connected through the Antenna Genius model. The ShackSwitch row shows "Connected" in that case instead.

**To open the ShackSwitch web interface:**

1. Click `Settings > Radio Setup...`.
2. Select the **Peripherals** tab.
3. Ensure the ShackSwitch is connected (the ShackSwitch row shows "Connected").
4. Click **⚙ Web UI**. Your default browser opens the device's configuration page.

## Tips

- If **Radio SN** is blank, the radio has not yet sent its chassis serial. Disconnect and reconnect to the radio.
- **Options** reflects what the radio itself reports. If you have recently purchased a license
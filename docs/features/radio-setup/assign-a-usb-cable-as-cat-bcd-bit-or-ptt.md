# Assign a USB cable as CAT, BCD, bit or PTT

Use this page to configure the USB serial adapters connected to your FLEX-8600 and assign each one a role — CAT control, BCD band data, individual bit output, or PTT — along with its serial parameters and behavior options.

## Before you start

- Connect the USB serial adapter(s) to the computer running AetherSDR before opening the dialog.
- AetherSDR must be connected to the radio. The USB Cables tab is not available without an active radio connection.

## Steps

1. Open `Settings > USB Cables...`. This opens the Radio Setup dialog directly on the USB Cables tab. Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Locate the cables list on the left side of the tab. Each detected USB cable appears with its name and a **Plugged** or **Unplugged** status indicator.
3. Select the cable you want to configure by clicking it in the list.
4. Set the cable type using the **Name:** field and the associated type selector. Choose from CAT, BCD, bit, or PTT depending on the role this cable should serve.
5. Set **Enabled** to enable the cable. The cable will not function until it is enabled.
6. Configure the serial parameters for the cable:
   - **Speed** — baud rate for the serial connection.
   - **Data Bits** — number of data bits.
   - **Parity** — parity setting.
   - **Stop Bits** — number of stop bits.
   - **Flow** — flow control method.
7. Configure the behavioral options relevant to the cable type:
   - **Source** — selects what drives the cable output.
   - **Auto Report** — controls whether state changes are reported automatically.
   - **BCD Type** — selects the BCD encoding format (BCD cables only).
   - **Polarity** — sets active-high or active-low logic.
   - **Bit Configuration (0–7)** — assigns functions to individual output bits (bit cables only).
8. Repeat steps 3–7 for any additional cables.
9. Click **Close** to dismiss the dialog. Settings take effect immediately when each cable is enabled; no separate Apply step is required.

## What each control does

| Control | Description | Notes |
|---|---|---|
| **Cables list / Status** | Lists all detected USB serial adapters with **Plugged** or **Unplugged** status. Select a cable here to edit its settings. | |
| **Name:** | User-visible label for the cable. | |
| **Enabled** | Activates the cable. The cable is inactive until enabled. | |
| **Speed** | Serial baud rate. | |
| **Data Bits** | Number of serial data bits. | |
| **Parity** | Serial parity: None, Even, Odd, etc. | |
| **Stop Bits** | Number of stop bits. | |
| **Flow** | Flow control method (None, Hardware, Software). | |
| **Source** | Selects the radio signal source that drives the cable output. | |
| **Auto Report** | When active, the radio reports state changes to the cable automatically. | |
| **BCD Type** | Selects the BCD band-data encoding format. Applies to BCD-type cables only. | |
| **Polarity** | Sets whether the output logic is active-high or active-low. | |
| **Bit Configuration (0–7)** | Maps individual output pins to specific functions. Applies to bit-type cables only. | |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. | Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. | |
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. | Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. | Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. | Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows **Connected** status only when the connected device is a standard Antenna Genius, not a ShackSwitch. | |
| **Connect / Disconnect (ShackSwitch)** | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. | ShackSwitch is detected by the 'ShackSwitch' field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from **Connected** status if Antenna Genius (non-ShackSwitch) is the connected device. |
| **⚙ Web UI (ShackSwitch)** | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. | |
| **Select Installer...** | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. | Label changed from **Browse .ssdr...** in v0.9.3. When an update is available, download the SmartSDR installer from flexradio.com, then click **Select Installer...** to stage it. |
| **APD (tab)** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. | Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. | Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. |
| **Equalizer Reset (APD)** | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. | |
| **Themes (tab)** | UI customization tab — currently hosts the Slice Colors section. | |
| **Use Aether defaults / Custom colors** | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. | Backed by `SliceColorManager::useCustomColors()`. |
| **Slice A–H color buttons** | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. | Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. |
| **Reset All to Defaults (Themes)** | Resets all custom slice colors to the built-in AetherSDR palette. | |

## RX tab — frequency calibration (v0.9.2.1)

The **RX** tab now shows the frequency calibration controls regardless of whether a GPSDO is installed. In previous releases, the calibration fields were hidden when a GPSDO was detected.

- If a GPSDO is installed, a green status line reads "GPSDO installed. Manual frequency offset calibration available."
- If no GPSDO is installed, a yellow status line reads "Manual frequency offset calibration available."

In both cases the **Cal Frequency (MHz):**, **Start**, and **Freq Offset (ppb):** controls are always visible.

### Calibration procedure

1. Open `Settings > Radio Setup...` and click the **RX** tab.
2. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
3. Click **Start**. The button changes to **Busy** and is disabled while calibration runs. A status label to the right of the button shows progress text.
   - "Starting…" appears immediately.
   - The radio receives `radio set cal_freq=<value>` followed by `radio set freq_error_ppb=0`, then `radio pll_start` to begin the sweep.
   - If you leave the **Cal Frequency (MHz):** field empty and click **Start**, the status label shows "Enter cal frequency" in amber and the calibration does not start.
4. Wait for the status label to indicate completion. The **Start** button re-enables automatically.
5. Confirm or adjust the result using **Freq Offset (ppb):**.

### RX tab controls

| Control | Description | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for calibration, entered in MHz to six decimal places. | Sent to the radio as `radio set cal_freq=<value>`. |
| **Start** | Begins the calibration sweep. Disabled and labelled **Busy** while a calibration is in progress. | Resets `freq_error_ppb` to 0 before starting. Requires a non-empty cal frequency. |
| **Freq Offset (ppb):** | Manual frequency offset correction in parts per billion. | |
| **10 MHz Reference Source:** | Selects the oscillator reference: Auto, TCXO, GPSDO, or External. Available options depend on installed hardware. | Lock status (Locked / Unlocked) is shown alongside the selector and updates live. |

## Firmware update (v0.9.3)

In v0.9.3, the firmware update workflow changed. AetherSDR no longer downloads the installer automatically. When **Check for Update** reports that a newer version is available, download the SmartSDR installer from flexradio.com yourself, then use **Select Installer...** to stage it locally.

### Supported installer formats

| Format | Extension | Notes |
|---|---|---|
| WiX MSI installer | `.msi` | FlexRadio v4.2 and later. |
| Self-extracting EXE installer | `.exe` | Older SmartSDR releases. |
| Pre-extracted firmware file | `.ssdr` | Direct firmware file, if you already have one. |

The firmware stager auto-detects the format from the first 8
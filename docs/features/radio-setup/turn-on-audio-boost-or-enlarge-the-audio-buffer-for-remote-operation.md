# Turn on audio boost or enlarge the audio buffer for remote operation

Use these settings to compensate for low receive volume or audio breakup when operating AetherSDR over a VPN or SmartLink connection. Audio Boost adds extra gain on the client audio path; a larger Audio Buffer absorbs network jitter at the cost of increased latency.

## Before you start

- AetherSDR must be connected to the radio. These controls are unavailable when no radio is connected.
- Open `Settings > Radio Setup...` and select the **Audio** tab before following the steps below.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. To increase receive volume, click **Audio Boost:** to toggle it on. The button shows its active state when enabled.
4. To reduce audio breakup or dropouts, click the **Audio Buffer:** spinbox and enter a value between 50 and 1000 ms. Higher values add more buffering at the cost of latency.
5. Close the dialog. Settings take effect immediately.

## What each control does

| Control | What it does | Valid range |
|---|---|---|
| **Audio Boost:** | Enables extra gain on the client audio path. | On / Off |
| **Audio Buffer:** | Sets the client-side audio buffer to absorb network jitter. Increase this when using VPN or SmartLink connections with unstable latency. | 50–1000 ms |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto / Uncompressed / Opus |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | On / Off |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | On / Off |
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. | 0–3 |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. | On / Off |
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | — |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | — |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row is hidden from the Connected state if a ShackSwitch (rather than an Antenna Genius) is the currently connected device. | — |
| **Connect / Disconnect (ShackSwitch)** | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the 'ShackSwitch' field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from Connected status if Antenna Genius (non-ShackSwitch) is the connected device. | — |
| **⚙ Web UI (ShackSwitch)** | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's webPort if > 1024, otherwise falls back to `SS_WebPort` or port 5000. | — |
| **Select Installer...** | Opens a file picker that accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools. This button was labelled **Browse .ssdr...** before v0.9.3. | — |
| **APD (tab)** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. | — |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. | INTERNAL / RX_A / RX_B / XVTA / XVTB |
| **Equalizer Reset (APD)** | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. | — |
| **Themes (tab)** | UI customization tab — currently hosts the Slice Colors section. | — |
| **Use Aether defaults / Custom colors** | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. | Use Aether defaults / Custom colors |
| **Slice A–H color buttons** | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices supported. | — |
| **Reset All to Defaults (Themes)** | Resets all custom slice colors to the built-in AetherSDR palette. | — |

## Peripherals tab — ShackSwitch web interface (v0.9.4 change)

In v0.9.4 the Peripherals tab gains a **⚙ Web UI** button on the ShackSwitch row. Clicking it opens the ShackSwitch device's built-in web configuration interface in your system browser.

The button determines the URL as follows:

1. If the ShackSwitch is currently connected and its discovery beacon advertises a `webPort` greater than 1024, that port is used.
2. Otherwise the value stored in `SS_WebPort` is used.
3. If neither is available, port 5000 is used as a fallback.

The IP address is taken from `SS_ManualIp` if set. If that field is empty and the currently connected device is a ShackSwitch, the live peer address is used instead. The button does nothing if no IP address can be resolved.

The Antenna Genius row also gains a small behavioral change in v0.9.4: when a ShackSwitch is the connected device, the Antenna Genius row no longer shows a Connected status, keeping the two rows visually distinct.

### How to open the ShackSwitch web interface

1. Click `Settings > Radio Setup...`.
2. Click the **Peripherals** tab.
3. Confirm the ShackSwitch row shows **Connected**. If not, enter the device IP and click **Connect**.
4. Click **⚙ Web UI**. Your default browser opens the ShackSwitch configuration page.

> **Note:** If your ShackSwitch uses a non-standard web port, set it manually in `SS_WebPort` before clicking **⚙ Web UI**.

## Firmware update — selecting an installer (v0.9.3 change)

In v0.9.3 the firmware staging workflow changed. The button previously labelled **Browse .ssdr...** is now labelled **Select Installer...**. The file picker now accepts the full SmartSDR installer package in addition to a pre-extracted .ssdr file.

When **Check for Update** detects a newer firmware version, AetherSDR no longer downloads it automatically. Instead, the status label instructs you to download the SmartSDR installer from flexradio.com yourself, then use **Select Installer...** to stage it.

### How to stage and upload firmware

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**. If an update is available, the status label displays the version number and instructs you to download the installer from flexradio.com.
4. Download the SmartSDR installer from flexradio.com to your computer (.msi for v4.2+, .exe for older releases).
5. Click **Select Installer...**. In the file picker, select the downloaded .msi, .exe, or .ssdr file and click **Open**. The status label shows **Preparing firmware from \<filename\>...** and a progress bar appears while the stager extracts the firmware.
6. When staging completes, click **Upload Firmware** to transfer the firmware to the radio. A progress bar and status label track the upload.

> **Note:** If you already have a pre-extracted .ssdr file, you can select it directly in step 5. The stager detects the format automatically.

## RX tab — frequency calibration

In v0.9.2.1 the RX tab calibration section was revised. The **Cal Frequency (MHz):** field and **Start** button are now always visible regardless of whether a GPSDO is installed. When a GPSDO is present, the status label confirms it in green; when no GPSDO is installed, the label appears in amber. Both cases allow manual frequency offset calibration.

### Calibration controls

| Control | What it does |
|---|---|
| **Cal Frequency (MHz):** | Enter the known-accurate reference frequency in MHz to use for calibration. The field must not be empty before clicking Start. |
| **Start** | Begins the frequency calibration sequence. AetherSDR resets the frequency error to 0 ppb, then sends `radio pll_start` to the radio. The button is disabled and labelled **Busy** while calibration is running. A status label beside the button reports progress (Starting…, and subsequent states). |
| **Freq Offset (ppb):** | Displays or manually sets the current frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Selects the oscillator reference. Available options depend on installed hardware. The status label beside the control updates live and shows the active source, lock state, and any resolution in progress (see below). |

### 10 MHz Reference Source — status label behavior (v0.9.7 change)

In v0.9.7 the lock status label beside **10 MHz Reference Source:** was revised to show richer state information.

The label text is determined as follows:

- If the radio has not yet reported oscillator state, the label shows **Waiting for oscillator status**.
- If **Auto** is selected and the radio has resolved to a specific source, the label shows **Auto -> \<resolved source\>** followed by **Locked** or **Unlocked**.
- If a specific source is selected but the radio is actively using a different source, the label shows **\<selected source\> -> \<active source\>** followed by **Locked** or **Unlocked**.
- Otherwise the label shows the active source name followed by **Locked** or **Unlocked
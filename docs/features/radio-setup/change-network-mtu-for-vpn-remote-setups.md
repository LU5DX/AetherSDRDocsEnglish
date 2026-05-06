# Change Network MTU for VPN/Remote Setups

The Network MTU setting controls the maximum packet size the radio sends over the network. Lowering it prevents fragmentation when you connect through a VPN or other tunnel that reduces the available path MTU.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is not accessible when disconnected.
- Know the MTU of your VPN tunnel or network path. Common VPN MTUs are 1400–1450 bytes; a standard Ethernet path is 1500 bytes.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match your network path MTU.
5. Click **Apply** to push the new MTU to the radio.

## What each control does

| Control | Description | Default |
|---|---|---|
| **Network MTU:** | Outgoing packet size in bytes. Lower this when operating over a VPN or any link with a reduced MTU. | 1450 |
| **Apply** | Sends the current Network tab configuration, including the MTU value, to the radio. | — |
| TX Follows Active Slice | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | False |
| Active Slice Follows TX | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | False |
| Voice / CW / Digital filter sharpness sliders | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. | — |
| Auto (Voice / CW / Digital) | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. | — |
| Connect / Disconnect (TGXL) | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | — |
| Connect / Disconnect (PGXL) | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | — |
| Connect / Disconnect (Antenna Genius) | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows a Connected status only when the connected device is an Antenna Genius proper (not a ShackSwitch). | — |
| Connect / Disconnect (ShackSwitch) | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. The row is hidden from Connected status if an Antenna Genius (non-ShackSwitch) is the connected device. | — |
| ⚙ Web UI (ShackSwitch) | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. | — |
| Select Installer... | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer) or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v0.9.3. | — |
| APD (tab) | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. | — |
| ANT1 / ANT2 / XVTA / XVTB sampler combos (APD) | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. | INTERNAL |
| Equalizer Reset (APD) | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. | — |
| Themes (tab) | UI customization tab — currently hosts the Slice Colors section. | — |
| Use Aether defaults / Custom colors (radio button) | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. | Use Aether defaults |
| Slice A–H color buttons | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. | — |
| Reset All to Defaults (Themes) | Resets all custom slice colors to the built-in AetherSDR palette. | — |

## Firmware update (Radio tab)

In v0.9.3, the firmware staging workflow changed. AetherSDR no longer downloads firmware automatically when an update is detected. Instead, download the SmartSDR installer from flexradio.com yourself, then stage it manually.

### Staging a firmware update

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, a status message appears telling you the available version and directing you to download the installer from flexradio.com.
   - If firmware is current, a green status message confirms the installed version.
4. Download the SmartSDR installer from flexradio.com. Accepted formats:
   - `.msi` — WiX installer (FlexRadio SmartSDR v4.2 and later)
   - `.exe` — older self-extracting installer
   - `.ssdr` — pre-extracted firmware file
5. Click **Select Installer...**.
   - A file picker opens filtered to `*.msi`, `*.exe`, and `*.ssdr`.
   - Select the file you downloaded.
   - AetherSDR reads the file, auto-detects its format from the first 8 bytes, and extracts the `.ssdr` payload if needed. A status label shows progress.
6. When staging completes and the upload button becomes active, click **Upload Firmware**.
   - A progress bar tracks the upload.
   - Do not close the dialog or disconnect from the radio while the upload is in progress.

### Firmware status messages

| Message | Meaning |
|---|---|
| Update available: v*x.y.z* | A newer firmware version exists. Download the installer from flexradio.com, then click **Select Installer...**. |
| Firmware is up to date (v*x.y.z*) | No action needed. |
| Preparing firmware from *filename*... | The stager is reading and extracting the selected file. |
| (error text in red) | Staging or upload failed. Check the file is a valid SmartSDR installer or firmware file and try again. |

### Notes

- The **Select Installer...** button was labelled **Browse .ssdr...** in versions prior to v0.9.3.
- Staging runs entirely on the client; no external tools are required to unpack `.msi` or `.exe` installers.

## Frequency calibration (RX tab)

In v0.9.2.1 the RX tab frequency calibration controls are available regardless of whether a GPSDO is installed. Previously, the **Cal Frequency (MHz):**, **Start**, and **Freq Offset (ppb):** controls were hidden when a GPSDO was detected. Now all calibration fields are always shown; a status label at the top of the group indicates whether a GPSDO is present (green text) or not (amber text).

### 10 MHz reference source

The **10 MHz Reference Source:** combo box on the RX tab selects the oscillator reference used by the radio. In v0.9.7 the combo and its lock-status label were updated with the following behavior changes:

- The combo is populated dynamically. Only sources supported by the connected hardware appear. **TCXO** and **External 10 MHz** entries are shown when the radio reports those sources as present or when the current or active oscillator state involves them, even if the hardware-present flags are not yet reported. **Auto** is always available.
- The label beside the combo now shows the resolved source as well as the lock state. When **Auto** is selected and the radio has chosen a specific source, the label reads `Auto -> <source>`. When a specific source is selected and the radio is using a different one, the label reads `<selected> -> <active>`. When the setting and state agree, only the active source is shown.
- Lock state is appended: `Locked` (green) or `Unlocked` (red).
- If **External 10 MHz** is selected or active but no external reference is detected, the label appends `(not detected)`.
- While the radio has not yet reported oscillator status, the label reads `Waiting for oscillator status` in grey.
- The combo label for the external source changed from **External** to **External 10 MHz**.

#### 10 MHz Reference Source combo options

| Option | When shown |
|---|---|
| Auto | Always. |
| TCXO | When oscillator status has been received, or when the radio reports `tcxoPresent`, or when the current or active setting is `tcxo`. |
| GPSDO | When the radio reports `gpsdoPresent`, or when the current or active setting is `gpsdo`. |
| External 10 MHz | When oscillator status has been received, or when the radio reports `extPresent`, or when the current or active setting is `external`. |

### Calibration procedure

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in the **Cal Frequency (MHz):** field.
4. Click **Start**.
   - The button label changes to **Busy** and is disabled while the calibration sweep runs.
   - A status label beside the button updates as the sweep progresses.
   - The radio first resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`), then begins the PLL calibration sequence.
5. When calibration completes the button re-enables and the status label shows the result.
6. If you prefer to set the offset manually, enter a value directly in **Freq Offset (ppb):** without clicking **Start**.

### Calibration status messages

| Message | Meaning |
|---|---|
| Starting… | The sweep command has been sent to the radio. |
| Busy | PLL calibration is in progress. |
| Enter cal frequency | The **Cal Frequency (MHz):** field was
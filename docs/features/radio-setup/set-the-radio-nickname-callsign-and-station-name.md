# Set the radio nickname, callsign and station name

Set a human-readable nickname, your callsign, and a station name on the connected FLEX-8600. These values identify the radio and this client to other multiFLEX stations on the network.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) controls are not available without an active connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. In the **Radio Identification** group, locate the **Nickname** field. Type the nickname you want to assign to the radio.
4. Press Tab or click away from the field to confirm. AetherSDR sends the new name to the radio immediately.
5. In the **Callsign** field, type your station callsign.
6. Press Tab or click away from the field to confirm.
7. In the **Station Name** field, type the name that identifies this client to other multiFLEX stations.
8. Press Tab or click away from the field to confirm.
9. Click **Close** to dismiss the dialog.

## What each control does

| Control | Description | Default |
|---|---|---|
| **Nickname** | User-friendly label for the radio. Sent to the radio as the radio name. | Radio's reported name |
| **Callsign** | Your station callsign, stored on the radio. | _(blank)_ |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. | OS hostname |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | False |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | False |
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. | — |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. | — |
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | Connect |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | Connect |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | Connect |
| **Select Installer...** | Opens a file picker that accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer) or a pre-extracted .ssdr firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools. Label changed from **Browse .ssdr...** in v0.9.3. | — |
| **APD (tab)** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. | — |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. | INTERNAL |
| **Equalizer Reset (APD)** | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. | — |
| **Themes (tab)** | UI customization tab — currently hosts the Slice Colors section. | — |
| **Use Aether defaults / Custom colors** | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. | Use Aether defaults |
| **Slice A–H color buttons** | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. | — |
| **Reset All to Defaults (Themes)** | Resets all custom slice colors to the built-in AetherSDR palette. | — |

## Firmware update (Radio tab)

Use the firmware update controls in the **Radio** tab to check for and apply firmware updates to the radio.

### To check for a firmware update

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, the status label shows the available version number and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it.
   - If firmware is up to date, the status label confirms the current version in green.

### To stage and upload firmware

1. Download the SmartSDR installer from flexradio.com. AetherSDR accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file.
2. Click **Select Installer...**
   - The file picker opens with the filter set to `*.msi *.exe *.ssdr`.
   - Select the downloaded file and click Open.
   - AetherSDR begins preparing the firmware automatically. The status label shows "Preparing firmware from \<filename\>..." and the progress bar appears.
   - The firmware stager auto-detects the file format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr payload without external tools.
   - When staging is complete, **Upload Firmware** becomes enabled.
3. Click **Upload Firmware** to send the firmware to the radio.
   - A progress bar tracks the upload.
   - The status label reports the result when the upload finishes.

> **Note:** In v0.9.3 the button formerly labelled **Browse .ssdr...** was renamed to **Select Installer...** and extended to accept .msi and .exe installer packages in addition to .ssdr files. The automatic download-and-stage path that had been triggered by a second click of **Check for Update** was also removed; download the installer manually from flexradio.com instead.

### Firmware update controls

| Control | Description |
|---|---|
| **Check for Update** | Queries the update server for the latest available firmware version. |
| **Select Installer...** | Opens a file picker. Select a .msi, .exe, or .ssdr file. AetherSDR stages the firmware automatically after selection. |
| **Upload Firmware** | Sends the staged firmware to the radio. Enabled only after a file has been successfully staged. |
| Firmware status label | Empty until an operation begins, then shows progress and result text. |

## Frequency calibration (RX tab)

The **RX** tab provides manual frequency offset calibration regardless of whether a GPSDO is installed.

- If a GPSDO is installed, the status label reads "GPSDO installed. Manual frequency offset calibration available." in green.
- If no GPSDO is installed, the status label reads "Manual frequency offset calibration available." in amber.

In both cases the **Cal Frequency (MHz)** field and the **Start** button are always shown.

### To run a frequency calibration

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known reference frequency in the **Cal Frequency (MHz)** field.
4. Click **Start**.
   - The button label changes to **Busy** and is disabled while calibration is in progress.
   - A status label beside the button shows the current state (for example, "Starting…").
   - AetherSDR resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`) before initiating the calibration sweep.
5. Wait for the status label to report completion. The **Start** button re-enables automatically.

### Cal Frequency (MHz) field behavior

| Condition | Result |
|---|---|
| Field is empty when Start is clicked | Status label shows "Enter cal frequency" in amber; calibration does not start. |
| Valid frequency entered | AetherSDR sends `radio set cal_freq=<value>`, resets freq error to 0 ppb, then starts the PLL calibration sweep. |

### RX tab controls

| Control | Description | Default |
|---|---|---|
| **Cal Frequency (MHz)** | Reference frequency used for manual calibration. Always shown from v0.9.2.1 onward, regardless of GPSDO presence. | — |
| **Start** | Starts the frequency calibration sweep. Disabled and labelled **Busy** while a calibration is running. | — |
| **Freq Offset (ppb)** | Manual frequency offset in parts per billion. | — |
| **10 MHz Reference Source** | Selects oscillator reference: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. Lock status (Locked / Unlocked) updates live alongside the selector. | Auto |

## Tips

- If **Nickname** is left blank, AetherSDR pre-fills the field with the radio's reported name from the network.
- **Station Name** defaults to the OS hostname when no value has been saved. To restore the default, clear the field and press Tab — then re-enter the hostname manually if needed.
- Changes to **Nickname** and **Callsign** are pushed to the radio the moment you leave each field. No separate Save or Apply step is required.
- **Station Name** is saved locally in AetherSDR's settings and also sent to the radio as the client station identifier for multiFLEX.
- Prior to v0.9.2.1, the **Cal Frequency** field and **Start** button were hidden when a GPSDO was installed. They are now always available.
- In v0.9.3, **Select Installer...** replaces the former **Browse .ssdr...** button and accepts .msi and .exe installer packages in addition to pre-extracted .ssdr files. If you have a previously downloaded .ssdr file it still works — select it the same way.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
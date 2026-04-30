# Enable auto-record on TX and pick a save folder

When auto-record on TX is enabled, AetherSDR starts recording audio automatically each time you transmit and stops after a configurable idle timeout. This page explains how to turn that feature on and choose where recordings are saved.

## Before you start

- The radio must be connected. Radio Setup requires an active radio connection.
- Decide whether you want radio-side or client-side recording, as this affects where audio is captured.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Recording:**, click either **Radio Side** or **Client Side** to select where audio is captured. The active selection is highlighted. This choice is saved to `RecordingMode`.
4. In the **Save to:** field, type the full path to your recordings folder, or click **...** to browse for a folder. The path is saved to `QsoRecordingDir`.
5. Check the **Auto-record on TX** checkbox. This enables automatic recording whenever the radio transitions to transmit. The setting is saved to `QsoRecordingAutoRecord`.
6. Set **Idle timeout:** to the number of seconds of silence after which the recording stops. The value is saved to `QsoRecordingIdleTimeout`.
7. Close the dialog. Settings take effect immediately.

## What each control does

| Control | What it does | Default |
|---|---|---|
| **Recording: Radio Side / Client Side** | Selects whether audio is captured at the radio or at this PC. | Radio Side |
| **Save to:** | Folder path where recording files are written. Defaults to Documents/AetherSDR/Recordings. | — |
| **...** | Opens a folder browser to select the save location. | — |
| **Auto-record on TX** | When checked, recording starts automatically on each transmit and stops after the idle timeout elapses. | Unchecked |
| **Idle timeout:** | Seconds of silence before the recording stops after TX ends. | 120 s |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. | Off |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. | Off |
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. | — |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode and disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. | — |
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | Connect |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | Connect |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | Connect |
| **Select Installer...** | Opens a file picker that accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools. Label changed from **Browse .ssdr...** in v0.9.3. | — |
| **APD (tab)** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. | — |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. | INTERNAL |
| **Equalizer Reset (APD)** | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. | — |
| **Themes (tab)** | UI customization tab — currently hosts the Slice Colors section. | — |
| **Use Aether defaults / Custom colors** | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. | Use Aether defaults |
| **Slice A–H color buttons** | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. | — |
| **Reset All to Defaults (Themes)** | Resets all custom slice colors to the built-in AetherSDR palette. | — |

## Firmware update (Radio tab)

The **Radio** tab includes firmware update controls. In v0.9.3 the workflow for staging a firmware file changed.

### Checking for updates

1. Click the **Radio** tab in Radio Setup.
2. Click **Check for Update**. AetherSDR queries the FlexRadio update server.
3. If an update is available, the status label shows the available version and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it.
4. If firmware is current, the status label confirms the installed version.

> **Note:** In v0.9.3 the one-click download button was removed. You must download the SmartSDR installer from flexradio.com yourself, then stage it using **Select Installer...**.

### Staging and uploading firmware

1. Download the SmartSDR installer from flexradio.com. Supported file types are .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file.
2. Click **Select Installer...**. A file picker opens filtered to those file types.
3. Select the downloaded file. AetherSDR automatically detects the format and extracts the .ssdr without external tools. A progress bar and status label show extraction progress.
4. When staging completes successfully, click **Upload Firmware** to transfer the firmware to the radio.

### Firmware update controls

| Control | What it does |
|---|---|
| **Check for Update** | Queries the FlexRadio update server and reports whether a newer firmware version is available. |
| **Select Installer...** | Opens a file picker accepting .msi, .exe, or .ssdr files. The stager auto-detects format and extracts the .ssdr. Changed from **Browse .ssdr...** in v0.9.3. |
| **Upload Firmware** | Transfers the staged firmware to the radio. A progress bar and status label track the upload. |

## Frequency calibration (RX tab)

The **RX** tab provides manual frequency offset calibration and 10 MHz reference source selection.

In v0.9.2.1 the calibration controls are available regardless of whether a GPSDO is installed. When a GPSDO is present the status label reads "GPSDO installed. Manual frequency offset calibration available." (green). Without a GPSDO the label reads "Manual frequency offset calibration available." (amber).

### Calibration controls

| Control | What it does |
|---|---|
| **Cal Frequency (MHz):** | Enter the known reference frequency in MHz. The value is sent to the radio as `radio set cal_freq=<value>` when you finish editing the field. |
| **Start** | Resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`), then starts the calibration sweep. The button label changes to **Busy** and is disabled while calibration is running. A status label beside the button reports progress. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Selects the oscillator reference: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. A live lock status indicator (Locked / Unlocked) appears beside the selector. |

### Starting a calibration

1. Click the **RX** tab in Radio Setup.
2. Enter the known reference frequency in **Cal Frequency (MHz):**.
3. Click **Start**. The button shows **Busy** while the sweep runs. Watch the status label for progress and result.
4. When calibration completes, the button re-enables and the status label shows the result.

> **Note:** Leaving **Cal Frequency (MHz):** empty and clicking **Start** will show a warning ("Enter cal frequency") and will not begin calibration.

## Tips

- If you use SmartLink or a VPN, consider whether **Radio Side** or **Client Side** better matches where you want the files stored. Radio-side recordings stay on the FLEX-8600; client-side recordings go to the folder set in **Save to:**.
- Set **Idle timeout:** to a low value (a few seconds) if you want each transmission captured as a separate file. A higher value merges pauses within a QSO into one file.
- When staging firmware, .msi and .exe installers are accepted directly — you do not need to extract the .ssdr file manually.

## Troubleshooting

- **No files appear in the save folder after transmitting** — Confirm **Auto-record on TX** is checked and that the path in **Save to:** exists and is writable. If the folder does not exist, AetherSDR cannot create the file.
- **Save to: field shows no path** — Click **...** and select a folder explicitly. Leaving the field empty may prevent recording from starting.
- **Start button stays disabled after clicking** — Check that **Cal Frequency (MHz):** contains a valid frequency value. The button re-enables automatically when calibration finishes or fails.
- **Upload Firmware button is disabled after clicking Select Installer...** — The stager is still extracting the .ssdr from the installer. Wait for the progress bar to complete and the status label to confirm the firmware is ready, then click **Upload Firmware**.
- **APD tab is not visible** — The APD tab only appears on FLEX-8x00 series radios running SmartSDR 4.2.18 or later firmware. If the tab is absent, your radio model or firmware version does not support configurable APD.

## Related

- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Pick Opus vs
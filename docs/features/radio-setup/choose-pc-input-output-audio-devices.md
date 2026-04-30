# Choose PC input/output audio devices

This page explains how to select which PC audio devices AetherSDR uses for radio receive audio output and microphone input. You need to do this when you first set up AetherSDR or when you change headsets, speakers, or audio interfaces.

## Before you start

- The radio must be connected. Radio Setup controls are unavailable without an active radio connection.
- Know which audio input and output devices your PC exposes (check your OS audio settings if unsure).

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Audio** tab.
3. Under **PC Audio Devices:**, click the **Input:** drop-down and select the device you want to use for microphone or audio input.
4. Click the **Output:** drop-down and select the device you want to use for receive audio playback.
5. Close the dialog. The selections take effect immediately.

## What each control does

| Control | What it does | Default |
|---|---|---|
| **PC Audio Devices: Input:** | Selects the host audio input device (microphone, audio interface, etc.). | System default |
| **PC Audio Devices: Output:** | Selects the host audio output device (speakers, headphones, audio interface, etc.). | System default |
| **Audio Boost:** | Applies extra gain on the client audio path. | Off |
| **Audio Buffer:** | Increases the client audio buffer to absorb jitter on VPN or SmartLink connections. | 200 ms |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink or LAN. | Auto |
| **Recording: Radio Side / Client Side** | Selects whether recordings are captured at the radio or the client. | Radio Side |
| **Save to:** | Folder where client-side recordings are saved. Defaults to Documents/AetherSDR/Recordings. | — |
| **...** | Opens a folder browser to select the recording directory. | — |
| **Auto-record on TX** | Automatically starts recording when you transmit. | Off |
| **Idle timeout:** | Seconds of silence after which an active recording stops automatically. | 120 s |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. | Off |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. | Off |
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode. Disabled when Auto is enabled for that mode. | — |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode and disables the manual sharpness slider. | — |
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | Connect |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | Connect |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | Connect |
| **Select Installer...** | Opens a file picker that accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools. Label changed from **Browse .ssdr...** in v0.9.3. | — |
| **APD (tab)** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. | — |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. | INTERNAL |
| **Equalizer Reset (APD)** | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. | — |
| **Themes (tab)** | UI customization tab — currently hosts the Slice Colors section. | — |
| **Use Aether defaults / Custom colors** | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. | Use Aether defaults |
| **Slice A–H color buttons** | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. | — |
| **Reset All to Defaults (Themes)** | Resets all custom slice colors to the built-in AetherSDR palette. | — |

## Firmware update changes in v0.9.3

The firmware update workflow on the **Radio** tab has changed in v0.9.3.

### Selecting a firmware file

The **Browse .ssdr...** button has been renamed **Select Installer...**. It now accepts three file types:

- **.msi** — FlexRadio SmartSDR v4.2+ WiX installer
- **.exe** — older self-extracting SmartSDR installer
- **.ssdr** — a pre-extracted firmware file

The firmware stager auto-detects the format from the first 8 bytes of the file (OLE/MSI magic for .msi, PE/COFF MZ header for .exe) and extracts the .ssdr payload without requiring any external tools. A progress indicator and status label update as the extraction proceeds.

### Check for Update behavior

When **Check for Update** finds a newer firmware version, the status label now reads:

> Update available: v*X.Y.Z*  
> Download the SmartSDR installer from flexradio.com,  
> then click 'Select Installer...' to stage it.

In previous versions, the **Check for Update** button re-labeled itself to **Download v***X.Y.Z* and triggered an in-app download. That in-app download step has been removed. Download the installer manually from flexradio.com, then use **Select Installer...** to stage it.

### Steps to update firmware

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Radio** tab.
3. Click **Check for Update** to see whether a newer firmware version is available.
4. If an update is available, download the SmartSDR installer (.msi or .exe) from flexradio.com.
5. Click **Select Installer...** and select the downloaded installer or a pre-extracted .ssdr file.
6. Wait for the stager to extract and prepare the firmware. The status label shows progress.
7. Click **Upload Firmware** to transfer the firmware to the radio.

## Frequency calibration changes in v0.9.2.1

The **RX** tab calibration panel has been redesigned. In previous versions, the **Cal Frequency (MHz):** field, **Start** button, and manual **Freq Offset (ppb):** controls were hidden when a GPSDO was detected. Starting with v0.9.2.1, these controls are always visible regardless of whether a GPSDO is installed.

The status indicator at the top of the calibration group now reads:

- **Green** — "GPSDO installed. Manual frequency offset calibration available." (GPSDO present)
- **Amber** — "Manual frequency offset calibration available." (no GPSDO)

### How calibration now works

When you click **Start**, AetherSDR:

1. Validates that the **Cal Frequency (MHz):** field is not empty. If it is empty, the status label shows "Enter cal frequency" and the calibration does not proceed.
2. Resets the frequency error to zero (`radio set freq_error_ppb=0`) before starting, so each calibration run begins from a known baseline.
3. Disables and relabels the **Start** button to **Busy** while calibration is in progress.
4. Sends `radio pll_start` and monitors the response. The status label updates live to reflect progress (Starting… / running states / result).
5. Re-enables the **Start** button when calibration completes or fails.

The **Start** button is safe to use while a GPSDO is installed; the GPSDO reference is not disturbed.

If you navigate away from the **RX** tab or close Radio Setup while calibration is running, the in-progress callbacks are discarded safely — no partial state is written.

## Tips

- The Input and Output drop-downs list only devices the OS currently exposes. If a device is missing, connect it and reopen the Audio tab — device enumeration happens when the tab is first displayed.
- If receive audio sounds too quiet with your chosen output device, enable **Audio Boost:** before increasing OS volume.
- On VPN or SmartLink connections, raise **Audio Buffer:** to reduce dropouts. Values above 200 ms add noticeable delay.
- On the **RX** tab, always enter a known-accurate reference frequency in **Cal Frequency (MHz):** before clicking **Start**. Using an inaccurate frequency produces a wrong offset correction.
- To update firmware in v0.9.3 and later, download the SmartSDR installer from flexradio.com first. The in-app download step no longer exists. Use **Select Installer...** to stage the file you downloaded.

## Troubleshooting

- **No audio devices appear in the drop-downs** — The Audio tab enumerates devices when it first loads. Close Radio Setup, verify the OS recognizes the device, then reopen `Settings > Radio Setup...` and click the Audio tab again.
- **Receive audio plays through the wrong device** — The Output drop-down may still be set to a previously selected device. Open the Audio tab and reselect the correct output.
- **Microphone is not heard by the radio** — Confirm the correct device is selected in the **Input:** drop-down, and that the OS has not muted or blocked access to that device.
- **Start button stays labeled Busy** — A previous calibration run did not complete. Close and reopen Radio Setup to reset the calibration state, then try again.
- **"Enter cal frequency" appears when I click Start** — Type a valid frequency in MHz into the **Cal Frequency (MHz):** field before clicking **Start**.
- **Select Installer... shows an error or the Upload Firmware button stays disabled** — The stager could not extract a valid .ssdr from the selected file. Confirm you selected the correct SmartSDR installer for your radio model and that the download completed without errors, then try again.
- **APD tab is not visible** —
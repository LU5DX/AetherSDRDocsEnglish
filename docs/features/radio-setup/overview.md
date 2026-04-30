# Radio Setup Overview

The Radio Setup dialog is the central configuration window for your FLEX-8600. It brings together radio identification, network, GPS, transmit, audio, filters, transverters, USB cables, peripherals, slice color themes, and FlexControl serial settings in one place. Open it whenever you need to change anything about how AetherSDR interacts with your radio hardware.

## Before you start

- The radio must be connected. Radio Setup requires an active radio connection.

## How it works

Open Radio Setup from `Settings > Radio Setup...`. The dialog contains a row of tabs across the top; each tab covers a distinct area of configuration. Tabs other than Radio load their contents the first time you click them.

You can also jump directly to specific tabs:

- `Settings > USB Cables...` opens Radio Setup with the **USB Cables** tab active.
- `Settings > FlexControl...` opens Radio Setup with the **Serial** tab active (only available when serial port support is built in).

The dialog remembers its size and position between sessions.

### Tabs at a glance

| Tab | What you configure here |
|---|---|
| **Radio** | Serial number, hardware version, region, licensed options, nickname, callsign, station name, license info, and firmware update. |
| **Network** | IP address (DHCP or static), network MTU, and private IP enforcement. |
| **GPS** | Live GPS status: latitude, longitude, altitude, time, and satellite count. |
| **TX** | TX hang/delay timings, interlocks, global power cap, tune mode, waterfall TX display, TX/slice follow behavior, and a shortcut to per-band settings. |
| **Phone/CW** | Microphone level meter, iambic keyer (mode A/B, swap, sideband), CWX, CW decoder, and RTTY mark default. |
| **RX** | Frequency offset calibration and 10 MHz reference source selection. Calibration controls are always visible; when a GPSDO is installed the status label confirms its presence. |
| **Audio** | Line out, headphone, and speaker levels; audio compression codec; PC audio device selection; audio boost; audio buffer size; recording mode, folder, auto-record on TX, and idle timeout; NVIDIA BNR container control. |
| **Filters** | Low-latency vs. sharp filter selection per bandwidth, and a separate option for digital modes. |
| **XVTR** | Per-transverter configuration; create or remove transverter entries. |
| **APD** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna feedback port selection and equalizer reset. Visible only on FLEX-8x00 radios reporting `apd configurable=1` (SmartSDR 4.2.18+ firmware). |
| **USB Cables** | Assign USB serial adapters to CAT, BCD, bit, and PTT cable types and configure their serial parameters. |
| **Peripherals** | Manual IP connection to external devices: TGXL, PGXL, and Antenna Genius. |
| **Themes** | Slice color scheme: switch between built-in AetherSDR palette and custom per-slice colors (A–H). |
| **Serial** | FlexControl serial port selection, line parameters, pin function assignments (DTR/RTS), paddle swap, auto-open, and tuning knob detection. (Visible only when serial port support is built in.) |

## What each control does

The following controls have persisted settings keys or notable behaviors.

| Control | Tab | Behavior |
|---|---|---|
| **Station Name** | Radio | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if left empty. Stored as `StationName`. Sent to the radio as `client station <name>`. |
| **Select Installer...** | Radio | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v0.9.3. |
| **Network MTU:** | Network | Sets maximum outgoing VITA-49 UDP packet size in bytes (576–9000). Default 1450 is safe for most VPN/SD-WAN tunnels. Stored as `NetworkMtu`. |
| **TX Follows Active Slice** | TX | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored as `TxFollowsActiveSlice`. |
| **Active Slice Follows TX** | TX | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored as `ActiveFollowsTxSlice`. |
| **Iambic Mode: A / B** | Phone/CW | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. Default: A. |
| **Decode:** | Phone/CW | Enables the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`. Default: enabled. |
| **Voice / CW / Digital filter sharpness sliders** | Filters | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Filters | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos** | APD | Selects the feedback path used to sample outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. Default: INTERNAL. |
| **Equalizer Reset** | APD | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| **Audio Compression (SmartLink):** Auto / Uncompressed / Opus | Audio | Selects the audio codec used over SmartLink or LAN. Stored as `AudioCompression`. Default: Auto. |
| **Prevent system sleep while connected** | Audio | Keeps the OS awake while the radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. Default: disabled. |
| **Audio Boost:** | Audio | Enables extra gain on the client-side audio path. Stored as `AudioBoost`. |
| **Audio Buffer:** | Audio | Increases the audio buffer (50–1000 ms) to absorb VPN or SmartLink jitter. Default: 200 ms. Stored as `AudioBufferMs`. |
| **Recording:** Radio Side / Client Side | Audio | Selects whether recordings are captured at the radio or on this computer. Stored as `RecordingMode`. Default: Radio Side. |
| **Save to:** | Audio | Folder path where client-side recordings are saved. Stored as `QsoRecordingDir`. Defaults to `Documents/AetherSDR/Recordings`. |
| **Auto-record on TX** | Audio | Automatically starts recording whenever the radio transmits. Stored as `QsoRecordingAutoRecord`. Default: disabled. |
| **Idle timeout:** | Audio | Seconds of silence (10–3600) after which an active recording stops automatically. Default: 120 s. Stored as `QsoRecordingIdleTimeout`. |
| **Connect / Disconnect (TGXL)** | Peripherals | Opens/closes a direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has already discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Peripherals | Opens/closes a direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Peripherals | Opens/closes a connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |
| **Use Aether defaults / Custom colors** | Themes | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. Default: Use Aether defaults. |
| **Slice A–H color buttons** | Themes | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices supported. |
| **Reset All to Defaults** | Themes | Resets all custom slice colors to the built-in AetherSDR palette. |

## Firmware update (Radio tab)

In v0.9.3 the firmware update workflow changed. AetherSDR no longer downloads the installer automatically. The button previously labeled **Browse .ssdr...** is now labeled **Select Installer...** and the check-for-update flow works as follows:

1. Click **Check for Update**. AetherSDR queries the update server.
   - If the firmware is current, the status label shows "Firmware is up to date (v*x.x.x*)." in green.
   - If an update is available, the status label shows the new version number and instructs you to download the SmartSDR installer from flexradio.com.
2. Download the SmartSDR installer from [flexradio.com](https://www.flexradio.com) to your computer. The installer can be a `.msi` file (FlexRadio v4.2+ WiX installer), a `.exe` file (older self-extracting installer), or a pre-extracted `.ssdr` firmware file.
3. Click **Select Installer...**. A file picker opens with the filter:
   - SmartSDR installer or firmware (`*.msi *.exe *.ssdr`)
   - MSI installer (`*.msi`)
   - EXE installer (`*.exe`)
   - Extracted firmware (`*.ssdr`)
   - All files (`*`)
4. Select the file you downloaded. AetherSDR reads the first 8 bytes to detect the format (OLE/MSI magic vs PE/COFF MZ vs raw `.ssdr`) and extracts the firmware automatically without external tools. A status label shows "Preparing firmware from *filename*..." while extraction runs.
5. When staging completes, click **Upload Firmware**. A progress bar and status label track the upload.

> **Note:** If you already have a `.ssdr` file extracted from a previous installation, you can select it directly in step 3 — no installer is required.

## RX tab — frequency calibration

In v0.9.2.1 the RX tab layout was revised. The calibration controls are now always visible regardless of whether a GPSDO is installed. A status label at the top of the group changes color and text to reflect the hardware present:

- **GPSDO installed** — label shown in green: "GPSDO installed. Manual frequency offset calibration available."
-
# Switch to an External 10 MHz Reference

This page explains how to select an external 10 MHz reference clock on a connected FLEX-8600. Use an external reference when you have a GPS-disciplined oscillator or other precision 10 MHz source and want the radio to lock to it instead of its internal oscillator.

## Before you start

- AetherSDR must be connected to the radio. The Radio Setup dialog requires an active radio connection.
- Your external 10 MHz reference signal must be connected to the rear-panel REF IN port on the FLEX-8600 before switching the source.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `RX` tab.
3. Locate the `10 MHz Reference Source:` combo box.
4. Select `External 10 MHz` from the combo box. To return to the built-in oscillator, select `Auto`.

## What each control does

| Control | Kind | Valid range / Behavior |
|---|---|---|
| `10 MHz Reference Source:` | Combo box | `Auto` \| `TCXO` \| `GPSDO` \| `External 10 MHz`. Options shown depend on hardware installed and on the current oscillator state reported by the radio. The combo is populated dynamically: `TCXO` appears when the hardware has a TCXO or when the radio currently reports TCXO as its active state; `GPSDO` appears when a GPSDO is present; `External 10 MHz` appears when an external reference is detected or currently active. Lock status is shown alongside the combo and updates live (see below). |
| Lock status label | Indicator | Shows the current oscillator source and lock state. When `Auto` is selected, the label reads `Auto -> <active source>` to indicate what the radio has chosen. When the selected source differs from the active state, both are shown (e.g. `TCXO -> GPSDO`). Appends `Locked` (green) or `Unlocked` (red). If `External 10 MHz` is selected but no external signal is detected, the label appends `(not detected)`. While waiting for the radio to report status the label reads `Waiting for oscillator status` (grey). |
| `TX Follows Active Slice` | Push button | TX follows the active slice. Mutually exclusive with `Active Slice Follows TX`. Disabled automatically during Split operation. |
| `Active Slice Follows TX` | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with `TX Follows Active Slice`. |
| `Voice / CW / Digital filter sharpness sliders` | Slider (0–3) | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| `Auto (Voice / CW / Digital)` | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| `Connect / Disconnect (TGXL)` | Push button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. If the IP field is cleared and the dialog is closed without clicking Connect/Disconnect, the saved IP and port are wiped and the device disconnects. |
| `Connect / Disconnect (PGXL)` | Push button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. If the IP field is cleared and the dialog is closed without clicking Connect/Disconnect, the saved IP and port are wiped and the device disconnects. |
| `Connect / Disconnect (Antenna Genius)` | Push button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row is hidden from "Connected" status when a ShackSwitch (rather than a standard Antenna Genius) is the connected device. If the IP field is cleared and the dialog is closed without clicking Connect/Disconnect, the saved IP and port are wiped and the device disconnects. |
| `Connect / Disconnect (ShackSwitch)` | Push button | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from "Connected" status if an Antenna Genius (non-ShackSwitch) is the connected device. |
| `⚙ Web UI (ShackSwitch)` | Push button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if > 1024, otherwise falls back to `SS_WebPort` or port 5000. |
| `Select Installer...` | Push button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label was `Browse .ssdr...` before v0.9.3. |
| `APD` (tab) | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (`INTERNAL` / `RX_A` / `RX_B` / `XVTA` / `XVTB`) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| `ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)` | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Default `INTERNAL`. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to `INTERNAL` if the radio reports an unrecognised value. |
| `Equalizer Reset (APD)` | Push button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| `Themes` (tab) | Tab | UI customization tab — currently hosts the Slice Colors section. |
| `Use Aether defaults / Custom colors` | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. |
| `Slice A–H color buttons` | Push button | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when `Use Aether defaults` is selected. Up to 8 slices (`kSliceColorCount`). |
| `Reset All to Defaults (Themes)` | Push button | Resets all custom slice colors to the built-in AetherSDR palette. |
| `FlexControl Tuning Knob: Detect / Close` | Push button | Detects or closes a FlexControl knob. |
| `WheelRit` / `WheelXit` | Action mapping options | Available button action mappings for FlexControl wheels. WheelFrequency is the default. |
| `Station Name` | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored as `StationName` in AppSettings. Sent to radio as 'client station <name>'. |
| `Network MTU:` | Spinbox (576-9000) | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored as `NetworkMtu` in AppSettings. |
| `Audio Compression (SmartLink):` | Push button (Auto/Uncompressed/Opus) | Selects audio codec for SmartLink/LAN. |
| `Prevent system sleep while connected` | Checkbox | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. |
| `Audio Boost:` | Toggle button | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| `Audio Buffer:` | Text field (50-1000 ms) | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Default 200. Stored as `AudioBufferMs`. |
| `Recording: Radio Side / Client Side` | Push button | Picks radio-side or client-side recording. |
| `Save to:` | Text field | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored as `QsoRecordingDir`. |
| `Auto-record on TX` | Checkbox | Automatically records while transmitting. Stored as `QsoRecordingAutoRecord`. |
| `Idle timeout:` | Spinbox (10-3600 sec) | Seconds of silence before recording stops. Default 120. Stored as `QsoRecordingIdleTimeout`. |

## Firmware update (Radio tab)

Starting in v0.9.3, the firmware update workflow no longer downloads installer files automatically. When `Check for Update` finds a newer version, the status label instructs you to download the SmartSDR installer from flexradio.com and then use `Select Installer...` to stage it locally. The button previously labelled `Browse .ssdr...` is now labelled `Select Installer...` and accepts `.msi`, `.exe`, and `.ssdr` files.

### How to update firmware

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `Radio` tab.
3. Click `Check for Update`. AetherSDR contacts FlexRadio's update server and reports the latest available version in the status label.
4. If an update is available, download the SmartSDR installer from flexradio.com.
5. Click `Select Installer...` and choose the downloaded `.msi`, `.exe`, or pre-extracted `.ssdr` file. AetherSDR auto-detects the format and extracts the firmware. The status label shows preparation progress.
6. When staging completes, click `Upload Firmware`. A progress bar and status label track the upload.

## Frequency calibration (RX tab)

As of v0.9.2.1, the frequency calibration controls on the RX tab are always visible, regardless of whether a GPSDO is installed. When a GPSDO is present, the status label reads "GPSDO installed. Manual frequency offset calibration available." (shown in green). When no GPSDO is present, the label reads "Manual frequency offset calibration available." (shown in amber). In previous versions, the calibration controls were hidden when a GPSDO was detected.

### Calibration controls

| Control | Kind | Behavior |
|---|---|---|
| `Cal Frequency (MHz):` | Text field | Frequency used for manual calibration. Enter the exact frequency of your reference signal in MHz. |
| `Start` | Push button | Sets the calibration frequency, resets `freq_error_ppb` to 0, then starts the calibration sweep. The button is disabled and shows "Busy" while calibration is in progress. A status label beside the button shows the current state (Starting…, progress text, or result). The field must not be empty; if it is, the status label prompts you to enter a frequency before proceeding. |
| `Freq Offset (ppb):` | Spinbox | Manual frequency offset in parts per billion. Adjust if you need to apply a known offset without running the automated calibration sweep. |

### How to run a calibration sweep

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `RX` tab.
3. Enter the exact frequency of your reference signal in the `Cal Frequency (MHz):` field.
4. Click `Start`. The button becomes disabled and shows "Busy". Watch the status label for progress.
5. When the sweep finishes, the status label reports the result and the `Start` button re-enables.

## Oscillator source combo behavior (v0.9.7)

In v0.9.7, the `10 MHz Reference Source:` combo box is populated dynamically based on the live state the radio reports, rather than solely on hardware-presence flags detected at dialog open time. The following rules apply:

- `Auto` is always present.
- `TCXO` appears if the radio has a TCXO installed, or if the radio is currently reporting TCXO as its oscillator state, or if TCXO was previously selected.
- `GPSDO` appears if a GPSDO is installed, or if the radio is currently
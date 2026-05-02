# Pick Opus vs Uncompressed Audio for SmartLink

Select the audio codec AetherSDR uses over SmartLink or LAN connections. Opus reduces bandwidth at the cost of a small amount of compression; uncompressed PCM preserves full fidelity when bandwidth allows. Auto lets the radio choose.

## Before you start

- AetherSDR must be connected to the radio. The Audio tab is not accessible without an active connection.
- Open `Settings > Radio Setup...` and click the **Audio** tab.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Audio** tab.
3. Under **Audio Compression (SmartLink):**, click **Auto**, **Uncompressed**, or **Opus** to select the codec.
   - **Auto** — the radio negotiates the codec automatically (default).
   - **Uncompressed** — sends raw PCM audio; uses more bandwidth.
   - **Opus** — sends Opus-encoded audio; lower bandwidth, slight compression.
4. Close the dialog. The setting takes effect immediately and is saved.

## What each control does

| Control | Default | Valid values |
|---|---|---|
| **Audio Compression (SmartLink):** Auto / Uncompressed / Opus | Auto | Auto, Uncompressed, Opus |
| **Audio Boost:** | — | Enabled / Disabled |
| **Audio Buffer:** | 200 ms | 50–1000 ms |
| **Recording:** Radio Side / Client Side | Radio Side | Radio Side, Client Side |
| **Save to:** | — | Folder path |
| **Auto-record on TX** | — | Checked / Unchecked |
| **Idle timeout:** | 120 sec | 10–3600 sec |
| **TX Follows Active Slice** | False | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | False | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| **Voice / CW / Digital filter sharpness sliders** | — | 0–3. Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | — | Enabled / Disabled. Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Connect | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Connect | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Connect | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows a Connected status only when the connected device is a non-ShackSwitch Antenna Genius. |
| **Connect / Disconnect (ShackSwitch)** | Connect | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the 'ShackSwitch' field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from 'Connected' status if Antenna Genius (non-ShackSwitch) is the connected device. |
| **⚙ Web UI (ShackSwitch)** | — | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's webPort if > 1024, otherwise falls back to `SS_WebPort` or port 5000. |
| **Cal Frequency (MHz):** | — | Frequency used for manual calibration. Available regardless of whether a GPSDO is installed. If the field is empty when you click **Start**, a warning appears and calibration does not begin. |
| **Start** | — | Sets the calibration frequency, resets `freq_error_ppb` to 0, then starts the radio PLL calibration sweep. The button is disabled and labelled **Busy** while calibration is running. |
| **Freq Offset (ppb):** | — | Manual frequency offset in parts per billion. |
| **Select Installer...** | — | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v0.9.3. |
| **APD (tab)** | — | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | INTERNAL | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. |
| **Equalizer Reset (APD)** | — | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| **Themes (tab)** | — | UI customization tab — currently hosts the Slice Colors section. |
| **Use Aether defaults / Custom colors** | Use Aether defaults | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. |
| **Slice A–H color buttons** | — | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. |
| **Reset All to Defaults (Themes)** | — | Resets all custom slice colors to the built-in AetherSDR palette. |

## Firmware update — changes in v0.9.3

The **Browse .ssdr...** button on the **Radio** tab has been renamed to **Select Installer...**. It now accepts three file types in addition to a pre-extracted `.ssdr` file:

- `.msi` — the WiX-based SmartSDR installer used by FlexRadio from v4.2 onward.
- `.exe` — the older self-extracting installer.
- `.ssdr` — a firmware file you have already extracted yourself.

The firmware stager examines the first 8 bytes of the selected file to determine its format (OLE/MSI magic or PE/COFF MZ header) and extracts the `.ssdr` payload automatically without requiring any external tools. Progress is shown in the status area below the buttons.

When **Check for Update** reports that a newer firmware version is available, AetherSDR no longer offers to download the installer automatically. Instead the status area displays:

> Update available: v*X.Y.Z*  
> Download the SmartSDR installer from flexradio.com, then click 'Select Installer...' to stage it.

To update firmware:

1. Open `Settings > Radio Setup...` and click the **Radio** tab.
2. Click **Check for Update**. Note the version number shown in the status area.
3. Download the SmartSDR installer for that version from flexradio.com.
4. Click **Select Installer...** and choose the downloaded `.msi`, `.exe`, or `.ssdr` file.
5. AetherSDR stages the firmware. Watch the progress bar and status label.
6. When staging is complete, click **Upload Firmware** to transfer the firmware to the radio.

## RX tab — frequency calibration changes in v0.9.2.1

In previous versions, the **Cal Frequency (MHz):** field and **Start** button were only shown when no GPSDO was installed. From v0.9.2.1, those controls are always visible on the **RX** tab. The status banner at the top of the group still indicates whether a GPSDO is present (green text) or not (amber text).

When you click **Start**:

1. AetherSDR validates that the **Cal Frequency (MHz):** field is not empty. If it is empty, a warning message appears next to the button and calibration does not proceed.
2. The frequency offset is reset to 0 (`radio set freq_error_ppb=0`) and the calibration frequency is sent to the radio (`radio set cal_freq=<value>`).
3. The radio PLL calibration sweep begins (`radio pll_start`).
4. The **Start** button is disabled and shows **Busy** for the duration of the sweep.
5. A status label next to the button updates as the sweep progresses and shows the result when complete.

## Peripherals tab — ShackSwitch changes in v0.9.4

The **Antenna Genius** row now shows a Connected status only when the device identified on the connection is a non-ShackSwitch Antenna Genius. If a ShackSwitch is the connected device, the Antenna Genius row hides its Connected indicator and the **ShackSwitch** row shows Connected instead.

A new **ShackSwitch** row has been added to the Peripherals tab. Enter the ShackSwitch IP address and click **Connect** to open a connection on port 9007 using the AG control protocol. The IP is saved to `SS_ManualIp`. If the ShackSwitch has already been discovered via UDP beacon, the IP field is pre-filled.

A new **⚙ Web UI** button has been added to the ShackSwitch row. Click it to open the ShackSwitch device's built-in web configuration interface in your system browser. The URL is constructed as follows:

1. AetherSDR uses the IP from `SS_ManualIp`, or if that is empty and a ShackSwitch is currently connected, the live peer address.
2. The port is taken from the beacon's `webPort` field when that value is greater than 1024. If not, AetherSDR falls back to the `SS_WebPort` setting or port 5000.

If no IP address is available (not connected and `SS_ManualIp` is empty), clicking **⚙ Web UI** does nothing.

## Tips

- On a fast local LAN, **Uncompressed** avoids any codec artefacts and is the better choice for critical listening or digital mode decoding.
- On a slow or congested link (VPN, cellular SmartLink), **Opus** reduces audio dropouts.
<!-- docmesh:llm version=v0.9.4 date=2026-05-02 -->

# Switch the Radio Between DHCP and Static IP

Use this page to change how the FLEX-8600 obtains its network address — either automatically via DHCP or with a fixed static IP, subnet mask, and gateway you specify.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available when a radio connection is active.
- If you are switching to static IP, have the IP address, subnet mask, and gateway values ready before you begin.
- Changing the network configuration will cause the radio to move to a new address. You will need to reconnect after applying.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Network** tab.
3. Note the current **IP Address**, **Mask**, and **MAC Address** shown as read-only indicators.
4. Click the **DHCP / Static** toggle button to switch modes. The button reflects the current mode; clicking it switches to the other.
5. If you selected static mode, fill in the **IP Address:**, **Mask:**, and **Gateway:** text fields with the values for your network.
6. Click **Apply** to push the network configuration to the radio.
7. Reconnect to the radio at its new address using `Settings > Connect to Radio...`.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicators (read-only) | Displays the radio's current network addresses. |
| **DHCP / Static** | Toggle button | Switches the radio between DHCP and static IP modes. |
| **IP Address:** | Text field | Static IP address to assign to the radio. Active only in static mode. |
| **Mask:** | Text field | Subnet mask for the static configuration. Active only in static mode. |
| **Gateway:** | Text field | Default gateway for the static configuration. Active only in static mode. |
| **Apply** | Push button | Sends the network configuration to the radio. |
| **Enforce Private IP Connections:** | Toggle button | Rejects non-RFC1918 peers. |
| **Network MTU:** | Spinbox (576-9000 bytes, default 1450) | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings (`NetworkMtu`). |
| **TX Follows Active Slice** | Push button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |
| **Voice / CW / Digital filter sharpness sliders** | Sliders (0–3) | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Toggle button | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Connect / Disconnect (TGXL)** | Push button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. |
| **Connect / Disconnect (PGXL)** | Push button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| **Connect / Disconnect (Antenna Genius)** | Push button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row is hidden from Connected status if a ShackSwitch (not a standard Antenna Genius) is the connected device. |
| **Connect / Disconnect (ShackSwitch)** | Push button | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from Connected status if a standard Antenna Genius (non-ShackSwitch) is the connected device. |
| **Web UI (ShackSwitch)** | Push button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. |
| **Select Installer...** | Push button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v0.9.3. |
| **APD (tab)** | Tab | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna selection of the feedback sample port (INTERNAL / RX_A / RX_B / XVTA / XVTB) and an equalizer reset button. Tab is hidden unless the radio reports `apd configurable=1`. Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible. |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos (APD)** | Combo box | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. |
| **Equalizer Reset (APD)** | Push button | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| **Themes (tab)** | Tab | UI customization tab — currently hosts the Slice Colors section. |
| **Use Aether defaults / Custom colors** | Radio button | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Backed by `SliceColorManager::useCustomColors()`. |
| **Slice A–H color buttons** | Push buttons | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges. Buttons are disabled when **Use Aether defaults** is selected. Up to 8 slices. |
| **Reset All to Defaults (Themes)** | Push button | Resets all custom slice colors to the built-in AetherSDR palette. |
| **Enable/Disable the Level Meter During Receive** | Toggle button | Shows mic level meter even in RX. |
| **Iambic:** | Toggle button | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Push buttons (mutually exclusive) | Selects Curtis iambic mode A or B for both the radio and the local software keyer. |
| **Swap:** | Toggle button | Swaps dit/dah. |
| **Sideband:** | Combo box (LSB / USB) | Selects CW pitch sideband. |
| **CWX:** | Toggle button | Enables CWX macro keying. |
| **Decode:** | Toggle button (default True) | Enables the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`. |
| **RTTY Mark Default:** | Spinbox | Default RTTY mark frequency. |
| **TX Band Settings** | Push button | Opens the dedicated per-band power/tune dialog. |
| **Timings (in ms)** | Spinbox | TX hang / delay timings. |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle button | Enables RCA and accessory interlock inputs. |
| **Max Power:** | Spinbox (0-100 %) | Sets radio-level TX power cap. |
| **Tune Mode:** | Combo box | Selects how the tune button behaves. |
| **Show TX in Waterfall:** | Toggle button | Draws TX signal in the waterfall. |
| **Line Out:** | Slider | Line-out gain. |
| **Mute (Line Out)** | Push button | Mutes line-out. |
| **Headphone:** | Slider | Headphone gain. |
| **Mute (Headphone)** | Push button | Mutes headphone. |
| **Front Speaker: / Mute** | Push button | Mutes front speaker (model-specific). |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Push button (default Auto) | Selects audio codec for SmartLink/LAN. Stored as `AudioCompression`. |
| **Prevent system sleep while connected** | Checkbox (default False) | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. |
| **PC Audio Devices: Input: / Output:** | Combo box | Picks host audio in/out devices. |
| **Audio Boost:** | Toggle button | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| **Audio Buffer:** | Text field (default 200, range 50-1000 ms) | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Stored as `AudioBufferMs`. |
| **Recording: Radio Side / Client Side** | Push button (default Radio Side) | Picks radio-side or client-side recording. Stored as `RecordingMode`. |
| **Save to:** | Text field | Folder for saved recordings (client-side only). Stored as `QsoRecordingDir`. Defaults to Documents/AetherSDR/Recordings. |
| **... (browse)** | Push button | Browses for recording folder. |
| **Auto-record on TX** | Checkbox (default False) | Automatically records while transmitting. Stored as `QsoRecordingAutoRecord`. |
| **Idle timeout:** | Spinbox (default 120, range 10-3600 sec) | Seconds of silence before recording stops. Stored as `QsoRecordingIdleTimeout`. |
| **NVIDIA BNR: Autostart Container / Start / Stop / Check Status** | Push buttons | Controls the NVIDIA Broadcast noise-removal container. |

## Peripheral auto-connect and clearing manual IP

When you enter an IP address for a peripheral (TGXL, PGXL, Antenna Genius, or ShackSwitch) and click **Connect**, the IP and port are saved to settings. On subsequent startups, AetherSDR automatically attempts to reconnect to that peripheral.

If you clear the IP field and click **Connect** while disconnected, the saved manual IP and port are removed from settings, preventing auto-connect on startup. If you clear the IP field and close the **Radio Setup** dialog without clicking Connect/Disconnect, the saved settings are also cleared and any active connection is disconnected, ensuring downstream handlers (such as button visibility) see the cleared state.

## Firmware update (Radio tab)

The **Radio** tab includes controls to check for firmware updates and stage a firmware file for upload.

### How to update firmware in v0.9.3

1. Click **Check for Update**. AetherSDR queries the FlexRadio update server. If an update is available, the status label shows the version number and instructs you to download the SmartSDR installer from flexradio.com.
2. Download the SmartSDR installer from flexradio.com (`.msi` for v4.2+, `.exe` for older releases).
3. Click **Select Installer...** to open the file picker. Select the installer you downloaded, or a pre-extracted `.ssdr` file if you already have one. The stager detects the file format automatically and extracts the firmware without external tools. The status label updates to show preparation progress.
4. When staging is complete, click **Upload Firmware** to transfer the firmware to the radio. A progress bar and status label track the upload.

> **Note:** In v0.9.3 the button formerly labeled **Browse .ssdr...** was renamed to **Select Installer...** and the file picker now accepts `.msi`, `.exe`, and `.ssdr` files. The **Check for Update** button no longer switches to a download button when an update is found; you download the installer manually from flexradio.com and stage it locally.

### Firmware tab controls

| Control |
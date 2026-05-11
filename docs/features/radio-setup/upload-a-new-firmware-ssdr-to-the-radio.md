# Upload a New Firmware File to the Radio

This page explains how to load a firmware image onto your FLEX-8600 using the Radio Setup dialog. You would do this to update the radio to a specific firmware version without using the automatic update check.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) will not populate correctly without a live connection.
- Download the SmartSDR installer from flexradio.com and note where it is saved on your computer. AetherSDR accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file.
- Do not transmit during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Select Installer...** to open a file chooser.
4. Navigate to the installer or firmware file on your computer, select it, and confirm. AetherSDR auto-detects the format from the file header and extracts the `.ssdr` if needed. A status message appears while the firmware is being prepared.
5. When the status indicates the firmware is ready, click **Upload Firmware**.
6. Watch the progress bar and status text below the button. Wait until the status indicates the upload is complete before doing anything else.
7. Reboot the radio as directed by the firmware release notes to apply the new firmware.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Radio SN** | Indicator | Chassis serial number (read-only). |
| **Region** | Indicator | Radio regulatory region. |
| **HW Version** | Indicator | Hardware version string. |
| **Model** | Indicator | Radio model. |
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as `client station <name>`. |
| **Remote On** | Button | Enables remote wake / remote-on. |
| **Options** | Indicator | Shows licensed radio options. |
| **FlexControl** | Indicator | Detected state of FlexControl hardware. |
| **multiFLEX** | Indicator | multiFLEX enabled state. |
| **License Info** | Indicator | Displays license details (Subscription / Expiration / Radio ID / Licensed version) from the radio. |
| **Check for Update** | Button | Queries for available firmware updates. If an update is found, the status area shows the available version and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it. |
| **Select Installer...** | Button | Opens a file dialog that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. A status message is shown while the file is being prepared. Renamed from **Browse .ssdr...** in v0.9.3. |
| **Upload Firmware** | Button | Starts the upload using the file staged by **Select Installer...**. A progress bar and status text appear below and update as the transfer proceeds. |
| TX Follows Active Slice | Button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| Active Slice Follows TX | Button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |

## Network tab

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator | Read-only network addresses. |
| **Enforce Private IP Connections:** | Toggle | Rejects non-RFC1918 peers. |
| **Network MTU:** | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes (576-9000). Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. |
| **DHCP / Static** | Toggle | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text field | Static IP configuration fields. |
| **Apply** | Button | Pushes the network config to the radio. |

## GPS tab

| Control | Kind | Behavior |
|---|---|---|
| GPS info | Indicator | GPS presence and live lat/lon/alt/time/satellites info. |

## TX tab

| Control | Kind | Behavior |
|---|---|---|
| **TX Band Settings** | Button | Opens the dedicated per-band power/tune dialog. |
| **Timings (in ms)** | Spinbox | TX hang / delay timings. |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle | Enables RCA and accessory interlock inputs. |
| **Max Power:** | Spinbox | Sets radio-level TX power cap (0-100%). |
| **Tune Mode:** | Combo box | Selects how the tune button behaves. |
| **Show TX in Waterfall:** | Toggle | Draws TX signal in the waterfall. |
| **TX Follows Active Slice** | Button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |

## Phone/CW tab

| Control | Kind | Behavior |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle | Shows mic level meter even in RX. |
| **Iambic:** | Toggle | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Button | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| **Swap:** | Toggle | Swaps dit/dah. |
| **Sideband:** | Combo box | Selects CW pitch sideband (LSB / USB). |
| **CWX:** | Toggle | Enables CWX macro keying. |
| **Decode:** | Toggle | Enables the CW decode overlay on the panadapter. |
| **RTTY Mark Default:** | Spinbox | Default RTTY mark frequency. |

## RX tab

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz)** | Field | Enter the known reference frequency in MHz (six decimal places). |
| **Start** | Button | Resets the frequency error to 0 ppb, then starts the calibration sweep. Disabled and labeled **Busy** while a sweep is running. |
| **Freq Offset (ppb)** | Spinbox | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference source. Options shown depend on hardware installed and live radio state. |
| Oscillator status label | Indicator | Shows the resolved source, lock state, and (for External) whether a signal is detected. Updates live. |

## Audio tab

| Control | Kind | Behavior |
|---|---|---|
| **Line Out:** | Slider | Line-out gain. |
| **Mute (Line Out)** | Button | Mutes line-out. |
| **Headphone:** | Slider | Headphone gain. |
| **Mute (Headphone)** | Button | Mutes headphone. |
| **Front Speaker: / Mute** | Button | Mutes front speaker (model-specific). |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Button | Selects audio codec for SmartLink/LAN. |
| **Prevent system sleep while connected** | Checkbox | Keeps OS awake while radio is connected. |
| **PC Audio Devices: Input: / Output:** | Combo box | Picks host audio in/out devices. |
| **Audio Boost:** | Toggle | Enables extra gain on the client audio path. |
| **Audio Buffer:** | Text field | Increases audio buffer in milliseconds (50-1000 ms) for VPN/SmartLink jitter. |
| **Recording: Radio Side / Client Side** | Button | Picks radio-side or client-side recording. |
| **Save to:** | Text field | Folder for saved recordings (client-side only). |
| **...** | Button | Browses for recording folder. |
| **Auto-record on TX** | Checkbox | Automatically records while transmitting. |
| **Idle timeout:** | Spinbox | Seconds of silence before recording stops (10-3600 sec). |
| **NVIDIA BNR: Autostart Container / Start / Stop / Check Status** | Button | Controls the NVIDIA Broadcast noise-removal container. |

## Filters tab

| Control | Kind | Behavior |
|---|---|---|
| **Voice / CW / Digital filter sharpness sliders** | Slider | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. |
| **Auto (Voice / CW / Digital)** | Toggle | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | Forces low-latency filters in DIGU/DIGL. |

## XVTR tab

| Control | Kind | Behavior |
|---|---|---|
| **RX Only:** | Toggle | Forces RX-only on that transverter. |
| **Remove (xvtr)** | Button | Deletes the transverter definition. |
| **Create New Transverter** | Button | Adds a new transverter entry. |

## USB Cables tab

| Control | Kind | Behavior |
|---|---|---|
| **Cables list / Status** | Indicator | Detected USB cables per type with Plugged/Unplugged status. |
| **Name: / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0-7)** | Combo box | Per-cable serial parameters and behavior. |

## Peripherals tab

| Control | Kind | Behavior |
|---|---|---|
| **Connect / Disconnect (TGXL)** | Button | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has already discovered the TGXL, the discovered IP is pre-filled. If the user clears the IP field and closes the dialog without clicking Connect/Disconnect, the saved manual IP/port is removed and the device disconnects automatically. |
| **Connect / Disconnect (PGXL)** | Button | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. Same behavior as TGXL for empty IP field on close. |
| **Connect / Disconnect (Antenna Genius)** | Button | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row shows a Connected status only when the connected device is a genuine Antenna Genius (not a ShackSwitch). Same behavior as TGXL for empty IP field on close. |
| **Connect / Disconnect (ShackSwitch)** | Button | Opens/closes connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the 'ShackSwitch' field in the AG broadcast beacon. Auto-discovery via UDP also works without this row. Row hidden from Connected status if Antenna Genius (non-ShackSwitch) is the connected device. |
| **⚙ Web UI (ShackSwitch)** | Button | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024, otherwise falls back to `SS_WebPort` or port 5000. |

## Serial tab

| Control | Kind | Behavior |
|---|---|---|
| **Port / Refresh / Path** | Combo box | Picks/edits the serial device. |
| **Baud / Data / Parity / Stop** | Combo box | Serial line parameters. |
| **DTR / RTS: Function / Polarity** | Combo box | Assigns signal function and polarity. |
| **Paddle Swap (swap dit/dah)** | Checkbox | Swaps dit/dah for paddle. |
| **Auto-open serial port on startup** | Checkbox | Reopens the port on app launch. |
| **FlexControl Tuning Knob: Detect / Close** | Button | Detects or closes a FlexControl knob. |
| **Auto-detect on startup
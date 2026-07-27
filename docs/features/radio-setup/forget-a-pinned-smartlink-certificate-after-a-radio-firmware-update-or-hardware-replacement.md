# Radio Setup Dialog Reference

The **Radio Setup** dialog is the master per-radio configuration window. It contains tabs for radio information, network settings, GPS, TX, Phone/CW, RX, audio, filters, transverters, USB cables, peripherals, APD, themes, SmartLink certificate management, and serial port configuration.

## Opening the dialog

1. Click **Settings > Radio Setup...** in the main menu.
2. The dialog opens with the **Radio** tab selected.

Many read-only values (serial number, HW version, options, model, subscription details, IP address, MAC address, firmware version) include a clipboard copy button next to the label. Click this button to copy the value to your clipboard for sharing with support.

## Radio tab

The **Radio** tab displays radio identification, license information, and firmware update controls.

| Control | Type | Description |
|---------|------|-------------|
| Radio SN | Indicator | Chassis serial number (read-only). Includes clipboard copy button. |
| Region | Indicator | Radio regulatory region. Default: USA. |
| HW Version | Indicator | Hardware version string. Includes clipboard copy button. |
| Remote On | Push button | Enables remote wake / remote-on. |
| Options | Indicator | Licensed radio options. Includes clipboard copy button. |
| FlexControl | Indicator | Detected state of FlexControl hardware. |
| multiFLEX | Indicator | multiFLEX enabled state. |
| Model | Indicator | Radio model. Includes clipboard copy button. |
| Nickname | Text field | User-friendly radio nickname. |
| Callsign | Text field | Station callsign. |
| Station Name | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as 'client station <name>'. |
| License Info | Indicator | Displays license details including Subscription, Expiration, Radio ID, and Licensed version. Each field includes a clipboard copy button. |
| Check for Update | Push button | Queries for firmware updates. |
| Select Installer... | Push button | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. Label changed from 'Browse .ssdr...' in v26.5.3. |
| Upload Firmware | Push button | Starts firmware upload with progress bar and status. |

## Network tab

The **Network** tab displays radio network information and advanced network options.

| Control | Type | Description |
|---------|------|-------------|
| IP Address / Mask / MAC Address | Indicator | Read-only network addresses. Each includes a clipboard copy button. |
| Enforce Private IP Connections: | Toggle button | Rejects non-RFC1918 peers. |
| Network MTU: | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default: 1450. Valid range: 576-9000 bytes. Stored in AppSettings as `NetworkMtu`. Default 1450 is safe for most VPN/SD-WAN tunnels. |
| DHCP / Static | Toggle button | Switches between DHCP and Static IP modes. |
| IP Address: / Mask: / Gateway: | Text field | Static IP configuration fields. |
| Apply | Push button | Pushes the network config to the radio. |

## GPS tab

The **GPS** tab displays GPS presence and live lat/lon/alt/time/satellites information.

## TX tab

The **TX** tab configures TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and provides a shortcut to TX Band Settings.

| Control | Type | Description |
|---------|------|-------------|
| TX Band Settings | Push button | Opens the dedicated per-band power/tune dialog. |
| Timings (in ms) | Spinbox | TX hang / delay timings. |
| Interlocks - TX REQ: RCA / Accessory | Toggle button | Enables RCA and accessory interlock inputs. |
| Max Power: | Spinbox | Sets radio-level TX power cap. Valid range: 0-100%. |
| Tune Mode: | Combo box | Selects how the tune button behaves. |
| Show TX in Waterfall: | Toggle button | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | Default: False. TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. Stored as `TxFollowsActiveSlice`. |
| Active Slice Follows TX | Push button | Default: False. Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. Stored as `ActiveFollowsTxSlice`. |

## Phone/CW tab

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

| Control | Type | Description |
|---------|------|-------------|
| Enable/Disable the Level Meter During Receive | Toggle button | Shows mic level meter even in RX. |
| Iambic: | Toggle button | Enables or disables the iambic keyer on the radio. In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. These also drive the new local software iambic keyer (IambicKeyer) which mirrors the radio's iambic state for sub-5 ms sidetone. |
| Iambic Mode: A / B | Push button | Default: A. Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair added in v0.9.1. |
| Swap: | Toggle button | Swaps dit/dah. |
| Sideband: | Combo box | Selects CW pitch sideband. Options: LSB, USB. |
| CWX: | Toggle button | Enables CWX macro keying. |
| Decode: | Toggle button | Default: True. Enables the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`. |
| RTTY Mark Default: | Spinbox | Default RTTY mark frequency. |

## RX tab

The **RX** tab configures GPSDO frequency offset calibration and 10 MHz reference source.

| Control | Type | Description |
|---------|------|-------------|
| Cal Frequency (MHz): | Spinbox | Frequency used for manual calibration. |
| Start | Push button | Starts the frequency calibration sweep. |
| Freq Offset (ppb): | Spinbox | Manual frequency offset in ppb. |
| 10 MHz Reference Source: | Combo box | Selects oscillator reference source. Default: Auto. Options depend on hardware installed: Auto, TCXO, GPSDO, External. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

## Audio tab

The **Audio** tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

| Control | Type | Description |
|---------|------|-------------|
| Line Out: | Slider | Line-out gain. |
| Mute (Line Out) | Push button | Mutes line-out. |
| Headphone: | Slider | Headphone gain. |
| Mute (Headphone) | Push button | Mutes headphone. |
| Front Speaker: / Mute | Push button | Mutes front speaker (model-specific). |
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Push button | Default: Auto. Selects audio codec for SmartLink/LAN. Stored as `AudioCompression`. |
| Prevent system sleep while connected | Checkbox | Default: False. Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. |
| PC Audio Devices: Input: / Output: | Combo box | Picks host audio in/out devices. |
| Audio Boost: | Toggle button | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| Audio Buffer: | Text field | Default: 200. Increases audio buffer in milliseconds for VPN/SmartLink jitter. Valid range: 50-1000 ms. Stored as `AudioBufferMs`. Applied to AudioEngine::setRxBufferCapMs(). |
| Recording: Radio Side / Client Side | Push button | Default: Radio Side. Picks radio-side or client-side recording. Stored as `RecordingMode`. |
| Save to: | Text field | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored as `QsoRecordingDir`. |
| ... | Push button | Browses for recording folder. |
| Auto-record on TX | Checkbox | Default: False. Automatically records while transmitting. Stored as `QsoRecordingAutoRecord`. |
| Idle timeout: | Spinbox | Default: 120. Seconds of silence before recording stops. Valid range: 10-3600 sec. Stored as `QsoRecordingIdleTimeout`. |
| NVIDIA BNR: Autostart Container / Start / Stop / Check Status | Push button | Controls the NVIDIA Broadcast noise-removal container. |

## Filters tab

The **Filters** tab configures low-latency and sharp filter options per bandwidth.

| Control | Type | Description |
|---------|------|-------------|
| Voice / CW / Digital filter sharpness sliders | Slider | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as 'radio filter_sharpness <mode> level=<N>'. |
| Auto (Voice / CW / Digital) | Toggle button | Enables automatic filter-level selection for that mode. Disables the manual sharpness slider. Commands sent as 'radio filter_sharpness <mode> auto_level=1'. |
| Use Low Latency Filters for Digital Modes | Checkbox | Forces low-latency filters in DIGU/DIGL. |

## XVTR tab

The **XVTR** tab configures per-transverter settings. Contains nested tabs, one per transverter, and a '+' tab to create new ones.

| Control | Type | Description |
|---------|------|-------------|
| RX Only: | Toggle button | Forces RX-only on that transverter. |
| Remove (xvtr) | Push button | Deletes the transverter definition. |
| Create New Transverter | Push button | Adds a new transverter entry. |

## USB Cables tab

The **USB Cables** tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

| Control | Type | Description |
|---------|------|-------------|
| Cables list / Status | Indicator | Detected USB cables per type with Plugged/Unplugged status. |
| Name: / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0-7) | Combo box | Per-cable serial parameters and behavior. |

## Peripherals tab

The **Peripherals** tab configures external devices manual IP connection for TGXL, PGXL, and Antenna Genius.

| Control | Type | Description |
|---------|------|-------------|
| Connect / Disconnect (TGXL) | Push button | Default: Connect. Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to TGXL_ManualIp and TGXL_ManualPort on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the broken radio-side path. If IP field is empty and radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Push button | Default: Connect. Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to PGXL_ManualIp and PGXL_ManualPort. |
| Connect / Disconnect (Antenna Genius) | Push button | Default: Connect. Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to AG_ManualIp and AG_ManualPort. |

## APD tab

The **APD** tab configures external Adaptive Pre-Distortion sample port selection per TX antenna (ANT1, ANT2, XVTA, XVTB). This tab is hidden unless the radio reports apd configurable=1 (FLEX-8x00 with SmartSDR 4.2.18+). Added in v26.5.1 (#2186). Lazy-built only when the tab is first clicked.

| Control | Type | Description |
|---------|------|-------------|
| ANT1: / ANT2: / XVTA: / XVTB: | Combo box | Picks the sample port (INTERNAL, RX_A, RX_B, XVTA, XVTB) that the radio uses for APD feedback on that TX antenna. INTERNAL samples inside the radio; external ports require a coupled feedback signal from the linear amplifier output. Changing sends setApdSamplerPort() to the radio. |
| Reset (APD Equalizer) | Push button | Clears all per-antenna APD training data on the radio. Sends resetApdEqualizer() to the radio's TransmitModel. |

## Themes tab

The **Themes** tab configures UI appearance settings including per-slice color overrides. Lazy-built when first clicked.

| Control | Type | Description |
|---------|------|-------------|
| Use
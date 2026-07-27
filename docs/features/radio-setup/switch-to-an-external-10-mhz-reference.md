# Radio Setup Dialog

## Overview

The Radio Setup dialog is the master per-radio configuration window. It provides access to radio information, network settings, GPS, transmit configuration, phone/CW settings, receive calibration, audio, filters, transverters, USB cables, peripherals, serial ports, SmartLink pinned certificate management, KiwiSDR receiver configuration, and APD settings.

To open the dialog, click `Settings > Radio Setup...`. The dialog requires an active radio connection.

## Radio Tab

The Radio tab displays radio identification information, license details, and firmware update controls.

### Information Fields

| Control | Kind | Behavior |
|---------|------|----------|
| Radio SN | Indicator | Chassis serial number (read-only). Includes a clipboard copy button next to the value. |
| Region | Indicator | Radio regulatory region. |
| HW Version | Indicator | Hardware version string. Includes a clipboard copy button. |
| Options | Indicator | Shows licensed radio options. Includes a clipboard copy button. |
| FlexControl | Indicator | Detected state of FlexControl hardware. |
| multiFLEX | Indicator | multiFLEX enabled state. |
| Model | Indicator | Radio model. Includes a clipboard copy button. |
| Nickname | Text field | User-friendly radio nickname. |
| Callsign | Text field | Station callsign. |
| Station Name | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored as `StationName` in AppSettings. Sent to radio as 'client station <name>'. |
| License Info (Subscription / Expiration / Radio ID / Licensed version) | Indicator | Displays license details from the radio. Each field includes a clipboard copy button. |

### Controls

| Control | Kind | Behavior |
|---------|------|----------|
| Remote On | Push button | Enables remote wake / remote-on. |
| Check for Update | Push button | Queries for firmware updates. |
| Select Installer... | Push button | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. |
| Upload Firmware | Push button | Starts firmware upload with progress bar and status. |

## Network Tab

The Network tab displays radio network information and advanced network options.

### Information Fields

| Control | Kind | Behavior |
|---------|------|----------|
| IP Address / Mask / MAC Address | Indicator | Read-only network addresses. Each includes a clipboard copy button. |

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Enforce Private IP Connections: | Toggle button | Enabled | - | Rejects non-RFC1918 peers. |
| Network MTU: | Spinbox | 1450 | 576-9000 bytes | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored as `NetworkMtu` in AppSettings. |
| DHCP / Static | Toggle button | - | - | Switches between DHCP and Static IP modes. |
| IP Address: / Mask: / Gateway: | Text field | - | - | Static IP configuration fields. |
| Apply | Push button | - | - | Pushes the network config to the radio. |

## GPS Tab

The GPS tab displays GPS presence and live position information including latitude, longitude, altitude, time, and satellite count.

## TX Tab

The TX tab controls transmit timings, interlocks, maximum power, tune mode, waterfall display, and slice/TX follow behavior.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| TX Band Settings | Push button | - | - | Opens the dedicated per-band power/tune dialog. |
| Timings (in ms) | Spinbox | - | - | TX hang / delay timings. |
| Interlocks - TX REQ: RCA / Accessory | Toggle button | - | - | Enables RCA and accessory interlock inputs. |
| Max Power: | Spinbox | - | 0-100 % | Sets radio-level TX power cap. |
| Tune Mode: | Combo box | - | - | Selects how the tune button behaves. |
| Show TX in Waterfall: | Toggle button | - | - | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | False | - | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | False | - | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. |

## Phone/CW Tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Enable/Disable the Level Meter During Receive | Toggle button | - | - | Shows mic level meter even in RX. |
| Iambic: | Toggle button | - | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| Iambic Mode: A / B | Push button | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| Swap: | Toggle button | - | - | Swaps dit/dah. |
| Sideband: | Combo box | - | LSB / USB | Selects CW pitch sideband. |
| CWX: | Toggle button | - | - | Enables CWX macro keying. |
| Decode: | Toggle button | True | - | Enables the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`. |
| RTTY Mark Default: | Spinbox | - | - | Default RTTY mark frequency. |

## RX Tab

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Cal Frequency (MHz): | Spinbox | - | - | Frequency used for manual calibration. |
| Start | Push button | - | - | Starts the frequency calibration sweep. |
| Freq Offset (ppb): | Spinbox | - | - | Manual frequency offset in ppb. |
| 10 MHz Reference Source: | Combo box | Auto | Auto / TCXO / GPSDO / External | Selects oscillator reference source. Options shown depend on hardware installed. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

## Audio Tab

The Audio tab manages radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Line Out: | Slider | - | - | Line-out gain. |
| Mute (Line Out) | Push button | - | - | Mutes line-out. |
| Headphone: | Slider | - | - | Headphone gain. |
| Mute (Headphone) | Push button | - | - | Mutes headphone. |
| Front Speaker: / Mute | Push button | - | - | Mutes front speaker (model-specific). |
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Push button | Auto | - | Selects audio codec for SmartLink/LAN. Stored as `AudioCompression`. |
| Prevent system sleep while connected | Checkbox | False | - | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. |
| PC Audio Devices: Input: / Output: | Combo box | - | - | Picks host audio in/out devices. |
| Audio Boost: | Toggle button | - | - | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| Audio Buffer: | Text field | 200 | 50-1000 ms | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Stored as `AudioBufferMs`. |
| Recording: Radio Side / Client Side | Push button | Radio Side | Radio Side / Client Side | Picks radio-side or client-side recording. Stored as `RecordingMode`. |
| Save to: | Text field | - | - | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored as `QsoRecordingDir`. |
| ... | Push button | - | - | Browses for recording folder. |
| Auto-record on TX | Checkbox | False | - | Automatically records while transmitting. Stored as `QsoRecordingAutoRecord`. |
| Idle timeout: | Spinbox | 120 | 10-3600 sec | Seconds of silence before recording stops. Stored as `QsoRecordingIdleTimeout`. |
| NVIDIA BNR: Autostart Container / Start / Stop / Check Status | Push button | - | - | Controls the NVIDIA Broadcast noise-removal container. |

## Filters Tab

The Filters tab provides low-latency and sharp filter options per bandwidth.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Voice / CW / Digital filter sharpness sliders | Slider | - | 0-3 | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. |
| Auto (Voice / CW / Digital) | Toggle button | - | - | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. |
| Use Low Latency Filters for Digital Modes | Checkbox | - | - | Forces low-latency filters in DIGU/DIGL. |

## XVTR Tab

The XVTR tab configures per-transverter settings including RX Only, valid, remove, and create new transverter.

### Controls

| Control | Kind | Behavior |
|---------|------|----------|
| RX Only: | Toggle button | Forces RX-only on that transverter. |
| Remove (xvtr) | Push button | Deletes the transverter definition. |
| Create New Transverter | Push button | Adds a new transverter entry. |

## USB Cables Tab

The USB Cables tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

### Controls

| Control | Kind | Behavior |
|---------|------|----------|
| Cables list / Status | Indicator | Detected USB cables per type with Plugged/Unplugged status. |
| Name: / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0-7) | Combo box | Per-cable serial parameters and behavior. |

## Peripherals Tab

The Peripherals tab manages external devices via manual IP connection (TGXL, PGXL, Antenna Genius).

### Controls

| Control | Kind | Default | Behavior |
|---------|------|---------|----------|
| Connect / Disconnect (TGXL) | Push button | Connect | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. If IP field is empty and radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Push button | Connect | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Connect / Disconnect (Antenna Genius) | Push button | Connect | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |

## APD Tab

The APD tab provides external Adaptive Pre-Distortion sample port selection per TX antenna. The tab is hidden unless the radio reports `apd configurable=1` (FLEX-8x00 with SmartSDR 4.2.18+).

### Controls

| Control | Kind | Behavior |
|---------|------|----------|
| ANT1: / ANT2: / XVTA: / XVTB: | Combo box | Picks the sample port (INTERNAL, RX_A, RX_B, XVTA, XVTB) that the radio uses for APD feedback on that TX antenna. INTERNAL samples inside the radio; external ports require a coupled feedback signal from the linear amplifier output. |
| Reset (APD Equalizer) | Push button | Clears all per-antenna APD training data on the radio. |

## KiwiSDR Tab

The KiwiSDR tab manages connection to KiwiSDR public receivers for remote RX capabilities.

### Controls

| Control | Kind | Default | Behavior |
|---------|------|---------|----------|
| KiwiSDR Receiver URL | Text field | - | URL of the KiwiSDR receiver to connect to. |
| Connect / Disconnect | Push button | Connect | Establishes or tears down the connection to the configured KiwiSDR receiver
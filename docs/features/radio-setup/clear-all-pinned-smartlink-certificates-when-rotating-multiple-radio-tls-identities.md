# Radio Setup Dialog

The **Radio Setup** dialog is the master per-radio configuration window. It contains radio information, network settings, GPS, TX, Phone/CW, RX, audio, filters, XVTR, USB cables, peripherals serial port, SmartLink pinned certificate management, and KiwiSDR public receiver settings.

## Opening the dialog

1. Click **Settings > Radio Setup...** in the main menu.

## Radio (tab)

The Radio tab displays radio identification, license information, and provides firmware update controls.

### Read-only indicators with copy buttons

All read-only fields include a clipboard copy button (tray icon) next to the label for easy sharing with support.

| Control | Behavior |
|---------|----------|
| **Radio SN** | Chassis serial number (read-only). Includes a clipboard copy button. |
| **Region** | Radio regulatory region (read-only). Includes a clipboard copy button. |
| **HW Version** | Hardware version string (read-only). Includes a clipboard copy button. |
| **Options** | Shows licensed radio options (read-only). Includes a clipboard copy button. |
| **Model** | Radio model (read-only). Includes a clipboard copy button. |
| **License Info** fields | Displays Subscription, Expiration, Radio ID, and Licensed version. Each includes a clipboard copy button. |

### Other controls on the Radio tab

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **FlexControl** | Detected state of FlexControl hardware. | (none) |
| **multiFLEX** | multiFLEX enabled state. | (none) |
| **Nickname** | User-friendly radio nickname. | (none) |
| **Callsign** | Station callsign. | (none) |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. | `StationName` |
| **Remote On** | Enables remote wake / remote-on. | (none) |
| **Check for Update** | Queries for firmware updates. | (none) |
| **Select Installer...** | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. | (none) |
| **Upload Firmware** | Starts firmware upload with progress bar and status. | (none) |

## Network (tab)

Advanced network configuration for the radio.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each includes a clipboard copy button. | (none) |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers. Toggle button displays "Enabled" when checked. | (none) |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes (576-9000). Default 1450. | `NetworkMtu` |
| **DHCP / Static** | Switches between DHCP and Static IP modes. | (none) |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields (shown when Static mode is selected). | (none) |
| **Apply** | Pushes the network config to the radio. | (none) |
| **Reboot Radio** | Opens a confirmation dialog before rebooting the radio. AetherSDR disconnects and, for LAN connections, automatically reconnects after the radio boots. SmartLink/WAN requires manual reconnect. Button is disabled when radio is disconnected. | (none) |

## GPS (tab)

Displays GPS presence and live location/time/satellite information.

## TX (tab)

Transmit configuration including timings, interlocks, power limits, and slice follow behavior.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **TX Band Settings** | Opens the dedicated per-band power/tune dialog. | (none) |
| **Timings (in ms)** | TX hang / delay timings. | (none) |
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs. | (none) |
| **Max Power:** | Sets radio-level TX power cap (0-100%). | (none) |
| **Tune Mode:** | Selects how the tune button behaves. | (none) |
| **Show TX in Waterfall:** | Draws TX signal in the waterfall. | (none) |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. | `TxFollowsActiveSlice` |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. | `ActiveFollowsTxSlice` |

## Phone/CW (tab)

Microphone, CW keyer, and RTTY defaults.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. | (none) |
| **Iambic:** | Enables or disables the iambic keyer on the radio. | (none) |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | (none) |
| **Swap:** | Swaps dit/dah. | (none) |
| **Sideband:** | Selects CW pitch sideband (LSB/USB). | (none) |
| **CWX:** | Enables CWX macro keying. | (none) |
| **Decode:** | Enables the CW decode overlay on the panadapter. | `CwDecodeOverlay` |
| **RTTY Mark Default:** | Default RTTY mark frequency. | (none) |

## RX (tab)

GPSDO frequency offset calibration and 10 MHz reference source.

| Control | Behavior |
|---------|----------|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. |
| **Start** | Starts the frequency calibration sweep. |
| **Freq Offset (ppb):** | Manual frequency offset in ppb. |
| **10 MHz Reference Source:** | Selects oscillator reference source (Auto/TCXO/GPSDO/External). Lock status shown alongside. |

## Audio (tab)

Radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **Line Out:** | Line-out gain slider. | (none) |
| **Mute (Line Out)** | Mutes line-out. | (none) |
| **Headphone:** | Headphone gain slider. | (none) |
| **Mute (Headphone)** | Mutes headphone. | (none) |
| **Front Speaker: / Mute** | Mutes front speaker (model-specific). | (none) |
| **Audio Compression (SmartLink):** | Selects audio codec for SmartLink/LAN (Auto/Uncompressed/Opus). | `AudioCompression` |
| **Prevent system sleep while connected** | Keeps OS awake while radio is connected. | `InhibitSleepWhileConnected` |
| **PC Audio Devices: Input: / Output:** | Picks host audio in/out devices. | (none) |
| **Audio Boost:** | Enables extra gain on the client audio path. | `AudioBoost` |
| **Audio Buffer:** | Increases audio buffer in milliseconds for VPN/SmartLink jitter (50-1000 ms). Default 200. | `AudioBufferMs` |
| **Recording: Radio Side / Client Side** | Picks radio-side or client-side recording. | `RecordingMode` |
| **Save to:** | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. | `QsoRecordingDir` |
| **...** | Browses for recording folder. | (none) |
| **Auto-record on TX** | Automatically records while transmitting. | `QsoRecordingAutoRecord` |
| **Idle timeout:** | Seconds of silence before recording stops (10-3600 sec). Default 120. | `QsoRecordingIdleTimeout` |
| **NVIDIA BNR: Autostart Container / Start / Stop / Check Status** | Controls the NVIDIA Broadcast noise-removal container. | (none) |

## Filters (tab)

Low-latency and sharp filter options per bandwidth.

| Control | Behavior |
|---------|----------|
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. |
| **Use Low Latency Filters for Digital Modes** | Forces low-latency filters in DIGU/DIGL. |

## XVTR (tab)

Per-transverter configuration.

| Control | Behavior |
|---------|----------|
| **RX Only:** | Forces RX-only on that transverter. |
| **Remove (xvtr)** | Deletes the transverter definition. |
| **Create New Transverter** | Adds a new transverter entry. |

## USB Cables (tab)

Assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

| Control | Behavior |
|---------|----------|
| **Cables list / Status** | Detected USB cables per type with Plugged/Unplugged status. |
| **Name: / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0-7)** | Per-cable serial parameters and behavior. |

## Peripherals (tab)

External devices manual IP connection.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **Connect / Disconnect (TGXL)** | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to settings. | `TGXL_ManualIp`, `TGXL_ManualPort` |
| **Connect / Disconnect (PGXL)** | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). | `PGXL_ManualIp`, `PGXL_ManualPort` |
| **Connect / Disconnect (Antenna Genius)** | Opens/closes connection to the Antenna Genius (default port 9007). | `AG_ManualIp`, `AG_ManualPort` |

## APD (tab)

External Adaptive Pre-Distortion sample port selection per TX antenna. Tab is hidden unless the radio reports APD configurable (FLEX-8x00 with SmartSDR 4.2.18+).

| Control | Behavior |
|---------|----------|
| **ANT1: / ANT2: / XVTA: / XVTB:** | Picks the sample port (INTERNAL, RX_A, RX_B, XVTA, XVTB) that the radio uses for APD feedback on that TX antenna. |
| **Reset (APD Equalizer)** | Clears all per-antenna APD training data on the radio. |

## Themes (tab)

UI appearance settings including per-slice color overrides.

| Control | Behavior |
|---------|----------|
| **Use Aether defaults** | Uses the built-in slice color palette (cyan/magenta/green/yellow/orange/teal/coral/lavender). |
| **Custom colors** | Enables per-slice color pickers (A-H). |
| **A/B/C/D/E/F/G/H color buttons** | Click to open a color picker for that slice letter. The button's background reflects the currently assigned color. |
| **Reset All to Defaults** | Resets every per-slice custom color to its built-in default. |

## SmartLink (tab)

Pinned SmartLink TLS certificate management. Lists each pinned certificate with per-row **Forget** and **Forget All** controls.

| Control | Behavior |
|---------|----------|
| **Pinned SmartLink Certificates** section | Lists every host this client has pinned on first connect. Shows Host, SHA-256 fingerprint, and Pinned date. |
| **Host / SHA-256 fingerprint / Pinned** (table columns) | 3-column read-only table: Host (hostname), SHA-256 fingerprint (monospace), Pinned (YYYY-MM-DD or '(pre-phase 2)'). |
| **Forget selected** | Removes the selected host's pinned certificate. Next connect to that host re-pins silently. |
| **Forget all** | Clears every pinned certificate after a confirmation prompt. Next connect to each radio silently re-pins. |

## Serial (tab)

FlexControl serial port configuration (build-gated by `HAVE_SERIALPORT`).

| Control | Behavior |
|---------|----------|
| **Port / Refresh / Path** | Picks/edits the serial device. |
| **Baud / Data / Parity / Stop** | Serial line parameters. |
| **DTR / RTS: Function / Polarity** | Assigns signal function and polarity. |
| **Paddle Swap (swap dit/dah)** | Swaps dit/dah for paddle. |
| **Auto-open serial port on startup** | Reopens the port on app launch. |
| **FlexControl Tuning Knob: Detect / Close** | Detects or closes a FlexControl knob. |
| **Auto-detect on startup / Invert tuning direction** | FlexControl startup and direction preferences. |

## KiwiSDR (tab) — new in v26.7.4

Public KiwiSDR receiver configuration. This tab provides settings for connecting to KiwiSDR public receivers and managing automation bridge connections
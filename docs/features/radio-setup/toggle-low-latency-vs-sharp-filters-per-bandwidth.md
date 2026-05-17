# Radio Setup Dialog

The Radio Setup dialog is the master configuration window for per-radio settings including radio information, network, GPS, TX, Phone/CW, RX, audio, filters, antennas, transverters, USB cables, peripherals, APD, themes, and serial port configuration.

## Opening the dialog

- Click `Settings > Radio Setup...` while connected to a radio.

## Dialog layout

The dialog contains a tabbed interface with the following tabs:

- **Radio** - Radio information, identification, license info, and firmware update
- **Network** - Network information and advanced network options
- **GPS** - GPS presence and live lat/lon/alt/time/satellites info
- **TX** - TX timings, interlocks, max power, tune mode, and slice/TX follow settings
- **Phone/CW** - Microphone, CW keyer, RTTY defaults
- **RX** - GPSDO frequency offset calibration and 10 MHz reference source
- **Antennas** - Antenna name configuration
- **Filters** - Low-latency / Sharp filter options per bandwidth
- **XVTR** - Per-transverter configuration
- **USB Cables** - USB serial adapter assignment
- **Peripherals** - External device manual IP connection (TGXL, PGXL, Antenna Genius)
- **APD** - External Adaptive Pre-Distortion sample port selection (FLEX-8x00 only)
- **Themes** - UI appearance settings including per-slice color overrides
- **Serial** - FlexControl serial port configuration

The dialog remembers its size and position between sessions using `RadioSetupDialogGeometry` in AppSettings.

## Radio tab

The Radio tab displays radio identification and license information, and provides firmware update controls.

### Radio information

| Control | Kind | Behavior |
|---|---|---|
| **Radio SN** | Indicator | Chassis serial number (read-only). |
| **Region** | Indicator | Radio regulatory region. |
| **HW Version** | Indicator | Hardware version string. |
| **Model** | Indicator | Radio model. |
| **Options** | Indicator | Shows licensed radio options. |
| **FlexControl** | Indicator | Detected state of FlexControl hardware. |
| **multiFLEX** | Indicator | multiFLEX enabled state. |
| **License Info** | Indicator | Displays subscription, expiration, radio ID, and licensed version from the radio. |

### Radio identification

| Control | Kind | Behavior |
|---|---|---|
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings. Sent to radio as `client station <name>`. |

### Remote On

| Control | Kind | Behavior |
|---|---|---|
| **Remote On** | Push button | Enables remote wake / remote-on. |

### Firmware update

| Control | Kind | Behavior |
|---|---|---|
| **Check for Update** | Push button | Queries for firmware updates from the radio. |
| **Select Installer...** | Push button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes and extracts the `.ssdr` without external tools. |
| **Upload Firmware** | Push button | Starts firmware upload with progress bar and status. |
| Firmware status | Indicator | Empty until a firmware upload begins, then progress and result text. |

#### Firmware update workflow

When **Check for Update** finds a newer version, the status area instructs you to download the SmartSDR installer from flexradio.com yourself. Use **Select Installer...** to point AetherSDR at the file you downloaded.

**Supported installer formats**

| File type | Description |
|---|---|
| `.msi` | FlexRadio WiX installer (SmartSDR v4.2 and later). Recommended. |
| `.exe` | Older self-extracting installer (pre-v4.2 releases). |
| `.ssdr` | Pre-extracted firmware file. |

**Steps**

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**. If an update is available, the status area displays the version number and instructs you to download the installer from flexradio.com.
4. Download the SmartSDR installer from flexradio.com.
5. Click **Select Installer...** and locate the downloaded `.msi`, `.exe`, or `.ssdr` file. AetherSDR stages the firmware and reports progress in the status area.
6. When staging completes, click **Upload Firmware** to transfer the firmware to the radio.

## Network tab

The Network tab displays radio network information and provides advanced network configuration.

### Network information

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator | Read-only network addresses. |

### Network configuration

| Control | Kind | Behavior |
|---|---|---|
| **Enforce Private IP Connections** | Toggle button | Rejects non-RFC1918 peers. |
| **Network MTU** | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range 576-9000 bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. |
| **DHCP / Static** | Toggle button | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text field | Static IP configuration fields. |
| **Apply** | Push button | Pushes the network config to the radio. |

## GPS tab

The GPS tab displays GPS presence and live positioning information.

| Control | Kind | Behavior |
|---|---|---|
| GPS info | Indicator | Live lat/lon/alt/time/satellites info. |

## TX tab

The TX tab provides transmit timing, interlock, power, and slice/TX follow settings.

### TX Band Settings

| Control | Kind | Behavior |
|---|---|---|
| **TX Band Settings** | Push button | Opens the dedicated per-band power/tune dialog. |

### Timings

| Control | Kind | Behavior |
|---|---|---|
| **ACC TX:** | Spinbox | ACC TX delay in milliseconds. |
| **TX Delay:** | Spinbox | TX delay in milliseconds. |
| **RCA TX1:** | Spinbox | RCA TX1 delay in milliseconds. |
| **Timeout (sec):** | Spinbox | Interlock timeout in seconds (range 0-3600). The radio stores this value in milliseconds internally. |
| **TX2:** | Spinbox | TX2 delay in milliseconds. |

### Interlocks

| Control | Kind | Behavior |
|---|---|---|
| **TX REQ: RCA** | Toggle button | Enables RCA interlock input. |
| **TX REQ: Accessory** | Toggle button | Enables accessory interlock input. |

### Power and Tune

| Control | Kind | Behavior |
|---|---|---|
| **Max Power:** | Spinbox | Sets radio-level TX power cap (0-100%). |
| **Tune Mode:** | Combo box | Selects how the tune button behaves. |

### Waterfall display

| Control | Kind | Behavior |
|---|---|---|
| **Show TX in Waterfall:** | Toggle button | Draws TX signal in the waterfall. |

### Slice/TX follow behavior

| Control | Kind | Behavior |
|---|---|---|
| **TX Follows Active Slice** | Push button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored as `TxFollowsActiveSlice`. Default: False. |
| **Active Slice Follows TX** | Push button | Switches the active slice when TX moves externally (e.g., WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored as `ActiveFollowsTxSlice`. Default: False. |

## Phone/CW tab

The Phone/CW tab provides microphone, CW keyer, and RTTY configuration.

### Microphone

| Control | Kind | Behavior |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle button | Shows mic level meter even in RX. |

### CW Keyer

| Control | Kind | Behavior |
|---|---|---|
| **Iambic:** | Toggle button | Enables/disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Push button | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. Default: A. |
| **Swap:** | Toggle button | Swaps dit/dah. |
| **Sideband:** | Combo box | Selects CW pitch sideband (LSB | USB). |
| **CWX:** | Toggle button | Enables CWX macro keying. |
| **Decode:** | Toggle button | Enables the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`. Default: True. |

### RTTY

| Control | Kind | Behavior |
|---|---|---|
| **RTTY Mark Default:** | Spinbox | Default RTTY mark frequency. |

## RX tab

The RX tab provides frequency calibration and reference source selection.

### Frequency calibration

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | Frequency used for manual calibration. |
| **Start** | Push button | Resets the frequency error to 0 ppb, applies the calibration frequency, and starts the PLL calibration sweep. Disabled and labelled "Busy" while a calibration is in progress. |
| **Freq Offset (ppb):** | Spinbox | Manual frequency offset in parts per billion. |

### 10 MHz Reference Source

| Control | Kind | Behavior |
|---|---|---|
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference: Auto, TCXO, GPSDO, or External 10 MHz. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

### Calibration procedure

1. Click `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz)**.
4. Click **Start**. AetherSDR resets the frequency error to 0 ppb, sets the calibration frequency, and starts the PLL calibration sweep. The status field beside the Start button updates as the calibration progresses.
5. While calibration is running, the **Start** button is disabled and shows "Busy". It re-enables when calibration completes or fails.
6. Adjust **Freq Offset (ppb)** manually if needed after calibration completes.

## Antennas tab

The Antennas tab provides antenna name configuration.

| Control | Kind | Behavior |
|---|---|---|
| Antenna name fields | Text field | Per-antenna name configuration for ANT1, ANT2, XVTA, and XVTB. |

## Audio tab

The Audio tab provides radio audio output, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container controls.

### Radio audio outputs

| Control | Kind | Behavior |
|---|---|---|
| **Line Out:** | Slider | Line-out gain. |
| **Mute (Line Out)** | Push button | Mutes line-out. |
| **Headphone:** | Slider | Headphone gain. |
| **Mute (Headphone)** | Push button | Mutes headphone. |
| **Front Speaker: / Mute** | Push button | Mutes front speaker (model-specific). |

### Audio Compression (SmartLink)

| Control | Kind | Behavior |
|---|---|---|
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Push button | Selects audio codec for SmartLink/LAN. Stored as `AudioCompression`. Default: Auto. |

### System sleep prevention

| Control | Kind | Behavior |
|---|---|---|
| **Prevent system sleep while connected** | Checkbox | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. Default: False. |

### PC Audio Devices

| Control | Kind | Behavior |
|---|---|---|
| **PC Audio Devices: Input:** | Combo box | Picks host audio input device. |
| **PC Audio Devices: Output:** | Combo box | Picks host audio output device. |

### Audio boost and buffer

| Control | Kind | Behavior |
|---|---|---|
| **Audio Boost:** | Toggle button | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| **Audio Buffer:** | Text field | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Range 50-1000 ms. Stored as `AudioBufferMs`. Default: 200. |

### Recording

| Control | Kind | Behavior |
|---|---|---|
| **Recording: Radio Side / Client Side** | Push button | Picks radio-side or client-side recording. Stored as `RecordingMode`. Default: Radio Side. |
| **Save to:** | Text field | Folder for saved recordings (client-side only). Stored as `QsoRecordingDir`. Defaults to Documents/AetherSDR/Recordings. |
| **...** | Push button | Browses for recording folder. |
| **Auto-record on TX** | Checkbox | Automatically records while transmitting. Stored as `QsoRecordingAutoRecord`. Default: False. |
| **Idle timeout:** | Spinbox | Seconds of silence before recording stops. Range 10-3600 sec. Stored as `QsoRecordingIdleTimeout`. Default: 
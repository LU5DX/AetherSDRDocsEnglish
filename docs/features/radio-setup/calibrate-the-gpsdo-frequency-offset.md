# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, Phone/CW, RX, Antennas, Audio, Filters, XVTR, USB cables, peripherals, APD, Themes, SmartLink, and Serial (FlexControl).

## Opening Radio Setup

1. Click **Settings** in the main menu.
2. Select **Radio Setup...**.

The dialog remembers its position and size between sessions.

## Radio (tab)

The Radio tab shows radio identification, license information, and firmware update controls. Each read-only value has a copy button that appears with a document icon on hover or focus; click it to copy the value to the clipboard. A brief "Copied!" popup confirms the action.

### Radio information

The following fields are read-only indicators of the connected radio:

| Control | Description |
|---|---|
| **Radio SN** | Chassis serial number (read-only). Includes a clipboard copy button (tray icon) next to the value. |
| **Region** | Radio regulatory region (e.g., USA). |
| **HW Version** | Hardware version string. Includes a clipboard copy button next to the value. |
| **Options** | Licensed radio options. Includes a clipboard copy button next to the value. |
| **FlexControl** | Detected state of FlexControl hardware. |
| **multiFLEX** | multiFLEX enabled state. |
| **Model** | Radio model. Includes a clipboard copy button next to the value. |
| **License Info** | Subscription details, expiration date, Radio ID, and licensed version. Each field includes a clipboard copy button next to the value. |

### Radio identification fields

| Control | Description |
|---|---|
| **Nickname** | User-friendly radio nickname. |
| **Callsign** | Station callsign. |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Setting key: `StationName`. |

### Remote control and reboot

| Control | Description |
|---|---|
| **Remote On** | Enables remote wake / remote-on. |
| **Reboot Radio** | Reboots the connected radio. Click to see a confirmation dialog. On LAN connections, AetherSDR automatically reconnects after the radio finishes booting. On SmartLink/WAN connections, you must reconnect manually. The button is disabled when the radio is disconnected. |

### Firmware update

| Control | Description |
|---|---|
| **Check for Update** | Queries for firmware updates. |
| **Select Installer...** | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. |

1. Click **Check for Update** to query for firmware updates. If an update is available, the status label displays the version number and instructs you to download the installer.
2. Download the installer from flexradio.com (`.msi` for SmartSDR 4.2+, `.exe` for older releases).
3. Click **Select Installer...** and choose the downloaded file. AetherSDR accepts `.msi`, `.exe`, or a pre-extracted `.ssdr` file and stages the firmware automatically.
4. Click **Upload Firmware** to transfer the staged firmware to the radio. A progress bar and status text show the upload progress.

## Network (tab)

The Network tab displays radio network information and provides advanced network options.

### Network information

| Control | Description |
|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each includes a clipboard copy button. |

### Network settings

| Control | Description |
|---|---|
| **Enforce Private IP Connections** | Toggle to reject non-RFC1918 peers. |
| **Network MTU** | Sets maximum outgoing VITA-49 UDP packet size in bytes. Valid range: 576-9000 bytes. Default: 1450. Setting key: `NetworkMtu`. Default 1450 is safe for most VPN/SD-WAN tunnels. |

### IP configuration

1. Switch between **DHCP** and **Static** using the toggle button.
2. In Static mode, enter the **IP Address**, **Mask**, and **Gateway**.
3. Click **Apply** to push the network configuration to the radio.

## GPS (tab)

The GPS tab shows GPS presence and live information including latitude, longitude, altitude, time, and satellite count.

## TX (tab)

The TX tab provides transmit configuration including timings, interlocks, power limits, tune mode, and waterfall display options.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

| Control | Description |
|---|---|
| **Timings (in ms)** | TX hang / delay timings. |

### Interlocks

| Control | Description |
|---|---|
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs. |

### Power and tune

| Control | Description |
|---|---|
| **Max Power** | Sets radio-level TX power cap. Valid range: 0-100%. |
| **Tune Mode** | Selects how the tune button behaves. |

### Waterfall and slice tracking

| Control | Description |
|---|---|
| **Show TX in Waterfall** | Draws TX signal in the waterfall. |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Setting key: `TxFollowsActiveSlice`. Default: False. |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g., WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Setting key: `ActiveFollowsTxSlice`. Default: False. |

## Phone/CW (tab)

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### Microphone

| Control | Description |
|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. |

### CW keyer

| Control | Description |
|---|---|
| **Iambic** | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. Default: A. |
| **Swap** | Swaps dit/dah. |
| **Sideband** | Selects CW pitch sideband. Valid range: LSB, USB. |
| **CWX** | Enables CWX macro keying. |
| **Decode** | Enables the CW decode overlay on the panadapter. Setting key: `CwDecodeOverlay`. Default: True. |

### RTTY

| Control | Description |
|---|---|
| **RTTY Mark Default** | Default RTTY mark frequency. |

## RX (tab)

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

### Frequency calibration

1. In **Cal Frequency (MHz):**, enter the frequency of a known-accurate reference signal.
2. Click **Start** to begin the calibration sweep. The button label changes to **Busy** while the sweep runs.
3. When the sweep completes, review the measured offset in **Freq Offset (ppb):**.
4. If you prefer to set the offset manually, edit **Freq Offset (ppb):** directly.

### Calibration status messages

| Message | Colour | Meaning |
|---|---|---|
| Starting... | Blue-grey | The calibration command sequence has been sent to the radio. |
| Enter cal frequency | Amber | **Cal Frequency (MHz):** was empty when **Start** was clicked. |
| Busy | — | Shown on the **Start** button itself while a sweep is in progress. |

### 10 MHz reference source

| Control | Description |
|---|---|
| **10 MHz Reference Source** | Selects oscillator reference source. Valid values: Auto, TCXO, GPSDO, External 10 MHz. Options shown depend on hardware installed. |

The lock status label beside the combo box displays the current oscillator state:

| Display | Meaning |
|---|---|
| `Auto -> GPSDO` (locked) | Auto selected, radio chose GPSDO, locked |
| `GPSDO` (locked) | Source matched and locked |
| `External 10 MHz` (not detected) | External selected but no signal detected |

Colour coding:
- Green (`#00c040`): Oscillator is locked.
- Red (`#c04040`): Oscillator is unlocked.
- Blue-grey (`#8aa8c0`): Oscillator state not yet received.

### GPSDO status banner

- **Green banner**: GPSDO is installed. Manual frequency offset calibration is available.
- **Amber banner**: No GPSDO installed. Manual frequency offset calibration is available.

## Antennas (tab)

The Antennas tab allows you to assign custom names to each antenna port on the radio.

### Steps

1. Select an antenna port from the list.
2. Enter a custom name in the text field.
3. The name is sent to the radio and appears in antenna selection controls throughout AetherSDR.

## Audio (tab)

The Audio tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

### Radio audio outputs

| Control | Description |
|---|---|
| **Line Out** | Line-out gain slider. |
| **Mute (Line Out)** | Mutes line-out. |
| **Headphone** | Headphone gain slider. |
| **Mute (Headphone)** | Mutes headphone. |
| **Front Speaker / Mute** | Mutes front speaker (model-specific). |

### Audio compression

| Control | Description |
|---|---|
| **Audio Compression (SmartLink)** | Selects audio codec for SmartLink/LAN. Options: Auto, Uncompressed, Opus. Setting key: `AudioCompression`. Default: Auto. |

### Power management

| Control | Description |
|---|---|
| **Prevent system sleep while connected** | Keeps OS awake while radio is connected. Setting key: `InhibitSleepWhileConnected`. Default: False. |

### PC audio devices

| Control | Description |
|---|---|
| **PC Audio Devices: Input / Output** | Picks host audio input and output devices. |

### Audio boost and buffer

| Control | Description |
|---|---|
| **Audio Boost** | Enables extra gain on the client audio path. Setting key: `AudioBoost`. |
| **Audio Buffer** | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Valid range: 50-1000 ms. Default: 200. Setting key: `AudioBufferMs`. |

### Recording

| Control | Description |
|---|---|
| **Recording** | Picks radio-side or client-side recording. Setting key: `RecordingMode`. Default: Radio Side. |
| **Save to** | Folder for saved recordings (client-side only). Setting key: `QsoRecordingDir`. Defaults to Documents/AetherSDR/Recordings. |
| **...** | Browses for recording folder. |
| **Auto-record on TX** | Automatically records while transmitting. Setting key: `QsoRecordingAutoRecord`. Default: False. |
| **Idle timeout** | Seconds of silence before recording stops. Valid range: 10-3600 sec. Default: 120. Setting key: `QsoRecordingIdleTimeout`. |

### NVIDIA BNR

| Control | Description |
|---|---|
| **Autostart Container** | Enables automatic start of the NVIDIA Broadcast noise-removal container. |
| **Start** | Starts the NVIDIA BNR container. |
| **Stop** | Stops the NVIDIA BNR container. |
| **Check Status** | Checks the running state of the container. |

A coloured status dot indicates the container state: green for Running, red for Stopped, grey for Unknown.

## Filters (tab)

The Filters tab provides low-latency and sharp filter options per bandwidth mode.

### Filter sharpness

| Control | Description |
|---|---|
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness per mode (0=lowest latency to 3=sharpest). Disabled when Auto is enabled. |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode. Disables the manual sharpness slider. |

### Digital mode filters

| Control | Description |
|---|---|
| **Use Low Latency Filters for Digital Modes** | Forces low-latency filters in DIGU/DIGL. |

## XVTR (tab)

The XVTR tab provides per-transverter configuration. It contains nested tabs, one per configured transverter, plus a '+' tab for creating new ones.

### Transverter management

| Control | Description |
|---|---|
| **RX Only** | Forces RX-only on that transverter. |
| **Remove** | Deletes the transverter definition. |
| **Create New Transverter** | Adds a new transverter entry. |

## USB Cables (tab)

The USB Cables tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

### Cable configuration

| Control | Description |
|---|---|
| **Cables list / Status** | Detected USB cables per type with Plugged/Unplugged status. |
| **Name** | Cable name. |
| **Enabled** | Enables the cable. |
| **Speed** | Baud rate. |
| **Data Bits** | Data bits configuration. |
| **Parity** | Parity setting. |
| **Stop Bits** | Stop bits setting. |
| **Flow** | Flow control. |
| **Source** | Cable source. |
| **Auto Report**
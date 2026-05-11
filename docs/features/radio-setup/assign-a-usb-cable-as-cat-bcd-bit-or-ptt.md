# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network settings, GPS, TX configuration, Phone/CW, RX calibration, audio, filters, transverters, USB cables, peripherals, serial ports, APD, and themes.

## Opening the Radio Setup dialog

- Select `Settings > Radio Setup...` from the main menu.

## Radio tab

The Radio tab displays radio identification, licensing information, and firmware update controls.

### Radio information (read-only)

| Control | Description |
|---|---|
| **Radio SN** | Chassis serial number. |
| **Region** | Regulatory region (USA by default). |
| **HW Version** | Hardware version string. |
| **Options** | Licensed radio options. |
| **FlexControl** | Detected state of FlexControl hardware. |
| **multiFLEX** | multiFLEX enabled state. |
| **Model** | Radio model. |

### User-configurable fields

| Control | Description | Notes |
|---|---|---|
| **Nickname** | User-friendly radio nickname. | |
| **Callsign** | Station callsign. | |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. | Defaults to the OS hostname if empty. Stored in AppSettings with key `StationName`. Sent to radio as "client station <name>". |

### License information

The **License Info** section displays subscription status, expiration date, radio ID, and licensed version.

### Firmware update

| Control | Description |
|---|---|
| **Check for Update** | Queries for firmware updates. |
| **Select Installer...** | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. |
| **Firmware status** | Empty until a firmware upload begins, then shows progress and result text. |

### Remote control

| Control | Description |
|---|---|
| **Remote On** | Enables remote wake / remote-on. |

## Network tab

The Network tab displays radio network information and provides network configuration options.

### Network information (read-only)

| Control | Description |
|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. |

### Network settings

| Control | Default | Range | Setting Key | Description |
|---|---|---|---|---|
| **Enforce Private IP Connections:** | | | | Rejects non-RFC1918 peers. |
| **Network MTU:** | 1450 | 576-9000 bytes | `NetworkMtu` | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. |
| **DHCP / Static** | | | | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | | | | Static IP configuration fields (visible only in Static mode). |
| **Apply** | | | | Pushes the network configuration to the radio. |

## GPS tab

The GPS tab displays GPS presence and live position data.

| Control | Description |
|---|---|
| GPS status | Shows lat/lon/alt/time/satellites information when a GPS is installed and active. |

## TX tab

The TX tab controls transmit timings, interlocks, power limits, tuning modes, and slice/TX follow behavior.

### TX band settings

| Control | Description |
|---|---|
| **TX Band Settings** | Opens the dedicated per-band power/tune dialog. |

### Timings

| Control | Description |
|---|---|
| **Timings (in ms)** | TX hang / delay timings. |

### Interlocks

| Control | Description |
|---|---|
| **TX REQ: RCA** | Enables RCA interlock input. |
| **TX REQ: Accessory** | Enables accessory interlock input. |

### Power and tuning

| Control | Default | Range | Description |
|---|---|---|---|
| **Max Power:** | | 0-100% | Sets radio-level TX power cap. |
| **Tune Mode:** | | | Selects how the tune button behaves. |

### Waterfall display

| Control | Description |
|---|---|
| **Show TX in Waterfall:** | When enabled, the TX signal is drawn in the waterfall display. |

### Slice/TX follow behavior

| Control | Default | Setting Key | Description |
|---|---|---|---|
| **TX Follows Active Slice** | False | `TxFollowsActiveSlice` | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | False | `ActiveFollowsTxSlice` | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### Level meter

| Control | Description |
|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. |

### CW keyer

| Control | Default | Range | Description |
|---|---|---|---|
| **Iambic:** | | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| **Swap:** | | | Swaps dit/dah. |
| **Sideband:** | | LSB / USB | Selects CW pitch sideband. |
| **CWX:** | | | Enables CWX macro keying. |

### Decode

| Control | Default | Setting Key | Description |
|---|---|---|---|
| **Decode:** | True | `CwDecodeOverlay` | Enables the CW decode overlay on the panadapter. |

### RTTY

| Control | Description |
|---|---|
| **RTTY Mark Default:** | Default RTTY mark frequency. |

## RX tab

The RX tab provides frequency calibration controls and 10 MHz reference source selection.

### Frequency calibration

The calibration controls are visible regardless of whether a GPSDO is installed.

- If a GPSDO is installed, a green status line reads "GPSDO installed. Manual frequency offset calibration available."
- If no GPSDO is installed, a yellow status line reads "Manual frequency offset calibration available."

#### Calibration procedure

1. Open `Settings > Radio Setup...` and click the **RX** tab.
2. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
3. Click **Start**. The button changes to **Busy** and is disabled while calibration runs. A status label to the right of the button shows progress text.
   - "Starting…" appears immediately.
   - If you leave the **Cal Frequency (MHz):** field empty and click **Start**, the status label shows "Enter cal frequency" in amber and the calibration does not start.
4. Wait for the status label to indicate completion. The **Start** button re-enables automatically.
5. Confirm or adjust the result using **Freq Offset (ppb):**.

| Control | Description | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for calibration, entered in MHz to six decimal places. | Sent to the radio as `radio set cal_freq=<value>`. |
| **Start** | Begins the calibration sweep. Disabled and labelled **Busy** while a calibration is in progress. | Resets `freq_error_ppb` to 0 before starting. Requires a non-empty cal frequency. |
| **Freq Offset (ppb):** | Manual frequency offset correction in parts per billion. | |

### 10 MHz reference

| Control | Default | Range | Description | Notes |
|---|---|---|---|---|
| **10 MHz Reference Source:** | Auto | Auto / TCXO / GPSDO / External | Selects oscillator reference source. Options shown depend on hardware installed. | Lock status (Locked / Unlocked) is shown alongside the combo and updates live. When Auto is selected and the radio has resolved to a specific source, the label shows "Auto -> <source>" to indicate the active hardware. If an External 10 MHz source is selected but no external signal is detected, the label appends "(not detected)". The label reads "Waiting for oscillator status" until the radio reports its first oscillator state. |

## Audio tab

The Audio tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR.

### Radio audio outputs

| Control | Description |
|---|---|
| **Line Out:** | Line-out gain slider. |
| **Mute (Line Out)** | Mutes line-out. |
| **Headphone:** | Headphone gain slider. |
| **Mute (Headphone)** | Mutes headphone. |
| **Front Speaker:** / **Mute** | Mutes front speaker (model-specific). |

### Audio compression

| Control | Default | Setting Key | Description |
|---|---|---|---|
| **Audio Compression (SmartLink):** | Auto | `AudioCompression` | Selects audio codec for SmartLink/LAN: Auto, Uncompressed, or Opus. |

### System sleep

| Control | Default | Setting Key | Description |
|---|---|---|---|
| **Prevent system sleep while connected** | False | `InhibitSleepWhileConnected` | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. |

### PC audio devices

| Control | Description |
|---|---|
| **PC Audio Devices: Input:** | Picks host audio input device. |
| **PC Audio Devices: Output:** | Picks host audio output device. |

### Audio boost and buffer

| Control | Default | Range | Setting Key | Description |
|---|---|---|---|---|
| **Audio Boost:** | | | `AudioBoost` | Enables extra gain on the client audio path. |
| **Audio Buffer:** | 200 | 50-1000 ms | `AudioBufferMs` | Increases audio buffer in milliseconds for VPN/SmartLink jitter. |

### Recording

| Control | Default | Range | Setting Key | Description |
|---|---|---|---|---|
| **Recording:** | Radio Side | Radio Side / Client Side | `RecordingMode` | Picks radio-side or client-side recording. |
| **Save to:** | | | `QsoRecordingDir` | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. |
| **...** | | | | Browses for recording folder. |
| **Auto-record on TX** | False | | `QsoRecordingAutoRecord` | Automatically records while transmitting. |
| **Idle timeout:** | 120 | 10-3600 sec | `QsoRecordingIdleTimeout` | Seconds of silence before recording stops. |

### NVIDIA BNR

| Control | Description |
|---|---|
| **NVIDIA BNR: Autostart Container** | Enables automatic container startup. |
| **NVIDIA BNR: Start / Stop** | Manually starts or stops the NVIDIA Broadcast noise-removal container. |
| **NVIDIA BNR: Check Status** | Checks container status. |
| **NVIDIA BNR status dot** | Colored dot indicating container Running/Stopped/Unknown. |

## Filters tab

The Filters tab configures filter sharpness per mode.

### Filter sharpness

| Control | Range | Description | Notes |
|---|---|---|---|
| **Voice / CW / Digital filter sharpness sliders** | 0-3 | Sets filter sharpness per mode (0=lowest latency to 3=sharpest). Slider is disabled when Auto is enabled. | Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. | Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **Use Low Latency Filters for Digital Modes** | | Forces low-latency filters in DIGU/DIGL. | |

## XVTR tab

The XVTR tab manages per-transverter configuration.

| Control | Description |
|---|---|
| **RX Only:** | Forces RX-only on that transverter. |
| **Remove (xvtr)** | Deletes the transverter definition. |
| **Create New Transverter** | Adds a new transverter entry. |

The tab contains nested tabs, one per configured transverter, plus a "+" tab for creating new transverters.

## USB Cables tab

Use this tab to configure USB serial adapters connected to your FLEX-8600 and assign each one a role.

### Before you start

- Connect the USB serial adapter(s) to the computer running AetherSDR before opening the dialog.
- AetherSDR must be connected to the radio. The USB Cables tab is not available without an active radio connection.

### Steps

1. Open `Settings > USB Cables...`. This opens the Radio Setup dialog directly on the USB Cables tab. Alternatively, open `Settings > Radio Setup...` and click the **USB Cables** tab.
2. Locate the cables list on the left side of the tab. Each detected USB cable appears with its name and a **Plugged** or **Unplugged** status indicator.
3. Select the cable you want to configure by clicking it in the list.
4. Set the cable type using the **Name:** field and the associated type selector. Choose from CAT, BCD, bit, or PTT depending on the role this cable
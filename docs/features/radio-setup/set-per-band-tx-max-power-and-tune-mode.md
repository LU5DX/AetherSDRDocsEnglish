# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It organizes radio identification, network, GPS, transmit, phone/CW, receive, audio, filters, transverters, USB cables, peripherals, and serial port settings across multiple tabs.

## Opening Radio Setup

1. Open `Settings > Radio Setup...`.
2. The dialog opens as a frameless window with a custom title bar. Drag the title bar to move the window.

## Radio tab

The Radio tab displays radio information, identification, license info, and firmware update controls.

### Radio information

| Control | Kind | Notes |
|---|---|---|
| **Radio SN** | Indicator | Chassis serial number (read-only). |
| **Region** | Indicator | Radio regulatory region. |
| **HW Version** | Indicator | Hardware version string. |
| **Model** | Indicator | Radio model. |
| **Options** | Indicator | Shows licensed radio options. |
| **FlexControl** | Indicator | Detected state of FlexControl hardware. |
| **multiFLEX** | Indicator | multiFLEX enabled state. |

### Identification

| Control | Kind | Notes |
|---|---|---|
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings. Sent to radio as 'client station <name>'. |

### License information

The dialog displays license details from the radio including subscription status, expiration date, radio ID, and licensed version.

### Firmware update

1. Click **Check for Update** to query for firmware updates.
   - If an update is available, the status label shows the available version and instructs you to download the SmartSDR installer from flexradio.com.
   - If the firmware is already current, the status label shows "Firmware is up to date."
2. Download the SmartSDR installer from flexradio.com if one is available.
3. Click **Select Installer...**.
   - The file picker accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` file.
   - The firmware stager detects the file format automatically and extracts the `.ssdr` without requiring external tools.
   - While the stager prepares the firmware, the progress bar is shown and the status label reads "Preparing firmware from \<filename\>...".
4. Once staging completes, click **Upload Firmware** to transfer the firmware to the radio. Progress and result are shown in the status label.

| Control | Kind | Notes |
|---|---|---|
| **Check for Update** | Button | Queries for available firmware updates. |
| **Select Installer...** | Button | Opens a file picker. Accepts `.msi`, `.exe`, or `.ssdr`. Previously labelled **Browse .ssdr...** (changed in v0.9.3). |
| **Upload Firmware** | Button | Starts the firmware upload. Progress bar and status label update throughout. |

### Remote On

Click **Remote On** to enable remote wake / remote-on capability.

## Network tab

The Network tab displays radio network information and provides advanced network options.

### Network information

| Control | Kind | Notes |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator | Read-only network addresses. |

### Network settings

| Control | Kind | Default | Valid range | Notes |
|---|---|---|---|---|
| **Enforce Private IP Connections:** | Toggle button | — | — | Rejects non-RFC1918 peers. |
| **Network MTU:** | Spin box | 1450 | 576–9000 bytes | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. |
| **DHCP / Static** | Toggle button | — | — | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text field | — | — | Static IP configuration fields. |

### Apply network configuration

Click **Apply** to push the network configuration to the radio.

## GPS tab

The GPS tab displays GPS presence and live latitude, longitude, altitude, time, and satellite information.

## TX tab

Use this page to configure transmit settings including timings, interlocks, max power, tune mode, waterfall display, and slice/TX follow behavior.

### TX band settings

Click **TX Band Settings** to open the dedicated per-band power and tune dialog.

### TX controls

| Control | Kind | Default | Valid range | Notes |
|---|---|---|---|---|
| **Max Power:** | Spin box | — | 0–100 % | Sets radio-level TX power cap. |
| **Tune Mode:** | Combo box | — | See radio firmware options | Selects how the tune button behaves. |
| **Timings (in ms)** | Spin box | — | — | TX hang / delay timings. |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle button | — | — | Enables RCA and accessory interlock inputs. |
| **Show TX in Waterfall:** | Toggle button | — | Enabled / Disabled | Draws TX signal in the waterfall. |
| **TX Follows Active Slice** | Button | False | — | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Button | False | — | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. |

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### CW keyer settings

| Control | Kind | Default | Valid range | Notes |
|---|---|---|---|---|
| **Iambic:** | Toggle button | — | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Button | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| **Swap:** | Toggle button | — | — | Swaps dit/dah. |
| **Sideband:** | Combo box | — | LSB / USB | Selects CW pitch sideband. |
| **CWX:** | Toggle button | — | — | Enables CWX macro keying. |
| **Decode:** | Toggle button | True | — | Enables the CW decode overlay on the panadapter. |

### Other audio settings

| Control | Kind | Notes |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle button | Shows mic level meter even in RX. |
| **RTTY Mark Default:** | Spin box | Default RTTY mark frequency. |

## RX tab

The RX tab contains controls for manual frequency offset calibration and 10 MHz reference source selection. Calibration controls are always shown regardless of whether a GPSDO is installed.

### How to run a frequency calibration

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
4. Click **Start**.
   - The button label changes to **Busy** and becomes disabled while calibration runs.
   - The status field to the right of the button shows progress text ("Starting…" then live state).
   - Before starting, AetherSDR resets the frequency error to zero (`radio set freq_error_ppb=0`) and then issues `radio pll_start`.
   - If you leave **Cal Frequency (MHz):** empty and click **Start**, the status field shows "Enter cal frequency" and the calibration does not proceed.
5. When calibration completes, the button re-enables and the status field shows the result.
6. If you need to set an offset manually, enter a value in **Freq Offset (ppb):**.

### Calibration controls

| Control | Kind | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Spin box | Frequency used for calibration. Must not be empty before clicking **Start**. |
| **Start** | Button | Begins calibration. Resets `freq_error_ppb` to 0, then issues `radio pll_start`. Disabled while busy. |
| **Freq Offset (ppb):** | Spin box | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Combo box | Default: Auto. Selects the oscillator reference. Options: Auto, TCXO, GPSDO, External. Lock status (Locked / Unlocked) shown alongside the combo and updates live. |

## Audio tab

The Audio tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

### Audio output controls

| Control | Kind | Notes |
|---|---|---|
| **Line Out:** | Slider | Line-out gain. |
| **Mute (Line Out)** | Button | Mutes line-out. |
| **Headphone:** | Slider | Headphone gain. |
| **Mute (Headphone)** | Button | Mutes headphone. |
| **Front Speaker: / Mute** | Button | Mutes front speaker (model-specific). |

### Audio codec

| Control | Kind | Default | Notes |
|---|---|---|---|
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Button | Auto | Selects audio codec for SmartLink/LAN. |

### PC audio settings

| Control | Kind | Notes |
|---|---|---|
| **PC Audio Devices: Input: / Output:** | Combo box | Picks host audio in/out devices. |
| **Audio Boost:** | Toggle button | Enables extra gain on the client audio path. |
| **Audio Buffer:** | Text field | Default: 200. Valid range: 50–1000 ms. Increases audio buffer for VPN/SmartLink jitter. |

### System settings

| Control | Kind | Default | Notes |
|---|---|---|---|
| **Prevent system sleep while connected** | Checkbox | False | Keeps OS awake while radio is connected. |

### Recording settings

| Control | Kind | Default | Notes |
|---|---|---|---|
| **Recording: Radio Side / Client Side** | Button | Radio Side | Picks radio-side or client-side recording. |
| **Save to:** | Text field | — | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. |
| **...** | Button | — | Browses for recording folder. |
| **Auto-record on TX** | Checkbox | False | Automatically records while transmitting. |
| **Idle timeout:** | Spin box | 120 | Valid range: 10–3600 sec. Seconds of silence before recording stops. |

### NVIDIA BNR

| Control | Kind | Notes |
|---|---|---|
| **NVIDIA BNR: Autostart Container / Start / Stop / Check Status** | Button | Controls the NVIDIA Broadcast noise-removal container. Colored dot indicates container Running/Stopped/Unknown status. |

## Filters tab

The Filters tab configures low-latency or sharp filter options per bandwidth.

### Filter sharpness controls

| Control | Kind | Default | Notes |
|---|---|---|---|
| Voice / CW / Digital filter sharpness sliders | Slider | — | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode. Slider is disabled when Auto is enabled. |
| Auto (Voice / CW / Digital) | Toggle button | — | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. |
| **Use Low Latency Filters for Digital Modes** | Checkbox | — | Forces low-latency filters in DIGU/DIGL. |

## XVTR tab

The XVTR tab provides per-transverter configuration. It contains nested tabs, one per transverter, and a '+' tab for creating new transverters.

| Control | Kind | Notes |
|---|---|---|
| **RX Only:** | Toggle button | Forces RX-only on that transverter. |
| **Remove (xvtr)** | Button | Deletes the transverter definition. |
| **Create New Transverter** | Button | Adds a new transverter entry. |

## USB Cables tab

The USB Cables tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

### Cable configuration

| Control | Kind | Notes |
|---|---|---|
| Cables list / Status | Indicator | Detected USB cables per type with Plugged/Unplugged status. |
| Name: / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0-7) | Combo box | Per-cable serial parameters and behavior. |

## Peripherals tab

The Peripherals tab provides manual IP connection for external devices including the TGXL, PGXL, Antenna Genius, and ShackSwitch.

### Connecting peripheral devices

Each device has its own row with **Connect** / **Disconnect** buttons, IP address field, port field, and status indicator.

#### Behavior when clearing the IP field

- If you clear the IP address field and click **Connect** while disconnected, any previously saved manual IP and port are removed from settings and the device stops auto-connecting on startup.
- If you clear the IP address field and close the dialog without clicking **Connect** or **Disconnect**, the saved manual IP and port are also removed and the device is disconnected if it was connected.

#### TGXL

| Control | Default | Notes |
|---|---|---|
|
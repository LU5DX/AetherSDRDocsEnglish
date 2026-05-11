# AetherSDR Radio Setup Dialog

The **Radio Setup** dialog is the master configuration window for per-radio settings. It contains tabs for radio information, network, GPS, transmit, phone/CW, receive, audio, filters, transverters, USB cables, peripherals, and optionally serial ports.

## Opening the Radio Setup dialog

1. Click `Settings > Radio Setup...`.

## Dialog layout

The **Radio Setup** dialog now uses a frameless window design with a custom title bar. The title bar displays "Radio Setup" and provides standard window controls (minimize, maximize, close).

The dialog remembers its size and position between sessions. Geometry is saved in `RadioSetupDialogGeometry` in the application settings.

## Radio tab

The **Radio** tab displays radio identification and firmware management controls.

### Radio information (read-only)

| Control | What it shows |
|---|---|
| **Radio SN** | Chassis serial number |
| **Region** | Regulatory region (e.g., USA) |
| **HW Version** | Hardware version string |
| **Model** | Radio model (e.g., FLEX-8600) |
| **Options** | Licensed radio options |
| **FlexControl** | Detected state of FlexControl hardware |
| **multiFLEX** | multiFLEX enabled state |
| **License Info** | Subscription status, expiration date, Radio ID, and licensed version |

### User-configurable fields

| Control | What it does |
|---|---|
| **Nickname** | Enter a friendly name for the radio |
| **Callsign** | Enter the station callsign |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in `StationName`. |

### Remote On

Click **Remote On** to enable remote wake / remote-on capability for the radio.

### Firmware update

The firmware update workflow uses the **Select Installer...** button (labelled **Browse .ssdr...** before v0.9.3).

1. Click **Check for Update** to query the radio for available firmware versions.
2. If an update is available, the status label displays the version and instructs you to download the SmartSDR installer from flexradio.com.
3. Download the SmartSDR installer (.msi for v4.2+, .exe for older releases).
4. Click **Select Installer...** and choose the downloaded installer or a pre-extracted .ssdr file in the file picker.
5. A progress bar and status label show the extraction progress. When staging completes, click **Upload Firmware** to transfer the firmware to the radio.

The stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools.

## Network tab

The **Network** tab displays radio network information and allows configuration.

### Network information (read-only)

| Control | What it shows |
|---|---|
| **IP Address / Mask / MAC Address** | Current network addresses |

### Configuration

| Control | What it does | Valid range |
|---|---|---|
| **Enforce Private IP Connections:** | Toggle to reject non-RFC1918 peers | On / Off |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in `NetworkMtu`. | 576–9000 bytes |
| **DHCP / Static** | Switches between DHCP and Static IP modes | DHCP / Static |

When **Static** is selected, enter the **IP Address:**, **Mask:**, and **Gateway:** in the text fields, then click **Apply** to push the configuration to the radio.

## GPS tab

The **GPS** tab shows GPS presence and live information when a GPS module is installed and active.

### GPS information (read-only)

| Indicator | What it shows |
|---|---|
| GPS status | Latitude, longitude, altitude, UTC time, and number of satellites when GPS is active |

## TX tab

The **TX** tab configures transmit parameters.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

Use the **Timings** spinboxes to set TX hang and delay timings in milliseconds.

### Interlocks

Toggle **TX REQ: RCA** and **Accessory** to enable interlock inputs.

### Power and Tune

| Control | What it does | Valid range |
|---|---|---|
| **Max Power:** | Sets radio-level TX power cap | 0–100 % |
| **Tune Mode:** | Selects how the tune button behaves | — |

### Display

| Control | What it does |
|---|---|
| **Show TX in Waterfall:** | Toggle to draw TX signal in the waterfall |

### Slice following behavior

| Control | What it does |
|---|---|
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. Stored in `TxFollowsActiveSlice`. |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g., WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. Stored in `ActiveFollowsTxSlice`. |

## Phone/CW tab

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

### Level meter

Toggle **Enable/Disable the Level Meter During Receive** to show the mic level meter even during receive.

### CW keyer

| Control | What it does | Valid range |
|---|---|---|
| **Iambic:** | Enables or disables the iambic keyer on the radio | Enabled / Disabled |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | A / B |
| **Swap:** | Swaps dit/dah | On / Off |
| **Sideband:** | Selects CW pitch sideband | LSB / USB |
| **CWX:** | Enables CWX macro keying | On / Off |
| **Decode:** | Enables the CW decode overlay on the panadapter. Stored in `CwDecodeOverlay`. | On / Off |

### RTTY

| Control | What it does |
|---|---|
| **RTTY Mark Default:** | Sets the default RTTY mark frequency |

## RX tab

The **RX** tab provides frequency calibration and reference source selection.

### Frequency calibration

The calibration section is always visible regardless of GPSDO presence. When a GPSDO is present, the status label confirms it in green; when absent, in amber.

| Control | What it does |
|---|---|
| **Cal Frequency (MHz):** | Enter the known-accurate reference frequency in MHz to use for calibration |
| **Start** | Begins the frequency calibration sequence. AetherSDR resets the frequency error to 0 ppb, then sends `radio pll_start` to the radio. The button shows **Busy** while calibration runs. |
| **Freq Offset (ppb):** | Displays or manually sets the current frequency offset in parts per billion |

### 10 MHz Reference Source

| Control | What it does | Valid range |
|---|---|---|
| **10 MHz Reference Source:** | Selects the oscillator reference source. Options depend on installed hardware. | Auto / TCXO / GPSDO / External |

The lock status label beside the control updates live:

- If the radio has not yet reported oscillator state: **Waiting for oscillator status**
- If **Auto** is selected and the radio resolved to a specific source: **Auto -> \<resolved source\>** followed by **Locked** or **Unlocked**
- If a specific source is selected but a different source is active: **\<selected source\> -> \<active source\>** followed by **Locked** or **Unlocked**
- Otherwise: active source name followed by **Locked** or **Unlocked**

## Audio tab

The **Audio** tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR.

### Radio audio outputs

| Control | What it does |
|---|---|
| **Line Out:** | Slide to adjust line-out gain |
| **Mute (Line Out)** | Click to mute line-out |
| **Headphone:** | Slide to adjust headphone gain |
| **Mute (Headphone)** | Click to mute headphone |
| **Front Speaker:** / **Mute** | Click to mute front speaker (model-specific) |

### Audio Compression

| Control | What it does | Valid range |
|---|---|---|
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects the audio codec used over SmartLink/LAN. Stored in `AudioCompression`. | Auto / Uncompressed / Opus |

### System sleep prevention

Check **Prevent system sleep while connected** to keep the OS awake while the radio is connected. Stored in `InhibitSleepWhileConnected`.

### PC Audio Devices

| Control | What it does |
|---|---|
| **PC Audio Devices: Input:** | Select the host audio input device |
| **PC Audio Devices: Output:** | Select the host audio output device |

### Audio Boost

Toggle **Audio Boost:** on to enable extra gain on the client audio path. Stored in `AudioBoost`.

### Audio Buffer

Enter a value in **Audio Buffer:** to set the client-side audio buffer in milliseconds. Increase this when using VPN or SmartLink connections with unstable latency. Stored in `AudioBufferMs`.

| Valid range | Default |
|---|---|
| 50–1000 ms | 200 ms |

### Recording

| Control | What it does | Valid range |
|---|---|---|
| **Recording: Radio Side / Client Side** | Picks radio-side or client-side recording. Stored in `RecordingMode`. | Radio Side / Client Side |
| **Save to:** | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored in `QsoRecordingDir`. | — |
| **...** | Click to browse for recording folder | — |
| **Auto-record on TX** | Check to automatically record while transmitting. Stored in `QsoRecordingAutoRecord`. | On / Off |
| **Idle timeout:** | Seconds of silence before recording stops. Stored in `QsoRecordingIdleTimeout`. | 10–3600 sec (default 120) |

### NVIDIA BNR

| Control | What it does |
|---|---|
| **Autostart Container** | Click to configure automatic container startup |
| **Start** | Click to start the NVIDIA Broadcast noise-removal container |
| **Stop** | Click to stop the container |
| **Check Status** | Click to check container status |

A colored status dot indicates the container state (Running/Stopped/Unknown).

## Filters tab

The **Filters** tab configures filter sharpness per mode.

### Filter sharpness

Use the sliders for **Voice**, **CW**, and **Digital** to set filter sharpness:

| Value | Meaning |
|---|---|
| 0 | Lowest latency |
| 1 | — |
| 2 | — |
| 3 | Sharpest |

Sliders are disabled when **Auto** is enabled for that mode.

### Auto mode

Toggle **Auto** for Voice, CW, or Digital to enable automatic filter-level selection. When enabled, the manual sharpness slider for that mode is disabled.

### Low Latency Filters

Check **Use Low Latency Filters for Digital Modes** to force low-latency filters in DIGU/DIGL.

## XVTR tab

The **XVTR** tab configures per-transverter settings. It contains nested tabs, one per configured transverter, plus a **+** tab to create new transverters.

### Per-transverter controls

| Control | What it does |
|---|---|
| **RX Only:** | Toggle to force RX-only on that transverter |
| **Remove** | Click to delete the transverter definition |

### Creating a new transverter

1. Click the **+** tab (labelled **Create New Transverter**).
2. Configure the transverter parameters.

## USB Cables tab

The **USB Cables** tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

### Cable detection

The **Cables list / Status** shows detected USB cables per type with Plugged/Unplugged status.

### Per-cable configuration

Each detected cable provides the following parameters:

| Control | What it does |
|---|---|
| **Name:** | Cable identifier |
| **Enabled** | Toggle cable enable |
| **Speed** | Baud rate selection |
| **Data Bits** | Data bits selection |
| **Parity** | Parity selection |
| **Stop Bits** | Stop bits selection |
| **Flow** | Flow control selection |
| **Source** | Signal source selection |
| **Auto Report** | Toggle auto-reporting |
| **BCD Type** | BCD output type selection |
| **Polarity** | Signal polarity selection |
| **Bit Configuration (0-7)** | Bit configuration per pin |

## Peripherals tab

The **Peripherals** tab manages external devices via direct TCP connection (TGXL, PGXL, Antenna Genius, ShackSwitch).

### TGXL

Click **Connect** to open a direct TCP connection to the TGXL on port 9010. The IP and port are saved to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup.

When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed.

If the IP field is empty and the radio has discovered the TGXL, the discovered
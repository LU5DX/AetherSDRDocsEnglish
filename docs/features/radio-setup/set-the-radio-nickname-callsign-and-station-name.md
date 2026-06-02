# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It provides access to all radio-level settings including radio identification, network configuration, GPS, transmit parameters, phone/CW settings, receive calibration, audio configuration, filters, transverters, USB cables, peripherals, and SmartLink certificate management.

## Before you start

- AetherSDR must be connected to the radio. Most controls are not available without an active connection.

## Opening the dialog

1. Open `Settings > Radio Setup...`.
2. The dialog opens as a persistent window. Its position and size are saved automatically when you close it and restored the next time you open it. The geometry is stored in AppSettings under the key `RadioSetupDialogGeometry`.

## Radio tab

The **Radio** tab displays radio information, identification, license info, and firmware update controls.

### Radio Information

The radio information section shows read-only indicators for:

| Control | Description |
|---|---|
| **Radio SN** | Chassis serial number (read-only). |
| **Region** | Radio regulatory region (e.g., USA). |
| **HW Version** | Hardware version string. |
| **Model** | Radio model. |
| **Options** | Shows licensed radio options. |
| **FlexControl** | Detected state of FlexControl hardware. |
| **multiFLEX** | multiFLEX enabled state. |

### Radio Identification

Set a human-readable nickname, your callsign, and a station name on the connected FLEX-8600. These values identify the radio and this client to other multiFLEX stations on the network.

| Control | Description | Default |
|---|---|---|
| **Nickname** | User-friendly label for the radio. Sent to the radio as the radio name. | Radio's reported name |
| **Callsign** | Your station callsign, stored on the radio. | _(blank)_ |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Stored in AppSettings. Sent to radio as 'client station <name>'. | OS hostname |

### Steps to set radio identification

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. In the **Nickname** field, type the nickname you want to assign to the radio.
4. Press Tab or click away from the field to confirm. AetherSDR sends the new name to the radio immediately.
5. In the **Callsign** field, type your station callsign.
6. Press Tab or click away from the field to confirm.
7. In the **Station Name** field, type the name that identifies this client to other multiFLEX stations.
8. Press Tab or click away from the field to confirm.
9. Click the window's close button or press Escape to dismiss the dialog.

### License Information

The **License Info** section displays subscription details, expiration date, Radio ID, and Licensed version from the radio.

### Remote On

Click **Remote On** to enable remote wake / remote-on capability.

### Firmware Update

Use the firmware update controls to check for and apply firmware updates to the radio.

| Control | Description |
|---|---|
| **Check for Update** | Queries for firmware updates. |
| **Select Installer...** | Opens a file picker that accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer) or a pre-extracted .ssdr firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. |

#### To check for a firmware update

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, the status label shows the available version number and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it.
   - If firmware is up to date, the status label confirms the current version in green.

#### To stage and upload firmware

1. Download the SmartSDR installer from flexradio.com. AetherSDR accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file.
2. Click **Select Installer...**
   - The file picker opens with the filter set to `*.msi *.exe *.ssdr`.
   - Select the downloaded file and click Open.
   - AetherSDR begins preparing the firmware automatically. The status label shows "Preparing firmware from \<filename\>..." and the progress bar appears.
   - The firmware stager auto-detects the file format from the first 8 bytes (OLE/MSI magic for .msi, PE/COFF MZ for .exe, or CTRL+Z for .ssdr) and extracts the .ssdr without external tools.
3. Wait for preparation to complete. The status label shows "Ready to upload \<filename\>".
4. Click **Upload Firmware**.
   - A confirmation dialog appears: "This will restart the radio. Are you sure you want to upload \<filename\>?"
5. Click **Yes** to confirm.
   - The upload begins. The status label shows "Uploading... (X%)" and the progress bar updates.
   - The radio restarts after upload completes. The status label shows "Upload and reboot successful."
6. Click the window's close button or press Escape to dismiss the dialog.

## Network tab

The **Network** tab displays radio network information and provides advanced network options.

| Control | Description | Default |
|---|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. | — |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers. | — |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings. | 1450 |
| **DHCP / Static** | Switches between DHCP and Static IP modes. | — |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields. | — |
| **Apply** | Pushes the network config to the radio. | — |

### To configure static IP

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Click **DHCP / Static** to switch to Static mode.
4. Enter the **IP Address**, **Mask**, and **Gateway** values.
5. Click **Apply** to push the configuration to the radio.

## GPS tab

The **GPS** tab displays GPS presence and live latitude, longitude, altitude, time, and satellites information.

## TX tab

The **TX** tab provides transmit timing controls, interlocks, max power, tune mode, waterfall display, slice/TX follow behavior, and a shortcut to TX Band Settings.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

The timing controls include fields for interlock delays and timeout. The timeout field is displayed in seconds for readability, but stored and transmitted to the radio in milliseconds.

| Control | Description | Default |
|---|---|---|
| **ACC TX:** | ACC transmit delay in milliseconds. | — |
| **TX Delay:** | TX delay in milliseconds. | — |
| **RCA TX1:** | RCA TX1 delay in milliseconds. | — |
| **Timeout (sec):** | Interlock timeout displayed in seconds. The radio stores this value in milliseconds internally. | — |

### Interlocks

| Control | Description |
|---|---|
| **TX REQ: RCA** | Enables RCA interlock input. |
| **TX REQ: Accessory** | Enables accessory interlock input. |

### Power and Tune

| Control | Description | Default |
|---|---|---|
| **Max Power:** | Sets radio-level TX power cap (0-100%). | — |
| **Tune Mode:** | Selects how the tune button behaves. | — |
| **Show TX in Waterfall:** | Draws TX signal in the waterfall. | — |

### Slice/TX Follow Behavior

| Control | Description | Default |
|---|---|---|
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. | False |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. | False |

## Phone/CW tab

The **Phone/CW** tab provides microphone, CW keyer, and RTTY default settings.

| Control | Description | Default |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. | — |
| **Iambic:** | Enables or disables the iambic keyer on the radio. | — |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | A |
| **Swap:** | Swaps dit/dah. | — |
| **Sideband:** | Selects CW pitch sideband (LSB or USB). | — |
| **CWX:** | Enables CWX macro keying. | — |
| **Decode:** | Enables the CW decode overlay on the panadapter. | True |
| **RTTY Mark Default:** | Default RTTY mark frequency. | — |

## RX tab

The **RX** tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

| Control | Description | Default |
|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. | — |
| **Start** | Starts the frequency calibration sweep. | — |
| **Freq Offset (ppb):** | Manual frequency offset in ppb. | — |
| **10 MHz Reference Source:** | Selects oscillator reference source. Options depend on hardware installed (TCXO/GPSDO/External). Lock status (Locked/Unlocked) is shown alongside the combo and updates live. | Auto |

## Audio tab

The **Audio** tab provides radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container controls.

| Control | Description | Default |
|---|---|---|
| **Line Out:** | Line-out gain slider. | — |
| **Mute (Line Out)** | Mutes line-out. | — |
| **Headphone:** | Headphone gain slider. | — |
| **Mute (Headphone)** | Mutes headphone. | — |
| **Front Speaker: / Mute** | Mutes front speaker (model-specific). | — |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects audio codec for SmartLink/LAN. Stored in AppSettings. | Auto |
| **Prevent system sleep while connected** | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. | False |
| **PC Audio Devices: Input: / Output:** | Picks host audio in/out devices. | — |
| **Audio Boost:** | Enables extra gain on the client audio path. Stored in AppSettings. | — |
| **Audio Buffer:** | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Stored as `AudioBufferMs`. | 200 |
| **Recording: Radio Side / Client Side** | Picks radio-side or client-side recording. Stored in AppSettings. | Radio Side |
| **Save to:** | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. | — |
| **...** | Browses for recording folder. | — |
| **Auto-record on TX** | Automatically records while transmitting. | False |
| **Idle timeout:** | Seconds of silence before recording stops. | 120 |
| **NVIDIA BNR: Autostart Container / Start / Stop / Check Status** | Controls the NVIDIA Broadcast noise-removal container. | — |

## Filters tab

The **Filters** tab provides low-latency and sharp filter options per bandwidth.

| Control | Description | Default |
|---|---|---|
| **Voice / CW / Digital filter sharpness sliders** | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. | — |
| **Auto (Voice / CW / Digital)** | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. | — |
| **Use Low Latency Filters for Digital Modes** | Forces low-latency filters in DIGU/DIGL. | — |

## XVTR tab

The **XVTR** tab provides per-transverter configuration. Contains nested tabs, one per transverter, plus a '+' tab to create new transverters.

| Control | Description |
|---|---|
| **RX Only:** | Forces RX-only on that transverter. |
| **Remove (xvtr)** | Deletes the transverter definition. |
| **Create New Transverter** | Adds a new transverter entry. |

## USB Cables tab

The **USB Cables** tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

| Control | Description |
|---|---|
| **Cables list / Status** | Detected USB cables per type with Plugged/Unplugged status. |
| **Name: / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto
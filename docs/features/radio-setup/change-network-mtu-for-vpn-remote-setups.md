# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, phone/CW, RX, audio, filters, XVTR, USB cables, peripherals, serial/FlexControl, and themes.

## Opening the dialog

1. Click `Settings > Radio Setup...`.
2. The dialog opens with the **Radio** tab selected.

## General dialog behavior

- The dialog is a frameless window by default when the `FramelessWindow` setting is `True`. You can resize it by dragging any edge.
- The dialog geometry is persisted across sessions.
- Changes made on some tabs are applied immediately; others require clicking an Apply or Connect button.
- If you clear an IP field on the **Peripherals** tab and close the dialog without clicking Connect/Disconnect, the saved manual IP and port are automatically removed and the device disconnects.

## Radio (tab)

The Radio tab displays radio information, identification, license info, and firmware update controls.

| Control | Description |
|---|---|
| **Radio SN** | Chassis serial number (read-only). |
| **Region** | Radio regulatory region (read-only). |
| **HW Version** | Hardware version string (read-only). |
| **Remote On** | Enables remote wake / remote-on. |
| **Options** | Shows licensed radio options (read-only). |
| **FlexControl** | Detected state of FlexControl hardware (read-only). |
| **multiFLEX** | multiFLEX enabled state (read-only). |
| **Model** | Radio model (read-only). |
| **Nickname** | User-friendly radio nickname. |
| **Callsign** | Station callsign. |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as "client station \<name\>". |
| **License Info** | Displays license details from the radio: subscription, expiration, radio ID, and licensed version. |
| **Check for Update** | Queries for firmware updates. |
| **Select Installer...** | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes and extracts the `.ssdr` without external tools. See [Firmware update](#firmware-update-radio-tab) below. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. |

### Firmware update (Radio tab)

AetherSDR does not download firmware automatically when an update is detected. Download the SmartSDR installer from flexradio.com yourself, then stage it manually.

#### Staging a firmware update

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, a status message tells you the available version and directs you to download the installer from flexradio.com.
   - If firmware is current, a green status message confirms the installed version.
4. Download the SmartSDR installer from flexradio.com. Accepted formats:
   - `.msi` — WiX installer (FlexRadio SmartSDR v4.2 and later)
   - `.exe` — older self-extracting installer
   - `.ssdr` — pre-extracted firmware file
5. Click **Select Installer...**.
   - A file picker opens filtered to `*.msi`, `*.exe`, and `*.ssdr`.
   - Select the file you downloaded.
   - AetherSDR reads the file, auto-detects its format from the first 8 bytes, and extracts the `.ssdr` payload if needed. A status label shows progress.
6. When staging completes and the upload button becomes active, click **Upload Firmware**.
   - A progress bar tracks the upload.
   - Do not close the dialog or disconnect from the radio while the upload is in progress.

#### Firmware status messages

| Message | Meaning |
|---|---|
| Update available: v*x.y.z* | A newer firmware version exists. Download the installer from flexradio.com, then click **Select Installer...**. |
| Firmware is up to date (v*x.y.z*) | No action needed. |
| Preparing firmware from *filename*... | The stager is reading and extracting the selected file. |
| (error text in red) | Staging or upload failed. Check the file is a valid SmartSDR installer or firmware file and try again. |

#### Notes

- The **Select Installer...** button was labelled **Browse .ssdr...** in versions prior to v0.9.3.
- Staging runs entirely on the client; no external tools are required to unpack `.msi` or `.exe` installers.

## Network (tab)

The Network tab displays radio network information and lets you configure advanced network options.

| Control | Description | Default |
|---|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. | — |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers. | — |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range 576–9000 bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. | 1450 |
| **DHCP / Static** | Switches between DHCP and Static IP modes. | — |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields. | — |
| **Apply** | Pushes the network configuration to the radio. | — |

### Changing the Network MTU

The Network MTU setting controls the maximum packet size the radio sends over the network. Lowering it prevents fragmentation when you connect through a VPN or other tunnel that reduces the available path MTU.

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match your network path MTU.
5. Click **Apply** to push the new MTU to the radio.

## GPS (tab)

The GPS tab displays GPS presence and live latitude, longitude, altitude, time, and satellite information.

| Control | Description |
|---|---|
| **GPS status** | Shows GPS presence and live position data. |

## TX (tab)

The TX tab controls TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX Band Settings.

| Control | Description | Default |
|---|---|---|
| **TX Band Settings** | Opens the dedicated per-band power/tune dialog. | — |
| **Timings (in ms)** | TX hang / delay timings. | — |
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs. | — |
| **Max Power:** | Sets radio-level TX power cap (0–100%). | — |
| **Tune Mode:** | Selects how the tune button behaves. | — |
| **Show TX in Waterfall:** | Draws TX signal in the waterfall. | — |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | False |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | False |

## Phone/CW (tab)

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

| Control | Description | Default |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. | — |
| **Iambic:** | Enables or disables the iambic keyer on the radio. | Enabled |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | A |
| **Swap:** | Swaps dit/dah. | — |
| **Sideband:** | Selects CW pitch sideband (LSB or USB). | — |
| **CWX:** | Enables CWX macro keying. | — |
| **Decode:** | Enables the CW decode overlay on the panadapter. Stored in AppSettings as `CwDecodeOverlay`. | True |
| **RTTY Mark Default:** | Default RTTY mark frequency. | — |

## RX (tab)

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection. All calibration controls are always visible, regardless of whether a GPSDO is installed. A status label at the top of the group indicates whether a GPSDO is present (green text) or not (amber text).

| Control | Description |
|---|---|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. |
| **Start** | Starts the frequency calibration sweep. The button label changes to **Busy** while the sweep runs. |
| **Freq Offset (ppb):** | Manual frequency offset in ppb. |
| **10 MHz Reference Source:** | Selects oscillator reference source. Options depend on hardware installed. See table below. |

### 10 MHz Reference Source

The **10 MHz Reference Source:** combo box is populated dynamically. Only sources supported by the connected hardware appear. A label beside the combo shows the resolved source and lock state.

#### Combo options

| Option | When shown |
|---|---|
| Auto | Always. |
| TCXO | When oscillator status has been received, or when the radio reports `tcxoPresent`, or when the current or active setting is `tcxo`. |
| GPSDO | When the radio reports `gpsdoPresent`, or when the current or active setting is `gpsdo`. |
| External 10 MHz | When oscillator status has been received, or when the radio reports `extPresent`, or when the current or active setting is `external`. |

#### Status label behavior

- When **Auto** is selected and the radio has chosen a specific source, the label reads `Auto -> <source>`.
- When a specific source is selected and the radio is using a different one, the label reads `<selected> -> <active>`.
- When the setting and state agree, only the active source is shown.
- Lock state is appended: `Locked` (green) or `Unlocked` (red).
- If **External 10 MHz** is selected or active but no external reference is detected, the label appends `(not detected)`.
- While the radio has not yet reported oscillator status, the label reads `Waiting for oscillator status` in grey.

### Calibration procedure

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in the **Cal Frequency (MHz):** field.
4. Click **Start**.
   - The button label changes to **Busy** and is disabled while the calibration sweep runs.
   - A status label beside the button updates as the sweep progresses.
   - The radio first resets the frequency error to 0 ppb, then begins the PLL calibration sequence.
5. When calibration completes the button re-enables and the status label shows the result.
6. If you prefer to set the offset manually, enter a value directly in **Freq Offset (ppb):** without clicking **Start**.

#### Calibration status messages

| Message | Meaning |
|---|---|
| Starting… | The sweep command has been sent to the radio. |
| Busy | PLL calibration is in progress. |
| Enter cal frequency | The Cal Frequency field was empty when Start was clicked. |

## Audio (tab)

The Audio tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

| Control | Description | Default |
|---|---|---|
| **Line Out:** | Line-out gain slider. | — |
| **Mute (Line Out)** | Mutes line-out. | — |
| **Headphone:** | Headphone gain slider. | — |
| **Mute (Headphone)** | Mutes headphone. | — |
| **Front Speaker: / Mute** | Mutes front speaker (model-specific). | — |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Selects audio codec for SmartLink/LAN. Stored in AppSettings as `AudioCompression`. | Auto |
| **Prevent system sleep while connected** | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored in AppSettings as `InhibitSleepWhileConnected`. | False |
| **PC Audio Devices: Input: / Output:** | Picks host audio in/out devices. | — |
| **Audio Boost:** | Enables extra gain on the client audio path. Stored in AppSettings as `AudioBoost`. | — |
| **Audio Buffer:** | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Range 50–1000 ms. Stored in AppSettings as `AudioBufferMs`. | 200 |
| **Recording: Radio Side / Client Side** | Picks radio-side or client-side recording. Stored in AppSettings as `RecordingMode`. | Radio Side |
| **Save to:** | Folder for saved recordings (client-side only). Stored in AppSettings as `QsoRecordingDir`. Defaults to Documents/AetherSDR/Recordings. | — |
| **...** | Browses for recording folder. | — |
| **Auto-record on TX** | Automatically records while transmitting. Stored in AppSettings as `QsoRecordingAutoRecord`. | False |
| **Idle timeout:** | Seconds of silence
# Configure Radio Setup

The **Radio Setup** dialog (`Settings > Radio Setup...`) provides master per-radio configuration with tabbed sections for radio information, network, GPS, TX, Phone/CW, RX, audio, filters, transverters, USB cables, peripherals, adaptive pre-distortion, themes, SmartLink pinned certificates, and serial port settings.

## Before you start

- The radio must be connected before most tabs show live information.
- Some tabs (APD, Themes, SmartLink, Serial) are built lazily and only appear when first clicked.
- AetherSDR uses a `PersistentDialog` base class that saves and restores window geometry automatically.

## Steps to open

1. Click **Settings > Radio Setup...** in the main menu.
2. The dialog opens showing the **Radio** tab by default.
3. Click any tab to access its settings.

---

## Radio tab

The **Radio** tab shows radio identification, license information, and firmware update controls.

### Reading radio information

- **Radio SN** — Chassis serial number (read-only). Shows the chassis serial if available, otherwise the radio serial.
- **Region** — Radio regulatory region (read-only).
- **HW Version** — Hardware version string (read-only).
- **Model** — Radio model (read-only).
- **Options** — Licensed radio options (read-only). Shows the radio's options list, or a default like "GPS, PGXL" if an amplifier is detected.
- **FlexControl** — Detected state of FlexControl hardware (read-only).
- **multiFLEX** — multiFLEX enabled state (read-only).
- **License Info** — Displays subscription, expiration, Radio ID, and licensed version (read-only).

### Copying radio information

Each read-only value has a small copy button next to it. Click the copy button to copy the value to your clipboard. A brief "Copied!" popup appears near the button. The copy button is disabled when the value is empty or shows "—".

### Setting identification

| Control | What it does | Notes |
|---|---|---|
| **Nickname** | User-friendly radio nickname (editable). | — |
| **Callsign** | Station callsign (editable). | — |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Stored in AppSettings. | Defaults to the OS hostname if empty. Sent to radio as 'client station <name>'. |

### Firmware update

1. Click **Check for Update** to query for available firmware updates. The result appears in the status label. If an update is available, the label directs you to download the SmartSDR installer from flexradio.com.
2. Click **Select Installer...** to open a file picker. Select one of:
   - `.msi` — WiX-based SmartSDR installer for firmware 4.2+.
   - `.exe` — Older self-extracting SmartSDR installer.
   - `.ssdr` — Pre-extracted firmware file.
3. The firmware stager detects the file format automatically and extracts the `.ssdr` payload. A progress bar and status label show extraction progress.
4. Once extraction completes, click **Upload Firmware** to start the upload. A progress bar and status label show upload progress.

| Control | What it does | Notes |
|---|---|---|
| **Check for Update** | Queries for available firmware updates. | When an update is found, the label directs you to download the installer from flexradio.com. |
| **Select Installer...** | Opens a file picker for `.msi`, `.exe`, or `.ssdr` files. | Renamed from **Browse .ssdr...** in v0.9.3. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. | Enabled only after extraction completes. |

### Remote On

Click **Remote On** to enable remote wake / remote-on functionality on the radio.

---

## Network tab

The **Network** tab shows radio network information and advanced network options.

### Reading network info

- **IP Address / Mask / MAC Address** — Read-only network addresses.

### Network configuration

| Control | What it does | Default | Notes |
|---|---|---|---|
| **Enforce Private IP Connections:** | Toggle to reject non-RFC1918 peers. | — | — |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes. | 1450 | Range 576–9000 bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings. |
| **DHCP / Static** | Toggle between DHCP and Static IP modes. | — | — |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields. | — | Enabled when Static mode is selected. |
| **Apply** | Pushes the network config to the radio. | — | — |

---

## GPS tab

The **GPS** tab shows GPS presence and live position/satellite information when a GPS receiver is active.

- Latitude, longitude, altitude, time, and satellite count (read-only).
- GPS lock status indicator.

---

## TX tab

The **TX** tab configures transmit timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX Band Settings.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

Use the spinboxes in the **Timings (in ms)** section to set TX hang and delay timings.

### Interlocks

Toggle **TX REQ: RCA** and **TX REQ: Accessory** to enable RCA and accessory interlock inputs.

### Max Power

Set the radio-level TX power cap using the **Max Power:** spinbox (0–100%).

### Tune Mode

Select the tune button behavior from the **Tune Mode:** combo box.

### Waterfall

Toggle **Show TX in Waterfall:** to draw the TX signal in the waterfall.

### Slice/TX follow

| Control | What it does | Default | Notes |
|---|---|---|---|
| **TX Follows Active Slice** | TX follows the active slice. | False | Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). | False | Mutually exclusive with **TX Follows Active Slice**. |

---

## Phone/CW tab

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

### Level Meter

Toggle **Enable/Disable the Level Meter During Receive** to show the mic level meter even during receive.

### CW Keyer

| Control | What it does | Default | Notes |
|---|---|---|---|
| **Iambic:** | Enables or disables the iambic keyer on the radio. | — | In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. | A | Mutually exclusive pair added in v0.9.1. |
| **Swap:** | Swaps dit/dah. | — | — |
| **Sideband:** | Selects CW pitch sideband. | — | Options: LSB / USB. |
| **CWX:** | Enables CWX macro keying. | — | — |
| **Decode:** | Enables the CW decode overlay on the panadapter. | True | Stored as `CwDecodeOverlay`. |

### RTTY

Set the **RTTY Mark Default:** spinbox to the default RTTY mark frequency.

---

## RX tab

The **RX** tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

### Frequency calibration

The calibration section is always visible, regardless of whether a GPSDO is installed.

- **GPSDO installed** — shown in green: *GPSDO installed. Manual frequency offset calibration available.*
- **No GPSDO** — shown in amber: *Manual frequency offset calibration available.*

| Control | What it does | Notes |
|---|---|---|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. | Always shown. |
| **Start** | Starts the frequency calibration sweep. | Disabled and labelled **Busy** while active. Validates that a cal frequency has been entered. Resets stored frequency error to zero before starting. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion. | Reset to 0 when **Start** is clicked. |

### 10 MHz Reference Source

The **10 MHz Reference Source:** combo box populates dynamically based on detected hardware and live oscillator state.

| Control | What it does | Notes |
|---|---|---|
| **10 MHz Reference Source:** | Selects the oscillator reference source. Sends `radio oscillator <value>` to the radio when changed. | **Auto** always present. Additional entries: **TCXO**, **GPSDO**, **External 10 MHz**. Options depend on hardware detected and live oscillator state. |
| Lock status label | Shows the active source, resolution of Auto, and lock state. Updates live. | Green = Locked; Red = Unlocked; Grey-blue = waiting for status. Appends *(not detected)* when External 10 MHz is active but no external reference signal is present. |

The lock status label shows:
- *Waiting for oscillator status* when status has not yet been received.
- *Auto -> \<resolved source\>* when Auto is selected and the radio has resolved to a specific source.
- *\<setting\> -> \<active state\>* when the setting and active state differ.
- The active source name alone when they match.

The lock state (*Locked* or *Unlocked*) is always appended.

---

## Audio tab

The **Audio** tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

### Radio audio outputs

| Control | What it does | Notes |
|---|---|---|
| **Line Out:** | Line-out gain slider. | — |
| **Mute (Line Out)** | Mutes line-out. | — |
| **Headphone:** | Headphone gain slider. | — |
| **Mute (Headphone)** | Mutes headphone. | — |
| **Front Speaker: / Mute** | Mutes front speaker (model-specific). | — |

### Audio Compression

Select the audio codec for SmartLink/LAN using the **Audio Compression (SmartLink):** buttons: **Auto**, **Uncompressed**, or **Opus** (default: Auto). Stored as `AudioCompression`.

### System sleep

Check **Prevent system sleep while connected** to keep the OS awake while the radio is connected (default: False). Stored as `InhibitSleepWhileConnected`.

### PC Audio Devices

Select host audio input and output devices using the **Input:** and **Output:** combo boxes.

### Audio Boost

Toggle **Audio Boost:** to enable extra gain on the client audio path. Stored as `AudioBoost`.

### Audio Buffer

Set the **Audio Buffer:** text field to increase audio buffer in milliseconds for VPN/SmartLink jitter. Default: 200, range 50–1000 ms. Stored as `AudioBufferMs`.

### Recording

| Control | What it does | Default | Notes |
|---|---|---|---|
| **Recording: Radio Side / Client Side** | Picks radio-side or client-side recording. | Radio Side | Stored as `RecordingMode`. |
| **Save to:** | Folder for saved recordings (client-side only). | Documents/AetherSDR/Recordings | Stored as `QsoRecordingDir`. |
| **...** | Browses for recording folder. | — | — |
| **Auto-record on TX** | Automatically records while transmitting. | False | Stored as `QsoRecordingAutoRecord`. |
| **Idle timeout:** | Seconds of silence before recording stops. | 120 | Range 10–3600 sec. Stored as `QsoRecordingIdleTimeout`. |

### NVIDIA BNR

Use the **NVIDIA BNR** controls to manage the NVIDIA Broadcast noise-removal container:
- **Autostart Container** — Enables automatic startup.
- **Start / Stop** — Manually starts or stops the container.
- **Check Status** — Shows the container status (Running/Stopped/Unknown) with a colored dot indicator.

---

## Filters tab

The **Filters** tab configures low-latency or sharp filter options per bandwidth.

### Filter sharpness

For Voice, CW, and Digital modes, use the **Voice / CW / Digital filter sharpness sliders** to set filter sharpness (0 = lowest latency to 3 = sharpest). The slider is disabled when **Auto** is enabled for that mode.

### Auto filter selection

Toggle **Auto (Voice / CW / Digital)** to enable automatic filter-level selection for that mode. When enabled, the manual sharpness slider is disabled.

### Low latency for digital modes

Check **Use Low Latency Filters for Digital Modes** to force low-latency filters in DIGU/DIGL.

---

## XVTR tab

The **XVTR** tab manages per-transverter configuration.

### Transverter list

The tab contains nested tabs, one per transverter, plus a **'+'** tab to create new entries.

### Controls per transverter

| Control | What it does | Notes |
|---|---|---|
| **RX Only:** | Forces RX-only on that transverter. | — |
| **Remove (xvtr)** | Deletes the transverter definition. | — |

### Adding a transverter

Click **Create New Transverter** to add a new transverter entry.

---

## USB Cables tab

The **USB Cables** tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable
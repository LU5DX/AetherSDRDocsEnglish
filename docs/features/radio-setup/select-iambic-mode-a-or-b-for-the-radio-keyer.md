# Radio Setup dialog

This page describes every control in the **Radio Setup** dialog
(`Settings > Radio Setup...`). The dialog has a tab strip along the top;
each section below covers one tab.

---

## Radio tab

Displays radio identification, license information, and firmware update controls.

### Indicators

| Indicator | Behavior |
|---|---|
| **Radio SN** | Chassis serial number (read-only). |
| **Model** | Radio model (read-only). |
| **HW Version** | Hardware version string (read-only). |
| **Region** | Regulatory region; default USA (read-only). |
| **FlexControl** | Detected state of FlexControl hardware (read-only). |
| **multiFLEX** | multiFLEX enabled state (read-only). |
| **Options** | Shows licensed radio options (read-only). |
| **License Info** | Displays subscription, expiration, Radio ID, and licensed version from the radio (read-only). |

### Editable fields

| Control | Kind | Behavior |
|---|---|---|
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Stored in `StationName`. Defaults to the OS hostname if left empty. Sent to the radio as `client station <name>`. |

### Buttons

| Control | Behavior |
|---|---|
| **Remote On** | Enables remote wake / remote-on. |
| **Check for Update** | Queries for available firmware updates. When an update is found, the status label reads: *Update available: vX.Y.Z — Download the SmartSDR installer from flexradio.com, then click 'Select Installer...' to stage it.* When firmware is current, the label reads: *Firmware is up to date (vX.Y.Z).* |
| **Select Installer...** | Opens a file picker. Accepts a SmartSDR `.msi` installer (FlexRadio v4.2+ WiX format), an `.exe` self-extracting installer (older releases), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs. PE/COFF MZ header) and extracts the `.ssdr` payload without external tools. Previously labelled **Browse .ssdr...** (changed in v0.9.3). |
| **Upload Firmware** | Starts the firmware upload. A progress bar and status label track progress. Enabled only after a valid file has been staged by **Select Installer...**. |

### Staging a firmware update (v0.9.3 and later)

1. Click **Check for Update**.
2. If an update is available, download the SmartSDR installer from flexradio.com.
3. Click **Select Installer...** and select the downloaded `.msi`, `.exe`, or `.ssdr` file.
   - The status label shows *Preparing firmware from \<filename\>...* while the stager extracts the payload.
4. When staging completes the status label confirms readiness and **Upload Firmware** becomes active.
5. Click **Upload Firmware** to transfer the firmware to the radio.

---

## Network tab

Displays network addresses and lets you adjust network settings.

### Indicators

| Indicator | Behavior |
|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses reported by the radio. |

### Controls

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Enforce Private IP Connections:** | Toggle button | — | Rejects non-RFC1918 peers. |
| **Network MTU:** | Spinbox | 1450 | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range: 576–9000 bytes. Stored in `NetworkMtu`. |
| **DHCP / Static** | Toggle button | — | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text fields | — | Static IP configuration fields. |
| **Apply** | Push button | — | Pushes the network configuration to the radio. |

---

## GPS tab

Displays GPS presence and live position data when a GPS receiver is attached to the radio.

| Indicator | Behavior |
|---|---|
| Live GPS data | Shows latitude, longitude, altitude, time, and satellite count. Updated in real time. |

---

## TX tab

Controls TX timings, interlocks, power limits, tune mode, and slice-follow behavior.

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Timings (in ms)** | Spinbox | — | TX hang and delay timings in milliseconds. |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle button | — | Enables the RCA and accessory interlock inputs. |
| **Max Power:** | Spinbox | — | Radio-level TX power cap (0–100%). |
| **Tune Mode:** | Combo box | — | Selects how the Tune button behaves. |
| **Show TX in Waterfall:** | Toggle button | — | Draws the TX signal in the waterfall display. |
| **TX Follows Active Slice** | Push button | False | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored in `TxFollowsActiveSlice`. |
| **Active Slice Follows TX** | Push button | False | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored in `ActiveFollowsTxSlice`. |
| **TX Band Settings** | Push button | — | Opens the dedicated per-band power and tune dialog. |

---

## Phone/CW tab

Configures the microphone, CW keyer, and RTTY defaults.

### Iambic keyer

1. Click `Settings > Radio Setup...`.
2. Click the **Phone/CW** tab.
3. Confirm **Iambic:** reads **Enabled**. If it reads **Disabled**, click it once to enable the keyer.
4. Click **A** or **B** to select Curtis iambic mode.

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle button | — | Shows the mic level meter during RX. |
| **Iambic:** | Toggle button | — | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Push button (mutually exclusive pair) | A | Selects Curtis iambic mode A or B for both the radio hardware keyer and the local software keyer. Mode A = Curtis A; Mode B = Curtis B. Added in v0.9.1. |
| **Swap:** | Toggle button | — | Swaps dit and dah. |
| **Sideband:** | Combo box | — | Selects CW pitch sideband (LSB or USB). |
| **CWX:** | Toggle button | — | Enables CWX macro keying. |
| **Decode:** | Toggle button | True | Enables the CW decode overlay on the panadapter. Stored in `CwDecodeOverlay`. |
| **RTTY Mark Default:** | Spinbox | — | Default RTTY mark frequency. |

**Mode A vs. Mode B:** Mode A (Curtis A) releases the last element when both paddles are released mid-squeeze. Mode B (Curtis B) completes the last element before stopping. The local software keyer mirrors whichever mode you select, providing sub-5 ms sidetone response independent of network latency.

---

## RX tab

Provides GPSDO frequency offset calibration and 10 MHz reference source selection.

In v0.9.2.1, the calibration controls became available regardless of whether a GPSDO is installed. The status label at the top of the group reads:

- **GPSDO installed. Manual frequency offset calibration available.** (green) — GPSDO present.
- **Manual frequency offset calibration available.** (amber) — no GPSDO.

### Using frequency calibration

1. Click `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
4. Click **Start**.
   - The button label changes to **Busy** and becomes disabled while calibration runs.
   - The status label reports progress (Starting… and subsequent states).
   - AetherSDR resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`) before starting the sweep.
5. When calibration completes, the button re-enables and the status label updates with the result.
6. If **Cal Frequency (MHz):** is empty when you click **Start**, the status label shows **Enter cal frequency** and calibration does not begin.

### Calibration controls

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | — | Frequency used for calibration. Must not be empty before clicking Start. |
| **Start** | Push button | — | Resets frequency error to 0 ppb, then starts the calibration sweep. Disabled and labelled Busy during an active calibration. |
| **Freq Offset (ppb):** | Spinbox | — | Manual frequency offset in parts per billion. Applied directly without running a sweep. |
| **10 MHz Reference Source:** | Combo box | Auto | Selects the oscillator reference source: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. Lock status (Locked / Unlocked) is shown alongside and updates live. |

---

## Audio tab

Configures radio audio outputs, PC audio devices, recording, and the NVIDIA BNR container.

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Line Out:** | Slider | — | Line-out gain. |
| **Mute (Line Out)** | Push button | — | Mutes line-out. |
| **Headphone:** | Slider | — | Headphone gain. |
| **Mute (Headphone)** | Push button | — | Mutes headphone output. |
| **Front Speaker: / Mute** | Push button | — | Mutes the front speaker (model-specific). |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Push button | Auto | Selects the audio codec for SmartLink/LAN connections. Stored in `AudioCompression`. |
| **Prevent system sleep while connected** | Checkbox | False | Keeps the OS awake while the radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored in `InhibitSleepWhileConnected`. |
| **PC Audio Devices: Input: / Output:** | Combo box | — | Picks the host audio input and output devices. |
| **Audio Boost:** | Toggle button | — | Enables extra gain on the client audio path. Stored in `AudioBoost`. |
| **Audio Buffer:** | Text field | 200 | Audio buffer size in milliseconds for VPN/SmartLink jitter compensation. Range: 50–1000 ms. Stored in `AudioBufferMs`. |
| **Recording: Radio Side / Client Side** | Push button | Radio Side | Selects radio-side or client-side recording. Stored in `RecordingMode`. |
| **Save to:** | Text field | — | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored in `QsoRecordingDir`. |
| **...** | Push button | — | Opens a folder browser for the recording directory. |
| **Auto-record on TX** | Checkbox | False | Automatically records while transmitting. Stored in `QsoRecordingAutoRecord`. |
| **Idle timeout:** | Spinbox | 120 | Seconds of silence before recording stops. Range: 10–3600 s. Stored in `QsoRecordingIdleTimeout`. |
| **NVIDIA BNR: Autostart Container / Start / Stop / Check Status** | Push button |
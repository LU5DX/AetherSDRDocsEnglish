# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, Phone/CW, RX, audio, antennas, filters, XVTR, USB cables, peripherals, APD, themes, and serial port configuration.

## Opening the dialog

1. Open `Settings > Radio Setup...`.
2. The dialog opens as a persistent window. Its size and position are saved between sessions.

---

## Radio tab

The Radio tab displays radio information, identification, license info, and firmware update controls.

### Radio information

| Control | Type | Behavior |
|---|---|---|
| Radio SN | Indicator | Chassis serial number (read-only). |
| Region | Indicator | Radio regulatory region. |
| HW Version | Indicator | Hardware version string. |
| Model | Indicator | Radio model. |
| Options | Indicator | Shows licensed radio options. |
| FlexControl | Indicator | Detected state of FlexControl hardware. |
| multiFLEX | Indicator | multiFLEX enabled state. |
| Nickname | Text field | User-friendly radio nickname. |
| Callsign | Text field | Station callsign. |
| Station Name | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings. Sent to radio as 'client station \<name\>'. |
| License Info | Indicator | Displays license details from the radio (Subscription, Expiration, Radio ID, Licensed version). |

### Remote On

Click **Remote On** to enable remote wake / remote-on functionality.

### Firmware update

**Check for Update** queries the radio for available firmware updates. When a newer version is found, AetherSDR displays an informational message:

> Update available: v*X.Y.Z*
> Download the SmartSDR installer from flexradio.com,
> then click 'Select Installer...' to stage it.

**Select Installer...** (renamed from Browse .ssdr... in v0.9.3) accepts three file types:

| File type | Extension | Notes |
|---|---|---|
| SmartSDR WiX installer | .msi | FlexRadio v4.2 and later |
| SmartSDR self-extracting installer | .exe | Older SmartSDR releases |
| Extracted firmware file | .ssdr | As in previous AetherSDR versions |

The firmware stager detects the format automatically from the first 8 bytes of the file (OLE/MSI magic versus PE/COFF MZ header) and extracts the .ssdr payload without requiring any external tools.

#### To stage firmware from a local installer

1. Download the SmartSDR installer from flexradio.com.
2. Open `Settings > Radio Setup...`.
3. Click the **Radio** tab.
4. Click **Select Installer...**.
5. In the file picker, select the .msi, .exe, or .ssdr file.
6. AetherSDR extracts and stages the firmware. Watch the progress bar and status line for progress and any errors.
7. When staging is complete, click **Upload Firmware** to send the firmware to the radio.

---

## Network tab

The Network tab displays radio network information and advanced network options.

### Network information

| Control | Type | Behavior |
|---|---|---|
| IP Address / Mask / MAC Address | Indicator | Read-only network addresses. |

### Network settings

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| Enforce Private IP Connections | Toggle button | — | — | Rejects non-RFC1918 peers. |
| Network MTU | Spinbox | 1450 | 576–9000 bytes | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings. |
| DHCP / Static | Toggle button | — | — | Switches between DHCP and Static IP modes. |
| IP Address / Mask / Gateway | Text field | — | — | Static IP configuration fields. |
| Apply | Push button | — | — | Pushes the network config to the radio. |

---

## GPS tab

The GPS tab shows GPS presence and live latitude, longitude, altitude, time, and satellites information.

---

## TX tab

The TX tab contains TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow options, and a TX Band Settings shortcut.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

The TX timings section includes spinbox fields for millisecond values.

| Control | Display label | Default | Behavior |
|---|---|---|---|
| ACC TX | ACC TX: | — | ACC timing delay in ms. |
| TX Delay | TX Delay: | — | TX delay in ms. |
| RCA TX1 | RCA TX1: | — | RCA TX1 delay in ms. |
| Timeout | Timeout (sec): | — | Interlock timeout displayed in seconds. The radio stores this value in milliseconds. |

### Interlocks

**TX REQ: RCA** and **TX REQ: Accessory** toggle buttons enable RCA and accessory interlock inputs.

### Power and tune

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| Max Power | Spinbox | — | 0–100% | Sets radio-level TX power cap. |
| Tune Mode | Combo box | — | — | Selects how the tune button behaves. |

### Waterfall and slice follow

| Control | Type | Default | Setting key | Behavior |
|---|---|---|---|---|
| Show TX in Waterfall | Toggle button | — | — | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | False | `TxFollowsActiveSlice` | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | False | `ActiveFollowsTxSlice` | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. |

---

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### Microphone

**Enable/Disable the Level Meter During Receive** toggles showing the mic level meter even in RX.

### CW keyer

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| Iambic | Toggle button | — | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| Iambic Mode | Push button | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| Swap | Toggle button | — | — | Swaps dit/dah. |
| Sideband | Combo box | — | LSB / USB | Selects CW pitch sideband. |
| CWX | Toggle button | — | — | Enables CWX macro keying. |
| Decode | Toggle button | True | — | Enables the CW decode overlay on the panadapter. Setting key: `CwDecodeOverlay`. |

### RTTY

**RTTY Mark Default** spinbox sets the default RTTY mark frequency.

---

## RX tab

The RX tab contains GPSDO frequency offset calibration and 10 MHz reference source selection.

### Frequency calibration

| Control | Type | Behavior |
|---|---|---|
| Cal Frequency (MHz) | Spinbox | Frequency used for manual calibration. |
| Start | Push button | Starts the frequency calibration sweep. |
| Freq Offset (ppb) | Spinbox | Manual frequency offset in ppb. |

### 10 MHz Reference Source

The **10 MHz Reference Source:** combo box lists available oscillator sources dynamically based on hardware present and the radio's reported oscillator state.

| Label | Internal value | When shown |
|---|---|---|
| Auto | auto | Always shown |
| TCXO | tcxo | Shown when TCXO hardware is present, oscillator status has been received, or the current or saved setting is `tcxo` |
| GPSDO | gpsdo | Shown when GPSDO hardware is present or the current or saved setting is `gpsdo` |
| External 10 MHz | external | Shown when an external reference is present, oscillator status has been received, or the current or saved setting is `external` |

#### Lock status display

The lock status label beside the combo shows richer information than plain text:

| Situation | Example text shown |
|---|---|
| Oscillator status not yet received | `Waiting for oscillator status` |
| Auto mode has resolved to a source | `Auto -> GPSDO Locked` |
| Saved setting differs from active state | `TCXO -> GPSDO Locked` |
| Setting and state agree | `GPSDO Locked` |
| External selected but reference not detected | `External 10 MHz Unlocked (not detected)` |

The label color updates automatically: green (`#00c040`) when locked, red (`#c04040`) when unlocked, and grey (`#8aa8c0`) while waiting for status.

---

## Audio tab

The Audio tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

### Radio audio outputs

| Control | Type | Behavior |
|---|---|---|
| Line Out | Slider | Line-out gain. |
| Mute (Line Out) | Push button | Mutes line-out. |
| Headphone | Slider | Headphone gain. |
| Mute (Headphone) | Push button | Mutes headphone. |
| Front Speaker / Mute | Push button | Mutes front speaker (model-specific). |

### Audio compression

**Audio Compression (SmartLink):** toggles between Auto, Uncompressed, and Opus. Setting key: `AudioCompression`.

### System sleep

**Prevent system sleep while connected** checkbox keeps the OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Default: False. Setting key: `InhibitSleepWhileConnected`.

### PC audio devices

**PC Audio Devices: Input:** and **Output:** combo boxes pick host audio input and output devices.

### Audio boost

**Audio Boost** toggle button enables extra gain on the client audio path. Setting key: `AudioBoost`.

### Audio buffer

**Audio Buffer** text field sets the audio buffer in milliseconds for VPN/SmartLink jitter. Default: 200. Range: 50–1000 ms. Setting key: `AudioBufferMs`.

### Recording

| Control | Type | Default | Setting key | Behavior |
|---|---|---|---|---|
| Recording | Push button | Radio Side | `RecordingMode` | Picks radio-side or client-side recording. Options: Radio Side / Client Side. |
| Save to | Text field | — | `QsoRecordingDir` | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. |
| ... | Push button | — | — | Browses for recording folder. |
| Auto-record on TX | Checkbox | False | `QsoRecordingAutoRecord` | Automatically records while transmitting. |
| Idle timeout | Spinbox | 120 | `QsoRecordingIdleTimeout` | Seconds of silence before recording stops. Range: 10–3600 sec. |

### NVIDIA BNR

**NVIDIA BNR** controls (Autostart Container, Start, Stop, Check Status) manage the NVIDIA Broadcast noise-removal container. A status dot indicates Running (green), Stopped (red), or Unknown (grey).

---

## Antennas tab

The Antennas tab allows naming radio antenna ports for display in the panadapter and slice panels. This tab is built lazily when first clicked.

---

## Filters tab

The Filters tab provides low-latency and sharp filter options per bandwidth.

### Filter sharpness

**Voice / CW / Digital filter sharpness sliders** set filter sharpness (0 = lowest latency to 3 = sharpest) per mode. The slider is disabled when Auto is enabled.

**Auto (Voice / CW / Digital)** toggle buttons enable automatic filter-level selection for that mode, disabling the manual sharpness slider.

### Digital mode filters

**Use Low Latency Filters for Digital Modes** checkbox forces low-latency filters in DIGU/DIGL.

---

## XVTR tab

The XVTR tab configures per-transverter settings. It contains nested tabs, one per transverter, and a '+' tab for creating new transverters.

| Control | Type | Behavior |
|---|---|---|
| RX Only | Toggle button | Forces RX-only on that transverter. |
| Remove | Push button | Deletes the transverter definition. |
| Create New Transverter | Push button | Adds a new transverter entry. |

---

## USB Cables tab

The USB Cables tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

| Control | Type | Behavior |
|---|---|---|
| Cables list / Status | Indicator | Detected USB cables per type with Plugged/Unplugged status. |
| Name / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0–7) | Combo box | Per-cable serial parameters and behavior. |

---

## Peripherals tab

The Peripherals tab enables manual IP connection to external devices (TGXL, PGXL, Antenna Genius, or ShackSwitch) when automatic discovery has not picked up the device.

### Before you start

- AetherSDR must already be connected to a FLEX-8600 radio. The Peripherals tab is only available when a radio connection is active.
- Have the IP address of the TGXL, PGXL, Antenna Genius, or ShackSwitch device ready.

### Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Peripherals**
# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It provides access to radio information, network settings, GPS, TX configuration, Phone/CW settings, RX calibration, audio configuration, antenna names, filter options, transverter definitions, USB cable assignments, peripheral connections, APD sampling, theme appearance, and FlexControl serial port setup.

## Before you start

- AetherSDR must be connected to the radio. Many fields are populated from live radio data.
- The dialog remembers its size and position between sessions. If the dialog appears off-screen, delete the `RadioSetupDialogGeometry` entry from your settings file.

## Opening Radio Setup

1. Click `Settings > Radio Setup...`.
2. The dialog opens at its last-used position and size.

# Radio tab

The Radio tab shows identifying information reported directly by the radio — serial number, hardware version, regulatory region, and licensed options. Use this page to verify what hardware and options your radio has before troubleshooting or contacting support.

## Steps

1. Click `Settings > Radio Setup...`.
2. The dialog opens on the **Radio** tab by default.
3. Read the values in the **Radio Information** group:
   - **Radio SN** — the chassis serial number.
   - **HW Version** — the hardware version string reported by the radio.
   - **Region** — the radio's regulatory region (defaults to `USA` if the radio does not report one).
   - **Options** — the licensed options active on this radio (for example, `GPS`, `PGXL`).

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Radio SN | Indicator (read-only) | Chassis serial number as reported by the radio. |
| HW Version | Indicator (read-only) | Hardware version string prefixed with `v`. |
| Region | Indicator (read-only) | Regulatory region. Displays `USA` if the radio reports none. |
| Options | Indicator (read-only) | Licensed radio options. |
| Remote On | Push button | Enables remote wake / remote-on. |
| FlexControl | Indicator | Detected state of FlexControl hardware. |
| multiFLEX | Indicator | multiFLEX enabled state. |
| Model | Indicator | Radio model. |
| Nickname | Text field | User-friendly radio nickname. |
| Callsign | Text field | Station callsign. |
| Station Name | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. |
| License Info | Indicator | Displays license details from the radio (Subscription / Expiration / Radio ID / Licensed version). |
| Check for Update | Push button | Queries for firmware updates. |
| Browse .ssdr... | Push button | Chooses a firmware image file. |
| Upload Firmware | Push button | Starts firmware upload with progress bar and status. |

All Radio Information fields are read-only. No persisted settings keys are associated with them.

# Network tab

The Network tab shows radio network information and advanced network options.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Network** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| IP Address / Mask / MAC Address | Indicator (read-only) | Read-only network addresses. |
| Enforce Private IP Connections: | Toggle button | Rejects non-RFC1918 peers. |
| Network MTU: | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range 576-9000 bytes, default 1450. Stored in AppSettings as `NetworkMtu`. |
| DHCP / Static | Toggle button | Switches between DHCP and Static IP modes. |
| IP Address: / Mask: / Gateway: | Text field | Static IP configuration fields. |
| Apply | Push button | Pushes the network config to the radio. |

# GPS tab

The GPS tab shows GPS presence and live lat/lon/alt/time/satellites info.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **GPS** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| GPS | Tab | GPS presence and live lat/lon/alt/time/satellites info. |

# TX tab

The TX tab shows TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow and TX Band Settings shortcut.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **TX** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| TX Band Settings | Push button | Opens the dedicated per-band power/tune dialog. |
| Timings (in ms / Timeout (sec)) | Spinbox / Text field | TX hang / delay timings. The **Timeout** field is displayed in seconds; the radio stores the value in milliseconds (FlexLib internal). |
| Interlocks - TX REQ: RCA / Accessory | Toggle button | Enables RCA and accessory interlock inputs. |
| Max Power: | Spinbox | Sets radio-level TX power cap. Range 0-100 %. |
| Tune Mode: | Combo box | Selects how the tune button behaves. |
| Show TX in Waterfall: | Toggle button | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. |

### TX Timings

The timing fields control how long the radio holds key states:

| Field | Display unit | Radio storage unit | Behavior |
|---|---|---|---|
| ACC TX: | ms | ms | Accessory TX delay. |
| TX Delay: | ms | ms | TX keying delay. |
| RCA TX1: | ms | ms | RCA TX1 delay. |
| Timeout: | seconds | ms | Interlock timeout. Displayed in whole seconds for readability; the radio expects and stores milliseconds. |

# Phone/CW tab

The Phone/CW tab shows microphone, CW keyer, RTTY defaults.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Phone/CW** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Enable/Disable the Level Meter During Receive | Toggle button | Shows mic level meter even in RX. |
| Iambic: | Toggle button | Enables or disables the iambic keyer on the radio. |
| Iambic Mode: A / B | Push button | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| Swap: | Toggle button | Swaps dit/dah. |
| Sideband: | Combo box | Selects CW pitch sideband (LSB | USB). |
| CWX: | Toggle button | Enables CWX macro keying. |
| Decode: | Toggle button | Enables the CW decode overlay on the panadapter. Stored in AppSettings as `CwDecodeOverlay`. |
| RTTY Mark Default: | Spinbox | Default RTTY mark frequency. |

# RX tab

The RX tab shows GPSDO frequency offset calibration and 10 MHz reference source.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **RX** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Cal Frequency (MHz): | Spinbox | Frequency used for manual calibration. |
| Start | Push button | Starts the frequency calibration sweep. |
| Freq Offset (ppb): | Spinbox | Manual frequency offset in ppb. |
| 10 MHz Reference Source: | Combo box | Selects oscillator reference source. Options: Auto, TCXO, GPSDO, External. Lock status (Locked / Unlocked) is shown alongside. |

## Frequency calibration

The calibration controls are always visible regardless of whether a GPSDO is installed. The status banner at the top of the group reads:

- **GPSDO installed** — "GPSDO installed. Manual frequency offset calibration available." (green text)
- **No GPSDO** — "Manual frequency offset calibration available." (amber text)

The following controls are available in both configurations:

| Label | Kind | Behavior |
|---|---|---|
| Cal Frequency (MHz): | Spinbox | Frequency used for calibration. Enter the known reference frequency before clicking Start. |
| Start | Push button | Starts the frequency calibration sequence. The button is disabled and its label changes to **Busy** while calibration is in progress. Before triggering the PLL sweep, AetherSDR resets the radio's frequency error to zero (`radio set freq_error_ppb=0`) and then issues `radio pll_start`. If the Cal Frequency field is empty, the button shows a warning and takes no action. |
| Freq Offset (ppb): | Spinbox | Manual frequency offset in parts per billion, applied after calibration completes or set directly for manual correction. |

A status label appears to the right of the Start button and updates throughout the calibration sequence:

| State | Text | Color |
|---|---|---|
| Idle | *(empty)* | — |
| Cal frequency not entered | "Enter cal frequency" | Amber |
| Sequence started | "Starting…" | Grey-blue |
| In progress | Updated as PLL state is reported by the radio | Grey-blue |

The Start button is re-enabled and its label reverts to **Start** when the calibration sequence completes or fails.

## 10 MHz reference source

The **10 MHz Reference Source:** combo box and its accompanying lock-status label were updated to handle a wider range of oscillator states reported by the radio.

**Combo box population:** The list of available sources is built dynamically each time the tab opens or the radio's oscillator state changes. Sources appear in the combo only if the radio reports the relevant hardware as present, if the current setting or active state uses that source, or if oscillator status has been received (in which case TCXO and External 10 MHz are always included as options).

| Source value | Label shown in combo |
|---|---|
| `auto` | Auto |
| `tcxo` | TCXO |
| `gpsdo` | GPSDO |
| `external` / `ext` | External 10 MHz |

**Lock-status label:** The label to the right of the combo shows richer state information:

| Condition | Text shown | Color |
|---|---|---|
| No oscillator status received yet | "Waiting for oscillator status" | Grey-blue |
| Source locked | `<source> Locked` | Green (`#00c040`) |
| Source unlocked | `<source> Unlocked` | Red (`#c04040`) |
| Auto mode has selected a source | `Auto -> <resolved source> Locked/Unlocked` | Green or red |
| Setting and active state differ | `<setting> -> <active> Locked/Unlocked` | Green or red |
| External selected but no signal detected | `External 10 MHz` | Grey-blue |

# Audio tab

The Audio tab shows radio audio outputs, compression, PC devices, boost, buffer, recording and NVIDIA BNR container.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Audio** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Line Out: | Slider | Line-out gain. |
| Mute (Line Out) | Push button | Mutes line-out. |
| Headphone: | Slider | Headphone gain. |
| Mute (Headphone) | Push button | Mutes headphone. |
| Front Speaker: / Mute | Push button | Mutes front speaker (model-specific). |
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Push button | Selects audio codec for SmartLink/LAN. Stored in AppSettings as `AudioCompression`. |
| Prevent system sleep while connected | Checkbox | Keeps OS awake while radio is connected. Stored in AppSettings as `InhibitSleepWhileConnected`. |
| PC Audio Devices: Input: / Output: | Combo box | Picks host audio in/out devices. |
| Audio Boost: | Toggle button | Enables extra gain on the client audio path. Stored in AppSettings as `AudioBoost`. |
| Audio Buffer: | Text field | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Range 50-1000 ms, default 200. Stored in AppSettings as `AudioBufferMs`. |
| Recording: Radio Side / Client Side | Push button | Picks radio-side or client-side recording. Stored in AppSettings as `RecordingMode`. |
| Save to: | Text field | Folder for saved recordings (client-side only). Stored in AppSettings as `QsoRecordingDir`. |
| ... | Push button | Browses for recording folder. |
| Auto-record on TX | Checkbox | Automatically records while transmitting. Stored in AppSettings as `QsoRecordingAutoRecord`. |
| Idle timeout: | Spinbox | Seconds of silence before recording stops. Range 10-3600 sec, default 120. Stored in AppSettings as `QsoRecordingIdleTimeout`. |
| NVIDIA BNR: Autostart Container / Start / Stop / Check Status | Push button | Controls the NVIDIA Broadcast noise-removal container. |

# Antennas tab

The Antennas tab allows you to assign user-friendly names to each antenna port on the radio.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Antennas** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| ANT1 / ANT2 / XVTA / XVTB | Text field | Text fields for entering custom names for each
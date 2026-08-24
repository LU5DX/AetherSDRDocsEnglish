# Radio Setup Dialog

## Overview

The Radio Setup dialog is the master per-radio configuration window. It provides access to radio information, network settings, GPS, transmit configuration, phone/CW settings, receive calibration, audio, filters, transverters, USB cables, peripherals, serial ports, SmartLink pinned certificate management, KiwiSDR receiver configuration, and APD settings.

To open the dialog, click `Settings > Radio Setup...`. The dialog requires an active radio connection.

## Radio Tab

The Radio tab displays radio identification information, license details, and firmware update controls.

### Information Fields

| Control | Kind | Behavior |
|---------|------|----------|
| Radio SN | Indicator | Chassis serial number (read-only). Includes a clipboard copy button next to the value. |
| Region | Indicator | Radio regulatory region. |
| HW Version | Indicator | Hardware version string. Includes a clipboard copy button. |
| Options | Indicator | Shows licensed radio options. Includes a clipboard copy button. |
| FlexControl | Indicator | Detected state of FlexControl hardware. |
| multiFLEX | Indicator | multiFLEX enabled state. |
| Model | Indicator | Radio model. Includes a clipboard copy button. |
| Nickname | Text field | User-friendly radio nickname. |
| Callsign | Text field | Station callsign. |
| Station Name | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored as `StationName` in AppSettings. Sent to radio as 'client station <name>'. |
| License Info (Subscription / Expiration / Radio ID / Licensed version) | Indicator | Displays license details from the radio. Each field includes a clipboard copy button. |

### Controls

| Control | Kind | Behavior |
|---------|------|----------|
| Remote On | Push button | Enables remote wake / remote-on. |
| Check for Update | Push button | Queries for firmware updates. |
| Select Installer... | Push button | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. |
| Upload Firmware | Push button | Starts firmware upload with progress bar and status. |
| Reboot Radio | Push button | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes. New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot. |
| Agent Automation (MCP): | Toggle button | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token: | Text field | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store. New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| Copy (Access Token) | Push button | Copies the access token to the clipboard. New in v26.8.4. |
| Rotate (Access Token) | Push button | Generates a new token and applies it immediately, locking out any client still using the old one. New in v26.8.4. |
| Allow TX via MCP: Enable transmit control | Checkbox | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| Observe only: Read-only (block all driving) | Checkbox | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs. |
| VITA-49 RX buffer: | Slider | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted. |
| granted: (VITA-49 RX buffer) | Indicator | Shows the buffer size the kernel actually granted (vs the requested preset). New in v26.8.4. Shows '(applies on connect)' when no connection is active. |

## Network Tab

The Network tab displays radio network information and advanced network options.

### Information Fields

| Control | Kind | Behavior |
|---------|------|----------|
| IP Address / Mask / MAC Address | Indicator | Read-only network addresses. Each includes a clipboard copy button. |

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Enforce Private IP Connections: | Toggle button | Enabled | - | Rejects non-RFC1918 peers. |
| Network MTU: | Spinbox | 1450 | 576-9000 bytes | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored as `NetworkMtu` in AppSettings. |
| DHCP / Static | Toggle button | - | - | Switches between DHCP and Static IP modes. |
| IP Address: / Mask: / Gateway: | Text field | - | - | Static IP configuration fields. |
| Apply | Push button | - | - | Pushes the network config to the radio. |

## GPS Tab

The GPS tab displays GPS presence and live position information including latitude, longitude, altitude, time, and satellite count.

## TX Tab

The TX tab controls transmit timings, interlocks, maximum power, tune mode, waterfall display, and slice/TX follow behavior.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| TX Band Settings | Push button | - | - | Opens the dedicated per-band power/tune dialog. |
| Timings (in ms) | Spinbox | - | - | TX hang / delay timings. |
| Interlocks - TX REQ: RCA / Accessory | Toggle button | - | - | Enables RCA and accessory interlock inputs. |
| Max Power: | Spinbox | - | 0-100 % | Sets radio-level TX power cap. |
| Tune Mode: | Combo box | - | - | Selects how the tune button behaves. |
| Show TX in Waterfall: | Toggle button | - | - | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | False | - | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | False | - | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. |

## Phone/CW Tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Enable/Disable the Level Meter During Receive | Toggle button | - | - | Shows mic level meter even in RX. |
| Iambic: | Toggle button | - | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| Iambic Mode: A / B | Push button | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| Swap: | Toggle button | - | - | Swaps dit/dah. |
| Sideband: | Combo box | - | LSB / USB | Selects CW pitch sideband. |
| CWX: | Toggle button | - | - | Enables CWX macro keying. |
| Decode: RX | Toggle button | True | - | Enables the CW decode overlay on the panadapter for received CW. Stored as nested JSON under `CwDecoder` (rx field). |
| Decode: TX | Toggle button | False | - | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Stored as nested JSON under `CwDecoder` (tx field). |
| RTTY Mark Default: | Spinbox | - | - | Default RTTY mark frequency. |

## RX Tab

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Cal Frequency (MHz): | Spinbox | - | - | Frequency used for manual calibration. |
| Start | Push button | - | - | Starts the frequency calibration sweep. |
| Freq Offset (ppb): | Spinbox | - | - | Manual frequency offset in ppb. |
| 10 MHz Reference Source: | Combo box | Auto | Auto / TCXO / GPSDO / External | Selects oscillator reference source. Options shown depend on hardware installed. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

## Calibration Tab

The Calibration tab provides manual frequency calibration for radios that cannot calibrate their own oscillator (e.g. HL2). This tab is hidden unless the connected radio's backend supports host frequency calibration; it is capability-gated, not family-gated, so it never appears on a Flex where the RX tab's hardware calibration handles the task.

The tab re-reads the stored calibration each time the dialog is shown, so a `freqcal` bridge call or a different radio's settings made while the dialog was closed are picked up before any Trim press can commit the wrong value.

### Controls

| Control | Kind | Behavior |
|---------|------|----------|
| Calibration controls | Various | Frequency calibration inputs and Trim control for the connected radio. Re-seeded from the live radio model whenever the dialog opens or the connection changes. |

## Audio Tab

The Audio tab manages radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

### Controls

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Line Out: | Slider | - | - | Line-out gain. |
| Mute (Line Out) | Push button | - | - | Mutes line-out. |
| Headphone: | Slider | - | - | Headphone gain. |
| Mute (Headphone) | Push button | - | - | Mutes headphone. |
| Front Speaker: / Mute | Push button | - | - | Mutes front speaker (model-specific). |
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Push button | Auto | - | Selects audio codec for SmartLink/LAN. Stored as `AudioCompression`. |
| Prevent system sleep while connected | Checkbox | False | - | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. |
| PC Audio Devices: Input: / Output: | Combo box | - | - | Picks host audio in/out devices. |
| Audio Boost: | Toggle button | - | - | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| Audio Buffer: | Text field | 200 | 50-1000 ms | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Stored as `AudioBufferMs`. |
| Recording: Radio Side / Client Side | Push button | Radio Side | Radio Side / Client Side | Picks radio-side or client-side recording. Stored as `RecordingMode`. |
| Save to: | Text field | - | - | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored as `QsoRecordingDir`. |
| ... | Push button | - | - | Browses for recording folder. |
| Auto-record on TX | Checkbox | False | - | Automatically records while transmitting. Stored as `QsoRecordingAutoRecord`. |
| Idle timeout: | Spinbox | 120 | 10-3600 sec | Seconds of silence before recording stops. Stored as `QsoRecordingIdleTimeout`. |
| NVIDIA BNR: Autostart Container / Start / Stop / Check Status | Push button | - | - | Controls the NVIDIA
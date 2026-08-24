# Radio Setup Dialog

The **Radio Setup** dialog is the master per-radio configuration window. It contains radio information, network settings, GPS, TX, Phone/CW, RX, audio, filters, XVTR, USB cables, peripherals serial port, SmartLink pinned certificate management, and KiwiSDR public receiver settings.

## Opening the dialog

1. Click **Settings > Radio Setup...** in the main menu.

## Radio (tab)

The Radio tab displays radio identification, license information, and provides firmware update controls.

### Read-only indicators with copy buttons

All read-only fields include a clipboard copy button (tray icon) next to the label for easy sharing with support.

| Control | Behavior |
|---------|----------|
| **Radio SN** | Chassis serial number (read-only). Includes a clipboard copy button. |
| **Region** | Radio regulatory region (read-only). Includes a clipboard copy button. |
| **HW Version** | Hardware version string (read-only). Includes a clipboard copy button. |
| **Options** | Shows licensed radio options (read-only). Includes a clipboard copy button. |
| **Model** | Radio model (read-only). Includes a clipboard copy button. |
| **License Info** fields | Displays Subscription, Expiration, Radio ID, and Licensed version. Each includes a clipboard copy button. |

### Other controls on the Radio tab

| Control                                     | Behavior                                                                                                                                                                 | Setting key                                                                                                                                                                                                                                                                      |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **FlexControl**                             | Detected state of FlexControl hardware.                                                                                                                                  | (none)                                                                                                                                                                                                                                                                           |
| **multiFLEX**                               | multiFLEX enabled state.                                                                                                                                                 | (none)                                                                                                                                                                                                                                                                           |
| **Nickname**                                | User-friendly radio nickname.                                                                                                                                            | (none)                                                                                                                                                                                                                                                                           |
| **Callsign**                                | Station callsign.                                                                                                                                                        | (none)                                                                                                                                                                                                                                                                           |
| **Station Name**                            | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty.                                                                      | `StationName`                                                                                                                                                                                                                                                                    |
| **Remote On**                               | Enables remote wake / remote-on.                                                                                                                                         | (none)                                                                                                                                                                                                                                                                           |
| **Check for Update**                        | Queries for firmware updates.                                                                                                                                            | (none)                                                                                                                                                                                                                                                                           |
| **Select Installer...**                     | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file.                                                                          | (none)                                                                                                                                                                                                                                                                           |
| **Upload Firmware**                         | Starts firmware upload with progress bar and status.                                                                                                                     | (none)                                                                                                                                                                                                                                                                           |
| Reboot Radio                                | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes.                                        | New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot.                                                            |
| Agent Automation (MCP):                     | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.      | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                               | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                           | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                         | Copies the access token to the clipboard.                                                                                                                                | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                       | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                        | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control   | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                              | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                          | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                          | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                             | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |

## Calibration (tab)

New in v26.8.4. Manual frequency calibration for radios that cannot calibrate themselves (HL2 and any other backend whose `hostFrequencyCalibration` capability is false). The tab is hidden for radios that handle their own oscillator calibration (e.g., Flex, which uses the Receive tab's hardware calibration).

The tab is gated on the radio's capability, not on the family name: if the radio corrects its own oscillator, the page stays hidden. The page title is searchable with keywords such as "frequency calibration ppb ppm oscillator crystal clock error wwv gpsdo zero beat."

The stored calibration value is re-read whenever the dialog is opened (so a `freqcal` bridge call made while the dialog was closed is reflected) and whenever a different radio is connected, so a later **Trim** press cannot commit the previous radio's number.

| Control | Behavior |
|---------|----------|
| **Calibration** page | Manual oscillator frequency offset calibration for radios that lack built-in calibration. Shown only when the connected backend reports `hostFrequencyCalibration`. |

## Network (tab)

Advanced network configuration for the radio.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each includes a clipboard copy button. | (none) |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers. Toggle button displays "Enabled" when checked. | (none) |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes (576-9000). Default 1450. | `NetworkMtu` |
| **DHCP / Static** | Switches between DHCP and Static IP modes. | (none) |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields (shown when Static mode is selected). | (none) |
| **Apply** | Pushes the network config to the radio. | (none) |
| **Reboot Radio** | Opens a confirmation dialog before rebooting the radio. AetherSDR disconnects and, for LAN connections, automatically reconnects after the radio boots. SmartLink/WAN requires manual reconnect. Button is disabled when radio is disconnected. | (none) |

## GPS (tab)

Displays GPS presence and live location/time/satellite information.

## TX (tab)

Transmit configuration including timings, interlocks, power limits, and slice follow behavior.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **TX Band Settings** | Opens the dedicated per-band power/tune dialog. | (none) |
| **Timings (in ms)** | TX hang / delay timings. | (none) |
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs. | (none) |
| **Max Power:** | Sets radio-level TX power cap (0-100%). | (none) |
| **Tune Mode:** | Selects how the tune button behaves. | (none) |
| **Show TX in Waterfall:** | Draws TX signal in the waterfall. | (none) |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. | `TxFollowsActiveSlice` |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. | `ActiveFollowsTxSlice` |

## Phone/CW (tab)

Microphone, CW keyer, and RTTY defaults.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. | (none) |
| **Iambic:** | Enables or disables the iambic keyer on the radio. | (none) |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | (none) |
| **Swap:** | Swaps dit/dah. | (none) |
| **Sideband:** | Selects CW pitch sideband (LSB/USB). | (none) |
| **CWX:** | Enables CWX macro keying. | (none) |
| **Decode: RX** | Enables the CW decode overlay on the panadapter for received CW. | `CwDecoder` (nested JSON, `rx` field) |
| **Decode: TX** | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. | `CwDecoder` (nested JSON, `tx` field) |
| **RTTY Mark Default:** | Default RTTY mark frequency. | (none) |

## RX (tab)

GPSDO frequency offset calibration and 10 MHz reference source.

| Control | Behavior |
|---------|----------|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. |
| **Start** | Starts the frequency calibration sweep. |
| **Freq Offset (ppb):** | Manual frequency offset in ppb. |
| **10 MHz Reference Source:** | Selects oscillator reference source (Auto/TCXO/GPSDO/External). Lock status shown alongside. |

## Antennas (tab)

Per-port antenna display-name editor for the radio. Lets the operator assign custom names to each antenna port (ANT1, ANT2, XVTA, XVTB, etc.) which are shown in the panadapter RX/TX antenna indicators instead of the raw port tokens.

| Control | Behavior |
|---------|----------|
| **Port / Custom name / Preview / Clear** (table columns) | Grid of antenna port rows. Each row has a read-only port label (e.g. ANT1), an editable text field (max 16 chars), a preview of the final display name, and a Clear button to reset the custom name. |

## Audio (tab)

Radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

| Control | Behavior | Setting key |
|---------|----------|-------------|
| **Line Out:** | Line-out gain slider. | (none) |
| **Mute (Line Out)** | Mutes line-out. | (none) |
| **Headphone:** | Headphone gain slider. | (none) |
| **Mute (Headphone)** | Mutes headphone. | (none) |
| **Front Speaker: / Mute** | Mutes front speaker (model-specific). | (none) |
| **Audio Compression (SmartLink):** | Selects audio codec for SmartLink/LAN (Auto/Uncompressed/Opus). | `AudioCompression` |
| **Prevent system sleep while connected** | Keeps OS awake while radio is connected. | `InhibitSleepWhileConnected` |
| **PC Audio Devices: Input: / Output:** | Picks host audio in/out devices. | (none) |
| **Audio Boost:** | Enables extra gain on the client audio path. | `AudioBoost` |
| **Audio Buffer:** | Increases audio buffer in milliseconds for VPN/SmartLink jitter (50-1000 ms). Default 200. | `AudioBufferMs` |
| **Recording: Radio Side / Client Side** | Picks radio-side or client-side recording. | `RecordingMode` |
| **Save to:** | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. | `QsoRecordingDir` |
| **...** | Browses for recording folder. | (none) |
| **Auto-record on
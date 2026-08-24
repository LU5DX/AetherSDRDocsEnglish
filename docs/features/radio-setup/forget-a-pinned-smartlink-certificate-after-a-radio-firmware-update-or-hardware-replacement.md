# Radio Setup Dialog Reference

The **Radio Setup** dialog is the master per-radio configuration window. It contains tabs for radio information, network settings, GPS, TX, Phone/CW, RX, calibration, audio, filters, transverters, USB cables, peripherals, APD, themes, SmartLink certificate management, and serial port configuration.

## Opening the dialog

1. Click **Settings > Radio Setup...** in the main menu.
2. The dialog opens with the **Radio** tab selected.

Many read-only values (serial number, HW version, options, model, subscription details, IP address, MAC address, firmware version) include a clipboard copy button next to the label. Click this button to copy the value to your clipboard for sharing with support.

## Radio tab

The **Radio** tab displays radio identification, license information, and firmware update controls.

| Control                                     | Type                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                      |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Radio SN                                    | Indicator                                                                                                                                                                | Chassis serial number (read-only). Includes clipboard copy button.                                                                                                                                                                                                               |
| Region                                      | Indicator                                                                                                                                                                | Radio regulatory region. Default: USA.                                                                                                                                                                                                                                           |
| HW Version                                  | Indicator                                                                                                                                                                | Hardware version string. Includes clipboard copy button.                                                                                                                                                                                                                         |
| Remote On                                   | Push button                                                                                                                                                              | Enables remote wake / remote-on.                                                                                                                                                                                                                                                 |
| Options                                     | Indicator                                                                                                                                                                | Licensed radio options. Includes clipboard copy button.                                                                                                                                                                                                                          |
| FlexControl                                 | Indicator                                                                                                                                                                | Detected state of FlexControl hardware.                                                                                                                                                                                                                                          |
| multiFLEX                                   | Indicator                                                                                                                                                                | multiFLEX enabled state.                                                                                                                                                                                                                                                         |
| Model                                       | Indicator                                                                                                                                                                | Radio model. Includes clipboard copy button.                                                                                                                                                                                                                                     |
| Nickname                                    | Text field                                                                                                                                                               | User-friendly radio nickname.                                                                                                                                                                                                                                                    |
| Callsign                                    | Text field                                                                                                                                                               | Station callsign.                                                                                                                                                                                                                                                                |
| Station Name                                | Text field                                                                                                                                                               | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as 'client station <name>'.                                                                                            |
| License Info                                | Indicator                                                                                                                                                                | Displays license details including Subscription, Expiration, Radio ID, and Licensed version. Each field includes a clipboard copy button.                                                                                                                                        |
| Check for Update                            | Push button                                                                                                                                                              | Queries for firmware updates.                                                                                                                                                                                                                                                    |
| Select Installer...                         | Push button                                                                                                                                                              | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. Label changed from 'Browse .ssdr...' in v26.5.3.                                     |
| Upload Firmware                             | Push button                                                                                                                                                              | Starts firmware upload with progress bar and status.                                                                                                                                                                                                                             |
| Reboot Radio                                | Push button                                                                                                                                                              | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes. New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot. |
| Agent Automation (MCP):                     | Toggle button                                                                                                                                                            | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                               | Text field                                                                                                                                                              | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store. New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                   |
| Copy (Access Token)                         | Push button                                                                                                                                                              | Copies the access token to the clipboard. New in v26.8.4.                                                                                                                                                                                                                                                                                      |
| Rotate (Access Token)                       | Push button                                                                                                                                                              | Generates a new token and applies it immediately, locking out any client still using the old one. New in v26.8.4.                                                                                                                                                                                                                              |
| Allow TX via MCP: Enable transmit control   | Checkbox                                                                                                                                                                | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| Observe only: Read-only (block all driving) | Checkbox                                                                                                                                                                | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                       |
| VITA-49 RX buffer:                          | Slider                                                                                                                                                                   | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted. |
| granted: (VITA-49 RX buffer)                | Indicator                                                                                                                                                               | Shows the buffer size the kernel actually granted (vs the requested preset). New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                         |

## Network tab

The **Network** tab displays radio network information and advanced network options.

| Control | Type | Description |
|---------|------|-------------|
| IP Address / Mask / MAC Address | Indicator | Read-only network addresses. Each includes a clipboard copy button. |
| Enforce Private IP Connections: | Toggle button | Rejects non-RFC1918 peers. |
| Network MTU: | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default: 1450. Valid range: 576-9000 bytes. Stored in AppSettings as `NetworkMtu`. Default 1450 is safe for most VPN/SD-WAN tunnels. |
| DHCP / Static | Toggle button | Switches between DHCP and Static IP modes. |
| IP Address: / Mask: / Gateway: | Text field | Static IP configuration fields. |
| Apply | Push button | Pushes the network config to the radio. |

## GPS tab

The **GPS** tab displays GPS presence and live lat/lon/alt/time/satellites information.

## TX tab

The **TX** tab configures TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and provides a shortcut to TX Band Settings.

| Control | Type | Description |
|---------|------|-------------|
| TX Band Settings | Push button | Opens the dedicated per-band power/tune dialog. |
| Timings (in ms) | Spinbox | TX hang / delay timings. |
| Interlocks - TX REQ: RCA / Accessory | Toggle button | Enables RCA and accessory interlock inputs. |
| Max Power: | Spinbox | Sets radio-level TX power cap. Valid range: 0-100%. |
| Tune Mode: | Combo box | Selects how the tune button behaves. |
| Show TX in Waterfall: | Toggle button | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | Default: False. TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. Stored as `TxFollowsActiveSlice`. |
| Active Slice Follows TX | Push button | Default: False. Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. Stored as `ActiveFollowsTxSlice`. |

## Phone/CW tab

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

| Control | Type | Description |
|---------|------|-------------|
| Enable/Disable the Level Meter During Receive | Toggle button | Shows mic level meter even in RX. |
| Iambic: | Toggle button | Enables or disables the iambic keyer on the radio. In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. These also drive the new local software iambic keyer (IambicKeyer) which mirrors the radio's iambic state for sub-5 ms sidetone. |
| Iambic Mode: A / B | Push button | Default: A. Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair added in v0.9.1. |
| Swap: | Toggle button | Swaps dit/dah. |
| Sideband: | Combo box | Selects CW pitch sideband. Options: LSB, USB. |
| CWX: | Toggle button | Enables CWX macro keying. |
| Decode: RX | Toggle button | Default: True. Enables the CW decode overlay on the panadapter for received CW. Stored as nested JSON under `CwDecoder` (rx field). New in v26.5.3: split from single CwDecodeOverlay toggle into independent RX/TX toggles. Legacy `CwDecodeOverlay` key auto-migrated on first read. |
| Decode: TX | Toggle button | Default: False. Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Stored as nested JSON under `CwDecoder` (tx field). New in v26.5.3 (#2417). |
| RTTY Mark Default: | Spinbox | Default RTTY mark frequency. |

## RX tab

The **RX** tab configures GPSDO frequency offset calibration and 10 MHz reference source.

| Control | Type | Description |
|---------|------|-------------|
| Cal Frequency (MHz): | Spinbox | Frequency used for manual calibration. |
| Start | Push button | Starts the frequency calibration sweep. |
| Freq Offset (ppb): | Spinbox | Manual frequency offset in ppb. |
| 10 MHz Reference Source: | Combo box | Selects oscillator reference source. Default: Auto. Options depend on hardware installed: Auto, TCXO, GPSDO, External. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

## Calibration tab

The **Calibration** tab provides manual host-side frequency calibration for radios that cannot calibrate their own oscillator (e.g. HL2). This tab is hidden for radios that support hardware calibration (such as Flex radios, which calibrate on the RX tab). New in v26.8.4.

| Control | Type | Description |
|---------|------|-------------|
| Calibration controls | Various | Manual frequency calibration in ppb/ppm for radios without self-calibration capability. The tab is capability-gated: it only appears when the connected radio reports `hostFrequencyCalibration` support. |

## Audio tab

The **Audio** tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

| Control | Type | Description |
|---------|------|-------------|
| Line Out: | Slider | Line-out gain. |
| Mute (Line Out) | Push button | Mutes line-out. |
| Headphone: | Slider | Headphone gain. |
| Mute (Headphone) | Push button | Mutes headphone. |
| Front Speaker: / Mute | Push button | Mutes front speaker (model-specific). |
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Push button | Default: Auto. Selects audio codec for SmartLink/LAN. Stored as `AudioCompression`. |
| Prevent system sleep while connected | Checkbox | Default: False. Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. |
| PC Audio Devices: Input: / Output: | Combo box | Picks host audio in/out devices. |
| Audio Boost: | Toggle button | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| Audio Buffer: | Text field | Default: 200. Increases audio buffer in milliseconds for VPN/SmartLink jitter. Valid range: 50-1000 ms. Stored as `AudioBufferMs`. Applied to AudioEngine::setRxBufferCapMs(). |
| Recording: Radio Side / Client Side | Push button | Default: Radio Side. Picks radio-side or client-side recording. Stored as `RecordingMode`. |
| Save to: | Text
# Radio Setup

This page covers the **Radio Setup** dialog, the master per-radio configuration window. It includes radio information, network settings, GPS, TX, Phone/CW, RX, audio, filters, transverters, USB cables, peripheral connections, and pinned SmartLink certificate management. Many read-only values include a clipboard copy button for easy sharing with support.

## Before you start

- Your radio must be connected to AetherSDR unless noted otherwise.

## Opening Radio Setup

1. Click `Settings > Radio Setup...`.
2. The dialog opens with a left-hand navigation list of tabs and a right-hand configuration panel.

## Copying values to the clipboard

Several read-only values (serial number, hardware version, model, options, IP address, MAC address, license fields) include a clipboard copy button (tray icon) immediately to the right of the value. Click it to copy the value to your system clipboard and paste it into a support ticket or email.

### Copy the radio serial number

1. Open `Settings > Radio Setup...`.
2. On the **Radio** tab, locate the **Radio SN** read-only label.
3. Click the clipboard copy button (tray icon) immediately to the right of the serial number value.

### Copy the radio IP address or MAC address

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **IP Address** or **MAC Address** read-only label.
4. Click the clipboard copy button (tray icon) immediately to the right of the value.

### Copy firmware version or license info

1. Open `Settings > Radio Setup...`.
2. On the **Radio** tab, scroll to the **License Info** section.
3. Click the clipboard copy button next to any field: **Subscription**, **Expiration**, **Radio ID**, or **Licensed version**.

You can also copy **HW Version**, **Model**, or **Options** from the **Radio** tab the same way.

## Tabs

### Radio

The **Radio** tab shows radio identification, license info, and firmware update controls.

| Control | Behavior | Notes |
|---------|----------|-------|
| Radio SN | Chassis serial number (read-only). | Includes a clipboard copy button (tray icon) next to the value. |
| Region | Radio regulatory region. | |
| HW Version | Hardware version string. | Includes a clipboard copy button next to the value. |
| Remote On | Enables remote wake / remote-on. | |
| Options | Shows licensed radio options. | Includes a clipboard copy button next to the value. |
| FlexControl | Detected state of FlexControl hardware. | |
| multiFLEX | multiFLEX enabled state. | |
| Reboot Radio | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes. | Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot. |
| Model | Radio model. | Includes a clipboard copy button next to the value. |
| Nickname | User-friendly radio nickname. | |
| Callsign | Station callsign. | |
| Station Name | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. | Stored in AppSettings. Sent to radio as 'client station `<name>`'. |
| License Info (Subscription / Expiration / Radio ID / Licensed version) | Displays license details from the radio. | Each field includes a clipboard copy button next to the value. |
| Check for Update | Queries for firmware updates. | |
| Select Installer... | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. | Label changed from 'Browse .ssdr...' in a prior release. |
| Upload Firmware | Starts firmware upload with progress bar and status. | |

### Network

The **Network** tab shows radio network information and advanced network options.

| Control | Behavior | Notes |
|---------|----------|-------|
| IP Address / Mask / MAC Address | Read-only network addresses. | Each includes a clipboard copy button. |
| Enforce Private IP Connections: | Rejects non-RFC1918 peers. | |
| Agent Automation (MCP): | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. | Persisted via AutomationBridgeSettings. The `AETHER_AUTOMATION` launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless `AETHER_AUTOMATION_ALLOW_TX` is set. |
| Access Token: | Read-only display of the MCP access token; paste it into the assistant's `AETHER_MCP_TOKEN` environment variable. Stored in the OS secret store. | Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| Copy (Access Token) | Copies the access token to the clipboard. | |
| Rotate (Access Token) | Generates a new token and applies it immediately, locking out any client still using the old one. | |
| Allow TX via MCP: Enable transmit control | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. | Enforced in the bridge; no client can flip it. Overridden by `AETHER_AUTOMATION_ALLOW_TX` (force on) and `AETHER_AUTOMATION_NO_TX` (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. | Enforced in the app, so a client cannot bypass it. `AETHER_AUTOMATION_READONLY` launch variable pins it on for headless/CI runs. |
| VITA-49 RX buffer: | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. | Presets 256 KB to 4 MB. The system caps the grant at `net.core.rmem_max`; a live 'granted: \<size\>' label shows what the kernel actually granted. |
| granted: (VITA-49 RX buffer) | Shows the buffer size the kernel actually granted (vs the requested preset). | Shows '(applies on connect)' when no connection is active. |
| Network MTU: | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450. Range 576-9000 bytes. | Stored in AppSettings. |
| DHCP / Static | Switches between DHCP and Static IP modes. | |
| IP Address: / Mask: / Gateway: | Static IP configuration fields. | |
| Apply | Pushes the network config to the radio. | |

### GPS

The **GPS** tab shows GPS presence and live lat/lon/alt/time/satellites info.

### TX

The **TX** tab configures TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and provides a TX Band Settings shortcut.

| Control | Behavior | Notes |
|---------|----------|-------|
| TX Band Settings | Opens the dedicated per-band power/tune dialog. | |
| Timings (in ms) | TX hang / delay timings. | |
| Interlocks - TX REQ: RCA / Accessory | Enables RCA and accessory interlock inputs. | |
| Max Power: | Sets radio-level TX power cap. Range 0-100 %. | |
| Tune Mode: | Selects how the tune button behaves. | |
| Show TX in Waterfall: | Draws TX signal in the waterfall. | |
| TX Follows Active Slice | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Default False. | Disabled automatically during Split operation. |
| Active Slice Follows TX | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. Default False. | |

### Phone/CW

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

| Control | Behavior | Notes |
|---------|----------|-------|
| Enable/Disable the Level Meter During Receive | Shows mic level meter even in RX. | |
| Iambic: | Enables or disables the iambic keyer on the radio. | Mode A and Mode B buttons were added beside the Enabled toggle. |
| Iambic Mode: A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Default A. | Mutually exclusive pair. |
| Swap: | Swaps dit/dah. | |
| Sideband: | Selects CW pitch sideband. Options: LSB, USB. | |
| CWX: | Enables CWX macro keying. | |
| Decode: RX | Enables the CW decode overlay on the panadapter for received CW. Default True. | Persisted as nested JSON blob under `CwDecoder` with `rx` and `tx` fields. Legacy `CwDecodeOverlay` key auto-migrated on first read. |
| Decode: TX | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Default False. | |
| RTTY Mark Default: | Default RTTY mark frequency. | |

### RX

The **RX** tab handles GPSDO frequency offset calibration and 10 MHz reference source.

| Control | Behavior | Notes |
|---------|----------|-------|
| Cal Frequency (MHz): | Frequency used for manual calibration. | |
| Start | Starts the frequency calibration sweep. | |
| Freq Offset (ppb): | Manual frequency offset in ppb. | |
| 10 MHz Reference Source: | Selects oscillator reference source. Options: Auto, TCXO, GPSDO, External. Default Auto. | Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

### Calibration

The **Calibration** tab is available only on radios whose backend requires host-side frequency calibration (currently only HL2 and similar RX-only backends). On FLEX radios, this tab is hidden because the radio performs its own hardware calibration on the **RX** tab.

When connected to a supported radio, the tab provides:

| Control | Behavior | Notes |
|---------|----------|-------|
| (Host frequency calibration controls) | Manually corrects the radio's local oscillator frequency in ppb/ppm. | Tab is hidden unless the connected backend reports `hostFrequencyCalibration` capability. Typing "calibration" in the dialog search box will not surface the tab on a FLEX radio. |

### Antennas

The **Antennas** tab lets you assign custom display names to each antenna port (ANT1, ANT2, XVTA, XVTB, etc.). These names appear in the panadapter RX/TX antenna indicators instead of the raw port tokens.

| Control | Behavior | Notes |
|---------|----------|-------|
| Port / Custom name / Preview / Clear (table columns) | Grid of antenna port rows. Each row has a read-only port label (e.g. ANT1), an editable text field (max 16 chars), a preview of the final display name, and a Clear button to reset the custom name. | Rows auto-update when slice antenna assignments change. When a port's custom name is empty, the raw port token is used as the display name. |

### Audio

The **Audio** tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and the NVIDIA BNR container.

| Control | Behavior | Notes |
|---------|----------|-------|
| Line Out: | Line-out gain. | |
| Mute (Line Out) | Mutes line-out. | |
| Headphone: | Headphone gain. | |
| Mute (Headphone) | Mutes headphone. | |
| Front Speaker: / Mute | Mutes front speaker (model-specific). | |
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Selects audio codec for SmartLink/LAN. Default Auto. | |
| Prevent system sleep while connected | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Default False. | |
| PC Audio Devices: Input: / Output: | Picks host audio in/out devices. | |
| Audio Boost: | Enables extra gain on the client audio path. | |
| Audio Buffer: | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Default 200. Range 50-1000 ms. | Stored as `AudioBufferMs`. |
| Recording: Radio Side / Client Side | Picks radio-side or client-side recording. Default Radio Side. | |
| Save to: | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. | |
| ... | Browses for recording folder. | |
| Auto-record on TX | Automatically records while transmitting. Default False. | |
| Idle timeout: | Seconds of silence before recording stops. Default 120. Range 10-3600 sec. | |
| NVIDIA BNR: Autostart Container / Start / Stop / Check Status | Controls the NVIDIA Broadcast noise-
# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It provides tabs for radio information, network, GPS, TX, Phone/CW, RX, audio, filters, XVTR, USB cables, peripherals, APD, themes, serial (FlexControl), antenna names, SmartLink pinned certificate management, and KiwiSDR public receiver access.

## Before you start

- AetherSDR must be connected to the radio to access most tabs.
- Open `Settings > Radio Setup...`.

## Radio tab

The Radio tab displays radio identification, license information, and firmware update controls.

| Control | Default | Behavior |
|---------|----------|----------|
| Radio SN | Chassis serial number (read-only). | Includes a clipboard copy button (tray icon) next to the value. New in v26.5.3 (#2976). |
| Region | USA | Radio regulatory region. |
| HW Version | Hardware version string. | Includes a clipboard copy button next to the value (#2976). |
| Remote On | — | Enables remote wake / remote-on. |
| Options | Shows licensed radio options. | Includes a clipboard copy button next to the value (#2976). |
| FlexControl | — | Detected state of FlexControl hardware. |
| multiFLEX | — | multiFLEX enabled state. |
| Model | Radio model. | Includes a clipboard copy button next to the value (#2976). |
| Nickname | — | User-friendly radio nickname. |
| Callsign | — | Station callsign. |
| Station Name | — | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored as `StationName`. |
| License Info | — | Displays license details from the radio (Subscription / Expiration / Radio ID / Licensed version). Click the copy button to copy to clipboard. |
| Check for Update | — | Queries for firmware updates. |
| Select Installer... | — | Chooses a firmware image file (`.msi`, `.exe`, or `.ssdr`). |
| Upload Firmware | — | Starts firmware upload with progress bar and status. |
| Reboot Radio | — | Prompts for confirmation, then reboots the connected radio. AetherSDR disconnects during reboot. Automatically reconnects on LAN; SmartLink/WAN requires manual reconnect. Button is disabled when radio is not connected or when the backend does not support client reboot (e.g. HL2 is RX-only). New in v26.8.4 (#4448). |
| Agent Automation (MCP): | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token: | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store. | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| Copy (Access Token) | Copies the access token to the clipboard. | New in v26.8.4. |
| Rotate (Access Token) | Generates a new token and applies it immediately, locking out any client still using the old one. | New in v26.8.4. |
| Allow TX via MCP: Enable transmit control | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs. |
| VITA-49 RX buffer: | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted. |
| granted: (VITA-49 RX buffer) | Shows the buffer size the kernel actually granted (vs the requested preset). | New in v26.8.4. Shows '(applies on connect)' when no connection is active. |

### Copy value buttons

Each read-only indicator (Radio SN, HW Version, License Info, etc.) now shows a small overlay copy button when hovered or focused. Clicking the button copies the displayed value to the system clipboard. A brief "copied" popup appears near the button after a successful copy.

### Firmware upload status

The firmware upload area shows a progress bar and status text during an active upload. When no upload is in progress, the status area is empty.

### Reboot Radio

Click **Reboot Radio** to restart the connected radio. A confirmation dialog appears before the reboot proceeds. AetherSDR disconnects during the reboot:

- **LAN connection:** AetherSDR automatically reconnects once the radio finishes booting.
- **SmartLink/WAN connection:** You must reconnect manually after the radio boots.

The button is enabled only when the radio is connected and the backend supports a client-initiated reboot. For example, the button is disabled on HL2 radios because they are receive-only. The button updates automatically when the connection state changes, so you do not need to reopen the dialog.

## Network tab

The Network tab displays radio network information and advanced network options.

| Control | Default | Behavior |
|---------|---------|----------|
| IP Address / Mask / MAC Address | — | Read-only network addresses. Each includes a clipboard copy button. |
| Enforce Private IP Connections | — | Rejects non-RFC1918 peers. |
| Agent Automation (MCP) | Disabled | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token | (none) | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store. New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| Copy (Access Token) | — | Copies the access token to the clipboard. New in v26.8.4. |
| Rotate (Access Token) | — | Generates a new token and applies it immediately, locking out any client still using the old one. New in v26.8.4. |
| Allow TX via MCP: Enable transmit control | False | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| Observe only: Read-only (block all driving) | False | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs. |
| VITA-49 RX buffer | 4 MB | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted. |
| granted: (VITA-49 RX buffer) | — | Shows the buffer size the kernel actually granted (vs the requested preset). New in v26.8.4. Shows '(applies on connect)' when no connection is active. |
| Network MTU | 1450 | Sets maximum outgoing VITA-49 UDP packet size in bytes (576–9000). Stored as `NetworkMtu`. Default 1450 is safe for most VPN/SD-WAN tunnels. |
| DHCP / Static | — | Switches between DHCP and Static IP modes. |
| IP Address / Mask / Gateway | — | Static IP configuration fields. |
| Apply | — | Pushes the network config to the radio. |

## GPS tab

The GPS tab shows GPS presence and live latitude/longitude/altitude/time/satellites information.

## TX tab

The TX tab configures TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX band settings.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| TX Band Settings | — | — | Opens the dedicated per-band power/tune dialog. |
| ACC TX | — | — | TX hang delay in milliseconds. |
| TX Delay | — | — | TX delay in milliseconds. |
| RCA TX1 | — | — | RCA TX1 delay in milliseconds. |
| Timeout (sec) | — | — | Interlock timeout displayed in seconds. The radio stores this value in milliseconds. |
| RCA TX2 | — | — | RCA TX2 delay in milliseconds. |
| Interlocks - TX REQ: RCA / Accessory | — | — | Enables RCA and accessory interlock inputs. |
| Max Power | — | 0–100 % | Sets radio-level TX power cap. |
| Tune Mode | — | — | Selects how the tune button behaves. |
| Show TX in Waterfall | — | — | Draws TX signal in the waterfall. |
| TX Follows Active Slice | False | — | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. |
| Active Slice Follows TX | False | — | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. |

### Timing fields

The timing fields on the TX tab accept values in milliseconds except for Timeout (sec) which displays and accepts values in seconds for readability. The radio stores the timeout value internally in milliseconds.

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| Enable/Disable the Level Meter During Receive | — | — | Shows mic level meter even in RX. |
| Iambic | — | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| Iambic Mode: A / B | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. |
| Swap | — | — | Swaps dit/dah. |
| Sideband | — | LSB / USB | Selects CW pitch sideband. |
| CWX | — | — | Enables CWX macro keying. |
| Decode: RX | True | — | Enables the CW decode overlay on the panadapter for received CW. Persisted as nested JSON blob under `CwDecoder` with rx and tx fields. Legacy `CwDecodeOverlay` key auto-migrated on first read. |
| Decode: TX | False | — | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. New in v26.5.3 (#2417). |
| RTTY Mark Default | — | — | Default RTTY mark frequency. |

## RX tab

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| Cal Frequency (MHz) | — | — | Frequency used for manual calibration. Available regardless of whether a GPSDO is installed. If the field is empty when you click **Start**, a warning appears and calibration does not begin. |
| Start | — | —
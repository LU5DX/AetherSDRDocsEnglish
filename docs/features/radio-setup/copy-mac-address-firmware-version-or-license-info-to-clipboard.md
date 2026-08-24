# Radio Setup

The **Radio Setup** dialog is the master per-radio configuration window. It provides access to radio information, network settings, GPS, TX/Phone/CW/RX configuration, audio, filters, transverters, USB cables, peripherals, and SmartLink pinned certificate management.

Open it from the menu: `Settings > Radio Setup...`.

## Before you start

- AetherSDR must be running.
- To modify radio-level settings, connect to the radio first.
- The dialog is a persistent singleton: closing it keeps your changes; reopening it shows the current state.

## What each section/tab does

### Radio (tab)

Radio information, identification, license info and firmware update.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **Radio SN** | — | Chassis serial number (read-only). | Includes a clipboard copy button next to the value. |
| **Region** | USA | Radio regulatory region. | Read-only. |
| **HW Version** | — | Hardware version string. | Includes a clipboard copy button next to the value. |
| **Remote On** | — | Enables remote wake / remote-on. | Push button. |
| **Options** | — | Shows licensed radio options. | Includes a clipboard copy button next to the value. |
| **FlexControl** | — | Detected state of FlexControl hardware. | Indicator. |
| **multiFLEX** | — | multiFLEX enabled state. | Indicator. |
| **Reboot Radio** | — | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes. | New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot. |
| **Model** | — | Radio model. | Includes a clipboard copy button next to the value. |
| **Nickname** | — | User-friendly radio nickname. | Text field. |
| **Callsign** | — | Station callsign. | Text field. |
| **Station Name** | — | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. | Stored in AppSettings (`StationName`). Sent to radio as 'client station <name>'. |
| **License Info** (Subscription / Expiration / Radio ID / Licensed version) | — | Displays license details from the radio. | Each field (Subscription, Expiration, Radio ID, Licensed version) includes a clipboard copy button next to the value. |
| **Check for Update** | — | Queries for firmware updates. | Push button. |
| **Select Installer...** | — | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. | Label changed from 'Browse .ssdr...' to 'Select Installer...' in v26.5.3. |
| **Upload Firmware** | — | Starts firmware upload with progress bar and status. | Push button. |

### Network (tab)

Radio network information and advanced network options.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **IP Address / Mask / MAC Address** | — | Read-only network addresses. | Each includes a clipboard copy button. |
| **Enforce Private IP Connections:** | — | Rejects non-RFC1918 peers. | Toggle button. |
| **Agent Automation (MCP):** | Disabled | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The `AETHER_AUTOMATION` launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless `AETHER_AUTOMATION_ALLOW_TX` is set. |
| **Access Token:** | (none) | Read-only display of the MCP access token; paste it into the assistant's `AETHER_MCP_TOKEN` environment variable. Stored in the OS secret store. | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| **Copy (Access Token)** | — | Copies the access token to the clipboard. | New in v26.8.4. |
| **Rotate (Access Token)** | — | Generates a new token and applies it immediately, locking out any client still using the old one. | New in v26.8.4. |
| **Allow TX via MCP: Enable transmit control** | False | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by `AETHER_AUTOMATION_ALLOW_TX` (force on) and `AETHER_AUTOMATION_NO_TX` (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| **Observe only: Read-only (block all driving)** | False | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. `AETHER_AUTOMATION_READONLY` launch variable pins it on for headless/CI runs. |
| **VITA-49 RX buffer:** | 4 MB | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at `net.core.rmem_max`; a live 'granted: <size>' label shows what the kernel actually granted. |
| **granted: (VITA-49 RX buffer)** | — | Shows the buffer size the kernel actually granted (vs the requested preset). | New in v26.8.4. Shows '(applies on connect)' when no connection is active. |
| **Network MTU:** | 1450 | Sets maximum outgoing VITA-49 UDP packet size in bytes (576-9000). | Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings (`NetworkMtu`). |
| **DHCP / Static** | — | Switches between DHCP and Static IP modes. | Toggle button. |
| **IP Address: / Mask: / Gateway:** | — | Static IP configuration fields. | Text fields. |
| **Apply** | — | Pushes the network config to the radio. | Push button. |

### GPS (tab)

GPS presence and live lat/lon/alt/time/satellites info.

### TX (tab)

TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow and TX Band Settings shortcut.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **TX Band Settings** | — | Opens the dedicated per-band power/tune dialog. | Push button. |
| **Timings (in ms)** | — | TX hang / delay timings. | Spinbox. |
| **Interlocks - TX REQ: RCA / Accessory** | — | Enables RCA and accessory interlock inputs. | Toggle button. |
| **Max Power:** | — | Sets radio-level TX power cap (0-100 %). | Spinbox. |
| **Tune Mode:** | — | Selects how the tune button behaves. | Combo box. |
| **Show TX in Waterfall:** | — | Draws TX signal in the waterfall. | Toggle button. |
| **TX Follows Active Slice** | False | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. | Disabled automatically during Split operation. Stored in AppSettings (`TxFollowsActiveSlice`). |
| **Active Slice Follows TX** | False | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. | Stored in AppSettings (`ActiveFollowsTxSlice`). |

### Phone/CW (tab)

Microphone, CW keyer, RTTY defaults.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **Enable/Disable the Level Meter During Receive** | — | Shows mic level meter even in RX. | Toggle button. |
| **Iambic:** | Enabled | Enables or disables the iambic keyer on the radio. | Toggle button. In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. These also drive the local software iambic keyer (IambicKeyer) which mirrors the radio's iambic state for sub-5 ms sidetone. |
| **Iambic Mode: A / B** | A | Selects Curtis iambic mode A or B for both the radio and the local software keyer. | Mutually exclusive pair added in v0.9.1. Push buttons. |
| **Swap:** | — | Swaps dit/dah. | Toggle button. |
| **Sideband:** | LSB/USB | Selects CW pitch sideband. | Combo box. |
| **CWX:** | — | Enables CWX macro keying. | Toggle button. |
| **Decode: RX** | True | Enables the CW decode overlay on the panadapter for received CW. | New in v26.5.3: split from single CwDecodeOverlay toggle into independent RX/TX toggles. Persisted as nested JSON blob under `CwDecoder` with `rx` and `tx` fields. Legacy `CwDecodeOverlay` key auto-migrated on first read. |
| **Decode: TX** | False | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. | New in v26.5.3 (#2417). |
| **RTTY Mark Default:** | — | Default RTTY mark frequency. | Spinbox. |

### RX (tab)

GPSDO frequency offset calibration and 10 MHz reference source.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **Cal Frequency (MHz):** | — | Frequency used for manual calibration. | Spinbox. |
| **Start** | — | Starts the frequency calibration sweep. | Push button. |
| **Freq Offset (ppb):** | — | Manual frequency offset in ppb. | Spinbox. |
| **10 MHz Reference Source:** | Auto | Selects oscillator reference source (Auto / TCXO / GPSDO / External). Options shown depend on hardware installed. | Lock status (Locked / Unlocked) shown alongside and updates live. |

### Calibration (tab)

Frequency calibration for radios that cannot self-calibrate (e.g. HL2). Shown only when the connected backend supports host-side frequency calibration.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **Calibration (tab)** | — | Manual frequency calibration with measurement sweep. | New in v26.8.4. Hidden unless the backend advertises `hostFrequencyCalibration` capability (a Flex radio uses its own hardware calibration on the RX page). Re-reads the stored calibration whenever the dialog is opened or the connected radio changes, so a later trim command cannot commit a previous radio's number. |

### Antennas (tab)

Per-port antenna display-name editor for the radio. Lets the operator assign custom names to each antenna port (ANT1, ANT2, XVTA, XVTB, etc.) which are shown in the panadapter RX/TX antenna indicators instead of the raw port tokens.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **Port / Custom name / Preview / Clear** | — | Grid of antenna port rows. Each row has a read-only port label (e.g. ANT1), an editable text field (max 16 chars), a preview of the final display name, and a Clear button to reset the custom name. | Rows auto-update when slice antenna assignments change. Ports are fetched from RadioModel::knownAntennaTokens(). Lazy-built when first clicked. When a port's custom name is empty, the raw port token is used as the display name. |

### Audio (tab)

Radio audio outputs, compression, PC devices, boost, buffer, recording and NVIDIA BNR container.

| Control | Default | Behavior | Notes |
|---|---|---|---|
| **Line Out:** | — | Line-out gain. | Slider. |
| **Mute (Line Out)** | — | Mutes line-out. | Push button. |
| **Headphone:** | — | Headphone gain. | Slider. |
| **Mute (Headphone)** | — | Mutes headphone. | Push button. |
| **Front Speaker: / Mute** | — | Mutes front speaker (model-specific). | Push button. |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Auto | Selects audio codec for SmartLink/LAN. | Stored in AppSettings (`AudioCompression`). |
| **Prevent system sleep while connected
# Radio Setup Dialog

The Radio Setup dialog is the master configuration window for per-radio settings including radio information, network, GPS, TX, Phone/CW, RX, calibration, audio, filters, antennas, transverters, USB cables, peripherals, APD, themes, serial port, SmartLink pinned certificate management, and KiwiSDR receiver integration.

## Opening the dialog

- Click `Settings > Radio Setup...` while connected to a radio.

## Dialog layout

The dialog contains a tabbed interface with the following tabs:

- **Radio** - Radio information, identification, license info, firmware update, and radio reboot
- **Network** - Network information and advanced network options
- **GPS** - GPS presence and live lat/lon/alt/time/satellites info
- **TX** - TX timings, interlocks, max power, tune mode, and slice/TX follow settings
- **Phone/CW** - Microphone, CW keyer, RTTY defaults
- **RX** - GPSDO frequency offset calibration and 10 MHz reference source
- **Calibration** - Manual frequency calibration for radios that cannot calibrate themselves (HL2 only)
- **Antennas** - Antenna name configuration
- **Filters** - Low-latency / Sharp filter options per bandwidth
- **XVTR** - Per-transverter configuration
- **USB Cables** - USB serial adapter assignment
- **Peripherals** - External device manual IP connection (TGXL, PGXL, Antenna Genius)
- **APD** - External Adaptive Pre-Distortion sample port selection (FLEX-8x00 only)
- **Themes** - UI appearance settings including per-slice color overrides
- **SmartLink** - Pinned TLS certificate management
- **Serial** - FlexControl serial port configuration
- **KiwiSDR** - KiwiSDR public receiver configuration and connection

The dialog remembers its size and position between sessions using `RadioSetupDialogGeometry` in AppSettings.

Tabs whose content may exceed the dialog's visible height (Radio, Themes, Audio, Filters, Peripherals on small or high-DPI displays) are wrapped in a scroll area so the dialog does not grow past the screen edge. The scrollbar appears only when needed; on wide screens there is no visual change.

The dialog is a persistent singleton: it is built once and shown/raised on demand. Pages are built lazily when first selected, and any stored calibration values are re-read whenever the dialog is shown or the connection state changes.

## Radio tab

The Radio tab displays radio identification and license information, provides firmware update controls, and includes a Reboot Radio button. Each read-only value has a copy button (clipboard icon) that appears on hover or focus — click to copy the value.

### Radio information

| Control                                     | Kind                                                                                                                                                                     | Behavior                                                                                                                                                                                                                                                                         |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Radio SN**                                | Indicator                                                                                                                                                                | Chassis serial number (read-only). If chassis serial is empty, falls back to radio serial number. Displays "—" if unavailable. Includes a clipboard copy button (tray icon) next to the value.                                                                                   |
| **Region**                                  | Indicator                                                                                                                                                                | Radio regulatory region. Default: USA.                                                                                                                                                                                                                                           |
| **HW Version**                              | Indicator                                                                                                                                                                | Hardware version string. Prefixed with "v" if not already present. Displays "—" if unavailable. Includes a clipboard copy button next to the value.                                                                                                                              |
| **Model**                                   | Indicator                                                                                                                                                                | Radio model. Includes a clipboard copy button next to the value.                                                                                                                                                                                                                 |
| **Options**                                 | Indicator                                                                                                                                                                | Shows licensed radio options. If empty, shows a guess based on amplifier presence ("GPS, PGXL" or "GPS"). Displays "—" if unavailable. Includes a clipboard copy button next to the value.                                                                                       |
| **FlexControl**                             | Indicator                                                                                                                                                                | Detected state of FlexControl hardware.                                                                                                                                                                                                                                          |
| **multiFLEX**                               | Indicator                                                                                                                                                                | multiFLEX enabled state.                                                                                                                                                                                                                                                         |
| **License Info**                            | Indicator                                                                                                                                                                | Displays subscription, expiration, radio ID, and licensed version from the radio. Each field includes a clipboard copy button next to the value.                                                                                                                                 |
| Reboot Radio                                | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes.                                        | New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot.                                                            |
| Agent Automation (MCP):                     | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.      | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                               | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                           | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                         | Copies the access token to the clipboard.                                                                                                                                | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                       | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                        | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control   | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                              | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                          | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                          | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                             | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |
### Radio identification

| Control | Kind | Behavior |
|---|---|---|
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as `client station <name>`. |

### Remote On

| Control | Kind | Behavior |
|---|---|---|
| **Remote On** | Push button | Enables remote wake / remote-on. |

### Reboot Radio

| Control | Kind | Behavior |
|---|---|---|
| **Reboot Radio** | Push button | Reboots the connected radio. A confirmation dialog appears before rebooting. On LAN connections, AetherSDR automatically reconnects once the radio finishes booting. On SmartLink/WAN connections, you must reconnect manually after the radio boots. The dialog closes after reboot. The button is disabled when the radio is disconnected. |

### Firmware update

| Control | Kind | Behavior |
|---|---|---|
| **Check for Update** | Push button | Queries for firmware updates from the radio. |
| **Select Installer...** | Push button | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes and extracts the `.ssdr` without external tools. |
| **Upload Firmware** | Push button | Starts firmware upload with progress bar and status. |
| Firmware status | Indicator | Empty until a firmware upload begins, then progress and result text. |

#### Firmware update workflow

When **Check for Update** finds a newer version, the status area instructs you to download the SmartSDR installer from flexradio.com yourself. Use **Select Installer...** to point AetherSDR at the file you downloaded.

**Supported installer formats**

| File type | Description |
|---|---|
| `.msi` | FlexRadio WiX installer (SmartSDR v4.2 and later). Recommended. |
| `.exe` | Older self-extracting installer (pre-v4.2 releases). |
| `.ssdr` | Pre-extracted firmware file. |

**Steps**

1. Click `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**. If an update is available, the status area displays the version number and instructs you to download the installer from flexradio.com.
4. Download the SmartSDR installer from flexradio.com.
5. Click **Select Installer...** and locate the downloaded `.msi`, `.exe`, or `.ssdr` file. AetherSDR stages the firmware and reports progress in the status area.
6. When staging completes, click **Upload Firmware** to transfer the firmware to the radio.

## Network tab

The Network tab displays radio network information and provides advanced network configuration.

### Network information

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator | Read-only network addresses. Each includes a clipboard copy button. |

### Network configuration

| Control | Kind | Behavior |
|---|---|---|
| **Enforce Private IP Connections:** | Toggle button | Rejects non-RFC1918 peers. Always shows "Enabled" text. |
| **Network MTU:** | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range 576-9000 bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. |
| **DHCP / Static** | Toggle button | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text field | Static IP configuration fields. |
| **Apply** | Push button | Pushes the network config to the radio. |

## GPS tab

The GPS tab displays GPS presence and live positioning information.

| Control | Kind | Behavior |
|---|---|---|
| GPS info | Indicator | Live lat/lon/alt/time/satellites info. |

## TX tab

The TX tab provides transmit timing, interlock, power, and slice/TX follow settings.

### TX Band Settings

| Control | Kind | Behavior |
|---|---|---|
| **TX Band Settings** | Push button | Opens the dedicated per-band power/tune dialog. |

### Timings

| Control | Kind | Behavior |
|---|---|---|
| **ACC TX:** | Spinbox | ACC TX delay in milliseconds. |
| **TX Delay:** | Spinbox | TX delay in milliseconds. |
| **RCA TX1:** | Spinbox | RCA TX1 delay in milliseconds. |
| **Timeout (sec):** | Spinbox | Interlock timeout in seconds (range 0-3600). The radio stores this value in milliseconds internally. |
| **TX2:** | Spinbox | TX2 delay in milliseconds. |

### Interlocks

| Control | Kind | Behavior |
|---|---|---|
| **Interlocks - TX REQ: RCA** | Toggle button | Enables RCA interlock input. |
| **Interlocks - TX REQ: Accessory** | Toggle button | Enables accessory interlock input. |

### Power and Tune

| Control | Kind | Behavior |
|---|---|---|
| **Max Power:** | Spinbox | Sets radio-level TX power cap (0-100%). |
| **Tune Mode:** | Combo box | Selects how the tune button behaves. |

### Waterfall display

| Control | Kind | Behavior |
|---|---|---|
| **Show TX in Waterfall:** | Toggle button | Draws TX signal in the waterfall. |

### Slice/TX follow behavior

| Control | Kind | Behavior |
|---|---|---|
| **TX Follows Active Slice** | Push button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored as `TxFollowsActiveSlice`. Default: False. |
| **Active Slice Follows TX** | Push button | Switches the active slice when TX moves externally (e.g., WSJT-X or
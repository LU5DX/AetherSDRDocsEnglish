# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It provides controls for radio information, network, GPS, TX, Antennas, Phone/CW, RX, Calibration, audio, filters, XVTR, USB cables, peripherals, serial (FlexControl), APD, Themes, and SmartLink pinned certificate management. Many read-only values include a clipboard copy button next to the label for easy sharing with support.

## Opening the dialog

1. Select `Settings > Radio Setup...` from the main menu.
2. The dialog opens as a persistent window that remembers its position and size between sessions. You can drag it by the title bar.
3. Close the dialog by clicking the **X** button on the title bar or pressing `Escape`.

## Radio tab

The **Radio** tab displays radio identification, license information, and firmware update controls. The tab content is wrapped in a scrollable area so all controls remain accessible on small or high-DPI displays.

### Radio information (read-only)

Each read-only field includes a copy button (clipboard icon) that appears on hover or focus. Click the button to copy the field value to the system clipboard. A brief "Copied!" popup confirms the action.

| Control | Behavior |
|---|---|
| **Radio SN** | Chassis serial number. Click the copy button to copy. |
| **Region** | Radio regulatory region. |
| **HW Version** | Hardware version string. Click the copy button to copy. |
| **Model** | Radio model. |
| **Options** | Shows licensed radio options. Click the copy button to copy. |
| **FlexControl** | Detected state of FlexControl hardware. |
| **multiFLEX** | multiFLEX enabled state. |
| **License Info** | Displays subscription, expiration, Radio ID (click the copy button to copy), and licensed version details. |

### Identification fields

| Control | Behavior |
|---|---|
| **Nickname** | User-friendly radio nickname. |
| **Callsign** | Station callsign. |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in `StationName` setting. Sent to radio as "client station <name>". |

### Remote On

Click **Remote On** to enable remote wake / remote-on capability.

### Reboot Radio

Click **Reboot Radio** to restart the connected radio. A confirmation dialog appears before the reboot proceeds.

- **On a LAN connection**: AetherSDR disconnects and automatically reconnects once the radio finishes booting.
- **On a SmartLink/WAN connection**: AetherSDR disconnects. You will need to reconnect manually after the radio finishes booting.

The button is disabled when the radio is disconnected or when the connected backend does not support a client reboot (for example, an RX-only radio like the HL2). It re-enables automatically when the radio reconnects, without requiring you to reopen the dialog.

### Firmware update

1. Click **Check for Update** to query the FlexRadio update server for available firmware versions.
   - If firmware is up to date, the status label shows the current version in green.
   - If an update is available, the status label shows the version number and instructs you to download the SmartSDR installer from flexradio.com.
2. Download the SmartSDR installer from flexradio.com (`.msi` for v4.2+, `.exe` for older releases).
3. Click **Select Installer...** and choose the downloaded installer or a pre-extracted `.ssdr` file. The stager detects the file format automatically and extracts the firmware without external tools. A progress indicator appears while staging completes.
4. Click **Upload Firmware** to transfer the staged firmware to the radio.

## Network tab

The **Network** tab displays radio network information and provides advanced network options.

### Network information (read-only)

| Control | Behavior |
|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each field includes a copy button (clipboard icon) that appears on hover or focus. Click the button to copy the value to the system clipboard. |

### Agent Automation (MCP)

The Network tab includes the Agent Automation (MCP) section for the in-app automation bridge.

| Control | Default | Range | Behavior |
|---|---|---|---|
| **Agent Automation (MCP):** | Disabled | - | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. Persisted via AutomationBridgeSettings. The `AETHER_AUTOMATION` launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless `AETHER_AUTOMATION_ALLOW_TX` is set. |
| **Access Token:** | (none) | - | Read-only display of the MCP access token; paste it into the assistant's `AETHER_MCP_TOKEN` environment variable. Stored in the OS secret store. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| **Copy (Access Token)** | - | - | Copies the access token to the clipboard. |
| **Rotate (Access Token)** | - | - | Generates a new token and applies it immediately, locking out any client still using the old one. |
| **Allow TX via MCP: Enable transmit control** | False | - | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. Enforced in the bridge; no client can flip it. Overridden by `AETHER_AUTOMATION_ALLOW_TX` (force on) and `AETHER_AUTOMATION_NO_TX` (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| **Observe only: Read-only (block all driving)** | False | - | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. Enforced in the app, so a client cannot bypass it. `AETHER_AUTOMATION_READONLY` launch variable pins it on for headless/CI runs. |

### Network settings

| Control | Default | Range | Behavior |
|---|---|---|---|
| **Enforce Private IP Connections:** | Off | - | Rejects non-RFC1918 peers. |
| **VITA-49 RX buffer:** | 4 MB | 0.25-4 MB (presets) | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. Presets 256 KB to 4 MB. The system caps the grant at `net.core.rmem_max`. |
| **granted: (VITA-49 RX buffer)** | - | - | Shows the buffer size the kernel actually granted (vs the requested preset). Shows '(applies on connect)' when no connection is active. |
| **Network MTU:** | 1450 | 576-9000 bytes | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in `NetworkMtu` setting. |
| **DHCP / Static** | DHCP | - | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | - | - | Static IP configuration fields (shown when Static mode is selected). |
| **Apply** | - | - | Pushes the network configuration to the radio. |

## GPS tab

The **GPS** tab shows GPS presence and live latitude/longitude/altitude/time/satellites information.

## TX tab

The **TX** tab controls TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and provides a shortcut to TX Band Settings.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### TX timings

| Control | Default | Range | Behavior |
|---|---|---|---|
| **Timings (in ms)** | - | - | TX hang / delay timings. |

### Other TX controls

| Control | Default | Range | Behavior |
|---|---|---|---|
| **Interlocks - TX REQ: RCA / Accessory** | Off | - | Enables RCA and accessory interlock inputs. |
| **Max Power:** | - | 0-100 % | Sets radio-level TX power cap. |
| **Tune Mode:** | - | - | Selects how the tune button behaves. |
| **Show TX in Waterfall:** | Off | - | Draws TX signal in the waterfall. |
| **TX Follows Active Slice** | False | - | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. Stored in `TxFollowsActiveSlice` setting. |
| **Active Slice Follows TX** | False | - | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. Stored in `ActiveFollowsTxSlice` setting. |

## Antennas tab

The **Antennas** tab allows you to assign custom names to each antenna port on the radio. This tab is lazily built when first clicked. When a port's custom name is empty, the raw port token is used as the display name.

### Antenna name fields

| Control | Behavior |
|---|---|
| **Port / Custom name / Preview / Clear (table columns)** | Grid of antenna port rows. Each row has a read-only port label (e.g. ANT1), an editable text field (max 16 chars), a preview of the final display name, and a Clear button to reset the custom name. Rows auto-update when slice antenna assignments change. |

## Phone/CW tab

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

### Audio meter

| Control | Behavior |
|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. |

### CW keyer

| Control | Default | Range | Behavior |
|---|---|---|---|
| **Iambic:** | Disabled | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| **Swap:** | Off | - | Swaps dit/dah. |
| **Sideband:** | - | LSB / USB | Selects CW pitch sideband. |
| **CWX:** | Off | - | Enables CWX macro keying. |
| **Decode: RX** | True | - | Enables the CW decode overlay on the panadapter for received CW. Stored in `CwDecoder` setting (nested JSON, rx field). |
| **Decode: TX** | False | - | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Stored in `CwDecoder` setting (nested JSON, tx field). |

### RTTY

| Control | Behavior |
|---|---|
| **RTTY Mark Default:** | Default RTTY mark frequency. |

## RX tab

The **RX** tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

### Frequency calibration

The calibration controls are available regardless of whether a GPSDO is installed. The status label at the top of the group reads:
- **GPSDO installed. Manual frequency offset calibration available.** (green) — GPSDO present.
- **Manual frequency offset calibration available.** (amber) — no GPSDO.

| Control | Behavior |
|---|---|
| **Cal Frequency (MHz):** | Enter the reference frequency in MHz used for calibration. Must not be empty before clicking Start. |
| **Start** | Validates the field, resets `freq_error_ppb` to 0, and starts the calibration sweep. Disabled and labeled **Busy** while a sweep is in progress. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion. Applied directly without running a sweep. |
| Status label | Shows current calibration state: Starting, progress text, or error. Updates live during the sweep. |

### 10 MHz reference source

The **10 MHz Reference Source:** combo box selects which oscillator the radio uses as its frequency reference.

#### Combo box population

The combo is populated dynamically based on what the radio reports. Items appear according to the following rules:

| Item label | When shown |
|---|---|
| Auto | Always present. |
| TCXO | Present when the radio has reported any oscillator status, when the radio reports `tcxoPresent`, or when the current or active setting is `tcxo`. |
| GPSDO | Present when the radio reports `gpsdoPresent`, or when the current or active setting is `gpsdo`. |
| External 10 MHz | Present when the radio has reported any oscillator status, when the radio reports `extPresent`, or when the current or active setting is `external`. |

The combo selects the item matching the radio's current `oscSetting`. If that value is not in the list, the combo falls back to the current selection, then to **Auto**.

#### Lock-status label

The label to the right of the combo shows the current oscillator state and lock condition.

| Condition | Label text | Color |
|---|---|---|
| No status received yet | Waiting for oscillator status | Grey |
| Setting is Auto, radio has selected a source | Auto -> \<source\
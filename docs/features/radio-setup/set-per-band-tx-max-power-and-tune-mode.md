# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It organizes radio identification, network, GPS, transmit, phone/CW, receive, calibration, antenna names, filters, transverters, USB cables, peripherals, APD, themes, SmartLink certificate management, serial port settings, DX cluster, KiwiSDR receivers, and user interface settings across multiple tabs.

## Opening Radio Setup

1. Open `Settings > Radio Setup...`.
2. The dialog opens as a persistent dialog; its geometry is saved and restored automatically across sessions.

## Radio tab

The Radio tab displays radio information, identification, license info, and firmware update controls.

### Radio information

| Control | Kind | Notes |
|---|---|---|
| **Radio SN** | Indicator | Chassis serial number (read-only). Click the copy icon next to the value to copy it to clipboard. New in v26.5.3 (#2976). |
| **Region** | Indicator | Radio regulatory region. |
| **HW Version** | Indicator | Hardware version string. Click the copy icon to copy the text. New in v26.5.3 (#2976). |
| **Model** | Indicator | Radio model. Click the copy icon to copy the text. New in v26.5.3 (#2976). |
| **Options** | Indicator | Shows licensed radio options. Click the copy icon to copy the text. New in v26.5.3 (#2976). |
| **FlexControl** | Indicator | Detected state of FlexControl hardware. |
| **multiFLEX** | Indicator | multiFLEX enabled state. |

### Identification

| Control | Kind | Notes |
|---|---|---|
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings. Sent to radio as 'client station <name>'. |

### Copying read-only values

Each read-only information field on this tab (Radio SN, Callsign, Options, HW Version, Region, Model, IP Address, Mask, MAC Address, and License Info fields) displays a small copy icon when you hover over the value. Click the icon to copy the text to the clipboard. A brief "Copied" popup confirms the action.

### License information

The dialog displays license details from the radio including subscription status, expiration date, radio ID, and licensed version. Each field includes a clipboard copy button next to the value.

### Firmware update

1. Click **Check for Update** to query for firmware updates.
   - If an update is available, the status label shows the available version and instructs you to download the SmartSDR installer from flexradio.com.
   - If the firmware is already current, the status label shows "Firmware is up to date."
2. Download the SmartSDR installer from flexradio.com if one is available.
3. Click **Select Installer...**.
   - The file picker accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` file.
   - The firmware stager detects the file format automatically and extracts the `.ssdr` without requiring external tools.
   - While the stager prepares the firmware, the progress bar is shown and the status label reads "Preparing firmware from \<filename\>...".
4. Once staging completes, click **Upload Firmware** to transfer the firmware to the radio. Progress and result are shown in the status label.

| Control | Kind | Notes |
|---|---|---|
| **Check for Update** | Button | Queries for available firmware updates. |
| **Select Installer...** | Button | Opens a file picker. Accepts `.msi`, `.exe`, or `.ssdr`. Previously labelled **Browse .ssdr...** (changed in v26.5.3). |
| **Upload Firmware** | Button | Starts the firmware upload. Progress bar and status label update throughout. |

### Remote On

Click **Remote On** to enable remote wake / remote-on capability.

### Reboot Radio

Click **Reboot Radio** to restart the connected radio.

| Control | Kind | Notes |
|---|---|---|
| **Reboot Radio** | Button | Restarts the radio. A confirmation dialog is shown before rebooting. The button is disabled when the radio is not connected. For LAN connections, AetherSDR automatically reconnects after the radio finishes booting. For SmartLink/WAN connections, you must reconnect manually. The dialog closes after initiating the reboot. |

1. Click **Reboot Radio**.
2. A confirmation dialog explains the behavior difference between LAN and WAN connections.
3. Click **OK** to confirm. AetherSDR sends the reboot command to the radio and closes the setup dialog.

## Network tab

The Network tab displays radio network information and provides advanced network options.

### Network information

| Control | Kind | Notes |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator | Read-only network addresses. Each includes a clipboard copy button. |

### Network settings

| Control | Kind | Default | Valid range | Notes |
|---|---|---|---|---|
| **Enforce Private IP Connections:** | Toggle button | Enabled | — | Rejects non-RFC1918 peers. The button always shows "Enabled" when checked. |
| **Agent Automation (MCP):** | Toggle button | Disabled | — | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| **Access Token:** | Text field | (none) | — | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store. New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| **Copy (Access Token)** | Button | — | — | Copies the access token to the clipboard. New in v26.8.4. |
| **Rotate (Access Token)** | Button | — | — | Generates a new token and applies it immediately, locking out any client still using the old one. New in v26.8.4. |
| **Allow TX via MCP: Enable transmit control** | Checkbox | False | — | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| **Observe only: Read-only (block all driving)** | Checkbox | False | — | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs. |
| **VITA-49 RX buffer:** | Slider | 4 MB | 0.25–4 MB (presets) | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted. |
| **granted: (VITA-49 RX buffer)** | Indicator | — | — | Shows the buffer size the kernel actually granted (vs the requested preset). Shows '(applies on connect)' when no connection is active. New in v26.8.4. |
| **Network MTU:** | Spin box | 1450 | 576–9000 bytes | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. |
| **DHCP / Static** | Toggle button | — | — | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text field | — | — | Static IP configuration fields. |

### Apply network configuration

Click **Apply** to push the network configuration to the radio.

## GPS tab

The GPS tab displays GPS presence and live latitude, longitude, altitude, time, and satellite information.

## TX tab

Use this page to configure transmit settings including timings, interlocks, max power, tune mode, waterfall display, and slice/TX follow behavior.

### TX band settings

Click **TX Band Settings** to open the dedicated per-band power and tune dialog.

### TX controls

| Control | Kind | Default | Notes |
|---|---|---|---|
| **Max Power:** | Spin box | — | Sets radio-level TX power cap. |
| **Tune Mode:** | Combo box | — | Selects how the tune button behaves. |
| **Timings** | Spin box | — | TX hang / delay timings. |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle button | — | Enables RCA and accessory interlock inputs. |
| **Show TX in Waterfall:** | Toggle button | — | Draws TX signal in the waterfall. |
| **TX Follows Active Slice** | Button | False | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Button | False | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. |

### TX timing fields

| Field | Display label | Reported unit | Command suffix |
|---|---|---|---|
| ACC TX | ACC TX | ms | `acc_tx_delay` |
| TX Delay | TX Delay | ms | `tx_delay` |
| RCA TX1 | RCA TX1 | ms | `tx1_delay` |
| Timeout (sec) | Timeout (sec) | seconds | `interlock_timeout` (value multiplied by 1000 before sending to radio) |

The interlock timeout field displays in whole seconds for readability. The radio stores and expects the value in milliseconds; AetherSDR multiplies by 1000 before sending the command to the radio.

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### CW keyer settings

| Control | Kind | Default | Valid range | Notes |
|---|---|---|---|---|
| **Iambic:** | Toggle button | — | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Button | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| **Swap:** | Toggle button | — | — | Swaps dit/dah. |
| **Sideband:** | Combo box | — | LSB / USB | Selects CW pitch sideband. |
| **CWX:** | Toggle button | — | — | Enables CWX macro keying. |
| **Decode: RX** | Toggle button | True | — | Enables the CW decode overlay on the panadapter for received CW. New in v26.5.3: split from single CwDecodeOverlay toggle into independent RX/TX toggles. Persisted as nested JSON blob under `CwDecoder` with rx and tx fields. Legacy `CwDecodeOverlay` key auto-migrated on first read. |
| **Decode: TX** | Toggle button | False | — | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. New in v26.5.3 (#2417). |

### Other audio settings

| Control | Kind | Notes |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle button | Shows mic level meter even in RX. |
| **RTTY Mark Default:** | Spin box | Default RTTY mark frequency. |

## RX tab

The RX tab contains controls for manual frequency offset calibration and 10 MHz reference source selection. Calibration controls are always shown regardless of whether a GPSDO is installed.

### How to run a frequency calibration

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
4. Click **Start**.
   - The button label changes to **Busy** and becomes disabled while calibration runs.
   - The status field to the right of the button shows progress text ("Starting…" then live state).
   - Before starting, AetherSDR resets the frequency error to zero (`radio set freq_error_ppb=0`) and then issues `radio pll
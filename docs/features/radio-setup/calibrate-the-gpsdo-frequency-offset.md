# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, Phone/CW, RX, Calibration, Antennas, Audio, Filters, XVTR, USB cables, peripherals, APD, Themes, SmartLink, and Serial (FlexControl).

## Opening Radio Setup

1. Click **Settings** in the main menu.
2. Select **Radio Setup...**.

The dialog remembers its position and size between sessions.

## Radio (tab)

The Radio tab shows radio identification, license information, and firmware update controls. Each read-only value has a copy button that appears with a document icon on hover or focus; click it to copy the value to the clipboard. A brief "Copied!" popup confirms the action.

### Radio information

The following fields are read-only indicators of the connected radio:

| Control | Description |
|---|---|
| **Radio SN** | Chassis serial number (read-only). Includes a clipboard copy button (tray icon) next to the value. |
| **Region** | Radio regulatory region (e.g., USA). |
| **HW Version** | Hardware version string. Includes a clipboard copy button next to the value. |
| **Options** | Licensed radio options. Includes a clipboard copy button next to the value. |
| **FlexControl** | Detected state of FlexControl hardware. |
| **multiFLEX** | multiFLEX enabled state. |
| **Model** | Radio model. Includes a clipboard copy button next to the value. |
| **License Info** | Subscription details, expiration date, Radio ID, and licensed version. Each field includes a clipboard copy button next to the value. |

### Radio identification fields

| Control | Description |
|---|---|
| **Nickname** | User-friendly radio nickname. |
| **Callsign** | Station callsign. |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Setting key: `StationName`. |

### Remote control and reboot

| Control                                     | Description                                                                                                                                                                                                                                                                 | Notes                                                                                                                                                                                                                                                                            |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Remote On**                               | Enables remote wake / remote-on.                                                                                                                                                                                                                                            |                                                                                                                                                                                                                                                                                  |
| **Reboot Radio**                            | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes.                                                                                                                                           | New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot.                                                            |
| Agent Automation (MCP):                     | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.                                                                                                         | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                               | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                                                                                                                              | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                         | Copies the access token to the clipboard.                                                                                                                                                                                                                                   | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                       | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                                                                                                                           | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control   | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                                                                                                                                 | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                                                                                                                             | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                          | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped.                                                                                                    | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                                                                                                                                | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |
### Firmware update

| Control | Description |
|---|---|
| **Check for Update** | Queries for firmware updates. |
| **Select Installer...** | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. |

1. Click **Check for Update** to query for firmware updates. If an update is available, the status label displays the version number and instructs you to download the installer.
2. Download the installer from flexradio.com (`.msi` for SmartSDR 4.2+, `.exe` for older releases).
3. Click **Select Installer...** and choose the downloaded file. AetherSDR accepts `.msi`, `.exe`, or a pre-extracted `.ssdr` file and stages the firmware automatically.
4. Click **Upload Firmware** to transfer the staged firmware to the radio. A progress bar and status text show the upload progress.

## SmartLink (tab)

The SmartLink tab manages pinned SmartLink TLS certificates. It lists each pinned certificate (host, SHA-256 fingerprint, pinned date) with per-row Forget and Forget All buttons. The tab is lazy-built when first clicked. If a certificate-pin mismatch occurs, the handshake hard-pauses with a modal dialog.

| Control | Description |
|---|---|
| **Pinned SmartLink Certificates (section)** | Section header for the pinned certs table. Lists every host this client has pinned on first connect (trust-on-first-use). |
| **Host / SHA-256 fingerprint / Pinned (table columns)** | 3-column read-only table: Host (hostname), SHA-256 fingerprint (monospace), Pinned (YYYY-MM-DD or '(pre-phase 2)'). |
| **Forget selected** | Removes the selected host's pinned cert fingerprint so the next connect re-pins silently. |
| **Forget all** | Clears every pinned cert (with confirmation). Next connect to each radio silently re-pins. Shows a confirmation dialog before wiping. |

## Network (tab)

The Network tab displays radio network information and provides advanced network options.

### Network information

| Control | Description |
|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each includes a clipboard copy button. |

### Network settings

| Control | Description |
|---|---|
| **Enforce Private IP Connections** | Toggle to reject non-RFC1918 peers. |
| **Network MTU** | Sets maximum outgoing VITA-49 UDP packet size in bytes. Valid range: 576-9000 bytes. Default: 1450. Setting key: `NetworkMtu`. Default 1450 is safe for most VPN/SD-WAN tunnels. |

### IP configuration

1. Switch between **DHCP** and **Static** using the toggle button.
2. In Static mode, enter the **IP Address**, **Mask**, and **Gateway**.
3. Click **Apply** to push the network configuration to the radio.

## GPS (tab)

The GPS tab shows GPS presence and live information including latitude, longitude, altitude, time, and satellite count.

## TX (tab)

The TX tab provides transmit configuration including timings, interlocks, power limits, tune mode, and waterfall display options.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

| Control | Description |
|---|---|
| **Timings (in ms)** | TX hang / delay timings. |

### Interlocks

| Control | Description |
|---|---|
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs. |

### Power and tune

| Control | Description |
|---|---|
| **Max Power** | Sets radio-level TX power cap. Valid range: 0-100%. |
| **Tune Mode** | Selects how the tune button behaves. |

### Waterfall and slice tracking

| Control | Description |
|---|---|
| **Show TX in Waterfall** | Draws TX signal in the waterfall. |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Setting key: `TxFollowsActiveSlice`. Default: False. |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g., WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Setting key: `ActiveFollowsTxSlice`. Default: False. |

## Phone/CW (tab)

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### Microphone

| Control | Description |
|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. |

### CW keyer

| Control | Description |
|---|---|
| **Iambic** | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. Default: A. |
| **Swap** | Swaps dit/dah. |
| **Sideband** | Selects CW pitch sideband. Valid range: LSB, USB. |
| **CWX** | Enables CWX macro keying. |
| **Decode: RX** | Enables the CW decode overlay on the panadapter for received CW. Setting key: `CwDecoder` (nested JSON, `rx` field). Default: True. |
| **Decode: TX** | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Setting key: `CwDecoder` (nested JSON, `tx` field). Default: False. |

### RTTY

| Control | Description |
|---|---|
| **RTTY Mark Default** | Default RTTY mark frequency. |

## RX (tab)

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

### Frequency calibration

1. In **Cal Frequency (MHz):**, enter the frequency of a known-accurate reference signal.
2. Click **Start** to begin the calibration sweep. The button label changes to **Busy** while the sweep runs.
3. When the sweep completes, review the measured offset in **Freq Offset (ppb):**.
4. If you prefer to set the offset manually, edit **Freq Offset (ppb):** directly.

### Calibration status messages

| Message | Colour | Meaning |
|---|---|---|
| Starting... | Blue-grey | The calibration command sequence has been sent to the radio. |
| Enter cal frequency | Amber | **Cal Frequency (MHz):** was empty when **Start** was clicked. |
| Busy | — | Shown on the **Start** button itself while a sweep is in progress. |

### 10 MHz reference source

| Control | Description |
|---|---|
| **10 MHz Reference Source** | Selects oscillator reference source. Valid values: Auto, TCXO, GPSDO, External 10 MHz. Options shown depend on hardware installed. |

The lock status label beside the combo box displays the current oscillator state:

| Display | Meaning |
|---|---|
| `Auto -> GPSDO` (locked) | Auto selected, radio chose GPSDO, locked |
| `GPSDO` (locked) | Source matched and locked |
| `External 10 MHz` (not detected) | External selected but no signal detected |

Colour coding:
- Green (`#00c040`): Oscillator is locked.
- Red (`#c04040`): Oscillator is unlocked.
- Blue-grey (`#8aa8c0`): Oscillator state not yet received.

### GPSDO status banner

- **Green banner**: GPSDO is installed. Manual frequency offset calibration is available.
- **Amber banner**: No GPSDO installed. Manual frequency offset calibration is available.

## Calibration (tab)

The Calibration tab provides host-side manual frequency calibration for radios
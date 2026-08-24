# Radio Setup dialog

This page describes every control in the **Radio Setup** dialog
(`Settings > Radio Setup...`). The dialog has a tab strip along the top;
each section below covers one tab.

---

## Radio tab

Displays radio identification, license information, and firmware update controls.

### Indicators

| Indicator | Behavior |
|---|---|
| **Radio SN** | Chassis serial number (read-only). Includes a clipboard copy button (tray icon) next to the value. |
| **Model** | Radio model (read-only). Includes a clipboard copy button next to the value. |
| **HW Version** | Hardware version string (read-only). Includes a clipboard copy button next to the value. |
| **Region** | Regulatory region; default USA (read-only). |
| **FlexControl** | Detected state of FlexControl hardware (read-only). |
| **multiFLEX** | multiFLEX enabled state (read-only). |
| **Options** | Shows licensed radio options (read-only). Includes a clipboard copy button next to the value. |
| **License Info** | Displays subscription, expiration, Radio ID, and licensed version from the radio (read-only). Each field includes a clipboard copy button next to the value. |

### Editable fields

| Control | Kind | Behavior |
|---|---|---|
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Stored in `StationName`. Defaults to the OS hostname if left empty. Sent to the radio as `client station <name>`. |

### Copy buttons

Each read-only indicator on the Radio tab now has a small **copy-to-clipboard button** (overlapping-documents icon) to its right. Click the button to copy the indicator's value to the system clipboard. A brief popup label ("Copied!") appears near the button after a successful copy. The button is visually dimmed when the value is empty or a dash placeholder.

| Indicator with copy button | Value copied |
|---|---|
| **Radio SN** | The chassis serial number, or the radio serial number if chassis serial is empty. |
| **Model** | The radio model string. |
| **HW Version** | The hardware version string, prefixed with "v" if not already present. |
| **Region** | The regulatory region string. |
| **FlexControl** | The FlexControl detection state string. |
| **multiFLEX** | The multiFLEX enabled state string. |
| **Options** | The licensed options string; if empty, shows "GPS" or "GPS, PGXL" based on amplifier presence. |
| **License Info** | The full license details string as displayed. |

### Buttons

| Control | Behavior |
|---|---|
| **Remote On** | Enables remote wake / remote-on. |
| **Check for Update** | Queries for available firmware updates. When an update is found, the status label reads: *Update available: vX.Y.Z — Download the SmartSDR installer from flexradio.com, then click 'Select Installer...' to stage it.* When firmware is current, the label reads: *Firmware is up to date (vX.Y.Z).* |
| **Select Installer...** | Opens a file picker. Accepts a SmartSDR `.msi` installer (FlexRadio v4.2+ WiX format), an `.exe` self-extracting installer (older releases), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs. PE/COFF MZ header) and extracts the `.ssdr` payload without external tools. Previously labelled **Browse .ssdr...** (changed in v26.5.3). |
| **Upload Firmware** | Starts the firmware upload. A progress bar and status label track progress. Enabled only after a valid file has been staged by **Select Installer...**. |
| **Reboot Radio** | Prompts for confirmation: *Reboot the connected radio now?* The warning text differs for WAN (SmartLink) vs. LAN connections. On LAN, AetherSDR will automatically reconnect after the radio boots. On WAN, you must reconnect manually. Clicking OK sends the reboot command and closes the dialog. Disabled when the radio is not connected. Styled with a reddish background to indicate the destructive nature of the action. |

### Staging a firmware update

1. Click **Check for Update**.
2. If an update is available, download the SmartSDR installer from flexradio.com.
3. Click **Select Installer...** and select the downloaded `.msi`, `.exe`, or `.ssdr` file.
   - The status label shows *Preparing firmware from \<filename\>...* while the stager extracts the payload.
4. When staging completes the status label confirms readiness and **Upload Firmware** becomes active.
5. Click **Upload Firmware** to transfer the firmware to the radio.

---

## Network tab

Displays network addresses and lets you adjust network settings.

### Indicators

| Indicator | Behavior |
|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses reported by the radio. Each includes a clipboard copy button. |

### Controls

| Control                                     | Kind                                                                                                                                                                     | Default                                                                                                                                                                                                                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Enforce Private IP Connections:**         | Toggle button                                                                                                                                                            | Enabled                                                                                                                                                                                                                                                                          |
| **Agent Automation (MCP):**                 | Toggle button                                                                                                                                                            | Disabled. Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| **Access Token:**                           | Text field (read-only)                                                                                                                                                   | (none). Auto-mints a 128-bit hex token when the bridge is enabled without one. Paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store. Placeholder '(loading…)' until the keychain read lands. New in v26.8.4. |
| **Copy (Access Token)**                     | Push button                                                                                                                                                              | Copies the access token to the clipboard. New in v26.8.4.                                                                                                                                                                                                                        |
| **Rotate (Access Token)**                   | Push button                                                                                                                                                              | Generates a new token and applies it immediately, locking out any client still using the old one. New in v26.8.4.                                                                                                                                                               |
| **Allow TX via MCP: Enable transmit control** | Checkbox                                                                                                                                                               | False. Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX. New in v26.8.4. |
| **Observe only: Read-only (block all driving)** | Checkbox                                                                                                                                                              | False. Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs. New in v26.8.4 (#4188). |
| **VITA-49 RX buffer:**                      | Slider (snap-to-preset)                                                                                                                                                  | 4 MB. Sets the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted. New in v26.8.4 (#3810). |
| **granted: (VITA-49 RX buffer)**            | Indicator                                                                                                                                                                | Shows the buffer size the kernel actually granted (vs the requested preset). Shows '(applies on connect)' when no connection is active. New in v26.8.4.                                                                                                                           |
| **Network MTU:**                            | Spinbox                                                                                                                                                                  | 1450. Sets maximum outgoing VITA-49 UDP packet size in bytes (576–9000). Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in `NetworkMtu`.                                                                                                                               |
| **DHCP / Static**                           | Toggle button                                                                                                                                                            | —                                                                                                                                                                                                                                                                                |
| **IP Address: / Mask: / Gateway:**          | Text fields                                                                                                                                                              | —                                                                                                                                                                                                                                                                                |
| **Apply**                                   | Push button                                                                                                                                                              | Pushes the network config to the radio.                                                                                                                                                                                                                                          |

---

## Calibration tab

Provides manual frequency offset calibration for radios that cannot calibrate their own oscillator. This tab is hidden by default and only appears for backends that report a `hostFrequencyCalibration` capability (such as HL2).

> **Note:** Unlike the Flex RX tab (which offers the same calibration controls for radios with GPSDO hardware), this Calibration tab is used when the radio itself cannot correct its oscillator and the correction must happen in the host client. The tab is capability-gated: it stays hidden on a FLEX-8600 even if you type "calibration" in the filter box.

### Controls

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | — | Frequency used for manual calibration. |
| **Freq Offset (ppb):** | Spinbox | — | Manual frequency offset in parts per billion. Applied directly without running a sweep. |
| **Trim** | Push button | — | Commits the displayed frequency offset to the connected radio's calibration. The value is re-read from the radio each time the dialog opens or the connection changes, so a stale value from a previously connected radio cannot be committed accidentally. |

### Using the Calibration tab

1. Click `Settings > Radio Setup...`.
2. Click the **Calibration** tab.
3. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
4. Adjust **Freq Offset (ppb):** to correct the displayed frequency error.
5. Click **Trim** to commit the offset to the radio.

The calibration values are re-read whenever the dialog is shown or a different radio connects, ensuring the displayed offset always reflects the currently connected radio.

---

## GPS tab

Displays GPS presence and live position data when a GPS receiver is attached to the radio.

| Indicator | Behavior |
|---|---|
| Live GPS data | Shows latitude, longitude, altitude, time, and satellite count. Updated in real time. |

---

## TX tab

Controls TX timings, power limits, tune mode, and slice-follow behavior.

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Timings (in ms)** | Spinbox fields | — | TX hang and delay timings. Fields: ACC TX (ms), TX Delay (ms), RCA TX1 (ms). |
| **Timeout (sec):** | Spinbox | — | Interlock timeout in seconds. The value is sent to the radio in milliseconds (multiplied by 1000). |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle button | — | Enables the RCA and accessory interlock inputs. |
| **Max Power:** | Spinbox | — | Radio-level TX power cap (0–100%). |
| **Tune Mode:** | Combo box | — | Selects how the Tune button behaves. |
| **Show TX in Waterfall:** | Toggle button | — | Draws the TX signal in the waterfall display. |
| **TX Follows Active Slice** | Push button | False | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored in `TxFollowsActiveSlice`. |
| **Active Slice Follows TX** | Push button | False | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored in `ActiveFollowsTxSlice`. |
| **TX Band Settings** | Push button | — | Opens the dedicated per-band power and tune dialog. |

---

## Phone/CW tab

Configures the microphone, CW keyer, and RTTY defaults.

### Iambic keyer

1. Click `Settings > Radio Setup...`.
2. Click the **Phone/CW** tab.
3. Confirm **Iambic:** reads **Enabled**. If it reads **Disabled**, click it once to enable the keyer.
4. Click **A** or **B** to select Curtis iambic mode.

| Control | Kind | Default | Behavior |
|---|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle button | — | Shows the mic level meter during RX. |
| **Iambic:** | Toggle button | — | Enables or disables the iambic keyer on the radio. Always reads "Enabled" when toggled on. |
| **Iambic Mode: A / B** | Push button (mutually exclusive pair) | A | Selects Curtis iambic mode A or B for both the radio hardware keyer and the local software keyer. Mode A = Curtis A; Mode B = Curtis B
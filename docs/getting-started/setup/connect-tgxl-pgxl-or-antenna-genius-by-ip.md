# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, Phone/CW, RX, Calibration, audio, antennas, filters, XVTR, USB cables, peripherals, APD, themes, serial port, SmartLink pinned certificate configuration, and KiwiSDR public receiver access.

## Opening the dialog

1. Open `Settings > Radio Setup...`.
2. The dialog opens as a persistent window. Its size and position are saved between sessions.

---

## Radio tab

The Radio tab displays radio information, identification, license info, and firmware update controls.

### Radio information

| Control                                             | Type                                                                                                                                                                                        | Behavior                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Radio SN                                            | Chassis serial number (read-only).                                                                                                                                                          | Includes a clipboard copy button (tray icon) next to the value. New in v26.5.3 (#2976).                                                                                                                                                                                          |
| Region                                              | Indicator                                                                                                                                                                                   | Radio regulatory region.                                                                                                                                                                                                                                                         |
| HW Version                                          | Hardware version string.                                                                                                                                                                    | Includes a clipboard copy button next to the value (#2976).                                                                                                                                                                                                                      |
| Model                                               | Radio model.                                                                                                                                                                                | Includes a clipboard copy button next to the value (#2976).                                                                                                                                                                                                                      |
| Options                                             | Shows licensed radio options.                                                                                                                                                               | Includes a clipboard copy button next to the value (#2976).                                                                                                                                                                                                                      |
| FlexControl                                         | Indicator                                                                                                                                                                                   | Detected state of FlexControl hardware.                                                                                                                                                                                                                                          |
| multiFLEX                                           | Indicator                                                                                                                                                                                   | multiFLEX enabled state.                                                                                                                                                                                                                                                         |
| Nickname                                            | Text field                                                                                                                                                                                  | User-friendly radio nickname.                                                                                                                                                                                                                                                    |
| Callsign                                            | Text field                                                                                                                                                                                  | Station callsign.                                                                                                                                                                                                                                                                |
| Station Name                                        | Text field                                                                                                                                                                                  | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings. Sent to radio as 'client station \<name\>'.                                                                                                           |
| License Info                                        | Indicator                                                                                                                                                                                   | Displays license details from the radio (Subscription, Expiration, Radio ID, Licensed version).                                                                                                                                                                                  |
| Select Installer...                                 | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. | Label changed from 'Browse .ssdr...' to 'Select Installer...' in v26.5.3.                                                                                                                                                                                                        |
| Reboot Radio                                        | Push button                                                                                                                                                                                 | Reboots the connected radio. Disabled when the radio is disconnected. Shows a confirmation dialog before rebooting. On LAN connections, AetherSDR auto-reconnects after the radio boots; on SmartLink/WAN, manual reconnection is required. New in v26.8.4 (#4448).               |
| SmartLink (tab)                                     | Pinned SmartLink TLS certificate management. Lists each pinned certificate (host, SHA-256 fingerprint, pinned date) with per-row Forget and Forget All. New in v26.5.3 (#2951 Phase 2).     | Lazy-built when first clicked. Phase 2 of GHSA-wfx7-w6p8-4jr2: cert-pin mismatch now hard-pauses the handshake with a modal dialog.                                                                                                                                              |
| Pinned SmartLink Certificates (section)             | Section header for the pinned certs table inside the SmartLink tab. Lists every host this client has pinned on first connect (trust-on-first-use).                                          | Phase 2 of GHSA-wfx7-w6p8-4jr2. Pin schema migrated from plain strings to {fp, pinnedAt} objects.                                                                                                                                                                                |
| Host / SHA-256 fingerprint / Pinned (table columns) | 3-column read-only table: Host (hostname), SHA-256 fingerprint (monospace), Pinned (YYYY-MM-DD or '(pre-phase 2)').                                                                         | Backed by WanCertCache in WanConnection.cpp.                                                                                                                                                                                                                                     |
| Forget selected                                     | Removes the selected host's pinned cert fingerprint so the next connect re-pins silently.                                                                                                   |                                                                                                                                                                                                                                                                                  |
| Forget all                                          | Clears every pinned cert (with confirmation). Next connect to each radio silently re-pins.                                                                                                  | Shows QMessageBox::question before wiping.                                                                                                                                                                                                                                       |
| Check for Update                                    | Push button                                                                                                                                                                                 | Queries for firmware updates.                                                                                                                                                                                                                                                    |
| Upload Firmware                                     | Push button                                                                                                                                                                                 | Starts firmware upload with progress bar and status.                                                                                                                                                                                                                             |
| Agent Automation (MCP):                             | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.                         | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                                       | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                                              | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                                 | Copies the access token to the clipboard.                                                                                                                                                   | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                               | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                                           | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control           | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                                                 | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving)         | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                                             | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                                  | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped.                    | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                        | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                                                | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |

Each read-only value has a copy-to-clipboard button next to it (a small icon appearing on hover). Click the button to copy the value.

### Remote On

Click **Remote On** to enable remote wake / remote-on functionality.

### Reboot Radio

Click **Reboot Radio** to restart the connected radio. A confirmation dialog warns:

- **LAN connection:** AetherSDR disconnects and automatically reconnects once the radio finishes booting.
- **SmartLink/WAN connection:** AetherSDR disconnects. You must reconnect manually after the radio reboots.

The button is disabled when the radio is disconnected or reconnecting. It re-enables automatically when the radio reconnects.

### Firmware update

**Check for Update** queries the radio for available firmware updates. When a newer version is found, AetherSDR displays an informational message:

> Update available: v*X.Y.Z*
> Download the SmartSDR installer from flexradio.com,
> then click 'Select Installer...' to stage it.

**Select Installer...** (renamed from Browse .ssdr... in v0.9.3) accepts three file types:

| File type | Extension | Notes |
|---|---|---|
| SmartSDR WiX installer | .msi | FlexRadio v4.2 and later |
| SmartSDR self-extracting installer | .exe | Older SmartSDR releases |
| Extracted firmware file | .ssdr | As in previous AetherSDR versions |

The firmware stager detects the format automatically from the first 8 bytes of the file (OLE/MSI magic versus PE/COFF MZ header) and extracts the .ssdr payload without requiring any external tools.

#### To stage firmware from a local installer

1. Download the SmartSDR installer from flexradio.com.
2. Open `Settings > Radio Setup...`.
3. Click the **Radio** tab.
4. Click **Select Installer...**.
5. In the file picker, select the .msi, .exe, or .ssdr file.
6. AetherSDR extracts and stages the firmware. Watch the progress bar and status line for progress and any errors.
7. When staging is complete, click **Upload Firmware** to send the firmware to the radio.

---

## Network tab

The Network tab displays radio network information and advanced network options.

### Network information

| Control | Type | Behavior |
|---|---|---|
| IP Address / Mask / MAC Address | Indicator | Read-only network addresses. Each includes a clipboard copy button (#2976). |

### Network settings

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| Enforce Private IP Connections | Toggle button | — | — | Rejects non-RFC1918 peers. |
| Network MTU | Spinbox | 1450 | 576–9000 bytes | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings. |
| DHCP / Static | Toggle button | — | — | Switches between DHCP and Static IP modes. |
| IP Address / Mask / Gateway | Text field | — | — | Static IP configuration fields. |
| Apply | Push button | — | — | Pushes the network config to the radio. |

---

## GPS tab

The GPS tab shows GPS presence and live latitude, longitude, altitude, time, and satellites information.

---

## TX tab

The TX tab contains TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow options, and a TX Band Settings shortcut.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

The TX timings section includes spinbox fields for millisecond values.

| Control | Display label | Default | Behavior |
|---|---|---|---|
| ACC TX | ACC TX: | — | ACC timing delay in ms. |
| TX Delay | TX Delay: | — | TX delay in ms. |
| RCA TX1 | RCA TX1: | — | RCA TX1 delay in ms. |
| Timeout | Timeout (sec): | — | Interlock timeout displayed in seconds. The radio stores this value in milliseconds. |

### Interlocks

**TX REQ: RCA** and **TX REQ: Accessory** toggle buttons enable RCA and accessory interlock inputs.

### Power and tune

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| Max Power | Spinbox | — | 0–100% | Sets radio-level TX power cap. |
| Tune Mode | Combo box | — | — | Selects how the tune button behaves. |

### Waterfall and slice follow

| Control | Type | Default | Setting key | Behavior |
|---|---|---|---|---|
| Show TX in Waterfall | Toggle button | — | — | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | False | `TxFollowsActiveSlice` | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. |
| Active Slice Follows TX | Push button | False | `ActiveFollowsTxSlice` | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. |

---

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

### Microphone

**Enable/Disable the Level Meter During Receive** toggles showing the mic level meter even in RX.

### CW keyer

| Control | Type | Default | Range | Behavior |
|---|---|---|---|---|
| Iambic | Toggle button | — | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| Iambic Mode | Push button | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| Swap | Toggle button | — | — | Swaps dit/dah. |
| Sideband | Combo box | — | LSB / USB | Selects CW pitch sideband. |
| CWX | Toggle button | — | — | Enables CW
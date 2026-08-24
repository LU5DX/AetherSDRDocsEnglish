# Configure Radio Setup

The **Radio Setup** dialog (`Settings > Radio Setup...`) provides master per-radio configuration with tabbed sections for radio information, network, GPS, TX, Phone/CW, RX, audio, filters, calibration, antennas, transverters, USB cables, peripherals, adaptive pre-distortion, themes, SmartLink pinned certificates, serial port settings, KiwiSDR public receiver browsing, callsign lookup parameters, amplifier (Acom) configuration, and Automation Bridge parameters.

## Before you start

- The radio must be connected before most tabs show live information.
- Some tabs (APD, Themes, SmartLink, Serial, KiwiSDR, Callsign Lookup, Acom, Automation Bridge) are built lazily and only appear when first clicked.
- AetherSDR uses a `PersistentDialog` base class that saves and restores window geometry automatically.

## Steps to open

1. Click **Settings > Radio Setup...** in the main menu.
2. The dialog opens showing the **Radio** tab by default.
3. Click any tab to access its settings.

---

## Radio tab

The **Radio** tab shows radio identification, license information, and firmware update controls.

### Reading radio information

- **Radio SN** — Chassis serial number (read-only). Shows the chassis serial if available, otherwise the radio serial. Includes a clipboard copy button next to the value.
- **Region** — Radio regulatory region (read-only).
- **HW Version** — Hardware version string (read-only). Includes a clipboard copy button next to the value.
- **Model** — Radio model (read-only). Includes a clipboard copy button next to the value.
- **Options** — Licensed radio options (read-only). Shows the radio's options list, or a default like "GPS, PGXL" if an amplifier is detected. Includes a clipboard copy button next to the value.
- **FlexControl** — Detected state of FlexControl hardware (read-only).
- **multiFLEX** — multiFLEX enabled state (read-only).
- **License Info** — Displays subscription, expiration, Radio ID, and licensed version (read-only). Each field includes a clipboard copy button next to the value.

### Copying radio information

Each read-only value has a small copy button next to it. Click the copy button to copy the value to your clipboard. A brief "Copied!" popup appears near the button. The copy button is disabled when the value is empty or shows "—".

### Setting identification

| Control                                             | What it does                                                                                                                                                                                | Notes                                                                                                                                                                                                                                                                            |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nickname**                                        | User-friendly radio nickname (editable).                                                                                                                                                    | —                                                                                                                                                                                                                                                                                |
| **Callsign**                                        | Station callsign (editable).                                                                                                                                                                | —                                                                                                                                                                                                                                                                                |
| **Station Name**                                    | Identifies this AetherSDR client to other multiFLEX stations. Stored in AppSettings.                                                                                                        | Defaults to the OS hostname if empty. Sent to radio as 'client station <name>'.                                                                                                                                                                                                  |
| Select Installer...                                 | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. | Label changed from 'Browse .ssdr...' to 'Select Installer...' in v26.5.3.                                                                                                                                                                                                        |
| SmartLink (tab)                                     | Pinned SmartLink TLS certificate management. Lists each pinned certificate (host, SHA-256 fingerprint, pinned date) with per-row Forget and Forget All. New in v26.5.3 (#2951 Phase 2).     | Lazy-built when first clicked. Phase 2 of GHSA-wfx7-w6p8-4jr2: cert-pin mismatch now hard-pauses the handshake with a modal dialog.                                                                                                                                              |
| Pinned SmartLink Certificates (section)             | Section header for the pinned certs table inside the SmartLink tab. Lists every host this client has pinned on first connect (trust-on-first-use).                                          | Phase 2 of GHSA-wfx7-w6p8-4jr2. Pin schema migrated from plain strings to {fp, pinnedAt} objects.                                                                                                                                                                                |
| Host / SHA-256 fingerprint / Pinned (table columns) | 3-column read-only table: Host (hostname), SHA-256 fingerprint (monospace), Pinned (YYYY-MM-DD or '(pre-phase 2)').                                                                         | Backed by WanCertCache in WanConnection.cpp.                                                                                                                                                                                                                                     |
| Forget selected                                     | Removes the selected host's pinned cert fingerprint so the next connect re-pins silently.                                                                                                   |                                                                                                                                                                                                                                                                                  |
| Forget all                                          | Clears every pinned cert (with confirmation). Next connect to each radio silently re-pins.                                                                                                  | Shows QMessageBox::question before wiping.                                                                                                                                                                                                                                       |
| Reboot Radio                                        | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes.                                                           | New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot.                                                            |
| Agent Automation (MCP):                             | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.                         | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                                       | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                                              | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                                 | Copies the access token to the clipboard.                                                                                                                                                   | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                               | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                                           | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control           | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                                                 | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving)         | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                                             | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                                  | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped.                    | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                        | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                                                | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |
### Firmware update

1. Click **Check for Update** to query for available firmware updates. The result appears in the status label. If an update is available, the label directs you to download the SmartSDR installer from flexradio.com.
2. Click **Select Installer...** to open a file picker. Select one of:
   - `.msi` — WiX-based SmartSDR installer for firmware 4.2+.
   - `.exe` — Older self-extracting SmartSDR installer.
   - `.ssdr` — Pre-extracted firmware file.
3. The firmware stager detects the file format automatically and extracts the `.ssdr` payload. A progress bar and status label show extraction progress.
4. Once extraction completes, click **Upload Firmware** to start the upload. A progress bar and status label show upload progress.

| Control | What it does | Notes |
|---|---|---|
| **Check for Update** | Queries for available firmware updates. | When an update is found, the label directs you to download the installer from flexradio.com. |
| **Select Installer...** | Opens a file picker for `.msi`, `.exe`, or `.ssdr` files. | Renamed from **Browse .ssdr...** in v26.5.3. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. | Enabled only after extraction completes. |

### Remote On

Click **Remote On** to enable remote wake / remote-on functionality on the radio.

### Reboot Radio

Click **Reboot Radio** to reboot the connected radio. A confirmation dialog appears:
- **LAN connection**: AetherSDR disconnects and automatically reconnects once the radio finishes booting.
- **SmartLink/WAN connection**: AetherSDR disconnects and does not auto-reconnect. You must reconnect manually once the radio finishes booting.

The button is disabled when the radio is disconnected. It re-enables automatically when the radio reconnects.

---

## Network tab

The **Network** tab shows radio network information and advanced network options.

### Reading network info

- **IP Address / Mask / MAC Address** — Read-only network addresses. Each includes a clipboard copy button.

### Network configuration

| Control | What it does | Default | Notes |
|---|---|---|---|
| **Enforce Private IP Connections:** | Toggle to reject non-RFC1918 peers. | Enabled | — |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes. | 1450 | Range 576–9000 bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings. |
| **DHCP / Static** | Toggle between DHCP and Static IP modes. | — | — |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields. | — | Enabled when Static mode is selected. |
| **Apply** | Pushes the network config to the radio. | — | — |

---

## GPS tab

The **GPS** tab shows GPS presence and live position/satellite information when a GPS receiver is active.

- Latitude, longitude, altitude, time, and satellite count (read-only).
- GPS lock status indicator.

---

## TX tab

The **TX** tab configures transmit timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX Band Settings.

### TX Band Settings

Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

### Timings

Use the spinboxes in the **Timings (in ms)** section to set TX hang and delay timings.

### Interlocks

Toggle **TX REQ: RCA** and **TX REQ: Accessory** to enable RCA and accessory interlock inputs.

### Max Power

Set the radio-level TX power cap using the **Max Power:** spinbox (0–100%).

### Tune Mode

Select the tune button behavior from the **Tune Mode:** combo box.

### Waterfall

Toggle **Show TX in Waterfall:** to draw the TX signal in the waterfall.

### Slice/TX follow

| Control | What it does | Default | Notes |
|---|---|---|---|
| **TX Follows Active Slice** | TX follows the active slice. | False | Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). | False | Mutually exclusive with **TX Follows Active Slice**. |

---

## Phone/CW tab

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

### Level Meter

Toggle **Enable/Disable the Level Meter During Receive** to show the mic level meter even during receive.

### CW Keyer

| Control | What it does | Default | Notes |
|---|---|---|---|
| **Iambic:** | Enables or disables the iambic keyer on the radio. | — | In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. | A | Mutually exclusive pair added in v0.9.1. |
| **Swap:** | Swaps dit/dah. | — | — |
| **Sideband:** | Selects CW pitch sideband. | — | Options: LSB / USB. |
|
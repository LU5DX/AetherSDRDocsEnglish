# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It provides access to all radio-level settings including radio identification, network configuration, GPS, transmit parameters, phone/CW settings, receive calibration, audio configuration, filters, transverters, USB cables, peripherals, APD sampling, themes, SmartLink certificate management, serial port configuration, KiwiSDR public receivers, and serial port configuration.

## Before you start

- AetherSDR must be connected to the radio. Most controls are not available without an active connection.

## Opening the dialog

1. Open `Settings > Radio Setup...`.
2. The dialog opens as a persistent window. Its position and size are saved automatically when you close it and restored the next time you open it. The geometry is stored in AppSettings under the key `RadioSetupDialogGeometry`.

### Tab scroll areas

Some tabs (Themes, Audio, Filters, Peripherals, KiwiSDR) contain more controls than fit vertically on small or high-DPI displays. These tabs are automatically wrapped in a vertical scroll area so you can scroll down to reach all controls without resizing the dialog beyond the screen edge. The scrollbar appears only when content exceeds the visible area.

## Radio tab

The **Radio** tab displays radio information, identification, license info, remote on, firmware update, and reboot controls.

### Radio Information

The radio information section shows read-only indicators for:

| Control                                                                    | Description                                                                                                                                                                                 | Notes                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Radio SN**                                                               | Chassis serial number (read-only).                                                                                                                                                          | Includes a clipboard copy button (tray icon) next to the value.                                                                                                                                                                                                                  |
| **Region**                                                                 | Radio regulatory region (e.g., USA).                                                                                                                                                        |                                                                                                                                                                                                                                                                                  |
| **HW Version**                                                             | Hardware version string.                                                                                                                                                                    | Includes a clipboard copy button next to the value.                                                                                                                                                                                                                              |
| **Model**                                                                  | Radio model.                                                                                                                                                                                | Includes a clipboard copy button next to the value.                                                                                                                                                                                                                              |
| **Options**                                                                | Shows licensed radio options.                                                                                                                                                               | Includes a clipboard copy button next to the value.                                                                                                                                                                                                                              |
| **FlexControl**                                                            | Detected state of FlexControl hardware.                                                                                                                                                     |                                                                                                                                                                                                                                                                                  |
| **multiFLEX**                                                              | multiFLEX enabled state.                                                                                                                                                                    |                                                                                                                                                                                                                                                                                  |
| **License Info** (Subscription / Expiration / Radio ID / Licensed version) | Displays license details from the radio.                                                                                                                                                    | Each field includes a clipboard copy button next to the value.                                                                                                                                                                                                                   |
| **Select Installer...**                                                    | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. | Label changed from 'Browse .ssdr...' to 'Select Installer...' in v26.5.3.                                                                                                                                                                                                        |
| **SmartLink (tab)**                                                        | Pinned SmartLink TLS certificate management. Lists each pinned certificate (host, SHA-256 fingerprint, pinned date) with per-row Forget and Forget All. New in v26.5.3 (#2951 Phase 2).     | Lazy-built when first clicked. Phase 2 of GHSA-wfx7-w6p8-4jr2: cert-pin mismatch now hard-pauses the handshake with a modal dialog.                                                                                                                                              |
| **Pinned SmartLink Certificates (section)**                                | Section header for the pinned certs table inside the SmartLink tab. Lists every host this client has pinned on first connect (trust-on-first-use).                                          | Phase 2 of GHSA-wfx7-w6p8-4jr2. Pin schema migrated from plain strings to {fp, pinnedAt} objects.                                                                                                                                                                                |
| **Host / SHA-256 fingerprint / Pinned (table columns)**                    | 3-column read-only table: Host (hostname), SHA-256 fingerprint (monospace), Pinned (YYYY-MM-DD or '(pre-phase 2)').                                                                         | Backed by WanCertCache in WanConnection.cpp.                                                                                                                                                                                                                                     |
| **Forget selected**                                                        | Removes the selected host's pinned cert fingerprint so the next connect re-pins silently.                                                                                                   |                                                                                                                                                                                                                                                                                  |
| **Forget all**                                                             | Clears every pinned cert (with confirmation). Next connect to each radio silently re-pins.                                                                                                  | Shows QMessageBox::question before wiping.                                                                                                                                                                                                                                       |
| Reboot Radio                                                               | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes.                                                           | New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot.                                                            |
| Agent Automation (MCP):                                                    | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.                         | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                                                              | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                                              | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                                                        | Copies the access token to the clipboard.                                                                                                                                                   | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                                                      | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                                           | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control                                  | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                                                 | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving)                                | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                                             | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                                                         | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped.                    | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                                               | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                                                | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |
### Radio Identification

Set a human-readable nickname, your callsign, and a station name on the connected FLEX-8600. These values identify the radio and this client to other multiFLEX stations on the network.

| Control | Description | Default |
|---|---|---|
| **Nickname** | User-friendly label for the radio. Sent to the radio as the radio name. | Radio's reported name |
| **Callsign** | Your station callsign, stored on the radio. | _(blank)_ |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Stored in AppSettings. Sent to radio as 'client station <name>'. | OS hostname |

### Steps to set radio identification

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. In the **Nickname** field, type the nickname you want to assign to the radio.
4. Press Tab or click away from the field to confirm. AetherSDR sends the new name to the radio immediately.
5. In the **Callsign** field, type your station callsign.
6. Press Tab or click away from the field to confirm.
7. In the **Station Name** field, type the name that identifies this client to other multiFLEX stations.
8. Press Tab or click away from the field to confirm.
9. Click the window's close button or press Escape to dismiss the dialog.

### Remote On

Click **Remote On** to enable remote wake / remote-on capability.

### Reboot Radio

The **Reboot Radio** button restarts the connected radio. This is useful after firmware updates or configuration changes that require a reboot.

- The button is enabled only when the radio is connected. It disables automatically on disconnect or reconnect.
- A confirmation dialog appears before rebooting.
- The warning text differs by connection type:
  - **SmartLink/WAN**: "Reboot the connected radio now? AetherSDR will disconnect. SmartLink/WAN sessions do not auto-reconnect today — you will need to reconnect manually once the radio finishes booting."
  - **Direct/LAN**: "Reboot the connected radio now? AetherSDR will disconnect and automatically reconnect once the radio finishes booting."
- Click **OK** to confirm. The dialog closes and AetherSDR disconnects.
- The button has a styled disabled appearance so it remains visible but clearly greyed out when the radio is not connected.

### Steps to reboot the radio

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Reboot Radio**.
4. Read the confirmation dialog that appears.
5. Click **OK** to confirm. AetherSDR disconnects and the dialog closes.
6. Wait for the radio to finish booting. On direct/LAN connections, AetherSDR reconnects automatically.

### Firmware Update

Use the firmware update controls to check for and apply firmware updates to the radio.

| Control | Description |
|---|---|
| **Check for Update** | Queries for firmware updates. |
| **Select Installer...** | Opens a file picker that accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer) or a pre-extracted .ssdr firmware file. The firmware stager auto-detects format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the .ssdr without external tools. Label changed from 'Browse .ssdr...' in v26.5.3. |
| **Upload Firmware** | Starts firmware upload with progress bar and status. |

#### To check for a firmware update

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, the status label shows the available version number and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it.
   - If firmware is up to date, the status label confirms the current version in green.

#### To stage and upload firmware

1. Download the SmartSDR installer from flexradio.com. AetherSDR accepts .msi (FlexRadio v4.2+ WiX installer), .exe (older self-extracting installer), or a pre-extracted .ssdr firmware file.
2. Click **Select Installer...**
   - The file picker opens with the filter set to `*.msi *.exe *.ssdr`.
   - Select the downloaded file and click Open.
   - AetherSDR begins preparing the firmware automatically. The status label shows "Preparing firmware from \<filename\>..." and the progress bar appears.
   - The firmware stager auto-detects the file format from the first 8 bytes (OLE/MSI magic for .msi, PE/COFF MZ for .exe, or CTRL+Z for .ssdr) and extracts the .ssdr without external tools.
3. Wait for preparation to complete. The status label shows "Ready to upload \<filename\>".
4. Click **Upload Firmware**.
   - A confirmation dialog appears: "This will restart the radio. Are you sure you want to upload \<filename\>?"
5. Click **Yes** to confirm.
   - The upload begins. The status label shows "Uploading... (X%)" and the progress bar updates.
   - The radio restarts after upload completes. The status label shows "Upload and reboot successful."
6. Click the window's close button or press Escape to dismiss the dialog.

## Network tab

The **Network** tab displays radio network information and provides advanced network options.

| Control | Description | Default |
|---|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each includes a clipboard copy button. | — |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers. Toggle button shows "Enabled"
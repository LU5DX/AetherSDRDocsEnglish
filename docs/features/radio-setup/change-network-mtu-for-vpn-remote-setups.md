# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, phone/CW, RX, calibration, antennas, filters, XVTR, USB cables, peripherals, serial/FlexControl, themes, APD, and SmartLink certificate management. Many read-only values include a clipboard copy button next to the label for easy sharing with support.

## Opening the dialog

1. Click `Settings > Radio Setup...`.
2. The dialog opens with the **Radio** tab selected.

## General dialog behavior

- The dialog geometry is persisted across sessions using `PersistentDialog`.
- Changes made on some tabs are applied immediately; others require clicking an Apply or Connect button.
- If you clear an IP field on the **Peripherals** tab and close the dialog without clicking Connect/Disconnect, the saved manual IP and port are automatically removed and the device disconnects.
- Tabs whose content may exceed the dialog's visible height (Themes, Audio, Filters, Peripherals on small or high-DPI displays) are wrapped in a vertical scroll area so the dialog does not overflow the screen edge.
- All QCheckBox indicators use ThemeManager tokens for visibility in dark mode, with hover and disabled pseudo-states.
- The search filter respects capability-gated pages: typing a keyword that matches a hidden page (e.g. "calibration" on a Flex) does not surface a page the radio cannot use.

## Radio (tab)

The Radio tab displays radio information, identification, license info, firmware update controls, and a reboot button.

| Control                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   | Notes                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Radio SN**                                | Chassis serial number (read-only).                                                                                                                                                                                                                                                                                                                                                                                                            | Includes a clipboard copy button next to the value. New in v26.5.3 (#2976).                                                                                                                                                                                                                                                                                              |
| **Region**                                  | Radio regulatory region (read-only).                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                           |
| **HW Version**                              | Hardware version string (read-only).                                                                                                                                                                                                                                                                                                                                                                                                          | Includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                                                                                       |
| **Remote On**                               | Enables remote wake / remote-on.                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                           |
| **Options**                                 | Shows licensed radio options (read-only).                                                                                                                                                                                                                                                                                                                                                                                                     | Includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                                                                                       |
| **FlexControl**                             | Detected state of FlexControl hardware (read-only).                                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                                           |
| **multiFLEX**                               | multiFLEX enabled state (read-only).                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                           |
| **Model**                                   | Radio model (read-only).                                                                                                                                                                                                                                                                                                                                                                                                                      | Includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                                                                                       |
| **Nickname**                                | User-friendly radio nickname.                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                           |
| **Callsign**                                | Station callsign.                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                           |
| **Station Name**                            | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty.                                                                                                                                                                                                                                                                                                                                           | Stored in AppSettings as `StationName`. Sent to radio as "client station \<name\>".                                                                                                                                                                                                                                                                                      |
| **License Info**                            | Displays license details from the radio: subscription, expiration, radio ID, and licensed version.                                                                                                                                                                                                                                                                                                                                            | Each field (Subscription, Expiration, Radio ID, Licensed version) includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                     |
| **Check for Update**                        | Queries for firmware updates.                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                                                                           |
| **Select Installer...**                     | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress.                                                                                                                                                                                                                                                   | Label changed from 'Browse .ssdr...' to 'Select Installer...' in v26.5.3.                                                                                                                                                                                                                                                                                                 |
| **Upload Firmware**                         | Starts firmware upload with progress bar and status.                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                           |
| **Reboot Radio**                            | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes.                                                                                                                                                                                                                                                                                                             | New in v26.8.4 (#4448). Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot.                                                                                                                                                      |
| Agent Automation (MCP):                     | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.                                                                                                                                                                                                                                                                          | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set.                                                                                           |
| Access Token:                               | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                                                                                                                                                                                                                                                                                               | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                                                                                                           |
| Copy (Access Token)                         | Copies the access token to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                     | New in v26.8.4.                                                                                                                                                                                                                                                                                                                                                           |
| Rotate (Access Token)                       | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                                                                                                                                                                                                                                                                                            | New in v26.8.4.                                                                                                                                                                                                                                                                                                                                                           |
| Allow TX via MCP: Enable transmit control   | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                                                                                                                                                                                                                                                                                                  | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                                                                                                           |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                                                                                                                                                                                                                                                                                              | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                                                                                                                     |
| VITA-49 RX buffer:                          | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped.                                                                                                                                                                                                                                                                     | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                                                                                                                   |
| granted: (VITA-49 RX buffer)                | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                                                                                                                                                                                                                                                                                                 | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                                                                                                               |

### Copyable values (Radio tab)

The Radio SN, HW Version, Options, Model, and each License Info field display a small copy button when hovered or focused. Clicking the button copies the displayed value to the system clipboard and shows a brief "Copied!" popup near the button.

### Rebooting the radio

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Locate **Reboot Radio** button.
4. Click **Reboot Radio**.
   - A confirmation dialog appears with different text depending on connection type:
     - **WAN/SmartLink:** "AetherSDR will disconnect. SmartLink/WAN sessions do not auto-reconnect today — you will need to reconnect manually once the radio finishes booting."
     - **LAN:** "AetherSDR will disconnect and automatically reconnect once the radio finishes booting."
5. Click **OK** to confirm.
   - The dialog closes automatically.
   - The radio reboots and AetherSDR disconnects.

### Firmware update (Radio tab)

AetherSDR does not download firmware automatically when an update is detected. Download the SmartSDR installer from flexradio.com yourself, then stage it manually.

#### Staging a firmware update

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, a status message tells you the available version and directs you to download the installer from flexradio.com.
   - If firmware is current, a green status message confirms the installed version.
4. Download the SmartSDR installer from flexradio.com. Accepted formats:
   - `.msi` — WiX installer (FlexRadio SmartSDR v4.2 and later)
   - `.exe` — older self-extracting installer
   - `.ssdr` — pre-extracted firmware file
5. Click **Select Installer...**.
   - A file picker opens filtered to `*.msi`, `*.exe`, and `*.ssdr`.
   - Select the file you downloaded.
6. When the upload button becomes active, click **Upload Firmware**.
   - A progress bar tracks the upload.
   - Do not close the dialog or disconnect from the radio while the upload is in progress.

#### Firmware status messages

| Message | Meaning |
|---|---|
| Update available: v*x.y.z* | A newer firmware version exists. Download the installer from flexradio.com, then click **Select Installer...**. |
| Firmware is up to date (v*x.y.z*) | No action needed. |
| (error text in red) | Upload failed. Check the file is a valid SmartSDR firmware file and try again. |

## Network (tab)

The Network tab displays radio network information and lets you configure advanced network options.

| Control | Description | Default |
|---|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each includes a clipboard copy button. | — |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers. Toggle button shows "Enabled". | — |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range 576–9000 bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. | 1450 |
| **DHCP / Static** | Switches between DHCP and Static IP modes. | — |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields. | — |
| **Apply** | Pushes the network configuration to the radio. | — |

### Changing the Network MTU

The Network MTU setting controls the maximum packet size the radio sends over the network. Lowering it prevents fragmentation when you connect through a VPN or other tunnel that reduces the available path MTU.

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match your network path MTU.
5. Click **Apply** to push the new MTU to the radio.

## GPS (tab)

The GPS tab displays GPS presence and live latitude, longitude, altitude, time, and satellite information.

| Control | Description |
|---|---|
| **GPS status** | Shows GPS presence and live position data. |

## TX (tab)

The TX tab controls TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX Band Settings.

| Control | Description | Default |
|---|---|---|
| **TX Band Settings** | Opens the dedicated per-band power/tune dialog. | — |
| **Timings (in ms)** | TX hang / delay timings. | — |
| **ACC TX:** | ACC TX delay in milliseconds. | — |
| **TX Delay:** | TX delay in milliseconds. | — |
| **RCA TX1:** | RCA TX1 delay in milliseconds. | — |
| **Timeout (sec):** | Interlock timeout in seconds (displayed in seconds, stored on radio in milliseconds). | — |
| **TX2 Delay:** | TX2 delay in milliseconds. | — |
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs. | — |
| **Max Power:** | Sets radio-level TX power cap (0–100%). | — |
| **Tune Mode:** | Selects how the tune button behaves. | — |
| **Show TX in Waterfall:** | Draws TX signal in the waterfall. | — |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | False |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | False |

### TX Timing fields

The TX timing fields control delays and timeouts for transmit operations. Note that the **Timeout** field displays in seconds for
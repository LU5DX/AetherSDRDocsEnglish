# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It provides access to radio information, network settings, GPS, TX configuration, Phone/CW settings, RX calibration, audio configuration, antenna names, filter options, transverter definitions, USB cable assignments, peripheral connections, APD sampling, theme appearance, KiwiSDR integration, callsign lookup, and FlexControl serial port setup.

## Before you start

- AetherSDR must be connected to the radio. Many fields are populated from live radio data.
- The dialog remembers its size and position between sessions. If the dialog appears off-screen, delete the `RadioSetupDialogGeometry` entry from your settings file.

## Opening Radio Setup

1. Click `Settings > Radio Setup...`.
2. The dialog opens at its last-used position and size.

# Radio tab

The Radio tab shows identifying information reported directly by the radio — serial number, hardware version, regulatory region, and licensed options. Use this page to verify what hardware and options your radio has before troubleshooting or contacting support.

## Steps

1. Click `Settings > Radio Setup...`.
2. The dialog opens on the **Radio** tab by default.
3. Read the values in the **Radio Information** group:
   - **Radio SN** — the chassis serial number.
   - **HW Version** — the hardware version string reported by the radio.
   - **Region** — the radio's regulatory region (defaults to `USA` if the radio does not report one).
   - **Options** — the licensed options active on this radio (for example, `GPS`, `PGXL`).

## What each control does

| Label                                       | Kind                                                                                                                                                                     | Behavior                                                                                                                                                                                                                                                                         |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Radio SN                                    | Indicator (read-only)                                                                                                                                                    | Chassis serial number. Includes a clipboard copy button (tray icon) next to the value.                                                                                                                                                                                           |
| HW Version                                  | Indicator (read-only)                                                                                                                                                    | Hardware version string. Includes a clipboard copy button next to the value.                                                                                                                                                                                                     |
| Region                                      | Indicator (read-only)                                                                                                                                                    | Regulatory region. Displays `USA` if the radio reports none.                                                                                                                                                                                                                     |
| Options                                     | Indicator (read-only)                                                                                                                                                    | Licensed radio options. Includes a clipboard copy button next to the value.                                                                                                                                                                                                      |
| Remote On                                   | Push button                                                                                                                                                              | Enables remote wake / remote-on.                                                                                                                                                                                                                                                 |
| FlexControl                                 | Indicator                                                                                                                                                                | Detected state of FlexControl hardware.                                                                                                                                                                                                                                          |
| multiFLEX                                   | Indicator                                                                                                                                                                | multiFLEX enabled state.                                                                                                                                                                                                                                                         |
| Model                                       | Indicator (read-only)                                                                                                                                                    | Radio model. Includes a clipboard copy button next to the value.                                                                                                                                                                                                                 |
| Nickname                                    | Text field                                                                                                                                                               | User-friendly radio nickname.                                                                                                                                                                                                                                                    |
| Callsign                                    | Text field                                                                                                                                                               | Station callsign.                                                                                                                                                                                                                                                                |
| Station Name                                | Text field                                                                                                                                                               | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`.                                                                                                                                      |
| License Info                                | Indicator                                                                                                                                                                | Displays license details from the radio (Subscription, Expiration, Radio ID, Licensed version). Each field includes a clipboard copy button.                                                                                                                                     |
| Check for Update                            | Push button                                                                                                                                                              | Queries for firmware updates.                                                                                                                                                                                                                                                    |
| Select Installer...                         | Push button                                                                                                                                                              | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress.                                                                                      |
| Upload Firmware                             | Push button                                                                                                                                                              | Starts firmware upload with progress bar and status.                                                                                                                                                                                                                             |
| Reboot Radio                                | Push button                                                                                                                                                              | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes. Only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). On SmartLink/WAN the operator must reconnect manually after the reboot. New in v26.8.4 (#4448). |
| Agent Automation (MCP):                     | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.      | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                               | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                           | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                         | Copies the access token to the clipboard.                                                                                                                                | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                       | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                        | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control   | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                              | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                          | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                          | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                             | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |

All Radio Information fields are read-only. No persisted settings keys are associated with them.
## Rebooting the radio

The **Reboot Radio** button is located in the Radio Information group.

1. Click **Reboot Radio**.
2. A confirmation dialog appears:
   - On LAN connections: "AetherSDR will disconnect and automatically reconnect once the radio finishes booting."
   - On WAN/SmartLink connections: "AetherSDR will disconnect. SmartLink/WAN sessions do not auto-reconnect today — you will need to reconnect manually once the radio finishes booting."
4. Click **OK** to confirm. The dialog closes automatically after confirming.
5. The radio reboots. AetherSDR disconnects and reconnects automatically on LAN, or waits for manual reconnection on WAN.

## Copying radio information

Each value in the Radio Information group has a small copy button to its right. Click the copy button to copy the value to the clipboard.

| Copy target | What is copied |
|---|---|
| Radio SN | The chassis serial number string. |
| HW Version | The hardware version string (with `v` prefix). |
| Region | The regulatory region string. |
| Options | The licensed options string. |
| Remote On | The "Remote On" label text. |
| FlexControl | The FlexControl state string. |
| multiFLEX | The multiFLEX state string. |
| Model | The radio model string. |
| Nickname | The nickname text. |
| Callsign | The callsign text. |
| Station Name | The station name text. |
| License Info | The full license details string. |
| Check for Update | The "Check for Update" label text. |
| Select Installer... | The file path text after browsing. |
| Upload Firmware | The "Upload Firmware" label text. |

The copy button appears as a small document icon. It is only clickable when the associated value is non-empty and not a dash placeholder. When clicked, the value is copied to the system clipboard and a brief "Copied!" popup appears near the button.

# Network tab

The Network tab shows radio network information and advanced network options.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Network** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| IP Address / Mask / MAC Address | Indicator (read-only) | Read-only network addresses. Each includes a clipboard copy button. |
| Enforce Private IP Connections: | Toggle button | Rejects non-RFC1918 peers. |
| Network MTU: | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range 576-9000 bytes, default 1450. Stored in AppSettings as `NetworkMtu`. |
| DHCP / Static | Toggle button | Switches between DHCP and Static IP modes. |
| IP Address: / Mask: / Gateway: | Text field | Static IP configuration fields. |
| Apply | Push button | Pushes the network config to the radio. |

# GPS tab

The GPS tab shows GPS presence and live lat/lon/alt/time/satellites info.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **GPS** tab.

No additional settings keys or controls beyond what is shown in the tab.

# TX tab

The TX tab shows TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow and TX Band Settings shortcut.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **TX** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| TX Band Settings | Push button | Opens the dedicated per-band power/tune dialog. |
| Timings (in ms) | Spinbox | TX hang / delay timings. |
| Interlocks - TX REQ: RCA / Accessory | Toggle button | Enables RCA and accessory interlock inputs. |
| Max Power: | Spinbox | Sets radio-level TX power cap. Range 0-100 %. |
| Tune Mode: | Combo box | Selects how the tune button behaves. |
| Show TX in Waterfall: | Toggle button | Draws TX signal in the waterfall. |
| TX Follows Active Slice | Push button | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. Stored in AppSettings as `TxFollowsActiveSlice`. |
| Active Slice Follows TX | Push button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. Stored in AppSettings as `ActiveFollowsTxSlice`. |

### TX Timings

| Field | Display unit | Radio storage unit | Behavior |
|---|---|---|---|
| ACC TX: | ms | ms | Accessory TX delay. |
| TX Delay: | ms | ms | TX keying delay. |
| RCA TX1: | ms | ms | RCA TX1 delay. |
| Timeout: | seconds | ms | Interlock timeout. Displayed in whole seconds for readability; the radio expects and stores milliseconds. |

# Phone/CW tab

The Phone/CW tab shows microphone, CW keyer, RTTY defaults.

## Steps

1. Click `Settings > Radio Setup...`.
2. Click the **Phone/CW** tab.

## What each control does

| Label | Kind | Behavior |
|---|---|---|
| Enable/Disable the Level Meter During Receive | Toggle button | Shows mic level meter even in RX. |
| Iambic: | Toggle button | Enables or disables the iambic keyer on the radio. |
| Iambic Mode: A / B | Push button | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. |
| Swap: | Toggle button | Swaps dit/dah. |
| Sideband: | Combo box | Selects CW pitch sideband (LSB | USB). |
| CWX: | Toggle button | Enables CWX macro keying. |
| Decode: RX | Toggle button | Enables the CW decode overlay on the panadapter for received CW. Stored in AppSettings as `CwDecoder` (nested JSON, rx field). New in v26.5.3: split from single CwDecodeOverlay toggle into independent RX/TX toggles. |
| Decode: TX | Toggle button | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Stored in AppSettings as `
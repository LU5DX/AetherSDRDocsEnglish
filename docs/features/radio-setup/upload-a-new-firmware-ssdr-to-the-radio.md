# Radio Setup Dialog

This page documents the Radio Setup dialog, the master per-radio configuration window in AetherSDR. It covers radio information, network settings, GPS, transmit, Phone/CW, receive, audio, filters, transverters, USB cables, peripheral connections, SmartLink certificate management, and more.

## Opening the Radio Setup dialog

1. Open AetherSDR and connect to your radio.
2. Click **Settings > Radio Setup...**.

The dialog opens as a persistent window. Many read-only values (serial number, hardware version, options, model, subscription, IP, MAC, firmware version) include a clipboard copy button next to the label for easy sharing with support.

## Search

The dialog includes a search box at the top. As you type, matching pages and controls are highlighted and non-matching rows are hidden. The search is case-insensitive and matches keywords that describe each control.

## Radio tab

The Radio tab contains radio information, identification, license info, and firmware update controls.

| Control | Kind | Behavior |
|---|---|---|
| **Radio SN** | Indicator | Chassis serial number (read-only). Shows the chassis serial if available, otherwise the radio serial. Displays an em dash (`—`) if no value is reported. A small copy button appears next to the value on hover or focus; click it to copy the serial number to the clipboard. |
| **Region** | Indicator | Radio regulatory region (default: USA). |
| **HW Version** | Indicator | Hardware version string. Displays an em dash (`—`) if empty, prefixed with `v` if no leading `v`. A copy button is available. |
| **Model** | Indicator | Radio model. A copy button is available. |
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as `client station <name>`. |
| **Remote On** | Button | Enables remote wake / remote-on. |
| **Options** | Indicator | Shows licensed radio options. Displays the radio's reported option string or, if empty, inserts sensible defaults (e.g. `GPS, PGXL` if the radio has an amplifier, otherwise `GPS`). A copy button is available. |
| **FlexControl** | Indicator | Detected state of FlexControl hardware. |
| **multiFLEX** | Indicator | multiFLEX enabled state. |
| **License Info** | Indicator | Displays license details (Subscription / Expiration / Radio ID / Licensed version) from the radio. Each field includes a clipboard copy button. |
| **Check for Update** | Button | Queries for available firmware updates. If an update is found, the status area shows the available version and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it. |
| **Select Installer...** | Button | Opens a file dialog that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. A status message is shown while the file is being prepared. Renamed from **Browse .ssdr...** in v26.5.3. |
| **Upload Firmware** | Button | Starts the upload using the file staged by **Select Installer...**. A progress bar and status text appear below and update as the transfer proceeds. |
| **Reboot Radio** | Button | Reboots the connected radio with a confirmation dialog. AetherSDR disconnects and (on LAN) auto-reconnects once booting finishes. On SmartLink/WAN connections, you must reconnect manually. The button is only enabled when connected and the backend supports a client reboot (e.g. HL2 is RX-only so the button is disabled). New in v26.8.4 (#4448). |

### Firmware status

Below the **Upload Firmware** button, a status area appears when a firmware upload begins. It shows progress and result text as the transfer proceeds.

## Network tab

The Network tab contains radio network information and advanced network options.

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator | Read-only network addresses. Each includes a clipboard copy button. |
| **Enforce Private IP Connections:** | Toggle | Rejects non-RFC1918 peers. Defaults to Enabled. |
| **Agent Automation (MCP):** | Toggle | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The `AETHER_AUTOMATION` launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless `AETHER_AUTOMATION_ALLOW_TX` is set. |
| **Access Token:** | Text field | Read-only display of the MCP access token; paste it into the assistant's `AETHER_MCP_TOKEN` environment variable. Stored in the OS secret store. New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder `(loading…)` until the keychain read lands. |
| **Copy (Access Token)** | Button | Copies the access token to the clipboard. New in v26.8.4. |
| **Rotate (Access Token)** | Button | Generates a new token and applies it immediately, locking out any client still using the old one. New in v26.8.4. |
| **Allow TX via MCP: Enable transmit control** | Checkbox | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation. New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by `AETHER_AUTOMATION_ALLOW_TX` (force on) and `AETHER_AUTOMATION_NO_TX` (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| **Observe only: Read-only (block all driving)** | Checkbox | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. `AETHER_AUTOMATION_READONLY` launch variable pins it on for headless/CI runs. |
| **VITA-49 RX buffer:** | Slider | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped. New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at `net.core.rmem_max`; a live **granted:** label shows what the kernel actually granted. |
| **granted: (VITA-49 RX buffer)** | Indicator | Shows the buffer size the kernel actually granted (vs the requested preset). New in v26.8.4. Shows `(applies on connect)` when no connection is active. |
| **Network MTU:** | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes (576-9000). Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. |
| **DHCP / Static** | Toggle | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text field | Static IP configuration fields. |
| **Apply** | Button | Pushes the network config to the radio. |

## Calibration tab

The Calibration tab provides manual frequency calibration for radios that cannot calibrate their own oscillator (such as HL2). It is hidden unless the connected radio's backend reports that it supports host-side frequency calibration.

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | Frequency used for manual calibration. |
| **Start** | Button | Starts the frequency calibration sweep. |
| **Freq Offset (ppb):** | Spinbox | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference source. Options shown depend on hardware installed (Auto, TCXO, GPSDO, External). Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

The calibration values are re-read whenever the dialog is shown or the connection state changes, so a Trim press can never commit a different radio's calibration number.

## GPS tab

| Control | Kind | Behavior |
|---|---|---|
| GPS info | Indicator | GPS presence and live lat/lon/alt/time/satellites info. |

## TX tab

The TX tab contains transmit timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and a TX Band Settings shortcut.

| Control | Kind | Behavior |
|---|---|---|
| **TX Band Settings** | Button | Opens the dedicated per-band power/tune dialog. |
| **Timings (in ms)** | Spinbox | TX hang / delay timings. |
| **ACC TX:** | Text field | ACC transmit delay in milliseconds. Range 0-5000 ms. |
| **TX Delay:** | Text field | TX delay in milliseconds. Range 0-5000 ms. |
| **RCA TX1:** | Text field | RCA TX1 delay in milliseconds. Range 0-5000 ms. |
| **Timeout (sec):** | Text field | Interlock timeout in seconds. The radio stores this value in milliseconds internally. Range 0-3600 seconds. |
| **TX2:** | Text field | TX2 delay in milliseconds. Range 0-5000 ms. |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle | Enables RCA and accessory interlock inputs. |
| **Max Power:** | Spinbox | Sets radio-level TX power cap (0-100%). |
| **Tune Mode:** | Combo box | Selects how the tune button behaves. |
| **Show TX in Waterfall:** | Toggle | Draws TX signal in the waterfall. |
| **TX Follows Active Slice** | Button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored in AppSettings as `TxFollowsActiveSlice`. |
| **Active Slice Follows TX** | Button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored in AppSettings as `ActiveFollowsTxSlice`. |

## Phone/CW tab

The Phone/CW tab contains microphone, CW keyer, and RTTY defaults.

| Control | Kind | Behavior |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle | Shows mic level meter even in RX. |
| **Iambic:** | Toggle | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Button | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. Default is A. |
| **Swap:** | Toggle | Swaps dit/dah. |
| **Sideband:** | Combo box | Selects CW pitch sideband (LSB | USB). |
| **CWX:** | Toggle | Enables CWX macro keying. |
| **Decode: RX** | Toggle | Enables the CW decode overlay on the panadapter for received CW. Default is True. Stored in AppSettings as nested JSON under `CwDecoder` (rx field). New in v26.5.3: split from single CwDecodeOverlay toggle into independent RX/TX toggles. Legacy `CwDecodeOverlay` key auto-migrated on first read. |
| **Decode: TX** | Toggle | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Default is False. Stored in AppSettings as nested JSON under `CwDecoder` (tx field). New in v26.5.3 (#2417). |
| **RTTY Mark Default:** | Spinbox | Default RTTY mark frequency. |

## RX tab

The RX tab contains GPSDO frequency offset calibration and 10 MHz reference source settings.

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz):** | Spinbox | Frequency used for manual calibration. |
| **Start** | Button | Starts the frequency calibration sweep. |
| **Freq Offset (ppb):** | Spinbox | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference source. Options shown depend on hardware installed (Auto, TCXO, GPSDO, External). Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

## Antennas tab

The Antennas tab provides per-port antenna display-name editing for the radio. It lets you assign custom names to each antenna port (ANT1, ANT2, XVTA
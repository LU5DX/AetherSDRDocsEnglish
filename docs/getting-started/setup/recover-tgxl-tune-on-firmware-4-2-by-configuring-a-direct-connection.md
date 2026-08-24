# Radio Setup

The Radio Setup dialog (`Settings > Radio Setup...`) is the master per-radio configuration window. It contains tabs for radio information, network, GPS, calibration, TX, Phone/CW, RX, antennas, audio, filters, XVTR, USB cables, peripherals, APD, themes, SmartLink certificate management, (optionally) FlexControl serial, KiwiSDR public receiver, and automation/QRZ lookup settings.

The dialog remembers its size and position between sessions.

## Radio tab

The Radio tab displays radio identification, license information and firmware update controls.

**Scroll support:** In v26.6.3 the Radio tab (and other tabs with stacked content groups) was wrapped in a vertical QScrollArea. This prevents the dialog from exceeding the screen height on small or high-DPI displays. The scrollbar is hidden when content already fits.

| Control                                     | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                         | Default                                                                                                                                                                                                                                                                          |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Radio SN                                    | Chassis serial number (read-only). Includes a clipboard copy button (tray icon) next to the value.                                                                                                                                                                                                                                                                                                                                               | —                                                                                                                                                                                                                                                                                |
| Region                                      | Radio regulatory region (read-only).                                                                                                                                                                                                                                                                                                                                                                                                             | USA                                                                                                                                                                                                                                                                              |
| HW Version                                  | Hardware version string. Includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                                                                                                                                     | —                                                                                                                                                                                                                                                                                |
| Remote On                                   | Enables remote wake / remote-on.                                                                                                                                                                                                                                                                                                                                                                                                                 | —                                                                                                                                                                                                                                                                                |
| Options                                     | Shows licensed radio options. Includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                                                                                                                                | —                                                                                                                                                                                                                                                                                |
| FlexControl                                 | Detected state of FlexControl hardware (read-only).                                                                                                                                                                                                                                                                                                                                                                                              | —                                                                                                                                                                                                                                                                                |
| multiFLEX                                   | multiFLEX enabled state (read-only).                                                                                                                                                                                                                                                                                                                                                                                                             | —                                                                                                                                                                                                                                                                                |
| Model                                       | Radio model. Includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                                                                                                                                                 | —                                                                                                                                                                                                                                                                                |
| Nickname                                    | User-friendly radio nickname.                                                                                                                                                                                                                                                                                                                                                                                                                    | —                                                                                                                                                                                                                                                                                |
| Callsign                                    | Station callsign.                                                                                                                                                                                                                                                                                                                                                                                                                                | —                                                                                                                                                                                                                                                                                |
| Station Name                                | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings. Sent to radio as 'client station <name>'.                                                                                                                                                                                                                                                                             | —                                                                                                                                                                                                                                                                                |
| License Info                                | Displays license details from the radio (Subscription / Expiration / Radio ID / Licensed version). Each field includes a clipboard copy button next to the value.                                                                                                                                                                                                                                                                                | —                                                                                                                                                                                                                                                                                |
| Check for Update                            | Queries for firmware updates.                                                                                                                                                                                                                                                                                                                                                                                                                    | —                                                                                                                                                                                                                                                                                |
| Upload Firmware                             | Starts firmware upload with progress bar and status.                                                                                                                                                                                                                                                                                                                                                                                             | —                                                                                                                                                                                                                                                                                |
| Select Installer...                         | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress.                                                                                                                                                                                                                                                      | —                                                                                                                                                                                                                                                                                |
| Reboot Radio                                | Reboots the connected radio. Opens a confirmation dialog before sending the reboot command. When connected via SmartLink/WAN, auto-reconnect is not supported after reboot; reconnect manually after the radio finishes booting. On LAN, AetherSDR automatically reconnects once the radio comes back online. The dialog closes after reboot. Disabled when the radio is disconnected; enabled/disabled automatically based on connection state. | —                                                                                                                                                                                                                                                                                |
| Agent Automation (MCP):                     | Enables the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in.                                                                                                                                                                                                                                                                              | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The AETHER_AUTOMATION launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless AETHER_AUTOMATION_ALLOW_TX is set. |
| Access Token:                               | Read-only display of the MCP access token; paste it into the assistant's AETHER_MCP_TOKEN environment variable. Stored in the OS secret store.                                                                                                                                                                                                                                                                                                   | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands.                                                                                                                                   |
| Copy (Access Token)                         | Copies the access token to the clipboard.                                                                                                                                                                                                                                                                                                                                                                                                        | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Rotate (Access Token)                       | Generates a new token and applies it immediately, locking out any client still using the old one.                                                                                                                                                                                                                                                                                                                                                | New in v26.8.4.                                                                                                                                                                                                                                                                  |
| Allow TX via MCP: Enable transmit control   | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.                                                                                                                                                                                                                                                                                                      | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by AETHER_AUTOMATION_ALLOW_TX (force on) and AETHER_AUTOMATION_NO_TX (pinned off). A force-unkey watchdog limits bridge-originated TX.                                                                 |
| Observe only: Read-only (block all driving) | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused.                                                                                                                                                                                                                                                                                                                  | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. AETHER_AUTOMATION_READONLY launch variable pins it on for headless/CI runs.                                                                                                                           |
| VITA-49 RX buffer:                          | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped.                                                                                                                                                                                                                                                                         | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at net.core.rmem_max; a live 'granted: <size>' label shows what the kernel actually granted.                                                                                                           |
| granted: (VITA-49 RX buffer)                | Shows the buffer size the kernel actually granted (vs the requested preset).                                                                                                                                                                                                                                                                                                                                                                     | New in v26.8.4. Shows '(applies on connect)' when no connection is active.                                                                                                                                                                                                       |

### Copy buttons

Each read-only indicator on the Radio tab (Radio SN, Region, HW Version, Options, FlexControl, multiFLEX, Model, License Info fields) includes a small copy button that appears on hover. Click the button to copy the displayed value to the clipboard.

### Summary area

The Radio tab also shows:
- **Firmware status** — Empty until a firmware upload begins, then displays progress and result text.
- **License Info** — Subscription status, expiration date, Radio ID, and licensed version.

## Network tab

The Network tab displays radio network information and advanced network options.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| IP Address / Mask / MAC Address | Read-only network addresses. Each includes a clipboard copy button. | — | — |
| Enforce Private IP Connections: | Rejects non-RFC1918 peers. | — | — |
| Network MTU: | Sets maximum outgoing VITA-49 UDP packet size in bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. | 1450 | `NetworkMtu` |
| DHCP / Static | Switches between DHCP and Static IP modes. | — | — |
| IP Address: / Mask: / Gateway: | Static IP configuration fields. | — | — |
| Apply | Pushes the network config to the radio. | — | — |

## GPS tab

The GPS tab shows GPS presence and live lat/lon/alt/time/satellites info.

## Calibration tab

The Calibration tab provides manual frequency calibration for radios that cannot calibrate their own oscillator (such as the HL2). This tab is only shown when the connected radio's backend reports that host-side frequency calibration is supported (`hostFrequencyCalibration` capability).

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Calibration controls | Manual frequency calibration controls for radios that cannot self-calibrate. | — | — |

**Note:** This tab is hidden for FlexRadio devices, which perform their own hardware calibration via the RX tab. The tab is re-evaluated on connection state changes, so switching to a different radio refreshes the calibration values shown. Calibration data is also re-read whenever the dialog is shown, to pick up changes made while the dialog was closed (for example, via a `freqcal` bridge call).

## TX tab

The TX tab configures TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow and TX Band Settings.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| TX Band Settings | Opens the dedicated per-band power/tune dialog. | — | — |
| Timings (in ms) | TX hang / delay timings. | — | — |
| Interlocks - TX REQ: RCA / Accessory | Enables RCA and accessory interlock inputs. | — | — |
| Max Power: | Sets radio-level TX power cap (0-100%). | — | — |
| Tune Mode: | Selects how the tune button behaves. | — | — |
| Show TX in Waterfall: | Draws TX signal in the waterfall. | — | — |
| TX Follows Active Slice | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. | False | `TxFollowsActiveSlice` |
| Active Slice Follows TX | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. | False | `ActiveFollowsTxSlice` |

**Note on timeout field:** The "Timeout" field is labeled **Timeout (sec)** and displays the value in seconds. Internally the radio stores it in milliseconds; the setting is converted automatically when sent.

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Enable/Disable the Level Meter During Receive | Shows mic level meter even in RX. | — | — |
| Iambic: | Enables or disables the iambic keyer on the radio. | — | — |
| Iambic Mode: A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | A | — |
| Swap: | Swaps dit/dah. | — | — |
| Sideband: | Selects CW pitch sideband (LSB | USB). | — | — |
| CWX: | Enables CWX macro keying. | — | — |
| Decode: RX | Enables the CW decode overlay on the panadapter for received CW. | True | `CwDecoder` (nested JSON, `rx` field) |
| Decode: TX | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. | False | `CwDecoder` (nested JSON, `tx` field) |
| RTTY Mark Default: | Default RTTY mark frequency. | — | — |

**Note:** In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. These also drive the local software iambic keyer (IambicKeyer) which mirrors the radio's iambic state for sub-5 ms sidetone.

Since v26.5.3, the CW decode overlay setting is split into two independent toggles: **Decode: RX** and **Decode: TX**. The settings are persisted as a nested JSON blob under `CwDecoder` with `rx` and `tx` fields. The legacy `CwDecodeOverlay` key is auto-migrated on first read.

## RX tab

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source configuration.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Cal Frequency (MHz): | Frequency used for manual calibration. | — | — |
| Start | Starts the frequency calibration sweep. | — | — |
| Freq Offset (ppb): | Manual frequency offset in ppb. | — | — |
| 10 MHz Reference Source: | Selects oscillator reference source. Options shown depend on hardware installed (TCXO/GPSDO/External). | Auto | — |

### 10 MHz reference source display

The `10 MHz Reference Source:` combo box on the `RX` tab is populated dynamically based on the hardware present in the connected radio and the current oscillator setting and state reported by the radio. The following sources may appear:

| Entry | When shown |
|---|---|
| Auto | Always shown. |
| TCXO | Shown when the radio reports a TCXO is present, or when the current or reported state refers to TCXO. |
| GPSDO | Shown when the radio reports a GPSDO is present, or when the current or reported state refers to GPSDO. |
| External 10 MHz | Shown when the radio reports an external reference is present or active, or when the current or reported state refers to external. |

The combo selects the saved oscillator setting automatically when the dialog opens. If the saved setting is not in the list
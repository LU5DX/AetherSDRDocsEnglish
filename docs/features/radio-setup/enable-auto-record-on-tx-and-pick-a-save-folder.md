# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It is opened from `Settings > Radio Setup...` and requires an active radio connection.

## Dialog Layout

The dialog window uses the persistent dialog framework, saving and restoring its geometry automatically between sessions. The main content area contains a tabbed interface with the following tabs:

- **Radio** — Radio information, identification, license info and firmware update
- **Network** — Radio network information and advanced network options
- **GPS** — GPS presence and live lat/lon/alt/time/satellites info
- **TX** — TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow and TX Band Settings shortcut
- **Phone/CW** — Microphone, CW keyer, RTTY defaults
- **RX** — GPSDO frequency offset calibration and 10 MHz reference source
- **Calibration** — Manual host-side frequency calibration (HL2 and other backends that cannot self-calibrate; hidden for radios with hostFrequencyCalibration capability)
- **Antennas** — Antenna name configuration
- **Audio** — Radio audio outputs, compression, PC devices, boost, buffer, recording and NVIDIA BNR container
- **Filters** — Low-latency / Sharp filter options per bandwidth
- **XVTR** — Per-transverter configuration
- **USB Cables** — Assigns USB serial adapters to CAT, BCD, bit, and PTT cable types
- **Peripherals** — External devices manual IP connection (TGXL, PGXL, Antenna Genius)
- **APD** — External Adaptive Pre-Distortion sampler configuration (FLEX-8x00 with SmartSDR 4.2.18+ only)
- **Themes** — UI customization including slice colors
- **SmartLink** — Pinned SmartLink TLS certificate management
- **Serial** — FlexControl serial port configuration and paddle/button mapping
- **KiwiSDR** — KiwiSDR receiver configuration, custom nickname, and public/private receiver management

Several tabs (Radio, Themes, Audio, Filters, Peripherals) are wrapped in a scroll area so that their content remains accessible on small or high-DPI screens. The scrollbar appears automatically when the content exceeds the dialog's visible height; it hides when all content fits without scrolling.

The dialog geometry (position and size) is saved automatically when you close the dialog and restored on next open. The dialog inherits from `PersistentDialog` which handles geometry persistence under the key `RadioSetupDialogGeometry`.

---

## Radio Tab

The **Radio** tab displays radio information, identification, license details, and firmware update controls.

### Radio Information

The following indicators are read-only and show information retrieved from the connected radio:

| Control | What it shows |
|---|---|
| **Radio SN** | Chassis serial number |
| **Region** | Radio regulatory region (e.g., USA) |
| **HW Version** | Hardware version string |
| **Model** | Radio model |
| **Options** | Licensed radio options |
| **FlexControl** | Detected state of FlexControl hardware |
| **multiFLEX** | multiFLEX enabled state |
| **License Info** | Subscription status, expiration date, radio ID, and licensed version |

Each read-only field has a copy button (clipboard icon) that appears on hover or focus. Click the copy button to copy that field's value to the system clipboard. A brief popup confirms the copy action.

### User Configuration Fields

| Control | What it does | Setting Key |
|---|---|---|
| **Nickname** | User-friendly radio nickname | — |
| **Callsign** | Station callsign | — |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. | `StationName` |
| **Remote On** | Enables remote wake / remote-on | — |

### Reboot Radio

| Control | What it does |
|---|---|
| **Reboot Radio** | Sends a reboot command to the connected radio. A confirmation dialog appears before rebooting. The button is disabled when the radio is disconnected. |

Click **Reboot Radio** to restart the connected radio. A confirmation dialog appears:

- For LAN connections: "AetherSDR will disconnect and automatically reconnect once the radio finishes booting."
- For SmartLink/WAN connections: "AetherSDR will disconnect. SmartLink/WAN sessions do not auto-reconnect today — you will need to reconnect manually once the radio finishes booting."

Click **OK** to confirm. The dialog closes, and the radio reboots.

The button is enabled only when the radio is connected and the backend supports a client reboot. For example, HL2 is RX-only so the button is disabled. It disables automatically on disconnect and re-enables on reconnect.

### Firmware Update

The **Radio** tab includes firmware update controls. For details, see the [Firmware Update](#firmware-update-radio-tab) section below.

---

## Network Tab

The **Network** tab displays network information and allows configuration of the radio's network settings.

### Network Information

The following indicators are read-only:

| Control | What it shows |
|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses |

### Network Configuration

| Control | What it does | Default | Range | Setting Key |
|---|---|---|---|---|
| **DHCP / Static** | Switches between DHCP and Static IP modes | — | — | — |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields | — | — | — |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers | — | — | — |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes | 1450 | 576-9000 bytes | `NetworkMtu` |
| **Apply** | Pushes the network config to the radio | — | — | — |

> **Note:** The default MTU of 1450 is safe for most VPN/SD-WAN tunnels. This setting is stored in AppSettings.

### Automation Bridge (MCP)

The **Network** tab includes controls for the in-app automation bridge that lets an AI coding assistant (via the MCP server) introspect and drive the running app.

| Control | What it does | Default | Notes |
|---|---|---|---|
| **Agent Automation (MCP):** | Enables the in-app automation bridge | Disabled | New in v26.8.4 (#3646). Persisted via AutomationBridgeSettings. The `AETHER_AUTOMATION` launch environment variable force-enables the bridge regardless of this toggle and disables the control in the UI. Transmit-keying stays blocked unless `AETHER_AUTOMATION_ALLOW_TX` is set. |
| **Access Token:** | Read-only display of the MCP access token; paste it into the assistant's `AETHER_MCP_TOKEN` environment variable. Stored in the OS secret store. | (none) | New in v26.8.4. Auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder '(loading…)' until the keychain read lands. |
| **Copy (Access Token)** | Copies the access token to the clipboard | — | New in v26.8.4. |
| **Rotate (Access Token)** | Generates a new token and applies it immediately, locking out any client still using the old one | — | New in v26.8.4. |
| **Allow TX via MCP: Enable transmit control** | Lets an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX) | False | New in v26.8.4. Enforced in the bridge; no client can flip it. Overridden by `AETHER_AUTOMATION_ALLOW_TX` (force on) and `AETHER_AUTOMATION_NO_TX` (pinned off). A force-unkey watchdog limits bridge-originated TX. |
| **Observe only: Read-only (block all driving)** | Makes the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused | False | New in v26.8.4 (#4188). Enforced in the app, so a client cannot bypass it. `AETHER_AUTOMATION_READONLY` launch variable pins it on for headless/CI runs. |

### VITA-49 Receive Buffer

| Control | What it does | Default | Range | Notes |
|---|---|---|---|---|
| **VITA-49 RX buffer:** | Snap-to-preset slider setting the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger absorbs panadapter/waterfall bursts so packets aren't dropped | 4 MB | 0.25-4 MB (presets) | New in v26.8.4 (#3810). Presets 256 KB to 4 MB. The system caps the grant at `net.core.rmem_max`; a live 'granted: <size>' label shows what the kernel actually granted. |
| **granted: (VITA-49 RX buffer)** | Shows the buffer size the kernel actually granted (vs the requested preset) | — | — | New in v26.8.4. Shows '(applies on connect)' when no connection is active. |

---

## GPS Tab

The **GPS** tab displays GPS presence and live information when a GPS receiver is installed.

| Control | What it shows |
|---|---|
| **GPS** | Live lat/lon/alt/time/satellites information |

---

## TX Tab

The **TX** tab configures transmit timings, interlocks, power, tune mode, and slice/TX follow behavior.

### TX Band Settings

| Control | What it does |
|---|---|
| **TX Band Settings** | Opens the dedicated per-band power/tune dialog |

### TX Configuration

| Control | What it does | Default | Range |
|---|---|---|---|
| **Timings** | TX hang / delay timings. Includes ACC TX, TX Delay, RCA TX1, and Timeout fields. | — | — |
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs | — | — |
| **Max Power:** | Sets radio-level TX power cap | — | 0-100 % |
| **Tune Mode:** | Selects how the tune button behaves | — | — |
| **Show TX in Waterfall:** | Draws TX signal in the waterfall | — | — |

### Timing Fields

The **Timings** section includes four fields:

| Control | What it does | Notes |
|---|---|---|
| **ACC TX:** | ACC transmit delay in milliseconds | — |
| **TX Delay:** | Transmit delay in milliseconds | — |
| **RCA TX1:** | RCA TX1 delay in milliseconds | — |
| **Timeout (sec):** | Interlock timeout displayed in seconds. The radio internally stores this value in milliseconds. | Enter the value in seconds; the dialog converts to milliseconds before sending to the radio. |

> **Note:** The Timeout field previously displayed minutes but now shows seconds for finer resolution on short-cycle TOT settings.

### Slice/TX Follow

| Control | What it does | Default | Setting Key |
|---|---|---|---|
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. | False | `TxFollowsActiveSlice` |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. | False | `ActiveFollowsTxSlice` |

---

## Phone/CW Tab

The **Phone/CW** tab configures microphone, CW keyer, and RTTY defaults.

| Control | What it does | Default | Range | Setting Key |
|---|---|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX | — | — | — |
| **Iambic:** | Enables or disables the iambic keyer on the radio | — | Enabled / Disabled | — |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | A | A / B | — |
| **Swap:** | Swaps dit/dah | — | — | — |
| **Sideband:** | Selects CW pitch sideband | — | LSB / USB | — |
| **CWX:** | Enables CWX macro keying | — | — | — |
| **Decode: RX** | Enables the CW decode overlay on the panadapter for received CW | True | — | `CwDecoder` (nested JSON, `rx` field) |
| **Decode: TX** | Decodes the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing | False | — | `CwDecoder` (nested JSON, `tx` field) |
| **RTTY Mark Default:** | Default RTTY mark frequency | — | — | — |

> **Note:** Mode A and Mode B buttons are available beside the Iambic Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. These also drive the local software iambic keyer (IambicKeyer) which mirrors the radio's iambic state for sub-5 ms sidetone.

> **Note:** The **Decode: RX** and **Decode: TX** toggles were split from a single `CwDecodeOverlay` toggle in v26.5.3. They persist as a nested JSON blob under `CwDecoder` with `rx` and `tx` fields. The legacy `CwDecode
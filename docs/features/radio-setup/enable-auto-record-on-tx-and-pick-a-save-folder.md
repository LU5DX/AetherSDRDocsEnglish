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

The button is enabled only when the radio is connected. It disables automatically on disconnect and re-enables on reconnect.

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
| **Decode:** | Enables the CW decode overlay on the panadapter | True | — | `CwDecodeOverlay` |
| **RTTY Mark Default:** | Default RTTY mark frequency | — | — | — |

> **Note:** Mode A and Mode B buttons are available beside the Iambic Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. These also drive the local software iambic keyer (IambicKeyer) which mirrors the radio's iambic state for sub-5 ms sidetone.

---

## RX Tab

The **RX** tab provides manual frequency offset calibration and 10 MHz reference source selection.

The calibration controls are available regardless of whether a GPSDO is installed. When a GPSDO is present the status label reads "GPSDO installed. Manual frequency offset calibration available." (green). Without a GPSDO the label reads "Manual frequency offset calibration available." (amber).

### Calibration Controls

| Control | What it does |
|---|---|
| **Cal Frequency (MHz):** | Enter the known reference frequency in MHz. The value is sent to the radio as `radio set cal_freq=<value>` when you finish editing the field. |
| **Start** | Resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`), then starts the calibration sweep. The button label changes to **Busy** and is disabled while calibration is running. A status label beside the button reports progress. |
| **Freq Offset (ppb):** | Manual frequency offset in parts per billion. |

### 10 MHz Reference Source

| Control | What it does | Default | Range |
|---|---|---|---|
| **10 MHz Reference Source:** | Selects oscillator reference source. Options shown depend on hardware installed (TCXO/GPSDO/External). Lock status (Locked / Unlocked) is shown alongside the combo and updates live. | Auto | Auto / TCXO / GPSDO / External |

The lock status label beside **10 MHz Reference Source:** shows richer information. The label text and color update live as the radio reports oscillator state changes.

**Label text format:**

| Condition | Example text |
|---|---|
| Auto mode resolving to a source | `Auto -> GPSDO Locked` |
| Setting overridden by radio | `TCXO -> GPSDO Locked` |
| Source matches setting | `GPSDO Locked` |
| External selected but not detected | `External 10 MHz Unlocked (not detected)` |
| Waiting for first status report | `Waiting for oscillator status` |

**Label color:**

| State | Color |
|---|---|
| Locked | Green |
| Unlocked | Red |
| No status received yet | Grey/blue |

The **10 MHz Reference Source:** combo box populates dynamically based on the hardware the radio reports as present, the current setting, and the active oscillator state. The **External** entry is labeled **External 10 MHz**. If the radio sends the value `ext` it is treated as equivalent to `external`.

### Starting a Calibration

1. Click the **RX** tab in Radio Setup.
2. Enter the known reference frequency in **Cal Frequency (MHz):**.
3. Click **Start**. The button shows **Busy** while the sweep runs. Watch the status label for progress and result.
4. When calibration completes, the button re-enables.

---

## Antennas Tab

The **Antennas** tab allows you to configure user-friendly names for each antenna port on the radio, replacing the default port labels (ANT1, ANT2, XVTA, XVTB, etc.) with custom identifiers that appear throughout the AetherSDR interface.

| Control | What it does |
|---|---|
| **Antenna name fields** | One text field per antenna port. Enter a custom name (e.g., "HF Vertical", "6M Yagi", "160M Loop"). Names are sent to the radio and persisted in the radio's configuration. |

**To set an antenna name:**

1. Click the **Antennas** tab in Radio Setup.
2. For each antenna port, type the desired name in the corresponding text field.
3. Press Enter or tab to the next field to commit the name to the radio.

---

## Audio Tab

The **Audio** tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

| Control | What it does | Default | Range | Setting Key |
|---|---|---|---|---|
| **Line Out:** | Line-out gain slider | — | — | — |
| **Mute (Line Out)** | Mutes line-out | — | — | — |
| **Headphone:** | Headphone gain slider | — | — | — |
| **Mute (Headphone)** | Mutes headphone | — | — | — |
| **Front Speaker: / Mute** | Mutes front speaker (model-specific) | — | — | — |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus
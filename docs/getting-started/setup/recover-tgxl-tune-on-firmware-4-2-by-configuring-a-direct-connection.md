# Radio Setup

The Radio Setup dialog (`Settings > Radio Setup...`) is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, Phone/CW, RX, audio, filters, XVTR, USB cables, peripherals and (optionally) FlexControl serial.

## Radio tab

The Radio tab displays radio identification, license information and firmware update controls.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Radio SN | Chassis serial number (read-only). | — | — |
| Region | Radio regulatory region (read-only). | USA | — |
| HW Version | Hardware version string (read-only). | — | — |
| Remote On | Enables remote wake / remote-on. | — | — |
| Options | Shows licensed radio options (read-only). | — | — |
| FlexControl | Detected state of FlexControl hardware (read-only). | — | — |
| multiFLEX | multiFLEX enabled state (read-only). | — | — |
| Model | Radio model (read-only). | — | — |
| Nickname | User-friendly radio nickname. | — | — |
| Callsign | Station callsign. | — | — |
| Station Name | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. | — | `StationName` |
| License Info | Displays license details from the radio (Subscription / Expiration / Radio ID / Licensed version). | — | — |
| Check for Update | Queries for firmware updates. | — | — |
| Browse .ssdr... | Chooses a firmware image file. | — | — |
| Upload Firmware | Starts firmware upload with progress bar and status. | — | — |

### Summary area

The Radio tab also shows:
- **Firmware status** — Empty until a firmware upload begins, then displays progress and result text.
- **License Info** — Subscription status, expiration date, Radio ID, and licensed version.

## Network tab

The Network tab displays radio network information and advanced network options.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| IP Address / Mask / MAC Address | Read-only network addresses. | — | — |
| Enforce Private IP Connections: | Rejects non-RFC1918 peers. | — | — |
| Network MTU: | Sets maximum outgoing VITA-49 UDP packet size in bytes. | 1450 | `NetworkMtu` |
| DHCP / Static | Switches between DHCP and Static IP modes. | — | — |
| IP Address: / Mask: / Gateway: | Static IP configuration fields. | — | — |
| Apply | Pushes the network config to the radio. | — | — |

**Note:** The default MTU of 1450 is safe for most VPN/SD-WAN tunnels.

## GPS tab

The GPS tab shows GPS presence and live lat/lon/alt/time/satellites info.

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

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Enable/Disable the Level Meter During Receive | Shows mic level meter even in RX. | — | — |
| Iambic: | Enables or disables the iambic keyer on the radio. | — | — |
| Iambic Mode: A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. | A | — |
| Swap: | Swaps dit/dah. | — | — |
| Sideband: | Selects CW pitch sideband (LSB | USB). | — | — |
| CWX: | Enables CWX macro keying. | — | — |
| Decode: | Enables the CW decode overlay on the panadapter. | True | `CwDecodeOverlay` |
| RTTY Mark Default: | Default RTTY mark frequency. | — | — |

**Note:** In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle. Mode A = Curtis A; Mode B = Curtis B. These also drive the new local software iambic keyer (IambicKeyer) which mirrors the radio's iambic state for sub-5 ms sidetone.

## RX tab

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source configuration.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Cal Frequency (MHz): | Frequency used for manual calibration. | — | — |
| Start | Starts the frequency calibration sweep. | — | — |
| Freq Offset (ppb): | Manual frequency offset in ppb. | — | — |
| 10 MHz Reference Source: | Selects oscillator reference source. Options shown depend on hardware installed (TCXO/GPSDO/External). | Auto | — |

### 10 MHz reference source display (v0.9.7)

The `10 MHz Reference Source:` combo box on the `RX` tab was updated in v0.9.7. The list of available sources and the lock-status label next to it now behave differently from earlier releases.

#### Source combo box

The combo box is now populated dynamically based on the hardware present in the connected radio and the current oscillator setting and state reported by the radio. The following sources may appear:

| Entry | When shown |
|---|---|
| Auto | Always shown. |
| TCXO | Shown when the radio reports a TCXO is present, or when the current or reported state refers to TCXO. |
| GPSDO | Shown when the radio reports a GPSDO is present, or when the current or reported state refers to GPSDO. |
| External 10 MHz | Shown when the radio reports an external reference is present or active, or when the current or reported state refers to external. Note: the label changed from "External" to "External 10 MHz" in v0.9.7. |

The combo selects the saved oscillator setting automatically when the dialog opens. If the saved setting is not in the list, the current reported state is tried; if that is also absent, Auto is selected.

#### Lock status label

The status label next to the combo box was updated to show richer information:

- When Auto is selected and the radio has switched to a specific source, the label reads **Auto -> \<source\>** followed by **Locked** or **Unlocked**.
- When the requested source differs from the active source, the label reads **\<requested\> -> \<active\>** followed by **Locked** or **Unlocked**.
- When the requested and active sources match, the label reads **\<source\> Locked** or **\<source\> Unlocked**.
- When External 10 MHz is selected but no external reference is detected, the label appends **(not detected)**.
- While waiting for the radio to report oscillator status, the label reads **Waiting for oscillator status**.

The label color is green when locked and red when unlocked. Before the radio reports any oscillator state, the label is shown in a neutral gray.

## Audio tab

The Audio tab configures radio audio outputs, compression, PC devices, boost, buffer, recording and NVIDIA BNR container.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Line Out: | Line-out gain slider. | — | — |
| Mute (Line Out) | Mutes line-out. | — | — |
| Headphone: | Headphone gain slider. | — | — |
| Mute (Headphone) | Mutes headphone. | — | — |
| Front Speaker: / Mute | Mutes front speaker (model-specific). | — | — |
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Selects audio codec for SmartLink/LAN. | Auto | `AudioCompression` |
| Prevent system sleep while connected | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. | False | `InhibitSleepWhileConnected` |
| PC Audio Devices: Input: / Output: | Picks host audio in/out devices. | — | — |
| Audio Boost: | Enables extra gain on the client audio path. | — | `AudioBoost` |
| Audio Buffer: | Increases audio buffer in milliseconds for VPN/SmartLink jitter. | 200 | `AudioBufferMs` |
| Recording: Radio Side / Client Side | Picks radio-side or client-side recording. | Radio Side | `RecordingMode` |
| Save to: | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. | — | `QsoRecordingDir` |
| ... | Browses for recording folder. | — | — |
| Auto-record on TX | Automatically records while transmitting. | False | `QsoRecordingAutoRecord` |
| Idle timeout: | Seconds of silence before recording stops. | 120 | `QsoRecordingIdleTimeout` |
| NVIDIA BNR: Autostart Container / Start / Stop / Check Status | Controls the NVIDIA Broadcast noise-removal container. | — | — |

### NVIDIA BNR status dot

A colored dot next to the NVIDIA BNR controls indicates the container status (Running/Stopped/Unknown).

## Filters tab

The Filters tab configures low-latency / sharp filter options per bandwidth.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Voice / CW / Digital filter sharpness sliders | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. | — | — |
| Auto (Voice / CW / Digital) | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. | — | — |
| Use Low Latency Filters for Digital Modes | Forces low-latency filters in DIGU/DIGL. | — | — |

## XVTR tab

The XVTR tab provides per-transverter configuration. Contains nested tabs, one per xvtr, and a '+' tab.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| RX Only: | Forces RX-only on that transverter. | — | — |
| Remove (xvtr) | Deletes the transverter definition. | — | — |
| Create New Transverter | Adds a new transverter entry. | — | — |

## USB Cables tab

The USB Cables tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Cables list / Status | Detected USB cables per type with Plugged/Unplugged status. | — | — |
| Name: / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0-7) | Per-cable serial parameters and behavior. | — | — |

## Peripherals tab

The Peripherals tab allows connecting to external devices by IP (TGXL, PGXL, Antenna Genius).

### TGXL direct connection

See the dedicated section below for detailed setup instructions.

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| Connect / Disconnect (TGXL) | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect. | Connect | — |
| Connect / Disconnect (PGXL) | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | Connect | — |
| Connect / Disconnect (Antenna Genius) | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | Connect | — |

### IP field clearing behavior (v26.5.1)

In v26.5.1, the peripherals tab handles cleared IP fields as follows:

- **When connected:** If you clear the IP field and click `Disconnect`, the saved manual IP and port are removed immediately before the disconnect occurs. This ensures downstream visibility handlers (e.g., SmartSDR button visibility) see the cleared settings.
- **When disconnected:** If you clear the IP field (so it is empty) and click `Connect`, the dialog treats this as "save back to default" — it removes any previously-saved manual IP and port. No connection attempt is made.
- **On dialog close:** If you clear the IP field and close the dialog without clicking `Connect` or `Disconnect`, the saved manual IP and port are removed
# Radio Setup

The Radio Setup dialog is the master per-radio configuration window. It provides tabs for radio information, network, GPS, TX, Phone/CW, RX, audio, filters, XVTR, USB cables, peripherals, APD, themes, serial (FlexControl), and antenna names.

## Before you start

- AetherSDR must be connected to the radio to access most tabs.
- Open `Settings > Radio Setup...`.

## Radio tab

The Radio tab displays radio identification, license information, and firmware update controls.

| Control | Default | Behavior |
|---------|---------|----------|
| Radio SN | — | Chassis serial number (read-only). |
| Region | USA | Radio regulatory region. |
| HW Version | — | Hardware version string. |
| Remote On | — | Enables remote wake / remote-on. |
| Options | — | Shows licensed radio options. |
| FlexControl | — | Detected state of FlexControl hardware. |
| multiFLEX | — | multiFLEX enabled state. |
| Model | — | Radio model. |
| Nickname | — | User-friendly radio nickname. |
| Callsign | — | Station callsign. |
| Station Name | — | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored as `StationName`. |
| License Info | — | Displays license details from the radio (Subscription / Expiration / Radio ID / Licensed version). |
| Check for Update | — | Queries for firmware updates. |
| Select Installer... | — | Chooses a firmware image file (`.msi`, `.exe`, or `.ssdr`). |
| Upload Firmware | — | Starts firmware upload with progress bar and status. |

## Network tab

The Network tab displays radio network information and advanced network options.

| Control | Default | Behavior |
|---------|---------|----------|
| IP Address / Mask / MAC Address | — | Read-only network addresses. |
| Enforce Private IP Connections | — | Rejects non-RFC1918 peers. |
| Network MTU | 1450 | Sets maximum outgoing VITA-49 UDP packet size in bytes (576–9000). Stored as `NetworkMtu`. Default 1450 is safe for most VPN/SD-WAN tunnels. |
| DHCP / Static | — | Switches between DHCP and Static IP modes. |
| IP Address / Mask / Gateway | — | Static IP configuration fields. |
| Apply | — | Pushes the network config to the radio. |

## GPS tab

The GPS tab shows GPS presence and live latitude/longitude/altitude/time/satellites information.

## TX tab

The TX tab configures TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX band settings.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| TX Band Settings | — | — | Opens the dedicated per-band power/tune dialog. |
| ACC TX | — | — | TX hang delay in milliseconds. |
| TX Delay | — | — | TX delay in milliseconds. |
| RCA TX1 | — | — | RCA TX1 delay in milliseconds. |
| Timeout (sec) | — | — | Interlock timeout displayed in seconds. The radio stores this value in milliseconds. |
| RCA TX2 | — | — | RCA TX2 delay in milliseconds. |
| Interlocks - TX REQ: RCA / Accessory | — | — | Enables RCA and accessory interlock inputs. |
| Max Power | — | 0–100 % | Sets radio-level TX power cap. |
| Tune Mode | — | — | Selects how the tune button behaves. |
| Show TX in Waterfall | — | — | Draws TX signal in the waterfall. |
| TX Follows Active Slice | False | — | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'. Disabled automatically during Split operation. |
| Active Slice Follows TX | False | — | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'. |

### Timing fields

The timing fields on the TX tab accept values in milliseconds except for Timeout (sec) which displays and accepts values in seconds for readability. The radio stores the timeout value internally in milliseconds.

## Phone/CW tab

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| Enable/Disable the Level Meter During Receive | — | — | Shows mic level meter even in RX. |
| Iambic | — | Enabled / Disabled | Enables or disables the iambic keyer on the radio. |
| Iambic Mode: A / B | A | A / B | Selects Curtis iambic mode A or B for both the radio and the local software keyer. |
| Swap | — | — | Swaps dit/dah. |
| Sideband | — | LSB / USB | Selects CW pitch sideband. |
| CWX | — | — | Enables CWX macro keying. |
| Decode | True | — | Enables the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`. |
| RTTY Mark Default | — | — | Default RTTY mark frequency. |

## RX tab

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| Cal Frequency (MHz) | — | — | Frequency used for manual calibration. Available regardless of whether a GPSDO is installed. If the field is empty when you click **Start**, a warning appears and calibration does not begin. |
| Start | — | — | Sets the calibration frequency, resets `freq_error_ppb` to 0, then starts the radio PLL calibration sweep. The button is disabled and labelled **Busy** while calibration is running. |
| Freq Offset (ppb) | — | — | Manual frequency offset in parts per billion. |
| 10 MHz Reference Source | Auto | Auto / TCXO / GPSDO / External 10 MHz | Selects oscillator reference source. Options shown depend on hardware installed. Lock status (Locked / Unlocked) is shown alongside the combo and updates live. |

### 10 MHz Reference Source

The combo populates dynamically each time the dialog opens or the radio reports oscillator status:

- **Auto** is always present.
- **TCXO** appears when the radio reports any oscillator status, when `tcxoPresent` is true, or when the current or configured value is `tcxo`.
- **GPSDO** appears when `gpsdoPresent` is true or the current or configured value is `gpsdo`.
- **External 10 MHz** appears when the radio reports any oscillator status, when `extPresent` is true, or when the current or configured value is `external`.

The combo pre-selects the value that matches the radio's current configured setting (`oscSetting`). If that value is not in the list, the previously selected item is used; if neither is present, **Auto** is selected.

## Audio tab

The Audio tab configures radio audio outputs, compression, PC devices, boost, buffer, recording, and NVIDIA BNR container.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| Line Out | — | — | Line-out gain slider. |
| Mute (Line Out) | — | — | Mutes line-out. |
| Headphone | — | — | Headphone gain slider. |
| Mute (Headphone) | — | — | Mutes headphone. |
| Front Speaker / Mute | — | — | Mutes front speaker (model-specific). |
| Audio Compression (SmartLink) | Auto | Auto / Uncompressed / Opus | Selects audio codec for SmartLink/LAN. Stored as `AudioCompression`. |
| Prevent system sleep while connected | False | — | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. |
| PC Audio Devices: Input / Output | — | — | Picks host audio in/out devices. |
| Audio Boost | — | — | Enables extra gain on the client audio path. Stored as `AudioBoost`. |
| Audio Buffer | 200 ms | 50–1000 ms | Increases audio buffer in milliseconds for VPN/SmartLink jitter. Stored as `AudioBufferMs`. |
| Recording: Radio Side / Client Side | Radio Side | Radio Side / Client Side | Picks radio-side or client-side recording. Stored as `RecordingMode`. |
| Save to | — | — | Folder for saved recordings (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored as `QsoRecordingDir`. |
| ... (browse) | — | — | Browses for recording folder. |
| Auto-record on TX | False | — | Automatically records while transmitting. Stored as `QsoRecordingAutoRecord`. |
| Idle timeout | 120 sec | 10–3600 sec | Seconds of silence before recording stops. Stored as `QsoRecordingIdleTimeout`. |
| NVIDIA BNR: Autostart Container / Start / Stop / Check Status | — | — | Controls the NVIDIA Broadcast noise-removal container. |

## Antennas tab

The Antennas tab (new in v26.5.2.1) allows naming and configuring antennas. This tab is lazy-built when first clicked.

## Filters tab

The Filters tab provides low-latency / sharp filter options per bandwidth.

| Control | Default | Valid Range | Behavior |
|---------|---------|-------------|----------|
| Voice / CW / Digital filter sharpness sliders | — | 0–3 | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode; slider is disabled when Auto is enabled. |
| Auto (Voice / CW / Digital) | — | — | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. |
| Use Low Latency Filters for Digital Modes | — | — | Forces low-latency filters in DIGU/DIGL. |

## XVTR tab

The XVTR tab provides per-transverter configuration with nested tabs, one per transverter, plus a '+' tab for creating new transverters.

| Control | Default | Behavior |
|---------|---------|----------|
| RX Only | — | Forces RX-only on that transverter. |
| Remove | — | Deletes the transverter definition. |
| Create New Transverter | — | Adds a new transverter entry. |

## USB Cables tab

The USB Cables tab assigns USB serial adapters to CAT, BCD, bit, and PTT cable types.

| Control | Behavior |
|---------|----------|
| Cables list / Status | Detected USB cables per type with Plugged/Unplugged status. |
| Name / Enabled / Speed / Data Bits / Parity / Stop Bits / Flow / Source / Auto Report / BCD Type / Polarity / Bit Configuration (0-7) | Per-cable serial parameters and behavior. |

## Peripherals tab

The Peripherals tab configures external device manual IP connections (TGXL, PGXL, Antenna Genius).

| Control | Default | Behavior |
|---------|---------|----------|
| Connect / Disconnect (TGXL) | Connect | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable. If IP field is empty and radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL) | Connect | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. |
| Connect / Disconnect (Antenna Genius) | Connect | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. |

### Clearing saved IPs

When the **Connect** button is clicked while the IP field is empty, the saved manual IP and port for that device are removed from settings. If you close the Radio Setup dialog with a cleared IP field and a previously-saved manual IP exists, AetherSDR automatically removes that saved IP and port from settings and disconnects the device if it is currently connected.

## APD tab

The APD tab (External Adaptive Pre-Distortion) configures sample port selection per TX antenna. The tab is hidden unless the radio reports `apd configurable=1` (FLEX-8x00 with SmartSDR 4.2.18+). Only FLEX-8x00 series with SmartSDR 4.2.18+ firmware exposes this; 6000-series and pre-4.2.18 radios keep the tab invisible.

| Control | Default | Behavior |
|---------|---------|----------|
| ANT1 / ANT2 / XVTA / XVTB sampler combos | INTERNAL | Selects the feedback path the radio uses to sample the outgoing RF for APD training for that TX antenna. Options: INTERNAL, RX_A, RX_B, XVTA, XVTB. INTERNAL samples inside the radio; external ports require a coupled feedback signal from the linear amplifier
# Radio Setup Overview

The Radio Setup dialog is the central configuration window for your FLEX-8600. It brings together radio identification, network, GPS, transmit, audio, filters, transverters, USB cables, peripherals, antenna names, slice color themes, APD sampler configuration, SmartLink certificate management, and FlexControl serial settings in one place. Open it whenever you need to change anything about how AetherSDR interacts with your radio hardware.

## Before you start

- The radio must be connected. Radio Setup requires an active radio connection.

## How it works

Open Radio Setup from `Settings > Radio Setup...`. The dialog contains a row of tabs across the top; each tab covers a distinct area of configuration. Tabs other than Radio load their contents the first time you click them.

The dialog remembers its size and position between sessions using `PersistentDialog`. A title bar with the text "Radio Setup" appears at the top. You can drag the title bar to move the dialog.

You can also jump directly to specific tabs:

- `Settings > USB Cables...` opens Radio Setup with the **USB Cables** tab active.
- `Settings > FlexControl...` opens Radio Setup with the **Serial** tab active (only available when serial port support is built in).

### Tab scroll behavior

Tabs whose content may exceed the visible dialog height on small or high-DPI displays (Radio, Audio, Filters, Themes, Peripherals, SmartLink) automatically embed a vertical scroll area. The scrollbar only appears when needed — users on wide screens see no visual change.

### Tabs at a glance

| Tab | What you configure here |
|---|---|
| **Radio** | Serial number, hardware version, region, licensed options, nickname, callsign, station name, license info, firmware update, and radio reboot. |
| **Network** | IP address (DHCP or static), network MTU, and private IP enforcement. |
| **GPS** | Live GPS status: latitude, longitude, altitude, time, and satellite count. |
| **TX** | TX hang/delay timings, interlocks, global power cap, tune mode, waterfall TX display, TX/slice follow behavior, and a shortcut to per-band settings. |
| **Phone/CW** | Microphone level meter, iambic keyer (mode A/B, swap, sideband), CWX, CW decoder, and RTTY mark default. |
| **RX** | Frequency offset calibration and 10 MHz reference source selection. Calibration controls are always visible; when a GPSDO is installed the status label confirms its presence. |
| **Antennas** | Display and rename antenna ports (ANT1, ANT2, XVTA, XVTB) as recognized by the radio. |
| **Audio** | Line out, headphone, and speaker levels; audio compression codec; PC audio device selection; audio boost; audio buffer size; recording mode, folder, auto-record on TX, and idle timeout; NVIDIA BNR container control. |
| **Filters** | Low-latency vs. sharp filter selection per bandwidth, and a separate option for digital modes. |
| **XVTR** | Per-transverter configuration; create or remove transverter entries. |
| **APD** | External Adaptive Pre-Distortion sampler configuration — per-TX-antenna feedback port selection and equalizer reset. Visible only on FLEX-8x00 radios reporting `apd configurable=1` (SmartSDR 4.2.18+ firmware). |
| **USB Cables** | Assign USB serial adapters to CAT, BCD, bit, and PTT cable types and configure their serial parameters. |
| **Peripherals** | Manual IP connection to external devices: TGXL, PGXL, Antenna Genius, and ShackSwitch. |
| **Themes** | Slice color scheme: switch between built-in AetherSDR palette and custom per-slice colors (A–H). |
| **Serial** | FlexControl serial port selection, line parameters, pin function assignments (DTR/RTS), paddle swap, auto-open, and tuning knob detection. (Visible only when serial port support is built in.) |
| **SmartLink** | Pinned TLS certificate management — lists each pinned certificate with Forget and Forget All buttons. |

## What each control does

The following controls have persisted settings keys or notable behaviors.

| Control | Tab | Behavior |
|---|---|---|
| **Radio SN** | Radio | Chassis serial number (read-only). Includes a clipboard copy button (tray icon) next to the value. |
| **HW Version** | Radio | Hardware version string (read-only). Includes a clipboard copy button next to the value. |
| **Options** | Radio | Shows licensed radio options (read-only). Includes a clipboard copy button next to the value. |
| **Model** | Radio | Radio model (read-only). Includes a clipboard copy button next to the value. |
| **License Info (Subscription / Expiration / Radio ID / Licensed version)** | Radio | Displays license details from the radio. Each field includes a clipboard copy button next to the value. |
| **IP Address / Mask / MAC Address** | Network | Read-only network addresses. Each includes a clipboard copy button. |
| **Station Name** | Radio | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if left empty. Stored as `StationName`. Sent to the radio as `client station <name>`. |
| **Select Installer...** | Radio | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. Label changed from **Browse .ssdr...** in v26.5.3. |
| **Reboot Radio** | Radio | Sends a reboot command to the radio. A confirmation dialog appears first. On LAN connections AetherSDR automatically reconnects once the radio finishes booting. On SmartLink/WAN connections you must reconnect manually. The button is disabled when the radio is disconnected. |
| **Network MTU:** | Network | Sets maximum outgoing VITA-49 UDP packet size in bytes (576–9000). Default 1450 is safe for most VPN/SD-WAN tunnels. Stored as `NetworkMtu`. |
| **Enforce Private IP Connections:** | Network | Rejects non-RFC1918 peers. The toggle button reads "Enabled" when checked and "Disabled" when unchecked. |
| **TX Follows Active Slice** | TX | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored as `TxFollowsActiveSlice`. |
| **Active Slice Follows TX** | TX | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored as `ActiveFollowsTxSlice`. |
| **Iambic:** | Phone/CW | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Phone/CW | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. Default: A. |
| **Decode:** | Phone/CW | Enables the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`. Default: enabled. |
| **10 MHz Reference Source:** | RX | Selects the oscillator reference source. The combo box is populated dynamically: Auto is always present; TCXO, GPSDO, and External 10 MHz appear based on what the radio reports as installed or currently active. If the radio sends `ext` for the oscillator setting or state, AetherSDR normalises it to `external` before displaying. When the setting is Auto and the radio has selected a specific source, the label shows the resolution (for example, "Auto -> GPSDO"). Lock status (Locked / Unlocked) is shown in green or red beside the combo and updates live. If External 10 MHz is selected but no external reference is detected, "(not detected)" is appended to the status text. |
| **Voice / CW / Digital filter sharpness sliders** | Filters | Sets filter sharpness (0 = lowest latency to 3 = sharpest) per mode. Slider is disabled when Auto is enabled. Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| **Auto (Voice / CW / Digital)** | Filters | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| **ANT1 / ANT2 / XVTA / XVTB sampler combos** | APD | Selects the feedback path used to sample outgoing RF for APD training for that TX antenna. Choose an external RX/XVTR input when driving an external linear amplifier. Options are populated live from the radio's `apd sampler` sub-object. Falls back to INTERNAL if the radio reports an unrecognised value. Default: INTERNAL. |
| **Equalizer Reset** | APD | Sends `apd reset` to the radio, clearing all per-antenna APD training data so adaptation starts fresh. |
| **Audio Compression (SmartLink):** Auto / Uncompressed / Opus | Audio | Selects the audio codec used over SmartLink or LAN. Stored as `AudioCompression`. Default: Auto. |
| **Prevent system sleep while connected** | Audio | Keeps the OS awake while the radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored as `InhibitSleepWhileConnected`. Default: disabled. |
| **Audio Boost:** | Audio | Enables extra gain on the client-side audio path. Stored as `AudioBoost`. |
| **Audio Buffer:** | Audio | Increases the audio buffer (50–1000 ms) to absorb VPN or SmartLink jitter. Default: 200 ms. Stored as `AudioBufferMs`. |
| **Recording:** Radio Side / Client Side | Audio | Selects whether recordings are captured at the radio or on this computer. Stored as `RecordingMode`. Default: Radio Side. |
| **Save to:** | Audio | Folder path where client-side recordings are saved. Stored as `QsoRecordingDir`. Defaults to `Documents/AetherSDR/Recordings`. |
| **Auto-record on TX** | Audio | Automatically starts recording whenever the radio transmits. Stored as `QsoRecordingAutoRecord`. Default: disabled. |
| **Idle timeout:** | Audio | Seconds of silence (10–3600) after which an active recording stops automatically. Default: 120 s. Stored as `QsoRecordingIdleTimeout`. |
| **Connect / Disconnect (TGXL)** | Peripherals | Opens/closes a direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has already discovered the TGXL, the discovered IP is pre-filled. If you clear the IP field and close the dialog, the saved manual IP and port are removed so the device no longer auto-connects. If you clear the IP field and click **Connect**, the saved settings are also removed and the connect is cancelled. |
| **Connect / Disconnect (PGXL)** | Peripherals | Opens/closes a direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. Same IP-clearing behavior as TGXL. |
| **Connect / Disconnect (Antenna Genius)** | Peripherals | Opens/closes a connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. The row is hidden from the Connected state if a ShackSwitch (rather than a standard Antenna Genius) is the device currently connected. Same IP-clearing behavior as TGXL. |
| **Connect / Disconnect (ShackSwitch)** | Peripherals | Opens/closes a connection to a ShackSwitch antenna switch via the AG UDP/TCP protocol on port 9007. Saves IP to `SS_ManualIp` and port to `SS_ControlPort`. ShackSwitch is detected by the `ShackSwitch` field in the AG broadcast beacon. Auto-discovery via UDP also works without manually entering an address. The row is hidden when a standard Antenna Genius (non-ShackSwitch) is the connected device. Same IP-clearing behavior as TGXL. |
| **⚙ Web UI (ShackSwitch)** | Peripherals | Opens the ShackSwitch device's local web configuration interface in the system browser. Uses the beacon's `webPort` if greater than 1024; otherwise falls back to `SS_WebPort` or port 5000. |
| **Use Aether defaults / Custom colors** | Themes | Switches the slice color scheme between the built-in AetherSDR palette and a fully custom per-slice set. Default: Use Aether defaults. |
| **Slice A–H color buttons** | Themes | Click any lettered button (A–H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overl
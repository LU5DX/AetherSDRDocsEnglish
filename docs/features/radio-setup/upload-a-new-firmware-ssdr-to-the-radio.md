# Upload a New Firmware File to the Radio

This page explains how to load a firmware image onto your FLEX-8600 using the Radio Setup dialog. You would do this to update the radio to a specific firmware version without using the automatic update check.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) will not populate correctly without a live connection.
- Download the SmartSDR installer from flexradio.com and note where it is saved on your computer. AetherSDR accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file.
- Do not transmit during the upload.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Select Installer...** to open a file chooser.
4. Navigate to the installer or firmware file on your computer, select it, and confirm. AetherSDR auto-detects the format from the file header and extracts the `.ssdr` if needed. A status message appears while the firmware is being prepared.
5. When the status indicates the firmware is ready, click **Upload Firmware**.
6. Watch the progress bar and status text below the button. Wait until the status indicates the upload is complete before doing anything else.
7. Reboot the radio as directed by the firmware release notes to apply the new firmware.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Radio SN** | Indicator | Chassis serial number (read-only). Shows the chassis serial if available, otherwise the radio serial. Displays an em dash (`—`) if no value is reported. A small copy button appears next to the value on hover or focus; click it to copy the serial number to the clipboard. |
| **Region** | Indicator | Radio regulatory region. |
| **HW Version** | Indicator | Hardware version string. Displays an em dash (`—`) if empty, prefixed with `v` if no leading `v`. A copy button is available. |
| **Model** | Indicator | Radio model. A copy button is available. |
| **Nickname** | Text field | User-friendly radio nickname. |
| **Callsign** | Text field | Station callsign. |
| **Station Name** | Text field | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as `client station <name>`. |
| **Remote On** | Button | Enables remote wake / remote-on. |
| **Options** | Indicator | Shows licensed radio options. Displays the radio's reported option string or, if empty, inserts sensible defaults (e.g. `GPS, PGXL` if the radio has an amplifier, otherwise `GPS`). A copy button is available. |
| **FlexControl** | Indicator | Detected state of FlexControl hardware. |
| **multiFLEX** | Indicator | multiFLEX enabled state. |
| **License Info** | Indicator | Displays license details (Subscription / Expiration / Radio ID / Licensed version) from the radio. |
| **Check for Update** | Button | Queries for available firmware updates. If an update is found, the status area shows the available version and instructs you to download the SmartSDR installer from flexradio.com, then use **Select Installer...** to stage it. |
| **Select Installer...** | Button | Opens a file dialog that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` file. The firmware stager auto-detects the format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools. A status message is shown while the file is being prepared. Renamed from **Browse .ssdr...** in v0.9.3. |
| **Upload Firmware** | Button | Starts the upload using the file staged by **Select Installer...**. A progress bar and status text appear below and update as the transfer proceeds. |
| TX Follows Active Slice | Button | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored in AppSettings as `TxFollowsActiveSlice`. |
| Active Slice Follows TX | Button | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored in AppSettings as `ActiveFollowsTxSlice`. |
| APD (tab) | Tab | External Adaptive Pre-Distortion sample port selection per TX antenna (ANT1, ANT2, XVTA, XVTB). Tab is hidden unless the radio reports apd configurable=1 (FLEX-8x00 with SmartSDR 4.2.18+). New in v26.5.1 (#2186). Lazy-built only when the tab is first clicked. |
| External Sampler (per TX ANT) | Section header inside the APD tab showing a 2x2 grid of ANT1/ANT2/XVTA/XVTB sampler-port combo boxes. |
| ANT1: / ANT2: / XVTA: / XVTB: | Combo box | Picks the sample port (INTERNAL, RX_A, RX_B, XVTA, XVTB) that the radio uses for APD feedback on that TX antenna. INTERNAL samples inside the radio; external ports require a coupled feedback signal from the linear amplifier output. Changing sends setApdSamplerPort() to the radio. |
| Equalizer Reset: | Section row label for the APD equalizer reset button. |
| Reset (APD Equalizer) | Button | Clears all per-antenna APD training data on the radio. Sends resetApdEqualizer() to the radio's TransmitModel. |
| Themes (tab) | Tab | UI appearance settings including per-slice color overrides. Tab label in code is 'Themes'. Lazy-built when first clicked. |
| Slice Colors | Group box header for the slice color controls. |
| Use Aether defaults | Radio button | Uses the built-in slice color palette (cyan/magenta/green/yellow/orange/teal/coral/lavender). Selecting this disables the custom color buttons. |
| Custom colors | Radio button | Enables per-slice color pickers (A-H). Selecting this enables the eight color buttons below. |
| A/B/C/D/E/F/G/H color buttons | Button | Click to open a color picker for that slice letter (A-H). The button's background reflects the currently assigned color. 8 buttons arranged in a horizontal grid. Stored via SliceColorManager which persists to AppSettings. |
| Reset All to Defaults | Button | Resets every per-slice custom color to its built-in default. |
| SmartLink (tab) | Tab | Pinned SmartLink TLS certificate management. Lists each pinned certificate (host, SHA-256 fingerprint, pinned date) with per-row Forget and Forget All. New in v26.5.3 (#2951 Phase 2). Lazy-built when first clicked. Phase 2 of GHSA-wfx7-w6p8-4jr2: cert-pin mismatch now hard-pauses the handshake with a modal dialog. |
| Pinned SmartLink Certificates (section) | Section header for the pinned certs table inside the SmartLink tab. Lists every host this client has pinned on first connect (trust-on-first-use). Phase 2 of GHSA-wfx7-w6p8-4jr2. Pin schema migrated from plain strings to {fp, pinnedAt} objects. |
| Host / SHA-256 fingerprint / Pinned (table columns) | 3-column read-only table: Host (hostname), SHA-256 fingerprint (monospace), Pinned (YYYY-MM-DD or '(pre-phase 2)'). Backed by WanCertCache in WanConnection.cpp. |
| Forget selected | Button | Removes the selected host's pinned cert fingerprint so the next connect re-pins silently. |
| Forget all | Button | Clears every pinned cert (with confirmation). Next connect to each radio silently re-pins. Shows QMessageBox::question before wiping. |

## Network tab

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator | Read-only network addresses. |
| **Enforce Private IP Connections:** | Toggle | Rejects non-RFC1918 peers. |
| **Network MTU:** | Spinbox | Sets maximum outgoing VITA-49 UDP packet size in bytes (576-9000). Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. |
| **DHCP / Static** | Toggle | Switches between DHCP and Static IP modes. |
| **IP Address: / Mask: / Gateway:** | Text field | Static IP configuration fields. |
| **Apply** | Button | Pushes the network config to the radio. |

## GPS tab

| Control | Kind | Behavior |
|---|---|---|
| GPS info | Indicator | GPS presence and live lat/lon/alt/time/satellites info. |

## TX tab

| Control | Kind | Behavior |
|---|---|---|
| **TX Band Settings** | Button | Opens the dedicated per-band power/tune dialog. |
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

| Control | Kind | Behavior |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Toggle | Shows mic level meter even in RX. |
| **Iambic:** | Toggle | Enables or disables the iambic keyer on the radio. |
| **Iambic Mode: A / B** | Button | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. Default is A. |
| **Swap:** | Toggle | Swaps dit/dah. |
| **Sideband:** | Combo box | Selects CW pitch sideband (LSB / USB). |
| **CWX:** | Toggle | Enables CWX macro keying. |
| **Decode:** | Toggle | Enables the CW decode overlay on the panadapter. Stored in AppSettings as `CwDecodeOverlay`. |
| **RTTY Mark Default:** | Spinbox | Default RTTY mark frequency. |

## RX tab

| Control | Kind | Behavior |
|---|---|---|
| **Cal Frequency (MHz)** | Field | Enter the known reference frequency in MHz (six decimal places). |
| **Start** | Button | Resets the frequency error to 0 ppb, then starts the calibration sweep. Disabled and labeled **Busy** while a sweep is running. |
| **Freq Offset (ppb)** | Spinbox | Manual frequency offset in parts per billion. |
| **10 MHz Reference Source:** | Combo box | Selects oscillator reference source. Options shown depend on hardware installed (Auto / TCXO / GPSDO / External). |
| Oscillator status label | Indicator | Shows the resolved source, lock state (Locked / Unlocked), and (for External) whether a signal is detected. Updates live. |

## Audio tab

| Control | Kind | Behavior |
|---|---|---|
| **Line Out:** | Slider | Line-out gain. |
| **Mute (Line Out)** | Button | Mutes line-out. |
| **Headphone:** | Slider | Headphone gain. |
| **Mute (Headphone)** | Button | Mutes headphone. |
| **Front Speaker: / Mute** | Button | Mutes front speaker (model-specific). |
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Button | Selects audio codec for SmartLink/LAN. Stored in AppSettings as `AudioCompression`. |
| **Prevent system sleep while connected** | Checkbox | Keeps OS awake while radio is connected to prevent audio/TCP/UDP stream drops during idle. Stored in AppSettings as `InhibitSleepWhileConnected`. |
| **PC Audio Devices: Input: / Output:** | Combo box | Picks host audio in/out devices. |
| **Audio Boost:** | Toggle | Enables extra gain on the
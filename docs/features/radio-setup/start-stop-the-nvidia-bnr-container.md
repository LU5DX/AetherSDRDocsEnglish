# Radio Setup Dialog

The Radio Setup dialog (`Settings > Radio Setup...`) is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, Phone/CW, RX, Antennas, audio, filters, XVTR, USB cables, peripherals, APD (Adaptive Pre-Distortion), Themes, SmartLink (pinned certificates), and serial (FlexControl).

## Opening the dialog

1. Ensure AetherSDR is connected to the radio.
2. Click `Settings > Radio Setup...`.
3. The dialog opens. You can drag the title bar to move the dialog and use the window edges to resize it. Dialog geometry is persisted between sessions.

If a tab contains more controls than fit vertically (e.g., on small or high-DPI displays), a scrollbar appears within that tab. The dialog itself does not grow beyond the screen edge.

## Radio (tab)

The Radio tab displays radio information, identification, license information, and firmware update controls. Each read-only value has a small copy button to its right — click to copy the value to your clipboard.

### Radio information

| Control                                             | Kind                                                                                                                                                                                        | Behavior                                                                                                                                                                              |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Radio SN**                                        | Indicator                                                                                                                                                                                   | Chassis serial number (read-only).                                                                                                                                                    |
| **Region**                                          | Indicator                                                                                                                                                                                   | Radio regulatory region (e.g., USA).                                                                                                                                                  |
| **HW Version**                                      | Indicator                                                                                                                                                                                   | Hardware version string.                                                                                                                                                              |
| **Model**                                           | Indicator                                                                                                                                                                                   | Radio model.                                                                                                                                                                          |
| **Nickname**                                        | Text field                                                                                                                                                                                  | User-friendly radio nickname.                                                                                                                                                         |
| **Callsign**                                        | Text field                                                                                                                                                                                  | Station callsign.                                                                                                                                                                     |
| **Station Name**                                    | Text field                                                                                                                                                                                  | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty. Stored in AppSettings as `StationName`. Sent to radio as `client station <name>`. |
| **Remote On**                                       | Button                                                                                                                                                                                      | Enables remote wake / remote-on.                                                                                                                                                      |
| **Options**                                         | Indicator                                                                                                                                                                                   | Shows licensed radio options.                                                                                                                                                         |
| **FlexControl**                                     | Indicator                                                                                                                                                                                   | Detected state of FlexControl hardware.                                                                                                                                               |
| **multiFLEX**                                       | Indicator                                                                                                                                                                                   | multiFLEX enabled state.                                                                                                                                                              |
| **License Info**                                    | Indicator                                                                                                                                                                                   | Displays license details (Subscription / Expiration / Radio ID / Licensed version) from the radio.                                                                                    |
| **Reboot:**                                         | Button + confirmation                                                                                                                                                                       | Reboots the connected radio. See "Rebooting the radio" below.                                                                                                                         |
| Select Installer...                                 | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress. | Label changed from 'Browse .ssdr...' to 'Select Installer...' in v26.5.3.                                                                                                             |
| SmartLink (tab)                                     | Pinned SmartLink TLS certificate management. Lists each pinned certificate (host, SHA-256 fingerprint, pinned date) with per-row Forget and Forget All. New in v26.5.3 (#2951 Phase 2).     | Lazy-built when first clicked. Phase 2 of GHSA-wfx7-w6p8-4jr2: cert-pin mismatch now hard-pauses the handshake with a modal dialog.                                                   |
| Pinned SmartLink Certificates (section)             | Section header for the pinned certs table inside the SmartLink tab. Lists every host this client has pinned on first connect (trust-on-first-use).                                          | Phase 2 of GHSA-wfx7-w6p8-4jr2. Pin schema migrated from plain strings to {fp, pinnedAt} objects.                                                                                     |
| Host / SHA-256 fingerprint / Pinned (table columns) | 3-column read-only table: Host (hostname), SHA-256 fingerprint (monospace), Pinned (YYYY-MM-DD or '(pre-phase 2)').                                                                         | Backed by WanCertCache in WanConnection.cpp.                                                                                                                                          |
| Forget selected                                     | Removes the selected host's pinned cert fingerprint so the next connect re-pins silently.                                                                                                   |                                                                                                                                                                                       |
| Forget all                                          | Clears every pinned cert (with confirmation). Next connect to each radio silently re-pins.                                                                                                  | Shows QMessageBox::question before wiping.                                                                                                                                            |
#### Rebooting the radio

1. Click **Reboot Radio**.
2. A confirmation dialog appears:
   - **SmartLink/WAN session**: The message reads "AetherSDR will disconnect. SmartLink/WAN sessions do not auto-reconnect today — you will need to reconnect manually once the radio finishes booting."
   - **Local session**: The message reads "AetherSDR will disconnect and automatically reconnect once the radio finishes booting."
3. Click **OK** to confirm. The dialog closes and AetherSDR disconnects. On local connections, reconnection happens automatically.
4. The button is disabled when the radio is disconnected.

### Firmware update

| Control                | Kind      | Behavior                                                                                                                                                                                                 |
|------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Check for Update**   | Button    | Queries the FlexRadio update server for firmware updates.                                                                                                                                                |
| **Select Installer...** | Button    | Opens a file picker that accepts `.msi` (FlexRadio v4.2+ WiX installer), `.exe` (older self-extracting installer), or a pre-extracted `.ssdr` firmware file. The firmware stager auto-detects format from the first 8 bytes and extracts the `.ssdr` without external tools. |
| **Upload Firmware**    | Button    | Starts firmware upload with progress bar and status.                                                                                                                                                     |
| Firmware status        | Indicator | Empty until a firmware upload begins, then progress and result text.                                                                                                                                     |

#### Checking for updates

1. Click **Check for Update**. AetherSDR queries the FlexRadio update server.
   - If firmware is up to date, the status label reads "Firmware is up to date (v*x.x.x*)." in green.
   - If an update is available, the status label reads "Update available: v*x.x.x* — Download the SmartSDR installer from flexradio.com, then click **Select Installer...** to stage it." in amber.

#### Staging and uploading firmware

1. Download the SmartSDR installer from flexradio.com if you do not already have it locally.
2. Click **Select Installer...**. A file picker opens that accepts:
   - `.msi` — FlexRadio v4.2+ WiX installer
   - `.exe` — older self-extracting installer
   - `.ssdr` — pre-extracted firmware file
3. Select the file. AetherSDR stages the firmware automatically. The stager detects the file format from the first 8 bytes and extracts the `.ssdr` payload without requiring any external tools. The status label shows "Preparing firmware from *filename*..." while staging is in progress.
4. When staging completes, click **Upload Firmware**. A progress bar and status label track the upload.

## Network (tab)

The Network tab displays radio network information and advanced network options.

| Control                              | Kind      | Behavior                                                                                                             |
|--------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------|
| **IP Address / Mask / MAC Address**  | Indicator | Read-only network addresses.                                                                                         |
| **Enforce Private IP Connections:**  | Toggle    | Rejects non-RFC1918 peers.                                                                                           |
| **Network MTU:**                     | Spinbox   | Sets maximum outgoing VITA-49 UDP packet size in bytes (576-9000, default 1450). Stored in AppSettings as `NetworkMtu`. Default 1450 is safe for most VPN/SD-WAN tunnels. |
| **DHCP / Static**                    | Toggle    | Switches between DHCP and Static IP modes.                                                                           |
| **IP Address: / Mask: / Gateway:**   | Text fields | Static IP configuration fields (enabled in Static mode).                                                            |
| **Apply**                            | Button    | Pushes the network configuration to the radio.                                                                       |

## GPS (tab)

The GPS tab displays GPS presence and live latitude/longitude/altitude/time/satellites information.

| Control           | Kind      | Behavior                                         |
|-------------------|-----------|--------------------------------------------------|
| GPS information   | Indicator | Live GPS data when a GPS module is installed and has a fix. |

## TX (tab)

The TX tab controls TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX Band Settings.

| Control                          | Kind      | Behavior                                                                                                                                                               |
|----------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TX Band Settings**             | Button    | Opens the dedicated per-band power/tune dialog.                                                                                                                        |
| **Timings**                      | Spinbox   | TX hang / delay timings. See subtleties below.                                                                                                                         |
| **Interlocks - TX REQ: RCA / Accessory** | Toggle    | Enables RCA and accessory interlock inputs.                                                                                                                            |
| **Max Power:**                   | Spinbox   | Sets radio-level TX power cap (0-100%).                                                                                                                                |
| **Tune Mode:**                   | Combo box | Selects how the tune button behaves.                                                                                                                                   |
| **Show TX in Waterfall:**        | Toggle    | Draws TX signal in the waterfall.                                                                                                                                      |
| **TX Follows Active Slice**      | Button    | TX follows the active slice. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation. Stored in AppSettings as `TxFollowsActiveSlice`. |
| **Active Slice Follows TX**      | Button    | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with **TX Follows Active Slice**. Stored in AppSettings as `ActiveFollowsTxSlice`. |

### Timings

| Field          | Display unit | Radio unit          | Behavior                                                                 |
|----------------|--------------|---------------------|--------------------------------------------------------------------------|
| **ACC TX:**    | milliseconds | milliseconds        | Delay after PTT before TX starts.                                        |
| **TX Delay:**  | milliseconds | milliseconds        | Additional TX hold delay.                                                 |
| **RCA TX1:**   | milliseconds | milliseconds        | RCA interlock TX1 delay.                                                  |
| **Timeout:**   | seconds      | milliseconds        | Interlock timeout. Displayed in seconds for readability; stored on the radio in milliseconds. Entry value is multiplied by 1000 before sending. |
| **TX2:**       | milliseconds | milliseconds        | Second TX timing delay.                                                   |

## Phone/CW (tab)

The Phone/CW tab controls microphone, CW keyer, and RTTY defaults.

| Control                                          | Kind      | Behavior                                                                                                                         |
|--------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------|
| **Enable/Disable the Level Meter During Receive** | Toggle    | Shows mic level meter even in RX.                                                                                                |
| **Iambic:**                                      | Toggle    | Enables or disables the iambic keyer on the radio.                                                                               |
| **Iambic Mode: A / B**                           | Button pair | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive.                          |
| **Swap:**                                        | Toggle    | Swaps dit/dah.                                                                                                                   |
| **Sideband:**                                    | Combo box | Selects CW pitch sideband (LSB \| USB).                                                                                          |
| **CWX:**                                         | Toggle    | Enables CWX macro keying.                                                                                                        |
| **Decode:**                                      | Toggle    | Enables the CW decode overlay on the panadapter. Stored in AppSettings as `CwDecodeOverlay`.                                     |
| **RTTY Mark Default:**                           | Spinbox   | Default RTTY mark frequency.                                                                                                      |

## RX (tab)

The RX tab controls GPSDO frequency offset calibration and 10 MHz reference source selection.

| Control                         | Kind      | Behavior                                                                                                 |
|---------------------------------|-----------|----------------------------------------------------------------------------------------------------------|
| **Cal Frequency (MHz):**        | Spinbox   | Frequency used for manual calibration.                                                                   |
| **Start**                       | Button    | Starts the frequency calibration sweep.                                                                  |
| **Freq Offset (ppb):**          | Spinbox   | Manual frequency offset in parts per billion.                                                            |
| **10 MHz Reference Source:**    | Combo box | Selects oscillator reference source. Options shown depend on hardware installed. Lock status (Locked / Unlocked) is shown alongside and updates live. |

### Frequency calibration

The frequency calibration controls are available regardless of whether a GPSDO is installed.

A status label appears beside **Start** and provides inline feedback:

| Status text       | Meaning                                                                 |
|-------------------|-------------------------------------------------------------------------|
| Starting...       | AetherSDR has sent the calibration commands to the radio.               |
| Busy              | The **Start** button is disabled; calibration is in progress.           |
| (error text)      | A problem was reported; check the value in **Cal Frequency (MHz)**.     |

When GPSDO hardware is present, the label at the top of the group reads "GPSDO installed. Manual frequency offset calibration available." (green). Without GPSDO the label reads "Manual frequency offset calibration available." (amber).

### 10 MHz Reference Source

The combo box is populated dynamically based on what the radio reports:

| Entry                | Shown when                                                                 |
|----------------------|----------------------------------------------------------------------------|
| Auto                 | Always present.                                                            |
| TCXO                 | Radio reports TCXO hardware present, or TCXO
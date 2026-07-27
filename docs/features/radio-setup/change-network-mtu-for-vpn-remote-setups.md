# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It contains tabs for radio information, network, GPS, TX, phone/CW, RX, antennas, filters, XVTR, USB cables, peripherals, serial/FlexControl, themes, APD, KiwiSDR, and SmartLink certificate management. Many read-only values include a clipboard copy button next to the label for easy sharing with support.

## Opening the dialog

1. Click `Settings > Radio Setup...`.
2. The dialog opens with the **Radio** tab selected.

## General dialog behavior

- The dialog geometry is persisted across sessions using `PersistentDialog`.
- Changes made on some tabs are applied immediately; others require clicking an Apply or Connect button.
- If you clear an IP field on the **Peripherals** tab and close the dialog without clicking Connect/Disconnect, the saved manual IP and port are automatically removed and the device disconnects.
- Tabs whose content may exceed the dialog's visible height (Themes, Audio, Filters, Peripherals, KiwiSDR on small or high-DPI displays) are wrapped in a vertical scroll area so the dialog does not overflow the screen edge.
- All QCheckBox indicators use ThemeManager tokens for visibility in dark mode, with hover and disabled pseudo-states.

## Radio (tab)

The Radio tab displays radio information, identification, license info, firmware update controls, and a reboot button.

| Control                                             | Description                                                                                                                                                                                                                                        | Notes                                                                                                                               |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Radio SN**                                        | Chassis serial number (read-only).                                                                                                                                                                                                                 | Click the copy button to copy the serial number to clipboard.                                                                       |
| **Region**                                          | Radio regulatory region (read-only).                                                                                                                                                                                                               |                                                                                                                                     |
| **HW Version**                                      | Hardware version string (read-only).                                                                                                                                                                                                               | Click the copy button to copy the version string to clipboard.                                                                      |
| **Remote On**                                       | Enables remote wake / remote-on.                                                                                                                                                                                                                   |                                                                                                                                     |
| **Options**                                         | Shows licensed radio options (read-only).                                                                                                                                                                                                          | Click the copy button to copy the options string to clipboard.                                                                      |
| **FlexControl**                                     | Detected state of FlexControl hardware (read-only).                                                                                                                                                                                                |                                                                                                                                     |
| **multiFLEX**                                       | multiFLEX enabled state (read-only).                                                                                                                                                                                                               |                                                                                                                                     |
| **Model**                                           | Radio model (read-only).                                                                                                                                                                                                                           | Click the copy button to copy the model string to clipboard.                                                                        |
| **Nickname**                                        | User-friendly radio nickname.                                                                                                                                                                                                                      |                                                                                                                                     |
| **Callsign**                                        | Station callsign.                                                                                                                                                                                                                                  |                                                                                                                                     |
| **Station Name**                                    | Identifies this AetherSDR client to other multiFLEX stations. Defaults to the OS hostname if empty.                                                                                                                                                | Stored in AppSettings as `StationName`. Sent to radio as "client station \<name\>".                                                 |
| **License Info**                                    | Displays license details from the radio: subscription, expiration, radio ID, and licensed version.                                                                                                                                                 | Each field includes a clipboard copy button next to the value.                                                                      |
| **Check for Update**                                | Queries for firmware updates.                                                                                                                                                                                                                      |                                                                                                                                     |
| **Select Installer...**                             | Opens a file dialog for a SmartSDR installer (.msi, .exe) or pre-extracted .ssdr firmware file. Passes the selected path to FirmwareStager which extracts .ssdr payload and emits progress.                                                        | Label changed from 'Browse .ssdr...' to 'Select Installer...' in v26.5.3.                                                           |
| **Upload Firmware**                                 | Starts firmware upload with progress bar and status.                                                                                                                                                                                               |                                                                                                                                     |
| **Reboot Radio**                                    | Sends a reboot command to the connected radio. Disabled when radio is disconnected. Shows a confirmation dialog before rebooting. On LAN, AetherSDR automatically reconnects after the radio boots. On SmartLink/WAN, you must reconnect manually. | New in v26.6.3. The dialog closes after reboot starts.                                                                              |

### Copyable values (Radio tab)

The Radio SN, HW Version, Options, Model, and each License Info field display a small copy button when hovered or focused. Clicking the button copies the displayed value to the system clipboard and shows a brief "Copied!" popup near the button.

### Rebooting the radio

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Locate **Reboot Radio** button.
4. Click **Reboot Radio**.
   - A confirmation dialog appears with different text depending on connection type:
     - **WAN/SmartLink:** "AetherSDR will disconnect. SmartLink/WAN sessions do not auto-reconnect today — you will need to reconnect manually once the radio finishes booting."
     - **LAN:** "AetherSDR will disconnect and automatically reconnect once the radio finishes booting."
5. Click **OK** to confirm.
   - The dialog closes automatically.
   - The radio reboots and AetherSDR disconnects.

### Firmware update (Radio tab)

AetherSDR does not download firmware automatically when an update is detected. Download the SmartSDR installer from flexradio.com yourself, then stage it manually.

#### Staging a firmware update

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. Click **Check for Update**.
   - If an update is available, a status message tells you the available version and directs you to download the installer from flexradio.com.
   - If firmware is current, a green status message confirms the installed version.
4. Download the SmartSDR installer from flexradio.com. Accepted formats:
   - `.msi` — WiX installer (FlexRadio SmartSDR v4.2 and later)
   - `.exe` — older self-extracting installer
   - `.ssdr` — pre-extracted firmware file
5. Click **Select Installer...**.
   - A file picker opens filtered to `*.msi`, `*.exe`, and `*.ssdr`.
   - Select the file you downloaded.
6. When the upload button becomes active, click **Upload Firmware**.
   - A progress bar tracks the upload.
   - Do not close the dialog or disconnect from the radio while the upload is in progress.

#### Firmware status messages

| Message | Meaning |
|---|---|
| Update available: v*x.y.z* | A newer firmware version exists. Download the installer from flexradio.com, then click **Select Installer...**. |
| Firmware is up to date (v*x.y.z*) | No action needed. |
| (error text in red) | Upload failed. Check the file is a valid SmartSDR firmware file and try again. |

## Network (tab)

The Network tab displays radio network information and lets you configure advanced network options.

| Control | Description | Default |
|---|---|---|
| **IP Address / Mask / MAC Address** | Read-only network addresses. Each includes a clipboard copy button. | — |
| **Enforce Private IP Connections:** | Rejects non-RFC1918 peers. Toggle button shows "Enabled". | — |
| **Network MTU:** | Sets maximum outgoing VITA-49 UDP packet size in bytes. Range 576–9000 bytes. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`. | 1450 |
| **DHCP / Static** | Switches between DHCP and Static IP modes. | — |
| **IP Address: / Mask: / Gateway:** | Static IP configuration fields. | — |
| **Apply** | Pushes the network configuration to the radio. | — |

### Changing the Network MTU

The Network MTU setting controls the maximum packet size the radio sends over the network. Lowering it prevents fragmentation when you connect through a VPN or other tunnel that reduces the available path MTU.

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **Network MTU:** spinbox.
4. Set the value to match your network path MTU.
5. Click **Apply** to push the new MTU to the radio.

## GPS (tab)

The GPS tab displays GPS presence and live latitude, longitude, altitude, time, and satellite information.

| Control | Description |
|---|---|
| **GPS status** | Shows GPS presence and live position data. |

## TX (tab)

The TX tab controls TX timings, interlocks, max power, tune mode, waterfall display, slice/TX follow, and TX Band Settings.

| Control | Description | Default |
|---|---|---|
| **TX Band Settings** | Opens the dedicated per-band power/tune dialog. | — |
| **Timings (in ms)** | TX hang / delay timings. | — |
| **ACC TX:** | ACC TX delay in milliseconds. | — |
| **TX Delay:** | TX delay in milliseconds. | — |
| **RCA TX1:** | RCA TX1 delay in milliseconds. | — |
| **Timeout (sec):** | Interlock timeout in seconds (displayed in seconds, stored on radio in milliseconds). | — |
| **TX2 Delay:** | TX2 delay in milliseconds. | — |
| **Interlocks - TX REQ: RCA / Accessory** | Enables RCA and accessory interlock inputs. | — |
| **Max Power:** | Sets radio-level TX power cap (0–100%). | — |
| **Tune Mode:** | Selects how the tune button behaves. | — |
| **Show TX in Waterfall:** | Draws TX signal in the waterfall. | — |
| **TX Follows Active Slice** | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. Disabled automatically during Split operation. | False |
| **Active Slice Follows TX** | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | False |

### TX Timing fields

The TX timing fields control delays and timeouts for transmit operations. Note that the **Timeout** field displays in seconds for readability, but the radio stores and expects this value in milliseconds internally.

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. Locate the **Timings** section.
4. Enter the desired value in each field.
   - ACC TX, TX Delay, RCA TX1, and TX2 Delay are in milliseconds.
   - Timeout is in seconds (range 0–3600 seconds).
5. Press Enter or move focus away from the field to apply the change.

## Phone/CW (tab)

The Phone/CW tab configures microphone, CW keyer, and RTTY defaults.

| Control | Description | Default |
|---|---|---|
| **Enable/Disable the Level Meter During Receive** | Shows mic level meter even in RX. | — |
| **Iambic:** | Enables or disables the iambic keyer on the radio. Toggle button shows "Enabled". | Enabled |
| **Iambic Mode: A / B** | Selects Curtis iambic mode A or B for both the radio and the local software keyer. Mutually exclusive pair. | A |
| **Swap:** | Swaps dit/dah. | — |
| **Sideband:** | Selects CW pitch sideband (LSB or USB). | — |
| **CWX:** | Enables CWX macro keying. | — |
| **Decode:** | Enables the CW decode overlay on the panadapter. Stored in AppSettings as `CwDecodeOverlay`. | True |
| **RTTY Mark Default:** | Default RTTY mark frequency. | — |

## RX (tab)

The RX tab provides GPSDO frequency offset calibration and 10 MHz reference source selection. All calibration controls are always visible, regardless of whether a GPSDO is installed. A status label at the top of the group indicates whether a GPSDO is present (green text) or not (amber text).

| Control | Description |
|---|---|
| **Cal Frequency (MHz):** | Frequency used for manual calibration. |
| **Start** | Starts the frequency calibration sweep. The button label changes to **Busy** while the sweep runs. |
| **Freq Offset (ppb):** | Manual frequency offset in ppb. |
| **10 MHz Reference Source:** | Selects oscillator reference source. Options depend on hardware installed. See table below. |

### 10 MHz Reference Source

The **10 MHz Reference Source:** combo box is populated dynamically. Only sources supported by the connected hardware appear. A label beside the combo shows the resolved source and lock state.

#### Combo options

| Option | When shown |
|---|---|
| Auto | Always. |
| TCXO | When oscillator status has been received, or when the radio reports `tcxoPresent`, or when the current or active setting is `tcxo`. |
| GPSDO | When the radio reports `gpsdoPresent`, or when the current or active setting is `gpsdo`. |
| External 10 MHz | When oscillator status has been received, or when the radio reports `extPresent`, or when the current or active setting is `external`. |

#### Status label behavior

- When **Auto** is selected and the radio has chosen a specific source, the label reads `Auto -> <source>`.
- When a specific source is selected and the radio is using a different one, the label reads `<selected> -> <active>`.
- When the setting and state agree, only the active source is shown.
- Lock state is appended: `Locked` (green) or `Unlocked` (red).
- If **External 10 MHz** is selected or active but no external reference is detected, the label appends `(not detected)`.
- While the radio has not yet reported oscillator status, the label reads
# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It provides tabs for radio information, network settings, GPS, transmit configuration, Phone/CW settings, receive calibration, audio, antennas, filters, transverters, USB cables, peripherals, Adaptive Pre-Distortion (APD), themes, and serial port configuration for FlexControl.

## Before you start

- AetherSDR must be connected to the radio to access tabs that communicate with the radio.
- Some tabs (APD, Themes, Serial) are built lazily when first clicked.
- The APD tab is only visible on FLEX-8x00 series radios with SmartSDR 4.2.18 or later firmware.

## Opening the dialog

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.

## General dialog behavior

- The dialog remembers its size and position between sessions.
- Tab order from left to right: Radio, Network, GPS, TX, Phone/CW, RX, Antennas, Audio, Filters, XVTR, USB Cables, Peripherals, APD, Themes, SmartLink, Serial.
- Click **Close** to dismiss the dialog.

## Radio tab

Displays radio identification, license information, and firmware update controls.

### Steps

1. Click the **Radio** tab.
2. View the read-only indicators for **Radio SN**, **Region**, **HW Version**, **Model**, **Options**, **FlexControl**, **multiFLEX**, and **License Info** (Subscription, Expiration, Radio ID, Licensed version).
3. Optionally set a **Nickname**, **Callsign**, or **Station Name** in the text fields. The **Station Name** identifies this AetherSDR client to other multiFLEX stations; it defaults to the OS hostname if empty. Stored in AppSettings as `StationName`.
4. Click **Remote On** to enable remote wake/remote-on.
5. Click the copy button next to any indicator to copy its value to the clipboard. A "Copied!" popup confirms the action.
6. To update firmware:
   - Click **Check for Update** to query the FlexRadio update server.
   - Download the SmartSDR installer from flexradio.com (`.msi` for v4.2+, `.exe` for older releases).
   - Click **Browse .ssdr...** to open a file picker. Select the installer or a pre-extracted `.ssdr` file.
   - When staging is complete, click **Upload Firmware** to transfer the firmware to the radio.

### Firmware update notes

- The **Browse .ssdr...** button accepts `.msi`, `.exe`, and `.ssdr` files.
- The stager auto-detects the file format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools.
- A progress bar and status label track the upload.

## Network tab

Configure how the radio obtains its network address and advanced network options.

### Steps

1. Click the **Network** tab.
2. Note the read-only **IP Address**, **Mask**, and **MAC Address**.
3. Click the **DHCP / Static** toggle button to switch modes.
4. If you selected static mode, fill in the **IP Address:**, **Mask:**, and **Gateway:** text fields.
5. Click **Apply** to push the network configuration to the radio.
6. Reconnect to the radio at its new address using `Settings > Connect to Radio...`.

### Additional network controls

- **Enforce Private IP Connections:** Toggle to reject non-RFC1918 peers.
- **Network MTU:** Spinbox (576-9000 bytes, default 1450). Sets maximum outgoing VITA-49 UDP packet size. Default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`.

## GPS tab

Displays GPS information from the radio.

- Shows GPS presence status.
- Displays live latitude, longitude, altitude, time, and satellite count.
- Read-only indicators.

## TX tab

Configure transmit timing, interlocks, power limits, and behavior.

### Steps

1. Click the **TX** tab.
2. Adjust **Timings** spinboxes for ACC TX, TX Delay, RCA TX1, Timeout, and TX2 delays in milliseconds.
   - **Timeout (sec):** Displays in whole seconds; the radio stores this in milliseconds internally.
3. Toggle **Interlocks - TX REQ: RCA / Accessory** to enable interlock inputs.
4. Set **Max Power:** as a percentage (0-100%).
5. Select **Tune Mode:** from the combo box.
6. Toggle **Show TX in Waterfall:** to display the TX signal in the waterfall.
7. Configure slice following:
   - **TX Follows Active Slice:** Push button (default False). Stored as `TxFollowsActiveSlice`. Mutually exclusive with **Active Slice Follows TX**. Disabled automatically during Split operation.
   - **Active Slice Follows TX:** Push button (default False). Stored as `ActiveFollowsTxSlice`. Switches the active slice when TX moves externally.
8. Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

## Phone/CW tab

Configure microphone, CW keyer, and RTTY defaults.

### Steps

1. Click the **Phone/CW** tab.
2. Toggle **Enable/Disable the Level Meter During Receive** to show the mic level meter even in RX.
3. Configure CW settings:
   - **Iambic:** Toggle to enable or disable the iambic keyer on the radio. In v0.9.1, Mode A and Mode B buttons were added beside the Enabled toggle for Curtis A and Curtis B modes. These also drive the local software iambic keyer which mirrors the radio's iambic state for sub-5 ms sidetone.
   - **Iambic Mode: A / B:** Select Curtis iambic mode A or B. This applies to both the radio and the local software keyer. Mutually exclusive pair added in v0.9.1.
   - **Swap:** Toggle to swap dit/dah.
   - **Sideband:** Select LSB or USB for CW pitch.
   - **CWX:** Toggle to enable CWX macro keying.
   - **Decode:** Toggle (default True) to enable the CW decode overlay on the panadapter. Stored as `CwDecodeOverlay`.
4. Set **RTTY Mark Default:** spinbox for default RTTY mark frequency.

## RX tab

Configure GPSDO frequency offset calibration and 10 MHz reference source.

### Steps

1. Click the **RX** tab.
2. Set **Cal Frequency (MHz):** for manual calibration.
3. Click **Start** to begin the frequency calibration sweep.
4. Adjust **Freq Offset (ppb):** manually.
5. Select **10 MHz Reference Source:** from the combo box (Auto, TCXO, GPSDO, External). Lock status (Locked/Unlocked) is shown alongside the combo and updates live.

## Antennas tab

Configure antenna names and assignments.

- New in v26.5.2.1.
- Tab labeled "Antennas" appears between RX and Filters tabs.
- Provides controls for naming and configuring antenna ports.

## Audio tab

Configure radio audio outputs, PC audio devices, recording, and NVIDIA BNR container.

### Steps

1. Click the **Audio** tab.
2. Adjust **Line Out:** and **Headphone:** sliders. Click the corresponding **Mute** buttons to mute.
3. Click **Front Speaker: / Mute** to mute the front speaker (model-specific).
4. Select **Audio Compression (SmartLink):** as **Auto**, **Uncompressed**, or **Opus**. Stored as `AudioCompression`.
5. Toggle **Prevent system sleep while connected** to keep the OS awake. Stored as `InhibitSleepWhileConnected`.
6. Select **PC Audio Devices: Input:** and **Output:** from combo boxes.
7. Toggle **Audio Boost:** for extra gain on the client audio path. Stored as `AudioBoost`.
8. Set **Audio Buffer:** (50-1000 ms, default 200) for VPN/SmartLink jitter. Stored as `AudioBufferMs`.
9. Configure recording:
   - **Recording: Radio Side / Client Side:** Select the recording mode. Stored as `RecordingMode`.
   - **Save to:** Text field for folder (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored as `QsoRecordingDir`.
   - Click **...** to browse for a recording folder.
   - Toggle **Auto-record on TX** to automatically record while transmitting. Stored as `QsoRecordingAutoRecord`.
   - Set **Idle timeout:** (10-3600 sec, default 120) for seconds of silence before recording stops. Stored as `QsoRecordingIdleTimeout`.
10. Control **NVIDIA BNR:** with Autostart Container, Start, Stop, and Check Status buttons. A colored dot indicates container Running/Stopped/Unknown status.

## Filters tab

Configure filter sharpness per mode and low-latency options for digital modes.

### Steps

1. Click the **Filters** tab.
2. Adjust **Voice / CW / Digital filter sharpness sliders** (0-3). 0 = lowest latency, 3 = sharpest. Slider is disabled when Auto is enabled.
3. Toggle **Auto (Voice / CW / Digital)** to enable automatic filter-level selection for that mode; disables the manual sharpness slider.
4. Toggle **Use Low Latency Filters for Digital Modes** to force low-latency filters in DIGU/DIGL.

## XVTR tab

Configure per-transverter settings.

### Steps

1. Click the **XVTR** tab.
2. The tab contains nested tabs, one per transverter, plus a '+' tab.
3. For each transverter:
   - Toggle **RX Only:** to force RX-only.
   - Click **Remove** to delete the transverter definition.
4. Click **Create New Transverter** to add a new transverter entry.

## USB Cables tab

Assign USB serial adapters to cable types.

### Steps

1. Click the **USB Cables** tab.
2. View detected **Cables list / Status** with Plugged/Unplugged status per cable type.
3. Configure per-cable parameters: **Name**, **Enabled**, **Speed**, **Data Bits**, **Parity**, **Stop Bits**, **Flow**, **Source**, **Auto Report**, **BCD Type**, **Polarity**, **Bit Configuration (0-7)**.

## Peripherals tab

Configure external device connections (TGXL, PGXL, Antenna Genius).

### Steps

1. Click the **Peripherals** tab.
2. For each peripheral, enter the IP address and port (default ports: TGXL=9010, PGXL=9008, Antenna Genius=9007).
3. Click **Connect** to establish a direct TCP connection. The IP and port are saved on connect so AetherSDR auto-reconnects on startup.
4. Click **Disconnect** to close the connection.

### Peripheral auto-connect and clearing manual IP

When you enter an IP address for a peripheral and click **Connect**, the IP and port are saved to settings. On subsequent startups, AetherSDR automatically attempts to reconnect to that peripheral.

If you clear the IP field and click **Connect** while disconnected, the saved manual IP and port are removed from settings, preventing auto-connect on startup. If you clear the IP field and close the **Radio Setup** dialog without clicking Connect/Disconnect, the saved settings are also cleared and any active connection is disconnected.

### TGXL specific notes

- Required to recover TUNE on firmware 4.2+.
- When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side path broken in firmware 4.2.
- The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed.
- If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled.

## APD tab

Configure Adaptive Pre-Distortion sample ports per TX antenna. Tab is hidden unless the radio reports `apd configurable=1` (FLEX-8x00 with SmartSDR 4.2.18+).

### Steps

1. Click the **APD** tab (only visible on compatible radios).
2. For each TX antenna (**ANT1**, **ANT2**, **XVTA**, **XVTB**), select the sampler port from the combo box (**INTERNAL**, **RX_A**, **RX_B**, **XVTA**, **XVTB**).
   - **INTERNAL** samples inside the radio.
   - External ports require a coupled feedback signal from the linear amplifier output.
3. Click **Reset** (APD Equalizer) to clear all per-antenna APD training data on the radio.

## Themes tab

Configure UI appearance including per-slice color overrides.

### Steps

1. Click the **Themes** tab.
2. In the **Slice Colors** section:
   - Select **Use Aether defaults** to use the built-in palette (cyan, magenta, green, yellow, orange, teal, coral, lavender).
   - Select **Custom colors** to enable per-slice color pickers.
3. If **Custom colors** is selected, click any lettered button (A-H) to open a color picker and assign a custom color for that slice. Changes are visible immediately in VFO widgets, panadapter overlays, and CAT channel badges.
4. Click **Reset All to Defaults** to reset all custom slice colors to the built-in palette.

## SmartLink tab

Manage pinned SmartLink TLS certificates. New in v26
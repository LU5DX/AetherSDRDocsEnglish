# Radio Setup Dialog

The Radio Setup dialog is the master per-radio configuration window. It provides tabs for radio information, network settings, GPS, transmit configuration, Phone/CW settings, receive calibration, antenna names, filters, transverters, USB cables, peripherals, Adaptive Pre-Distortion (APD), themes, SmartLink certificate management, and serial port configuration for FlexControl.

## Before you start

- AetherSDR must be connected to the radio to access tabs that communicate with the radio.
- Some tabs (APD, Themes, Calibration, SmartLink, Serial) are built lazily when first clicked.
- The APD tab is only visible on FLEX-8x00 series radios with SmartSDR 4.2.18 or later firmware.
- The Calibration tab is only visible when the connected radio cannot calibrate its own oscillator (e.g. HL2). Flex radios handle calibration on the RX tab.

## Opening the dialog

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.

## General dialog behavior

- The dialog remembers its size and position between sessions.
- Tab order from left to right: Radio, Network, GPS, TX, Phone/CW, RX, Calibration, Antennas, Audio, Filters, XVTR, USB Cables, Peripherals, APD, Themes, SmartLink, Serial.
- Tabs whose content may exceed the dialog height (Themes, Audio, Filters, Peripherals on small or high-DPI displays) are wrapped in a scroll area so the dialog never grows past the screen edge.
- Click **Close** to dismiss the dialog.

## Radio tab

Displays radio identification, license information, and firmware update controls. Includes a **Reboot Radio** button.

### Steps

1. Click the **Radio** tab.
2. View the read-only indicators for **Radio SN**, **Region**, **HW Version**, **Model**, **Options**, **FlexControl**, **multiFLEX**, and **License Info** (Subscription, Expiration, Radio ID, Licensed version). Each read-only indicator includes a clipboard copy button next to the label — click to copy the value to the clipboard.
3. Optionally set a **Nickname**, **Callsign**, or **Station Name** in the text fields. The **Station Name** identifies this AetherSDR client to other multiFLEX stations; it defaults to the OS hostname if empty. Stored in AppSettings as `StationName`.
4. Click **Remote On** to enable remote wake/remote-on.
5. To reboot the radio:
   - Click **Reboot Radio**. A confirmation dialog appears.
   - On LAN connections, AetherSDR automatically reconnects once the radio finishes booting.
   - On SmartLink/WAN connections, you must manually reconnect after the radio boots.
   - The button is disabled when the radio is disconnected or when the backend does not support a client reboot (e.g. HL2 is RX-only so the button is disabled). It re-enables automatically when the radio reconnects.
6. To update firmware:
   - Click **Check for Update** to query the FlexRadio update server.
   - Download the SmartSDR installer from flexradio.com (`.msi` for v4.2+, `.exe` for older releases).
   - Click **Select Installer...** to open a file picker. Select the installer or a pre-extracted `.ssdr` file.
   - When staging is complete, click **Upload Firmware** to transfer the firmware to the radio.

### Firmware update notes

- The **Select Installer...** button label changed from **Browse .ssdr...** in v26.5.3.
- The button accepts `.msi`, `.exe`, and `.ssdr` files.
- The stager auto-detects the file format from the first 8 bytes (OLE/MSI magic vs PE/COFF MZ) and extracts the `.ssdr` without external tools.
- A progress bar and status label track the upload.

## Network tab

Configure how the radio obtains its network address and advanced network options.

### Steps

1. Click the **Network** tab.
2. Note the read-only **IP Address**, **Mask**, and **MAC Address**. Each includes a clipboard copy button.
3. Toggle **Enforce Private IP Connections:** to reject non-RFC1918 peers.
4. Configure the Agent Automation (MCP) bridge:
   - Toggle **Agent Automation (MCP):** to enable the in-app automation bridge so an AI coding assistant (via the MCP server) can introspect and drive the running app. Off by default; the operator opts in. Persisted via AutomationBridgeSettings.
   - The **Access Token:** field displays the MCP access token (read-only). Paste it into the assistant's `AETHER_MCP_TOKEN` environment variable. Stored in the OS secret store.
   - Click **Copy** to copy the access token to the clipboard.
   - Click **Rotate** to generate a new token and apply it immediately, locking out any client still using the old one.
   - Check **Allow TX via MCP: Enable transmit control** to let an MCP client key the transmitter (MOX/PTT/TUNE/ATU/CWX). Off by default; first enable raises an operator-responsibility confirmation.
   - Check **Observe only: Read-only (block all driving)** to make the bridge observe-only: MCP clients can read state but every mutating verb (set/invoke/connect/tune/capture) is refused. Enforced in the app, so a client cannot bypass it.
5. Set **VITA-49 RX buffer:** as a snap-to-preset slider (256 KB to 4 MB, default 4 MB). This sets the kernel receive buffer (SO_RCVBUF) for the VITA-49 stream socket; larger values absorb panadapter/waterfall bursts so packets aren't dropped. The system caps the grant at `net.core.rmem_max`.
   - The **granted:** label shows the buffer size the kernel actually granted (vs the requested preset). Shows "(applies on connect)" when no connection is active.
6. Set **Network MTU:** as a spinbox value (576-9000 bytes, default 1450). This sets maximum outgoing VITA-49 UDP packet size. The default 1450 is safe for most VPN/SD-WAN tunnels. Stored in AppSettings as `NetworkMtu`.
7. Click the **DHCP / Static** toggle button to switch modes.
8. If you selected static mode, fill in the **IP Address:**, **Mask:**, and **Gateway:** text fields.
9. Click **Apply** to push the network configuration to the radio.
10. Reconnect to the radio at its new address using `Settings > Connect to Radio...`.

### Agent Automation (MCP) notes

- The `AETHER_AUTOMATION` launch environment variable force-enables the bridge regardless of the toggle and disables the control in the UI.
- Transmit-keying stays blocked unless `AETHER_AUTOMATION_ALLOW_TX` is set.
- `AETHER_AUTOMATION_ALLOW_TX` force-enables TX; `AETHER_AUTOMATION_NO_TX` pins it off.
- `AETHER_AUTOMATION_READONLY` pins the observe-only mode on for headless/CI runs.
- A force-unkey watchdog limits bridge-originated TX.
- The Access Token field auto-mints a 128-bit hex token when the bridge is enabled without one. Placeholder shows "(loading…)" until the keychain read lands.

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
   - **Active Slice Follows TX:** Push button (default False). Stored as `ActiveFollowsTxSlice`. Switches the active slice when TX moves externally (e.g. WSJT-X or CAT).
8. Click **TX Band Settings** to open the dedicated per-band power/tune dialog.

## Phone/CW tab

Configure microphone, CW keyer, and RTTY defaults.

### Steps

1. Click the **Phone/CW** tab.
2. Toggle **Enable/Disable the Level Meter During Receive** to show the mic level meter even in RX.
3. Configure CW settings:
   - **Iambic:** Toggle to enable or disable the iambic keyer on the radio. Mutually exclusive with the radio-side iambic keyer; also drives the local software iambic keyer for sub-5 ms sidetone.
   - **Iambic Mode: A / B:** Select Curtis iambic mode A or B. Applies to both the radio and the local software keyer.
   - **Swap:** Toggle to swap dit/dah.
   - **Sideband:** Select LSB or USB for CW pitch.
   - **CWX:** Toggle to enable CWX macro keying.
   - **Decode: RX:** Toggle (default True) to enable the CW decode overlay on the panadapter for received CW. Stored as a nested JSON blob under `CwDecoder` with an `rx` field.
   - **Decode: TX:** Toggle (default False) to decode the operator's own CW keying via client-side sidetone, useful as a self-training tool for paddle/bug timing. Stored as a nested JSON blob under `CwDecoder` with a `tx` field.
4. Set **RTTY Mark Default:** spinbox for default RTTY mark frequency.

### CW decode notes

- The RX and TX decode toggles were split from a single `CwDecodeOverlay` toggle in v26.5.3.
- The legacy `CwDecodeOverlay` key is auto-migrated on first read.

## RX tab

Configure GPSDO frequency offset calibration and 10 MHz reference source.

### Steps

1. Click the **RX** tab.
2. Set **Cal Frequency (MHz):** for manual calibration.
3. Click **Start** to begin the frequency calibration sweep.
4. Adjust **Freq Offset (ppb):** manually.
5. Select **10 MHz Reference Source:** from the combo box (Auto, TCXO, GPSDO, External). Options depend on hardware installed. Lock status (Locked/Unlocked) is shown alongside the combo and updates live.

## Calibration tab

Configure host-side frequency calibration for radios that cannot calibrate their own oscillator (e.g. HL2). This tab is hidden for Flex radios, which handle calibration on the RX tab.

### Steps

1. Click the **Calibration** tab (only visible when the connected radio requires host-side frequency calibration).
2. Configure the frequency calibration settings as appropriate for the connected radio.
3. Click **Trim** or the equivalent action to apply the calibration to the radio.

### Calibration notes

- The tab is gated on the capability `hostFrequencyCalibration`, not on the family name.
- The calibration value is re-read whenever the dialog is shown or the connection state changes, so a Trim press cannot commit a previous radio's number.

## Antennas tab

Configure antenna port display names.

### Steps

1. Click the **Antennas** tab.
2. For each antenna port row (e.g. **ANT1**, **ANT2**, **XVTA**, **XVTB**):
   - View the read-only port label.
   - Enter a custom name (max 16 characters) in the editable text field.
   - Preview the final display name in the Preview column.
   - Click **Clear** to reset the custom name to empty.
3. When a port's custom name is empty, the raw port token is used as the display name.
4. Rows auto-update when slice antenna assignments change.

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
   - **Save to:** Text field for folder (client-side only). Defaults to Documents/AetherSDR/Recordings. Stored as `Q
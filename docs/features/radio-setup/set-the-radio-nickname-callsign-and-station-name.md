# Set the radio nickname, callsign and station name

Set a human-readable nickname, your callsign, and a station name on the connected FLEX-8600. These values identify the radio and this client to other multiFLEX stations on the network.

## Before you start

- AetherSDR must be connected to the radio. The Radio (tab) controls are not available without an active connection.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Radio** tab.
3. In the **Radio Identification** group, locate the **Nickname** field. Type the nickname you want to assign to the radio.
4. Press Tab or click away from the field to confirm. AetherSDR sends the new name to the radio immediately.
5. In the **Callsign** field, type your station callsign.
6. Press Tab or click away from the field to confirm.
7. In the **Station Name** field, type the name that identifies this client to other multiFLEX stations.
8. Press Tab or click away from the field to confirm.
9. Click **Close** to dismiss the dialog.

## What each control does

| Control | Description | Default |
|---|---|---|
| **Nickname** | User-friendly label for the radio. Sent to the radio as the radio name. | Radio's reported name |
| **Callsign** | Your station callsign, stored on the radio. | _(blank)_ |
| **Station Name** | Identifies this AetherSDR client to other multiFLEX stations. | OS hostname |
| TX Follows Active Slice | TX follows the active slice. Mutually exclusive with Active Slice Follows TX. | Disabled automatically during Split operation. |
| Active Slice Follows TX | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with TX Follows Active Slice. | |
| Voice / CW / Digital filter sharpness sliders | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled. | Commands sent as `radio filter_sharpness <mode> level=<N>`. |
| Auto (Voice / CW / Digital) | Enables automatic filter-level selection for that mode; disables the manual sharpness slider. | Commands sent as `radio filter_sharpness <mode> auto_level=1`. |
| Connect / Disconnect (TGXL) | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on connect so AetherSDR auto-reconnects on startup. Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If the IP field is empty and the radio has discovered the TGXL, the discovered IP is pre-filled. | Connect |
| Connect / Disconnect (PGXL) | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to `PGXL_ManualIp` and `PGXL_ManualPort`. | Connect |
| Connect / Disconnect (Antenna Genius) | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to `AG_ManualIp` and `AG_ManualPort`. | Connect |

## Frequency calibration (RX tab)

The **RX** tab provides manual frequency offset calibration regardless of whether a GPSDO is installed.

- If a GPSDO is installed, the status label reads "GPSDO installed. Manual frequency offset calibration available." in green.
- If no GPSDO is installed, the status label reads "Manual frequency offset calibration available." in amber.

In both cases the **Cal Frequency (MHz)** field and the **Start** button are always shown.

### To run a frequency calibration

1. Open `Settings > Radio Setup...`.
2. Click the **RX** tab.
3. Enter a known reference frequency in the **Cal Frequency (MHz)** field.
4. Click **Start**.
   - The button label changes to **Busy** and is disabled while calibration is in progress.
   - A status label beside the button shows the current state (for example, "Starting…").
   - AetherSDR resets the frequency error to 0 ppb (`radio set freq_error_ppb=0`) before initiating the calibration sweep.
5. Wait for the status label to report completion. The **Start** button re-enables automatically.

### Cal Frequency (MHz) field behavior

| Condition | Result |
|---|---|
| Field is empty when Start is clicked | Status label shows "Enter cal frequency" in amber; calibration does not start. |
| Valid frequency entered | AetherSDR sends `radio set cal_freq=<value>`, resets freq error to 0 ppb, then starts the PLL calibration sweep. |

### RX tab controls

| Control | Description | Default |
|---|---|---|
| **Cal Frequency (MHz)** | Reference frequency used for manual calibration. Always shown from v0.9.2.1 onward, regardless of GPSDO presence. | — |
| **Start** | Starts the frequency calibration sweep. Disabled and labelled **Busy** while a calibration is running. | — |
| **Freq Offset (ppb)** | Manual frequency offset in parts per billion. | — |
| **10 MHz Reference Source** | Selects oscillator reference: Auto, TCXO, GPSDO, or External. Options shown depend on installed hardware. Lock status (Locked / Unlocked) updates live alongside the selector. | Auto |

## Tips

- If **Nickname** is left blank, AetherSDR pre-fills the field with the radio's reported name from the network.
- **Station Name** defaults to the OS hostname when no value has been saved. To restore the default, clear the field and press Tab — then re-enter the hostname manually if needed.
- Changes to **Nickname** and **Callsign** are pushed to the radio the moment you leave each field. No separate Save or Apply step is required.
- **Station Name** is saved locally in AetherSDR's settings and also sent to the radio as the client station identifier for multiFLEX.
- Prior to v0.9.2.1, the **Cal Frequency** field and **Start** button were hidden when a GPSDO was installed. They are now always available.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Radio Setup overview](overview.md)
# Radio Setup Overview

The Radio Setup dialog is the central configuration window for your FLEX-8600. It brings together radio identification, network, GPS, transmit, audio, filters, transverters, USB cables, peripherals, and FlexControl serial settings in one place. Open it whenever you need to change anything about how AetherSDR interacts with your radio hardware.

## Before you start

- The radio must be connected. Radio Setup requires an active radio connection.

## How it works

Open Radio Setup from `Settings > Radio Setup...`. The dialog contains a row of tabs across the top; each tab covers a distinct area of configuration. Tabs other than Radio load their contents the first time you click them.

You can also jump directly to specific tabs:

- `Settings > USB Cables...` opens Radio Setup with the **USB Cables** tab active.
- `Settings > FlexControl...` opens Radio Setup with the **Serial** tab active (only available when serial port support is built in).

The dialog remembers its size and position between sessions.

### Tabs at a glance

| Tab | What you configure here |
|---|---|
| **Radio** | Serial number, hardware version, region, licensed options, nickname, callsign, station name, license info, and firmware update. |
| **Network** | IP address (DHCP or static), network MTU, and private IP enforcement. |
| **GPS** | Live GPS status: latitude, longitude, altitude, time, and satellite count. |
| **TX** | TX hang/delay timings, interlocks, global power cap, tune mode, waterfall TX display, TX/slice follow behavior, and a shortcut to per-band settings. |
| **Phone/CW** | Microphone level meter, iambic keyer (mode A/B, swap, sideband), CWX, CW decoder, and RTTY mark default. |
| **RX** | Frequency offset calibration and 10 MHz reference source selection. Calibration controls are always visible; when a GPSDO is installed the status label confirms its presence. |
| **Audio** | Line out, headphone, and speaker levels; audio compression codec; PC audio device selection; audio boost; audio buffer size; recording mode, folder, auto-record on TX, and idle timeout; NVIDIA BNR container control. |
| **Filters** | Low-latency vs. sharp filter selection per bandwidth, and a separate option for digital modes. |
| **XVTR** | Per-transverter configuration; create or remove transverter entries. |
| **USB Cables** | Assign USB serial adapters to CAT, BCD, bit, and PTT cable types and configure their serial parameters. |
| **Peripherals** | Manual IP connection to external devices: TGXL, PGXL, and Antenna Genius. |
| **Serial** | FlexControl serial port selection, line parameters, pin function assignments (DTR/RTS), paddle swap, auto-open, and tuning knob detection. (Visible only when serial port support is built in.) |

## What each control does

The following controls have persisted settings keys.

| Control                                                       | Tab                                                                                                                                                                     | Behavior                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Audio Compression (SmartLink):** Auto / Uncompressed / Opus | Audio                                                                                                                                                                   | Selects the audio codec used over SmartLink or LAN.                                                                                                                                                                                                                                                                                                                                                                                             |
| **Audio Boost:**                                              | Audio                                                                                                                                                                   | Enables extra gain on the client-side audio path.                                                                                                                                                                                                                                                                                                                                                                                               |
| **Audio Buffer:**                                             | Audio                                                                                                                                                                   | Increases the audio buffer to absorb VPN or SmartLink jitter.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Recording:** Radio Side / Client Side                       | Audio                                                                                                                                                                   | Selects whether recordings are captured at the radio or on this computer.                                                                                                                                                                                                                                                                                                                                                                       |
| **Save to:**                                                  | Audio                                                                                                                                                                   | Folder path where recordings are saved.                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Auto-record on TX**                                         | Audio                                                                                                                                                                   | Automatically starts recording whenever the radio transmits.                                                                                                                                                                                                                                                                                                                                                                                    |
| **Idle timeout:**                                             | Audio                                                                                                                                                                   | Seconds of silence after which an active recording stops automatically.                                                                                                                                                                                                                                                                                                                                                                         |
| TX Follows Active Slice                                       | TX follows the active slice. Mutually exclusive with 'Active Slice Follows TX'.                                                                                         | Disabled automatically during Split operation.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Active Slice Follows TX                                       | Switches the active slice when TX moves externally (e.g. WSJT-X or CAT). Mutually exclusive with 'TX Follows Active Slice'.                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Voice / CW / Digital filter sharpness sliders                 | Sets filter sharpness (0=lowest latency to 3=sharpest) per mode; slider is disabled when Auto is enabled.                                                               | Commands sent as 'radio filter_sharpness <mode> level=<N>'.                                                                                                                                                                                                                                                                                                                                                                                     |
| Auto (Voice / CW / Digital)                                   | Enables automatic filter-level selection for that mode; disables the manual sharpness slider.                                                                           | Commands sent as 'radio filter_sharpness <mode> auto_level=1'.                                                                                                                                                                                                                                                                                                                                                                                  |
| Connect / Disconnect (TGXL)                                   | Opens/closes direct TCP connection to the TGXL on port 9010. Saves IP and port to TGXL_ManualIp and TGXL_ManualPort on connect so AetherSDR auto-reconnects on startup. | Required to recover TUNE on firmware 4.2+. When connected, the TUNE button sends the native `autotune` command directly to the TGXL (TgxlConnection::requestAutotune()) instead of the radio-side `tgxl autotune handle=<H>` path broken in firmware 4.2. The TGXL drives radio PTT via its hardware interlock cable; no client-side keying is needed. If IP field is empty and radio has discovered the TGXL, the discovered IP is pre-filled. |
| Connect / Disconnect (PGXL)                                   | Opens/closes direct TCP connection to the Power Genius XL (default port 9008). Saves IP and port to PGXL_ManualIp and PGXL_ManualPort.                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Connect / Disconnect (Antenna Genius)                         | Opens/closes connection to the Antenna Genius (default port 9007). Saves IP and port to AG_ManualIp and AG_ManualPort.                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## RX tab — frequency calibration

In v0.9.2.1 the RX tab layout was revised. The calibration controls are now always visible regardless of whether a GPSDO is installed. A status label at the top of the group changes color and text to reflect the hardware present:

- **GPSDO installed** — label shown in green: "GPSDO installed. Manual frequency offset calibration available."
- **No GPSDO** — label shown in amber: "Manual frequency offset calibration available."

The **Cal Frequency (MHz):** field and **Start** button are now always present. When you click **Start**:

1. AetherSDR validates that the **Cal Frequency (MHz):** field is not empty. If it is empty, a status label next to the button displays "Enter cal frequency" in amber and the calibration does not proceed.
2. The radio's stored frequency error is reset to zero (`radio set freq_error_ppb=0`) before the sweep begins.
3. The **Start** button is disabled and its label changes to **Busy** for the duration of the calibration.
4. A status label to the right of the button reports progress ("Starting...", then live updates as the calibration runs).
5. When the calibration completes or fails, the button re-enables and the status label updates with the result.

The calibration procedure sends `radio set cal_freq=<value>`, then `radio set freq_error_ppb=0`, then starts the radio PLL sweep. Diagnostic messages are written to the protocol log channel.

**To run a manual frequency calibration:**

1. Open the **RX** tab.
2. Enter a known-accurate reference frequency in **Cal Frequency (MHz):**.
3. Click **Start**.
4. Wait for the status label to confirm completion. Do not change frequency or transmit during the sweep.

## Tips

- If you are operating over a VPN or SmartLink and hear audio dropouts, increase **Audio Buffer:** toward the higher end of its 50–1000 ms range.
- **Auto-record on TX** combined with **Idle timeout:** is useful for contest logging: recording starts when you key up and stops automatically after a configurable silence period.
- The **TX Band Settings** button on the TX tab opens the dedicated per-band power and tune dialog, the same one available at `Settings > TX Band Settings...`.
- If **Start** on the RX tab stays labeled **Busy** longer than expected, check that the **Cal Frequency (MHz):** value is a valid frequency reachable by the radio and that no other calibration is already in progress.

## Related

- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
- [Select iambic mode A or B for the radio keyer](select-iambic-mode-a-or-b-for-the-radio-keyer.md)
- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.
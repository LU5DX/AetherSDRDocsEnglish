# Radio Setup Overview

The Radio Setup dialog is the central configuration window for your connected FLEX-8600. It covers everything from radio identity and network settings to audio, TX behavior, filters, transverters, USB cables, and peripheral devices.

## Before you start

- AetherSDR must be connected to a radio. Radio Setup requires an active radio connection.

## How it works

Open Radio Setup from `Settings > Radio Setup...`. The dialog opens on the **Radio** tab. Eleven tabs are available; tabs other than **Radio** are built on first selection.

You can also jump directly to specific tabs:

- `Settings > FlexControl...` — opens the dialog on the **Serial** tab.
- `Settings > USB Cables...` — opens the dialog on the **USB Cables** tab.

The dialog remembers its size and position between sessions. Close it with the **Close** button; all changes take effect immediately when controls are adjusted — there is no global Apply or Save.

### Tab summary

| Tab | What it covers |
|---|---|
| **Radio** | Serial number, hardware version, region, licensed options, FlexControl and multiFLEX state, nickname, callsign, station name, license info, firmware update. |
| **Network** | Read-only IP/mask/MAC, DHCP vs. static IP, MTU, and private-IP enforcement. |
| **GPS** | GPS presence and live latitude, longitude, altitude, time, and satellite count. |
| **TX** | TX timings, interlock inputs, radio-level power cap, tune mode, waterfall TX display, TX/slice follow behavior, and a shortcut to TX Band Settings. |
| **Phone/CW** | Microphone level meter, iambic keyer, dit/dah swap, CW pitch sideband, CWX macro keying, CW decoder, and RTTY mark frequency default. |
| **RX** | GPSDO frequency offset calibration and 10 MHz reference source selection. |
| **Audio** | Radio line-out and headphone levels, PC audio device selection, audio compression codec, audio boost, audio buffer size, recording mode and folder, auto-record on TX, idle timeout, and NVIDIA BNR container control. |
| **Filters** | Low-latency vs. sharp filter preference per bandwidth, and forced low-latency filters for digital modes. |
| **XVTR** | Per-transverter configuration; create, configure, and remove transverter entries. |
| **USB Cables** | Assign detected USB serial adapters as CAT, BCD, bit, or PTT cable types with per-cable serial parameters. |
| **Peripherals** | Manual IP connection to external devices: TGXL, PGXL, and Antenna Genius. |
| **Serial** | FlexControl serial port selection, line parameters, DTR/RTS pin function and polarity, paddle swap, auto-open on startup, and tuning knob detect. (Present only when serial port support is built in.) |

## What each control does

The following controls persist settings in AetherSDR's AppSettings store. All other controls in the dialog communicate directly with the radio and are not stored locally.

| Label | Tab | Behavior | Default | Range | Setting key |
|---|---|---|---|---|---|
| **Audio Compression (SmartLink): Auto / Uncompressed / Opus** | Audio | Selects the audio codec used over SmartLink or LAN. | Auto | Auto, Uncompressed, Opus | `AudioCompression` |
| **Audio Boost:** | Audio | Enables extra gain on the client audio path. | — | On / Off | `AudioBoost` |
| **Audio Buffer:** | Audio | Enlarges the client-side audio buffer to absorb VPN or SmartLink jitter. | — | 50–1000 ms | `AudioBuffer` |
| **Recording: Radio Side / Client Side** | Audio | Selects whether recording is handled by the radio or by AetherSDR on the PC. | — | Radio Side, Client Side | `RecordMode` |
| **Save to:** | Audio | Folder path where recordings are saved. | — | Any valid path | `RecordDir` |
| **Auto-record on TX** | Audio | Starts recording automatically whenever the radio transmits. | — | On / Off | `AutoRecordTx` |
| **Idle timeout:** | Audio | Seconds of silence after which an active recording stops. | — | — | `RecordIdleTimeout` |

## Tips

- The **Audio Buffer:** spinbox (50–1000 ms) is most useful on high-latency or jittery network paths such as VPNs and SmartLink connections. Increase it if audio breaks up during remote operation.
- **Auto-record on TX** combined with **Idle timeout:** lets you capture transmissions as individual files without manually starting and stopping the recorder.
- The **Serial** tab only appears if AetherSDR was built with serial port support. If you do not see it, use `Settings > FlexControl...`, which will open the dialog and show the tab if it is available.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
- [Choose PC input/output audio devices](choose-pc-input-output-audio-devices.md)
- [Pick Opus vs uncompressed audio for SmartLink](pick-opus-vs-uncompressed-audio-for-smartlink.md)
- [Turn on audio boost or enlarge the audio buffer for remote operation](turn-on-audio-boost-or-enlarge-the-audio-buffer-for-remote-operation.md)
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)
- [Toggle low-latency vs sharp filters per bandwidth](toggle-low-latency-vs-sharp-filters-per-bandwidth.md)
- [Create a new transverter entry](create-a-new-transverter-entry.md)
- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)
- [Connect TGXL, PGXL or Antenna Genius by IP](../../getting-started/setup/connect-tgxl-pgxl-or-antenna-genius-by-ip.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)

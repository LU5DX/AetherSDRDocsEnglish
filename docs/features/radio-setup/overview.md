# Radio Setup Overview

The Radio Setup dialog is the central configuration window for your connected FLEX-8600. It brings together radio identification, network, GPS, transmit, audio, filters, transverters, USB cables, and peripherals into a single tabbed interface.

## Before you start

- AetherSDR must be connected to a FLEX-8600. The dialog requires an active radio connection.

## How it works

Open the dialog via `Settings > Radio Setup...`. The dialog stays open while you work; close it with the Close button when finished.

The dialog is organized into tabs. Each tab covers a distinct area of radio configuration. Tabs other than Radio are built on first access, so there may be a brief delay the first time you click a tab.

You can also jump directly to specific tabs:

- `Settings > FlexControl...` opens the dialog on the Serial tab.
- `Settings > USB Cables...` opens the dialog on the USB Cables tab.

### Tab summary

| Tab | What it covers |
|---|---|
| Radio | Radio identification, nickname, callsign, station name, license info, and firmware update. |
| Network | IP address, MTU, DHCP vs. static IP, and private-IP enforcement. |
| GPS | GPS presence and live position, altitude, time, and satellite data. |
| TX | TX timings, interlocks, max power (0–100 %), tune mode, waterfall TX display, and TX/slice follow behavior. |
| Phone/CW | Microphone level meter, iambic keyer, dit/dah swap, CW pitch sideband (LSB or USB), CWX, CW decoder, and RTTY mark default. |
| RX | GPSDO frequency calibration, manual frequency offset (ppb), and 10 MHz reference source (Internal or External). |
| Audio | Radio audio outputs (line out, headphone, front speaker), PC audio device selection, audio compression, boost, buffer, recording, and NVIDIA BNR noise removal. |
| Filters | Low Latency vs. Sharp filter preference per bandwidth, with an option to force low-latency filters for digital modes. |
| XVTR | Per-transverter configuration: RX-only mode, remove, and Create New Transverter. |
| USB Cables | Assigns USB serial adapters to CAT, BCD, bit, and PTT cable types with full serial parameter control. |
| Peripherals | Manual IP connection for TGXL, PGXL, and Antenna Genius devices. |
| Serial | FlexControl serial port selection, line parameters, pin function assignment, paddle swap, auto-open, and FlexControl tuning knob detection. (Shown only when serial port support is compiled in.) |

### Audio and recording settings

The Audio tab holds the controls with persisted settings most commonly adjusted for remote and SmartLink operation.

| Control | What it does | Setting key | Default | Range |
|---|---|---|---|---|
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Selects the audio codec used over SmartLink or LAN. | `AudioCompression` | Auto | Auto, Uncompressed, Opus |
| Audio Boost: | Enables extra gain on the client audio path. | `AudioBoost` | — | On / Off |
| Audio Buffer: | Increases the audio buffer to absorb VPN or SmartLink jitter. | `AudioBuffer` | — | 50–1000 ms |
| Recording: Radio Side / Client Side | Selects whether recording happens on the radio or on this computer. | `RecordMode` | — | Radio Side, Client Side |
| Save to: | Folder where recordings are saved. | `RecordDir` | — | Any valid path |
| Auto-record on TX | Starts recording automatically whenever you transmit. | `AutoRecordTx` | — | On / Off |
| Idle timeout: | Seconds of silence after which an active recording stops. | `RecordIdleTimeout` | — | — |

## Tips

- The TX Band Settings shortcut on the TX tab opens the dedicated per-band power and tune dialog, the same one accessible via `Settings > TX Band Settings...`.
- Station Name defaults to the OS hostname if left blank. It identifies this client to other multiFLEX stations.
- The Serial tab appears only on builds that include serial port support. If you do not see it, use `Settings > FlexControl...` to confirm whether serial support is available on your installation.

## Related

- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
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

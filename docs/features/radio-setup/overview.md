# Radio Setup Overview

Radio Setup is the master per-radio configuration dialog in AetherSDR. It brings together every hardware and software setting that is specific to a connected FLEX-8600: identification, network, GPS, transmit, audio, filters, transverters, USB cables, and peripherals.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Radio Setup requires an active radio connection.

## How it works

Open Radio Setup from `Settings > Radio Setup...`. The dialog contains a set of tabs; each tab groups related settings. Tabs other than Radio are built on first access, so there may be a brief delay the first time you click a tab.

You can also jump directly to specific tabs:

- `Settings > USB Cables...` opens the dialog with the USB Cables tab active.
- `Settings > FlexControl...` opens the dialog with the Serial tab active.

The dialog remembers its size and position between sessions.

### Tab summary

| Tab | What it covers |
|---|---|
| Radio | Serial number, hardware version, region, licensed options, nickname, callsign, station name, license info, firmware update. |
| Network | IP address, MAC address, MTU, DHCP/static IP switching, private IP enforcement. |
| GPS | GPS presence and live position, altitude, time, and satellite count. |
| TX | TX timings, interlocks, max power cap (0–100 %), tune mode, waterfall TX display, TX/slice follow modes, and a shortcut to TX Band Settings. |
| Phone/CW | Microphone level meter, iambic keyer, dit/dah swap, CW sideband, CWX, CW decoder, RTTY mark default. |
| RX | GPSDO frequency offset calibration, manual frequency offset in ppb, 10 MHz reference source (Internal or External). |
| Audio | Radio line-out and headphone levels, PC audio device selection, audio compression, audio boost, audio buffer, recording mode and folder, auto-record on TX, idle timeout, NVIDIA BNR container. |
| Filters | Low Latency or Sharp filter family per bandwidth, with an option to force low-latency filters for digital modes. |
| XVTR | Per-transverter configuration, RX-only toggle, remove, and Create New Transverter. |
| USB Cables | Assigns USB serial adapters to CAT, BCD, bit, and PTT cable types with per-cable serial parameters. |
| Peripherals | Manual IP connection for TGXL, PGXL, and Antenna Genius peripherals. |
| Serial | FlexControl serial port selection, line parameters, DTR/RTS pin function assignment, paddle swap, auto-open on startup. (Present only when serial port support is available.) |

## What each control does

The following settings are persisted by AetherSDR across sessions.

| Label | Tab | Behavior | Default | Range | Setting key |
|---|---|---|---|---|---|
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Audio | Selects the audio codec used for SmartLink and LAN connections. | Auto | Auto, Uncompressed, Opus | `AudioCompression` |
| Audio Boost: | Audio | Enables extra gain on the client audio path. | — | On/Off | `AudioBoost` |
| Audio Buffer: | Audio | Increases the audio buffer to absorb jitter on VPN or SmartLink connections. | — | 50–1000 ms | `AudioBuffer` |
| Recording: Radio Side / Client Side | Audio | Selects whether recordings are captured at the radio or on the client PC. | — | Radio Side, Client Side | `RecordMode` |
| Save to: | Audio | Sets the folder where recordings are saved. | — | Any valid path | `RecordDir` |
| Auto-record on TX | Audio | Automatically starts recording whenever the radio transmits. | — | On/Off | `AutoRecordTx` |
| Idle timeout: | Audio | Number of seconds of silence before an active recording stops. | — | — | `RecordIdleTimeout` |

## Tips

- If you are operating over a VPN or SmartLink and hear choppy audio, increase `AudioBuffer` (Audio tab) and consider setting `AudioCompression` to Opus.
- The Serial tab is only present when AetherSDR was built with serial port support. If you do not see it, use `Settings > FlexControl...` as a shortcut — it will open the dialog and indicate whether the tab is available.
- The dialog reopens at the tab you last used within the session, but always starts on the Radio tab after a fresh launch.

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

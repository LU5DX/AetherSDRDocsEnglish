# Radio Setup Overview

The Radio Setup dialog is the central configuration window for your FLEX-8600. It collects all per-radio settings — identification, network, GPS, transmit, audio, filters, transverters, USB cables, and external peripherals — into a single tabbed interface.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. Radio Setup requires an active radio connection.

## How it works

Open the dialog from `Settings > Radio Setup...`. AetherSDR also provides two shortcuts that open the dialog directly at a specific tab: `Settings > FlexControl...` jumps to the Serial tab, and `Settings > USB Cables...` jumps to the USB Cables tab.

The dialog contains the following tabs:

**Radio** — Displays read-only hardware information (serial number, region, hardware version, licensed options, FlexControl state, multiFLEX state) and editable identification fields (Nickname, Callsign, Station Name). Also shows license details and provides firmware update controls.

**Network** — Shows the radio's current IP address, subnet mask, and MAC address. Allows switching between DHCP and static IP, setting a custom network MTU, and enforcing private IP connections.

**GPS** — Displays live GPS data (latitude, longitude, altitude, time, satellite count) when a GPS receiver is present.

**TX** — Controls transmit timing, TX/RCA interlocks, maximum output power (0–100 %), tune mode, waterfall TX display, and TX/slice follow behavior. Opens the per-band TX Band Settings dialog via the `TX Band Settings` button.

**Phone/CW** — Configures the microphone level meter, iambic keyer (Iambic, Swap), CW sideband (LSB or USB), CWX macro keying, CW decoder, and RTTY mark frequency default.

**RX** — Provides GPSDO frequency calibration (Cal Frequency, Freq Offset in ppb, Start) and selects the 10 MHz reference source (Internal or External).

**Audio** — Controls radio-side output levels (Line Out, Headphone, Front Speaker) with mute buttons, selects the audio codec for SmartLink (`AudioCompression`: Auto, Uncompressed, or Opus), picks PC audio input and output devices, enables `AudioBoost`, sets the `AudioBuffer` size (50–1000 ms), configures recording options, and manages the NVIDIA BNR noise-removal container.

**Filters** — Selects Low Latency or Sharp filter families per bandwidth, and optionally forces low-latency filters for digital modes (DIGU/DIGL).

**XVTR** — Creates and manages transverter definitions. Each transverter entry has its own nested tab with RX Only mode and a Remove button. The `Create New Transverter` button adds a new entry.

**USB Cables** — Lists detected USB serial adapters with their plugged/unplugged status and assigns each cable a type (CAT, BCD, bit, or PTT) with full serial parameter configuration.

**Peripherals** — Connects external devices (TGXL, PGXL, Antenna Genius) by IP address using per-device Connect and Disconnect buttons.

**Serial** — Configures the FlexControl serial port: port selection, baud/data/parity/stop parameters, DTR/RTS function and polarity assignment, paddle swap, and FlexControl tuning knob detection. This tab is only present when AetherSDR is built with serial port support.

## What each control does

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | Selects the audio codec used over SmartLink or LAN | Auto | Auto, Uncompressed, Opus | `AudioCompression` |
| Audio Boost: | Enables extra gain on the client audio path | — | On / Off | `AudioBoost` |
| Audio Buffer: | Increases the client audio buffer to absorb VPN or SmartLink jitter | — | 50–1000 ms | `AudioBuffer` |
| Recording: Radio Side / Client Side | Selects whether audio is recorded at the radio or on this PC | — | Radio Side, Client Side | `RecordMode` |
| Save to: | Folder path where recordings are saved | — | Any writable path | `RecordDir` |
| Auto-record on TX | Automatically starts recording when the radio transmits | — | On / Off | `AutoRecordTx` |
| Idle timeout: | Seconds of silence after which an active recording stops | — | — | `RecordIdleTimeout` |

## Tips

- The dialog remembers its size and position between sessions. Resize it once and it reopens at the same dimensions.
- Station Name defaults to the OS hostname if left blank. It identifies this AetherSDR client to other multiFLEX stations on the same radio.
- Increasing `AudioBuffer` reduces audio dropouts over high-latency links at the cost of added delay.

## Related

- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)
- [Set the radio nickname, callsign and station name](set-the-radio-nickname-callsign-and-station-name.md)
- [Upload a new firmware .ssdr to the radio](upload-a-new-firmware-ssdr-to-the-radio.md)
- [Switch the radio between DHCP and static IP](switch-the-radio-between-dhcp-and-static-ip.md)
- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Set per-band TX max power and tune mode](set-per-band-tx-max-power-and-tune-mode.md)
- [Calibrate the GPSDO frequency offset](calibrate-the-gpsdo-frequency-offset.md)
- [Switch to an external 10 MHz reference](switch-to-an-external-10-mhz-reference.md)
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

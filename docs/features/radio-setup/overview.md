# Radio Setup Overview

The Radio Setup dialog is the central configuration window for your FLEX-8600. It brings together radio identification, network, GPS, transmit, audio, filters, transverters, USB accessories, external peripherals, and (on supported builds) FlexControl serial — all in one place. Open it once to orient yourself; return to specific tabs whenever you need to change a setting.

## How it works

Open the dialog with `Settings > Radio Setup...`. The dialog has a tab bar across the top; each tab covers a distinct area of radio configuration. Tabs are built on first use, so switching to a tab for the first time may take a moment while AetherSDR probes connected hardware.

You can also jump directly to specific tabs via `Settings > USB Cables...` (opens the USB Cables tab) and `Settings > FlexControl...` (opens the Serial tab, where available).

The dialog has no Apply or OK button for most tabs — changes take effect immediately when you interact with a control. The exception is the Network tab, which has its own "Apply" button. Close the dialog with the "Close" button at the bottom.

### Tab summary

| Tab | What it covers |
|---|---|
| Radio | Serial number, region, hardware version, licensed options, nickname, callsign, station name, license info, and firmware update. |
| Network | Read-only IP/MAC addresses, DHCP/Static switching, static IP fields, MTU, and private-IP enforcement. |
| GPS | GPS presence indicator and live latitude, longitude, altitude, time, and satellite count. |
| TX | TX timing, interlocks, max power cap (0–100 %), tune mode, waterfall TX display, TX/slice follow modes, and a shortcut to TX Band Settings. |
| Phone/CW | Microphone level meter, iambic keyer, dit/dah swap, CW sideband, CWX macros, CW decoder, and RTTY mark default. |
| RX | GPSDO frequency calibration, manual frequency offset (ppb), and 10 MHz reference source (Internal or External). |
| Audio | Line-out and headphone gain and mute, PC audio device selection, audio compression codec, audio boost, audio buffer size, recording mode and folder, auto-record on TX, idle timeout, and NVIDIA BNR container controls. |
| Filters | Low Latency or Sharp filter selection per bandwidth, and a separate option to force low-latency filters in digital modes. |
| XVTR | Per-transverter configuration tabs, RX-only toggle, remove, and Create New Transverter. |
| USB Cables | Lists detected USB serial adapters; assigns each as CAT, BCD, bit, or PTT with full serial parameters. |
| Peripherals | Manual IP-based connection and disconnection for TGXL, PGXL, and Antenna Genius. |
| Serial | FlexControl serial port selection, line parameters, DTR/RTS pin assignment, paddle swap, auto-open on startup, and tuning knob detect/close. Available only on builds with serial port support. |

### Persisted settings on the Audio tab

The following settings are saved in AetherSDR's application settings and persist across sessions.

| Control | Setting key | Default | Valid range | What it does |
|---|---|---|---|---|
| Audio Compression (SmartLink): Auto / Uncompressed / Opus | `AudioCompression` | Auto | Auto, Uncompressed, Opus | Selects the audio codec used over SmartLink or LAN. |
| Audio Boost: | `AudioBoost` | — | On / Off | Enables extra gain on the client audio path. |
| Audio Buffer: | `AudioBuffer` | — | 50–1000 ms | Increases the audio buffer to absorb VPN or SmartLink jitter. |
| Recording: Radio Side / Client Side | `RecordMode` | — | Radio Side, Client Side | Selects whether recording happens on the radio or on this PC. |
| Save to: | `RecordDir` | — | Any writable folder path | Folder where recordings are saved. |
| Auto-record on TX | `AutoRecordTx` | — | On / Off | Starts recording automatically whenever you transmit. |
| Idle timeout: | `RecordIdleTimeout` | — | — (seconds) | Seconds of silence after which an auto-started recording stops. |

## Tips

- If `Settings > FlexControl...` is not visible in your menu, the build does not include serial port support.
- The Serial tab is also absent from the tab bar in that case.
- TX Band Settings can be reached from `Settings > TX Band Settings...` in the menu or from the "TX Band Settings" button inside the TX tab.

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

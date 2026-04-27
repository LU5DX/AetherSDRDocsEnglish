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
| **RX** | GPSDO frequency calibration and 10 MHz reference source selection. |
| **Audio** | Line out, headphone, and speaker levels; audio compression codec; PC audio device selection; audio boost; audio buffer size; recording mode, folder, auto-record on TX, and idle timeout; NVIDIA BNR container control. |
| **Filters** | Low-latency vs. sharp filter selection per bandwidth, and a separate option for digital modes. |
| **XVTR** | Per-transverter configuration; create or remove transverter entries. |
| **USB Cables** | Assign USB serial adapters to CAT, BCD, bit, and PTT cable types and configure their serial parameters. |
| **Peripherals** | Manual IP connection to external devices: TGXL, PGXL, and Antenna Genius. |
| **Serial** | FlexControl serial port selection, line parameters, pin function assignments (DTR/RTS), paddle swap, auto-open, and tuning knob detection. (Visible only when serial port support is built in.) |

## What each control does

The following controls have persisted settings keys.

| Control | Tab | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|---|
| **Audio Compression (SmartLink):** Auto / Uncompressed / Opus | Audio | Selects the audio codec used over SmartLink or LAN. | Auto | Auto, Uncompressed, Opus | `AudioCompression` |
| **Audio Boost:** | Audio | Enables extra gain on the client-side audio path. | — | Enabled / Disabled | `AudioBoost` |
| **Audio Buffer:** | Audio | Increases the audio buffer to absorb VPN or SmartLink jitter. | — | 50–1000 ms | `AudioBuffer` |
| **Recording:** Radio Side / Client Side | Audio | Selects whether recordings are captured at the radio or on this computer. | — | Radio Side, Client Side | `RecordMode` |
| **Save to:** | Audio | Folder path where recordings are saved. | — | Any valid directory path | `RecordDir` |
| **Auto-record on TX** | Audio | Automatically starts recording whenever the radio transmits. | — | Checked / Unchecked | `AutoRecordTx` |
| **Idle timeout:** | Audio | Seconds of silence after which an active recording stops automatically. | — | — | `RecordIdleTimeout` |

## Tips

- If you are operating over a VPN or SmartLink and hear audio dropouts, increase **Audio Buffer:** toward the higher end of its 50–1000 ms range.
- **Auto-record on TX** combined with **Idle timeout:** is useful for contest logging: recording starts when you key up and stops automatically after a configurable silence period.
- The **TX Band Settings** button on the TX tab opens the dedicated per-band power and tune dialog, the same one available at `Settings > TX Band Settings...`.

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
- [Enable auto-record on TX and pick a save folder](enable-auto-record-on-tx-and-pick-a-save-folder.md)
- [Start/stop the NVIDIA BNR container](start-stop-the-nvidia-bnr-container.md)
- [Toggle low-latency vs sharp filters per bandwidth](toggle-low-latency-vs-sharp-filters-per-bandwidth.md)
- [Create a new transverter entry](create-a-new-transverter-entry.md)
- [Assign a USB cable as CAT, BCD, bit or PTT](assign-a-usb-cable-as-cat-bcd-bit-or-ptt.md)
- [Connect TGXL, PGXL or Antenna Genius by IP](../../getting-started/setup/connect-tgxl-pgxl-or-antenna-genius-by-ip.md)
- [Configure FlexControl serial port pin functions](configure-flexcontrol-serial-port-pin-functions.md)

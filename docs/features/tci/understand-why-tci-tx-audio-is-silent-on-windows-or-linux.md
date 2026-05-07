# Understand why TCI TX audio is silent on Windows or Linux

AetherSDR routes DAX TX audio through a platform-aware policy in the main window. On Windows and Linux, the TCI TX audio path has specific requirements that, if unmet, produce silence with no error message.

## Before you start

- Confirm you are running AetherSDR on Windows or Linux (macOS uses a different DAX TX routing path).
- Confirm your FlexRadio hardware is connected and the slice you intend to transmit on is visible in the main window.

## Steps

1. Open the AetherSDR main window (launched automatically on application start).
2. Check that your system default audio **output** device is available and not disabled. AetherSDR selects the default output device automatically for the local audio sink; if no default device is present, the TX audio chain starts but produces silence.
3. Verify that the TX chain is active: look for an active transmit state on the target slice in the main window. If the slice is not in TX, no audio is passed to the DAX TX path regardless of input level.
4. If you recently changed your default audio device in the OS, restart the RX/TX stream by disconnecting and reconnecting to the radio from the main window. The local audio sink is opened once at stream start and does not re-enumerate devices mid-session.

## What each control does

| Control | Behavior |
|---|---|
| Default system audio output device (OS setting) | AetherSDR selects this device automatically when the RX stream starts. If no default device is found, the local audio sink fails to open and TX audio is silent. |
| FlexRadio connection (LAN / SmartLink) | Must be active for the TX audio chain to receive data. A dropped WAN connection triggers automatic reconnection; the audio chain restarts once the connection is restored. |
| TX slice state | The DAX TX path only passes audio when the selected slice is actively transmitting. Confirm the slice shows TX active in the main window. |

## Tips

- On Linux, check that PulseAudio or PipeWire has a default sink configured (`pactl info | grep "Default Sink"`). AetherSDR calls the Qt `QMediaDevices::defaultAudioOutput()` API; if the system reports no default output, the local sink will not open.
- On Windows, open **Sound > Playback** in Control Panel and confirm a default playback device is set and not disabled. Disabled or unplugged devices are not returned by the audio API and cause silent TX.
- If TX audio was working and then went silent after a system sleep/wake cycle, disconnect and reconnect to the radio to force the audio stream to restart and re-acquire the output device.

## Related

- [DAX TX routing overview](dax-tx-routing.md)
- [Connect to FlexRadio over SmartLink WAN](smartlink-wan-connect.md)
- [NR2 noise-reduction setup](nr2-noise-reduction.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->

# Troubleshoot DAX RX audio routing or double-speed playback

`PanadapterStream::registerDaxStream` routes incoming audio packets for a specific DAX channel to the correct audio output by registering the radio's stream ID with a DAX channel number. Misconfiguration here causes audio to reach the wrong channel or play back at double speed.

## Before you start

- Confirm the radio is connected and at least one DAX RX channel is enabled.
- Note which DAX channel number your application is listening on.

## Steps

1. Check that each application consuming DAX RX audio is assigned a **unique** DAX channel number. If two applications share the same channel, each receives every packet intended for that channel, which can produce double-speed playback because both consumers advance through the stream simultaneously.
2. If playback runs at double speed on a single application, verify the sample rate your audio driver or application expects matches the rate the radio is streaming. A mismatch of 2× (for example, driver configured for 48 000 Hz when the stream is 24 000 Hz) causes the audio engine to consume samples twice as fast as they arrive, doubling perceived speed.
3. If audio is routed to the wrong channel, disconnect and reconnect the DAX session so that `registerDaxStream` re-registers the stream ID against the correct channel number. Do this from your host application's DAX settings or by toggling the DAX RX channel off and back on in AetherSDR.
4. If you are running SmartSDR DAX2 alongside AetherSDR, be aware that DAX2 owns the Windows audio device layer for TX. RX routing is handled independently per channel by AetherSDR, but conflicts on shared audio devices can still misdirect RX audio. Assign each DAX RX channel to a dedicated virtual audio device to isolate streams.

## What each control does

| Control | Behavior |
|---|---|
| DAX channel number | Identifies which radio stream slot receives audio packets. Must be unique per consuming application. |
| Stream ID registration | `registerDaxStream` binds the radio-assigned stream ID to the selected channel number. Called automatically on DAX session start; re-triggered by toggling the channel off and on. |
| Sample rate setting | Must match the radio's configured DAX sample rate. A 2× mismatch between driver and stream rate produces double-speed playback. |

## Tips

- Toggle the DAX RX channel off, wait two seconds, then turn it back on to force a clean re-registration if audio is absent or misrouted after a reconnect.
- Use a per-channel virtual audio cable (e.g. VAC or VB-Audio) so each DAX channel maps to exactly one audio device, eliminating cross-channel bleed.
- Check the AetherSDR debug log for `lcVita49` entries — byte-count messages confirm packets are being sent and received on the expected stream.

## Related

- [dax-rx-channels.md](dax-rx-channels.md)
- [dax-tx-policy.md](dax-tx-policy.md)
- [panadapter-stream.md](panadapter-stream.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->

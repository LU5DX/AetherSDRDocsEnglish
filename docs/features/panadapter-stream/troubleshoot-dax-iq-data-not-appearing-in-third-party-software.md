# Troubleshoot DAX IQ data not appearing in third-party software

`PanadapterStream::registerIqStream` routes incoming DAX IQ baseband samples to the correct consumer by mapping the radio's stream ID to a channel number. If this mapping is missing or incorrect, third-party software receives no data.

## Before you start

- Confirm the radio is connected and the DAX IQ channel is enabled in AetherSDR.
- Confirm your third-party software is configured to receive on the correct DAX IQ channel number.
- Ensure no firewall or antivirus software is blocking UDP traffic on the port AetherSDR uses for the stream.

## Steps

1. **Verify the DAX IQ channel assignment.** In AetherSDR, open the DAX settings panel and confirm that the IQ channel number shown matches the channel number configured in your third-party software. A mismatch here prevents `registerIqStream` from routing samples to the correct consumer.

2. **Check for stream registration errors.** Enable diagnostic logging in AetherSDR (if available) and look for messages referencing `PanadapterStream` and the IQ stream ID. A missing or zero stream ID means the radio has not yet assigned a stream, and no data will flow regardless of channel settings.

3. **Restart the DAX IQ stream.** Disable the DAX IQ channel in AetherSDR, wait two seconds, then re-enable it. This forces a new stream ID registration and re-runs the routing logic.

4. **Confirm UDP registration completed.** AetherSDR sends a UDP registration packet to the radio when the stream starts. If the radio is unreachable at that moment, registration silently fails. Check your network connection, then restart the stream as described in step 3.

5. **Rule out a packet error condition.** Sustained packet errors can stall the stream pipeline. If your diagnostic log shows a rising packet error count, check for network congestion or RF overload causing the radio to drop packets, then reduce the IQ sample rate if your radio supports it.

## What each control does

| Control | Behavior |
|---|---|
| DAX IQ channel number | Identifies which channel the radio's stream ID is mapped to. Must match the channel number set in your third-party software. |
| DAX IQ enable toggle | Activating this triggers stream ID registration with the radio. Toggling it off and on resets the registration. |

## Tips

- If you have multiple panadapters open, each has its own stream. Confirm you are enabling the DAX IQ channel on the panadapter that covers the frequency your third-party software expects.
- After any network interruption, toggle the DAX IQ channel off and on to force re-registration — AetherSDR does not automatically re-register a lost stream.

## Related

- [Configure DAX IQ channels](configure-dax-iq-channels.md)
- [DAX audio troubleshooting](troubleshoot-dax-audio.md)
- [Network and UDP setup](network-udp-setup.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->

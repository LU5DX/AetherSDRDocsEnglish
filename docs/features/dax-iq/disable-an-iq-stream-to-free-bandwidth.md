# Disable an IQ stream to free bandwidth

Each active DAX IQ stream consumes radio DSP resources and network bandwidth. Disabling a stream you are not using releases that capacity for other slices, audio streams, or IQ channels.

## Before you start

- AetherSDR must be connected to the radio. The DAX IQ applet requires an active radio connection.
- The DAX IQ applet must be visible. If it is not, click the IQ tray button on the right sidebar to show it.

## Steps

1. Locate the row for the channel you want to stop — IQ 1, IQ 2, IQ 3, or IQ 4.
2. Check that the toggle button on the right of that row shows "On". If it already shows "Off", the stream is already inactive.
3. Click "On". The button label changes to "Off", the button style dims, and the level meter resets to 0. The stream is removed from the radio for this session.

## What each control does

| Control | Default | Behavior | Persisted key |
|---|---|---|---|
| IQ 1..4 Off/On | Off | Clicking toggles the stream. When turned off, the button shows "Off" and the meter resets to 0. | `DaxIqEnabled1` – `DaxIqEnabled4` |
| IQ 1..4 meter | 0 | Displays the RMS level of the stream (0–100). Resets to 0 when the stream is disabled or the radio disconnects. | — |
| IQ 1..4 rate | 48k | Sets the sample rate for the channel (24k, 48k, 96k, 192k). Unchanged by disabling the stream. | `DaxIqRate1` – `DaxIqRate4` |

## Tips

- IQ streams are per-session. The radio does not persist stream state across connections. AetherSDR stores your last enable/disable choice in `DaxIqEnabled1` through `DaxIqEnabled4` and restores those streams automatically about 1.5 seconds after reconnecting.
- If you want a channel to stay off after a reconnect, disabling it here is sufficient — the persisted key is set to `False` immediately when you click "On" to turn it off.
- Disabling a stream also clears the level meter. If the meter continues to show a non-zero reading after you click "Off", the radio state has not yet synced; the button will update again once the radio confirms the stream was removed.

## Troubleshooting

- **Button shows "Off" but immediately returns to "On"** — The radio may be restoring a persisted stream state on reconnect. Wait for the 1.5-second session setup delay to complete, then click "On" to disable the stream again.
- **Level meter does not reset to 0 after disabling** — The radio stream removal confirmation has not yet arrived. The meter will reset once the radio reports the stream no longer exists.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)

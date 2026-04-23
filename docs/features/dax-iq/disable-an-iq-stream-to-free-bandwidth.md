# Disable an IQ stream to free bandwidth

Disabling an active DAX IQ stream stops it from consuming radio DSP bandwidth and network throughput. Do this when an external SDR application no longer needs the IQ data, or when you want to reclaim resources for other slices.

## Before you start

- AetherSDR must be connected to a Flex radio. The DAX IQ applet requires an active radio connection.
- Open the DAX IQ applet by clicking the IQ tray button on the right sidebar. The applet is hidden by default.
- Identify which channel (IQ 1–4) you want to disable. The toggle button for that channel must currently show "On".

## Steps

1. Click the IQ tray button on the right sidebar to reveal the DAX IQ applet if it is not already visible.
2. Find the row for the channel you want to stop — IQ 1, IQ 2, IQ 3, or IQ 4.
3. Click the "On" button at the right end of that row.
4. The button label changes to "Off", the button style changes to the inactive appearance, and the level meter resets to 0.

The stream is now disabled. The radio stops transmitting IQ data for that channel.

## What each control does

| Control | What it does | Default | Valid values |
|---|---|---|---|
| IQ 1–4 Off/On | Toggles the IQ stream for that channel on or off. When clicked while "On", disables the stream and resets the meter. | Off | Off, On |
| IQ 1–4 rate | Sets the sample rate for the channel. Has no effect while the stream is disabled, but retains its value. | 48k | 24k, 48k, 96k, 192k |
| IQ 1–4 meter | Shows real-time RMS level of the IQ stream. Resets to 0 immediately when the stream is disabled. | 0 | 0–100 |

## Tips

- IQ streams are per-session and are not persisted by the radio. If AetherSDR disconnects and reconnects, all four channels return to "Off" regardless of their previous state.
- Disabling a stream also resets its level meter to 0. If the meter continues to read above 0 briefly after clicking "Off", it will settle once the radio confirms the stream has stopped and the button state syncs back from the radio.
- If external SDR software is still holding the stream open, the button may revert to "On" when the radio reports stream state back to AetherSDR. Close the external application first, then disable the stream.

## Troubleshooting

- **Button reverts to "On" immediately after clicking** — The radio is reporting the stream as still active, likely because external software connected to that IQ channel is keeping it open. Close the external application and try again.
- **Level meter does not reset to 0** — The meter resets when the radio confirms the stream is gone. A brief delay is normal. If it does not reset at all, the stream may not have been successfully disabled; check your radio connection status.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [DAX IQ overview](overview.md)

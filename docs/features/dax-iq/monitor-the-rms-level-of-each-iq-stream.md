# Monitor the RMS level of each IQ stream

The DAX IQ applet displays a real-time level meter for each of the four IQ streams, letting you confirm that an active stream is carrying signal and roughly gauge its strength.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- At least one IQ stream must be enabled (button shows "On"). The meter reads 0 when a stream is off or the radio is disconnected.

## Steps

1. Click the "IQ" tray button on the right sidebar to open the DAX IQ applet.
2. Locate the row for the channel you want to watch: **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. Confirm the toggle button on the right of that row shows "On". If it shows "Off", the meter will remain at 0.
4. Observe the progress bar in the middle of the row. It updates in real time as the stream carries signal.

## What each control does

| Control | Description | Default | Range |
|---|---|---|---|
| IQ 1–4 meter | Progress bar showing the RMS level of the IQ stream. Scaled from the raw RMS value × 200. | 0 | 0–100 |
| IQ 1–4 Off/On | Toggles the IQ stream on or off. The meter resets to 0 when switched to "Off". | Off | Off / On |
| IQ 1–4 rate | Sample rate for the IQ stream. Does not affect the meter scale. | 48k | 24k, 48k, 96k, 192k |

None of these controls have persisted setting keys that affect the meter directly. The meter state is live and resets to 0 on disconnect or disable.

## Tips

- A meter reading of 0 on an "On" stream can indicate no signal within the slice, a misconfigured receiver, or a network issue dropping IQ packets.
- The meter resets to 0 automatically when the radio disconnects or when the stream is toggled to "Off". This is expected behavior, not an error.
- The meter scale is 0–100, derived from RMS × 200. A full-scale reading (100) corresponds to an RMS value of 0.5 or above.

## Troubleshooting

- **Meter stays at 0 even though the stream is "On"** — The radio may still be setting up the stream. Wait a moment after enabling; the radio connection requires a short settling period before stream data flows. If the meter remains at 0, verify that your external SDR software is connected to the correct IQ channel and that the radio has an active slice on that channel.
- **Meter resets to 0 after reconnecting** — This is normal. Streams are per-session and not preserved by the radio across connections. AetherSDR re-enables persisted streams automatically after reconnect.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [DAX IQ overview](overview.md)

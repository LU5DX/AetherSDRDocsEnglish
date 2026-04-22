# Monitor the RMS level of each IQ stream

The DAX IQ applet shows a real-time level meter for each of the four IQ streams. Use it to confirm that an active stream is carrying signal before routing it to external software.

## Before you start

- AetherSDR must be connected to the radio. The DAX IQ applet requires an active radio connection.
- At least one IQ stream must be enabled (toggled to "On"). The meter reads 0 when a stream is off or the radio is disconnected.

## Steps

1. Click the **IQ** tray button on the right sidebar to open the DAX IQ applet.
2. Locate the row for the channel you want to monitor: **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. Confirm the toggle button on that row reads **On**. If it reads **Off**, enable the stream first — see [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md).
4. Watch the level meter in the center of the row. It updates in real time as the stream carries signal.

## What each control does

| Control | What it shows | Range | Default |
|---|---|---|---|
| IQ 1–4 meter | RMS level of the IQ stream, scaled from the raw RMS value (RMS × 200) | 0–100 | 0 |
| IQ 1–4 Off/On | Whether the stream is active on the radio | Off / On | Off |

The meter resets to 0 when the stream is toggled to **Off** or the radio disconnects.

## Tips

- A meter that stays at 0 on an **On** stream indicates no IQ data is arriving. Check that the sample rate is set and that the radio has an active slice on that channel.
- The meter scale is 0–100, derived by multiplying the raw RMS value by 200. IQ amplitude values typically fall in the 0.0–0.5 range, so a reading of 100 represents full scale.
- The meter does not persist between sessions. IQ streams are per-session and are not saved by the radio.

## Troubleshooting

- **Meter shows 0 even though the stream is On** — The radio may not yet be sending data on that channel. Verify a slice receiver is assigned to the IQ channel in your radio configuration. Also confirm the external application has opened the stream.
- **Meter resets to 0 after reconnecting** — Expected behavior. IQ streams are per-session. Toggle the stream back to **On** after each connection.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [DAX IQ overview](overview.md)

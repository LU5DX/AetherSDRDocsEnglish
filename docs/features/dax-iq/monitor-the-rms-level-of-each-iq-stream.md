# Monitor the RMS level of each IQ stream

The DAX IQ applet includes a real-time level meter for each of the four IQ streams. Use it to confirm that an active stream is receiving signal and to get a rough sense of input level.

## Before you start

- AetherSDR must be connected to the radio. The meters only update when a stream is active.
- At least one IQ stream must be enabled (button shows "On"). A disabled stream holds the meter at 0.

## Steps

1. Click the **IQ** tray button on the right sidebar to open the DAX IQ applet.
2. Locate the row for the channel you want to watch — **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. If the toggle button for that row shows "Off", click it so it shows "On" to start the stream.
4. Observe the level meter in that row. It updates in real time as IQ data arrives from the radio.

## What each control does

| Control | Description | Default | Range |
|---|---|---|---|
| IQ 1–4 meter | Displays the RMS level of the IQ stream as a bar graph. Resets to 0 when the stream is disabled or the radio disconnects. | 0 | 0–100 (scaled from RMS × 200) |
| IQ 1–4 Off/On | Enables or disables the IQ stream for that channel. The meter only updates while the button shows "On". | Off | Off / On |
| IQ 1–4 rate | Sets the sample rate for that channel's stream. | 48k | 24k, 48k, 96k, 192k |

## Tips

- A meter that stays at 0 while the button shows "On" can indicate the stream was not accepted by the radio yet. Disconnect and reconnect; AetherSDR re-enables persisted streams automatically after the session settles.
- The meter scale runs 0–100 internally, derived by multiplying the raw RMS value by 200. IQ signal levels in normal operation typically fall in the lower portion of the scale.
- The meter has no text readout; it is a bar only. For a precise RMS value, use the receiving application connected to the IQ stream.

## Troubleshooting

- **Meter stays at 0 even though the button shows "On"** — The stream may not have been accepted by the radio. Disconnect from the radio and reconnect. AetherSDR will attempt to re-enable the stream after a short delay once the session is ready.
- **Meter resets to 0 after reconnecting** — This is expected behavior. AetherSDR resets all meters on disconnect. Streams that were previously enabled are restored automatically on reconnect.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [DAX IQ overview](overview.md)

# Monitor the RMS level of each IQ stream

The DAX IQ applet includes a real-time level meter for each of the four IQ streams. Use these meters to confirm that a stream is active and receiving signal.

## Before you start

- AetherSDR must be connected to the radio. The DAX IQ applet requires an active radio connection.
- At least one IQ stream must be enabled. A disabled stream shows a meter value of 0.

## Steps

1. Click the **IQ** tray button on the right sidebar to open the DAX IQ applet.
2. Locate the row for the channel you want to monitor: **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. Confirm the toggle button for that channel shows **On**. If it shows **Off**, enable the stream first — see [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md).
4. Observe the level meter in the center of the row. The bar updates in real time as IQ data arrives from the radio.

## What each control does

| Control | What it shows | Range | Notes |
|---|---|---|---|
| IQ 1–4 meter | RMS level of the IQ stream, scaled for display | 0–100 (scaled from RMS × 200) | Resets to 0 when the stream is disabled or the radio disconnects |
| IQ 1–4 Off/On | Whether this IQ stream is currently active | Off / On | Stream must be **On** for the meter to advance above 0 |

## Tips

- A meter that stays at 0 on an **On** stream can indicate the radio has no active slice or the external software has not opened the stream yet.
- The meter resets to 0 on disconnect and on any stream that is toggled to **Off**.
- The meter value is a display-only indicator. It has no persisted setting key and no effect on radio configuration.

## Troubleshooting

- **Meter stays at 0 even though the stream is On** — The radio resets all IQ streams per session. If you just reconnected, AetherSDR waits approximately 1.5 seconds before re-enabling persisted streams. Wait for the toggle to settle to **On**, then check the meter again.
- **Stream toggles back to Off immediately after connecting** — The radio was not ready when the enable request was sent. AetherSDR retries automatically after the session setup settles. If the button remains **Off**, click it manually to request the stream again.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [DAX IQ overview](overview.md)

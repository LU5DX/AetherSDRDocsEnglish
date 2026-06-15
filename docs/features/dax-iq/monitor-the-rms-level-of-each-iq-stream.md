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
| IQ 1–4 meter | RMS level of the IQ stream, scaled for display | 0–100 (scaled from RMS × 200) | Resets to 0 when the stream is disabled, the radio disconnects, or the stream is not bound to a pan. The meter uses the current theme accent color for the progress bar chunk. |
| IQ 1–4 Off/On | Whether this IQ stream is currently active | Off / On | Stream must be **On** and bound to a pan for the meter to advance above 0 |
| IQ 1–4 rate | Selected sample rate for the IQ stream | 24k (24000), 48k (48000), 96k (96000), 192k (192000) | Changing the rate emits a signal to the radio. The combo box syncs back to the radio-reported rate when a stream is active, but does not overwrite the user selection during stream disable or rate-settling. |

## Tips

- An **On** stream may still show a meter at 0 if the radio has no active slice, the external software has not opened the stream yet, or the stream is not bound to a pan.
- The meter resets to 0 on disconnect and on any stream that is toggled to **Off**.
- The meter value is a display-only indicator. It has no persisted setting key and no effect on radio configuration.
- The rate combo box preserves the user-selected rate even when the stream is off. If you choose a non-default rate while the stream is off, that rate is applied when you next enable the stream.

## Troubleshooting

- **Meter stays at 0 even though the stream is On** — The radio resets all IQ streams per session. If you just reconnected, AetherSDR waits approximately 1.5 seconds before re-enabling persisted streams. Wait for the toggle to settle to **On**, then check the meter again.
- **Stream toggles back to Off immediately after connecting** — The radio was not ready when the enable request was sent. AetherSDR retries automatically after the session setup settles. If the button remains **Off**, click it manually to request the stream again.
- **Meter stays at 0 on a newly enabled stream with a non-default rate** — The rate setting is applied when the stream is enabled. The meter may read 0 momentarily while the rate settles. If it remains 0, verify the stream is bound to a pan (the meter drops to 0 when unbound).

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [DAX IQ overview](overview.md)
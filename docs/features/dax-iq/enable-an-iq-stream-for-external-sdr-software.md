# Enable an IQ stream for external SDR software

The DAX IQ applet lets you activate one or more of four IQ streams on the FLEX-8600, making raw IQ data available to external SDR software on your system. You must enable a stream before external applications can receive data from it.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. DAX IQ controls are unavailable without an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **IQ** tray button on the right sidebar to open the DAX IQ applet.
2. Locate the row for the channel you want — **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. If needed, set the sample rate using the rate combo box for that channel (default: **48k**). See [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md) for details.
4. Click the **Off** button on that channel's row. The button label changes to **On** and its style changes to indicate the stream is active.
5. Configure your external SDR software to receive the IQ stream on the corresponding DAX IQ channel number.

## What each control does

| Control | Description | Default | Valid values |
|---|---|---|---|
| Rate combo box (IQ 1–4) | Sets the sample rate for the IQ stream. The combo syncs back to the radio-reported rate when a stream is active. The selected rate is saved per channel. | 48k | 24k, 48k, 96k, 192k |
| Off/On toggle button (IQ 1–4) | Enables or disables the IQ stream for that channel. Displays **Off** when inactive, **On** when active. | Off | Off, On |
| Level meter (IQ 1–4) | Shows the RMS level of the active IQ stream on a 0–100 scale. Resets to 0 when the stream is disabled or the radio disconnects. | 0 | 0–100 |

## Tips

- IQ streams are per-session on the radio. AetherSDR saves which channels you had enabled and which sample rate you selected. On reconnect, AetherSDR waits briefly for the radio session to settle before re-enabling previously active streams — the buttons will briefly show **Off** after connecting before restoring.
- You can enable up to four IQ streams simultaneously, one per channel.
- If your external software is not receiving data, confirm the **On** button is lit for the correct channel and that the external application is configured for the matching channel number.

## Troubleshooting

- **Button returns to Off shortly after clicking On** — The radio rejected the stream request, likely because the session was not yet fully established. Wait a few seconds after connecting and try again.
- **Level meter stays at 0 despite the stream being On** — The external application may not be consuming the stream, or the radio is not sending audio on that slice. Verify your external software is connected to the correct DAX IQ channel.

## Related

- [DAX IQ overview](overview.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)

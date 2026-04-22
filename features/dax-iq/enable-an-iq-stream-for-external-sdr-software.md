# Enable an IQ stream for external SDR software

The DAX IQ applet lets you activate one or more of four IQ data streams from your FLEX-8600. External SDR software can then receive raw IQ samples from the radio over the local network.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. If not connected, open `Settings > Connect to Radio...` first.
- The applet panel must be visible. If it is not, open `View > Applet Panel`.

## Steps

1. Click the **IQ** tray button on the right sidebar to open the DAX IQ applet.
2. Locate the row for the channel you want — **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. Select a sample rate from the rate combo box in that row. The default is **48k**. See [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md) for guidance on choosing a rate.
4. Click the **Off** button at the right of that row. The button changes to **On** and highlights to confirm the stream is active.
5. Configure your external SDR software to receive the IQ stream on the corresponding DAX IQ channel number.

## What each control does

| Control | Default | Valid values | Behavior |
|---|---|---|---|
| Rate combo box (IQ 1–4) | 48k | 24k, 48k, 96k, 192k | Sets the sample rate sent to the radio for this channel. Syncs back to the radio-reported rate when a stream is active. |
| Level meter (IQ 1–4) | 0 | 0–100 | Shows the RMS level of the active IQ stream. Resets to 0 when the stream is disabled or the radio disconnects. |
| Off/On toggle button (IQ 1–4) | Off | Off, On | Enables or disables the IQ stream for that channel. |

## Tips

- IQ streams are per-session and are not persisted by the radio. After reconnecting, all buttons reset to **Off** and you must re-enable any streams you need.
- The level meter rising above 0 after clicking **On** confirms that IQ data is flowing. If it stays at 0, your external software may not have opened the stream yet.
- Scrolling the applet panel does not accidentally change the rate combo box; you must click the combo box to open it before the scroll wheel takes effect.

## Troubleshooting

- **Button shows On but the level meter stays at 0** — The radio has accepted the stream request but no client is consuming the data. Verify that your external SDR software is running and connected to the correct DAX IQ channel.
- **Rate combo box reverts to a different value after enabling** — The radio reported a different sample rate for that channel. The combo box syncs to the radio-reported rate when a stream becomes active; select the desired rate again before clicking **On**, or adjust it in your external software.
- **IQ tray button is not visible on the sidebar** — The applet panel may be hidden. Open `View > Applet Panel` to show it, then click the **IQ** tray button.

## Related

- [DAX IQ overview](overview.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)

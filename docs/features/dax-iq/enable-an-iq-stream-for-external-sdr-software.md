# Enable an IQ stream for external SDR software

The DAX IQ applet lets you activate one or more of four IQ streams on your FLEX-8600 so that external SDR software can receive raw IQ data from the radio. Each stream can be independently enabled with its own sample rate.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. IQ streams are not available without an active radio connection.
- The DAX IQ applet is hidden by default. You must open it before you can enable a stream.

## Steps

1. Click the **IQ** tray button on the right sidebar to show the DAX IQ applet.
2. In the row for the channel you want (IQ 1 through IQ 4), select a sample rate from the rate combo box. The default is **48k**. Available rates are **24k**, **48k**, **96k**, and **192k**.
3. Click the **Off** button in that channel's row. The button label changes to **On** and the button style changes to indicate the stream is active.
4. Configure your external SDR software to connect to the corresponding DAX IQ channel.

## What each control does

| Control | Default | Valid values | Persisted key |
|---|---|---|---|
| Rate combo box (IQ 1–4) | `48k` | `24k` (24000), `48k` (48000), `96k` (96000), `192k` (192000) | `DaxIqRate1` – `DaxIqRate4` |
| Off/On toggle (IQ 1–4) | `Off` | `Off`, `On` | `DaxIqEnabled1` – `DaxIqEnabled4` |
| Level meter (IQ 1–4) | 0 | 0–100 (scaled from RMS × 200) | — |

## Tips

- Your sample rate selection is persisted across sessions. When you reconnect to the radio, AetherSDR waits briefly for the session to settle before re-enabling any streams that were active in the previous session.
- The rate combo box syncs back to the radio-reported rate once a stream is active. If the radio overrides your selection, the combo will reflect the radio's value.
- The level meter resets to 0 whenever a stream is disabled or the radio disconnects.

## Troubleshooting

- **The IQ tray button is not visible** — The applet panel may be hidden. Go to `View > Applet Panel` to show it, then click the **IQ** tray button.
- **The button switches to On but no data arrives in external software** — The stream request may have been sent before the radio was ready. Disable the stream by clicking **On** to return it to **Off**, wait a moment, then click **Off** again to re-enable it.
- **The rate combo reverts after enabling** — The radio has reported a different sample rate for the active stream. The combo syncs to the radio-reported value; select your preferred rate before enabling the stream.

## Related

- [DAX IQ overview](overview.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)

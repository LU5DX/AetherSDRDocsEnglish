# Enable an IQ stream for external SDR software

The DAX IQ applet lets you activate up to four IQ streams from your FLEX-8600 and route them to external SDR software. Enable a channel here to start the stream on the radio; your external application then connects to that stream to receive IQ samples.

## Before you start

- AetherSDR must be connected to the radio. The DAX IQ applet requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## Steps

1. Click the **IQ** tray button on the right sidebar to open the DAX IQ applet.
2. Locate the row for the channel you want — **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
3. Select a sample rate from the rate combo box in that row. The default is **48k**. Available rates are 24k, 48k, 96k, and 192k.
4. Click the **Off** button at the right end of the row. The button changes to **On** and the stream becomes active on the radio.
5. Configure your external SDR software to connect to the corresponding DAX IQ channel. The level meter in that row will show signal activity once samples are flowing.

## What each control does

| Control | Description | Default | Valid values |
|---|---|---|---|
| Rate combo box (IQ 1–4) | Sets the IQ sample rate for the channel. The combo syncs to the radio-reported rate when a stream is active. | 48k | 24k (24000), 48k (48000), 96k (96000), 192k (192000) |
| Level meter (IQ 1–4) | Shows the RMS level of the active IQ stream, scaled 0–100. Resets to 0 on disconnect or disable. | 0 | 0–100 |
| Off / On toggle (IQ 1–4) | Enables or disables the IQ stream for that channel. | Off | Off, On |

## Tips

- IQ streams are per-session and are not persisted by the radio. However, AetherSDR saves the enabled state for each channel locally (keys `DaxIqEnabled1` through `DaxIqEnabled4`) and restores active streams automatically about 1.5 seconds after reconnecting to the radio.
- The rate combo box is also saved locally per channel (`DaxIqRate1` through `DaxIqRate4`), so your preferred sample rate is restored on next launch.
- If you scroll the applet panel without meaning to change values, AetherSDR's controls-lock mechanism prevents accidental rate changes while scrolling.

## Troubleshooting

- **Button shows "On" after reconnect but no samples arrive in the external application** — AetherSDR requests streams approximately 1.5 seconds after connecting to allow session setup to complete. Wait a moment, then check that your external software is connected to the correct DAX IQ channel number.
- **Rate combo shows a different value than selected** — When a stream is active, the combo syncs to the rate reported by the radio, which may override your selection. Disable the stream, change the rate, then re-enable it.

## Related

- [DAX IQ overview](overview.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)

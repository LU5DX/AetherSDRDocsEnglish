# DAX IQ overview

The DAX IQ applet lets you enable up to four independent IQ data streams from the FLEX-8600, set each stream's sample rate, and monitor its live signal level. Use these streams to feed external SDR software with raw IQ samples from the radio.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio. The DAX IQ applet requires an active radio connection.
- The applet panel must be visible. If it is not, click `View > Applet Panel` to show it.

## How it works

The DAX IQ applet provides four independent IQ channels, numbered IQ 1 through IQ 4. Each channel is controlled independently and all four share the same layout within the applet.

IQ streams are per-session only. The radio does not persist stream state across connections. Each time AetherSDR connects to the radio, all four channels start in the Off state.

When a stream is active, its rate combo syncs back to the sample rate reported by the radio. The level meter updates in real time based on the RMS level of the incoming IQ data.

**Opening the applet:** The DAX IQ applet is hidden by default. Click the IQ tray button on the right sidebar to show or hide it.

## What each control does

Each of the four IQ channels (IQ 1, IQ 2, IQ 3, IQ 4) has the following controls:

| Control | What it does | Default | Valid values |
|---|---|---|---|
| Rate combo | Sets the sample rate for the IQ stream. When a stream is active, this syncs to the rate reported by the radio. | 48k | 24k (24000 Hz), 48k (48000 Hz), 96k (96000 Hz), 192k (192000 Hz) |
| Level meter | Displays the RMS level of the IQ stream in real time, scaled 0–100. Resets to 0 when the stream is disabled or the radio disconnects. | 0 | 0–100 |
| Off / On toggle | Enables or disables the IQ stream for that channel. Button text shows the current state: "Off" when inactive, "On" when active. | Off | Off, On |

None of these controls persist to a settings key. Stream state and rate are held on the radio for the duration of the session only.

## Tips

- Set the sample rate before enabling a stream. Once the stream is active, the rate combo will reflect the radio-confirmed rate.
- Higher sample rates (96k, 192k) consume more network bandwidth. Use the lowest rate that meets your software's requirements.
- If you scroll the applet panel with the mouse wheel, the rate combos will not change value accidentally — the applet uses guarded controls that ignore scroll events unless the dropdown is open.

## Troubleshooting

- **All channels show Off after reconnecting to the radio** — IQ streams are per-session and are not persisted by the radio. Re-enable any channels you need after each connection.
- **Level meter stays at 0 with the stream On** — confirm that your external SDR software has opened the IQ stream. The meter only shows a level when data is actively being consumed.
- **Rate combo jumps back after you change it** — if a stream is already active, the radio may report its own rate back, causing the combo to sync. Disable the stream, change the rate, then re-enable it.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Pick the IQ sample rate (24k/48k/96k/192k)](pick-the-iq-sample-rate-24k-48k-96k-192k.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)

# Pick the IQ sample rate (24k/48k/96k/192k)

Select the sample rate for each DAX IQ channel to match the requirements of your external SDR software. Higher rates give more bandwidth; lower rates reduce CPU and network load.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The DAX IQ applet must be visible. If it is not, click the **IQ** tray button on the right sidebar to show it.

## Steps

1. Locate the row for the channel you want to configure: **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
2. Click the rate combo box in that row. It shows the current rate (default **48k**).
3. Select one of the four options: **24k**, **48k**, **96k**, or **192k**.

AetherSDR immediately sends the new rate to the radio and saves your choice. The setting persists across restarts as `DaxIqRate1` through `DaxIqRate4`.

If the stream is already active, the combo box will sync back to the rate reported by the radio whenever the radio confirms the stream state.

## What each control does

| Control | Default | Valid values | Persisted setting key |
|---|---|---|---|
| Rate combo box (per channel) | 48k | 24k (24000 Hz), 48k (48000 Hz), 96k (96000 Hz), 192k (192000 Hz) | `DaxIqRate1` … `DaxIqRate4` |
| On/Off toggle (per channel) | Off | Off, On | `DaxIqEnabled1` … `DaxIqEnabled4` |
| Level meter (per channel) | 0 | 0–100 (scaled from RMS × 200) | — |

## Tips

- You can change the rate whether the stream is off or on. If the stream is already enabled, the radio applies the new rate to the active stream.
- On reconnect, the combo box resets briefly before the radio reports the confirmed stream state. The displayed rate will sync automatically once the stream is re-established.
- Scroll wheel events on the combo box are suppressed when the applet panel scroll lock is active. If the combo box does not respond to the scroll wheel, scroll the panel to the desired position and then click the combo directly.

## Troubleshooting

- **Rate combo shows a value different from what you selected** — The radio has reported a different rate for the active stream, and the combo has synced to match. This is normal. Disable the stream, change the rate, then re-enable it.
- **Rate combo is unresponsive to the scroll wheel** — The applet panel scroll lock is active. Click the combo box to open the dropdown instead.

## Related

- [DAX IQ overview](overview.md)
- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)

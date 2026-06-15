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

If the stream is already active, the combo box syncs back to the rate reported by the radio when the stream exists and is not in a rate-settling state. This prevents the combo from briefly showing 48k while the radio applies a non-default rate you selected while the stream was off.

## What each control does

| Control | Default | Valid values | Persisted setting key |
|---|---|---|---|
| Rate combo box (per channel) | 48k | 24k (24000 Hz), 48k (48000 Hz), 96k (96000 Hz), 192k (192000 Hz) | `DaxIqRate1` … `DaxIqRate4` |
| On/Off toggle (per channel) | Off | Off, On | `DaxIqEnabled1` … `DaxIqEnabled4` |
| Level meter (per channel) | 0 | 0–100 (scaled from RMS × 200) | — |

## Behavior details

- **Rate selection while stream is off**: Select a rate while the stream is off, then enable it. The rate you chose is applied to the newly created stream, not the radio's 48k default.
- **Rate sync while stream is on**: The combo box updates to match the radio-reported rate only when the stream exists and is not in a rate-settling transient state. During the brief settling period after enabling a non-default rate, the combo keeps your selection.
- **Stream disable**: When you disable a stream, the combo box retains your last selected rate. The radio resets the stream's sample rate to 48k internally, but the combo does not sync to that reset value.
- **Meter behavior**: The level meter resets to 0 when the channel is off or when it is enabled but not bound to a pan (for example, if the pan's `daxiq_channel` was moved to another IQ channel). No IQ data flows in either case.
- **Restoring enabled channels on connect**: After connecting or reconnecting to the radio, AetherSDR waits 1.5 seconds for session setup to settle, then re-enables any channels that were enabled before disconnect. If two connection events occur within the settle window, the second is ignored to prevent double-enabling.

## Tips

- You can change the rate whether the stream is off or on. If the stream is already enabled, the radio applies the new rate to the active stream.
- On reconnect, the combo box resets briefly before the radio confirms the stream state. The displayed rate syncs automatically once the stream is re-established and the settling period ends.
- Scroll wheel events on the combo box are suppressed when the applet panel scroll lock is active. If the combo box does not respond to the scroll wheel, scroll the panel to the desired position and then click the combo directly.
- The level meter uses the current theme's accent color and background palette.

## Troubleshooting

- **Rate combo shows a value different from what you selected** — The radio has reported a different rate for the active stream after the settling period, and the combo has synced to match. This is normal. Disable the stream, change the rate, then re-enable it.
- **Rate combo is unresponsive to the scroll wheel** — The applet panel scroll lock is active. Click the combo box to open the dropdown instead.
- **Level meter colors look different than expected** — The meter follows the active theme. Change the theme in **Settings > Appearance > Theme** to adjust meter colors.
- **Channels do not re-enable after reconnect** — If the 1.5-second settle timer has elapsed before the applet finishes loading, channels may not restore automatically. Disconnect and reconnect to trigger restoration again.
- **Rate combo briefly shows 48k after enabling** — This is the rate-settling period. The combo will update to your selected rate once the radio confirms the new rate.

## Related

- [DAX IQ overview](overview.md)
- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
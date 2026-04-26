# Pick the IQ Sample Rate (24k/48k/96k/192k)

This page explains how to change the IQ sample rate for any of the four DAX IQ channels. Use a higher rate when your external SDR software requires more bandwidth; use a lower rate to reduce CPU and network load.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The DAX IQ applet must be visible. If it is not, click the IQ tray button on the right sidebar to show it.

## Steps

1. Locate the row for the channel you want to change: **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
2. Click the rate combo box in that row. It currently shows the active rate (default **48k**).
3. Select one of the four rates: **24k**, **48k**, **96k**, or **192k**.

The new rate takes effect immediately and is sent to the radio. If that channel's stream is active, the combo box will sync back to the rate reported by the radio to confirm the change was accepted.

## What each control does

| Control | Description | Default | Valid values | Persisted setting |
|---|---|---|---|---|
| Rate combo box (IQ 1–4) | Sets the IQ sample rate for that channel | 48k | 24k (24000), 48k (48000), 96k (96000), 192k (192000) | `DaxIqRate1` – `DaxIqRate4` |
| Off/On toggle (IQ 1–4) | Enables or disables the IQ stream for that channel | Off | Off, On | `DaxIqEnabled1` – `DaxIqEnabled4` |
| Level meter (IQ 1–4) | Shows the RMS level of the active stream (0–100 scale) | 0 | 0–100 | — |

## Tips

- The rate combo syncs back to the radio-reported rate when a stream is active. If the value you selected does not stick, the radio rejected the rate change; try disabling the stream first, changing the rate, then re-enabling.
- Rate settings are persisted. On reconnect, AetherSDR restores the last-used rate for each channel from `DaxIqRate1` through `DaxIqRate4`.
- Stream enable state is also persisted. If a channel was left **On** when you disconnected, AetherSDR will re-enable it automatically about 1.5 seconds after reconnection to allow the radio's session setup to complete first.

## Troubleshooting

- **Rate combo reverts to the previous value after selection** — The radio rejected the rate change while the stream was active. Click **On** to switch the channel to **Off**, set the desired rate, then click **Off** to switch it back to **On**.
- **Combo box shows a rate that differs from what you selected** — The radio reported a different rate for the active stream and the combo has synced to match. The radio's reported value is authoritative when a stream is running.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [DAX IQ overview](overview.md)

# Pick the IQ sample rate (24k/48k/96k/192k)

Change the sample rate of a DAX IQ channel to match the input requirements of your external SDR software. A higher rate captures more bandwidth; a lower rate reduces CPU and network load.

## Before you start

- AetherSDR must be connected to the radio. The DAX IQ applet requires an active radio connection.
- The DAX IQ applet must be visible. If it is hidden, click the **IQ** tray button on the right sidebar to show it.

## Steps

1. Locate the row for the channel you want to change: **IQ 1**, **IQ 2**, **IQ 3**, or **IQ 4**.
2. Click the rate combo box in that row. It shows the current rate (default: **48k**).
3. Select one of the available rates: **24k**, **48k**, **96k**, or **192k**.

The new rate takes effect immediately and is sent to the radio. If the stream is active, the combo box will reflect the rate reported back by the radio.

## What each control does

| Control | Default | Valid values | Notes |
|---|---|---|---|
| Rate combo box (IQ 1–4) | 48k | 24k (24000 Hz), 48k (48000 Hz), 96k (96000 Hz), 192k (192000 Hz) | Syncs back to the radio-reported rate when the stream is active. No persisted setting key. |
| Off/On toggle (IQ 1–4) | Off | Off, On | Must be **On** for the rate change to affect a live stream. |
| Level meter (IQ 1–4) | 0 | 0–100 | Shows RMS level of the stream. Resets to 0 when the stream is disabled or the radio disconnects. |

## Tips

- You can change the rate whether the stream is **On** or **Off**. If the stream is off, the selected rate will be used when you enable it.
- Scrolling the mouse wheel over a closed rate combo box does nothing — the dropdown must be open for wheel input to register. Click the combo box first to open it, then scroll.
- IQ stream settings are per-session and are not persisted by the radio. After reconnecting, streams return to **Off** and the rate combo returns to **48k**.

## Troubleshooting

- **The rate combo box snaps back to a different value after I change it.** — The radio reported a different rate for the active stream. This is normal; the combo syncs to the radio-confirmed rate. If the stream is **On**, disable it with the **Off/On** toggle, change the rate, then re-enable.
- **The rate combo box does not respond to clicks.** — The applet panel may be in scroll mode with controls locked. Try clicking directly on the combo box rather than scrolling over it.

## Related

- [Enable an IQ stream for external SDR software](enable-an-iq-stream-for-external-sdr-software.md)
- [Monitor the RMS level of each IQ stream](monitor-the-rms-level-of-each-iq-stream.md)
- [Disable an IQ stream to free bandwidth](disable-an-iq-stream-to-free-bandwidth.md)
- [DAX IQ overview](overview.md)

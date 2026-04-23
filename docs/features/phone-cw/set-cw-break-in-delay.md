# Set CW break-in delay

The Phone/CW applet lets you set how long the radio waits after the last CW element before returning to receive. Adjusting this delay prevents the radio from switching back to RX between characters at high speed, or lets it return quickly for quick-response QSOs.

## Before you start

- Connect to a Flex radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a CW mode. The applet automatically switches to the CW sub-panel when the slice is in CW; the Delay control is not visible in phone modes.

## Steps

1. Locate the **P/CW** tray button on the right sidebar and confirm the applet is visible. If the applet is hidden, click the **P/CW** tray button to show it.
2. Verify the applet is showing the CW sub-panel. If the active slice is in CW mode, the CW controls appear automatically.
3. Find the **Delay (CW)** slider.
4. Drag the **Delay (CW)** slider to the desired value. The delay applies immediately.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Delay (CW)** | Sets the break-in delay: how long the radio waits after the last keyed element before returning to receive. | — | 0–2000 ms, step 10 | — |
| **Breakin** | Toggles full break-in (QSK). When enabled, the radio switches to RX between every element. | — | On / Off | — |

## Tips

- Set **Delay (CW)** to 0 ms with **Breakin** active for full QSK operation.
- At higher speeds, increase the delay slightly to prevent RX/TX chatter between characters.

## Related

- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

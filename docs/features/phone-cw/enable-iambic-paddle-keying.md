# Enable iambic paddle keying

The iambic keyer lets you use a squeeze paddle to generate CW with the Flex radio's built-in keyer. This page explains how to turn it on and adjust the related CW controls.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW control panel when a CW mode is selected; the iambic controls are not visible in phone modes.

## Steps

1. Select a CW mode on the slice you want to key. The P/CW applet switches to the CW panel automatically.
2. If the P/CW applet is not visible, click the "P/CW" tray button on the right sidebar to open it.
3. Click "Iambic" to toggle the iambic paddle keyer on. The button lights when active.

## What each control does

| Control | Kind | Default | Valid range | Persisted key |
|---|---|---|---|---|
| Iambic | Toggle button | — | On / Off | — |
| Breakin | Toggle button | — | On / Off | — |
| Delay (CW) | Slider | — | 0–2000 ms (step 10) | — |
| Speed (CW) | Slider | — | 5–100 WPM | — |
| Sidetone | Toggle button | — | On / Off | — |
| Sidetone volume | Slider | — | 0–100 | — |
| Pitch < / > | Spinbox | 600 Hz | 100–6000 Hz (step 10) | — |
| L / R pan (CW) | Slider | 50 | 0–100 | — |

## Tips

- Enable "Breakin" alongside "Iambic" if you want full QSK operation — the radio will switch back to receive between each element.
- Adjust "Delay (CW)" to set how long the radio stays in transmit after the last keyed element before returning to receive. At 0 ms the radio drops to receive immediately.

## Related

- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

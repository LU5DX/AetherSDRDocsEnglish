# Set CW keying speed in WPM

Use the Speed slider in the Phone/CW applet to control how fast AetherSDR keys the FLEX-8600 when operating in CW mode. The speed is set in words per minute (WPM) and sent directly to the radio.

## Before you start

- AetherSDR must be connected to the radio. The CW controls are only available when connected.
- The active slice must be in a CW mode. The Phone/CW applet switches to the CW panel automatically when the slice mode is CW.

## Steps

1. Locate the `P/CW` tray button in the right sidebar and confirm the Phone/CW applet is visible. If it is not visible, click the `P/CW` tray button to show it.
2. Confirm that the CW sub-panel is displayed. If the active slice is in CW mode, the applet switches to the CW panel automatically. If you still see the Phone panel, set the slice mode to CW first.
3. Find the **Speed (CW)** slider.
4. Drag the **Speed (CW)** slider left to decrease WPM or right to increase WPM.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| Speed (CW) | Sets CW keying speed sent to the radio | — | 5–100 WPM | — |

## Tips

- The CW panel also contains the **Delay (CW)** slider (0–2000 ms, step 10) for break-in timing, and the **Breakin** toggle for full QSK. Adjusting speed does not affect those controls.
- The applet reverts to the Phone panel automatically when the active slice leaves CW mode, but your speed setting is retained by the radio.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

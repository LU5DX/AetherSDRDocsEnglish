# Set CW keying speed in WPM

Use the Speed slider in the Phone/CW applet to set how fast the radio keys CW, measured in words per minute. This setting is sent directly to the FLEX-8600 and takes effect immediately.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a CW mode. The applet automatically shows CW controls only when the slice is in CW mode; in voice modes it shows the Phone panel instead.

## Steps

1. Locate the **P/CW** tray button on the right sidebar and confirm the applet panel is visible. If the panel is hidden, click the **P/CW** tray button to show it.
2. Verify the CW sub-panel is displayed. If the Phone controls are showing instead, switch the active slice to a CW mode.
3. Find the **Speed (CW)** slider in the CW panel.
4. Drag the slider to the desired keying speed. The valid range is **5–100 WPM**.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| Speed (CW) | Sets CW keying speed sent to the radio. | — | 5–100 WPM | — |

## Tips

- The CW panel also contains the **Delay (CW)** slider (0–2000 ms, step 10) for break-in timing, and the **Pitch < / >** spinbox (100–6000 Hz, step 10) for sidetone pitch. Adjust these together with speed to match your operating preference.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

# Set CW keying speed in WPM

Use the Speed slider in the Phone/CW applet to set how fast the radio keys CW, measured in words per minute. This controls the radio's internal keyer and affects paddle, straight-key, and CWX transmissions.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a CW mode. The Phone/CW applet shows the CW sub-panel only when the active slice is in CW mode; otherwise the Phone panel is displayed.
- Open the Phone/CW applet by clicking the P/CW tray button in the right sidebar, or confirm it is already visible.

## Steps

1. Verify that the active slice is in a CW mode. The applet automatically switches to the CW sub-panel when CW mode is active.
2. Locate the **Speed (CW)** slider in the CW sub-panel.
3. Drag the **Speed (CW)** slider left to decrease WPM or right to increase WPM. The valid range is 5–100 WPM.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| Speed (CW) | Sets CW keying speed sent to the radio's internal keyer. | — | 5–100 WPM | — |

## Tips

- The Speed (CW) slider operates the radio's keyer speed. Changes take effect immediately and apply to the paddle, straight key, and any CWX text transmissions.
- The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone in lockstep. Adjusting speed does not affect sidetone pitch; pitch always follows the radio's `cw_pitch` setting automatically.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
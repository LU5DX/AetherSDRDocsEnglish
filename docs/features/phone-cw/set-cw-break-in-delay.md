# Set CW break-in delay

The CW break-in delay controls how long the radio waits after the last keypress before returning to receive. Adjusting this prevents choppy QSK switching while still allowing a fast return to RX between words or characters.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet shows controls only when a radio connection is active.
- The active slice must be in a CW mode. The CW sub-panel replaces the Phone sub-panel automatically when CW is selected on the active slice.

## Steps

1. Locate the **P/CW** tray button in the right sidebar and confirm the applet is visible. If the applet is not visible, click the **P/CW** tray button to show it.
2. Confirm the CW sub-panel is displayed. If the Phone controls are showing instead, switch the active slice to a CW mode using the mode selector in the main VFO area.
3. Locate the **Delay (CW)** slider in the CW sub-panel.
4. Drag the **Delay (CW)** slider left to decrease the delay or right to increase it. The value is applied to the radio immediately.

## What each control does

| Control | Description | Valid range | Default | Setting key |
|---|---|---|---|---|
| Delay (CW) | Sets the CW break-in delay. The radio returns to receive this many milliseconds after the last keyed element. | 0–2000 ms (step 10) | — | — |
| Breakin | Toggles full break-in (QSK). When enabled, the radio switches to receive between every element. The **Delay (CW)** slider still takes effect when **Breakin** is off. | On / Off | — | — |

## Tips

- A delay of 0 ms with **Breakin** enabled gives full QSK operation. Increase the delay to reduce relay wear during fast sending.
- The **Delay (CW)** slider steps in 10 ms increments. For fine adjustment, click the slider track and use the arrow keys (if keyboard shortcuts are enabled under `View > Keyboard Shortcuts`).

## Related

- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

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

| Control    | Description                                                                                                                                                           | Valid range         |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| Delay (CW) | Sets the CW break-in delay. The radio returns to receive this many milliseconds after the last keyed element.                                                         | 0–2000 ms (step 10) |
| Breakin    | Toggles full break-in (QSK). When enabled, the radio switches to receive between every element. The **Delay (CW)** slider still takes effect when **Breakin** is off. | On / Off            |

## Tips

- A delay of 0 ms with **Breakin** enabled gives full QSK operation. Increase the delay to reduce relay wear during fast sending.
- The **Delay (CW)** slider steps in 10 ms increments. For fine adjustment, click the slider track and use the arrow keys (if keyboard shortcuts are enabled under `View > Keyboard Shortcuts`).

## Notes for v0.9.3

- **Level gauge (Phone panel):** When the mic source is set to **PC**, the Level gauge now appears immediately on connect without waiting for the radio's `met_in_rx` flag to be set. This is because PC mic metering runs client-side and is independent of `met_in_rx`. For all other mic sources the previous suppression behavior is unchanged: the gauge reads −150 dBFS when `met_in_rx` is off and the radio is not transmitting.
- **VOX / Phone panel refresh:** VOX setters now emit `phoneStateChanged`, so the Phone sub-panel updates instantly when VOX is toggled via a keyboard shortcut. No manual panel interaction is needed to see the current VOX state.
- **Sidetone on Windows:** The CW sidetone stream (low-latency `CwSidetoneGenerator`) now starts immediately on connect on Windows. If you previously had to toggle **Sidetone** off and on after connecting to hear the local sidetone, this workaround is no longer needed.

## Related

- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
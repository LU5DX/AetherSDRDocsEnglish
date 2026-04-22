# Change CW pitch / sidetone frequency

The CW pitch setting controls the tone frequency used for both the sidetone monitor and the CW decode offset. Adjusting it lets you match your preferred listening pitch and align the panadapter filter marker with your operating frequency.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW panel when CW mode is active.

## Steps

1. Locate the Phone/CW applet in the Applet Panel (right sidebar). If it is not visible, click the **P/CW** tray button to show it.
2. Confirm the CW sub-panel is displayed. It appears automatically when the active slice is in CW mode.
3. Find the **Pitch** spinbox near the bottom of the CW panel. The current pitch value is shown in Hz between two arrow buttons.
4. Click **<** to decrease the pitch by 10 Hz, or click **>** to increase it by 10 Hz.
5. Repeat until the displayed value matches your desired pitch.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Pitch < / >** | Steps the CW sidetone and decode pitch frequency. Each click changes the value by 10 Hz. | 600 Hz | 100–6000 Hz (step 10) | — |
| **Sidetone** | Toggles the CW sidetone monitor on or off. Pitch has no audible effect unless Sidetone is enabled. | — | On / Off | — |
| **Sidetone volume** | Sets the CW monitor volume level. | — | 0–100 | — |

## Tips

- The pitch value affects both the audible sidetone tone and the frequency offset used for CW decoding. Set it to match your preferred listening pitch before operating.
- Pitch changes in 10 Hz increments only. To reach a value such as 750 Hz from 600 Hz, click **>** fifteen times.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)

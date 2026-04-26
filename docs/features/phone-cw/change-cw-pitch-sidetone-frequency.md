# Change CW pitch / sidetone frequency

The CW pitch setting controls the tone frequency used for both the sidetone you hear while keying and the CW decode offset. Adjust it to match your preferred listening pitch or to place decoded CW correctly in the passband.

## Before you start

- AetherSDR must be connected to the radio.
- The active slice must be in a CW mode. The Phone/CW applet automatically switches to the CW panel when a CW mode is selected; the pitch control is not visible in Phone mode.

## Steps

1. Locate the P/CW tray button on the right sidebar and confirm the CW panel is showing. If the applet is hidden, click the P/CW tray button to show it.
2. Find the **Pitch < / >** spinbox at the bottom of the CW panel.
3. Click **<** to decrease the pitch by 10 Hz, or click **>** to increase it by 10 Hz.
4. Repeat until the displayed value matches your target frequency.

## What each control does

| Control | Description | Default | Valid range | Setting key |
|---|---|---|---|---|
| **Pitch < / >** | Steps the CW sidetone and decode pitch up or down. Each click moves the value by 10 Hz. | 600 Hz | 100–6000 Hz (step 10) | — |

## Tips

- The pitch value affects both what you hear in the sidetone and the frequency offset used for CW decoding. If decoded text appears shifted, verify the pitch matches your filter center.
- The pitch setting is sent directly to the radio; there is no separate client-side persistence for it.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)

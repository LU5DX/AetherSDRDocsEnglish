# Configure break-in OFF so CW keys queue and PTT is manual

When Breakin is OFF, CW keyboard and MIDI key events are queued and sent to the radio without triggering TX automatically. You engage PTT manually to begin transmitting. Use this when you want full control over when the transmitter keys — for example, during contest operating or when running a linear amplifier that needs deliberate PTT sequencing.

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a CW mode so the applet switches to the CW panel. The Breakin control is only visible in the CW sub-panel.

## Steps

1. Open the Phone/CW applet. Click the **P/CW** tray button in the right sidebar, or confirm it is already visible in the Applet Panel.
2. Verify the CW sub-panel is showing. If the Phone panel is displayed instead, change the active slice mode to CW on the radio.
3. Locate the **Breakin** toggle button in the CW sub-panel.
4. If **Breakin** is lit (active), click it to turn it off. The button will appear unlit when break-in is disabled.
5. Key CW using your keyboard or MIDI controller. Characters are queued and sent to the radio, but the radio does not assert TX automatically.
6. Press PTT manually to key the transmitter before or while the keyer sends the queued characters.

## What each control does

| Control                | Behavior                                                                                                                                                                                                                                                                    | Default |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **Breakin**            | Toggles full break-in (QSK). When ON, key edges trigger TX and the break-in delay holds the relay open between characters. When OFF, keyed characters are queued and PTT must be engaged manually.                                                                          | —       |
| **Delay (CW)**         | Sets the CW break-in hang time — how long the relay stays keyed after the last element. Relevant when Breakin is ON. The slider adjusts from 0 to 2000 ms in 10 ms steps. In v0.9.8, you can click the adjacent QLineEdit and type a value directly (0–2000).             | 500 ms  |
| **Speed (CW)**         | Sets CW keying speed in words per minute. The slider adjusts from 5 to 100 WPM. In v0.9.8, you can click the adjacent QLineEdit and type a value directly (5–100).                                                                                                          | 20 WPM  |
| **Sidetone**           | Toggles CW sidetone monitor. Controls both the radio's DAX-fed monitor and the client-side low-latency CwSidetoneGenerator in lockstep. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically.                                          | —       |
| **Sidetone volume**    | Sets CW monitor volume. Controls both the radio-side (`mon_gain_cw`) and client-side sidetone volumes in lockstep. The slider adjusts from 0 to 100. In v0.9.8, you can click the adjacent QLineEdit and type a value directly (0–100).                                      | 50      |
| **L / R pan (CW)**     | Sets CW monitor stereo pan. Calls `TransmitModel::setMonPanCw` and applies constant-power pan to the local sidetone generator. Double-click recenters to 50 (centre).                                                                                                        | 50      |
| **Iambic**             | Toggles iambic paddle keyer.                                                                                                                                                                                                                                                | —       |
| **Pitch < / >**        | Sets CW sidetone pitch. Click the **<** or **>** buttons to step by 10 Hz, or click the QLineEdit and type a value directly (100–6000 Hz). Calls `TransmitModel::setCwPitch`. In v0.9.8, the QLineEdit accepts typed direct entry.                                            | 600 Hz  |

## Tips

- With Breakin OFF, no auto-PTT envelope is applied. The radio will not transmit queued characters until you assert PTT. Drop PTT after the last character clears to return to RX.
- If you are running an external amplifier, Breakin OFF gives you time to close the amplifier's T/R relay before the keyer begins sending.
- To adjust how long the relay stays engaged between characters when you later switch Breakin back ON, use the **Delay (CW)** slider (0–2000 ms) or type a value in the adjacent QLineEdit.

## Troubleshooting

- **Radio transmits immediately when a key is pressed even though Breakin appears off** — This was a known issue in versions before v0.9.7, where an auto-PTT envelope overrode the Breakin setting. Confirm AetherSDR is at v0.9.7 or later.
- **CW panel is not visible; Phone controls are shown instead** — The applet switches to the CW panel automatically only when the active slice is in a CW mode. Change the slice mode to CW on the radio.
- **The Delay slider snaps back after typing a value** — This was fixed in v0.9.8 (#2428). The value is now cached immediately so the radio emission does not snap the slider back.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Use keyboard or MIDI to trigger straight key or iambic paddles](use-keyboard-or-midi-to-trigger-straight-key-or-iambic-paddles.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [View Phone/CW applet controls](view-phone-cw-applet-controls.md)
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

| Control | Behavior | Default | Range | Setting key |
|---|---|---|---|---|
| **Breakin** | Toggles full break-in (QSK). When ON, key edges trigger TX and the break-in delay holds the relay open between characters. When OFF, keyed characters are queued and PTT must be engaged manually. | — | On / Off | — |
| **Delay (CW)** | Sets the CW break-in hang time — how long the relay stays keyed after the last element. Relevant when Breakin is ON. | — | 0–2000 ms (step 10) | — |

## Tips

- With Breakin OFF, no auto-PTT envelope is applied. The radio will not transmit queued characters until you assert PTT. Drop PTT after the last character clears to return to RX.
- If you are running an external amplifier, Breakin OFF gives you time to close the amplifier's T/R relay before the keyer begins sending.
- To adjust how long the relay stays engaged between characters when you later switch Breakin back ON, use the **Delay (CW)** slider (0–2000 ms).

## Troubleshooting

- **Radio transmits immediately when a key is pressed even though Breakin appears off** — This was a known issue in versions before v0.9.7, where an auto-PTT envelope overrode the Breakin setting. Confirm AetherSDR is at v0.9.7 or later.
- **CW panel is not visible; Phone controls are shown instead** — The applet switches to the CW panel automatically only when the active slice is in a CW mode. Change the slice mode to CW on the radio.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Use keyboard or MIDI to trigger straight key or iambic paddles](use-keyboard-or-midi-to-trigger-straight-key-or-iambic-paddles.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)

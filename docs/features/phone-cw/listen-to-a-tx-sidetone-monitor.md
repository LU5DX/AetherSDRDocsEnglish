# Listen to a TX sidetone monitor

AetherSDR provides a radio-side monitor (available in both Phone and CW modes) and a client-side low-latency CW sidetone (approximately 10 ms latency) that is controlled in lockstep with the radio sidetone via the single Sidetone button and Sidetone volume slider. This page covers both paths so you can hear your own transmitted audio while operating.

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Open the Applet Panel. If it is not visible, click View > Applet Panel.

## Steps

### Phone mode: enable the sideband monitor

1. Click the P/CW tray button on the right sidebar to open the Phone/CW applet.
2. Confirm the applet is showing the Phone panel (the active slice must be in a voice mode such as SSB or AM).
3. Click MON to enable the TX sideband monitor. The button highlights when active.
4. Adjust the Monitor volume slider to set the playback level (0–100).

### CW mode: enable the sidetone monitor

1. Switch the active slice to a CW mode. The applet automatically shows the CW panel.
2. Click Sidetone to enable the CW monitor. The button highlights when active.
   - This single button controls both the radio's DAX-fed monitor and the client-side low-latency sidetone generator in lockstep.
3. Adjust the Sidetone volume slider to set the level (0–100).
   - This single slider sets the volume for both the radio-side monitor (`mon_gain_cw`) and the local sidetone generator simultaneously.
4. Pitch and stereo pan are set automatically from the radio's `cw_pitch` and `mon_pan_cw` settings. To adjust pan manually, use the L / R pan (CW) slider (double-click to recentre).

## What each control does

| Control         | What it does                                                                                                                                                                                                                                                                                                                                                                                                          | Default |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| MON             | Enables the TX sideband monitor (Phone panel).                                                                                                                                                                                                                                                                                                                                                                        | —       |
| Monitor volume  | Sets sideband monitor playback level.                                                                                                                                                                                                                                                                                                                                                                                 | —       |
| Sidetone        | Toggles CW sidetone monitor. Also enables/disables the client-side low-latency CwSidetoneGenerator in lockstep. Both the radio's DAX-fed monitor and the local PortAudio sidetone are controlled by this single button. Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` automatically. v0.9.3: sidetone stream now starts immediately on connect on Windows (#2105 — AudioEngine init order fix). | —       |
| Sidetone volume | Sets the CW monitor playback level for both the radio-side monitor and the local sidetone generator simultaneously.                                                                                                                                                                                                                                                                                                   | —       |
| L / R pan (CW)  | Sets CW monitor stereo pan; applies to both the radio monitor and the local sidetone generator. Double-click to recentre.                                                                                                                                                                                                                                                                                             | 50      |

## Tips

- The Sidetone button and Sidetone volume slider control both audio paths (radio DAX monitor and client-side generator) together. There is no separate control to enable or adjust the local sidetone independently.
- Pitch always follows the radio's CW pitch setting automatically. Use the Pitch < / > spinbox to change the radio's CW pitch, and both the decode pitch and sidetone pitch will update accordingly.
- The MON button and the Sidetone button are separate controls on separate panels. MON applies to voice modes; Sidetone applies to CW mode.
- When the mic source is set to PC, the Level gauge appears immediately on connect. In v0.9.7, the same applies when RADE mode is active: the Level gauge is shown during RX regardless of the `met_in_rx` setting. In other mic source modes (without RADE active), the gauge is suppressed when `met_in_rx` is off and the radio is not transmitting.
- When RADE mode is active, the Mic gain slider acts as a client-side RADE gain control and its value is stored in `PcMicGain`. The slider does not send a mic level command to the radio in this state, which prevents overwriting your hardware mic setting.

## Troubleshooting

- **MON or Sidetone button has no effect** — Confirm the radio is connected and the active slice mode matches the panel being shown (Phone vs. CW). The applet switches panels automatically based on the active slice mode.
- **Sidetone produces no audio** — Check that your system audio output is configured correctly. The client-side sidetone is generated locally by AetherSDR; confirm the Sidetone button is active. On Windows, the sidetone stream now starts immediately on connect (v0.9.3, #2105).
- **Sidetone pitch is wrong** — Pitch is derived automatically from the radio's `cw_pitch` setting. Adjust the pitch using the Pitch < / > spinbox on the CW panel.
- **Level gauge does not appear on connect** — If the mic source is set to PC, or if RADE mode is active, the Level gauge appears immediately on connect and remains visible during RX. For other mic sources without RADE active, the gauge is suppressed until `met_in_rx` is enabled or the radio begins transmitting.
- **Mic gain slider appears to have no effect with RADE active** — When RADE mode is active, the Mic gain slider controls client-side RADE gain only and does not send commands to the radio. This is expected behavior. The value is saved as `PcMicGain`.

## Related

- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
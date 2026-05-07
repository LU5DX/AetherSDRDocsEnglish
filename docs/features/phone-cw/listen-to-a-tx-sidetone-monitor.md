# Phone/CW Applet

The Phone/CW applet is a mode-aware transmit panel that shows Phone controls (microphone, processor, monitor) in voice modes and automatically switches to CW controls (delay, speed, sidetone, iambic, pitch) when the active slice is in CW mode.

In v0.9.8, the four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator — click any value and type a number directly (SmartSDR parity).

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Open the Applet Panel. If it is not visible, click View > Applet Panel.

## Steps

### Phone mode: enable the sideband monitor

1. Click the P/CW tray button on the right sidebar to open the Phone/CW applet.
2. Confirm the applet is showing the Phone panel (the active slice must be in a voice mode such as SSB or AM).
3. Click MON to enable the TX sideband monitor. The button highlights when active.
4. Adjust the Monitor volume slider to set the playback level (0–100).

### Phone mode: adjust microphone settings

1. Select a Mic profile from the dropdown to load a named microphone processing profile.
2. Select the Mic source from the dropdown (options include MIC, BAL, LINE, ACC, PC, plus any from the radio's available mic inputs).
3. Adjust the Mic gain slider to set the microphone input level (0–100). When the source is PC, the value is stored locally in `PcMicGain`.
4. Click +ACC to enable the accessory microphone input mix.
5. Click PROC to toggle the speech processor.
6. Use the NOR/DX/DX+ slider to select the processor level: 0 (NOR), 1 (DX), or 2 (DX+).
7. Click DAX to enable DAX as the TX audio source.

### CW mode: adjust CW settings

1. Switch the active slice to a CW mode. The applet automatically shows the CW panel.
2. Adjust the Delay slider to set the CW break-in delay (0–2000 ms, step 10). You can also type a value directly into the QLineEdit (0–2000).
3. Adjust the Speed slider to set CW keying speed (5–100 WPM). You can also type a value directly into the QLineEdit (5–100).
4. Click Sidetone to enable the CW monitor. The button highlights when active.
5. Adjust the Sidetone volume slider to set the level (0–100). You can also type a value directly into the QLineEdit (0–100).
6. Use the L / R pan (CW) slider to set stereo pan (double-click to recentre to 50).
7. Click Breakin to toggle full break-in (QSK).
8. Click Iambic to toggle iambic paddle keyer.
9. Use the Pitch < / > buttons to step by 10 Hz, or type a value directly into the QLineEdit (100–6000 Hz).

## What each control does

| Control | What it does | Default | Valid Range |
|---------|--------------|---------|-------------|
| MON | Enables the TX sideband monitor (Phone panel). | — | — |
| Monitor volume | Sets sideband monitor playback level. | — | 0–100 |
| DAX | Enables DAX as the TX audio source. | — | — |
| Mic profile | Loads a named microphone processing profile. | — | Populated from radio |
| Mic source | Selects the microphone input source. | — | MIC, BAL, LINE, ACC, PC, plus radio inputs |
| Mic gain | Adjusts microphone input level. For PC source uses local PcMicGain persistence. | 50 | 0–100 |
| +ACC | Enables the accessory microphone input mix. | — | — |
| PROC | Toggles the speech processor. | — | — |
| NOR/DX/DX+ | Three-position processor level slider. | 0 | 0 (NOR), 1 (DX), 2 (DX+) |
| Delay (CW) | Sets CW break-in delay. Adjacent QLineEdit accepts typed values (0–2000) (v0.9.8, #2429). In v0.9.8, setCwDelay was fixed to cache the value immediately so the radio emission doesn't snap the slider back (#2428). | 500 ms | 0–2000 ms (step 10) |
| Speed (CW) | Sets CW keying speed. Adjacent QLineEdit accepts typed values (5–100) (v0.9.8, #2429). | 20 WPM | 5–100 WPM |
| Sidetone | Toggles CW sidetone monitor. Also enables/disables the client-side low-latency CwSidetoneGenerator in lockstep (v0.9.1+). Both the radio's DAX-fed monitor and the local PortAudio sidetone are controlled by this single button. Pitch and pan always follow the radio's cw_pitch and mon_pan_cw automatically. | — | — |
| Sidetone volume | Sets CW monitor volume. Also sets the local sidetone generator volume in lockstep. Adjacent QLineEdit accepts typed values (0–100) (v0.9.8, #2429). | 50 | 0–100 |
| L / R pan (CW) | Sets CW monitor stereo pan. Applies constant-power pan to the local sidetone generator (v0.9.1+). Double-click to recentre to 50. | 50 | 0–100 |
| Breakin | Toggles full break-in (QSK). In v0.9.7, the CW keyboard/MIDI paths now fully honor this setting: with Breakin ON (QSK) key edges trigger TX and break_in_delay holds the relay; with Breakin OFF keys are queued and the operator engages PTT manually. | — | — |
| Iambic | Toggles iambic paddle keyer. | — | — |
| Pitch < / > | QLineEdit with < / > buttons (CwTriBtn). Type a value (100–6000) or click the buttons to step by 10 Hz (v0.9.8, #2429). | 600 Hz | 100–6000 Hz (step 10) |

## Meter information

| Meter | What it shows | Valid Range | Notes |
|-------|--------------|-------------|-------|
| Level gauge | Microphone input peak level in dBFS. | -40 to +10 dBFS (red > 0) | Suppressed to -150 when met_in_rx is off and not transmitting. |
| Compression gauge | Speech compression amount in dB (reversed fill). | -25 to 0 dB | In v0.9.7, gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX. Driven via updateCompression() slot, independent of the mic level path. |
| ALC gauge | Automatic level control (CW sub-panel). | 0–100 (red > 80) | — |

## Tips

- The Sidetone button and Sidetone volume slider control both audio paths (radio DAX monitor and client-side generator) together. There is no separate control to enable or adjust the local sidetone independently.
- Pitch always follows the radio's CW pitch setting automatically. Use the Pitch < / > widget to change the radio's CW pitch, and both the decode pitch and sidetone pitch will update accordingly.
- The MON button and the Sidetone button are separate controls on separate panels. MON applies to voice modes; Sidetone applies to CW mode.
- When the mic source is set to PC, the Level gauge appears immediately on connect. In v0.9.7, the same applies when RADE mode is active: the Level gauge is shown during RX regardless of the `met_in_rx` setting. In other mic source modes (without RADE active), the gauge is suppressed when `met_in_rx` is off and the radio is not transmitting.
- When RADE mode is active, the Mic gain slider acts as a client-side RADE gain control and its value is stored in `PcMicGain`. The slider does not send a mic level command to the radio in this state, which prevents overwriting your hardware mic setting.
- In v0.9.8, the four CW QLineEdit fields (Delay, Speed, Sidetone Volume, Pitch) accept direct numeric input. Type a value and press Enter to apply it. Values are automatically clamped to the valid range.
- The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).

## Troubleshooting

- **MON or Sidetone button has no effect** — Confirm the radio is connected and the active slice mode matches the panel being shown (Phone vs. CW). The applet switches panels automatically based on the active slice mode.
- **Sidetone produces no audio** — Check that your system audio output is configured correctly. The client-side sidetone is generated locally by AetherSDR; confirm the Sidetone button is active. On Windows, the sidetone stream now starts immediately on connect (v0.9.3, #2105).
- **Sidetone pitch is wrong** — Pitch is derived automatically from the radio's `cw_pitch` setting. Adjust the pitch using the Pitch < / > widget on the CW panel.
- **Level gauge does not appear on connect** — If the mic source is set to PC, or if RADE mode is active, the Level gauge appears immediately on connect and remains visible during RX. For other mic sources without RADE active, the gauge is suppressed until `met_in_rx` is enabled or the radio begins transmitting.
- **Mic gain slider appears to have no effect with RADE active** — When RADE mode is active, the Mic gain slider controls client-side RADE gain only and does not send commands to the radio. This is expected behavior. The value is saved as `PcMicGain`.
- **Slider snaps back when adjusting CW delay** — This issue was fixed in v0.9.8 (#2428). The delay value is now cached immediately when set, preventing the radio emission from snapping the slider back.

## Related

- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
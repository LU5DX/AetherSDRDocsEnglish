# Phone/CW Applet

The Phone/CW applet is a mode-aware transmit panel that shows microphone/processor/monitor controls in voice modes and automatically switches to CW controls (delay, speed, sidetone, iambic, pitch) when the active slice is in CW mode. An ALC gauge appears on both the Phone and CW sub-panels, both driven by the software ALC meter (MeterModel::swAlcChanged, post-SSBMeter-peak dBFS), replacing the previous HWALC (RCA voltage) path that produced meaningless readings. The four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator — click any value and type a number directly. The single Sidetone toggle and volume slider drive both the radio's DAX-fed monitor and the client-side low-latency sidetone in lockstep — pitch and pan always follow the radio's cw_pitch and mon_pan_cw settings automatically. The CW sidetone routes to the user-selected audio output instead of the default output. The Compression gauge is gated on the radio's interlock TRANSMITTING state (not meter flow), so it reads 0 during RX; Breakin fully honors the radio's break_in setting — no auto-PTT envelope forces TX any more; the sidetone bus is shared with Quindar tones (mutually exclusive at the mode level). The embedded CWX panel's F1-F12 shortcuts are driven by the active slice's mode via MainWindow instead of panel visibility — they fire when the slice is in CW/CWL mode regardless of whether the panel is visible, while staying mutually exclusive with DVK panel F-key bindings. CWX macros also release TX automatically when the queue drains.

## Before you start

- The applet requires a connected FLEX-8600 radio running firmware 4.2
- The active slice must be in a voice mode (for Phone panel) or CW mode (for CW panel)

## Opening the applet

1. Click the **P/CW** tray button on the right sidebar to open the Phone/CW applet.
2. The applet automatically switches between Phone and CW panels based on the active slice mode.

## Phone controls

When the active slice is in a voice mode, the applet shows the Phone panel with the following controls:

| Control | Type | Range | Behavior |
|---------|------|-------|----------|
| Level | Meter | -40 to +10 dBFS (red > 0) | Shows microphone input peak level in dBFS. Suppressed to -150 when met_in_rx is off and not transmitting. |
| Compression | Meter | -25 to 0 dB (reversed fill) | Shows speech compression amount in dB. Gated on radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX to prevent confusing stale readings from the TX chain. Driven via updateCompression() slot, independent of the mic level path. |
| Mic profile | Combo box | Populated from radio micProfileList() | Loads the named mic processing profile; calls TransmitModel::loadMicProfile. |
| Mic source | Combo box | MIC, BAL, LINE, ACC, PC (plus any from micInputList()) | Selects microphone input source; calls TransmitModel::setMicSelection. |
| Mic gain | Slider | 0–100 | Adjusts mic input level. For "PC" source uses local PcMicGain persistence. Radio always reports mic_level=0 when source=PC; value kept client-side. |
| +ACC | Toggle | On/Off | Enables the accessory mic input mix; calls TransmitModel::setMicAcc. |
| PROC | Toggle | On/Off | Toggles the speech processor; calls TransmitModel::setSpeechProcessorEnable. |
| NOR/DX/DX+ | Slider | 0 (NOR), 1 (DX), 2 (DX+) | Three-position processor level; calls TransmitModel::setSpeechProcessorLevel. |
| DAX | Toggle | On/Off | Enables DAX as the TX audio source; calls TransmitModel::setDax. |
| MON | Toggle | On/Off | Enables TX sidetone monitor; calls TransmitModel::setSbMonitor. |
| Monitor volume | Slider | 0–100 | Sets sideband monitor volume; calls TransmitModel::setMonGainSb. |
| ALC (Phone panel) | Meter | -20 to 0 dBFS (red > -3) | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Rewired from HWALC (RCA voltage) to SW ALC meter. Mirrored by an identical gauge on the CW sub-panel. |

## CW controls

When the active slice is in CW mode, the applet shows the CW panel with the following controls:

| Control | Type | Range | Behavior |
|---------|------|-------|----------|
| Delay | Slider | 0–2000 ms (step 10) | Sets CW break-in delay; calls TransmitModel::setCwDelay. Adjacent QLineEdit accepts typed values (0–2000). |
| Speed | Slider | 5–100 WPM | Sets CW keying speed; calls TransmitModel::setCwSpeed. Adjacent QLineEdit accepts typed values (5–100). |
| Sidetone | Toggle | On/Off | Toggles CW sidetone monitor; calls TransmitModel::setCwSidetone. Controls both radio's DAX-fed monitor and client-side low-latency CwSidetoneGenerator in lockstep. Routes to the user-selected audio output instead of the default output. Pitch and pan always follow the radio's cw_pitch and mon_pan_cw automatically. |
| Sidetone volume | Slider | 0–100 | Sets CW monitor volume; calls TransmitModel::setMonGainCw. Also sets the local sidetone generator volume in lockstep. Adjacent QLineEdit accepts typed values (0–100). |
| L / R pan | Slider | 0–100 | Sets CW monitor stereo pan; calls TransmitModel::setMonPanCw and also applies constant-power pan to the local sidetone generator. Double-click recenters to 50 (centre). |
| Breakin | Toggle | On/Off | Toggles full break-in (QSK); calls TransmitModel::setCwBreakIn. Fully honors the radio's break_in setting: with Breakin ON (QSK) key edges trigger TX and break_in_delay holds the relay; with Breakin OFF keys are queued and the operator engages PTT manually. |
| Iambic | Toggle | On/Off | Toggles iambic paddle keyer; calls TransmitModel::setCwIambic. |
| Pitch < / > | Text field | 100–6000 Hz (step 10) | QLineEdit with < / > buttons (CwTriBtn). Type a value or click buttons to step by 10 Hz. Calls TransmitModel::setCwPitch. |
| ALC (CW panel) | Meter | -20 to 0 dBFS (red > -3) | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Uses HGauge::setFillFromRight mode. |

## Common controls

| Control | Type | Range | Behavior |
|---------|------|-------|----------|
| ALC gauge | Meter | -20 to 0 dBFS (fill from right) | Shows automatic level control. Both Phone and CW panels display identical ALC readings. Both gauges initialize to -20 dBFS (empty) when the applet first opens. |

## F1-F12 shortcut scoping

- The embedded CWX panel's F1-F12 shortcuts are driven by the active slice's mode via MainWindow (CwxPanel::setShortcutsEnabled) instead of panel visibility — they fire when the slice is in CW/CWL mode regardless of whether the panel is visible.
- DVK panel F-key bindings and CWX hotkeys are mutually exclusive — they do not fire simultaneously.
- CWX macros automatically release TX when the queue drains.

## Notes

- The level meter is properly suppressed during receive when the user disables "Level Meter During Receive" (met_in_rx), regardless of mic source. The applyLevelMeterReceiveGate() method handles this consistently for all mic sources including PC and RADE paths.
- The compression gauge is gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX to prevent confusing stale readings from the TX chain. Driven via updateCompression() slot, independent of the mic level path. Inverts display: 0 dB = no compression, -25 dB = full compression.
- Both ALC gauges initialize to -20 dBFS (empty) when the applet is first built, preventing the display of stale 0 dBFS readings during the initial rendering phase.
- The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).
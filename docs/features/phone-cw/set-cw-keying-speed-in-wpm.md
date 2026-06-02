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
4. Alternatively, click the numeric value adjacent to the slider and type a value directly (5–100) using your keyboard. The slider updates to match your typed value.

## What each control does

| Control           | Description                                                                                                                                                       | Default                                                                                                                  |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Speed (CW)        | Sets CW keying speed; calls TransmitModel::setCwSpeed. The adjacent QLineEdit accepts typed values (5–100) (v0.9.8, #2429).                                       | 20 WPM                                                                                                                   |
| ALC (Phone panel) | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Initialised to -20 dBFS on connect. | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| ALC (CW panel)    | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Initialised to -20 dBFS on connect.      | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode.                          |
| Compression       | Meter showing speech compression amount. Reversed fill: 0 at the top (no compression), -25 dB at the bottom (full compression). Gated on interlock TRANSMITTING state and speech processor enable (v0.9.7). | Driven by MeterModel COMPPEAK values (0–25 dB positive), negated for gauge display (v26.5.3).                            |
| Delay (CW)        | Sets CW break-in delay; calls TransmitModel::setCwDelay. The adjacent QLineEdit accepts typed values (0–2000) (v0.9.8, #2429).                                      | 500 ms                                                                                                                   |
| Sidetone          | Toggles CW sidetone monitor; calls TransmitModel::setCwSidetone. Also enables/disables the client-side low-latency CwSidetoneGenerator in lockstep (v0.9.1+).      | Off                                                                                                                      |
| Sidetone volume   | Sets CW monitor volume; calls TransmitModel::setMonGainCw. Also sets the local sidetone generator volume in lockstep. The adjacent QLineEdit accepts typed values (0–100) (v0.9.8, #2429). | 50                                                                                                                       |
| L / R pan (CW)    | Sets CW monitor stereo pan; calls TransmitModel::setMonPanCw and also applies constant-power pan to the local sidetone generator (v0.9.1+).                        | 50 (centre)                                                                                                              |
| Breakin           | Toggles full break-in (QSK); calls TransmitModel::setCwBreakIn.                                                                                                   | Off                                                                                                                      |
| Iambic            | Toggles iambic paddle keyer; calls TransmitModel::setCwIambic.                                                                                                    | Off                                                                                                                      |
| Pitch < / >       | QLineEdit with < / > buttons (CwTriBtn). Type a value (100–6000) or click the buttons to step by 10 Hz. Calls TransmitModel::setCwPitch (v0.9.8, #2429).          | 600 Hz                                                                                                                   |
| Level             | Shows microphone input peak level in dBFS (Phone panel). Suppressed to -150 when met_in_rx is off and not transmitting.                                           | -40 to +10 dBFS                                                                                                          |
| Mic profile       | Loads the named mic processing profile; calls TransmitModel::loadMicProfile.                                                                                      | Populated from radio micProfileList()                                                                                    |
| Mic source        | Selects microphone input source; calls TransmitModel::setMicSelection. Options: MIC, BAL, LINE, ACC, PC (plus any from micInputList()).                           | MIC                                                                                                                      |
| Mic gain          | Adjusts mic input level. For 'PC' source uses local PcMicGain persistence.                                                                                        | 50                                                                                                                       |
| +ACC              | Enables the accessory mic input mix; calls TransmitModel::setMicAcc.                                                                                              | Off                                                                                                                      |
| PROC              | Toggles the speech processor; calls TransmitModel::setSpeechProcessorEnable.                                                                                      | Off                                                                                                                      |
| NOR/DX/DX+        | Three-position processor level; calls TransmitModel::setSpeechProcessorLevel. Values: 0 (NOR), 1 (DX), 2 (DX+).                                                   | 0 (NOR)                                                                                                                  |
| DAX               | Enables DAX as the TX audio source; calls TransmitModel::setDax.                                                                                                  | Off                                                                                                                      |
| MON               | Enables TX sidetone monitor; calls TransmitModel::setSbMonitor.                                                                                                   | Off                                                                                                                      |
| Monitor volume    | Sets sideband monitor volume; calls TransmitModel::setMonGainSb.                                                                                                  | 0-100                                                                                                                    |

## Tips

- The Speed (CW) slider operates the radio's keyer speed. Changes take effect immediately and apply to the paddle, straight key, and any CWX text transmissions.
- The four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator. Click any value and type a number directly for SmartSDR parity (v0.9.8).
- The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone in lockstep. Adjusting speed does not affect sidetone pitch; pitch always follows the radio's `cw_pitch` setting automatically. In v26.5.3 the CW sidetone now routes to the user-selected audio output instead of the default output (#2899). In v26.6.1 the slider style refactoring applies the theme-aware primary slider style to all sliders, including Speed, Delay, Sidetone volume, and Pan.
- The **Level** gauge appears immediately on connect when the mic source is set to PC, or when RADE mode is active. In v26.5.3 the gauge behavior is unified: the level meter is suppressed to -150 dB during receive whenever `met_in_rx` is off and the radio is not transmitting, regardless of mic source or RADE mode. The previous exception for PC mic and RADE mode has been removed.
- The **Compression** gauge reads 0 dB during RX. It only shows a non-zero value while the radio's interlock reports a TRANSMITTING state and the speech processor is enabled, preventing stale TX-chain readings from appearing during receive (v0.9.7). In v26.5.3 the gauge now correctly accepts positive compression values (0–25 dB) from the meter model and negates them for the reversed gauge display.
- The **Mic gain** slider behaves differently when RADE mode is active: it acts as client-side RADE gain and stores its value under `PcMicGain` rather than sending a mic level command to the radio. This prevents silently overwriting the hardware mic setting. The same `PcMicGain` setting is shared between PC source mode and RADE mode.
- The **Breakin** toggle fully controls whether CW keyboard and MIDI key edges trigger TX. With Breakin on (QSK), key edges trigger TX and the break-in delay holds the relay. With Breakin off, keys are queued and you engage PTT manually. No automatic PTT envelope overrides this behavior (v0.9.7).
- The **Delay (CW)** slider value is cached immediately when changed, preventing the radio emission from snapping the slider back (v0.9.8, #2428).
- The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).
- The ALC gauge appears on both the Phone and CW sub-panels. Both gauges read from the same MeterModel::swAlcChanged source, so SSB operators watching mic gain see the same indicator CW operators use to verify clean keying envelope shape (v26.5.1, #2552). The previous HWALC meter (RCA voltage path) has been removed. Both gauges are initialised to -20 dBFS on connect to prevent showing stale values (v26.5.3).
- In v26.6.1 the Phone/CW applet now uses theme-aware styling for all controls. Sliders use the primary slider style via `applyPrimarySliderStyle()`, and label text colors follow theme secondary text colors. The deprecated inline `kSliderStyle` constant has been removed. The applet container also applies a theme container via `theme::setContainer()` for consistent appearance across themes.

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- Set sidetone volume
- Toggle CW sidetone
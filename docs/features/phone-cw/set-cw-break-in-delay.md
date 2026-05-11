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
5. Alternatively, click the value display next to the slider and type a number directly (0-2000 ms). Press Enter to apply the value.

## What each control does

| Control           | Description                                                                                                                                                                                                                                                                                                                      | Valid range                                                                                                              |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Delay (CW)        | Sets CW break-in delay; calls TransmitModel::setCwDelay. The adjacent QLineEdit accepts typed values (0-2000) (v0.9.8, #2429). In v0.9.8, setCwDelay was fixed to cache the value immediately so the radio emission doesn't snap the slider back (#2428). The QLineEdit uses QIntValidator to restrict input to the valid range. | 0-2000 ms (step 10)                                                                                                      |
| Breakin           | Toggles full break-in (QSK). With **Breakin** ON, key edges trigger TX and the break-in delay holds the relay before returning to receive. With **Breakin** OFF, keyed characters are queued and the operator engages PTT manually.                                                                                              | On / Off                                                                                                                 |
| ALC (Phone panel) | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS.                                                                                                                                                                | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| ALC (CW panel)    | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Uses HGauge::setFillFromRight mode: empty at -20 dBFS, fills leftward toward 0 dBFS.                                                                                                                     | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Range: -20 to 0 dBFS (red > -3).                            |
| Speed (CW)        | Sets CW keying speed; calls TransmitModel::setCwSpeed. The adjacent QLineEdit accepts typed values (5-100).                                                                                                                                                                                                                     | 5-100 WPM                                                                                                                |
| Sidetone          | Toggles CW sidetone monitor; calls TransmitModel::setCwSidetone. Also enables/disables the client-side low-latency CwSidetoneGenerator in lockstep (v0.9.1+). Both the radio's DAX-fed monitor and the local PortAudio sidetone are controlled by this single button.                                                              | On / Off                                                                                                                 |
| Sidetone volume   | Sets CW monitor volume; calls TransmitModel::setMonGainCw. Also sets the local sidetone generator volume in lockstep. The adjacent QLineEdit accepts typed values (0-100) (v0.9.8, #2429).                                                                                                                                      | 0-100                                                                                                                    |
| L / R pan (CW)    | Sets CW monitor stereo pan; calls TransmitModel::setMonPanCw and also applies constant-power pan to the local sidetone generator (v0.9.1+). Double-click recenters to 50 (centre).                                                                                                                                              | 0-100                                                                                                                    |
| Iambic            | Toggles iambic paddle keyer; calls TransmitModel::setCwIambic.                                                                                                                                                                                                                                                                   | On / Off                                                                                                                 |
| Pitch < / >       | QLineEdit with < / > buttons (CwTriBtn). Type a value (100-6000) or click the buttons to step by 10 Hz. Calls TransmitModel::setCwPitch (v0.9.8, #2429).                                                                                                                                                                         | 100-6000 Hz (step 10)                                                                                                    |
| Mic profile       | Loads the named mic processing profile; calls TransmitModel::loadMicProfile.                                                                                                                                                                                                                                                    | Populated from radio micProfileList()                                                                                    |
| Mic source        | Selects microphone input source; calls TransmitModel::setMicSelection.                                                                                                                                                                                                                                                          | MIC, BAL, LINE, ACC, PC (plus any from micInputList())                                                                   |
| Mic gain          | Adjusts mic input level. For 'PC' source uses local PcMicGain persistence.                                                                                                                                                                                                                                                      | 0-100                                                                                                                    |
| +ACC              | Enables the accessory mic input mix; calls TransmitModel::setMicAcc.                                                                                                                                                                                                                                                            | On / Off                                                                                                                 |
| PROC              | Toggles the speech processor; calls TransmitModel::setSpeechProcessorEnable.                                                                                                                                                                                                                                                    | On / Off                                                                                                                 |
| NOR/DX/DX+        | Three-position processor level; calls TransmitModel::setSpeechProcessorLevel.                                                                                                                                                                                                                                                   | 0 (NOR), 1 (DX), 2 (DX+)                                                                                                 |
| DAX               | Enables DAX as the TX audio source; calls TransmitModel::setDax.                                                                                                                                                                                                                                                                | On / Off                                                                                                                 |
| MON               | Enables TX sidetone monitor; calls TransmitModel::setSbMonitor.                                                                                                                                                                                                                                                                 | On / Off                                                                                                                 |
| Monitor volume    | Sets sideband monitor volume; calls TransmitModel::setMonGainSb.                                                                                                                                                                                                                                                                | 0-100                                                                                                                    |

## Tips

- A delay of 0 ms with **Breakin** enabled gives full QSK operation. Increase the delay to reduce relay wear during fast sending.
- The **Delay (CW)** slider steps in 10 ms increments. For fine adjustment, click the slider track and use the arrow keys (if keyboard shortcuts are enabled under `View > Keyboard Shortcuts`).
- The value display is an editable QLineEdit. Click it to type a precise value, then press Enter. The slider will move to match.

## Notes for v26.5.1

- **SW ALC meter replacement:** Both ALC gauges (Phone panel and CW panel) now read from MeterModel::swAlcChanged, which provides post-software-ALC SSB peak in dBFS. This replaces the previous HWALC (RCA voltage) path that produced meaningless readings. The new gauges use a -20 to 0 dBFS range with fill-from-right display and a red threshold at -3 dBFS.
- **Dual-panel ALC mirroring:** The Phone panel now has its own ALC gauge (m_alcGaugePhone) that mirrors the CW-panel ALC gauge (m_alcGaugeCw). Both gauges receive the same data from the single updateAlc() slot connected to MeterModel::swAlcChanged, ensuring consistent readings across voice and CW modes.

## Notes for v0.9.8

- **Editable value fields:** The four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator. Click any value and type a number directly for precise entry.
- **Delay value caching fixed:** The setCwDelay function now caches the value immediately, preventing the radio emission from snapping the slider back to the previous value.

## Notes for v0.9.7

- **Breakin behavior corrected:** The **Breakin** toggle now fully controls whether the CW keyboard and MIDI keying paths trigger TX automatically. Previously, an internal auto-PTT envelope overrode the **Breakin OFF** state and suppressed QSK hang time. That envelope has been removed. With **Breakin** OFF, keys queue characters and PTT must be engaged manually; with **Breakin** ON, key edges trigger TX immediately and `break_in_delay` governs the relay hang time.
- **Compression gauge gated on transmit state:** The **Compression** gauge in the Phone sub-panel now reads 0 dB during receive. It only shows a non-zero value when the radio's interlock reports TRANSMITTING and the speech processor is enabled. This prevents stale readings from the TX chain appearing while you are listening.
- **Mic gain slider in RADE mode:** When RADE mode is active, the **Mic gain** slider acts as a client-side RADE gain control and uses the `PcMicGain` setting, the same key used for PC mic source. The slider value is no longer sent to the radio as `mic_level` while RADE is active, which would otherwise silently overwrite the hardware mic setting. When RADE mode is deactivated, the slider reverts to reflecting the radio's reported mic level.
- **Level gauge in RADE mode:** When RADE mode is active the **Level** gauge remains live during receive (it does not require `met_in_rx` to be set), consistent with the existing PC mic source behavior. When RADE mode is deactivated the gauge resets to −150 dBFS.

## Notes for v0.9.3

- **Level gauge (Phone panel):** When the mic source is set to **PC**, the Level gauge now appears immediately on connect without waiting for the radio's `met_in_rx` flag to be set. This is because PC mic metering runs client-side and is independent of `met_in_rx`. For all other mic sources the previous suppression behavior is unchanged: the gauge reads −150 dBFS when `met_in_rx` is off and the radio is not transmitting.
- **VOX / Phone panel refresh:** VOX setters now emit `phoneStateChanged`, so the Phone sub-panel updates instantly when VOX is toggled via a keyboard shortcut. No manual panel interaction is needed to see the current VOX state.
- **Sidetone on Windows:** The CW sidetone stream (low-latency `CwSidetoneGenerator`) now starts immediately on connect on Windows. If you previously had to toggle **Sidetone** off and on after connecting to hear the local sidetone, this workaround is no longer needed.

## Indicators

| Indicator              | Range                   | Meaning                                                                 |
|------------------------|-------------------------|-------------------------------------------------------------------------|
| Level gauge            | -40 to +10 dBFS         | Microphone peak level. Suppressed to -150 when met_in_rx is off and not transmitting. |
| Compression gauge      | -25 to 0 dB             | Speech compression amount (reversed fill). Gated on TRANSMITTING state and speech processor enable. |
| ALC gauge (Phone panel)| -20 to 0 dBFS (fill from right, red > -3) | Automatic level control — post-software-ALC SSB peak, read from MeterModel::swAlcChanged. |
| ALC gauge (CW panel)   | -20 to 0 dBFS (fill from right, red > -3) | Mirror of the Phone-panel ALC gauge, identically scaled.                |

## Related

- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
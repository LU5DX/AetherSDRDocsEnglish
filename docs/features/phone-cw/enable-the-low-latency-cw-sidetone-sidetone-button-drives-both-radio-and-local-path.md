# Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)

Turning on the CW sidetone in AetherSDR enables two paths at once: the radio's DAX-fed monitor and a client-side tone generator with approximately 10 ms latency. A single button and a single volume slider control both in lockstep, so you hear a consistent tone regardless of network jitter.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet requires an active radio connection.
- The active slice must be in a CW mode. The applet panel automatically switches from the Phone sub-panel to the CW sub-panel when CW mode is detected.

## Steps

1. If the Phone/CW applet is not visible, click the **P/CW** tray button on the right sidebar to open it.
2. Confirm the CW sub-panel is displayed. If the Phone sub-panel is showing, switch the active slice to a CW mode on the radio; the panel switches automatically.
3. Click **Sidetone** to enable the sidetone. The button lights up when active.
4. Adjust the **Sidetone volume** slider to a comfortable level. The slider controls both the radio-side monitor volume and the client-side tone generator volume simultaneously.
5. Optionally, adjust **Pitch < / >** to set the sidetone frequency. The pitch follows the radio's `cw_pitch` setting automatically, but you can step it in 10 Hz increments using the **<** and **>** controls. You can also type a value directly (100–6000) in the QLineEdit field (v0.9.8).
6. For **Delay (CW)**, **Speed (CW)**, and **Sidetone volume**, click the numeric value and type a new number directly. Press Enter or Tab to apply. The slider and the typed value stay in sync automatically (v0.9.8).

## What each control does

| Control             | Kind                                                                                                                                                                                          | Default                                                                                                                  |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Level               | Meter. Shows microphone input peak level in dBFS (Phone panel). Suppressed to -150 when met_in_rx is off and not transmitting.                                                                | —                                                                                                                        |
| Compression         | Meter. Shows speech compression amount in dB (Phone panel). Reversed fill. Gated on radio's interlock TRANSMITTING state and speech processor enable.                                        | —                                                                                                                        |
| ALC (Phone panel)   | Meter. Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Initializes to -20 dBFS on construction. | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| ALC (CW panel)      | Meter. Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Initializes to -20 dBFS on construction. | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode. Updated in v26.5.3 to initialize at -20 dBFS. |
| Mic profile         | Combo box. Loads the named mic processing profile; calls TransmitModel::loadMicProfile.                                                                                                       | —                                                                                                                        |
| Mic source          | Combo box. Selects microphone input source (MIC, BAL, LINE, ACC, PC, plus any from micInputList()); calls TransmitModel::setMicSelection.                                                     | —                                                                                                                        |
| Mic gain            | Slider. Adjusts mic input level (0–100). For 'PC' source uses local PcMicGain persistence. Default: 50. Setting key: `PcMicGain`.                                                             | 50                                                                                                                       |
| +ACC                | Toggle button. Enables the accessory mic input mix; calls TransmitModel::setMicAcc.                                                                                                           | —                                                                                                                        |
| PROC                | Toggle button. Toggles the speech processor; calls TransmitModel::setSpeechProcessorEnable.                                                                                                   | —                                                                                                                        |
| NOR/DX/DX+          | Slider. Three-position processor level (0=NOR, 1=DX, 2=DX+); calls TransmitModel::setSpeechProcessorLevel.                                                                                   | 0 (NOR)                                                                                                                  |
| DAX                 | Toggle button. Enables DAX as the TX audio source; calls TransmitModel::setDax.                                                                                                               | —                                                                                                                        |
| MON                 | Toggle button. Enables TX sidetone monitor; calls TransmitModel::setSbMonitor.                                                                                                                | —                                                                                                                        |
| Monitor volume      | Slider. Sets sideband monitor volume (0–100); calls TransmitModel::setMonGainSb.                                                                                                              | —                                                                                                                        |
| Delay (CW)          | Slider with QLineEdit (v0.9.8). Type a value (0–2000 ms) directly in the field, or drag the slider. Calls TransmitModel::setCwDelay.                                                          | 500 ms                                                                                                                   |
| Speed (CW)          | Slider with QLineEdit (v0.9.8). Type a value (5–100 WPM) directly in the field, or drag the slider. Calls TransmitModel::setCwSpeed.                                                          | 20 WPM                                                                                                                   |
| Sidetone            | Toggle button. Toggles CW sidetone monitor; calls TransmitModel::setCwSidetone. Also enables/disables the client-side CwSidetoneGenerator in lockstep (v0.9.1+). Routes to user-selected audio output (v26.5.3). | —                                                                                                                        |
| Sidetone volume     | Slider with QLineEdit (v0.9.8). Type a value (0–100) directly in the field, or drag the slider. Calls TransmitModel::setMonGainCw. Also sets the local sidetone generator volume in lockstep. | 50                                                                                                                       |
| Pitch < / >         | QLineEdit with < / > buttons (CwTriBtn). Type a value (100–6000) or click the buttons to step by 10 Hz. Calls TransmitModel::setCwPitch (v0.9.8, #2429).                                      | 600 Hz                                                                                                                   |
| L / R pan (CW)      | Slider. Sets CW monitor stereo pan (0–100); calls TransmitModel::setMonPanCw and applies constant-power pan to local sidetone generator (v0.9.1+).                                             | 50 (centre)                                                                                                              |
| Breakin             | Toggle button. Toggles full break-in (QSK); calls TransmitModel::setCwBreakIn.                                                                                                                | —                                                                                                                        |
| Iambic              | Toggle button. Toggles iambic paddle keyer; calls TransmitModel::setCwIambic.                                                                                                                 | —                                                                                                                        |

## Direct value entry (v0.9.8)

In v0.9.8 the four numeric value labels in the CW sub-panel were upgraded from read-only labels to editable QLineEdit fields:

- **Delay (CW)** — Type any value from 0 to 2000 ms. Press Enter or Tab to apply. The adjacent slider moves to match.
- **Speed (CW)** — Type any value from 5 to 100 WPM. Press Enter or Tab to apply. The adjacent slider moves to match.
- **Sidetone volume** — Type any value from 0 to 100. Press Enter or Tab to apply. The adjacent slider moves to match.
- **Pitch < / >** — Type any value from 100 to 6000 Hz. Press Enter or Tab to apply. The **<** and **>** buttons step by 10 Hz.

When you type a value that is outside the valid range, the field clamps the value to the nearest valid boundary (SmartSDR parity).

## ALC meters (v26.5.1+)

In v26.5.1 both the Phone and CW sub-panels received identical ALC gauges that read from the software ALC meter (MeterModel::swAlcChanged). This replaces the previous hardware ALC (RCA voltage) path that produced meaningless readings.

- Both gauges display in dBFS with a range of -20 to 0 dBFS.
- The fill direction is right-to-left: empty at -20 dBFS, full at 0 dBFS.
- A red zone appears above -3 dBFS.
- Values outside the [-20, 0] range clamp to the nearest endpoint.
- The single updateAlc() slot drives both gauges simultaneously, ensuring SSB and CW operators see the same post-ALC peak reading.
- In v26.5.3, both gauges initialize to -20 dBFS on construction, preventing a brief visual flash at 0 dBFS during startup.

## RADE mode and the mic level slider

When RADE mode is active, the **Mic gain** slider operates as a client-side gain control rather than sending a mic level command to the radio. The slider value is stored under `PcMicGain` (the same setting used when the mic source is PC) and is not written to the radio's `mic_level` property while RADE is active. This prevents RADE mode from silently overwriting your hardware mic setting on the radio.

- The **Level** meter remains active during RX when RADE is enabled, so you can monitor input level without transmitting.
- When RADE mode is deactivated, the slider reverts to reflecting the radio's `mic_level` and the Level meter returns to its normal suppression behaviour (hidden during RX unless `met_in_rx` is on).

## CW sidetone audio output (v26.5.3)

In v26.5.3 the CW sidetone generator now routes to the user-selected audio output device instead of the default system output (#2899). If you have multiple audio interfaces configured in AetherSDR, the sidetone follows the output device selected in **Settings > Audio > Output device**.

## Level meter receive gating (v26.5.3)

In v26.5.3 the suppression logic for the mic level meter was refactored. Previously, the Level gauge was suppressed inline within `updateMeters()`, with exceptions for PC mic and RADE modes. Now the suppression check lives in a dedicated `applyLevelMeterReceiveGate()` method that is called whenever the radio's transmit state changes or when RADE mode is activated or deactivated. This ensures the meter is always correctly dimmed or shown regardless of which event triggers the state change.

## Compression gauge mapping (v26.5.3)

In v26.5.3 the Compression gauge mapping was corrected. The MeterModel exposes the `COMPPEAK` meter as a positive 0–25 dB compression amount. The gauge face is reversed: 0 dB displayed means no compression, -25 dB means full compression. The gauge now converts the positive value to negative for display, so -25 corresponds to maximum compression and 0 to no compression.

## Tips

- The client-side tone generator pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. You do not need to configure them separately for the local path.
- Double-clicking the **L / R pan (CW)** slider resets it to centre (50).
- The **Compression** gauge reads 0 dB during RX. It only shows a non-zero value when the radio's interlock reports the TRANSMITTING state and the speech processor (**PROC**) is enabled. This prevents stale readings from the TX chain being displayed while you are receiving.
- With **Breakin** off, key presses are queued and TX must be engaged manually with PTT. With **Breakin** on (QSK), key edges trigger TX directly and `break_in_delay` controls the relay hang time. No automatic PTT envelope overrides this behaviour.
- The **Delay (CW)** slider now updates its cached value immediately when dragged, preventing the radio from snapping the slider back to its previous position (v0.9.8, #2428).
- The ALC gauge on both panels reads the same meter source, so you can monitor ALC regardless of which sub-panel is visible.

## Troubleshooting

- **No tone heard despite Sidetone being enabled** — Confirm the **Sidetone volume** slider is above 0. Also check that your system audio output device is correctly configured in **Settings > Audio > Output device**, as the client-side generator now routes to the user-selected output.
- **Sidetone button is not visible** — The CW sub-panel only appears when the active slice is in CW mode. Switch the active slice to CW on the radio; the applet panel switches automatically.
- **Pitch does not match expectation** — Pitch follows the radio's `cw_pitch` setting. Adjust it using **Pitch < / >** in the applet, which updates the radio setting in 10 Hz steps.
- **Compression gauge always shows 0** — This is expected during RX. The gauge is gated on the radio's interlock TRANSMITTING state. It will show compression only while you are transmitting with **PROC** enabled.
- **Breakin OFF does not hold TX between characters** — With **Breakin** off, AetherSDR no longer applies an automatic PTT envelope. Engage PTT manually before sending and release it when finished.
- **Mic gain slider has no effect in RADE mode**
# Phone/CW Applet

The Phone/CW applet provides mode-aware transmit controls. In voice modes (Phone sub-panel) it shows microphone, processor, and monitor controls. It automatically switches to the CW sub-panel with delay, speed, sidetone, iambic, and pitch controls when the active slice is in CW mode.

Both sub-panels include an ALC gauge driven by the software ALC meter (MeterModel::swAlcChanged), replacing the previous hardware ALC (RCA voltage) path that produced meaningless readings.

## Accessing the Phone/CW Applet

If the Phone/CW applet is not visible, click the **P/CW** tray button on the right sidebar to open it.

The CW sub-panel appears automatically when the active slice is in a CW mode. Switch the active slice to CW on the radio to switch from the Phone sub-panel to the CW sub-panel.

## Slider style theme support (v26.6.1)

In v26.6.1 all sliders within the Phone/CW applet now use `applyPrimarySliderStyle()` instead of a hard-coded stylesheet. This means sliders automatically follow the current theme's accent colours and background palette. If you change the theme, the slider appearance updates without requiring a restart.

## CW Sidetone Overview

Turning on the CW sidetone enables two paths simultaneously: the radio's DAX-fed monitor and a client-side tone generator with approximately 10 ms latency. A single button and a single volume slider control both in lockstep, ensuring consistent tone regardless of network jitter.

The client-side tone generator pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. You do not need to configure them separately for the local path.

## Steps

1. If the Phone/CW applet is not visible, click the **P/CW** tray button on the right sidebar to open it.
2. Confirm the CW sub-panel is displayed. If the Phone sub-panel is showing, switch the active slice to a CW mode on the radio; the panel switches automatically. The applet recognises bare **CW**, **CWU**, and **CWL** as CW modes.
3. Click **Sidetone** to enable the sidetone. The button lights up when active.
4. Adjust the **Sidetone volume** slider to a comfortable level. The slider controls both the radio-side monitor volume and the client-side tone generator volume simultaneously.
5. Optionally, adjust **Pitch < / >** to set the sidetone frequency. The pitch follows the radio's `cw_pitch` setting automatically, but you can step it in 10 Hz increments using the **<** and **>** controls. You can also type a value directly (100–6000) in the QLineEdit field.
6. For **Delay (CW)**, **Speed (CW)**, and **Sidetone volume**, click the numeric value and type a new number directly. Press Enter or Tab to apply. The slider and the typed value stay in sync automatically.

## Control Reference

| Control | Kind | Default | Valid Range | Behavior |
|---------|------|---------|-------------|----------|
| Level | Meter | — | -40 to +10 dBFS (red > 0 dBFS) | Shows microphone input peak level in dBFS (Phone panel). Suppressed to -150 when met_in_rx is off and not transmitting. Hidden when the radio's mic level meter is unavailable (e.g. when the radio is modulated by AetherSDR). Hover over the gauge for an exact numeric readout in dB with one decimal place. |
| Compression | Meter | — | -25 to 0 dB (reversed fill) | Shows speech compression amount in dB (Phone panel). Gated on radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX. Hover over the gauge for an exact numeric readout in dB with one decimal place. |
| ALC (Phone panel) | Meter | — | -20 to 0 dBFS (red > -3 dBFS) | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Hover over the gauge for an exact numeric readout in dBFS with one decimal place. Initializes to -20 dBFS on construction. |
| ALC (CW panel) | Meter | — | -20 to 0 dBFS (red > -3 dBFS) | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Hover over the gauge for an exact numeric readout in dBFS with one decimal place. Initializes to -20 dBFS on construction. Uses HGauge::setFillFromRight mode. |
| Mic profile | Combo box | — | Populated from radio micProfileList() | Loads the named mic processing profile; calls TransmitModel::loadMicProfile. |
| Mic source | Combo box | — | MIC, BAL, LINE, ACC, PC (plus any from micInputList()) | Selects microphone input source; calls TransmitModel::setMicSelection. When the radio cannot accept a client-side mic source selection, the combo is disabled, shows only "PC", and displays a tooltip explaining that the radio takes transmit audio from this computer. |
| Mic gain | Slider | 50 | 0–100 | Adjusts mic input level. For 'PC' source uses local PcMicGain persistence (`PcMicGain` setting key). Radio always reports mic_level=0 when source=PC; value kept client-side. The `micLevelChanged` signal is emitted only when the client owns the gain (RADE mode, or selectable mic inputs with PC selected). |
| +ACC | Toggle button | — | — | Enables the accessory mic input mix; calls TransmitModel::setMicAcc. |
| PROC | Toggle button | — | — | Toggles the speech processor; calls TransmitModel::setSpeechProcessorEnable. |
| NOR/DX/DX+ | Slider | 0 (NOR) | 0 (NOR), 1 (DX), 2 (DX+) | Three-position processor level; calls TransmitModel::setSpeechProcessorLevel. |
| DAX | Toggle button | — | — | Enables DAX as the TX audio source; calls TransmitModel::setDax. Hidden when this client cannot select DAX as a TX source; the button is forced off when hidden. |
| MON | Toggle button | — | — | Enables TX sidetone monitor; calls TransmitModel::setSbMonitor. |
| Monitor volume | Slider | — | 0–100 | Sets sideband monitor volume; calls TransmitModel::setMonGainSb. |
| Delay (CW) | Slider with QLineEdit | 500 ms | 0–2000 ms (step 10) | Sets CW break-in delay; calls TransmitModel::setCwDelay. The adjacent QLineEdit accepts typed values (0–2000). Cached immediately when dragged to prevent radio snapping back (#2428). |
| Speed (CW) | Slider with QLineEdit | 20 WPM | 5–100 WPM | Sets CW keying speed; calls TransmitModel::setCwSpeed. The adjacent QLineEdit accepts typed values (5–100). |
| Sidetone | Toggle button | — | — | Toggles CW sidetone monitor; calls TransmitModel::setCwSidetone. Also enables/disables the client-side CwSidetoneGenerator in lockstep. Routes to user-selected audio output (v26.5.3). |
| Sidetone volume | Slider with QLineEdit | 50 | 0–100 | Sets CW monitor volume; calls TransmitModel::setMonGainCw. Also sets the local sidetone generator volume in lockstep. The adjacent QLineEdit accepts typed values (0–100). |
| L / R pan (CW) | Slider | 50 (centre) | 0–100 | Sets CW monitor stereo pan; calls TransmitModel::setMonPanCw and also applies constant-power pan to the local sidetone generator. Double-click recenters to 50 (centre). |
| Breakin | Toggle button | — | — | Toggles full break-in (QSK); calls TransmitModel::setCwBreakIn. With Breakin ON, key edges trigger TX and break_in_delay holds the relay. With Breakin OFF, keys are queued and the operator engages PTT manually. No auto-PTT envelope overrides this behaviour. |
| Iambic | Toggle button | — | — | Toggles iambic paddle keyer; calls TransmitModel::setCwIambic. |
| Pitch < / > | QLineEdit with < / > buttons (CwTriBtn) | 600 Hz | 100–6000 Hz (step 10) | Type a value (100–6000) or click the buttons to step by 10 Hz. Calls TransmitModel::setCwPitch. |

## Direct Value Entry

The four numeric value labels in the CW sub-panel are editable QLineEdit fields:

- **Delay (CW)** — Type any value from 0 to 2000 ms. Press Enter or Tab to apply. The adjacent slider moves to match.
- **Speed (CW)** — Type any value from 5 to 100 WPM. Press Enter or Tab to apply. The adjacent slider moves to match.
- **Sidetone volume** — Type any value from 0 to 100. Press Enter or Tab to apply. The adjacent slider moves to match.
- **Pitch < / >** — Type any value from 100 to 6000 Hz. Press Enter or Tab to apply. The **<** and **>** buttons step by 10 Hz.

When you type a value outside the valid range, the field clamps the value to the nearest valid boundary (SmartSDR parity).

## ALC Meters

Both the Phone and CW sub-panels contain identical ALC gauges that read from the software ALC meter (MeterModel::swAlcChanged). This replaces the previous hardware ALC (RCA voltage) path that produced meaningless readings.

- Both gauges display in dBFS with a range of -20 to 0 dBFS.
- The fill direction is right-to-left: empty at -20 dBFS, full at 0 dBFS.
- A red zone appears above -3 dBFS.
- Values outside the [-20, 0] range clamp to the nearest endpoint.
- The single updateAlc() slot drives both gauges simultaneously, ensuring SSB and CW operators see the same post-ALC peak reading.
- Both gauges initialize to -20 dBFS on construction, preventing a brief visual flash at 0 dBFS during startup.
- Hovering over either ALC gauge shows an exact numeric readout in dBFS with one decimal place, allowing you to read the precise SSB-peak level instead of estimating against the -20 to 0 scale.

## CW Sidetone Audio Output

The CW sidetone generator routes to the user-selected audio output device instead of the default system output (#2899). If you have multiple audio interfaces configured in AetherSDR, the sidetone follows the output device selected in **Settings > Audio > Output device**.

## Level Meter Receive Gating

The mic level meter suppression uses a dedicated `applyLevelMeterReceiveGate()` method called whenever the radio's transmit state changes or when RADE mode is activated or deactivated. This ensures the meter is always correctly dimmed or shown regardless of which event triggers the state change.

## Compression Gauge Mapping

The compression gauge reads from the MeterModel `COMPPEAK` meter as a positive 0–25 dB compression amount. The gauge face is reversed: 0 dB displayed means no compression, -25 dB means full compression. The gauge converts the positive value to negative for display, so -25 corresponds to maximum compression and 0 to no compression. Hovering over the gauge shows a positive dB value (the amount of compression applied), with one decimal place.

## Mic Source on Radios with Fixed TX Audio Input

When the radio takes its transmit audio from this computer and its own input selection is made on the radio (for example, when AetherSDR is modulating the radio via the network), the **Mic source** combo box is automatically disabled and shows only "PC" as the available source. The tooltip explains that the radio takes transmit audio from this computer and its own input selection is made on the radio. In this state the combo box does not look broken: it states the effective source. The radio-side model is told the source is PC so downstream checks (such as radiocert warnings about transmit audio capture) do not fire incorrectly.

The **Level** meter gauge is also hidden in this state, since the radio is not reporting a meaningful mic level for the network-fed path. The **DAX** button is hidden as well when DAX cannot be selected as a TX source for the current radio configuration.

## Tips

- Double-clicking the **L / R pan (CW)** slider resets it to centre (50).
- The **Compression** gauge reads 0 dB during RX. It only shows a non-zero value when the radio's interlock reports the TRANSMITTING state and the speech processor (**PROC**) is enabled.
- With **Breakin** off, key presses are queued and TX must be engaged manually with PTT. With **Breakin** on (QSK), key edges trigger TX directly and `break_in_delay` controls the relay hang time. No automatic PTT envelope overrides this behaviour.
- The **Delay (CW)** slider updates its cached value immediately when dragged, preventing the radio from snapping
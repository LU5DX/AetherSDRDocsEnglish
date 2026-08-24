# Read the SW ALC meter (post-software-ALC SSB peak) on the Phone or CW panel

The **ALC** gauge on the Phone or CW sub-panel shows the post-software-ALC SSB peak in dBFS. This meter helps you set your microphone gain or CW keying envelope so you transmit at an appropriate level without overdriving the audio chain.

## What each control does

| Control | Label | Behavior | Valid range | Default | Setting key |
|---------|-------|----------|-------------|---------|-------------|
| ALC gauge (Phone panel) | **ALC** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Red zone above -3 dBFS. Initialised to -20 dBFS on construction. Hover over the gauge for an exact dBFS readout. | -20 to 0 dBFS | — | None |
| ALC gauge (CW panel) | **ALC** | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Initialised to -20 dBFS on construction. Hover over the gauge for an exact dBFS readout. | -20 to 0 dBFS | — | None |

## What each Phone/CW control does

| Control | Label | Behavior | Valid range | Default | Setting key |
|---------|-------|----------|-------------|---------|-------------|
| Level meter | **Level** | Shows microphone input peak level in dBFS (Phone panel). Suppressed to -150 when **Level Meter During Receive** is off and not transmitting. Hover over the gauge for an exact dB readout. | -40 to +10 dBFS (red > 0) | — | None |
| Compression meter | **Compression** | Shows speech compression amount in dB (Phone panel). Gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX. Conversion: MeterModel exposes COMPPEAK as positive 0..25 dB, the gauge displays reversed -25..0 dB. Hover over the gauge for an exact positive dB readout. | -25 to 0 dB (reversed fill) | — | None |
| Mic profile | **Mic profile** | Loads a named mic processing profile from the radio. | Populated from radio micProfileList() | — | None |
| Mic source | **Mic source** | Selects the microphone input source. When the radio is modulated by AetherSDR (host modulation enabled), this control is disabled and locked to **PC** only, with a tooltip explaining that other sources are FlexRadio jacks. If the radio's transmit audio is supplied from the computer and the client cannot select the input (e.g. a radio whose own input selection is made on the radio), the combo box is narrowed to **PC** only with a tooltip explaining that this radio takes transmit audio from the computer. | MIC, BAL, LINE, ACC, PC (plus any from micInputList()) | — | None |
| Mic gain | **Mic gain** | Adjusts mic input level. For 'PC' source uses local PcMicGain persistence. When the client owns the mic gain (RADE active, or a radio whose input selection is locked to PC), the value is emitted locally; otherwise it is sent to the radio. | 0-100 | 50 | PcMicGain |
| +ACC | **+ACC** | Enables the accessory mic input mix. | — | — | None |
| PROC | **PROC** | Toggles the speech processor. | — | — | None |
| NOR/DX/DX+ | **NOR/DX/DX+** | Three-position processor level. | 0 (NOR), 1 (DX), 2 (DX+) | 0 | None |
| DAX | **DAX** | Enables DAX as the TX audio source. Hidden when the radio is not capable of DAX TX audio. | — | — | None |
| MON | **MON** | Enables TX sidetone monitor. | — | — | None |
| Monitor volume | **Monitor volume** | Sets sideband monitor volume. | 0-100 | — | None |
| ALC gauge (Phone panel) | **ALC** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Red zone above -3 dBFS. Initialised to -20 dBFS on construction. Hover over the gauge for an exact dBFS readout. | -20 to 0 dBFS (red > -3) | — | None |
| Delay (CW) | **Delay (CW)** | Sets CW break-in delay. The adjacent QLineEdit accepts typed values (0–2000). | 0-2000 ms (step 10) | 500 | None |
| Speed (CW) | **Speed (CW)** | Sets CW keying speed. The adjacent QLineEdit accepts typed values (5–100). | 5-100 WPM | 20 | None |
| Sidetone | **Sidetone** | Toggles CW sidetone monitor and the client-side low-latency CwSidetoneGenerator in lockstep. Routes to the user-selected audio output. | — | — | None |
| Sidetone volume | **Sidetone volume** | Sets CW monitor volume. Controls both radio-side (mon_gain_cw) and client-side sidetone volumes. The adjacent QLineEdit accepts typed values (0–100). | 0-100 | 50 | None |
| L / R pan (CW) | **L / R pan (CW)** | Sets CW monitor stereo pan. Applies constant-power pan to the local sidetone generator. Double-click recenters to 50 (centre). | 0-100 | 50 | None |
| Breakin | **Breakin** | Toggles full break-in (QSK). With Breakin ON key edges trigger TX; with Breakin OFF keys are queued and the operator engages PTT manually. | — | — | None |
| Iambic | **Iambic** | Toggles iambic paddle keyer. | — | — | None |
| Pitch < / > | **Pitch < / >** | QLineEdit with < / > buttons. Type a value (100–6000) or click the buttons to step by 10 Hz. | 100-6000 Hz (step 10) | 600 | None |
| ALC gauge (CW panel) | **ALC** | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Initialised to -20 dBFS on construction. Hover over the gauge for an exact dBFS readout. | -20 to 0 dBFS (red > -3) | — | None |

## Notes

- **Mode detection (v26.8.4):** The applet now uses a single `isCwMode()` helper to detect CW-mode slices. A Flex reports bare "CW"; an Icom and an HL2 spell the same mode CWU, and CWL is the reverse-side one. All three drive the CW sub-panel.
- **Mic source on radios the client cannot select (v26.8.4):** When the radio takes transmit audio from the computer and the client cannot choose the input (the radio's own input selection is made on the radio), the **Mic source** combo box is rebuilt with only **PC** listed, disabled, and given a tooltip: "This radio takes transmit audio from this computer. Its own input selection is made on the radio." The model is told the mic selection is **PC** so radiocert does not warn that transmit audio capture is not running on a radio where that is simply not how audio gets there.
- **Mic gain ownership (v26.8.4):** The client owns mic gain when RADE is active, or when the radio's input selection is locked to PC. In those cases the gain value is emitted locally. Otherwise it is sent to the radio.
- **Level meter visibility (v26.8.4):** The Level gauge is hidden when the radio does not report a mic level meter.
- **DAX visibility (v26.8.4):** The **DAX** toggle is hidden when the radio is not capable of DAX TX audio, and when hidden it is forced off.
- **ALC meter source (v26.5.1, #2552):** Both ALC gauges read MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS), replacing the previous HWALC (RCA voltage) path that produced meaningless readings.
- In v26.5.3 both ALC gauges are initialised to -20 dBFS on construction, preventing a momentary full-scale reading at startup.
- The Compression gauge in v26.5.3 uses the MeterModel COMPPEAK value (positive 0..25 dB) and inverts it for the reversed -25..0 dB gauge display.
- The level meter suppression logic has been refactored in v26.5.3 into a dedicated `applyLevelMeterReceiveGate()` method, called when transmit state changes or the RADE active state changes.
- In v26.6.1 slider styling was updated to use the theme system instead of hardcoded color values. All sliders in the Phone/CW applet now respect the current theme.
- In v26.7.4 the Level, Compression, and ALC gauges gained mouse-over hover popups that show the exact meter reading in dB or dBFS. Hover over any gauge during transmission to read the precise value.
- In v26.7.4 the Mic source combo box is automatically disabled and locked to **PC** when the radio is modulated by AetherSDR (host modulation enabled), with a tooltip explaining why.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
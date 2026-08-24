# Phone/CW Applet

The Phone/CW applet provides a mode-aware transmit panel that automatically switches between Phone and CW controls based on the active slice's mode. In voice modes, it shows microphone, processor, and monitor controls. When the active slice is in CW mode, it automatically switches to CW controls including delay, speed, sidetone, iambic, and pitch settings.

## Opening the Applet

1. Click the **P/CW** button in the right sidebar or confirm it is already visible in the Applet Panel.
2. The applet requires an active connection to a FLEX-8600 radio.
3. The applet automatically switches between Phone and CW sub-panels based on the active slice's mode.

## Phone Panel Controls

The Phone panel is displayed when the active slice is in a voice mode (LSB, USB, AM, FM, etc.).

### Microphone Section

| Control | Behavior | Default |
|---------|----------|---------|
| **Level** | Shows microphone input peak level in dBFS. Hover the mouse over the gauge to see the exact reading with one decimal place (e.g., "-12.3 dB"). Suppressed to -150 when `met_in_rx` is off and not transmitting. | — |
| **Mic profile** | Selects a named microphone processing profile from the radio's available profiles. Calls `TransmitModel::loadMicProfile`. | — |
| **Mic source** | Selects microphone input source. Options include MIC, BAL, LINE, ACC, PC, plus any from the radio's `micInputList()`. When the radio is modulated by AetherSDR (host modulation enabled), the combo box is narrowed to only "PC" and disabled, with a tooltip explaining that the radio's own input selection is made on the radio. In v26.8.4, on radios without selectable mic inputs, the model is explicitly set to PC to match the UI. Calls `TransmitModel::setMicSelection`. | — |
| **Mic gain** | Adjusts microphone input level. Range 0-100. For 'PC' source, uses local `PcMicGain` persistence since the radio always reports `mic_level=0` when source=PC. In v26.8.4, the local gain is only applied when the client owns the gain (PC mode with selectable inputs, or RADE mode). | 50 |
| **+ACC** | Toggles the accessory microphone input mix. Calls `TransmitModel::setMicAcc`. | — |

### Speech Processor Section

| Control | Behavior | Default |
|---------|----------|---------|
| **PROC** | Toggles the speech processor. Calls `TransmitModel::setSpeechProcessorEnable`. | — |
| **NOR/DX/DX+** | Three-position processor level slider: 0 (NOR), 1 (DX), 2 (DX+). Calls `TransmitModel::setSpeechProcessorLevel`. | 0 |
| **Compression** | Shows speech compression amount in dB. Hover the mouse over the gauge to see the exact compression reading with one decimal place (e.g., "6.5 dB"). Gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX. Driven via `updateCompression()`, independent of the mic level path. Range -25 to 0 dB (reversed fill). | — |

### Audio Routing Section

| Control | Behavior | Default |
|---------|----------|---------|
| **DAX** | Enables DAX as the TX audio source. Calls `TransmitModel::setDax`. In v26.8.4, this button is hidden on radios that do not support DAX TX. | — |
| **MON** | Enables TX sidetone monitor. Calls `TransmitModel::setSbMonitor`. | — |
| **Monitor volume** | Sets sideband monitor volume. Calls `TransmitModel::setMonGainSb`. Range 0-100. | — |

### ALC Meter

| Control | Behavior | Range |
|---------|----------|-------|
| **ALC (Phone panel)** | Shows automatic level control reading from `MeterModel::swAlcChanged` (post-software-ALC SSB peak in dBFS). Hover the mouse over the gauge to see the exact reading with one decimal place (e.g., "-8.5 dBFS"). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Red zone above -3 dBFS. Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). | -20 to 0 dBFS |

## CW Panel Controls

The CW panel is displayed when the active slice is in CW or CWL mode.

### Timing and Speed Section

| Control | Behavior | Default |
|---------|----------|---------|
| **Breakin** | Toggles full break-in (QSK). When ON (QSK), key edges trigger TX and `break_in_delay` holds the relay. When OFF, keys are queued and the operator engages PTT manually. In v0.9.7, the CW keyboard/MIDI paths now fully honor this setting — the previous auto-PTT envelope that masked Breakin OFF and killed QSK hang time has been removed. | — |
| **Delay (CW)** | Sets CW break-in delay in milliseconds. Range 0-2000 ms (step 10). The adjacent QLineEdit accepts typed values (0–2000) (v0.9.8, #2429). In v0.9.8, `setCwDelay` was fixed to cache the value immediately so the radio emission doesn't snap the slider back (#2428). | 500 ms |
| **Speed (CW)** | Sets CW keying speed in words per minute. Range 5-100 WPM. The adjacent QLineEdit accepts typed values (5–100) (v0.9.8, #2429). | 20 WPM |

### Sidetone Section

| Control | Behavior | Default |
|---------|----------|---------|
| **Sidetone** | Toggles CW sidetone monitor. Controls both the radio's DAX-fed monitor and the client-side low-latency CwSidetoneGenerator (~10 ms latency) in lockstep (v0.9.1+). Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` automatically. In v26.5.3, the CW sidetone routes to the user-selected audio output instead of the default output (#2899). | — |
| **Sidetone volume** | Sets CW monitor volume. Controls both the radio-side (`mon_gain_cw`) and client-side sidetone volume in lockstep (v0.9.1+). Range 0-100. The adjacent QLineEdit accepts typed values (0–100) (v0.9.8, #2429). | 50 |
| **L / R pan (CW)** | Sets CW monitor stereo pan. Calls `TransmitModel::setMonPanCw` and applies constant-power pan to the local sidetone generator (v0.9.1+). Double-click recenters to 50 (centre). Range 0-100. | 50 |

### Keying Section

| Control | Behavior | Default |
|---------|----------|---------|
| **Iambic** | Toggles iambic paddle keyer. Calls `TransmitModel::setCwIambic`. | — |
| **Pitch < / >** | Sets CW sidetone pitch. QLineEdit with < / > buttons (CwTriBtn). Type a value (100–6000) or click the buttons to step by 10 Hz. Calls `TransmitModel::setCwPitch` (v0.9.8, #2429). | 600 Hz |

### ALC Meter

| Control | Behavior | Range |
|---------|----------|-------|
| **ALC (CW panel)** | Mirrors the Phone-panel ALC gauge; both read from `MeterModel::swAlcChanged` for consistent readings across voice and CW. Hover the mouse over the gauge to see the exact reading with one decimal place (e.g., "-8.5 dBFS"). Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses `HGauge::setFillFromRight` mode. Red zone above -3 dBFS. | -20 to 0 dBFS |

## CWX Panel Integration

The embedded CWX panel's F1-F12 shortcuts are driven by the active slice's mode via `MainWindow (CwxPanel::setShortcutsEnabled)` instead of panel visibility — they fire when the slice is in CW/CWL mode regardless of whether the panel is visible (#2582), while staying mutually exclusive with DVK panel F-key bindings. CWX macros also release TX automatically when the queue drains (#2450, #2507).

## Notes

- In v26.6.1, all applet styling uses the theme system. Sliders and labels adapt to the selected theme rather than using hardcoded colors.
- The ALC gauge on both panels is driven by the software ALC meter (`MeterModel::swAlcChanged`, post-SSBMeter-peak dBFS, #2552), replacing the previous HWALC (RCA voltage) path that produced meaningless readings.
- In v0.9.8, the four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator — click any value and type a number directly (SmartSDR parity).
- The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).
- With Breakin OFF, no auto-PTT envelope is applied. The radio will not transmit queued characters until you engage PTT manually. Release PTT after the last character is sent to return to RX.
- If you are using an external amplifier, Breakin OFF gives you time to close the amplifier's T/R relay before the keyer starts sending.
- In v26.5.3, CW sidetone is automatically routed to the audio output device selected in AetherSDR Audio settings, not the system default output. Check your audio output selection if you hear no sidetone.
- In v26.7.4, all gauges (Level, Compression, and both ALC gauges) now display exact numeric readings in a popup when you hover the mouse over them (#3936). The Level gauge shows dB, the Compression gauge shows positive dB compression, and the ALC gauges show dBFS — all with one decimal place.
- In v26.7.4, when the radio is modulated by AetherSDR (host modulation enabled), the **Mic source** combo box is locked to "PC" and displays a tooltip explaining that only the PC microphone input is available. This prevents confusion from selecting non-existent radio jacks.
- In v26.8.4, when the radio is modulated by AetherSDR (host modulation enabled), the **Mic source** combo box is narrowed to only "PC" rather than showing disabled entries for other sources. The model is explicitly set to PC state to keep the radio and UI consistent. The tooltip explains that the radio's own input selection is made on the radio.
- In v26.8.4, on radios where the mic level meter is not available, the **Level** gauge is hidden rather than showing a meaningless reading.
- In v26.8.4, on radios that do not support DAX TX, the **DAX** button is hidden and unchecked.
- In v26.8.4, the applet now uses a single shared CW-mode check (`isCwMode()`) that recognizes "CW", "CWU", and "CWL" across radio brands, replacing the previous hardcoded "CW" check that only matched Flex radios.

## Troubleshooting

- **The radio transmits immediately when a key is pressed, even with Breakin apparently off** — This was a known issue in versions prior to v0.9.7, where an auto-PTT envelope overrode the Breakin setting. Confirm AetherSDR is v0.9.7 or later.
- **The CW panel is not visible; Phone controls are shown** — The applet switches to the CW sub-panel automatically only when the active slice is in a CW mode. Change the slice mode to CW on the radio. In v26.8.4, the applet recognizes CW, CWU, and CWL modes across radio brands.
- **The Delay slider snaps back after typing a value** — This was fixed in v0.9.8 (#2428). The value is now cached immediately so the radio emission does not force the slider back.
- **The ALC meter shows a frozen reading** — In v26.5.3, the ALC meter is initialized to -20 dBFS at construction. If the reading stays at -20 dBFS, verify the radio is transmitting and audio signal is present. Hover over the gauge to see the exact numeric value.
- **The mic level meter shows -150 dBFS during RX** — In v26.5.3, the level meter is suppressed during receive when the "Meter level during receive" option is disabled in TransmitModel settings. To see mic level during RX, enable that option.
- **No CW sidetone heard** — In v26.5.3, verify the correct audio output is selected in AetherSDR Audio settings. Sidetone now routes to the user's audio output, not the system default output (#2899).
- **Mic source shows only PC on a Flex radio** — In v26.8.4, this is expected when the radio takes transmit audio from the computer over the network. The radio's own input selection is made on the radio itself, not in AetherSDR.
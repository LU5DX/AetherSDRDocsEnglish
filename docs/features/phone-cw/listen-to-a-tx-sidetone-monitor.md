# Phone/CW Applet

The Phone/CW applet is a mode-aware transmit panel that shows Phone controls (microphone, processor, monitor) in voice modes and automatically switches to CW controls (delay, speed, sidetone, iambic, pitch) when the active slice is in CW mode.

In v0.9.8, the four CW value labels (Delay, Speed, Sidetone Volume, Pitch) are now QLineEdit widgets with QIntValidator — click any value and type a number directly (SmartSDR parity).

In v26.5.3, the CW sidetone now routes to the user-selected audio output instead of the default output (#2899). The ALC gauges on both panels now initialize to -20 dBFS on startup.

In v26.6.1, all slider and label styles now use the ThemeManager for consistent theming across the application. The container widget applies a theme class of `applet/digi`.

In v26.7.4, all four gauges (Level, Compression, ALC Phone, ALC CW) now display a hover-value popup when you mouse over them, showing the exact reading with one decimal place for precise monitoring (#3936). Also, when host modulation is active, the Mic source combo box is locked to "PC" with a tooltip explaining that only the PC input is available.

In v26.8.4, the Mic source combo box now intelligently adapts to radios whose transmit audio input cannot be selected from this client. On such radios, the combo box is narrowed to a single "PC" entry with a tooltip explaining that the radio's own input selection is made on the radio. This prevents the misleading appearance of selectable microphone inputs that would be silently ignored. The client also automatically applies the PC mic selection state to the transmit model to keep it in sync. Additionally, CW mode detection now correctly recognizes all CW variants (CW, CWU, CWL) from any radio, not just the Flex bare "CW" mode.

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
2. Select the Mic source from the dropdown. On radios where the input is selectable, options include MIC, BAL, LINE, ACC, PC, plus any from the radio's available mic inputs. When host modulation is active, the combo box is locked to "PC" with a tooltip explaining that only the PC input is available. On radios whose transmit audio input cannot be selected from this client (v26.8.4), the combo box is narrowed to a single "PC" entry with a tooltip explaining that the radio's own input selection is made on the radio.
3. Adjust the Mic gain slider to set the microphone input level (0–100). When the source is PC, the value is stored locally in `PcMicGain`.
4. Click +ACC to enable the accessory microphone input mix.
5. Click PROC to toggle the speech processor.
6. Use the NOR/DX/DX+ slider to select the processor level: 0 (NOR), 1 (DX), or 2 (DX+).
7. Click DAX to enable DAX as the TX audio source.

### CW mode: adjust CW settings

1. Switch the active slice to a CW mode (CW, CWU, or CWL). The applet automatically shows the CW panel.
2. Adjust the Delay slider to set the CW break-in delay (0–2000 ms, step 10). You can also type a value directly into the QLineEdit (0–2000).
3. Adjust the Speed slider to set CW keying speed (5–100 WPM). You can also type a value directly into the QLineEdit (5–100).
4. Click Sidetone to enable the CW monitor. The button highlights when active.
5. Adjust the Sidetone volume slider to set the level (0–100). You can also type a value directly into the QLineEdit (0–100).
6. Use the L / R pan (CW) slider to set stereo pan (double-click to recentre to 50).
7. Click Breakin to toggle full break-in (QSK).
8. Click Iambic to toggle iambic paddle keyer.
9. Use the Pitch < / > buttons to step by 10 Hz, or type a value directly into the QLineEdit (100–6000 Hz).

### Reading gauge values with mouse hover

1. Move your mouse cursor over any gauge (Level, Compression, ALC Phone, ALC CW).
2. A popup appears showing the exact numeric value with one decimal place.
3. The Level gauge shows the value in dB (e.g., "-12.3 dB").
4. The Compression gauge shows the compression amount as a positive value in dB (e.g., "15.0 dB" for -15 dB of compression).
5. The ALC gauges show the value in dBFS (e.g., "-5.2 dBFS").

## What each control does

| Control             | What it does                                                                                                                                                                                                                                                                                                     | Default                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| MON                 | Enables the TX sideband monitor (Phone panel).                                                                                                                                                                                                                                                                   | —                                                        |
| Monitor volume      | Sets sideband monitor playback level.                                                                                                                                                                                                                                                                            | —                                                        |
| DAX                 | Enables DAX as the TX audio source.                                                                                                                                                                                                                                                                              | —                                                        |
| Mic profile         | Loads a named microphone processing profile.                                                                                                                                                                                                                                                                     | —                                                        |
| Mic source          | Selects the microphone input source. When host modulation is active, the combo box is locked to "PC" with a tooltip explaining that only the PC input is available (v26.7.4). On radios whose transmit audio input cannot be selected from this client, the combo box is narrowed to a single "PC" entry with a tooltip explaining that the radio's own input selection is made on the radio (v26.8.4). | —                                                        |
| Mic gain            | Adjusts microphone input level. For PC source uses local PcMicGain persistence.                                                                                                                                                                                                                                  | 50                                                       |
| +ACC                | Enables the accessory microphone input mix.                                                                                                                                                                                                                                                                      | —                                                        |
| PROC                | Toggles the speech processor.                                                                                                                                                                                                                                                                                    | —                                                        |
| NOR/DX/DX+          | Three-position processor level slider.                                                                                                                                                                                                                                                                           | 0                                                        |
| Delay (CW)          | Sets CW break-in delay. Adjacent QLineEdit accepts typed values (0–2000) (v0.9.8, #2429). In v0.9.8, setCwDelay was fixed to cache the value immediately so the radio emission doesn't snap the slider back (#2428).                                                                                             | 500 ms                                                   |
| Speed (CW)          | Sets CW keying speed. Adjacent QLineEdit accepts typed values (5–100) (v0.9.8, #2429).                                                                                                                                                                                                                           | 20 WPM                                                   |
| Sidetone            | Toggles CW sidetone monitor. Also enables/disables the client-side low-latency CwSidetoneGenerator in lockstep (v0.9.1+). Both the radio's DAX-fed monitor and the local PortAudio sidetone are controlled by this single button. Pitch and pan always follow the radio's cw_pitch and mon_pan_cw automatically. In v26.5.3, sidetone audio routes to the user-selected audio output (#2899). | —                                                        |
| Sidetone volume     | Sets CW monitor volume. Also sets the local sidetone generator volume in lockstep. Adjacent QLineEdit accepts typed values (0–100) (v0.9.8, #2429).                                                                                                                                                              | 50                                                       |
| L / R pan (CW)      | Sets CW monitor stereo pan. Applies constant-power pan to the local sidetone generator (v0.9.1+). Double-click to recentre to 50.                                                                                                                                                                                | 50                                                       |
| Breakin             | Toggles full break-in (QSK). In v0.9.7, the CW keyboard/MIDI paths now fully honor this setting: with Breakin ON (QSK) key edges trigger TX and break_in_delay holds the relay; with Breakin OFF keys are queued and the operator engages PTT manually.                                                          | —                                                        |
| Iambic              | Toggles iambic paddle keyer.                                                                                                                                                                                                                                                                                     | —                                                        |
| Pitch < / >         | QLineEdit with < / > buttons (CwTriBtn). Type a value (100–6000) or click the buttons to step by 10 Hz (v0.9.8, #2429).                                                                                                                                                                                          | 600 Hz                                                   |
| Level               | Microphone input peak level in dBFS (Phone panel). Suppressed to -150 when met_in_rx is off and not transmitting.                                                                                                                                                                                                | —                                                        |
| Compression         | Speech compression amount in dB (Phone panel). Gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX (v0.9.7). In v26.5.3, compression meter value is inverted: 0 dB = no compression, -25 dB = full compression.                                                   | —                                                        |
| ALC (Phone panel)   | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). In v26.5.3, initializes to -20 dBFS on startup. Mirrored by an identical gauge on the CW sub-panel. In v26.7.4, supports hover-value popup for exact reading (#3936). | —                                                        |
| ALC (CW panel)      | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode. In v26.5.3, initializes to -20 dBFS on startup. In v26.7.4, supports hover-value popup for exact reading (#3936). | —                                                        |

## Meter information

| Meter                | What it shows                                                                                                                               | Valid Range             | Notes                                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Level gauge          | Microphone input peak level in dBFS. Mouse hover shows the exact value with one decimal place (v26.7.4, #3936).                            | -40 to +10 dBFS (red > 0) | Suppressed to -150 when met_in_rx is off and not transmitting.                                                                 |
| Compression gauge    | Speech compression amount in dB (reversed fill). In v26.5.3, 0 dB = no compression, -25 dB = full compression. Mouse hover shows the compression amount as a positive value (v26.7.4, #3936). | -25 to 0 dB             | Gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX (v0.9.7). In v26.5.3, inverted from previous versions. |
| ALC gauge (Phone)    | Automatic level control — post-software-ALC SSB peak, read from MeterModel::swAlcChanged. Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Mouse hover shows the exact value with one decimal place in dBFS (v26.7.4, #3936). | -20 to 0 dBFS (red > -3) | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). In v26.5.3, initializes to -20 dBFS on startup. Mirrored by identical gauge on CW panel. |
| ALC gauge (CW)       | Mirror of the Phone-panel ALC gauge, identically scaled. Both read from MeterModel::swAlcChanged. Mouse hover shows the exact value with one decimal place in dBFS (v26.7.4, #3936). | -20 to 0 dBFS (red > -3) | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode. In v26.5.3, initializes to -20 dBFS on startup. |

## Tips

- The Sidetone button and Sidetone volume slider control both audio paths (radio DAX monitor and client-side generator) together. There is no separate control to enable or adjust the local sidetone independently.
- Pitch always follows the radio's CW pitch setting automatically. Use the Pitch < / > widget to change the radio's CW pitch, and both the decode pitch and sidetone pitch will update accordingly.
- The MON button and the Sidetone button are separate controls on separate panels. MON applies to voice modes; Sidet
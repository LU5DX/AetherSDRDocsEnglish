# Phone/CW applet

The Phone/CW applet is a mode-aware transmit panel. In voice modes (SSB, AM, FM) it shows microphone, processor, and monitor controls. When the active slice is in CW mode, it automatically switches to CW controls (delay, speed, sidetone, iambic, pitch).

## Opening the Phone/CW applet

Click the **P/CW** tray button in the right sidebar.

## Phone panel controls (voice modes)

| Control           | Kind                                                                                                                                                              | Behavior                                                                                                                                                                                            |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level             | Meter                                                                                                                                                             | Shows microphone input peak level in dBFS (-40 to +10 dBFS; red above 0). Suppressed to -150 dBFS when `met_in_rx` is off and not transmitting, except when the mic source is PC or RADE is active. Hover over the gauge to see the exact level in dB with one decimal place (v26.7.4+). |
| Compression       | Meter                                                                                                                                                             | Shows speech compression amount in dB (-25 to 0 dB, reversed fill). Gated on the radio's interlock TRANSMITTING state and speech processor enable: reads 0 dB during RX (v0.9.7+). Hover over the gauge to see the exact compression amount in dB with one decimal place (v26.7.4+). |
| ALC (Phone panel) | Meter                                                                                                                                                             | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Red threshold at -3 dBFS. Initializes to -20 dBFS on startup. Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. Hover over the gauge to see the exact dBFS value with one decimal place (v26.7.4+). |
| Mic profile       | Combo box                                                                                                                                                         | Loads a named microphone processing profile from the radio. Click to select a profile; it loads immediately.                                                                                        |
| Mic source        | Combo box                                                                                                                                                         | Selects the microphone input source: MIC, BAL, LINE, ACC, or PC. Calls `TransmitModel::setMicSelection`. When host modulation is enabled, the combo box shows only "PC" and is disabled (v26.7.4+). |
| Mic gain          | Slider (0-100)                                                                                                                                                    | Adjusts microphone input level. For the "PC" source, uses local `PcMicGain` persistence (the radio always reports mic_level=0 when source=PC).                                                      |
| +ACC              | Toggle                                                                                                                                                            | Enables the accessory microphone input mix. Calls `TransmitModel::setMicAcc`.                                                                                                                       |
| PROC              | Toggle                                                                                                                                                            | Toggles the speech processor. Calls `TransmitModel::setSpeechProcessorEnable`.                                                                                                                      |
| NOR/DX/DX+        | Slider (0=NOR, 1=DX, 2=DX+)                                                                                                                                       | Three-position processor level. Calls `TransmitModel::setSpeechProcessorLevel`.                                                                                                                     |
| DAX               | Toggle                                                                                                                                                            | Enables DAX as the TX audio source. Calls `TransmitModel::setDax`.                                                                                                                                  |
| MON               | Toggle                                                                                                                                                            | Enables TX sidetone monitor. Calls `TransmitModel::setSbMonitor`.                                                                                                                                   |
| Monitor volume    | Slider (0-100)                                                                                                                                                    | Sets sideband monitor volume. Calls `TransmitModel::setMonGainSb`.                                                                                                                                  |

### Level gauge — PC mic source and RADE exceptions

When the mic source is **PC** or **RADE** mode is active, the Level gauge remains active during receive (RX) even when `met_in_rx` is off and the radio is not transmitting. For hardware mic sources (MIC, BAL, LINE, ACC), the gauge is suppressed to -150 dBFS during RX unless `met_in_rx` is on.

### Level gauge — hover readout (v26.7.4+)

Hover your mouse cursor over the Level gauge to see a popup showing the exact microphone peak level in dB with one decimal place (#3936).

### Compression gauge behavior (v0.9.7+)

The Compression gauge only shows a live value while the radio is actually transmitting and the speech processor is enabled. During receive it reads 0 dB. This prevents confusing stale readings from the TX chain.

### Compression gauge — hover readout (v26.7.4+)

Hover your mouse cursor over the Compression gauge to see a popup showing the exact compression amount in dB with one decimal place (#3936).

### ALC gauge (Phone panel)

The ALC gauge shows the post-software-ALC SSB peak in dBFS, read from `MeterModel::swAlcChanged`. It fills from right to left: empty at -20 dBFS, full at 0 dBFS. The red threshold is at -3 dBFS. The gauge initializes to -20 dBFS on startup. This gauge mirrors the one on the CW panel — both read from the same source for consistent readings across voice and CW modes.

### ALC gauge — hover readout (v26.7.4+)

Hover your mouse cursor over the ALC gauge to see a popup showing the exact dBFS value with one decimal place (#3936).

### RADE mode behavior (v0.9.7+)

When RADE mode is active:
- The **Mic gain** slider acts as a client-side RADE gain control using the `PcMicGain` setting. Slider changes are not sent to the radio as `mic_level` commands.
- The **Level** gauge remains active during RX.
- When RADE deactivates, the slider reverts to showing the radio's `mic_level` value and the Level gauge resets to -150 dBFS.

### Host modulation behavior (v26.7.4+)

When the radio is modulated by AetherSDR (host modulation enabled):
- The **Mic source** combo box is disabled and shows only "PC" — no other source choices are available.
- A tooltip on the combo box explains that the PC microphone is the only input because the other sources are FlexRadio radio jacks.
- This is managed automatically; no user action is required.

## CW panel controls

| Control | Kind | Behavior |
|---------|------|----------|
| ALC (CW panel) | Meter | Mirrors the Phone-panel ALC gauge. Shows post-software-ALC SSB peak in dBFS (-20 to 0 dBFS; red above -3). Fills right-to-left. Initializes to -20 dBFS on startup. Added in v26.5.1 (#2552) as part of the SW ALC meter split. Hover over the gauge to see the exact dBFS value with one decimal place (v26.7.4+). |
| Delay (CW) | Slider (0-2000 ms, step 10) + QLineEdit | Sets CW break-in delay. Drag the slider or click the value and type a number directly (0-2000). Calls `TransmitModel::setCwDelay`. Default: 500. In v0.9.8, value caching was fixed to prevent the slider from snapping back when the radio emits (#2428). |
| Speed (CW) | Slider (5-100 WPM) + QLineEdit | Sets CW keying speed. Drag the slider or click the value and type a number directly (5-100). Calls `TransmitModel::setCwSpeed`. Default: 20. |
| Sidetone | Toggle | Toggles CW sidetone monitor. Controls both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (CwSidetoneGenerator, ~10 ms latency) in lockstep. Calls `TransmitModel::setCwSidetone`. In v26.5.3, the CW sidetone routes to the user-selected audio output instead of the default output (#2899). |
| Sidetone volume | Slider (0-100) + QLineEdit | Sets CW monitor volume for both the radio (mon_gain_cw) and the local sidetone generator. Drag the slider or click the value and type a number directly (0-100). Default: 50. |
| L / R pan (CW) | Slider (0-100) | Sets CW monitor stereo pan. Applies constant-power pan to both the radio side and the local sidetone generator. Double-click recenters to 50 (centre). Default: 50. |
| Breakin | Toggle | Toggles full break-in (QSK). Calls `TransmitModel::setCwBreakIn`. Fully honors the radio's break_in setting (v0.9.7+): with Breakin ON (QSK) key edges trigger TX immediately; with Breakin OFF keys are queued and the operator engages PTT manually. |
| Iambic | Toggle | Toggles iambic paddle keyer. Calls `TransmitModel::setCwIambic`. |
| Pitch < / > | QLineEdit with < / > buttons | Sets CW sidetone pitch. Type a value (100-6000 Hz) or click the buttons to step by 10 Hz. Calls `TransmitModel::setCwPitch`. Default: 600. |

### ALC gauge (CW panel)

The ALC gauge on the CW panel is identical to the one on the Phone panel. It shows the post-software-ALC SSB peak in dBFS (-20 to 0 dBFS), filling from right to left with red threshold at -3 dBFS. The gauge initializes to -20 dBFS on startup. Both gauges read from the same `MeterModel::swAlcChanged` source so operators see the same ALC indication regardless of which panel is active for the current mode.

### ALC gauge — hover readout (v26.7.4+)

Hover your mouse cursor over the ALC gauge to see a popup showing the exact dBFS value with one decimal place (#3936).

### Direct value entry (v0.9.8)

In v0.9.8, the four CW value labels were replaced with QLineEdit widgets that accept typed numeric input:

- **Delay (CW):** accepts 0-2000 (milliseconds)
- **Speed (CW):** accepts 5-100 (WPM)
- **Sidetone volume:** accepts 0-100
- **Pitch < / >:** accepts 100-6000 (Hz)

Click any value, type a number, and press Enter. The corresponding slider updates immediately. The slider continues to work as before; the edit field updates from the slider except while you are editing it.

### Sidetone behavior (v0.9.1+)

The single **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (CwSidetoneGenerator, ~10 ms latency) in lockstep. There are no separate local-sidtone controls.

Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically; no manual override is needed or available.

### Sidetone routing (v26.5.3)

In v26.5.3, the CW sidetone now routes to the user-selected audio output instead of the default audio output (#2899). Configure the audio output in **File > Settings > Audio** to choose where sidetone plays.

### Sidetone bus sharing with Quindar tones (v0.9.7+)

The sidetone audio bus is shared with Quindar tones. The two are mutually exclusive at the mode level: Quindar tones are active only outside CW mode, and the CW sidetone generator is active only in CW mode. The applet manages the switch automatically when the active slice mode changes.

### Breakin behavior (v0.9.7+)

- **Breakin ON (QSK):** key edges trigger TX immediately; the break-in delay set by the **Delay (CW)** slider holds the relay after the last element.
- **Breakin OFF:** keyed characters are queued; the operator engages PTT manually to transmit.

## Mic profile management

To select a mic profile:

1. Open the Phone/CW applet.
2. Confirm the active slice is in a voice mode (SSB, AM, FM). In CW mode the mic profile controls are not visible.
3. Click the **Mic profile** combo box. The list shows profiles stored on the radio.
4. Select the profile name for your microphone. The profile loads immediately.

The available profile names come from the radio. To create or rename profiles, use the radio's own profile management or open `Profiles > Profile Manager...` in AetherSDR. Selecting a profile does not change the **Mic source** or **Mic gain** settings; adjust those separately if needed.

## Changes in v0.9.3

### Level gauge — PC mic source exception

When the mic source is PC, the Level gauge appears immediately on connect even when `met_in_rx` is off. Hardware mic sources continue to be suppressed during RX.

### VOX toggle refresh

Toggling VOX via a keyboard shortcut now refreshes the Phone panel immediately (#2084).

### Sidetone stream on Windows

On Windows, the client-side sidetone stream starts correctly as soon as AetherSDR connects to the radio (#2105).

## Changes in v0.9.7

### Compression gauge gated on transmit state

The Compression gauge only shows a live value while the radio is transmitting and the speech processor is enabled. During receive it reads 
# Use keyboard or MIDI to trigger straight key or iambic paddles

This page explains how to send CW using a computer keyboard or MIDI controller as a straight key or iambic paddles through the Phone/CW applet. This lets you key the radio without physical paddle hardware connected to the FLEX-8600.

## Before you start

- The active slice must be in a CW mode. The Phone/CW applet switches to its CW sub-panel automatically when CW mode is selected.
- The Phone/CW applet must be visible. If it is not, click the **P/CW** tray button in the right sidebar, or go to `View > Applet Panel` to show the sidebar.
- For MIDI input, your MIDI controller must be connected before launching AetherSDR. Open `Settings > MIDI Mapping...` to assign controller inputs to key functions.

## Steps

1. Select a CW mode on the active slice. The Phone/CW applet switches to the CW sub-panel. (CW, CWU, and CWL modes all drive this applet.)
2. Decide whether you want straight key or iambic paddle operation. For iambic, click **Iambic** so it is active (highlighted). For straight key, leave **Iambic** inactive.
3. Set your keying speed with the **Speed (CW)** slider (5–100 WPM). You can also type a value directly into the adjacent text field.
4. Choose how TX is triggered:
   - For full break-in (QSK), click **Breakin** so it is active. Key edges from the keyboard or MIDI controller will trigger TX immediately; the radio's break-in delay holds the relay between characters.
   - For manual PTT, leave **Breakin** inactive. Key input will be queued; engage PTT separately to transmit. See [Configure break-in OFF so CW keys queue and PTT is manual](configure-break-in-off-so-cw-keys-queue-and-ptt-is-manual.md).
5. If you want sidetone while keying, click **Sidetone** to enable it. Adjust the **Sidetone volume** slider to a comfortable level. The client-side low-latency sidetone (approximately 10 ms latency) and the radio's DAX-fed monitor are both controlled by this single button and slider. You can also type a volume value directly into the adjacent text field. In v26.5.3, the CW sidetone routes to the user-selected audio output instead of the default output (#2899).
6. Set the **Delay (CW)** for break-in hang time (0–2000 ms). You can use the slider or type a value directly into the adjacent text field.
7. Set the **Pitch < / >** to your preferred sidetone frequency (100–6000 Hz). Type a value directly into the text field or click the **<** and **>** buttons to step by 10 Hz.
8. Begin keying from the keyboard or MIDI controller. With **Iambic** active, the dit and dah inputs are treated as paddle contacts. With **Iambic** inactive, any key input acts as a straight key closure.

## What each control does

| Control               | What it does                                                                                                                                                                                                  | Default                                                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Iambic**            | Toggles iambic paddle keyer. When active, keyboard/MIDI inputs are treated as dit and dah paddle contacts. When inactive, input acts as a straight key.                                                       | —                                                                                                                        |
| **Breakin**           | Toggles full break-in (QSK). When active, key edges trigger TX and break-in delay holds the relay. When inactive, keys queue and PTT must be engaged manually.                                                | —                                                                                                                        |
| **Speed (CW)**        | Sets the keying speed applied to keyboard and MIDI input. Type a value (5–100) directly in the text field or use the slider.                                                                                  | 20 WPM                                                                                                                   |
| **Delay (CW)**        | Sets the CW break-in hang time after the last key edge before TX drops. Type a value (0–2000 ms) directly in the text field or use the slider.                                                                | 500 ms                                                                                                                   |
| **Sidetone**          | Enables the CW sidetone monitor. Controls both the radio's DAX-fed monitor and the client-side low-latency sidetone generator in lockstep.                                                                    | —                                                                                                                        |
| **Sidetone volume**   | Sets CW monitor volume. Controls both radio-side and client-side sidetone volumes in lockstep. Type a value (0–100) directly in the text field or use the slider.                                             | 50                                                                                                                       |
| **Pitch < / >**       | Sets the sidetone and decode pitch. Type a value (100–6000 Hz) directly in the text field, or click the **<** and **>** buttons to step by 10 Hz. Pitch follows the radio's `cw_pitch` setting automatically. | 600 Hz                                                                                                                   |
| **L / R pan (CW)**    | Sets CW monitor stereo pan. Double-click recenters to 50 (centre).                                                                                                                                           | 50 (centre)                                                                                                              |
| **Mic source**        | Selects microphone input source from available options (MIC, BAL, LINE, ACC, PC). When the radio is modulated by AetherSDR (host modulation mode), this combo box is disabled and locked to "PC" only, and a tooltip explains that the radio's own input selection is made on the radio. | —                                                                                                                        |
| **Mic gain**          | Adjusts microphone input level (0–100). For the 'PC' source, the value is stored client-side as `PcMicGain`.                                                                                                 | 50                                                                                                                       |
| **+ACC**              | Enables the accessory microphone input mix.                                                                                                                                                                   | —                                                                                                                        |
| **PROC**              | Toggles the speech processor.                                                                                                                                                                                 | —                                                                                                                        |
| **NOR/DX/DX+**        | Three-position processor level slider: NOR (0), DX (1), DX+ (2).                                                                                                                                              | 0 (NOR)                                                                                                                  |
| **DAX**               | Enables DAX as the TX audio source. Hidden (and forced off) on radios whose input this client cannot choose.                                                                                                 | —                                                                                                                        |
| **MON**               | Enables TX sidetone monitor.                                                                                                                                                                                  | —                                                                                                                        |
| **Monitor volume**    | Sets sideband monitor volume (0–100).                                                                                                                                                                         | —                                                                                                                        |
| **Mic profile**       | Loads a named microphone processing profile from the radio.                                                                                                                                                   | —                                                                                                                        |
| **Level gauge**       | Microphone input peak level in dBFS (-40 to +10 dBFS, red above 0 dBFS). Hover to see the exact dBFS value with one decimal place. Hidden on radios whose input this client cannot choose.                      | —                                                                                                                        |
| **Compression gauge** | Speech compression amount in dB (-25 to 0 dB, reversed fill). Hover to see the compression amount as a positive value with one decimal place.                                                                | —                                                                                                                        |
| **ALC (Phone panel)** | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Hover to see the exact dBFS value with one decimal place. | Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| **ALC (CW panel)**    | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Hover to see the exact dBFS value with one decimal place.                            | Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode.                          |

## Tips

- In v0.9.8, the **Delay (CW)**, **Speed (CW)**, **Sidetone volume**, and **Pitch** value labels are now editable text fields. Click any value and type a number directly — this matches SmartSDR behavior.
- Sidetone pitch and stereo pan follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically; you do not need to reconfigure them after changing the radio's CW pitch.
- With **Breakin** OFF, key input from the keyboard or MIDI controller is queued. This is useful when you want to compose characters before transmitting. Engage PTT manually to send the queued input.
- Double-clicking the **L / R pan (CW)** slider recenters it to 50 (centre).
- In v26.5.3, the mic level meter is suppressed during receive when the user disables the level meter during receive (via `met_in_rx`). The Compression gauge displays 0 dB during RX to prevent confusing stale readings from the TX chain.
- In v26.6.1, the Phone/CW applet and its controls have been updated to use the application theme system (`ThemeManager`) for styling. All sliders, labels, and buttons now inherit their colors from the active theme instead of hardcoded values. If you have created custom themes, verify that slider and button colors are defined appropriately.
- In v26.7.4, hovering over the **Level**, **Compression**, and **ALC** gauges (both Phone and CW panels) displays a popup showing the exact value with one decimal place. This allows you to read precise dBFS or dB levels without estimating against the scale markings (#3936).
- In v26.8.4, when the radio is in host modulation mode (modulated by AetherSDR), the **Mic source** combo box is locked to "PC" as the only available option and disabled. The tooltip explains that this radio takes transmit audio from this computer and its own input selection is made on the radio. The **Level gauge** is hidden and the **DAX** button is suppressed (and forced off) on such radios, because the client cannot choose their input path.
- In v26.8.4, the applet now treats CW, CWU, and CWL modes uniformly as CW mode; previously only "CW" was recognized, which meant the applet would not switch to the CW sub-panel on radios that report CWU or CWL.

## Troubleshooting

- **MIDI controller is not recognized** — Ensure the controller was connected before launching AetherSDR. Open `Settings > MIDI Mapping...` to verify the device is listed and inputs are mapped.
- **Keying does not trigger TX** — Check that **Breakin** is active if you expect QSK operation. If **Breakin** is inactive, the radio expects a manual PTT to transmit queued keys.
- **No sidetone heard while keying** — Confirm **Sidetone** is active and **Sidetone volume** is above zero. Also verify the active slice is in CW mode; the CW sub-panel only appears in CW mode. In v26.5.3, verify the user-selected audio output is properly configured in `Settings > Audio Output`.
- **CW sub-panel does not appear in CWU or CWL mode** — Upgrade to v26.8.4 or later; earlier versions only recognized the "CW" mode name.
- **Iambic paddles send straight key behavior** — Confirm **Iambic** is active (highlighted) in the CW sub-panel.
- **Slider or label colors look incorrect after updating** — This may indicate an incomplete or incompatible theme. Go to `Settings > Theme` and select a built-in theme to reset, or update your custom theme definition with the appropriate color keys for sliders and buttons.
- **Mic source combo box is disabled and shows only "PC"** — This is expected when the radio is in host modulation mode. The radio is being modulated by AetherSDR, so only the PC microphone input is available. The tooltip explains that this radio takes transmit audio from this computer.
- **Level gauge and DAX button are missing** — This is expected on radios whose input this client cannot choose (host modulation mode). The level gauge is hidden and the DAX button is suppressed because the client cannot select the radio's input path.

## Related

- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Configure break-in OFF so CW keys queue and PTT is manual](configure-break-in-off-so-cw-keys-queue-and-ptt-is-manual.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)](enable-the-low-latency-cw-sidetone-sidetone-button-drives-both-radio-and-local-path.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
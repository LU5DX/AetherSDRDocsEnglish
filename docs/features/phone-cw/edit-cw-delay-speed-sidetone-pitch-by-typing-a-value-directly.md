# Edit CW Delay / Speed / Sidetone / Pitch by typing a value directly

Type a precise number directly into any of the four CW value fields (Delay, Speed, Sidetone Volume, Pitch) instead of dragging a slider or clicking step buttons. This matches native SmartSDR behavior and is useful when you already know the exact value you want.

## Before you start

- Ensure the active slice is in CW mode (the Phone/CW applet auto-switches to CW controls).

## Steps

1. Click the **P/CW** tray button on the right sidebar if the Phone/CW applet isn't visible.
2. Locate the CW control you want to edit: **Delay**, **Speed**, **Sidetone volume**, or **Pitch**. Each is next to its corresponding slider.
3. Click inside the number field (a QLineEdit). The field will show a text cursor.
4. Type the desired value using your keyboard.
5. Press **Enter** or click elsewhere to apply the value.

## What each control does

| Control             | Default | Valid range                                                                                                              |
|---------------------|---------|--------------------------------------------------------------------------------------------------------------------------|
| **Delay**           | 500     | 0–2000 ms (step 10)                                                                                                      |
| **Speed**           | 20      | 5–100 WPM                                                                                                                |
| **Sidetone volume** | 50      | 0–100                                                                                                                    |
| **Pitch**           | 600     | 100–6000 Hz (step 10)                                                                                                    |
| **ALC (Phone panel)** | —      | Shows automatic level control reading from MeterModel::swAlcChanged (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). Mirrored by an identical gauge on the CW sub-panel. |
| **ALC (CW panel)**    | —      | Mirrors the Phone-panel ALC gauge; both read from MeterModel::swAlcChanged for consistent readings across voice and CW. Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses HGauge::setFillFromRight mode. |

## Phone/CW Applet Overview

The Phone/CW applet is a mode-aware transmit panel. It shows Phone controls (mic, processor, monitor) in voice modes and automatically switches to CW controls (delay, speed, sidetone, iambic, pitch) when the active slice is in CW mode. ALC gauges appear on both the Phone and CW sub-panels, both driven by the software ALC meter (MeterModel::swAlcChanged, post-SSBMeter-peak dBFS, #2552), replacing the previous HWALC (RCA voltage) path that produced meaningless readings.

The Compression gauge is gated on the radio's interlock TRANSMITTING state (reads 0 during RX). Breakin fully honors the radio's break_in setting — no auto-PTT envelope forces TX. The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).

## ALC Gauges (v26.5.1)

Both the Phone panel and CW panel contain an ALC gauge. These gauges are identical mirrors reading from the same MeterModel::swAlcChanged source. This ensures that SSB operators watching mic gain see the same indicator CW operators use to verify clean keying envelope shape.

- **Range**: -20 dBFS (empty) to 0 dBFS (full)
- **Red zone**: > -3 dBFS
- **Fill direction**: Right-to-left (empty at -20, fills leftward toward 0)
- **Scale markings**: -20, -15, -10, -5, 0 dBFS

## Phone Panel Controls

| Control           | Type         | Default | Valid range                  | Behavior                                                                 |
|-------------------|--------------|---------|------------------------------|--------------------------------------------------------------------------|
| **Level**         | Meter        | —       | -40 to +10 dBFS (red > 0)    | Shows microphone input peak level in dBFS. Suppressed to -150 when met_in_rx is off and not transmitting. |
| **Compression**   | Meter        | —       | -25 to 0 dB (reversed fill)  | Shows speech compression amount in dB. Gated on radio interlock TRANSMITTING state and speech processor enable. |
| **ALC**           | Meter        | —       | -20 to 0 dBFS (red > -3)     | Shows automatic level control from MeterModel::swAlcChanged. Fills right-to-left. |
| **Mic profile**   | Combo box    | —       | Populated from radio          | Loads the named mic processing profile.                                   |
| **Mic source**    | Combo box    | —       | MIC, BAL, LINE, ACC, PC      | Selects microphone input source.                                         |
| **Mic gain**      | Slider       | 50      | 0-100                        | Adjusts mic input level. For PC source uses local PcMicGain persistence. |
| **+ACC**          | Toggle button| —       | —                            | Enables the accessory mic input mix.                                     |
| **PROC**          | Toggle button| —       | —                            | Toggles the speech processor.                                            |
| **NOR/DX/DX+**    | Slider       | 0       | 0 (NOR), 1 (DX), 2 (DX+)    | Three-position processor level.                                          |
| **DAX**           | Toggle button| —       | —                            | Enables DAX as the TX audio source.                                      |
| **MON**           | Toggle button| —       | —                            | Enables TX sidetone monitor.                                             |
| **Monitor volume**| Slider       | —       | 0-100                        | Sets sideband monitor volume.                                            |

## CW Panel Controls

| Control              | Type         | Default | Valid range               | Behavior                                                                    |
|----------------------|--------------|---------|---------------------------|-----------------------------------------------------------------------------|
| **ALC**              | Meter        | —       | -20 to 0 dBFS (red > -3)  | Mirrors Phone-panel ALC gauge. Fills right-to-left.                        |
| **Delay**            | Slider + edit| 500     | 0-2000 ms (step 10)       | Sets CW break-in delay. Type values 0-2000 directly.                       |
| **Speed**            | Slider + edit| 20      | 5-100 WPM                 | Sets CW keying speed. Type values 5-100 directly.                          |
| **Sidetone**         | Toggle button| —       | —                         | Toggles CW sidetone monitor. Controls both radio DAX-fed monitor and local low-latency CwSidetoneGenerator in lockstep. |
| **Sidetone volume**  | Slider + edit| 50      | 0-100                     | Sets CW monitor volume. Controls both radio-side and local sidetone volumes. Type values 0-100 directly. |
| **L / R pan (CW)**   | Slider       | 50      | 0-100                     | Sets CW monitor stereo pan. Double-click recenters to 50 (centre).        |
| **Breakin**          | Toggle button| —       | —                         | Toggles full break-in (QSK). CW keyboard/MIDI paths fully honor this setting. |
| **Iambic**           | Toggle button| —       | —                         | Toggles iambic paddle keyer.                                                |
| **Pitch < / >**      | Edit + buttons| 600    | 100-6000 Hz (step 10)     | QLineEdit with < / > buttons. Type values 100-6000 or click buttons to step by 10 Hz. |

## Troubleshooting

- **Typed value snaps back to previous value** — The radio may have rejected the value. Ensure your entry is within the valid range shown above. For Delay values, the radio emission no longer snaps the slider back in v0.9.8 (#2428).

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)](enable-the-low-latency-cw-sidetone-sidetone-button-drives-both-radio-and-local-path.md)
# Phone/CW Applet

## Overview

The Phone/CW applet is a mode-aware transmit panel. It shows Phone controls (mic, processor, monitor) in voice modes and automatically switches to CW controls (delay, speed, sidetone, iambic, pitch) when the active slice is in CW mode. ALC gauges appear on both the Phone and CW sub-panels, both driven by the software ALC meter (MeterModel::swAlcChanged, post-SSBMeter-peak dBFS, #2552), replacing the previous HWALC (RCA voltage) path that produced meaningless readings.

The Compression gauge is gated on the radio's interlock TRANSMITTING state (reads 0 during RX). Breakin fully honors the radio's break_in setting — no auto-PTT envelope forces TX. The sidetone bus is shared with Quindar tones (mutually exclusive at the mode level).

In v26.5.3 the CW sidetone now routes to the user-selected audio output instead of the default output (#2899).

In v26.6.1 the applet now properly inherits the active theme's color palette. Sliders use the primary slider style (`applyPrimarySliderStyle`) instead of hardcoded color values, and label colors follow the theme's secondary text color (`{{color.text.secondary}}`). The panel container is styled using `theme::setContainer` for consistent appearance across all themes.

In v26.7.4, all four gauges (Level, Compression, and both ALC meters) show an exact numeric readout when you hover the mouse over them, showing values to one decimal place. When the radio is modulated by AetherSDR (host modulation), the Mic source combo box is locked to "PC" and shows a tooltip explaining that only the PC input is available.

In v26.8.4, the applet detects the radio's transmit-audio capability and adapts the Mic source combo box accordingly. When the radio's transmit audio comes from this computer's network port (rather than its own microphone jacks), the Mic source combo box is narrowed to "PC" only, is disabled, and a tooltip explains that the radio's own input selection is made on the radio. The Mic level gauge is hidden on such radios because no usable input level is available. The DAX button is hidden when the radio has no DAX capability. CW mode detection now recognizes CWL and CWU variants (for Icom and HL2 radios), not just bare "CW" as on Flex radios.

## Opening the Phone/CW Applet

1. Click the **Phone/CW** tray button on the right sidebar.

The applet automatically shows Phone controls when the active slice is in a voice mode (LSB, USB, AM, FM, etc.) and CW controls when the active slice is in CW, CWL, or CWU mode.

## Phone Panel Controls

| Control           | Type         | Default | Valid range                  | Behavior                                                                 |
|-------------------|--------------|---------|------------------------------|--------------------------------------------------------------------------|
| **Level**         | Meter        | —       | -40 to +10 dBFS (red > 0)    | Shows microphone input peak level in dBFS. Hover to see exact value in dB with one decimal. Suppressed to -150 when met_in_rx is off and not transmitting (v26.5.3 applies suppression immediately on state changes). Hidden when the radio's transmit audio comes from this computer (no usable input level). |
| **Compression**   | Meter        | —       | 0 to -25 dB (reversed fill)  | Shows speech compression amount in dB. Hover to see exact value as a positive "amount of compression" in dB with one decimal. Gated on radio interlock TRANSMITTING state and speech processor enable. v26.5.3: MeterModel COMPPEAK (positive 0–25 dB) converted to negative gauge display. |
| **ALC**           | Meter        | —       | -20 to 0 dBFS (red > -3)     | Shows automatic level control from MeterModel::swAlcChanged. Fills right-to-left. Hover to see exact value in dBFS with one decimal. Initialized to -20 dBFS in v26.5.3. |
| **Mic profile**   | Combo box    | —       | Populated from radio          | Loads the named mic processing profile.                                   |
| **Mic source**    | Combo box    | —       | MIC, BAL, LINE, ACC, PC      | Selects microphone input source. Disabled and narrowed to "PC" when host modulation is active or when the radio's input cannot be chosen by this client. Tooltip explains why on such radios. |
| **Mic gain**      | Slider       | 50      | 0-100                        | Adjusts mic input level. For PC source uses local PcMicGain persistence. |
| **+ACC**          | Toggle button| —       | —                            | Enables the accessory mic input mix.                                     |
| **PROC**          | Toggle button| —       | —                            | Toggles the speech processor.                                            |
| **NOR/DX/DX+**    | Slider       | 0       | 0 (NOR), 1 (DX), 2 (DX+)    | Three-position processor level.                                          |
| **DAX**           | Toggle button| —       | —                            | Enables DAX as the TX audio source. Hidden when the radio has no DAX capability. |
| **MON**           | Toggle button| —       | —                            | Enables TX sidetone monitor.                                             |
| **Monitor volume**| Slider       | —       | 0-100                        | Sets sideband monitor volume.                                            |

## CW Panel Controls

| Control              | Type         | Default | Valid range               | Behavior                                                                    |
|----------------------|--------------|---------|---------------------------|-----------------------------------------------------------------------------|
| **ALC**              | Meter        | —       | -20 to 0 dBFS (red > -3)  | Mirrors Phone-panel ALC gauge. Fills right-to-left. Hover to see exact value in dBFS with one decimal. Initialized to -20 dBFS in v26.5.3. |
| **Delay**            | Slider + edit| 500     | 0-2000 ms (step 10)       | Sets CW break-in delay. Type values 0-2000 directly.                       |
| **Speed**            | Slider + edit| 20      | 5-100 WPM                 | Sets CW keying speed. Type values 5-100 directly.                          |
| **Sidetone**         | Toggle button| —       | —                         | Toggles CW sidetone monitor. Controls both radio DAX-fed monitor and local low-latency CwSidetoneGenerator in lockstep. Pitch and pan always follow the radio's cw_pitch and mon_pan_cw automatically. v26.5.3: routes to user-selected audio output instead of default. |
| **Sidetone volume**  | Slider + edit| 50      | 0-100                     | Sets CW monitor volume. Controls both radio-side and local sidetone volumes. Type values 0-100 directly. |
| **L / R pan (CW)**   | Slider       | 50      | 0-100                     | Sets CW monitor stereo pan. Double-click recenters to 50 (centre).        |
| **Breakin**          | Toggle button| —       | —                         | Toggles full break-in (QSK). CW keyboard/MIDI paths fully honor this setting. |
| **Iambic**           | Toggle button| —       | —                         | Toggles iambic paddle keyer.                                                |
| **Pitch < / >**      | Edit + buttons| 600    | 100-6000 Hz (step 10)     | QLineEdit with < / > buttons. Type values 100-6000 or click buttons to step by 10 Hz. |

## Editing CW Values by Typing

You can type a precise number directly into any of the four CW value fields (Delay, Speed, Sidetone Volume, Pitch) instead of dragging a slider or clicking step buttons. This matches native SmartSDR behavior.

### Steps

1. Open the Phone/CW applet with the active slice in CW mode.
2. Locate the CW control you want to edit: **Delay**, **Speed**, **Sidetone volume**, or **Pitch**. Each is next to its corresponding slider.
3. Click inside the number field (a QLineEdit). The field will show a text cursor.
4. Type the desired value using your keyboard.
5. Press **Enter** or click elsewhere to apply the value.

### Value ranges for direct entry

| Control             | Default | Valid range                                      |
|---------------------|---------|--------------------------------------------------|
| **Delay**           | 500     | 0-2000 ms (step 10)                              |
| **Speed**           | 20      | 5-100 WPM                                        |
| **Sidetone volume** | 50      | 0-100                                            |
| **Pitch**           | 600     | 100-6000 Hz (step 10)                            |

## ALC Gauges (v26.5.1)

Both the Phone panel and CW panel contain an ALC gauge. These gauges are identical mirrors reading from the same `MeterModel::swAlcChanged` source. This ensures that SSB operators watching mic gain see the same indicator CW operators use to verify clean keying envelope shape.

- **Range**: -20 dBFS (empty) to 0 dBFS (full)
- **Red zone**: > -3 dBFS
- **Fill direction**: Right-to-left (empty at -20, fills leftward toward 0)
- **Scale markings**: -20, -15, -10, -5, 0 dBFS
- **Initial state**: Both gauges start at -20 dBFS on applet construction (v26.5.3).
- **Hover readout**: Hover over either ALC gauge to see the exact dBFS value with one decimal (v26.7.4).

## Gauge Hover Readouts (v26.7.4)

All four gauges (Level, Compression, and both ALC meters) show an exact numeric readout when you hover your mouse cursor over them. This lets you read the precise metering value without having to eyeball it against the scale.

| Gauge               | Hover format                                      |
|---------------------|---------------------------------------------------|
| **Level**           | Shows value as dB with one decimal (e.g., "-12.3 dB") |
| **Compression**     | Shows value as positive dB with one decimal (e.g., "8.5 dB") |
| **ALC (both panels)**| Shows value as dBFS with one decimal (e.g., "-5.7 dBFS") |

## Mic Source Locking for Host Modulation (v26.7.4)

When the radio is modulated by AetherSDR (host modulation active), the **Mic source** combo box is automatically set to "PC" and becomes disabled. The tooltip explains:

> This radio is modulated by AetherSDR, so the PC microphone is the only input. The other sources are FlexRadio jacks.

This prevents selecting microphone jacks that do not exist on a host-modulated radio.

## Mic Source Limiting by Radio Capability (v26.8.4)

When the radio's transmit audio comes from this computer (its own input selection is made on the radio, not by this client), the **Mic source** combo box is narrowed to a single entry, "PC", and becomes disabled. The tooltip explains:

> This radio takes transmit audio from this computer. Its own input selection is made on the radio.

Setting the model state to "PC" in this situation keeps radiocert and other model readers in sync with what the UI shows.

## DAX Button Visibility (v26.8.4)

The **DAX** toggle button is hidden when the connected radio has no DAX capability. When hidden, DAX is also forced off client-side so no stale state persists.

## Troubleshooting

- **Typed value snaps back to previous value** — The radio may have rejected the value. Ensure your entry is within the valid range shown above. For Delay values, the radio emission no longer snaps the slider back in v0.9.8 (#2428).
- **Level meter stays at -150 after stopping transmit** — In v26.5.3 the level meter is suppressed whenever receiving with met_in_rx off. Check **Settings > Appearance > Disable level meter during receive** if you see unexpected -150 readings in RX.
- **Level meter does not appear at all** — In v26.8.4 the Level meter is hidden on radios whose transmit audio comes from this computer, because no usable input level exists. Verify the radio model and its audio input configuration.
- **Compression gauge shows unexpected values** — v26.5.3 changed the COMPPEAK interpretation to positive 0–25 dB; the gauge face reverses to -25–0 dB. If you see reversed scaling, verify you are running v26.5.3 or later.
- **Colors don't match the active theme** — v26.6.1 fixed theme inheritance for all UI elements in this applet. If colors appear hardcoded (e.g., blue on black regardless of theme), verify you are running v26.6.1 or later.
- **Gauge hover readout not appearing** — Hover readouts were added in v26.7.4. If you do not see them, verify you are running v26.7.4 or later.
- **Mic source combo box is stuck on "PC"** — Host modulation may be active, or the radio's input cannot be chosen by this client. Hover over the combo box to see the tooltip explaining why
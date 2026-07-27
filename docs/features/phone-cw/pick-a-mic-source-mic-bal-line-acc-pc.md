# Phone/CW (P/CW) Applet

The Phone/CW applet provides mode-aware transmit controls. When the active slice is in a phone mode (USB, LSB, AM, FM), the applet shows microphone and processor controls. When the active slice is in CW or CWL mode, it automatically switches to CW controls (delay, speed, sidetone, iambic, pitch).

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a phone mode or CW mode for the respective controls to appear.

## Opening the applet

1. Click the **P/CW** tray button in the right sidebar.

## Phone sub-panel

The Phone sub-panel contains microphone input selection, gain, processing, and monitoring controls.

### Mic source

Select which physical or virtual input the radio uses as the microphone source for voice transmissions. The choice determines where the FLEX-8600 takes its TX audio from.

1. Locate the **Mic source** drop-down box in the Phone sub-panel.
2. Click **Mic source** and select one of the available sources: `MIC`, `BAL`, `LINE`, `ACC`, or `PC`.

The selection takes effect immediately on the radio.

**Source descriptions:**

- **MIC** — Front-panel microphone connector.
- **BAL** — Balanced microphone input.
- **LINE** — Line-level input.
- **ACC** — Accessory port microphone input.
- **PC** — Computer audio system. The radio does not report mic level for this source; AetherSDR stores the gain value locally in `PcMicGain`.

When the radio is being modulated by AetherSDR (host modulation active), the **Mic source** drop-down is forced to `PC` only and disabled. A tooltip explains: "This radio is modulated by AetherSDR, so the PC microphone is the only input. The other sources are FlexRadio jacks."

### Phone controls

| Control            | Description                                                                                                                                                                                     | Default |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **Mic source**     | Selects the microphone input source sent to the radio.                                                                                                                                          | —       |
| **Mic gain**       | Adjusts the microphone input level. When the source is `PC`, the value is stored client-side in `PcMicGain` because the radio does not manage gain in that path.                                | 50      |
| **+ACC**           | Enables the accessory microphone input mix alongside the primary source.                                                                                                                        | —       |
| **PROC**           | Toggles the speech processor on or off.                                                                                                                                                         | —       |
| **NOR/DX/DX+**     | Three-position processor level: 0 (NOR), 1 (DX), 2 (DX+).                                                                                                                                      | 0       |
| **DAX**            | Enables DAX as the TX audio source.                                                                                                                                                             | —       |
| **MON**            | Enables TX sidetone monitor for phone modes.                                                                                                                                                    | —       |
| **Monitor volume** | Sets sideband monitor volume.                                                                                                                                                                   | —       |

### Metering gauges (Phone panel)

#### Level gauge

Shows microphone input peak level in dBFS from -40 to +10 dBFS. Values above 0 dBFS appear red, indicating clipping.

- Suppressed to -150 dBFS when the radio is receiving and `met_in_rx` is off.
- Hover the cursor over the gauge to see the exact peak level in dB with one decimal place.

#### Compression gauge

Shows speech compression amount in dB from -25 to 0 dB, with reversed fill. The gauge reads 0 dB during receive — it is gated on the radio's interlock TRANSMITTING state and the speech processor enable.

- Hover the cursor over the gauge to see the exact compression amount in dB with one decimal place. The value is displayed as a positive number (e.g., "12.5 dB" for 12.5 dB of compression).

#### ALC gauge (Phone panel)

Shows automatic level control reading from the software ALC meter (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. The red zone (> -3 dBFS) indicates excessive ALC.

- Hover the cursor over the gauge to see the exact ALC level in dBFS with one decimal place.

| Gauge             | Range        | Red zone | Fill direction | Source                                      |
|-------------------|--------------|----------|----------------|---------------------------------------------|
| **Level**         | -40 to +10 dBFS | > 0 dBFS | Bottom-up      | Microphone input peak                        |
| **Compression**   | -25 to 0 dB  | —        | Right-to-left  | Radio COMPPEAK value (0–25 dB positive, displayed as negative) |
| **ALC**           | -20 to 0 dBFS | > -3 dBFS | Right-to-left  | `MeterModel::swAlcChanged` (post-software-ALC SSB peak) |

## CW sub-panel

When the active slice is in a CW or CWL mode, the applet automatically switches to the CW sub-panel.

### CW controls

| Control               | Description                                                                                                                                              | Default | Valid range           | Notes                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-----------------------|------------------------------------------------------------------------------------------------|
| **Delay**             | CW break-in delay in milliseconds. Type a value directly in the text field or use the adjacent slider.                                                    | 500 ms  | 0–2000 ms (step 10)   | Value cached immediately to prevent slider snap-back (#2428).                                  |
| **Speed**             | CW keying speed in words per minute. Type a value directly or use the slider.                                                                             | 20 WPM  | 5–100 WPM             | —                                                                                              |
| **Sidetone**          | Enables or disables CW sidetone. Controls both the radio's DAX-fed monitor and the client-side sidetone generator simultaneously.                        | —       | On / Off              | —                                                                                              |
| **Sidetone volume**   | CW monitor volume. Type a value directly or use the slider. Controls both the radio side (`mon_gain_cw`) and client-side sidetone generator in lockstep.  | 50      | 0–100                 | One slider governs both paths.                                                                 |
| **L / R pan (CW)**    | Sets stereo pan for the CW monitor and applies constant-power pan to the local sidetone generator. Double-click to recentre at 50.                        | 50      | 0–100                 | —                                                                                              |
| **Breakin**           | Toggles full break-in (QSK). With Breakin ON, key edges trigger TX and the break-in delay holds the relay. With Breakin OFF, keys are queued and PTT must be engaged manually. | —       | On / Off              | Fully honors the radio's `break_in` setting as of v0.9.7.                                      |
| **Iambic**            | Toggles iambic paddle keyer mode.                                                                                                                        | —       | On / Off              | —                                                                                              |
| **Pitch < / >**       | CW sidetone and decode pitch. Type a value (100–6000) or click the **<** / **>** buttons to step by 10 Hz.                                                | 600 Hz  | 100–6000 Hz (step 10) | Pitch always follows the radio's `cw_pitch` setting automatically.                             |

### How typing works

1. Click on any value text field (e.g., the **Delay** field showing "500").
2. Type a new number using your keyboard.
3. Press Enter or Tab to commit the value. The slider updates to match immediately.
4. If you type a value outside the valid range, it is clamped to the nearest valid value when you press Enter.

### Sidetone behavior

The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (~10 ms latency) in lockstep. There are no separate local sidetone controls; a single set of controls governs both paths.

In v26.5.3 (#2899), the CW sidetone routes to the user-selected audio output (configured in Settings > Audio) instead of the default output.

Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. There is no separate "Follow" toggle or manual pitch override slider.

### ALC gauge (CW panel)

An identical ALC gauge appears on the CW sub-panel, reading from the same `MeterModel::swAlcChanged` source as the Phone panel ALC gauge. This ensures consistent ALC readings across voice and CW operation.

- Hover the cursor over the gauge to see the exact ALC level in dBFS with one decimal place.

| Gauge           | Range        | Red zone | Fill direction | Source                                      |
|-----------------|--------------|----------|----------------|---------------------------------------------|
| **ALC (CW)**    | -20 to 0 dBFS | > -3 dBFS | Right-to-left  | `MeterModel::swAlcChanged` (post-software-ALC SSB peak) |

## CWX panel integration

The embedded CWX panel's F1–F12 shortcuts are driven by the active slice's mode via `MainWindow::CwxPanel::setShortcutsEnabled` instead of panel visibility. The shortcuts fire when the slice is in CW/CWL mode regardless of whether the CWX panel is visible (#2582). These shortcuts are mutually exclusive with DVK panel F-key bindings. CWX macros also release TX automatically when the queue drains (#2450, #2507).

## Theme support (v26.6.1)

The Phone/CW applet supports the active theme. The following visual elements respect the selected theme:

- **Applet container** — Uses theme styling for consistent background.
- **Slider handles and grooves** — All sliders use `applyPrimarySliderStyle()` for theme colors.
- **Label colors** — Labels such as "Delay:", "Speed:", "L", and "R" pan labels use theme secondary text color.
- **Step buttons** — The **<** and **>** buttons for CW Pitch use theme background and accent colors for normal, hover, and pressed states.

## Hover readouts (v26.7.4)

In v26.7.4 (#3936), all three Phone panel meters (Level, Compression, ALC) and the CW panel ALC gauge gained hover readout popups. Hover the cursor over any gauge to see the exact numerical value:

- **Level gauge**: Shows "X.X dB" (one decimal place).
- **Compression gauge**: Shows the compression amount as a positive value in dB (e.g., "12.5 dB").
- **ALC gauges (Phone and CW)**: Shows "X.X dBFS" (one decimal place).

## Tips

- When using `PC` as the source, the **Level** meter appears immediately when AetherSDR connects to the radio, because PC mic metering runs client-side independently of the radio's `met_in_rx` setting.
- To mix in the accessory port alongside your primary source, enable the **+ACC** toggle button after selecting your main source.
- At higher CW speeds, the client-side sidetone path (~10 ms latency) is more usable than the radio's DAX-fed monitor. Because the **Sidetone** toggle controls both paths together, enabling sidetone always activates the low-latency path automatically.
- The **Compression** gauge reads 0 dB during receive. This is intentional: the gauge is gated on the radio's interlock TRANSMITTING state.
- The **Breakin** button fully honors the radio's `break_in` setting. With **Breakin** on (QSK), key edges trigger TX and the break-in delay holds the relay. With **Breakin** off, you must engage PTT manually.
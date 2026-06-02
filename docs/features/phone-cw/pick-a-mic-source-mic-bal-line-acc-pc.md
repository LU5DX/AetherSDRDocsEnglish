# Pick a mic source (MIC, BAL, LINE, ACC, PC)

Select which physical or virtual input the radio uses as the microphone source for voice transmissions. The choice determines where the FLEX-8600 takes its TX audio from — the front-panel mic connector, balanced input, line input, accessory port, or the PC's audio system.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a phone mode (USB, LSB, AM, FM, etc.). The Phone/CW applet shows the Phone sub-panel automatically in voice modes.

## Steps

1. Click the `P/CW` tray button in the right sidebar to open the Phone/CW applet.
2. Locate the **Mic source** drop-down box in the Phone sub-panel.
3. Click **Mic source** and select one of the available sources: `MIC`, `BAL`, `LINE`, `ACC`, or `PC`.

The selection takes effect immediately on the radio.

## What each control does

| Control            | Description                                                                                                                                                                                     | Default |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **Mic source**     | Selects the microphone input source sent to the radio.                                                                                                                                          | —       |
| **Mic gain**       | Adjusts the microphone input level. When the source is `PC`, or when RADE mode is active, the value is stored client-side in `PcMicGain` because the radio does not manage gain in those paths. | 50      |
| **ALC (Phone panel)** | Shows automatic level control reading from `MeterModel::swAlcChanged` (post-software-ALC SSB peak in dBFS). Fills right-to-left: empty at -20 dBFS, full at 0 dBFS. Rewired from HWALC (RCA voltage) to SW ALC meter in v26.5.1 (#2552). | — |
| **ALC (CW panel)**     | Mirrors the Phone-panel ALC gauge; both read from `MeterModel::swAlcChanged` for consistent readings across voice and CW. Added in v26.5.1 (#2552) as part of the SW ALC meter split. Uses `HGauge::setFillFromRight` mode. In v26.5.3 both gauges are initialised to -20 dBFS immediately to avoid a stale reading during startup (#2899). | — |

**Source descriptions:**

- **MIC** — Front-panel microphone connector.
- **BAL** — Balanced microphone input.
- **LINE** — Line-level input.
- **ACC** — Accessory port microphone input.
- **PC** — Computer audio system. The radio does not report mic level for this source; AetherSDR stores the gain value locally in `PcMicGain`.

## RADE mode and mic gain

When RADE mode is active, the **Mic gain** slider acts as a client-side RADE gain control rather than sending a mic level command to the radio. The slider value is stored in `PcMicGain`, the same setting used for the `PC` source. Moving the slider does not overwrite the radio's hardware mic level setting while RADE is active.

The **Level** meter remains active during receive when RADE is on. This allows you to monitor input level between transmissions without enabling `met_in_rx` on the radio.

When RADE mode is deactivated, the slider reverts to the radio's reported mic level and the **Level** gauge resets to −150 dBFS until a new meter value arrives.

## CW controls (v0.9.8+)

When the active slice is in a CW mode, the applet switches to the CW sub-panel. In v0.9.8, the four CW value labels (Delay, Speed, Sidetone Volume, Pitch) have been converted to `QLineEdit` widgets with `QIntValidator`. Click any value and type a number directly, matching SmartSDR behavior.

### CW value entry

| Control               | Description                                                                                                          | Default | Valid range           | Notes                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------|---------|-----------------------|------------------------------------------------------------------------------------------------|
| **Delay**             | CW break-in delay in milliseconds. Type a value directly in the text field or use the adjacent slider.               | 500 ms  | 0–2000 ms (step 10)   | In v0.9.8, `setCwDelay` was fixed to cache the value immediately so the radio emission doesn't snap the slider back (#2428). |
| **Speed**             | CW keying speed in words per minute. Type a value directly or use the slider.                                        | 20 WPM  | 5–100 WPM             | —                                                                                              |
| **Sidetone volume**   | CW monitor volume. Type a value directly or use the slider. Controls both the radio side (`mon_gain_cw`) and client-side sidetone generator in lockstep. | 50      | 0–100                 | (v0.9.8, #2429)                                                                                |
| **Pitch**             | CW sidetone and decode pitch. Type a value (100–6000) or click the **< / >** buttons to step by 10 Hz.               | 600 Hz  | 100–6000 Hz (step 10) | (v0.9.8, #2429)                                                                                |

### How typing works

1. Click on any value text field (e.g., the **Delay** field showing "500").
2. Type a new number using your keyboard.
3. Press Enter or Tab to commit the value. The slider updates to match immediately.
4. If you type a value outside the valid range, it is clamped to the nearest valid value when you press Enter.

### Sidetone behavior

The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (~10 ms latency) in lockstep. There are no separate local sidetone controls; a single set of controls governs both paths.

| Control               | Description                                                                                                                                              | Default | Valid values | Setting key |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------------|-------------|
| **Sidetone**          | Enables or disables CW sidetone. Controls both the radio's DAX-fed monitor and the client-side sidetone generator simultaneously.                        | —       | On / Off     | —           |
| **Sidetone volume**   | Sets the sidetone volume for both the radio side (`mon_gain_cw`) and the client-side generator.                                                          | —       | 0–100        | —           |
| **L / R pan (CW)**    | Sets stereo pan for the CW monitor and applies constant-power pan to the local sidetone generator. Double-click to recentre at 50.                        | 50      | 0–100        | —           |
| **Pitch < / >**       | Steps the CW sidetone and decode pitch by 10 Hz, or type a value directly.                                                                               | 600 Hz  | 100–6000 Hz  | —           |

Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. There is no separate "Follow" toggle or manual pitch override slider; those controls were removed in v0.9.2.1.

In v26.5.3 (#2899), the CW sidetone now routes to the user-selected audio output instead of the default output. This means the sidetone is heard through whatever device you have configured in Settings > Audio, not necessarily the system default.

## Metering: ALC gauges (v26.5.1+)

In v26.5.1 (#2552), both the Phone panel and CW panel received new, identical ALC gauges. These replace the previous HWALC (RCA voltage) path that produced meaningless readings.

| Gauge               | Range        | Red zone | Fill direction | Source                                      |
|---------------------|--------------|----------|----------------|---------------------------------------------|
| **ALC (Phone panel)** | -20 to 0 dBFS | > -3 dBFS | Right-to-left  | `MeterModel::swAlcChanged` (post-software-ALC SSB peak) |
| **ALC (CW panel)**    | -20 to 0 dBFS | > -3 dBFS | Right-to-left  | `MeterModel::swAlcChanged` (identical source)           |

In v26.5.3, both ALC gauges are initialised to -20 dBFS immediately on construction. This prevents a brief stale reading during startup while the first meter update is still in-flight.

Key points:
- Both gauges read from the same `MeterModel::swAlcChanged` source, ensuring consistent readings across voice and CW.
- The gauge is empty at -20 dBFS and fills leftward toward 0 dBFS.
- Values below -20 dBFS pin at the left end; values above 0 dBFS pin at the right end (full scale).
- The red zone (> -3 dBFS) indicates excessive ALC; aim to keep the gauge reading below -3 dBFS for clean transmit.

## Metering: Level gauge receive gating (v26.5.3+)

In v26.5.3 (#2899), the logic that suppresses the **Level** gauge during receive was moved into a dedicated `applyLevelMeterReceiveGate()` method. This method is called from the RX/TX state and MOX change signals, as well as from `updateMeters()` and `setRadeActive()`:

- When the radio is receiving and `met_in_rx` is disabled, the **Level** gauge is set to -150 dBFS regardless of the mic source (PC or RADE).
- Previously, the `PC` source and RADE mode had an exception that kept the **Level** gauge active during receive. As of v26.5.3, that exception is removed: all mic sources are suppressed equally when `met_in_rx` is off and the radio is not transmitting.

## Metering: Compression gauge (v26.5.3+)

In v26.5.3 (#2899), the `updateCompression()` slot was updated to correctly interpret the `COMPPEAK` value from the radio. The radio reports compression as a positive 0–25 dB amount. The P/CW gauge face is reversed: 0 = no compression (no reduction), -25 = full compression (25 dB reduction). The gauge now maps the radio's positive compression value to a negative gauge value:

- `compPeak = 0 dB` → gauge shows `0 dB`
- `compPeak = 25 dB` → gauge shows `-25 dB`

Values are clamped to the 0–25 dB range before the conversion, so the gauge never reads beyond `-25 dB`.

## Theme support (v26.6.1)

In v26.6.1, the Phone/CW applet gained full theme support. The following visual elements now respect the active theme:

- **Applet container** — Uses `theme::setContainer(this, "applet/digi")` for consistent background styling.
- **Slider handles and grooves** — All sliders (Mic gain, Processor level, Monitor volume, Delay, Speed, Sidetone volume, CW pan) now use `applyPrimarySliderStyle()` instead of a hard-coded style sheet, allowing theme colors to be applied.
- **Label colors** — Labels such as "Delay:", "Speed:", and "L" and "R" pan labels now use `{{color.text.secondary}}` from the theme.
- **Step buttons** — The **<** and **>** buttons for CW Pitch now use `{{color.background.1}}` for normal and hover states, and `{{color.accent}}` for the pressed state, replacing the previous hard-coded colors.

The theme integration ensures that the Phone/CW applet matches the visual style of the rest of the AetherSDR interface when a theme is selected.

## Tips

- When using `PC` as the source, the **Level** meter appears immediately when AetherSDR connects to the radio, because PC mic metering runs client-side independently of the radio's `met_in_rx` setting. The meter is not suppressed between transmissions for PC sources.
- When RADE mode is active, the **Level** meter also runs client-side and is not suppressed between transmissions, regardless of the `met_in_rx` setting. This matches the behavior of the `PC` source.
- To mix in the accessory port alongside your primary source, enable the **+ACC** toggle button after selecting your main source.
- At higher CW speeds, the client-side sidetone path (~10 ms latency) is more usable than the radio's DAX-fed monitor. Because the **Sidetone** toggle controls both paths together, enabling sidetone always activates the low-latency path automatically.
- When VOX is toggled via keyboard shortcut, the Phone panel refreshes instantly to reflect the new VOX state (v0.9.3).
- On Windows, the CW sidetone stream starts immediately on connect (v0.9.3). If sidetone is enabled before connecting, no additional steps are required after the connection is established.
- The **Compression** gauge reads 0 dB during receive. This is intentional: in v0.9.7 the gauge is gated on the radio's interlock TRANSMITTING state, so stale TX chain readings are not displayed between transmissions. In v26.5.3 the compression value mapping was corrected to use the radio's positive 0–25 dB range.
- The **Breakin** button fully honors the radio's `break_in` setting as of v0.9.7. With **Breakin** on (QSK), key edges trigger TX and the break-in delay holds the relay.
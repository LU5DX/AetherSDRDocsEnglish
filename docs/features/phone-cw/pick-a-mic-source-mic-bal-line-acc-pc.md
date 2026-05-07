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

| Control        | Description                                                                                                                                                                                     | Default |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| **Mic source** | Selects the microphone input source sent to the radio.                                                                                                                                          | —       |
| **Mic gain**   | Adjusts the microphone input level. When the source is `PC`, or when RADE mode is active, the value is stored client-side in `PcMicGain` because the radio does not manage gain in those paths. | 50      |

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

| Control | Description | Default | Valid range | Notes |
|---|---|---|---|---|
| **Delay** | CW break-in delay in milliseconds. Type a value directly in the text field or use the adjacent slider. | 500 ms | 0–2000 ms (step 10) | In v0.9.8, `setCwDelay` was fixed to cache the value immediately so the radio emission doesn't snap the slider back (#2428). |
| **Speed** | CW keying speed in words per minute. Type a value directly or use the slider. | 20 WPM | 5–100 WPM | — |
| **Sidetone volume** | CW monitor volume. Type a value directly or use the slider. Controls both the radio side (`mon_gain_cw`) and client-side sidetone generator in lockstep. | 50 | 0–100 | (v0.9.8, #2429) |
| **Pitch** | CW sidetone and decode pitch. Type a value (100–6000) or click the **< / >** buttons to step by 10 Hz. | 600 Hz | 100–6000 Hz (step 10) | (v0.9.8, #2429) |

### How typing works

1. Click on any value text field (e.g., the **Delay** field showing "500").
2. Type a new number using your keyboard.
3. Press Enter or Tab to commit the value. The slider updates to match immediately.
4. If you type a value outside the valid range, it is clamped to the nearest valid value when you press Enter.

### Sidetone behavior

The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (~10 ms latency) in lockstep. There are no separate local sidetone controls; a single set of controls governs both paths.

| Control | Description | Default | Valid values | Setting key |
|---|---|---|---|---|
| **Sidetone** | Enables or disables CW sidetone. Controls both the radio's DAX-fed monitor and the client-side sidetone generator simultaneously. | — | On / Off | — |
| **Sidetone volume** | Sets the sidetone volume for both the radio side (`mon_gain_cw`) and the client-side generator. | — | 0–100 | — |
| **L / R pan (CW)** | Sets stereo pan for the CW monitor and applies constant-power pan to the local sidetone generator. Double-click to recentre at 50. | 50 | 0–100 | — |
| **Pitch < / >** | Steps the CW sidetone and decode pitch by 10 Hz, or type a value directly. | 600 Hz | 100–6000 Hz | — |

Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. There is no separate "Follow" toggle or manual pitch override slider; those controls were removed in v0.9.2.1.

## Tips

- When using `PC` as the source, the **Level** meter appears immediately when AetherSDR connects to the radio, because PC mic metering runs client-side independently of the radio's `met_in_rx` setting. The meter is not suppressed between transmissions for PC sources.
- When RADE mode is active, the **Level** meter also runs client-side and is not suppressed between transmissions, regardless of the `met_in_rx` setting. This matches the behavior of the `PC` source.
- To mix in the accessory port alongside your primary source, enable the **+ACC** toggle button after selecting your main source.
- At higher CW speeds, the client-side sidetone path (~10 ms latency) is more usable than the radio's DAX-fed monitor. Because the **Sidetone** toggle controls both paths together, enabling sidetone always activates the low-latency path automatically.
- When VOX is toggled via keyboard shortcut, the Phone panel refreshes instantly to reflect the new VOX state (v0.9.3).
- On Windows, the CW sidetone stream starts immediately on connect (v0.9.3). If sidetone is enabled before connecting, no additional steps are required after the connection is established.
- The **Compression** gauge reads 0 dB during receive. This is intentional: in v0.9.7 the gauge is gated on the radio's interlock TRANSMITTING state, so stale TX chain readings are not displayed between transmissions.
- The **Breakin** button fully honors the radio's `break_in` setting as of v0.9.7. With **Breakin** on (QSK), key edges trigger TX and the break-in delay holds the relay. With **Breakin** off, keys are queued and PTT must be engaged manually. The previous behavior, where an auto-PTT envelope masked the **Breakin** off state and interfered with QSK hang time, has been removed.

## Troubleshooting

- **Mic source combo shows no selection or resets** — The list is populated from the radio's reported inputs. If the combo is empty, verify the radio connection is active (`Settings > Connect to Radio...`).
- **Level meter reads nothing when source is PC** — This is not expected behavior in v0.9.3. The **Level** gauge should appear immediately on connect when the mic source is `PC`. If it does not, verify that AetherSDR is running v0.9.3 or later. For non-PC sources, the meter is suppressed to −150 dBFS when not transmitting and `met_in_rx` is off; this is normal.
- **Level meter reads nothing when RADE is active** — The **Level** gauge should remain active during receive when RADE mode is on, independently of `met_in_rx`. If the gauge is not updating, verify that AetherSDR is running v0.9.7 or later.
- **Mic gain slider resets to 100 when RADE activates** — RADE mode and the `PC` source both use the `PcMicGain` setting. If you have not previously set a value for `PcMicGain`, the slider defaults to 100 when RADE becomes active. Adjust the slider to your preferred level; the value is stored immediately.
- **Sidetone pitch does not match expectation** — Pitch follows the radio's `cw_pitch` setting automatically. Adjust pitch using the **Pitch < / >** spinbox or type a value directly.
- **Sidetone does not start on connect (Windows)** — This was a known issue in versions before v0.9.3 caused by AudioEngine initialization order. Update to v0.9.3 or later to resolve it.
- **Compression gauge shows a value during receive** — This should not occur in v0.9.7. The gauge is gated on the radio's interlock TRANSMITTING state and reads 0 during RX. If you see a non-zero reading while receiving, verify that you are running v0.9.7 or later.
- **Breakin off does not prevent TX on key press** — This behavior was corrected in v0.9.7. Update to v0.9.7 or later. In earlier versions, an internal auto-PTT envelope could force TX regardless of the **Breakin** setting.
- **Typed CW value resets immediately** — If you type a value in a CW text field and it resets before you press Enter, ensure you press Enter or Tab to commit the value. The fields only accept the typed value when editing is finished.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
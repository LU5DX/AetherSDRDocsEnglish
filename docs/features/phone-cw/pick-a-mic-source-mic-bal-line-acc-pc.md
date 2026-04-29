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

| Control | Description | Default | Valid values | Setting key |
|---|---|---|---|---|
| **Mic source** | Selects the microphone input source sent to the radio. | — | `MIC`, `BAL`, `LINE`, `ACC`, `PC` | — |
| **Mic gain** | Adjusts the microphone input level. When the source is `PC`, the value is stored client-side because the radio always reports a level of 0 for PC sources. | 50 | 0–100 | `PcMicGain` |

**Source descriptions:**

- **MIC** — Front-panel microphone connector.
- **BAL** — Balanced microphone input.
- **LINE** — Line-level input.
- **ACC** — Accessory port microphone input.
- **PC** — Computer audio system. The radio does not report mic level for this source; AetherSDR stores the gain value locally in `PcMicGain`.

## CW sidetone controls (v0.9.1+)

When the active slice is in a CW mode, the applet switches to the CW sub-panel. The **Sidetone** toggle and **Sidetone volume** slider control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (~10 ms latency) in lockstep. There are no separate local sidetone controls; a single set of controls governs both paths.

| Control | Description | Default | Valid values | Setting key |
|---|---|---|---|---|
| **Sidetone** | Enables or disables CW sidetone. Controls both the radio's DAX-fed monitor and the client-side sidetone generator simultaneously. | — | On / Off | — |
| **Sidetone volume** | Sets the sidetone volume for both the radio side (`mon_gain_cw`) and the client-side generator. | — | 0–100 | — |
| **L / R pan (CW)** | Sets stereo pan for the CW monitor and applies constant-power pan to the local sidetone generator. Double-click to recentre at 50. | 50 | 0–100 | — |
| **Pitch < / >** | Steps the CW sidetone and decode pitch by 10 Hz. | 600 Hz | 100–6000 Hz | — |

Pitch and pan always follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically. There is no separate "Follow" toggle or manual pitch override slider; those controls were removed in v0.9.2.1.

## Tips

- When using `PC` as the source, the **Level** meter in the applet is suppressed while not transmitting. Transmit briefly to confirm audio is passing.
- To mix in the accessory port alongside your primary source, enable the **+ACC** toggle button after selecting your main source.
- At higher CW speeds, the client-side sidetone path (~10 ms latency) is more usable than the radio's DAX-fed monitor. Because the **Sidetone** toggle controls both paths together, enabling sidetone always activates the low-latency path automatically.

## Troubleshooting

- **Mic source combo shows no selection or resets** — The list is populated from the radio's reported inputs. If the combo is empty, verify the radio connection is active (`Settings > Connect to Radio...`).
- **Level meter reads nothing when source is PC** — This is expected. The radio reports `mic_level=0` for PC sources; the gain is managed by `PcMicGain` on the client side.
- **Sidetone pitch does not match expectation** — Pitch follows the radio's `cw_pitch` setting automatically. Adjust pitch using the **Pitch < / >** spinbox, which writes directly to the radio.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
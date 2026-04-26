# Phone/CW overview

The Phone/CW applet is the mode-aware transmit control panel in AetherSDR. It shows microphone, processor, and monitor controls when the active slice is in a voice mode, and automatically switches to CW controls when the active slice is in a CW mode.

## Before you start

- Connect to a FLEX-8600 radio. The applet requires an active radio connection.
- Make sure the Applet Panel is visible. If it is not, select `View > Applet Panel`.

## How it works

The applet is labeled **P/CW** in the Applet Panel tray. Click the **P/CW** tray button to show or hide it. The panel contains two sub-panels stacked behind each other:

**Phone sub-panel** — displayed when the active slice is in a voice mode (SSB, AM, FM, and similar). It provides microphone source selection, gain, speech processing, DAX, and a TX audio monitor.

**CW sub-panel** — displayed automatically when the active slice switches to a CW mode. It provides keying speed, break-in delay, iambic mode, sidetone, and CW pitch controls.

You do not select which sub-panel to show; AetherSDR switches between them based on the active slice mode.

## What each control does

### Phone sub-panel

| Control | Kind | Description | Default | Range / Options | Setting key |
|---|---|---|---|---|---|
| Level | Meter | Microphone input peak level in dBFS. Reads –150 when meter-in-RX is off and not transmitting. | — | –40 to +10 dBFS (red above 0) | — |
| Compression | Meter | Speech compression amount in dB. Fill is reversed (full bar = maximum compression). | — | –25 to 0 dB | — |
| Mic profile | Combo box | Loads a named mic processing profile from the radio's profile list. | — | Populated from radio | — |
| Mic source | Combo box | Selects the microphone input source. | — | MIC, BAL, LINE, ACC, PC | — |
| Mic gain | Slider | Adjusts microphone input level. When source is PC, the value is stored locally because the radio always reports mic level as 0 for the PC source. | 50 | 0–100 | `PcMicGain` |
| +ACC | Toggle button | Enables the accessory mic input mix alongside the selected source. | — | On / Off | — |
| PROC | Toggle button | Enables the speech processor. | — | On / Off | — |
| NOR/DX/DX+ | Slider | Sets the speech processor level. Three positions: NOR (0), DX (1), DX+ (2). | NOR (0) | 0, 1, 2 | — |
| DAX | Toggle button | Enables DAX as the TX audio source. | — | On / Off | — |
| MON | Toggle button | Enables the TX sideband monitor (listen to your own transmitted audio). | — | On / Off | — |
| Monitor volume | Slider | Sets the sideband monitor volume. | — | 0–100 | — |

### CW sub-panel

| Control | Kind | Description | Default | Range / Options | Setting key |
|---|---|---|---|---|---|
| ALC | Meter | Automatic level control reading. | — | 0–100 (red above 80) | — |
| Delay (CW) | Slider | Sets the CW break-in delay. | — | 0–2000 ms (step 10) | — |
| Speed (CW) | Slider | Sets the CW keying speed. | — | 5–100 WPM | — |
| Sidetone | Toggle button | Enables the CW sidetone monitor. | — | On / Off | — |
| Sidetone volume | Slider | Sets the CW monitor volume. | — | 0–100 | — |
| L / R pan (CW) | Slider | Sets the CW monitor stereo pan position. | 50 | 0–100 | — |
| Breakin | Toggle button | Enables full break-in (QSK) mode. | — | On / Off | — |
| Iambic | Toggle button | Enables the iambic paddle keyer. | — | On / Off | — |
| Pitch < / > | Spinbox | Steps the CW sidetone and decode pitch by 10 Hz per click. | 600 Hz | 100–6000 Hz (step 10) | — |

## Tips

- When **Mic source** is set to PC, the radio does not report the mic level back to the client. AetherSDR stores the **Mic gain** value locally using `PcMicGain` so the slider position is preserved across sessions.
- The **NOR/DX/DX+** slider only affects the processor level. **PROC** must be enabled for any compression to be applied.
- The **ALC** meter appears on the CW sub-panel, not the Phone sub-panel. Watch it while adjusting drive level to avoid overdrive.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)

# Phone/CW overview

The Phone/CW applet is AetherSDR's mode-aware transmit control panel. It shows microphone, processor, and monitor controls when the active slice is in a voice mode, and automatically switches to CW keyer controls when the active slice is in a CW mode.

## How it works

The Phone/CW applet lives in the Applet Panel on the right sidebar. Toggle it with the **P/CW** tray button. Internally it uses a two-panel stack: the Phone panel is shown for voice modes, and the CW panel is shown for CW modes. The switch happens automatically based on the active slice mode — you do not select it manually.

### Phone panel

The Phone panel provides the following controls.

| Control | Kind | Default | Valid range | Persisted key | What it does |
|---|---|---|---|---|---|
| Level | Meter | — | −40 to +10 dBFS (red above 0) | — | Shows microphone input peak level in dBFS. Suppressed to −150 when not transmitting and mic monitoring is off. |
| Compression | Meter | — | −25 to 0 dB (reversed fill) | — | Shows speech compression amount in dB. Fill runs right-to-left. |
| Mic profile | Combo box | — | Populated from radio | — | Loads the named mic processing profile. |
| Mic source | Combo box | — | MIC, BAL, LINE, ACC, PC | — | Selects microphone input source. |
| Mic gain | Slider | 50 | 0–100 | `PcMicGain` | Adjusts mic input level. When source is PC, the value is kept client-side; the radio always reports mic level as 0 for the PC source. |
| +ACC | Toggle button | — | On / Off | — | Enables the accessory mic input mix alongside the selected source. |
| PROC | Toggle button | — | On / Off | — | Toggles the speech processor. |
| NOR/DX/DX+ | Slider | 0 (NOR) | 0 = NOR, 1 = DX, 2 = DX+ | — | Sets speech processor level in three steps. |
| DAX | Toggle button | — | On / Off | — | Enables DAX as the TX audio source. |
| MON | Toggle button | — | On / Off | — | Enables the TX sideband monitor so you can hear your own transmitted audio. |
| Monitor volume | Slider | — | 0–100 | — | Sets sideband monitor volume. |

### CW panel

The CW panel provides the following controls.

| Control | Kind | Default | Valid range | Persisted key | What it does |
|---|---|---|---|---|---|
| ALC | Meter | — | 0–100 (red above 80) | — | Shows automatic level control reading. |
| Delay | Slider | — | 0–2000 ms (step 10) | — | Sets CW break-in (QSK) hang delay. |
| Speed | Slider | — | 5–100 WPM | — | Sets CW keying speed. |
| Sidetone | Toggle button | — | On / Off | — | Toggles CW sidetone monitor. |
| Sidetone volume | Slider | — | 0–100 | — | Sets CW sidetone monitor volume. |
| L / R pan | Slider | 50 | 0–100 | — | Pans the CW monitor audio left or right. |
| Breakin | Toggle button | — | On / Off | — | Toggles full break-in (QSK). |
| Iambic | Toggle button | — | On / Off | — | Toggles iambic paddle keyer mode. |
| Pitch < / > | Spin box | 600 Hz | 100–6000 Hz (step 10) | — | Steps CW sidetone and decode pitch. |

## Tips

- When Mic source is set to PC, the radio does not report a mic level back to AetherSDR. The Mic gain slider value is stored locally using `PcMicGain` and applied from the client side.
- The Phone and CW panels switch automatically. If your controls appear wrong, confirm the active slice mode on the panadapter.
- Keep the Level gauge peak below 0 dBFS during normal operation; the gauge turns red above that threshold.
- Keep the ALC meter below 80 during CW transmission; the gauge turns red above that value.

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

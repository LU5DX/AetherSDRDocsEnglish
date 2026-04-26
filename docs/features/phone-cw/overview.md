# Phone/CW overview

The Phone/CW applet is a mode-aware transmit control panel. It shows microphone, processor, and monitor controls when the active slice is in a voice mode, and automatically switches to CW controls — including keyer, sidetone, and pitch — when the active slice is in CW mode.

## Before you start

- AetherSDR must be connected to the radio. The applet requires an active radio connection.
- The applet is always present in the Applet Panel (right sidebar). If the panel is hidden, enable it via `View > Applet Panel`. Toggle the applet open or closed with the `P/CW` tray button.

## How it works

The applet contains two sub-panels stacked behind each other. AetherSDR switches between them automatically based on the active slice mode:

- **Phone sub-panel** — active in voice modes (SSB, AM, FM). Shows mic metering, mic source and gain, speech processor, DAX, and TX monitor controls.
- **CW sub-panel** — active when the slice is in CW mode. Shows ALC metering, keyer speed and delay, break-in, iambic, radio sidetone, and the client-side local sidetone path.

### Phone sub-panel controls

| Control | What it does | Default | Range / Values | Setting key |
|---|---|---|---|---|
| Level | Mic input peak meter (dBFS). Reads –150 when the radio is not transmitting and met_in_rx is off. | — | –40 to +10 dBFS (red above 0) | — |
| Compression | Speech compression meter (reversed fill — bar fills from the right). | — | –25 to 0 dB | — |
| Mic profile | Loads a named mic processing profile from the radio's profile list. | — | Populated from radio | — |
| Mic source | Selects the microphone input source. | — | MIC, BAL, LINE, ACC, PC | — |
| Mic gain | Adjusts mic input level. When source is PC, the value is kept client-side because the radio always reports mic_level=0 for that source. | 50 | 0–100 | `PcMicGain` |
| +ACC | Enables the accessory mic input mix. Checkable. | — | On / Off | — |
| PROC | Toggles the speech processor. Checkable. | — | On / Off | — |
| NOR/DX/DX+ | Three-position processor level slider. | 0 (NOR) | 0 = NOR, 1 = DX, 2 = DX+ | — |
| DAX | Enables DAX as the TX audio source. Checkable. | — | On / Off | — |
| MON | Enables the TX sideband monitor. Checkable. | — | On / Off | — |
| Monitor volume | Sets the sideband monitor volume. | — | 0–100 | — |

### CW sub-panel controls

| Control | What it does | Default | Range / Values | Setting key |
|---|---|---|---|---|
| ALC | ALC reading meter. Red above 80. | — | 0–100 | — |
| Delay | CW break-in delay in milliseconds. | — | 0–2000 ms (step 10) | — |
| Speed | CW keying speed. | — | 5–100 WPM | — |
| Breakin | Toggles full break-in (QSK). Checkable. | — | On / Off | — |
| Iambic | Toggles the iambic paddle keyer. Checkable. | — | On / Off | — |
| Pitch < / > | Steps the CW sidetone and decode pitch by 10 Hz. | 600 Hz | 100–6000 Hz (step 10) | — |
| Sidetone | Toggles the radio CW sidetone monitor (DAX-fed). Checkable. | — | On / Off | — |
| Sidetone volume | Sets the radio CW monitor volume. | — | 0–100 | — |
| L / R pan | CW monitor pan. | 50 | 0–100 | — |
| Local STn | Enables the client-side low-latency CW sidetone (~10 ms latency), generated independently of the radio's DAX-fed monitor. Works with paddle, straight key, and CWX text. Checkable. | Off | On / Off | `CwLocalSidetoneEnabled` |
| Local sidetone volume | Volume of the local sidetone, independent of the radio sidetone gain. | 50 | 0–100 | `CwLocalSidetoneVolume` |
| Follow | When on, the local sidetone pitch tracks the radio's CW pitch setting. When off, the manual pitch slider is active. Checkable. | On | On / Off | `CwLocalSidetonePitchFollow` |
| Local sidetone pitch | Manual pitch for the local sidetone in Hz. Only adjustable when Follow is off. | 600 Hz | 100–2000 Hz | `CwLocalSidetonePitchHz` |

## Tips

- The Phone and CW sub-panels switch automatically. You do not need to select them manually — changing the slice mode is sufficient.
- The local sidetone (Local STn) and the radio sidetone (Sidetone) are independent. You can run both simultaneously or use either alone.
- When Mic source is set to PC, the Mic gain value is stored in `PcMicGain` on the client. The radio does not retain it.
- Follow is on by default, so the local sidetone pitch stays in sync with the radio CW pitch without manual adjustment.

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
- [Enable the low-latency local CW sidetone (Local STn) for fast paddle / straight-key / CWX work](enable-the-low-latency-local-cw-sidetone-local-stn-for-fast-paddle-straight-key-cwx-work.md)
- [Set the local sidetone volume independently of the radio monitor](set-the-local-sidetone-volume-independently-of-the-radio-monitor.md)
- [Make the local sidetone pitch follow the radio's CW pitch, or set it manually with the slider](make-the-local-sidetone-pitch-follow-the-radio-s-cw-pitch-or-set-it-manually-with-the-slider.md)

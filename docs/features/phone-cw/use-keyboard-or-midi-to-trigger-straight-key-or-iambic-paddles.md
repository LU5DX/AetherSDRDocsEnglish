# Use keyboard or MIDI to trigger straight key or iambic paddles

This page explains how to send CW using a computer keyboard or MIDI controller as a straight key or iambic paddles through the Phone/CW applet. This lets you key the radio without physical paddle hardware connected to the FLEX-8600.

## Before you start

- The active slice must be in a CW mode. The Phone/CW applet switches to its CW sub-panel automatically when CW mode is selected.
- The Phone/CW applet must be visible. If it is not, click the **P/CW** tray button in the right sidebar, or go to `View > Applet Panel` to show the sidebar.
- For MIDI input, your MIDI controller must be connected before launching AetherSDR. Open `Settings > MIDI Mapping...` to assign controller inputs to key functions.

## Steps

1. Select a CW mode on the active slice. The Phone/CW applet switches to the CW sub-panel.
2. Decide whether you want straight key or iambic paddle operation. For iambic, click **Iambic** so it is active (highlighted). For straight key, leave **Iambic** inactive.
3. Set your keying speed with the **Speed (CW)** slider (5–100 WPM).
4. Choose how TX is triggered:
   - For full break-in (QSK), click **Breakin** so it is active. Key edges from the keyboard or MIDI controller will trigger TX immediately; the radio's break-in delay holds the relay between characters.
   - For manual PTT, leave **Breakin** inactive. Key input will be queued; engage PTT separately to transmit. See [Configure break-in OFF so CW keys queue and PTT is manual](configure-break-in-off-so-cw-keys-queue-and-ptt-is-manual.md).
5. If you want sidetone while keying, click **Sidetone** to enable it. Adjust the **Sidetone volume** slider to a comfortable level. The client-side low-latency sidetone (approximately 10 ms latency) and the radio's DAX-fed monitor are both controlled by this single button and slider.
6. Begin keying from the keyboard or MIDI controller. With **Iambic** active, the dit and dah inputs are treated as paddle contacts. With **Iambic** inactive, any key input acts as a straight key closure.

## What each control does

| Control | What it does | Default | Range | Setting key |
|---|---|---|---|---|
| **Iambic** | Toggles iambic paddle keyer. When active, keyboard/MIDI inputs are treated as dit and dah paddle contacts. When inactive, input acts as a straight key. | — | On / Off | — |
| **Breakin** | Toggles full break-in (QSK). When active, key edges trigger TX and break-in delay holds the relay. When inactive, keys queue and PTT must be engaged manually. | — | On / Off | — |
| **Speed (CW)** | Sets the keying speed applied to keyboard and MIDI input. | — | 5–100 WPM | — |
| **Delay (CW)** | Sets the CW break-in hang time after the last key edge before TX drops. | — | 0–2000 ms (step 10) | — |
| **Sidetone** | Enables the CW sidetone monitor. Controls both the radio's DAX-fed monitor and the client-side low-latency sidetone generator in lockstep. | — | On / Off | — |
| **Sidetone volume** | Sets CW monitor volume. Controls both radio-side and client-side sidetone volumes in lockstep. | — | 0–100 | — |
| **Pitch < / >** | Steps the sidetone and decode pitch by 10 Hz. Pitch follows the radio's `cw_pitch` setting automatically. | 600 Hz | 100–6000 Hz (step 10) | — |

## Tips

- Sidetone pitch and stereo pan follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically; you do not need to reconfigure them after changing the radio's CW pitch.
- With **Breakin** OFF, key input from the keyboard or MIDI controller is queued. This is useful when you want to compose characters before transmitting. Engage PTT manually to send the queued input.
- Double-clicking the **L / R pan (CW)** slider recenters it to 50 (centre).

## Troubleshooting

- **MIDI controller is not recognized** — Ensure the controller was connected before launching AetherSDR. Open `Settings > MIDI Mapping...` to verify the device is listed and inputs are mapped.
- **Keying does not trigger TX** — Check that **Breakin** is active if you expect QSK operation. If **Breakin** is inactive, the radio expects a manual PTT to transmit queued keys.
- **No sidetone heard while keying** — Confirm **Sidetone** is active and **Sidetone volume** is above zero. Also verify the active slice is in CW mode; the CW sub-panel only appears in CW mode.
- **Iambic paddles send straight key behavior** — Confirm **Iambic** is active (highlighted) in the CW sub-panel.

## Related

- [Enable iambic paddle keying](enable-iambic-paddle-keying.md)
- [Configure break-in OFF so CW keys queue and PTT is manual](configure-break-in-off-so-cw-keys-queue-and-ptt-is-manual.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)](enable-the-low-latency-cw-sidetone-sidetone-button-drives-both-radio-and-local-path.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)

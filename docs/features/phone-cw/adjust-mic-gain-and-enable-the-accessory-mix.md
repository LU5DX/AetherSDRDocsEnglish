# Adjust mic gain and enable the accessory mix

Use the Phone/CW applet to set the microphone input level and optionally blend in the accessory port input when operating in a voice mode.

## Before you start

- Connect to a FLEX-8600 radio. The Phone/CW applet requires an active radio connection.
- Set the active slice to a voice mode (SSB, AM, FM). The applet shows the Phone panel only when the active slice is not in CW mode.

## Steps

1. Open the Applet Panel if it is not visible. Click the **P/CW** tray button on the right sidebar, or go to `View > Applet Panel` to show the panel, then click **P/CW**.
2. Confirm the Phone panel is shown. If the active slice is in CW mode, switch it to a voice mode first.
3. Locate the **Mic gain** slider in the row that also contains the **Mic source** combo box and the **+ACC** button.
4. Drag the **Mic gain** slider left or right to set the desired input level. The valid range is 0–100. The default is 50. The numeric value updates to the right of the slider as you drag.
5. Watch the **Level** gauge above the slider. Aim to keep peaks below 0 dBFS; the gauge turns red above 0 dBFS. The valid display range is −40 to +10 dBFS.
6. To mix in the accessory port input alongside the currently selected mic source, click **+ACC** so it lights green. Click **+ACC** again to disable the mix.

## What each control does

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| **Mic gain** | Slider | 50 | 0–100 | `PcMicGain` |
| **+ACC** | Toggle button | — | On / Off | — |
| **Level** | Meter | — | −40 to +10 dBFS (red above 0) | — |

## Tips

- When **Mic source** is set to **PC**, the radio always reports a mic level of 0 internally. AetherSDR keeps the **Mic gain** value locally using the `PcMicGain` setting and applies it client-side. Set the level in the applet rather than relying on the radio's reported value.
- **+ACC** adds the accessory port input on top of the selected **Mic source**. It does not replace the current source selection.

## Troubleshooting

- **Level gauge reads −150 dBFS and does not respond while receiving** — The meter is suppressed to −150 when the radio is not transmitting and met_in_rx is off. The gauge becomes active when you transmit.
- **Mic gain slider resets to 0 after changing Mic source to PC** — The radio reports mic_level=0 for the PC source. The slider will reflect the locally stored `PcMicGain` value on the next update. Adjust the slider to your preferred level and it will be saved.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

# Adjust mic gain and enable the accessory mix

Use the Phone/CW applet to set the microphone input level and optionally blend in the accessory connector input alongside your primary mic source.

## Before you start

- AetherSDR must be connected to the radio. The Phone/CW applet controls are only active with a live radio connection.
- The active slice must be in a voice mode (SSB, AM, FM). In CW mode the applet switches to the CW panel and the mic controls are not shown.
- Open the Phone/CW applet if it is not already visible: click the **P/CW** tray button on the right sidebar, or confirm the applet panel is shown via `View > Applet Panel`.

## Steps

1. In the Phone/CW applet, locate the row containing the **Mic source** combo box, the **Mic gain** slider, and the **+ACC** button.
2. Drag the **Mic gain** slider left or right to set the desired input level. The numeric readout to the right of the slider updates as you drag. Valid range is 0–100; default is 50.
3. Watch the **Level** gauge above the slider. Keep peaks below 0 dBFS (the gauge turns red above 0). Aim for peaks in the −10 to −6 dBFS region during normal speech.
4. To add the accessory connector input to the mix, click **+ACC** so it lights green. Click it again to disable the mix.

## What each control does

| Control | Kind | Default | Range | Persisted key |
|---|---|---|---|---|
| **Mic gain** | Slider | 50 | 0–100 | `PcMicGain` (when Mic source is PC) |
| **+ACC** | Toggle button | — | On / Off | — |
| **Level** | Meter | — | −40 to +10 dBFS (red above 0) | — |

## Tips

- When **Mic source** is set to **PC**, the radio does not report the mic level back from firmware. AetherSDR stores the **Mic gain** value locally using `PcMicGain` and restores it on the next session. For all other sources (MIC, BAL, LINE, ACC) the radio holds the value.
- **+ACC** mixes the ACC input on top of whatever source is selected in **Mic source**. It does not replace the primary source.
- The **Compression** gauge shows how much reduction the speech processor is applying. If the gauge never moves, the speech processor (PROC) is off.

## Troubleshooting

- **Mic gain slider has no effect and the Level gauge stays at −150** — The radio is not transmitting and `met_in_rx` monitoring is off. The Level gauge is suppressed to −150 dBFS in that state. Key the transmitter briefly to confirm the slider is working.
- **Mic gain value resets to 50 after reconnecting** — This only affects the **PC** source. The value is saved in `PcMicGain`. If the slider is reset, the stored setting may not have been written before the session ended. Reconnect and set the level again.
- **+ACC button has no visible effect on the audio** — Confirm that the accessory connector has an active audio signal and that the radio's ACC input is physically connected.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

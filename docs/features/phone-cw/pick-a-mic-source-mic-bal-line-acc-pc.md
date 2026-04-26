# Pick a mic source (MIC, BAL, LINE, ACC, PC)

Select which physical or virtual microphone input the FLEX-8600 uses for transmission. The correct source depends on how your microphone or audio device is connected to the radio.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a voice mode (USB, LSB, AM, FM) so that the Phone sub-panel is visible in the Phone/CW applet.

## Steps

1. Locate the **P/CW** tray button on the right sidebar and confirm the Phone/CW applet is visible. If it is not, click the **P/CW** tray button to show it.
2. In the Phone sub-panel, find the **Mic source** combo box on the left side of the mic gain row.
3. Click **Mic source** and select one of the available options: **MIC**, **BAL**, **LINE**, **ACC**, or **PC**.

The selection takes effect immediately. The radio switches its transmit audio input to the chosen source.

## What each control does

| Control | Description | Default | Valid values | Setting key |
|---|---|---|---|---|
| **Mic source** | Selects the microphone input source sent to the radio. | — | MIC, BAL, LINE, ACC, PC | — |
| **Mic gain** | Adjusts the input level for the selected source (0–100). When **PC** is selected, the value is stored client-side because the radio always reports `mic_level=0` for that source. | 50 | 0–100 | `PcMicGain` (PC source only) |

## Tips

- When you select **PC**, the radio does not report a mic level back to AetherSDR. AetherSDR stores the **Mic gain** value locally using the `PcMicGain` setting and restores it on the next session.
- The **Mic source** combo box is populated from the radio's available input list. If your radio firmware exposes additional inputs, they will appear alongside the five standard options.

## Related

- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)

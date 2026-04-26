# Adjust mic gain and enable the accessory mix

Use this page to set the microphone input level and optionally blend in the accessory connector input on your FLEX-8600 while operating in a voice mode.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The active slice must be in a voice mode (USB, LSB, AM, FM, etc.) so that the Phone sub-panel is visible in the PhoneCwApplet.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet, if it is not already open.
2. Confirm the Phone sub-panel is displayed. If the active slice is in a CW mode, switch the slice to a voice mode first.
3. Locate the **Mic source** combo box. If you are using a PC microphone, select **PC** from the list. For other sources, see [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md).
4. Drag the **Mic gain** slider to set the desired input level. Watch the **Level** gauge: aim to keep peaks below 0 dBFS (the gauge turns red above 0).
5. To mix in the accessory connector input, click **+ACC** so it appears highlighted. Click it again to disable the mix.

## What each control does

| Control | Type | Default | Valid range | Persisted key | Behavior |
|---|---|---|---|---|---|
| **Level** | Meter | — | −40 to +10 dBFS (red above 0) | — | Shows microphone input peak level in dBFS. |
| **Mic gain** | Slider | 50 | 0–100 | `PcMicGain` | Adjusts mic input level. When **Mic source** is set to **PC**, the value is stored client-side; the radio always reports mic_level=0 for PC source. |
| **+ACC** | Toggle button | — | On / Off | — | Enables the accessory mic input mix. |

## Tips

- When **Mic source** is **PC**, the radio does not report the mic level back to AetherSDR. The **Mic gain** value is saved locally in `PcMicGain` and restored on the next session.
- Use the **Level** gauge while speaking to verify the gain setting before transmitting. Peaks that consistently hit the red region (above 0 dBFS) indicate the **Mic gain** is too high.
- **+ACC** can be active at the same time as any other mic source, allowing you to blend an accessory-connected audio device with the primary source.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Select a mic profile for a specific microphone](select-a-mic-profile-for-a-specific-microphone.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
- [Listen to a TX sidetone monitor](listen-to-a-tx-sidetone-monitor.md)

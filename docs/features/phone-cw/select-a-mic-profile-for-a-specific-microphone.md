# Select a mic profile for a specific microphone

The **Mic profile** combo box loads a named transmit processing profile stored on the radio, letting you switch quickly between EQ and processing presets optimised for different microphones.

## Before you start

- AetherSDR must be connected to the radio. The **Mic profile** list is populated from the radio; it is empty when disconnected.
- The active slice must be in a phone mode (USB, LSB, AM, FM). The Phone panel is not shown when the slice is in CW mode.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet, if it is not already visible.
2. Confirm the Phone panel is showing. If the CW panel is displayed instead, switch the active slice to a phone mode.
3. Click the **Mic profile** combo box. The list is populated from the profiles stored on the radio.
4. Select the profile name that matches your microphone. AetherSDR immediately loads that profile on the radio.

## What each control does

| Control | Kind | Behavior | Default | Range | Setting key |
|---|---|---|---|---|---|
| **Mic profile** | Combo box | Loads the named mic processing profile on the radio. | — | Populated from radio | — |

## Tips

- Profile names are defined on the radio, not in AetherSDR. To create, rename, or delete profiles, use `Profiles > Profile Manager...`.
- After selecting a profile, check the **Level** gauge (−40 to +10 dBFS, red above 0) and the **Compression** gauge (−25 to 0 dB) to verify the profile settings suit your microphone.
- If your mic source is **PC**, the radio always reports a mic level of 0. Use the **Mic gain** slider (0–100, default 50) to set gain client-side; this value is persisted as `PcMicGain`.

## Troubleshooting

- **The Mic profile combo box is empty** — The radio has no mic profiles defined, or AetherSDR is not connected. Check the connection via `Settings > Connect to Radio...`, then create a profile using `Profiles > Profile Manager...`.
- **The Phone panel is not visible; the CW panel is shown instead** — The active slice is in a CW mode. Switch the slice to a phone mode to reveal the Phone panel and the **Mic profile** control.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)

# Select a mic profile for a specific microphone

The Phone/CW applet lets you load a named mic processing profile stored on the radio. Use this when switching between microphones that need different EQ or gain characteristics.

## Before you start

- AetherSDR must be connected to the radio. The "Mic profile" combo box is only populated when a radio connection is active.
- The active slice must be in a Phone mode (SSB, AM, FM). In CW mode the Phone panel is hidden and "Mic profile" is not visible.
- Mic profiles must already exist on the radio. AetherSDR reads the list from the radio; it does not create or edit profiles.

## Steps

1. Click the **P/CW** tray button in the right sidebar to open the Phone/CW applet.
2. Confirm the Phone panel is showing (not the CW panel). If the CW panel is visible, switch the active slice to a voice mode.
3. Click the **Mic profile** combo box at the top of the Phone panel.
4. Select the profile name that matches your microphone.

The radio loads the selected profile immediately.

## What each control does

| Control | Kind | Behavior | Default | Valid values | Setting key |
|---|---|---|---|---|---|
| Mic profile | Combo box | Loads the named mic processing profile on the radio. The list is populated from the radio. | — | Names provided by the radio | — |

## Tips

- The "Mic profile" list reflects profiles stored on the radio. If a profile you expect is missing, create it using SmartSDR or the radio's own profile management before connecting AetherSDR.
- Changing the profile does not affect the **Mic gain** slider value. If you use the **PC** source, the gain is stored locally as `PcMicGain` (default 50, range 0–100) and is independent of the profile.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)

# Select a mic profile for a specific microphone

Use the "Mic profile" combo box in the Phone/CW applet to load a named microphone processing profile stored on the radio. Different microphones often need different EQ and processing settings; switching profiles applies the correct configuration for the connected mic without adjusting each parameter manually.

## Before you start

- AetherSDR must be connected to the radio. The "Mic profile" combo box is only populated when a connection is active.
- The active slice must be in a voice mode (SSB, AM, FM). The Phone/CW applet shows the Phone sub-panel in voice modes; in CW mode the mic profile controls are not visible.

## Steps

1. Click the "P/CW" tray button in the right sidebar to open the Phone/CW applet, if it is not already visible.
2. Confirm that the Phone sub-panel is displayed. If the applet shows CW controls, the active slice is in a CW mode — switch the slice to a voice mode first.
3. Click the "Mic profile" combo box. The list is populated from the profiles stored on the radio.
4. Select the profile name that matches your microphone. The profile loads immediately.

## What each control does

| Control | Kind | Behavior | Default | Valid values | Setting key |
|---|---|---|---|---|---|
| Mic profile | Combo box | Loads the named mic processing profile on the radio. | — | Populated from the radio's mic profile list. | — |

## Tips

- The available profile names come from the radio, not from AetherSDR. To create or rename profiles, use the radio's own profile management. In AetherSDR you can also open `Profiles > Profile Manager...` to manage transmit profiles.
- Selecting a profile does not change the "Mic source" or "Mic gain" settings; adjust those separately if needed.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)

# Select a mic profile for a specific microphone

The Phone/CW applet lets you load a named mic processing profile stored on the radio. Use this when switching between microphones that need different EQ, compression, or gain settings.

## Before you start

- AetherSDR must be connected to the radio. The "Mic profile" combo box is populated from the radio's profile list and will be empty with no connection.
- The active slice must be in a Phone mode (SSB, AM, FM). In CW mode the applet shows CW controls instead of Phone controls.

## Steps

1. Open the Applet Panel if it is not visible. Click the **P/CW** tray button on the right sidebar, or use `View > Applet Panel` to make the panel visible.
2. Confirm the Phone sub-panel is showing. If the CW controls are displayed, the active slice is in CW mode — switch the slice to a voice mode first.
3. Locate the **Mic profile** combo box. It appears directly below the Level and Compression gauges, above the **Mic source** row.
4. Click the **Mic profile** combo box and select the profile name that matches your microphone.

The radio loads the selected profile immediately.

## What each control does

| Control | Kind | Behavior | Default | Valid range | Setting key |
|---|---|---|---|---|---|
| Mic profile | Combo box | Loads the named mic processing profile on the radio. | — | Populated from radio profile list | — |

## Tips

- Profiles are stored on the radio, not in AetherSDR. To create or delete profiles, use `Profiles > Profile Manager...`.
- After switching profiles, watch the **Level** gauge (−40 to +10 dBFS, red above 0) to confirm the new profile's gain is appropriate for your microphone.
- If you use a PC microphone (Mic source set to **PC**), the mic gain value is kept client-side as `PcMicGain` and is not affected by the profile load.

## Troubleshooting

- **"Mic profile" combo box is empty** — The radio has no saved mic profiles, or AetherSDR is not connected. Check the connection status, then use `Profiles > Profile Manager...` to create at least one profile.
- **Selecting a profile has no audible effect** — Verify that **Mic source** is set to the input your microphone is physically connected to. A profile loaded for one source will not alter processing on a different source.

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)

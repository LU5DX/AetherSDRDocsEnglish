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

| Control     | Kind      | Behavior                                             |
|-------------|-----------|------------------------------------------------------|
| Mic profile | Combo box | Loads the named mic processing profile on the radio. |

## Tips

- The available profile names come from the radio, not from AetherSDR. To create or rename profiles, use the radio's own profile management. In AetherSDR you can also open `Profiles > Profile Manager...` to manage transmit profiles.
- Selecting a profile does not change the "Mic source" or "Mic gain" settings; adjust those separately if needed.

## CW sidetone behavior (v0.9.2.1)

In v0.9.2.1 the separate "Local STn" button, local sidetone volume slider, "Follow" pitch toggle, and manual local pitch slider have been removed. The single **Sidetone** toggle and **Sidetone volume** slider in the CW panel now control both the radio's DAX-fed monitor and the client-side low-latency sidetone generator (CwSidetoneGenerator, ~10 ms latency) in lockstep. There are no longer any independent local-sidetone controls or associated settings keys (`CwLocalSidetoneEnabled`, `CwLocalSidetoneVolume`, `CwLocalSidetonePitchFollow`, `CwLocalSidetonePitchHz`).

Pitch and pan continue to follow the radio's `cw_pitch` and `mon_pan_cw` settings automatically; no manual override is needed or available.

## Changes in v0.9.3

### Level gauge — PC mic source exception

Previously the Level gauge was suppressed to −150 dBFS whenever `met_in_rx` was off and the radio was not transmitting, regardless of mic source. Starting in v0.9.3, this suppression no longer applies when the selected mic source is **PC**. Because PC-source metering is driven by client-side audio rather than the radio's `met_in_rx` flag, the gauge now appears immediately on connect when the mic source is set to PC (#2086).

No change in behavior occurs for hardware mic sources (MIC, BAL, LINE, ACC); those continue to be suppressed when `met_in_rx` is off and the radio is not transmitting.

### VOX toggle now refreshes the Phone panel instantly

Toggling VOX via a keyboard shortcut now causes the Phone panel to refresh immediately. Previously, the panel did not update until some other UI event occurred. This was corrected by having the VOX setters emit `phoneStateChanged` (#2084).

### Sidetone stream on Windows

On Windows, the client-side sidetone stream (CwSidetoneGenerator) now starts correctly as soon as AetherSDR connects to the radio. A bug in the AudioEngine initialization order prevented the stream from starting until the applet was interacted with manually (#2105).

## Related

- [Pick a mic source (MIC, BAL, LINE, ACC, PC)](pick-a-mic-source-mic-bal-line-acc-pc.md)
- [Adjust mic gain and enable the accessory mix](adjust-mic-gain-and-enable-the-accessory-mix.md)
- [Enable speech processor at NOR, DX, or DX+ level](enable-speech-processor-at-nor-dx-or-dx-level.md)
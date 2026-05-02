# Enable squelch from the VFO panel

Squelch mutes audio for a slice when the received signal falls below a set threshold. Use this to silence background noise on FM, AM, or digital modes when no signal is present.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is not, click the VFO marker flag on the spectrum display for that slice.
- If the VFO panel is collapsed to the frequency-only strip, click it once to expand it.

## Steps

1. Open the VFO panel by clicking the VFO marker flag on the spectrum display for the slice you want to configure.
2. Click the **Audio** tab inside the VFO panel.
3. Click the **Squelch button** to enable squelch. The button activates and squelch is applied to the slice immediately.
4. Drag the adjacent squelch slider left or right to set the threshold. The valid range is 0–100.

To disable squelch, click the **Squelch button** again.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| Squelch button | Off | On / Off | Enables or disables squelch for this slice. |
| Squelch slider | — | 0–100 | Sets the squelch threshold. Higher values require a stronger signal to open the squelch. |

Neither the button state nor the slider position is persisted as an AetherSDR AppSettings key — both reflect live radio state.

## Tips

- Set the slider just above the noise floor to prevent the audio from cutting in and out on weak signals.
- The squelch threshold interacts with the AGC setting. If you change the AGC mode using the **AGC combo**, you may need to readjust the squelch slider.

## Related

- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [VFO Panel overview](overview.md)

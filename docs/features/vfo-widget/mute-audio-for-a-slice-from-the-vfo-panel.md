# Mute audio for a slice from the VFO panel

Silence the audio output of a single slice without changing its AF Gain setting. Use this when you want to suppress a slice temporarily and restore its previous volume with one click.

## Before you start

- AetherSDR must be connected to a FLEX-8600 radio.
- The VFO panel for the target slice must be open. If it is collapsed to a frequency-only strip, click anywhere on it to expand it first.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to mute. The VFO panel opens anchored to the marker.
2. Click **Audio** to select the Audio tab inside the VFO panel.
3. Click **Mute**. The button activates, and audio output for the slice stops. The AF Gain slider value is not changed.
4. To restore audio, click **Mute** again. The button deactivates and audio resumes at the previous AF Gain level.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| Mute button (Audio tab) | Toggle button | Off | Mutes audio output for this slice without changing the AF Gain setting. Click again to unmute. |
| AF Gain slider (Audio tab) | Slider | 100 | Sets the audio output level for this slice (0–100). Unaffected by Mute. |

## Tips

- Muting a slice does not reset the AF Gain slider. When you unmute, audio returns at the same level it was before.
- If you want to silence a slice permanently rather than temporarily, drag the AF Gain slider to 0 instead.

## Related

- [Adjust AF gain and pan from the VFO panel](adjust-af-gain-and-pan-from-the-vfo-panel.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)

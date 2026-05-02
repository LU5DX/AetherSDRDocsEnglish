# Adjust AF gain and pan from the VFO panel

Use the Audio tab in the VFO panel to set the audio output level and stereo pan position for any receive slice independently of other slices.

## Before you start

- AetherSDR must be connected to the radio. The VFO panel requires an active radio connection.
- The VFO panel for the target slice must be open. If it is collapsed to a frequency-only strip, click anywhere on the collapsed strip to expand it.

## Steps

1. Click the VFO marker flag on the spectrum display for the slice you want to adjust. The VFO panel opens anchored to the marker.
2. Click the **Audio** tab inside the VFO panel.
3. To set the audio output level, drag the **AF Gain slider** left or right. The default is 100; the valid range is 0–100.
4. To set the stereo position, drag the **Pan slider** left or right. The default is 50 (centre); the valid range is 0–100. A value below 50 moves audio toward the left channel; above 50 toward the right.

## What each control does

| Control | Default | Range | Behavior |
|---|---|---|---|
| AF Gain slider (Audio tab) | 100 | 0–100 | Sets the audio output level for this slice. Not persisted — reflects live radio state. |
| Pan slider (Audio tab) | 50 | 0–100 | Sets left/right stereo pan for this slice. 50 = centre. |

## Tips

- Double-clicking either slider resets it to its default value: 100 for AF Gain, 50 for Pan.
- AF gain is per-slice. Adjusting one slice does not affect any other slice.
- To silence a slice without moving the AF Gain slider, use the **Mute button** on the Audio tab instead. Muting does not change the stored gain value.

## Related

- [Mute audio for a slice from the VFO panel](mute-audio-for-a-slice-from-the-vfo-panel.md)
- [Enable squelch from the VFO panel](enable-squelch-from-the-vfo-panel.md)
- [Collapse the VFO panel to frequency-only view](collapse-the-vfo-panel-to-frequency-only-view.md)
- [VFO Panel overview](overview.md)

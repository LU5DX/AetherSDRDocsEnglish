# Enable Snap to Step for precise S-History tuning

Snap to Step rounds S-History click-to-tune to the nearest multiple of the active slice’s step size, hiding small carrier offsets. Enable it when you want to tune precisely to the frequency where a signal should be heard, rather than where its carrier appears.

## Before you start

- Signal History must be enabled (see [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter.md)).

## Steps

1. Open **Settings > SpotHub...**.
2. Click the **Display** tab.
3. Scroll to the **Signal History** section.
4. Click **Snap to Step** to enable it (toggle fills green when checked).

## What each control does

| Control | Default | Valid range | Setting key |
|---|---|---|---|
| Snap to Step | Disabled | On / Off | `SHistorySnapToStep` |

## Tips

- Snap to Step only affects clicks on Signal History markers — it does not change how the slice tunes when you click the spectrum directly.
- The Filter Match Window slider and the Edge Threshold, Marker Lifetime, and QRM Gate sliders all support left-double-click to reset to their stored default value.
- The SpotHub dialog now uses your current theme colors for the status labels and tab styling. Connected status appears in the accent color, disconnected in the label color, and error messages in the danger accent color.

## Troubleshooting

- **Clicking a Marker still tunes to the exact carrier frequency** — Make sure the **Snap to Step** toggle shows a green fill. If it’s still gray, click it once to enable.

## Related

- [Toggle Signal History voice markers on the panadapter](toggle-signal-history-voice-markers-on-the-panadapter.md)
- [Adjust S-History marker lifetime, QRM gate and edge threshold](adjust-s-history-marker-lifetime-qrm-gate-and-edge-threshold.md)
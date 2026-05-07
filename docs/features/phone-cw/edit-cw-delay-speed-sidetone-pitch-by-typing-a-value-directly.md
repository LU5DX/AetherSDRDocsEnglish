# Edit CW Delay / Speed / Sidetone / Pitch by typing a value directly

Type a precise number directly into any of the four CW value fields (Delay, Speed, Sidetone Volume, Pitch) instead of dragging a slider or clicking step buttons. This matches native SmartSDR behavior and is useful when you already know the exact value you want.

## Before you start

- Ensure the active slice is in CW mode (the Phone/CW applet auto-switches to CW controls).

## Steps

1. Click the **P/CW** tray button on the right sidebar if the Phone/CW applet isn't visible.
2. Locate the CW control you want to edit: **Delay**, **Speed**, **Sidetone volume**, or **Pitch**. Each is next to its corresponding slider.
3. Click inside the number field (a QLineEdit). The field will show a text cursor.
4. Type the desired value using your keyboard.
5. Press **Enter** or click elsewhere to apply the value.

## What each control does

| Control | Default | Valid range | Setting key | Behavior |
|---|---|---|---|---|
| **Delay** | 500 | 0–2000 ms (step 10) | — | Sets CW break-in delay. |
| **Speed** | 20 | 5–100 WPM | — | Sets CW keying speed. |
| **Sidetone volume** | 50 | 0–100 | — | Sets CW monitor volume (affects both radio and local sidetone). |
| **Pitch** | 600 | 100–6000 Hz (step 10) | — | Sets CW pitch/sidetone frequency. |

## Troubleshooting

- **Typed value snaps back to previous value** — The radio may have rejected the value. Ensure your entry is within the valid range shown above. For Delay values, the radio emission no longer snaps the slider back in v0.9.8 (#2428).

## Related

- [Set CW break-in delay](set-cw-break-in-delay.md)
- [Set CW keying speed in WPM](set-cw-keying-speed-in-wpm.md)
- [Change CW pitch / sidetone frequency](change-cw-pitch-sidetone-frequency.md)
- [Enable the low-latency CW sidetone (Sidetone button drives both radio and local path)](enable-the-low-latency-cw-sidetone-sidetone-button-drives-both-radio-and-local-path.md)

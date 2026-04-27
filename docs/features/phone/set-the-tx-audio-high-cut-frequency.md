# Set the TX audio high-cut frequency

Use the Phone applet to raise or lower the upper boundary of the TX audio passband. Narrowing the high-cut reduces transmitted bandwidth; raising it passes more high-frequency audio content.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet requires an active radio connection.
- The radio must be in a phone mode (SSB, AM, or similar) for TX filter changes to have audible effect.

## Steps

1. If the Phone applet is not visible, click the **PHNE** tray button in the right sidebar to show it.
2. Locate the **High Cut** column on the right side of the TX filter section, below the DEXP row.
3. Click **>** to increase the high-cut frequency by 50 Hz, or click **<** to decrease it by 50 Hz. You can also scroll the mouse wheel over the value display to step in either direction.
4. Read the current value in the numeric display between the **<** and **>** buttons.

## What each control does

| Control | Description | Default | Valid range |
|---|---|---|---|
| **High Cut `<`** | Decreases the TX filter high-cut frequency by one step. | — | — |
| **High Cut `>`** | Increases the TX filter high-cut frequency by one step. | — | — |
| High Cut value display | Shows the current high-cut frequency in Hz. | 3300 Hz | (low-cut + 50) to 10000 Hz, in 50 Hz steps |

The high-cut frequency cannot be set below the current low-cut frequency plus 50 Hz. For example, if low-cut is set to 100 Hz, the minimum high-cut value is 150 Hz.

## Tips

- Each click of **<** or **>** moves the frequency by exactly 50 Hz. For larger changes, hold the mouse button down or use the scroll wheel with rapid movement.
- A typical SSB passband uses a low-cut of 50 Hz and a high-cut of 3300 Hz. Reducing high-cut to around 2700–2800 Hz can improve intelligibility in noisy conditions by removing high-frequency hiss.
- The high-cut setting is not persisted by AetherSDR's local settings — it is sent directly to the radio and stored in the radio's active profile.

## Related

- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Phone overview](overview.md)

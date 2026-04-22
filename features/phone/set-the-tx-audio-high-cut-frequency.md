# Set the TX audio high-cut frequency

Use the Phone applet to raise or lower the upper boundary of the TX audio passband. Narrowing the high-cut removes unnecessary high-frequency content; widening it can improve audio clarity on wide-bandwidth modes.

## Before you start

- AetherSDR must be connected to the radio. The Phone applet is disabled without a radio connection.
- The radio must be in a phone mode (SSB, AM, or similar) for TX filter changes to take effect on air.

## Steps

1. If the Phone applet is not visible, click the **PHNE** tray button on the right sidebar to show it.
2. Locate the **High Cut** column on the right side of the TX filter section at the bottom of the Phone applet.
3. Click **>** to increase the high-cut frequency by 50 Hz, or click **<** to decrease it by 50 Hz. Alternatively, scroll the mouse wheel over the value display to step in either direction.
4. Read the current value in the numeric display between the **<** and **>** buttons.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| **High Cut `<`** | — | Steps down by 50 Hz | Decreases the TX filter high-cut frequency by 50 Hz per click. |
| **High Cut `>`** | — | Steps up by 50 Hz | Increases the TX filter high-cut frequency by 50 Hz per click. |
| High Cut value display | 3300 Hz | (low-cut + 50) to 10000 Hz, step 50 Hz | Shows the current high-cut frequency in Hz. Also accepts mouse wheel input. |

The high-cut frequency cannot be set lower than the current low-cut frequency plus 50 Hz, and cannot exceed 10000 Hz.

## Tips

- For standard SSB voice, a high-cut of 2800–3300 Hz is typical. Values above 3300 Hz pass more audio bandwidth but increase occupied spectrum.
- Adjust **Low Cut** first if you want a narrow or shaped passband, then set **High Cut** to maintain the minimum 50 Hz separation.

## Related

- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Phone overview](overview.md)

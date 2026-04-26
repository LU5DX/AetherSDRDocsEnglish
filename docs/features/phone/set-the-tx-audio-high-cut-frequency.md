# Set the TX audio high-cut frequency

Use the Phone applet to raise or lower the upper edge of the TX audio passband. Narrowing the high-cut removes high-frequency hiss; widening it improves audio fidelity on modes that support it.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Make sure the applet panel is visible. If it is not, click the PHNE tray button on the right sidebar, or go to `View > Applet Panel`.

## Steps

1. Click the **PHNE** tray button on the right sidebar to open the Phone applet.
2. Locate the **High Cut** section in the TX filter area at the bottom of the applet.
3. Click **>** to increase the high-cut frequency by 50 Hz, or click **<** to decrease it by 50 Hz.
   - Alternatively, hover over the frequency value and scroll the mouse wheel to step in the same 50 Hz increments.
4. Read the current value from the numeric display between the **<** and **>** buttons.

## What each control does

| Control | Default | Valid range | Notes |
|---|---|---|---|
| **High Cut `<`** | — | Steps down by 50 Hz | Cannot go below (low-cut + 50) Hz |
| **High Cut `>`** | — | Steps up by 50 Hz | Upper limit is 10000 Hz |
| High Cut value display | 3300 Hz | (low-cut + 50) to 10000, step 50 Hz | Read-only numeric display; also accepts mouse wheel |

## Tips

- The high-cut floor is always 50 Hz above the current low-cut value. If the high-cut will not step down further, lower the low-cut first.
- For standard SSB voice, a high-cut of 2800–3000 Hz reduces splatter on adjacent channels while keeping speech intelligible.

## Related

- [Set the TX audio low-cut frequency](set-the-tx-audio-low-cut-frequency.md)
- [Phone overview](overview.md)

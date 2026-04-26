# Set the TX audio low-cut frequency

Use the Phone applet to raise or lower the low-cut edge of the TX audio filter. Narrowing the low end reduces low-frequency noise and rumble on SSB and other phone modes.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Open the Applet Panel if it is not already visible. If the panel is hidden, click the PHNE tray button on the right sidebar to show it.

## Steps

1. Click the PHNE tray button on the right sidebar to open the Phone applet.
2. Locate the **Low Cut** section in the lower part of the applet. It shows a header labeled "Low Cut" above a row containing a value display and two triangle step buttons.
3. Click `<` to decrease the low-cut frequency by 50 Hz, or `>` to increase it by 50 Hz. Alternatively, hover over the value display and scroll the mouse wheel to step in the same increments.
4. Read the current frequency in Hz from the value display between the two buttons.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| `<` (Low Cut) | — | — | Decreases TX low-cut frequency by 50 Hz per click. Minimum is 0 Hz. |
| `>` (Low Cut) | — | — | Increases TX low-cut frequency by 50 Hz per click. Maximum is (high-cut − 50) Hz. |
| Low Cut value display | 50 Hz | 0 to (high-cut − 50), step 50 Hz | Shows the current low-cut frequency. Supports mouse-wheel adjustment. |

The low-cut value is not persisted in AetherSDR's settings; it is held by the radio.

## Tips

- The low-cut frequency cannot meet or exceed the high-cut frequency. The upper limit is always 50 Hz below the current high-cut value. If the `>` button has no effect, you have reached that ceiling.
- A typical SSB low-cut starting point is 100–150 Hz, which removes low-frequency hum without noticeably affecting voice clarity.

## Related

- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
- [Phone overview](overview.md)

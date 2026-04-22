# Set the TX audio low-cut frequency

Use this page to raise or lower the low-cut edge of the TX audio filter in the Phone applet. Adjusting the low-cut removes rumble, breath noise, or low-frequency interference from your transmitted audio.

## Before you start

- Connect to a FLEX-8600 radio. The Phone applet requires an active radio connection.
- Confirm the Phone applet is visible in the Applet Panel. If it is not, click the PHNE tray button on the right sidebar.

## Steps

1. Locate the **Low Cut** spinbox in the Phone applet. It appears as a header labeled "Low Cut" above a row of controls showing a `<` button, a frequency value, and a `>` button.
2. Click `<` to decrease the low-cut frequency by 50 Hz, or click `>` to increase it by 50 Hz.
3. Alternatively, position the mouse pointer over the frequency value label and scroll the mouse wheel to step the value up or down by 50 Hz.
4. Confirm the displayed value reflects the frequency you want.

## What each control does

| Control | Default | Valid range | Behavior |
|---|---|---|---|
| `<` (Low Cut) | — | — | Decreases TX filter low-cut by 50 Hz per click. |
| `>` (Low Cut) | — | — | Increases TX filter low-cut by 50 Hz per click. |
| Low-cut value display | 50 Hz | 0 Hz to (high-cut − 50 Hz), step 50 Hz | Shows the current TX filter low-cut frequency in Hz. Also responds to mouse wheel. |

## Tips

- The low-cut value cannot meet or exceed the current high-cut value. The upper limit is always the current high-cut setting minus 50 Hz.
- To cut more low-frequency content — for example, to reduce mic stand vibration on SSB — increase the low-cut value toward 200–300 Hz.

## Related

- [Set the TX audio high-cut frequency](set-the-tx-audio-high-cut-frequency.md)
- [Phone overview](overview.md)

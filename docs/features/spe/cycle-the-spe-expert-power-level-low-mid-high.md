# Cycle the SPE Expert power level (Low, Mid, High)

This page shows you how to cycle the SPE Expert amplifier's output power level between Low, Mid, and High, matching the front-panel POWER key on the amplifier.

## Before you start

- Connect to and configure your SPE Expert amplifier in the SPE applet. See [SPE Expert Amplifier overview](overview.md).
- Ensure the amplifier is powered on and responding — the POWER button is disabled while the amplifier is silent.

## Steps

1. Open the SPE applet: **Applet panel > SPE tile**.
2. Locate the **PWR** button in the first button row. The label shows the current power level (LOW, MID, or HIGH) once the applet knows it.
3. Click **PWR** to cycle to the next level. The button label updates to show the new level.

## What each control does

- **PWR** — Displays the current output power level (LOW, MID, or HIGH) and cycles to the next level when clicked. Mirrors the amplifier's front-panel POWER key. The button label shows the current level; clicking advances to the next one.

## Tips

- The button is labeled **PWR**, not "POWER" — this is to keep all five buttons in the row from clipping at the applet's default width.
- If the button shows no level text, the applet hasn't yet received the current level from the amplifier. Clicking will still cycle the level.

## Troubleshooting

- **PWR button is greyed out** — The amplifier isn't responding or is in a silent state. Verify the serial or ser2net connection and that the amplifier is powered on. Use **ON** to power it up if needed.

## Related

- [SPE Expert Amplifier overview](overview.md)
- [Monitor forward power and SWR on the SPE Expert amplifier](monitor-forward-power-and-swr-on-the-spe-expert-amplifier.md)
- [Put the SPE Expert amplifier in Operate or Standby](put-the-spe-expert-amplifier-in-operate-or-standby.md)
- [Tune the SPE Expert amplifier](tune-the-spe-expert-amplifier.md)

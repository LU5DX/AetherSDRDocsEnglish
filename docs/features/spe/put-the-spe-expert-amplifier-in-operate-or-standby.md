# Put the SPE Expert amplifier in Operate or Standby

This page shows you how to switch your SPE Expert linear amplifier between Operate and Standby from the SPE Amplifier applet.

## Before you start

- The amplifier must be connected via serial or ser2net TCP and powered ON.
- You must be connected to a FLEX-8600 radio.

## Steps

1. Open the applet panel and click the **SPE** tile.
2. Click **OPER** to switch the amplifier from Standby to Operate.
3. Click **OPER** again to switch back to Standby.

The status pill at the top of the applet shows the current mode: `OPR · RX` when operating and receiving, `OPR · TX` when operating and transmitting, or `STANDBY` when in standby.

## What each control does

| Control | Default | Behavior | Setting key |
|---|---|---|---|
| **OPER** | STBY | Toggles between Operate and Standby (mirrors the front-panel OPERATE key). | None |
| **Status** pill | — | Shows the current mode as `OPR · RX`, `OPR · TX`, or `STANDBY`. | None |

## Tips

- Use Standby when you want to run barefoot (without the amplifier) without powering the amp down.
- The **OPER** button is disabled while the amplifier is silent; power the amp on with **ON** first if needed.

## Related

- [SPE Expert Amplifier overview](overview.md)
- [Monitor forward power and SWR on the SPE Expert amplifier](monitor-forward-power-and-swr-on-the-spe-expert-amplifier.md)
- [Cycle the SPE Expert power level (Low, Mid, High)](cycle-the-spe-expert-power-level-low-mid-high.md)
- [Tune the SPE Expert amplifier](tune-the-spe-expert-amplifier.md)

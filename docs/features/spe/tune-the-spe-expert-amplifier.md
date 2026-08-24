# Tune the SPE Expert amplifier

Run an ATU tuning cycle on your SPE Expert linear amplifier (1.3K-FA, 1.5K-FA, 2K-FA) directly from AetherSDR, without touching the amplifier's front panel.

## Before you start

- Connect to your FLEX-8600 radio (the SPE applet requires an active radio connection).
- Ensure the SPE Expert amplifier is connected via serial or ser2net TCP and appears in the Applet panel.
- Open the SPE applet: **Applet panel > SPE tile**.

## Steps

1. Click **ON** to power the amplifier if it is not already on.
2. Click **OPER** to switch the amplifier from STANDBY to OPERATE mode. The status pill should read **OPR · RX**.
3. If needed, cycle **PWR** to select your desired power level (LOW, MID, or HIGH). The button label shows the current level.
4. Click **TUNE** to start the ATU tuning cycle. The amplifier keys TX and runs its tuning routine with RF drive.

The tuning cycle completes automatically. Watch the **ATU SWR** gauge settle to confirm the match.

## What each control does

| Control | Behavior |
| --- | --- |
| **ON** | Powers the amplifier on by pulsing the serial control lines. Over the network, this requires an rfc2217-enabled ser2net port. |
| **OPER** | Toggles between STANDBY and OPERATE (mirrors front-panel OPERATE key). |
| **PWR** | Cycles output power level LOW → MID → HIGH. Button label shows the current level. |
| **TUNE** | Starts ATU tuning (mirrors front-panel TUNE key). Keys TX during the cycle. |
| **OFF** | Switches the amplifier off. Use **ON** to power it back up. |
| **INPUT** | Toggles between input ports 1 and 2. |
| **ANT** | Cycles the TX antenna for the current band. |
| **▼ / ▲** | Lowers or raises the drive power the amplifier requests from the radio over CAT. |

## Tips

- The **ATU SWR** gauge shows SWR before the ATU; the **SWR** gauge shows the antenna-side SWR. After tuning, both should drop toward 1:1.
- The **TUNE** button is marked as a TX-keying control — ensure your band's tune power is set appropriately in **Settings > TX Band Settings...** before tuning.
- The amplifier follows your radio's band automatically; there are no band keys in the applet.

## Troubleshooting

- **TUNE is disabled (grayed out)** — The amplifier may be in STANDBY or OFF. Click **OPER** or **ON** first. Some keys disable while the amp is silent.
- **ON / OFF do nothing over the network** — These need an rfc2217-enabled ser2net port. Check your serial connection configuration in **Settings > Radio Setup...**.

## Related

- [SPE Expert Amplifier overview](overview.md)
- [Put the SPE Expert amplifier in Operate or Standby](put-the-spe-expert-amplifier-in-operate-or-standby.md)
- [Cycle the SPE Expert power level (Low, Mid, High)](cycle-the-spe-expert-power-level-low-mid-high.md)
- [Monitor forward power and SWR on the SPE Expert amplifier](monitor-forward-power-and-swr-on-the-spe-expert-amplifier.md)

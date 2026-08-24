# SPE Expert Amplifier overview

The SPE Expert Amplifier applet monitors and controls an SPE Expert linear amplifier (1.3K-FA, 1.5K-FA, 2K-FA) connected via serial or ser2net TCP, directly from the AetherSDR applet panel. It shows real-time forward power, antenna SWR, ATU SWR, supply voltage/current, and heatsink temperature on gauges and text readouts, and mirrors the amplifier's front-panel keys as buttons.

## Before you start

- Connect a supported SPE Expert amplifier to your radio via serial or ser2net TCP, and verify the connection is working in the Radio Setup.
- Connect to a FLEX-8600 radio. The applet requires an active radio connection.

## How it works

The applet opens from **Applet panel > SPE tile**. It polls the amplifier over the serial or TCP link and updates the gauges and readouts in real time (label text refreshes at 10 Hz). The applet detects the amplifier model on first poll and scales the forward-power gauge accordingly (default scale 0–1600 W for the 1.3K-FA, 1.5K-FA, and 2K-FA).

### Status readouts

| Control | Behavior |
|---|---|
| **Forward Power gauge** | Real-time forward power. Meter ballistics smooth the reading. Peak is held for 2.5 s before clearing. |
| **Antenna SWR gauge** | Real-time SWR at the antenna. Scale runs 1.0:1 to 3.0:1, with a warning marker at 2.0:1. |
| **ATU SWR gauge** | Real-time SWR at the ATU input. Scale runs 1.0:1 to 3.0:1, with a warning marker at 2.0:1. |
| **TEMP / V / I text** | Heatsink temperature (in the unit the amplifier's own display is configured for — C or F, with no C/F toggle), supply voltage, and supply current. |
| **Status pill** | Shows one of **OPR · TX**, **OPR · RX**, **STANDBY**, or a fault banner below the readouts. |

### Control buttons

The button row mirrors the amplifier's front-panel keys:

| Button | Behavior |
|---|---|
| **ON** | Pulses the serial control lines to power the amplifier on. Over the network, this requires an rfc2217-enabled ser2net port. Remains enabled while the amp is silent. |
| **OPER** | Toggles between Standby and Operate (front-panel OPERATE key). Disabled when the amp is silent. |
| **PWR** | Shows the current power level (LOW/MID/HIGH) once known; clicking cycles to the next level, mirroring the amplifier's POWER key. Disabled when the amp is silent. |
| **TUNE** | Starts ATU tuning (front-panel TUNE key). This keys the transmitter with RF drive. Disabled when the amp is silent. |
| **OFF** | Switches the amplifier off. Use **ON** to power it back up. Disabled when the amp is silent. |
| **INPUT** | Toggles input port 1 / 2. Disabled when the amp is silent. |
| **ANT** | Cycles the TX antenna for the current band. Disabled when the amp is silent. |
| **▼ / ▲** | Lowers / raises the drive power the amplifier requests from the radio over CAT (front-panel arrow keys). Disabled when the amp is silent. |

A **fault banner** appears in red across the full width when the amplifier reports a fault; the status pill shows **Fault** during this state. Buttons that would not function while the amplifier is silent are disabled to avoid sending invalid commands.

## Related

- [Monitor forward power and SWR on the SPE Expert amplifier](monitor-forward-power-and-swr-on-the-spe-expert-amplifier.md)
- [Put the SPE Expert amplifier in Operate or Standby](put-the-spe-expert-amplifier-in-operate-or-standby.md)
- [Cycle the SPE Expert power level (Low, Mid, High)](cycle-the-spe-expert-power-level-low-mid-high.md)
- [Tune the SPE Expert amplifier](tune-the-spe-expert-amplifier.md)

# Monitor forward power and SWR on the SPE Expert amplifier

Monitor real-time forward power, antenna SWR, and ATU input SWR from your SPE Expert amplifier (1.3K-FA, 1.5K-FA, 2K-FA) using the SPE applet in the applet panel.

## Before you start

- Your FLEX-8600 radio must be connected to AetherSDR.
- The SPE Expert amplifier must be connected via serial or ser2net TCP and powered on.
- The amplifier must have been polled at least once so the applet can detect the model and set the gauge scale.

## Steps

1. Open the applet panel by clicking the Applet Panel icon in the main toolbar.
2. Click the **SPE** tile to open the SPE Expert Amplifier applet.
3. Read the **Forward Power** gauge (labeled **PWR**) to see output power in watts. The gauge scale is set automatically from the model detected on first poll.
4. Read the **Antenna SWR** gauge (labeled **SWR**) to see real-time antenna-side SWR.
5. Read the **ATU SWR** gauge (labeled **ATU**) to see real-time SWR at the ATU input.
6. Check the **TEMP**, **V**, and **I** readouts for heatsink temperature, supply voltage, and supply current.
7. If a fault occurs, a banner appears at the top of the applet in red text describing the problem.

## What each control does

| Control | Type | Behavior |
|---------|------|----------|
| **Forward Power** (PWR) | Gauge | Real-time forward power in watts. Scale set from the detected model; 5 evenly spaced ticks. |
| **Antenna SWR** (SWR) | Gauge | Real-time antenna-side SWR, scale 1:1 to 3:1 with ticks at 1, 1.5, 2, 2.5, 3. |
| **ATU SWR** (ATU) | Gauge | Real-time SWR at the ATU input, same scale as antenna SWR. |
| **TEMP** | Text | Heatsink temperature, shown verbatim in the amplifier's own unit (C or F). |
| **V** | Text | Supply voltage in volts. |
| **I** | Text | Supply current in amperes. |
| **Status pill** | Indicator | Shows **OPR · TX**, **OPR · RX**, or **STANDBY** — the amplifier's operating mode. |
| **Fault banner** | Indicator | Appears in red text when the amplifier reports a fault condition. |

## Tips

- The **TEMP** readout uses whatever unit (Celsius or Fahrenheit) the amplifier's own display is configured for. AetherSDR does not convert it.
- The power gauge has ballistic smoothing; the peak value is held for 2.5 seconds after each transmission.

## Related

- [SPE Expert Amplifier overview](overview.md)
- [Put the SPE Expert amplifier in Operate or Standby](put-the-spe-expert-amplifier-in-operate-or-standby.md)
- [Tune the SPE Expert amplifier](tune-the-spe-expert-amplifier.md)

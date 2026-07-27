# Cross-Needle Meter overview

The Cross-Needle Meter displays forward and reflected RF power as two crossing needles on a classic analog-style meter face, with a computed SWR reading. It helps you monitor antenna match and power output at a glance, just like a traditional desk-top cross-needle SWR meter.

## Before you start

- A radio must be connected to AetherSDR.
- The Cross-Needle Meter requires an active radio connection to receive power and SWR data.

## How it works

The meter shows forward power (right needle) and reflected power (left needle) on the same calibrated meter face. Where the two needles cross indicates the SWR. The meter updates continuously in real time.

Open the meter from **Applet panel > Cross-Needle tile**.

## What each control does

| Control | Kind | Default | Behavior |
|---|---|---|---|
| Forward/Reflected needles | indicator | — | Dual-needle analog display: forward power (right needle) and reflected power (left needle) crossing to indicate SWR. |
| Peak hold | toggle button | Off | Holds the peak needle position for easier reading during SSB voice peaks. |
| Digital readout | indicator | — | Numeric forward power, reflected power and SWR values displayed below the meter. |
| Meter face theme | combo box | — | Select from preset meter face styles (classic black, white, military, etc.). |

## Tips

- Use Peak hold when operating SSB to capture voice peaks that are too brief to read on the analog meter.
- The digital readout below the meter provides exact numeric values for forward power, reflected power, and SWR, useful when the analog needle position is ambiguous.

## Related

- [Read forward and reflected power on the cross-needle meter](read-forward-and-reflected-power-on-the-cross-needle-meter.md)
- [Enable peak-hold for SSB voice peaks](enable-peak-hold-for-ssb-voice-peaks.md)
- [Change the meter face theme](change-the-meter-face-theme.md)

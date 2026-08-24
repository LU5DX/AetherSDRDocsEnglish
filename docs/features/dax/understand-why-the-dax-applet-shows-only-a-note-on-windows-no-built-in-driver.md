# Understand why the DAX applet shows only a note on Windows (no built-in driver)

This page explains why the DAX Audio applet displays only a note on Windows instead of the full set of meters and gain sliders, and what to use instead.

## Before you start

- You are running AetherSDR on Windows.
- You have a radio connection established (the applet is only available when connected).

## What happens on Windows

When you open the DAX Audio applet on Windows, it shows only this note:

> No built-in DAX driver on Windows.
> Use TCI, or SmartSDR DAX.

There is no **DAX Enable** button, no per-channel RX meter/sliders, and no TX gain control. All other DAX controls are omitted from the interface.

## Why this happens

AetherSDR does not ship a built-in DAX audio bridge for Windows. The DAX bridge requires a kernel-mode audio driver that AetherSDR provides only on macOS and Linux. Because the controls would have no effect without that driver, the Windows build shows only this explanatory note and nothing else.

DAX audio still works on Windows — it is provided by FlexRadio's own SmartSDR DAX drivers, which you can install separately. AetherSDR's on-screen DAX applet simply does not manage that path.

## What to use instead

On Windows, route slice audio to digital software using one of these alternatives:

- **SmartSDR DAX** — Install FlexRadio's DAX drivers and use the standard SmartSDR DAX channels.
- **TCI** — Enable the TCI server and connect your digital software (e.g., WSJT-X, fldigi) over the TCI protocol.

## Tips

- The **Autostart DAX with AetherSDR** setting (menu `Settings > Autostart DAX with AetherSDR`, AppSettings key `AutoStartDAX`) is also not applicable on Windows for the same reason.
- The Windows note is colored to stand out (amber text) and is pinned to the top of the applet panel.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

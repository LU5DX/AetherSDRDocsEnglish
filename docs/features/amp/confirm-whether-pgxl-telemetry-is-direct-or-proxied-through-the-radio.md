# Confirm whether PGXL telemetry is direct or proxied through the radio

This page helps you determine whether AetherSDR is reading Power Genius XL (PGXL) telemetry directly from the amplifier or through the FLEX-8600 radio proxy, and explains what data is available in each mode.

## Before you start

- A Power Genius XL amplifier must be connected and detected by AetherSDR.
- The Amplifier applet must be visible. If it isn't, toggle it with the **AMP** tray button on the right sidebar.

## Steps

1. Open the Amplifier applet by clicking the **AMP** tray button on the right sidebar.
2. Look at the **Source label** at the bottom-left of the applet.
   - **● RADIO** — telemetry is being proxied through the FLEX-8600 radio.
   - **● DIRECT** — telemetry is being read directly from the PGXL.

## What each control does

| Control | Behavior | Notes |
|---|---|---|
| **Source label** | Shows **● RADIO** or **● DIRECT** to indicate the telemetry path. | Vdd, Vac, and fan mode are only available on the DIRECT path. |
| **Vdd (drain voltage)** | Shows drain voltage as `Vdd  x.x V`. | Only updated on a direct connection. Shows a dash (`—`) when the drain supply is off (vdd < 1 V) or when connected via the radio proxy. Greyed out when proxied. |
| **Vac (mains voltage)** | Shows mains voltage as `Vac  N V`. | Only updated on a direct connection. Greyed out when proxied through the radio. |
| **Fan speed** | Dropdown with **STANDARD**, **CONTEST**, and **BROADCAST** options. | Hidden until a direct PGXL connection delivers the first fanmode status. |

## Tips

- When the **Source label** shows **● RADIO**, the missing Vdd/Vac/fan-mode controls are expected behavior — not a fault. Those values are only available on a direct connection.

## Related

- [Amplifier overview](overview.md)
- [Monitor forward power and SWR at the amplifier output](monitor-forward-power-and-swr-at-the-amplifier-output.md)
- [Watch PGXL temperature, drain current, and mains voltage](watch-pgxl-temperature-drain-current-and-mains-voltage.md)
- [Select the PGXL fan speed (Standard, Contest, Broadcast)](select-the-pgxl-fan-speed-standard-contest-broadcast.md)

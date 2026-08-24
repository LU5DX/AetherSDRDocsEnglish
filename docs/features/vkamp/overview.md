# VK3AMP Amplifier overview

The VK3AMP Amplifier applet monitors and controls a VK3AMP RF amplifier (600 W / 1000 W / 2000 W) connected to your radio over TCP with UDP telemetry. It shows forward power, reflected power, SWR, and supply current, plus antenna selection, bypass, cooling, reset, and fault indicators.

## Before you start

- A FLEX-8600 radio connection is required.
- The amplifier must be reachable over your network (TCP with UDP telemetry).

## How it works

Open the applet from **Applet panel > VKAMP tile**. The applet connects to the amplifier over TCP and receives live telemetry, which drives the gauges and status readouts. Controls send commands back over the same connection.

The applet is hardware-variant aware. The forward and reflected power gauges rescale to the selected variant's rated output, so a 2000 W unit shows a different full-scale range than a 600 W unit.

## What each control does

| Control | Type | Behavior |
|---|---|---|
| Forward Power | Indicator | Real-time forward power from the amplifier. Gauge rescales to the selected hardware variant's rated output. |
| Reflected Power | Indicator | Real-time reflected power. Gauge scales to 15% of the variant's rated output. |
| SWR | Indicator | Real-time standing-wave ratio, scaled 1.0 to 3.0. |
| Current | Indicator | Supply current text readout (labeled CURR). |
| Bypass | Push button (labeled BYPASS) | Toggles the amplifier between bypass and in-line. The label shows the current state, not the action. |
| Cooling | Push button (labeled COOLING) | Toggles the cooling override. |
| Antenna 1 / 2 / 3 | Push button | Selects the antenna port (1–3). The selection is read-only display until the amp confirms it. The amp's own table can revert a select within ~50 ms. |
| Voltage Low / High | Push button | Selects which voltage rail the live status reports. |
| Reset | Push button (hold-to-confirm) | Resets the amplifier. Hold to confirm. |
| Fault | Indicator | Fault state reported by the amplifier as a raw numeric code. Shows only when a fault is active. |

The applet also shows temperature (TEMP), supply voltage (SUPPLY), current (CURR), band (BAND), and antenna (ANT) in a text readout grid.

## Tips

- The bypass button label reflects the current state, not the action. When the amp is in-line, it shows the active state styling; when bypassed, it shows the bypass state.
- The antenna buttons are not optimistic — clicking asks the amplifier to switch, but the highlight only moves after the live status confirms. If the amp's internal table overrides the selection, the display reverts within about 50 ms.

## Troubleshooting

- **Fault banner shows** — The amplifier reports a fault with a raw numeric code. The applet displays the code; it does not map codes to names. Refer to your amplifier documentation for the code meaning.
- **Antenna selection reverts** — The amplifier's own antenna table can override your selection within ~50 ms. Check the amp's configured table for the current band.

## Related

- [Monitor forward and reflected power on the VK3AMP amplifier](monitor-forward-and-reflected-power-on-the-vk3amp-amplifier.md)
- [Bypass the VK3AMP amplifier](bypass-the-vk3amp-amplifier.md)
- [Select the VK3AMP antenna port](select-the-vk3amp-antenna-port.md)
- [Reset the VK3AMP amplifier](reset-the-vk3amp-amplifier.md)

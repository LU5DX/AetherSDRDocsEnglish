# Monitor forward and reflected power on the VK3AMP amplifier

View live forward power, reflected power, and SWR on the VK3AMP amplifier applet, along with supply current, so you can verify antenna performance and amplifier operation at a glance.

## Before you start

- The radio must be connected.
- The VK3AMP amplifier must be powered on, connected over TCP, and reporting telemetry.

## Steps

1. Open the applet panel.
2. Click the **VKAMP** tile to open the VK3AMP Amplifier applet.
3. Read the **Forward Power** gauge for real-time forward power. The gauge rescales to the selected hardware variant's rated output.
4. Read the **Reflected Power** gauge for real-time reflected power.
5. Read the **SWR** gauge for the standing-wave ratio.
6. Read the **CURR** text readout for supply current.

## What each control does

| Control | What it shows or does |
|---|---|
| **Forward Power** | Real-time forward power on a gauge. Rescales to the selected hardware variant's rated output (600 W / 1000 W / 2000 W). |
| **Reflected Power** | Real-time reflected power on a gauge. Full scale is 15% of the variant's rated output (e.g., 300 W on the 2000 W unit). |
| **SWR** | Standing-wave ratio on a gauge scaled 1:1 to 3:1. |
| **CURR** | Supply current as a text readout. |
| **TEMP** | Amplifier temperature as a text readout. |
| **SUPPLY** | Supply voltage as a text readout. Low/high rail selection is available via the **Voltage Low / High** buttons. |
| **Fault** | Fault state reported by the amplifier, shown as a raw numeric code when present. |

## Tips

- The **Forward Power** gauge's full scale adapts to the hardware variant you've selected in setup — a 600 W unit will show a smaller range than a 2000 W unit, so the needle stays readable.
- The **Reflected Power** gauge scales with the variant too, not a fixed 300 W — on a 600 W unit the full scale is 90 W, so low reflected power is still visible.

## Related

- [VK3AMP Amplifier overview](overview.md)
- [Bypass the VK3AMP amplifier](bypass-the-vk3amp-amplifier.md)
- [Select the VK3AMP antenna port](select-the-vk3amp-antenna-port.md)
- [Reset the VK3AMP amplifier](reset-the-vk3amp-amplifier.md)

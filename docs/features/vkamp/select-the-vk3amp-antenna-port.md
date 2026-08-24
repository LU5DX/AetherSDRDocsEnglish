# Select the VK3AMP antenna port

Select which antenna port (1–3) the VK3AMP amplifier routes RF to. The amplifier's own control table can override a selection within about 50 ms, so the applet reflects the live status rather than assuming your click was accepted.

## Before you start

- A radio connection is required (the applet is disabled without one).
- Open the VK3AMP Amplifier applet from the Applet panel > VKAMP tile.

## Steps

1. Wait for the amplifier connection status pill in the applet header to show a connected state.
2. In the ANT row, click the antenna port you want to use: **1**, **2**, or **3**.
3. Confirm the click took effect. The applet's ANT readout (next to "ANT" in the info grid) and the button highlight move only after the amplifier's live status confirms the selection.

## What each control does

| Control | Purpose | Notes |
| --- | --- | --- |
| **1** | Select antenna port 1 | Read-only display mirrors live status; the amp's own table can revert a select within ~50 ms. |
| **2** | Select antenna port 2 | Same as above. |
| **3** | Select antenna port 3 | Same as above. |

## Tips

- The antenna buttons are treated as read-only displays, not optimistic buttons. If your click doesn't seem to register, it may be because the amplifier's control table rejected or reverted the selection — check the applet's ANT readout and highlighted port for the authoritative state.

## Related

- [VK3AMP Amplifier overview](overview.md)
- [Bypass the VK3AMP amplifier](bypass-the-vk3amp-amplifier.md)
- [Monitor forward and reflected power on the VK3AMP amplifier](monitor-forward-and-reflected-power-on-the-vk3amp-amplifier.md)
- [Reset the VK3AMP amplifier](reset-the-vk3amp-amplifier.md)

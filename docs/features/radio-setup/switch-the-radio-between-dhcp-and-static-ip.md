# Switch the Radio Between DHCP and Static IP

Use this page to change how your FLEX-8600 receives its network address — either automatically via DHCP or with a fixed static IP that you specify.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available when a radio connection is active.
- If you are switching to static IP, have your intended IP address, subnet mask, and gateway address ready before you begin.
- Changing the radio's IP address will drop the current connection. You will need to reconnect using the new address.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Note the current **IP Address**, **Mask**, and **MAC Address** shown as read-only indicators. These reflect what the radio is currently using.
4. Click the **DHCP / Static** toggle button to switch modes. The button label reflects the currently active mode.
5. If you switched to **Static**, fill in the **IP Address:**, **Mask:**, and **Gateway:** fields with your intended values.
6. Click **Apply** to push the network configuration to the radio.
7. Reconnect to the radio using the new IP address if the connection drops.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator (read-only) | Shows the radio's current network addresses. Updated after a connection is established. |
| **DHCP / Static** | Toggle button | Switches the radio between DHCP mode (address assigned by your router) and Static mode (address you specify manually). |
| **IP Address:** | Text field | The static IPv4 address to assign to the radio. Only active in Static mode. |
| **Mask:** | Text field | The subnet mask for the static configuration. Only active in Static mode. |
| **Gateway:** | Text field | The default gateway for the static configuration. Only active in Static mode. |
| **Enforce Private IP Connections:** | Toggle button | When enabled, the radio rejects connections from non-RFC1918 (non-private) IP addresses. |
| **Network MTU:** | Spinbox | Sets the outgoing MTU in bytes. |
| **Apply** | Push button | Sends the current network configuration to the radio. |

## Tips

- After clicking **Apply** with a new static IP, AetherSDR will lose contact with the radio. Use `Settings > Connect to Radio...` to rediscover or manually enter the new address.
- If you are unsure which static address to use, check your router's DHCP lease table for the address currently assigned to the radio's MAC address, then reserve or assign that address as a static entry.

## Troubleshooting

- **The IP Address:, Mask:, and Gateway: fields are not editable** — The **DHCP / Static** toggle is set to DHCP. Switch it to Static first.
- **The radio does not appear after switching to static IP** — The address, mask, or gateway entered may be incorrect for your network. Connect the radio to a screen or use its front-panel controls to verify or reset the network settings, then retry.
- **Apply has no visible effect** — Confirm AetherSDR is still connected to the radio before clicking **Apply**. If the connection was already lost, reconnect first and then reapply the settings.

## Related

- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Radio Setup overview](overview.md)

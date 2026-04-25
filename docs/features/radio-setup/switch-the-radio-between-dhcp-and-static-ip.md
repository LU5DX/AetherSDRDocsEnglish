# Switch the Radio Between DHCP and Static IP

Use this page to change how your FLEX-8600 obtains its IP address — either automatically via DHCP or with a fixed static address you specify. You would use a static IP to ensure the radio is always reachable at a known address, for example in a remote or VPN setup.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available while connected.
- If you are switching to static IP, have your intended IP address, subnet mask, and gateway address ready before you start.
- Changing the radio's IP address will drop the current connection. Reconnect using the new address after applying.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Network** tab.
3. Locate the **DHCP / Static** toggle button. Click it to switch between DHCP and Static IP modes.
4. If you selected Static: type the desired values into the **IP Address:**, **Mask:**, and **Gateway:** fields.
5. Click **Apply** to push the network configuration to the radio.
6. Reconnect to the radio at its new address using `Settings > Connect to Radio...`.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **DHCP / Static** | Toggle button | Switches the radio between DHCP mode (address assigned by your router) and Static IP mode (address you enter manually). |
| **IP Address:** | Text field | The static IPv4 address to assign to the radio. Active only in Static mode. |
| **Mask:** | Text field | The subnet mask for the static address. Active only in Static mode. |
| **Gateway:** | Text field | The default gateway for the static address. Active only in Static mode. |
| **Apply** | Push button | Sends the current network configuration to the radio. |
| **IP Address / Mask / MAC Address** (read-only) | Indicator | Displays the radio's current network addresses. These are read-only. |

## Tips

- The read-only **IP Address / Mask / MAC Address** indicators at the top of the Network tab show the radio's current active addresses. Note these down before making changes so you can recover if needed.
- If you are connecting over a VPN or remote link, also review the **Network MTU:** setting on the same tab. See [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md).

## Troubleshooting

- **Cannot see the Network tab** — The tab is only available when AetherSDR is connected to the radio. Connect first via `Settings > Connect to Radio...`, then reopen Radio Setup.
- **Radio is unreachable after clicking Apply** — The radio has adopted its new address. If you switched to static IP, reconnect using the address you entered. If you switched to DHCP, check your router's DHCP lease table to find the address the radio was assigned.
- **Apply has no effect** — Verify that the IP Address:, Mask:, and Gateway: fields all contain valid values before clicking Apply. An incomplete static configuration may be rejected silently.

## Related

- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)

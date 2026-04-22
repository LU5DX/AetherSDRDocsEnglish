# Switch the Radio Between DHCP and Static IP

Use this page to change how the FLEX-8600 obtains its IP address — either automatically via DHCP or with a fixed static address you specify.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available when a connection is active.
- If you are switching to static IP, have the target IP address, subnet mask, and gateway address ready before you begin.
- Be aware that changing the IP configuration will cause the radio to use a new address. You may need to reconnect AetherSDR after applying.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Note the current **IP Address**, **Mask**, and **MAC Address** shown as read-only indicators.
4. Click the **DHCP / Static** toggle button to switch modes.
   - When set to DHCP, the radio requests an address from your network's DHCP server.
   - When set to Static, the **IP Address:**, **Mask:**, and **Gateway:** text fields become editable.
5. If you selected static mode, enter values in the **IP Address:**, **Mask:**, and **Gateway:** fields.
6. Click **Apply** to push the network configuration to the radio.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicators (read-only) | Show the radio's current network addresses. |
| **DHCP / Static** | Toggle button | Switches the radio between DHCP and static IP modes. |
| **IP Address:** | Text field | Static IP address to assign to the radio. Active only in static mode. |
| **Mask:** | Text field | Subnet mask for the static configuration. Active only in static mode. |
| **Gateway:** | Text field | Default gateway for the static configuration. Active only in static mode. |
| **Apply** | Push button | Sends the current network configuration to the radio. |

## Tips

- The read-only **IP Address** indicator reflects the radio's current address before any change is applied. Use it to confirm what address AetherSDR will need to reconnect to after switching.
- If you switch to DHCP and your network does not have a DHCP server, the radio may become unreachable. Ensure a DHCP server is available before switching.

## Troubleshooting

- **Radio becomes unreachable after clicking Apply** — The radio is now on a new IP address. Use `Settings > Connect to Radio...` to rediscover it on the network. If you assigned a static IP outside your subnet, you may need to connect a display to the radio directly to correct the address.
- **IP Address:, Mask:, and Gateway: fields are greyed out** — The toggle is set to DHCP. Click **DHCP / Static** to switch to static mode before editing the fields.

## Related

- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Radio Setup overview](overview.md)

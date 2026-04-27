# Switch the Radio Between DHCP and Static IP

Use this page to change how the FLEX-8600 obtains its network address — either automatically via DHCP or with a fixed static IP, subnet mask, and gateway you specify.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available when a radio connection is active.
- If you are switching to static IP, have the IP address, subnet mask, and gateway values ready before you begin.
- Changing the network configuration will cause the radio to move to a new address. You will need to reconnect after applying.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Network** tab.
3. Note the current **IP Address**, **Mask**, and **MAC Address** shown as read-only indicators.
4. Click the **DHCP / Static** toggle button to switch modes. The button reflects the current mode; clicking it switches to the other.
5. If you selected static mode, fill in the **IP Address:**, **Mask:**, and **Gateway:** text fields with the values for your network.
6. Click **Apply** to push the network configuration to the radio.
7. Reconnect to the radio at its new address using `Settings > Connect to Radio...`.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicators (read-only) | Displays the radio's current network addresses. |
| **DHCP / Static** | Toggle button | Switches the radio between DHCP and static IP modes. |
| **IP Address:** | Text field | Static IP address to assign to the radio. Active only in static mode. |
| **Mask:** | Text field | Subnet mask for the static configuration. Active only in static mode. |
| **Gateway:** | Text field | Default gateway for the static configuration. Active only in static mode. |
| **Apply** | Push button | Sends the network configuration to the radio. |

## Tips

- The **IP Address / Mask / MAC Address** indicators show what the radio is currently using. Record these values before making changes so you can revert if needed.
- The **Enforce Private IP Connections:** toggle on the same tab rejects connections from non-RFC1918 addresses. If you assign a static IP, confirm it falls within a private range (e.g. 192.168.x.x, 10.x.x.x) if that toggle is enabled.

## Troubleshooting

- **Cannot find the radio after clicking Apply** — The radio has moved to its new address. Use `Settings > Connect to Radio...` to discover and reconnect to it on the updated address.
- **IP Address:, Mask:, and Gateway: fields are not editable** — The toggle is set to DHCP. Click **DHCP / Static** to switch to static mode first.

## Related

- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Check radio serial, hardware version, region and options](check-radio-serial-hardware-version-region-and-options.md)

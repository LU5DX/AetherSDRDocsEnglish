# Switch the Radio Between DHCP and Static IP

Use this page to configure the FLEX-8600's network addressing mode. Switch to static IP when you need the radio at a fixed address on your LAN, or return to DHCP to let your router assign an address automatically.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available while connected.
- If you are assigning a static IP, have your intended IP address, subnet mask, and gateway address ready before you begin.
- Changing the IP address will disconnect AetherSDR from the radio. Be prepared to reconnect at the new address.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **Network** tab.
3. Locate the **DHCP / Static** toggle button. Click it to switch between modes.
   - When set to DHCP, the static address fields are not needed.
   - When set to Static, the **IP Address:**, **Mask:**, and **Gateway:** fields become active.
4. If you selected Static, enter the desired values in the **IP Address:**, **Mask:**, and **Gateway:** fields.
5. Click **Apply** to push the network configuration to the radio.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **DHCP / Static** | Toggle button | Switches the radio between DHCP and static IP modes. |
| **IP Address:** | Text field | The static IPv4 address to assign to the radio. Active only in Static mode. |
| **Mask:** | Text field | The subnet mask for the static configuration. Active only in Static mode. |
| **Gateway:** | Text field | The default gateway for the static configuration. Active only in Static mode. |
| **Apply** | Button | Pushes the current network configuration to the radio. |

## Tips

- The **IP Address / Mask / MAC Address** indicators above the toggle show the radio's current network addresses and are read-only. Use them to confirm the new settings took effect after reconnecting.
- After clicking **Apply** in Static mode, AetherSDR will lose the connection. Reconnect via `Settings > Connect to Radio...` using the new static address.

## Troubleshooting

- **Radio does not appear after switching to static IP** — The address entered may conflict with another device or may be outside your LAN's subnet. Verify the IP address, mask, and gateway are correct for your network. If the radio becomes unreachable, a hardware reset may be required to restore DHCP; see your FLEX-8600 hardware documentation.
- **Apply does not seem to take effect** — Ensure you are still connected to the radio at the moment you click **Apply**. If the connection dropped before you clicked, reopen `Settings > Radio Setup...`, re-enter the static values, and click **Apply** promptly.

## Related

- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Radio Setup overview](overview.md)

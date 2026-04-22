# Switch the Radio Between DHCP and Static IP

Use this page to change how your FLEX-8600 receives its IP address — either automatically from a DHCP server or from a fixed static address you enter manually. A static IP is useful when you need a predictable address for remote access or network integrations.

## Before you start

- AetherSDR must be connected to the radio. The Network tab is only available while connected.
- Have your desired static IP address, subnet mask, and gateway address ready before you start.
- If you are switching to static IP, confirm that the address you plan to use is not already in use on your network and is outside your router's DHCP assignment range.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the **Network** tab.
3. Locate the **DHCP / Static** toggle button.
4. Click **DHCP / Static** to switch between modes. The button reflects the currently active mode.
5. If you switched to Static, enter values in the **IP Address:**, **Mask:**, and **Gateway:** fields.
6. Click **Apply** to push the network configuration to the radio.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **IP Address / Mask / MAC Address** | Indicator (read-only) | Displays the radio's current network addresses. These update after Apply takes effect. |
| **DHCP / Static** | Toggle button | Switches the radio between DHCP and static IP assignment. |
| **IP Address:** | Text field | Static IP address to assign to the radio. Active only in Static mode. |
| **Mask:** | Text field | Subnet mask for the static configuration. Active only in Static mode. |
| **Gateway:** | Text field | Default gateway for the static configuration. Active only in Static mode. |
| **Apply** | Button | Sends the network settings to the radio. |
| **Enforce Private IP Connections:** | Toggle button | When enabled, rejects connections from non-RFC1918 (non-private) IP addresses. |
| **Network MTU:** | Spinbox | Sets the outgoing MTU in bytes. |

## Tips

- After clicking **Apply** with a new static IP, the radio will be unreachable at its old address. Reconnect using the new IP via `Settings > Connect to Radio...`.
- If you are switching back to DHCP, you do not need to fill in the address fields — click **Apply** immediately after toggling to DHCP.

## Troubleshooting

- **Radio is unreachable after applying a static IP** — The address, mask, or gateway may be incorrect for your network. Connect to the radio via its front-panel display or console to verify the settings, then correct them in AetherSDR.
- **Apply has no effect** — Confirm the radio is still connected (the Network tab requires an active connection). If the connection dropped, reconnect and re-enter the settings before clicking **Apply**.

## Related

- [Change network MTU for VPN/remote setups](change-network-mtu-for-vpn-remote-setups.md)
- [Radio Setup overview](overview.md)

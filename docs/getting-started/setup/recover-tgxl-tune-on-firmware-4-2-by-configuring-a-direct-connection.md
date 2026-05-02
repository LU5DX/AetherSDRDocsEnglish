# Recover TGXL TUNE on firmware 4.2 by configuring a direct connection

FlexRadio firmware 4.2 broke the radio-side `tgxl autotune` command path. Configuring a direct TCP connection from AetherSDR to the TGXL restores the TUNE button by sending the autotune command directly to the TGXL instead of routing it through the radio.

## Before you start

- AetherSDR must be connected to your FLEX-8600 radio.
- Your TGXL must be powered on and reachable on the network from the machine running AetherSDR.
- Know the TGXL's IP address. If the radio has already discovered the TGXL, AetherSDR will pre-fill it for you.

## Steps

1. Click `Settings > Radio Setup...` to open the Radio Setup dialog.
2. Click the `Peripherals` tab.
3. Locate the TGXL row. If the IP address field is empty, enter the TGXL's IP address. The default port is `9010`; leave it unchanged unless your network requires a different port.
4. Click `Connect` in the TGXL row.
5. Verify the button changes to `Disconnect`, indicating the direct TCP connection is active.
6. Close the dialog. The TUNE button now sends the autotune command directly to the TGXL.

AetherSDR saves the IP and port to `TGXL_ManualIp` and `TGXL_ManualPort` on a successful connect and will reconnect automatically on the next startup.

## What each control does

| Control | Behavior | Default | Setting key |
|---|---|---|---|
| IP address field (TGXL) | IP address of the TGXL on your network. Pre-filled with the radio-discovered address if available. | — | `TGXL_ManualIp` |
| Port field (TGXL) | TCP port for the direct TGXL connection. | `9010` | `TGXL_ManualPort` |
| `Connect` / `Disconnect` (TGXL) | Opens or closes the direct TCP connection to the TGXL. When connected, TUNE sends the autotune command directly to the TGXL. | Connect | — |

## Tips

- The TGXL drives radio PTT through its hardware interlock cable. No additional PTT configuration in AetherSDR is needed for tuning to work once the direct connection is active.
- If the radio has already discovered the TGXL on the LAN, the IP address field is pre-filled. You only need to click `Connect`.
- The saved `TGXL_ManualIp` and `TGXL_ManualPort` values persist across restarts, so you only need to perform this setup once.

## Troubleshooting

- **`Connect` button does not change to `Disconnect`** — The TGXL is not reachable at the entered IP and port. Confirm the TGXL is powered on, check that port `9010` is not blocked by a firewall, and verify the IP address is correct.
- **TUNE still does not work after connecting** — Confirm the `Disconnect` label is shown in the TGXL row, which confirms the direct connection is active. If the button reverted to `Connect`, the connection dropped; check network stability and reconnect.
- **IP address field is empty and the radio has not discovered the TGXL** — Enter the TGXL's IP address manually. You can find it in your router's DHCP table or on the TGXL's front panel.

## Related

- [Connect TGXL, PGXL or Antenna Genius by IP](connect-tgxl-pgxl-or-antenna-genius-by-ip.md)
- [Fix TUNE not working after upgrading to firmware 4.2 (configure direct TGXL connection)](fix-tune-not-working-after-upgrading-to-firmware-4-2-configure-direct-tgxl-connection.md)
- [Set per-band TX max power and tune mode](../../features/radio-setup/set-per-band-tx-max-power-and-tune-mode.md)
- [Radio Setup overview](../../features/radio-setup/overview.md)

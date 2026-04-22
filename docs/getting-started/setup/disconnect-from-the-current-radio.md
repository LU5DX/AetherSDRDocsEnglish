# Disconnect from the current radio

This page explains how to disconnect AetherSDR from a FLEX-8600 radio. You would do this to connect to a different radio, switch connection modes, or shut down your session cleanly.

## Before you start

- AetherSDR must already be connected to a radio. If it is not connected, the ConnectionPanel is already showing and no action is needed.

## Steps

1. Open `Settings > Connect to Radio...`.
2. Click `Disconnect`.

AetherSDR drops the radio connection and returns to the ConnectionPanel, where you can choose a new radio or connection mode.

## Tips

- After disconnecting, your last `ConnectionMode` is remembered. The ConnectionPanel re-opens on whichever mode — `Local`, `Remote with SmartLink`, or `Connect by IP` — you used previously.
- If you intend to reconnect to the same local radio, wait for it to reappear in the `Available radios` list before clicking `Connect Selected Radio`. Discovery restarts automatically after disconnect.

## Related

- [Connect to a Radio overview](../../features/connection/overview.md)
- [Connect to a local LAN radio](connect-to-a-local-lan-radio.md)
- [Connect to a remote radio through SmartLink](connect-to-a-remote-radio-through-smartlink.md)
- [Connect by IP across a VPN or routed network](connect-by-ip-across-a-vpn-or-routed-network.md)
- [Retry discovery when no radios appear](../../features/connection/retry-discovery-when-no-radios-appear.md)

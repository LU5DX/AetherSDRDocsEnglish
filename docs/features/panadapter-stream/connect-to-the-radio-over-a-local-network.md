# Connect to the radio over a local network

`RadioConnection` manages the TCP control connection to your radio and registers the UDP streams so audio and panadapter data flow to the correct port on your machine.

## Before you start

- Your radio and computer must be on the same local network (LAN).
- Note the radio's IP address (check your router's DHCP table or the radio's front panel network settings).
- Ensure no firewall is blocking TCP port 4992 or the UDP ports used for streaming.

## Steps

1. Launch AetherSDR. The **Radio Discovery** panel appears automatically and scans the local network for radios.
2. If your radio appears in the list, select it and click **Connect**.
3. If your radio does not appear, enter the radio's IP address manually in the address field and click **Connect**.
4. AetherSDR opens the TCP control connection and registers the UDP data streams. The panadapter and audio streams start automatically once the connection is confirmed.

## Tips

- If the radio is found but the connection fails, confirm that no other client is already connected (the radio allows a limited number of simultaneous connections).
- If UDP streams do not start after connecting, check that your firewall allows inbound UDP traffic on the port range shown in the radio's network settings.
- Use the network quality monitor in the status bar to watch packet error counts and audio packet gap — a high error rate usually points to a network switch or cable issue, not a radio fault.

## Related

- [Troubleshoot network streaming](./troubleshoot-network-streaming.md)
- [Connect to the radio over a WAN](./connect-wan.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->

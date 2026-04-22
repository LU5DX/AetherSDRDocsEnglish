# Start WSJT-X UDP Listener and Filter for CQ, POTA or Calls to Me

AetherSDR can listen for WSJT-X decode packets over UDP and display matching transmissions as spots on the panadapter. Use the filters to limit what appears to CQ calls, POTA activations, or stations calling your callsign.

## Before you start

- WSJT-X must be running on the same machine or a machine reachable over the network.
- In WSJT-X, confirm UDP messaging is enabled and the destination address and port match what you will set in AetherSDR. The WSJT-X default UDP port is 2237.
- Know your own callsign if you intend to use the "Calling Me" filter.

## Steps

1. Go to `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. In **Address:**, enter the UDP bind address AetherSDR should listen on. To accept packets from any interface, use `0.0.0.0`. This is stored as `WsjtxAddress`.
4. In **Port:**, set the UDP port to match WSJT-X's configured destination port. Valid range: 1–65535. This is stored as `WsjtxPort`.
5. Click **Start**. The status indicator changes to **Listening**.
6. To show only CQ calls, check **CQ**. This is stored as `WsjtxFilterCQ`.
7. To show only POTA activations, check **CQ POTA**. This is stored as `WsjtxFilterPOTA`.
8. To show only decodes addressed to your callsign, check **Calling Me**. This is stored as `WsjtxFilterCallingMe`.
9. To have AetherSDR start the listener automatically each time it launches, enable **Auto-start on startup (WSJT-X)**. This is stored as `WsjtxAutoStart`.

## What each control does

| Control | What it does | Setting key |
|---|---|---|
| **Address:** | UDP bind address for incoming WSJT-X messages. | `WsjtxAddress` |
| **Port:** | UDP port number. Valid range: 1–65535. | `WsjtxPort` |
| **Start / Stop** | Starts or stops the UDP listener. Status shows **Listening** when active. | — |
| **Auto-start on startup (WSJT-X)** | Starts the listener automatically when AetherSDR launches. | `WsjtxAutoStart` |
| **CQ** | Passes only CQ calls from WSJT-X decodes to the spot overlay. | `WsjtxFilterCQ` |
| **CQ POTA** | Passes only CQ POTA calls. | `WsjtxFilterPOTA` |
| **Calling Me** | Passes only decodes addressed to your callsign. | `WsjtxFilterCallingMe` |
| **CQ color** | Color picker for CQ spots on the panadapter. | `WsjtxColorCQ` |
| **POTA color** | Color picker for POTA spots. | `WsjtxColorPOTA` |
| **Calling Me color** | Color picker for spots calling you. | `WsjtxColorCallingMe` |
| **Default color** | Color picker for all other WSJT-X spots. | `WsjtxColorDefault` |
| **Spot Life:** | Seconds a WSJT-X spot remains visible on the panadapter. | `WsjtxSpotLife` |
| **WSJT-X Decodes** | Read-only console showing decoded transmissions as they arrive. | — |

## Tips

- You can enable more than one filter at the same time. For example, checking both **CQ** and **Calling Me** shows CQ calls and any station calling you.
- If no filters are checked, all WSJT-X decodes appear as spots.
- The **WSJT-X Decodes** console shows raw decode lines regardless of the active filters, which is useful for verifying that packets are arriving.
- Spot lifetime set with **Spot Life:** applies only to WSJT-X spots. The global panadapter spot lifetime is controlled separately on the **Display** tab under **Spot Lifetime:**.

## Troubleshooting

- **Status stays at Stopped after clicking Start** — Check that no other application is already bound to the same port. Change **Port:** if there is a conflict.
- **Decodes appear in the console but not on the panadapter** — Confirm that spots are globally enabled. Go to `Settings > SpotHub...`, open the **Display** tab, and verify that **Spots:** is set to **Enabled**.
- **"Calling Me" filter shows nothing** — WSJT-X must be configured with your callsign so that it includes your call in the UDP decode messages. Verify the callsign in WSJT-X matches what you expect AetherSDR to detect.
- **Packets are not arriving from a remote machine** — Ensure there is no firewall blocking UDP on the configured port, and that WSJT-X's UDP destination address is set to the IP address of the AetherSDR machine, not `127.0.0.1`.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

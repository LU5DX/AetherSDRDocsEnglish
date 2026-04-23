# Start WSJT-X UDP Listener and Filter for CQ, POTA or Calls to Me

AetherSDR can listen on a UDP port for WSJT-X decode messages and plot the resulting spots on the panadapter. Use the filters to limit what appears to CQ calls, POTA activations, or stations calling your callsign.

## Before you start

- WSJT-X must be configured to send UDP messages to the address and port you set here. In WSJT-X, open **File > Settings > Reporting** and confirm the UDP server address and port match what you enter below.
- AetherSDR does not need to be connected to a radio for the listener to run, but spots only appear on the panadapter when a radio is connected.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. In **Address:**, enter the UDP bind address where AetherSDR should listen (stored as `WsjtxAddress`). Use `127.0.0.1` if WSJT-X runs on the same machine.
4. In **Port:**, set the UDP port to match your WSJT-X reporting configuration (stored as `WsjtxPort`; valid range 1–65535).
5. Click **Start**. The status indicator changes to **Listening**.
6. To start the listener automatically at launch, click **Auto-start on startup** (stored as `WsjtxAutoStart`).
7. Enable one or more filters:
   - Check **CQ** to show only CQ calls (stored as `WsjtxFilterCQ`).
   - Check **CQ POTA** to show CQ POTA calls (stored as `WsjtxFilterPOTA`).
   - Check **Calling Me** to show only decodes addressed to your callsign (stored as `WsjtxFilterCallingMe`).
8. Optionally adjust **Spot Life:** to control how many seconds WSJT-X spots remain on the panadapter (stored as `WsjtxSpotLife`).
9. Confirm decoded transmissions are appearing in the **WSJT-X Decodes** console.

## What each control does

| Control | Behavior | Setting key | Default | Valid range |
|---|---|---|---|---|
| **Address:** | UDP bind address for WSJT-X messages | `WsjtxAddress` | — | — |
| **Port:** | UDP port for WSJT-X | `WsjtxPort` | — | 1–65535 |
| **Start / Stop** | Starts or stops the UDP listener | — | — | — |
| **Auto-start on startup** | Auto-starts the listener on launch | `WsjtxAutoStart` | — | — |
| **CQ** | Show only CQ calls | `WsjtxFilterCQ` | — | — |
| **CQ POTA** | Show CQ POTA calls | `WsjtxFilterPOTA` | — | — |
| **Calling Me** | Show only decodes addressed to your callsign | `WsjtxFilterCallingMe` | — | — |
| **CQ color** | Color picker for CQ spots | `WsjtxColorCQ` | — | — |
| **POTA color** | Color picker for POTA spots | `WsjtxColorPOTA` | — | — |
| **Calling Me color** | Color picker for stations calling you | `WsjtxColorCallingMe` | — | — |
| **Default color** | Color picker for all other WSJT-X spots | `WsjtxColorDefault` | — | — |
| **Spot Life:** | Seconds WSJT-X spots remain on the panadapter | `WsjtxSpotLife` | — | — |
| **WSJT-X Decodes** | Read-only console of decoded transmissions | — | — | — |

## Tips

- If none of the three filters (**CQ**, **CQ POTA**, **Calling Me**) are checked, all decoded spots are passed through to the panadapter.
- The **Calling Me** filter matches against the callsign AetherSDR receives from WSJT-X in each decode message, so ensure your callsign is set correctly in WSJT-X itself.
- You can assign distinct colors to each filter category so CQ calls, POTA activations, and stations calling you are visually distinct on the panadapter. Use the **CQ color**, **POTA color**, **Calling Me color**, and **Default color** pickers on the same tab.
- Decoded spots flow into the unified **Spot List** tab alongside spots from other sources. Use the band checkboxes there to narrow the view.

## Troubleshooting

- **No spots appear in WSJT-X Decodes** — Verify the address and port in AetherSDR match the UDP server address and port set in WSJT-X under **File > Settings > Reporting**. Confirm the listener status shows **Listening**, not **Stopped**. Check that your firewall is not blocking the UDP port.
- **Spots appear in the console but not on the panadapter** — Confirm the master spot overlay is enabled. Open the **Display** tab in SpotHub and check that **Spots:** is set to **Enabled** (`IsSpotsEnabled`). Also confirm a radio is connected, as the panadapter overlay requires an active radio connection.
- **Only some spots appear** — One or more filters are active. If you want all decodes, uncheck **CQ**, **CQ POTA**, and **Calling Me**.

## Related

- [SpotHub overview](overview.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Poll POTA activations](poll-pota-activations.md)

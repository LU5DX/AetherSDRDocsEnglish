# Start WSJT-X UDP Listener and Filter for CQ, POTA, or Calls to Me

AetherSDR can listen for WSJT-X decode messages over UDP and place matching stations as spots on the panadapter. Use this page to start the listener and restrict what appears to CQ calls, POTA activations, or decodes addressed to your callsign.

## Before you start

- WSJT-X must be running on the same machine or network and configured to send UDP status messages to the address and port you set here.
- Know the UDP address and port WSJT-X is sending to (check WSJT-X under **File > Settings > Reporting**, UDP Server field).
- The panadapter spot overlay must be enabled. If spots are not visible, open `Settings > SpotHub...`, go to the **Display** tab, and confirm **Spots:** is set to Enabled.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. In **Address:**, enter the UDP bind address that matches what WSJT-X is sending to (typically `127.0.0.1` for local use). This persists as `WsjtxAddress`.
4. In **Port:**, set the UDP port to match WSJT-X's UDP Server port. Valid range: 1–65535. This persists as `WsjtxPort`.
5. Click **Start**. The status indicator changes to **Listening**. The **WSJT-X Decodes** console begins showing received transmissions.
6. Enable the filters you want:
   - Check **CQ** to show only CQ calls. Persists as `WsjtxFilterCQ`.
   - Check **CQ POTA** to show CQ POTA calls. Persists as `WsjtxFilterPOTA`.
   - Check **Calling Me** to show only decodes addressed to your callsign. Persists as `WsjtxFilterCallingMe`.
7. To start the listener automatically each time AetherSDR launches, enable **Auto-start on startup (WSJT-X)**. Persists as `WsjtxAutoStart`.

## What each control does

| Control | What it does | Persisted key |
|---|---|---|
| **Address:** | UDP bind address for incoming WSJT-X messages | `WsjtxAddress` |
| **Port:** | UDP port to listen on (1–65535) | `WsjtxPort` |
| **Start / Stop** | Starts or stops the UDP listener | — |
| **Auto-start on startup (WSJT-X)** | Starts listener automatically on launch | `WsjtxAutoStart` |
| **CQ** | Shows only CQ calls from WSJT-X decodes | `WsjtxFilterCQ` |
| **CQ POTA** | Shows CQ POTA calls | `WsjtxFilterPOTA` |
| **Calling Me** | Shows only decodes addressed to your callsign | `WsjtxFilterCallingMe` |
| **CQ color** | Color for CQ spots on the panadapter | `WsjtxColorCQ` |
| **POTA color** | Color for POTA spots on the panadapter | `WsjtxColorPOTA` |
| **Calling Me color** | Color for spots calling you | `WsjtxColorCallingMe` |
| **Default color** | Color for all other WSJT-X spots | `WsjtxColorDefault` |
| **Spot Life:** | Seconds a WSJT-X spot remains on the panadapter | `WsjtxSpotLife` |
| **WSJT-X Decodes** | Read-only console of decoded transmissions | — |

## Tips

- You can check any combination of **CQ**, **CQ POTA**, and **Calling Me** simultaneously. A spot appears if it matches any checked filter. If none are checked, all WSJT-X decodes appear as spots.
- Each filter category has its own color picker. Assign distinct colors to tell CQ, POTA, and direct calls apart at a glance on the panadapter.
- Keep **Spot Life:** low (a few seconds to one FT8 period, 15 s) to avoid stale decodes cluttering the panadapter between WSJT-X decode cycles.
- The **WSJT-X Decodes** console shows all received decodes regardless of the active filters, so you can confirm the listener is working even before enabling filters.

## Troubleshooting

- **Status stays Stopped / no decodes appear** — Confirm WSJT-X UDP reporting is enabled and its UDP Server address and port match **Address:** and **Port:** in AetherSDR. Check that no firewall is blocking the port.
- **Spots appear on panadapter but filters seem to have no effect** — Verify the correct checkboxes (**CQ**, **CQ POTA**, **Calling Me**) are checked. If none are checked, all decodes are shown.
- **Calling Me filter shows nothing** — WSJT-X must know your callsign (set under WSJT-X **File > Settings > General**) for decodes directed to you to be identified correctly.
- **Spot overlay not visible at all** — Open the **Display** tab in SpotHub and confirm **Spots:** is Enabled.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)
- [Poll POTA activations](poll-pota-activations.md)

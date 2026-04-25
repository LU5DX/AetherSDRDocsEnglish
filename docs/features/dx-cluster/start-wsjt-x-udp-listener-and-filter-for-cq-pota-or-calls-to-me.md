# Start WSJT-X UDP Listener and Filter for CQ, POTA or Calls to Me

Configure AetherSDR to receive decoded transmissions from WSJT-X over UDP and show only the spot categories you care about — CQ calls, POTA activations, or stations calling your callsign — as overlays on the panadapter.

## Before you start

- WSJT-X must be running on the same machine or network and configured to send UDP status messages to the address and port you will set here.
- Know the UDP address and port WSJT-X is broadcasting to (check WSJT-X under **File > Settings > Reporting**, UDP Server section).
- Your callsign must be set in WSJT-X for the "Calling Me" filter to work.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **WSJT-X** tab.
3. In **Address:**, enter the UDP bind address AetherSDR should listen on (stored as `WsjtxAddress`). Use `127.0.0.1` if WSJT-X runs on the same machine, or `0.0.0.0` to listen on all interfaces.
4. In **Port:**, enter the UDP port number that matches the port configured in WSJT-X (stored as `WsjtxPort`; valid range 1–65535).
5. Click **Start**. The status indicator changes to **Listening**.
6. To start the listener automatically every time AetherSDR launches, enable **Auto-start on startup (WSJT-X)** (stored as `WsjtxAutoStart`).
7. Under the filter checkboxes, enable one or more of the following to restrict which decodes appear as panadapter spots:
   - **CQ** — shows stations sending a general CQ call (stored as `WsjtxFilterCQ`).
   - **CQ POTA** — shows stations sending CQ POTA (stored as `WsjtxFilterPOTA`).
   - **Calling Me** — shows decodes addressed to your callsign (stored as `WsjtxFilterCallingMe`).
8. Optionally assign a distinct color to each category by clicking the corresponding color button:
   - **CQ color** (stored as `WsjtxColorCQ`)
   - **POTA color** (stored as `WsjtxColorPOTA`)
   - **Calling Me color** (stored as `WsjtxColorCallingMe`)
   - **Default color** for decodes that pass no active filter (stored as `WsjtxColorDefault`)
9. Set **Spot Life:** to the number of seconds a WSJT-X spot should remain visible on the panadapter (stored as `WsjtxSpotLife`).
10. Confirm decoded transmissions are arriving in the **WSJT-X Decodes** console at the bottom of the tab.

## What each control does

| Control | Behavior | Setting key | Default / Range |
|---|---|---|---|
| **Address:** | UDP bind address for incoming WSJT-X messages. | `WsjtxAddress` | — |
| **Port:** | UDP port number. Must match WSJT-X reporting port. | `WsjtxPort` | 1–65535 |
| **Start / Stop** | Starts or stops the UDP listener. | — | — |
| **Auto-start on startup (WSJT-X)** | Starts the listener automatically on launch. | `WsjtxAutoStart` | — |
| **CQ** | Passes only CQ transmissions to the panadapter. | `WsjtxFilterCQ` | — |
| **CQ POTA** | Passes only CQ POTA transmissions. | `WsjtxFilterPOTA` | — |
| **Calling Me** | Passes only decodes addressed to your callsign. | `WsjtxFilterCallingMe` | — |
| **CQ color** | Color for CQ spots on the panadapter. | `WsjtxColorCQ` | — |
| **POTA color** | Color for CQ POTA spots. | `WsjtxColorPOTA` | — |
| **Calling Me color** | Color for spots calling your callsign. | `WsjtxColorCallingMe` | — |
| **Default color** | Color for spots that match no active filter. | `WsjtxColorDefault` | — |
| **Spot Life:** | Seconds a WSJT-X spot remains on the panadapter before fading. | `WsjtxSpotLife` | — |
| **WSJT-X Decodes** | Read-only console showing decoded transmissions as they arrive. | — | — |

## Tips

- If none of the three filter checkboxes (**CQ**, **CQ POTA**, **Calling Me**) are checked, all decoded transmissions are shown on the panadapter regardless of content.
- WSJT-X spots appear in the unified **Spot List** tab alongside spots from other sources. Double-click any row there to tune directly to that frequency.
- Spots from WSJT-X will only appear on the panadapter if the master **Spots:** toggle on the **Display** tab is enabled (stored as `IsSpotsEnabled`; default Enabled).
- FT8 operates on a 15-second cycle. Keep **Spot Life:** at 15 seconds or a multiple thereof so spots expire cleanly between cycles.

## Troubleshooting

- **Status stays at Stopped / no decodes appear in the console** — Verify the address and port in AetherSDR match exactly what is configured in WSJT-X under **File > Settings > Reporting**. Confirm no firewall is blocking the UDP port. Click **Stop** then **Start** after correcting the values.
- **Spots appear on the Spot List tab but not on the panadapter** — Open `Settings > SpotHub...`, go to the **Display** tab, and confirm **Spots:** is set to Enabled.
- **"Calling Me" filter shows no spots** — WSJT-X must have your callsign entered in its settings and must be actively decoding transmissions directed to that callsign. Verify your callsign in WSJT-X under **File > Settings > General**.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Poll POTA activations](poll-pota-activations.md)
- [Setting up digital modes (FT8, WSJT-X, fldigi)](../../operating/digital-modes/digital-modes-setup.md)

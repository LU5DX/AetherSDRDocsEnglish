# Enable SpotCollector UDP feed

AetherSDR can receive DX spots broadcast by Ham Radio Deluxe's SpotCollector over UDP and display them on the panadapter. This page explains how to start the listener, set the correct port, and configure it to start automatically.

## Before you start

- SpotCollector must be installed, configured, and running on the same machine or local network, and set to broadcast spots via UDP.
- Note the UDP port SpotCollector is broadcasting on — you will need to enter it in AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **SpotCollector** tab.
3. Set **UDP Port:** to the port SpotCollector is broadcasting on. Valid range: 1–65535. This value is saved as `SpotCollectorPort`.
4. Click **Start**.
5. Confirm the status indicator changes to **Listening**. Incoming spots will appear in the **SpotCollector Spots** console as they arrive.
6. To have the listener start automatically every time AetherSDR launches, enable **Auto-start on startup**. This is saved as `SpotCollectorAutoStart`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **UDP Port:** | UDP port AetherSDR listens on for SpotCollector broadcasts. Valid range: 1–65535. | `SpotCollectorPort` |
| **Start / Stop** | Starts or stops the UDP listener. | — |
| **Auto-start on startup** | Starts the listener automatically on launch. | `SpotCollectorAutoStart` |
| **SpotCollector Spots** | Read-only console showing spots received from SpotCollector. | — |
| **Enable FreeDV Reporter reporting when RADE is active** | Enables station-reporting to the public FreeDV Reporter map (qso.freedv.org) whenever the RADE modem is active. Requires a valid callsign and grid square — if either field is blank or unresolvable, the checkbox refuses to enable and displays a warning. | `FreeDvAutoReport` |
| **Callsign: (FreeDV Reporter)** | Callsign to report to the FreeDV Reporter map. Read-only when **Use radio** is checked. When **Use radio** is checked, the field is populated from the radio's configured callsign and updates automatically if that callsign changes. | `FreeDvMyCallsign` |
| **Use radio (callsign)** | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. | `FreeDvUseRadioCallsign` |
| **Grid Square: (FreeDV Reporter)** | Maidenhead grid square to report. Read-only when **Use GPS** is checked. | `FreeDvMyGrid` |
| **Use GPS (grid)** | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. | `FreeDvUseGpsGrid` |
| **Station Msg: (FreeDV Reporter)** | Optional free-text message shown beside the callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |

## FreeDV Reporter reporting

The **FreeDV** tab contains a **Station Reporting** group that controls whether AetherSDR broadcasts your station's activity to the public FreeDV Reporter map at qso.freedv.org.

### Requirements before enabling

- A valid callsign must be available — either from the radio (when **Use radio** is checked) or typed into the **Callsign:** field.
- A valid Maidenhead grid square must be available — either from the radio's GPS module (when **Use GPS** is checked, on supported hardware) or typed into the **Grid Square:** field.

If either value is missing when you attempt to enable **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR displays a warning and leaves the checkbox unchecked. This prevents blank or placeholder values from appearing on the shared public map.

### Steps to enable reporting

1. Open `Settings > SpotHub...` and click the **FreeDV** tab.
2. In the **Station Reporting** group, confirm the **Callsign:** field shows your callsign.
   - If **Use radio** is checked, the field is populated automatically from the radio's configured callsign and is read-only. Uncheck **Use radio** to enter a callsign manually.
3. Confirm the **Grid Square:** field shows your Maidenhead locator.
   - On radios with GPS hardware, check **Use GPS** to populate it automatically. Uncheck **Use GPS** to type a grid square manually.
4. Optionally enter a short message in **Station Msg:** — it appears beside your callsign on the map.
5. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If either the callsign or grid square is blank, a warning dialog appears. Fill in the missing value and try again.
6. Reporting is now active whenever the RADE modem is running.

## Tips

- Spots received from SpotCollector appear alongside spots from other sources in the **Spot List** tab. The **Source** column identifies them.
- If the panadapter spot overlay is not visible, check that **Spots:** is set to **Enabled** on the **Display** tab.

## Troubleshooting

- **Status stays Stopped / no spots appear** — Verify that SpotCollector is actively broadcasting and that the UDP port in AetherSDR matches the port configured in SpotCollector. Check that no firewall is blocking UDP traffic on that port.
- **Listener starts but the panadapter shows no spots** — Confirm that the master spot overlay is on: open the **Display** tab and check that **Spots:** is **Enabled**.
- **FreeDV Reporter checkbox unchecks itself with a warning** — The callsign or grid square field is empty or could not be resolved. Fill in both fields (or enable **Use radio** / **Use GPS** if the radio can supply the values) before enabling reporting.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Clear all spots from the panadapter](clear-all-spots-from-the-panadapter.md)
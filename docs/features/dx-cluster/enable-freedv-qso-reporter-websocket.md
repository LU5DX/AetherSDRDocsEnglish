# Enable FreeDV QSO Reporter WebSocket

Connect AetherSDR to the FreeDV QSO reporter at `qso.freedv.org` to receive FreeDV activity spots on your panadapter.

## Before you start

- The FreeDV WebSocket source is available only in AetherSDR builds compiled with WebSocket support (`HAVE_WEBSOCKETS`). If the FreeDV tab is absent from SpotHub, your build does not include it.
- Spots appear on the panadapter only when the master spot overlay is enabled. See [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md) if spots are not visible after connecting.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **FreeDV** tab.
3. Confirm the **Server:** indicator shows `qso.freedv.org (WebSocket)`. This endpoint is fixed and cannot be changed.
4. Click **Start**. The status indicator changes to **Connected** when the WebSocket handshake succeeds.
5. Optionally click **Auto-start on startup** so the connection is established automatically each time AetherSDR launches.
6. Optionally click **Spot Color:** to open the color picker and assign a distinct color to FreeDV spots on the panadapter. The chosen color is saved to `FreeDvSpotColor`.

## Reporting your station to the FreeDV Reporter map

The **Station Reporting** group at the bottom of the **FreeDV** tab lets you broadcast your activity to the public FreeDV Reporter map at `qso.freedv.org` whenever the RADE modem is active.

### Requirements before enabling

- A valid callsign must be present in the **Callsign:** field (or sourced from the radio).
- A valid Maidenhead grid square must be present in the **Grid Square:** field (or sourced from the radio's GPS).

If either value is blank when you check **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR shows a warning and leaves the checkbox unchecked. This prevents blank or placeholder values from being broadcast to the shared public map.

### Setup steps

1. In the **Station Reporting** group, review the **Callsign:** field.
   - If **Use radio** is checked (the default), the field is pre-filled with the callsign configured in your radio and is read-only. Changes to the radio's callsign in Radio Setup are reflected automatically.
   - Uncheck **Use radio** to enter a callsign manually. The entered value is saved to `FreeDvMyCallsign` and converted to upper case on save.
2. Review the **Grid Square:** field.
   - If your radio has GPS hardware and **Use GPS** is checked (the default on GPS-capable models), the field is pre-filled from the radio's GPS fix and is read-only. The **Use GPS** checkbox is hidden on radio models without GPS hardware.
   - Uncheck **Use GPS** (or if the checkbox is not present) to enter a grid square manually. The value is saved to `FreeDvMyGrid` and converted to upper case on save.
3. Optionally fill in **Station Msg:** with a short free-text note. This message appears beside your callsign on the public FreeDV Reporter map and is saved to `FreeDvMyMessage`.
4. Check **Enable FreeDV Reporter reporting when RADE is active**. AetherSDR validates callsign and grid before accepting the change, then saves `FreeDvAutoReport` = `True` and emits the reporting-enabled signal.

## What each control does

| Control | Kind | Behavior |
|---|---|---|
| **Server:** | Indicator | Fixed endpoint: `qso.freedv.org (WebSocket)`. Read-only. |
| **Start / Stop** | Push button | Connects or disconnects the FreeDV WebSocket. |
| **Auto-start on startup** | Toggle button | Starts the FreeDV connection automatically on launch. Saved to `FreeDvAutoStart`. |
| **FreeDV Spots** | Text field | Read-only console showing incoming FreeDV activity. |
| **Spot Color:** | Push button | Opens a color picker for FreeDV spots on the panadapter. Saved to `FreeDvSpotColor`. |
| **Enable FreeDV Reporter reporting when RADE is active** | Checkbox | Enables station-reporting to the public FreeDV Reporter map whenever the RADE modem is active. Refused if callsign or grid is blank. Saved to `FreeDvAutoReport`. Build-gated by `HAVE_WEBSOCKETS`; on Windows also requires `HAVE_RADE`. |
| **Callsign:** | Text field | Callsign to report to the FreeDV Reporter map. Read-only when **Use radio** is checked. Saved to `FreeDvMyCallsign`. |
| **Use radio** | Checkbox | Pre-fills **Callsign:** from the radio's configured callsign and locks the field read-only. Syncs automatically when the radio callsign changes. Saved to `FreeDvUseRadioCallsign`. Default: enabled. |
| **Grid Square:** | Text field | Maidenhead grid square to report. Read-only when **Use GPS** is checked. Saved to `FreeDvMyGrid`. |
| **Use GPS** | Checkbox | Pre-fills **Grid Square:** from the radio's GPS module and locks the field read-only. Shown only on radio models with GPS hardware. Saved to `FreeDvUseGpsGrid`. Default: enabled on GPS-capable models. |
| **Station Msg:** | Text field | Optional free-text message shown beside your callsign on the public FreeDV Reporter map. Saved to `FreeDvMyMessage`. |
| **Auto Mode:** | Toggle button | Automatically switches the slice mode when clicking a spot that includes mode information (e.g. CW, FT8, RTTY). Default: **Enabled** (as of v0.9.5.1). Saved to `SpotAutoSwitchMode`. |
| **Spot Lines:** | Toggle button | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Default: **Enabled**. Saved to `IsSpotsLinesEnabled`. New in v0.9.7. |
| Total Spots: | Indicator | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. |

## Tuning to a spot by double-clicking the spot list

Double-clicking a row in the **Spot List** tab tunes the active slice to the spot frequency. As of v0.9.7, AetherSDR also forwards the mode extracted from the spot comment, so the slice switches to the appropriate mode (for example, CW or SSB) to match the spot rather than only changing frequency.

## Tips

- Incoming activity appears in the **FreeDV Spots** console as well as in the unified spot table on the **Spot List** tab.
- If you want FreeDV spots to stand out from DX cluster or RBN spots, set a unique color using **Spot Color:** before connecting.
- If **Use radio** is checked, updating your callsign in Radio Setup immediately refreshes the **Callsign:** field without reopening SpotHub.
- Reporter broadcasting only activates while the RADE modem is running. You can leave the checkbox enabled at all times; no data is sent when RADE is idle.
- **Auto Mode:** on the **Display** tab defaults to **Enabled** as of v0.9.5.1. Spot density adjusts automatically as you zoom the panadapter without any manual configuration. If you previously disabled **Auto Mode:** and saved settings from an earlier version, check whether the new default is appropriate for your workflow. The setting is saved to `SpotAutoSwitchMode`.
- **Spot Lines:** is enabled by default. During contests, consider disabling it on the **Display** tab to reduce visual clutter on the panadapter. The setting is saved to `IsSpotsLinesEnabled`.

## Troubleshooting

- **FreeDV tab is missing** — Your AetherSDR build was compiled without WebSocket support. The tab is hidden at build time and cannot be enabled at runtime.
- **Status remains Disconnected after clicking Start** — Check your internet connection. The fixed endpoint `qso.freedv.org` must be reachable from your machine on the WebSocket port. Firewalls or proxy configurations may block the connection.
- **Spots appear in the console but not on the panadapter** — Verify that **Spots:** is set to **Enabled** on the **Display** tab of SpotHub.
- **"Please set both a callsign and a grid square" warning appears** — Fill in both **Callsign:** and **Grid Square:** before checking **Enable FreeDV Reporter reporting when RADE is active**. If **Use radio** or **Use GPS** is checked but the radio has not yet provided those values, uncheck the corresponding option and enter the values manually.
- **Use GPS checkbox is not visible** — Your radio model does not have GPS hardware. Enter a grid square manually in the **Grid Square:** field.
- **Double-clicking a spot does not switch mode** — Mode information is parsed from the spot comment. If the comment does not contain a recognized mode token, only the frequency is applied. Check the spot's Comment column in the **Spot List** tab to confirm whether mode information is present.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
<!-- docmesh:llm version=V0.9.7 date=2026-05-03 -->
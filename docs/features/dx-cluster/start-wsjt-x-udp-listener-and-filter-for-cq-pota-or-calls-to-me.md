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

| Control                            | Behavior                                                                                                                                                               | Setting key            |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------|
| **Address:**                       | UDP bind address for incoming WSJT-X messages.                                                                                                                         | `WsjtxAddress`         |
| **Port:**                          | UDP port number. Must match WSJT-X reporting port.                                                                                                                     | `WsjtxPort`            |
| **Start / Stop**                   | Starts or stops the UDP listener.                                                                                                                                      | —                      |
| **Auto-start on startup (WSJT-X)** | Starts the listener automatically on launch.                                                                                                                           | `WsjtxAutoStart`       |
| **CQ**                             | Passes only CQ transmissions to the panadapter.                                                                                                                        | `WsjtxFilterCQ`        |
| **CQ POTA**                        | Passes only CQ POTA transmissions.                                                                                                                                     | `WsjtxFilterPOTA`      |
| **Calling Me**                     | Passes only decodes addressed to your callsign.                                                                                                                        | `WsjtxFilterCallingMe` |
| **CQ color**                       | Color for CQ spots on the panadapter.                                                                                                                                  | `WsjtxColorCQ`         |
| **POTA color**                     | Color for CQ POTA spots.                                                                                                                                               | `WsjtxColorPOTA`       |
| **Calling Me color**               | Color for spots calling your callsign.                                                                                                                                 | `WsjtxColorCallingMe`  |
| **Default color**                  | Color for spots that match no active filter.                                                                                                                           | `WsjtxColorDefault`    |
| **Spot Life:**                     | Seconds a WSJT-X spot remains on the panadapter before fading.                                                                                                         | `WsjtxSpotLife`        |
| **WSJT-X Decodes**                 | Read-only console showing decoded transmissions as they arrive.                                                                                                        | —                      |
| **Spot Lines:**                    | Draws vertical lines from the spectrum up to each spot label. Disable during contests to reduce visual clutter. Default: Enabled.                                      | `IsSpotsLinesEnabled`  |
| Total Spots:                       | Live readout of how many spots are currently tracked across all sources. Updated whenever spots are added or cleared. Resets to 0 when **Clear All Spots** is pressed. | —                      |
## Tuning from the Spot List

Double-clicking a row in the **Spot List** tab tunes the active slice to that spot's frequency. As of v0.9.7, AetherSDR also forwards any mode information extracted from the spot comment, so the slice automatically switches to the correct mode (for example, CW or SSB) to match the spot rather than only changing frequency.

## FreeDV Reporter station reporting

The **FreeDV** tab contains a **Station Reporting** group that lets AetherSDR broadcast your station's activity to the public FreeDV Reporter map at `qso.freedv.org`. This section is only present in builds compiled with `HAVE_WEBSOCKETS`; on Windows it additionally requires `HAVE_RADE`.

### Controls

| Control | Behavior | Setting key |
|---|---|---|
| **Enable FreeDV Reporter reporting when RADE is active** | Enables station-reporting to the public FreeDV Reporter map whenever the RADE modem is active. The checkbox refuses to enable if either the callsign or grid square field resolves to an empty value; a warning dialog explains what is missing. Default: disabled. | `FreeDvAutoReport` |
| **Callsign:** | Callsign sent to the FreeDV Reporter map. The field is read-only while **Use radio** is checked. Callsign is automatically updated if you change it in Radio Setup while **Use radio** is active. | `FreeDvMyCallsign` |
| **Use radio (callsign)** | Pre-fills the callsign field from the radio's configured callsign and locks the field read-only. Default: enabled. | `FreeDvUseRadioCallsign` |
| **Grid Square:** | Maidenhead grid square sent to the FreeDV Reporter map. The field is read-only while **Use GPS** is checked. | `FreeDvMyGrid` |
| **Use GPS (grid)** | Pre-fills the grid field from the radio's GPS module and locks the field read-only. Only shown on radio models that have GPS hardware. | `FreeDvUseGpsGrid` |
| **Station Msg:** | Optional free-text message shown beside your callsign on the public FreeDV Reporter map. | `FreeDvMyMessage` |

### Enabling FreeDV Reporter reporting

1. Open `Settings > SpotHub...` and click the **FreeDV** tab.
2. In the **Station Reporting** group, verify the **Callsign:** field shows your callsign.
   - If **Use radio** is checked, the callsign is taken automatically from the radio. Uncheck it to enter a callsign manually.
3. Verify the **Grid Square:** field shows your Maidenhead locator (e.g. `FN20`).
   - On radios with GPS hardware, check **Use GPS (grid)** to populate the field automatically. Otherwise enter the grid square manually.
4. Optionally enter a short message in **Station Msg:** to appear next to your callsign on the map.
5. Check **Enable FreeDV Reporter reporting when RADE is active**.
   - If either the callsign or grid square is empty, a warning dialog appears and the checkbox is left unchecked. Fill in the missing field and try again.
   - When the checkbox enables successfully, AetherSDR begins reporting to `qso.freedv.org` whenever the RADE modem is active.
6. To report automatically on every launch, also enable **Auto-start on startup (FreeDV)** (stored as `FreeDvAutoStart`) so the FreeDV WebSocket connects without manual intervention.

### Notes on the callsign and grid validation

When you check **Enable FreeDV Reporter reporting when RADE is active**, AetherSDR resolves the effective callsign and grid square using the same priority order that the main reporting engine uses:

- **Callsign**: radio callsign (if **Use radio** is checked and the radio has one set), otherwise the value in the **Callsign:** field.
- **Grid square**: GPS grid (if **Use GPS** is checked and the radio has GPS hardware with a fix), otherwise the value in the **Grid Square:** field.

If either resolved value is empty the checkbox is automatically unchecked and a dialog prompts you to supply the missing information. This prevents blank or placeholder values from being broadcast to the shared community map.

## Auto Mode default changed

As of v0.9.5.1, the **Auto Mode:** toggle on the **Display** tab defaults to **Enabled** (stored as `SpotAutoSwitchMode`). In previous versions the default was Disabled. If you have not changed this setting, AetherSDR will now automatically switch the slice mode when you click a spot that includes mode information (e.g. CW, FT8, RTTY) immediately after a fresh install or settings reset.

## Spot Lines control added (v0.9.7)

The **Display** tab now includes a **Spot Lines:** toggle (stored as `IsSpotsLinesEnabled`; default Enabled). When enabled, AetherSDR draws a vertical line from the spectrum baseline up to each spot label, making it easier to locate the exact frequency of a spot. Disable this during contests or when the panadapter is crowded to reduce visual clutter.

## Tips

- If none of the three filter checkboxes (**CQ**, **CQ POTA**, **Calling Me**) are checked, all decoded transmissions are shown on the panadapter regardless of content.
- WSJT-X spots appear in the unified **Spot List** tab alongside spots from other sources. Double-click any row there to tune directly to that frequency. AetherSDR will also switch the slice mode to match the spot's mode if one is present in the comment.
- Spots from WSJT-X will only appear on the panadapter if the master **Spots:** toggle on the **Display** tab is enabled (stored as `IsSpotsEnabled`; default Enabled).
- FT8 operates on a 15-second cycle. Keep **Spot Life:** at 15 seconds or a multiple thereof so spots expire cleanly between cycles.
- FreeDV Reporter reporting is a community resource. Do not enable it with a test callsign or a placeholder grid square.

## Troubleshooting

- **Status stays at Stopped / no decodes appear in the console** — Verify the address and port in AetherSDR match exactly what is configured in WSJT-X under **File > Settings > Reporting**. Confirm no firewall is blocking the UDP port. Click **Stop** then **Start** after correcting the values.
- **Spots appear on the Spot List tab but not on the panadapter** — Open `Settings > SpotHub...`, go to the **Display** tab, and confirm **Spots:** is set to Enabled.
- **"Calling Me" filter shows no spots** — WSJT-X must have your callsign entered in its settings and must be actively decoding transmissions directed to that callsign. Verify your callsign in WSJT-X under **File > Settings > General**.
- **Double-clicking a spot does not change the slice mode** — Mode information is read from the spot comment. If the comment contains no recognizable mode string, only the frequency changes. Verify the spot source is including mode data in its comments.
- **FreeDV Reporter checkbox unchecks itself immediately** — The callsign or grid square field is empty or was not resolved. Fill in both fields (or enable **Use radio** / **Use GPS** so they are populated from the radio) and try again.
- **FreeDV Reporter section is not visible**
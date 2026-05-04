# Broadcast your station to the FreeDV Reporter map

When RADE mode is active, AetherSDR can publish your callsign, grid square, and an optional message to the public FreeDV Reporter map at qso.freedv.org.

## Before you start

- RADE mode must be available and active on your radio.
- A valid callsign and Maidenhead grid square must be set — reporting is blocked if either field is empty.

## Steps

1. Open **Settings > SpotHub...** and select the **FreeDV** tab.
2. In the **Callsign:** field, enter your callsign. To populate it automatically from the connected radio, check **Use radio**.
3. In the **Grid Square:** field, enter your Maidenhead grid square (up to 6 characters). On radios with GPS hardware (FLEX-8000 class, Aurora), check **Use GPS** to populate it automatically.
4. Optionally enter a short message in **Station Msg:** — this appears next to your station on the FreeDV Reporter map.
5. Press **Start** to connect the FreeDV WebSocket. The status indicator changes to **Connected**.
6. Check **Enable FreeDV Reporter reporting when RADE is active**. Your station begins broadcasting to the map immediately.

To stop broadcasting, uncheck **Enable FreeDV Reporter reporting when RADE is active** or press **Stop**.

## What each control does

| Control | Behavior |
|---|---|
| **Start / Stop** | Connects or disconnects the FreeDV WebSocket. After an unexpected drop the client auto-reconnects with exponential backoff; the status shows **Connecting...** during each attempt. Auto-reconnect stops only when you press **Stop**. |
| **Auto-Start: ON / OFF** | Automatically starts the FreeDV WebSocket connection when AetherSDR launches. Default: OFF. |
| **Enable FreeDV Reporter reporting when RADE is active** | Broadcasts your station to the public FreeDV Reporter map whenever RADE mode is active. Requires a callsign and grid square. Default: unchecked. |
| **Callsign:** | Your callsign sent to FreeDV Reporter. Read-only when **Use radio** is checked. |
| **Use radio** | Populates the **Callsign:** field automatically from the connected radio. Default: checked. |
| **Grid Square:** | Your Maidenhead grid square sent to FreeDV Reporter (up to 6 characters). Read-only when **Use GPS** is checked. |
| **Use GPS** | Populates **Grid Square:** from the radio's GPS hardware automatically. Only shown on radios that have GPS hardware (e.g. FLEX-8000 class, Aurora). Default: checked. |
| **Station Msg:** | Optional free-text message shown next to your station on the FreeDV Reporter map. |
| **Spot Color:** | Sets the color of FreeDV spot labels on the panadapter. Default: dark orange (#FF8C00). |
| **FreeDV Spots** | Read-only console showing incoming FreeDV activity from qso.freedv.org. |

## Tips

- If the callsign or grid square is empty when you try to enable reporting, the checkbox will refuse to activate. Fill in both fields first.
- The **Auto-Start: ON / OFF** toggle only starts the WebSocket listener — it does not automatically enable reporting. Check **Enable FreeDV Reporter reporting when RADE is active** separately.
- If your credentials change (for example after toggling RADE mode), the client reconnects transparently with updated credentials without any manual action.
- To receive FreeDV spots on the panadapter without broadcasting your own station, start the WebSocket but leave **Enable FreeDV Reporter reporting when RADE is active** unchecked.

## Related

- [spothub-overview.md](spothub-overview.md)
- [connect-dx-cluster.md](connect-dx-cluster.md)
- [freedv-spot-colors.md](freedv-spot-colors.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->

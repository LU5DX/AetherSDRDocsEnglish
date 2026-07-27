# Callsign Lookup overview

The Callsign Lookup feature queries online amateur radio databases — primarily QRZ.com — to display operator details such as name, location, grid square, DXCC entity, license class, country flag, and biography for any callsign you enter.

Results appear in a callsign card showing the operator’s details and a map when available. This is useful for identifying callsigns heard on the air, planning QSOs, or researching DX stations.

## How it works

1. Open the Callsign Lookup dialog using either method:
   - **Tools > Callsign Lookup...**
   - Right-click a spot in the panadapter and choose **Lookup**
2. Type a callsign into the **Callsign field**.
3. Press Enter or click the **Lookup** button to send the query.
4. The **Callsign card** appears with the lookup result, showing name, location, grid square, DXCC entity, country flag, license class, and a biography when available.

For full data (address, grid square, biography), the feature requires a valid QRZ.com XML subscription. Without a subscription, results may be limited to basic callsign data.

## What each control does

| Control | Type | Behavior | Notes |
|---------|------|----------|-------|
| **Callsign field** | Text field | Type a callsign and press Enter or click Lookup to start the query. | No default value; no persisted setting. |
| **Lookup button** | Push button | Sends the query to QRZ.com and other configured databases. | QRZ XML subscription required for full data. |
| **Callsign card** | Indicator | Displays the result: name, location, grid square, DXCC entity, country flag, license class, and biography. | Appearance depends on database response. |

## Tips

- A QRZ.com XML subscription is strongly recommended for the most useful results. Without it, you may only see basic callsign and grid square data.
- You can trigger a look up directly from a spot in the panadapter by right-clicking the spot label and choosing **Lookup** — no need to type the callsign manually.

## Related

- [Look up a callsign on QRZ.com](look-up-a-callsign-on-qrz-com.md)
- [See operator name, location and DXCC entity](see-operator-name-location-and-dxcc-entity.md)
- [View the callsign card with flag and details](view-the-callsign-card-with-flag-and-details.md)

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

## What each control does

| Control | Kind | Behavior | Setting key |
|---|---|---|---|
| **Server:** | Indicator | Fixed endpoint: `qso.freedv.org (WebSocket)`. Read-only. | — |
| **Start / Stop** | Push button | Connects or disconnects the FreeDV WebSocket. | — |
| **Auto-start on startup** | Toggle button | Starts the FreeDV connection automatically on launch. | `FreeDvAutoStart` |
| **FreeDV Spots** | Text field | Read-only console showing incoming FreeDV activity. | — |
| **Spot Color:** | Push button | Opens a color picker for FreeDV spots on the panadapter. | `FreeDvSpotColor` |

## Tips

- Incoming activity appears in the **FreeDV Spots** console as well as in the unified spot table on the **Spot List** tab.
- If you want FreeDV spots to stand out from DX cluster or RBN spots, set a unique color using **Spot Color:** before connecting.

## Troubleshooting

- **FreeDV tab is missing** — Your AetherSDR build was compiled without WebSocket support. The tab is hidden at build time and cannot be enabled at runtime.
- **Status remains Disconnected after clicking Start** — Check your internet connection. The fixed endpoint `qso.freedv.org` must be reachable from your machine on the WebSocket port. Firewalls or proxy configurations may block the connection.
- **Spots appear in the console but not on the panadapter** — Verify that **Spots:** is set to **Enabled** on the **Display** tab of SpotHub.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)

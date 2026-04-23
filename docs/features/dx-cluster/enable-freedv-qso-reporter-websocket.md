# Enable FreeDV QSO Reporter WebSocket

Connect AetherSDR to the FreeDV QSO reporter service at `qso.freedv.org` to receive FreeDV activity spots on your panadapter.

## Before you start

- The FreeDV WebSocket feature is only present in builds compiled with WebSocket support (`HAVE_WEBSOCKETS`). If the FreeDV tab is missing from SpotHub, your build does not include it.
- Spot display on the panadapter requires the master spot overlay to be enabled. See [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md) for display settings.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **FreeDV** tab.
3. Confirm the **Server:** indicator shows `qso.freedv.org (WebSocket)`. This endpoint is fixed and cannot be changed.
4. Click **Start**. The status indicator changes to **Connected** when the WebSocket connection is established.
5. Watch the **FreeDV Spots** console for incoming activity.
6. To change the color used for FreeDV spots on the panadapter, click **Spot Color:** and choose a color from the picker.
7. To connect automatically each time AetherSDR launches, click **Auto-start on startup** so it is active.

## What each control does

| Control | Description | Persisted setting |
|---|---|---|
| **Server:** | Read-only indicator showing the fixed endpoint `qso.freedv.org (WebSocket)`. | — |
| **Start / Stop** | Connects or disconnects the FreeDV WebSocket. | — |
| **Auto-start on startup** | When active, the WebSocket connects automatically on launch. | `FreeDvAutoStart` |
| **FreeDV Spots** | Read-only console showing raw FreeDV spot activity. | — |
| **Spot Color:** | Opens a color picker. The chosen color is applied to FreeDV spots on the panadapter. | `FreeDvSpotColor` |

## Troubleshooting

- **FreeDV tab is not visible** — Your AetherSDR build was compiled without WebSocket support. The tab is only present in `HAVE_WEBSOCKETS` builds. Check with the source of your package or rebuild with WebSocket support enabled.
- **Status stays Disconnected after clicking Start** — Confirm your system has outbound internet access to `qso.freedv.org`. Check any local firewall rules that may block WebSocket (typically port 443 or 80) connections.

## Related

- [SpotHub overview](overview.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Poll POTA activations](poll-pota-activations.md)

# Enable SpotCollector UDP feed

AetherSDR can receive DX spots broadcast by Ham Radio Deluxe's SpotCollector over UDP and display them on the panadapter. This page shows how to start the listener and configure it to run automatically on launch.

## Before you start

- Ham Radio Deluxe with SpotCollector must be running on your network and configured to broadcast UDP spot data.
- Note the UDP port SpotCollector is broadcasting on. You will need to enter that port in AetherSDR.

## Steps

1. Open `Settings > SpotHub...`.
2. Click the **SpotCollector** tab.
3. Set **UDP Port:** to the port SpotCollector is broadcasting on. Valid range: 1–65535. This value is saved as `SpotCollectorPort`.
4. Click **Start**. The status indicator changes to **Listening** when the listener is active.
5. Confirm spots are appearing in the **SpotCollector Spots** console.
6. To start the listener automatically each time AetherSDR launches, enable **Auto-start on startup**. This saves as `SpotCollectorAutoStart`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **UDP Port:** | UDP port that AetherSDR listens on for SpotCollector broadcasts. Valid range: 1–65535. | `SpotCollectorPort` |
| **Start / Stop** | Starts or stops the UDP listener. | — |
| **Auto-start on startup** | Automatically starts the listener when AetherSDR launches. | `SpotCollectorAutoStart` |
| **SpotCollector Spots** | Read-only console showing received spots as they arrive. | — |

## Tips

- SpotCollector spots appear alongside spots from other sources in the **Spot List** tab and on the panadapter. To control how they look on the panadapter, see [Pick colors for each spot source](pick-colors-for-each-spot-source.md).
- Double-click any row in the **Spot List** tab to tune the VFO to that spot's frequency.

## Troubleshooting

- **Status remains Stopped after clicking Start** — Verify no other application is already bound to the same UDP port on this machine.
- **Spots not appearing in the console** — Confirm SpotCollector is configured to broadcast to the same UDP port and that any host firewall allows inbound UDP traffic on that port.

## Related

- [SpotHub overview](overview.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)

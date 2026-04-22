# Enable SpotCollector UDP feed

AetherSDR can receive DX spots broadcast by Ham Radio Deluxe's SpotCollector over UDP and display them on your panadapter. Use this page to start the listener and configure it to run automatically on launch.

## Before you start

- SpotCollector must be configured to broadcast UDP spot data on a port you choose.
- Know the UDP port number SpotCollector is broadcasting on.

## Steps

1. Click `Settings > SpotHub...` to open the SpotHub dialog.
2. Click the **SpotCollector** tab.
3. Set **UDP Port:** to the port SpotCollector is broadcasting on. Valid range: 1–65535. This value is saved as `SpotCollectorPort`.
4. Click **Start** to begin listening. The status indicator changes to **Listening** when the port is open.
5. Incoming spots appear in the **SpotCollector Spots** console as they are received.
6. To start the listener automatically each time AetherSDR launches, enable **Auto-start on startup**. This is saved as `SpotCollectorAutoStart`.

## What each control does

| Control | Description | Setting key |
|---|---|---|
| **UDP Port:** | UDP port SpotCollector broadcasts on. Valid range: 1–65535. | `SpotCollectorPort` |
| **Start / Stop** | Starts or stops the UDP listener. | — |
| **Auto-start on startup** | Starts the listener automatically when AetherSDR launches. | `SpotCollectorAutoStart` |
| **SpotCollector Spots** | Read-only console showing received spots. | — |

## Tips

- Spots received from SpotCollector appear in the unified **Spot List** tab alongside spots from all other sources. The Source column identifies them.
- Double-click any row in the Spot List to tune your radio to that frequency.

## Troubleshooting

- **Status stays at Stopped after clicking Start** — Check that the UDP port number in AetherSDR matches what SpotCollector is configured to transmit on. Ensure no firewall or other application is blocking that port.
- **No spots appearing in the console** — Confirm SpotCollector is actively broadcasting and that both applications are running on the same host or that the broadcast reaches the AetherSDR machine's network interface.

## Related

- [SpotHub overview](overview.md)
- [Tune to a spot by double-clicking the spot list](tune-to-a-spot-by-double-clicking-the-spot-list.md)
- [Tune spot density, position, font size and lifetime](tune-spot-density-position-font-size-and-lifetime.md)
- [Pick colors for each spot source](pick-colors-for-each-spot-source.md)

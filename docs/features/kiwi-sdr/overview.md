# KiwiSDR overview

The KiwiSDR applet lets you browse and connect to public KiwiSDR receivers worldwide, then listen to them through an AetherSDR slice. This is useful for remote monitoring, propagation checking, or listening to bands your local radio cannot reach.

## How it works

The applet displays a searchable directory of online KiwiSDR receivers. You select a receiver from the list, click Assign to slice, and AetherSDR connects to that receiver and routes its audio through the active slice. A live status indicator shows the connection state and metadata about the connected receiver.

## What each control does

| Control | Type | Default | Behavior | Setting key |
|---------|------|---------|----------|-------------|
| Receiver list | List | Empty | Searchable, scrollable list of public KiwiSDR receivers with name, location, band, and status. | None (not persisted) |
| Assign to slice | Push button | — | Assigns the selected KiwiSDR receiver to the active slice for tuning and listening. | None (not persisted) |
| Status indicator | Indicator | Disconnected | Shows connection state: Disconnected, Connecting, Connected, or Error. | None (not persisted) |

## Tips

- The KiwiSDR applet does not require a connection to your FLEX-8600 radio. You can use it standalone for remote listening.
- The connection status indicator updates in real time; if you see "Error", verify the KiwiSDR receiver is online and reachable from your network.

## Related

- [Browse the public KiwiSDR directory](browse-the-public-kiwisdr-directory.md)
- [Connect to a KiwiSDR receiver](../../getting-started/setup/connect-to-a-kiwisdr-receiver.md)
- [Assign a KiwiSDR to a slice for listening](assign-a-kiwisdr-to-a-slice-for-listening.md)

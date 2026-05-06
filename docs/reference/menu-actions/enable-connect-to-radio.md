# Enable Connect to Radio

`Settings > Connect to Radio...` opens the connection dialog where you can discover and connect to FLEX-8600 radios on your network. Use this page to connect to a radio manually or to configure whether AetherSDR connects automatically on startup.

## Before you start

- AetherSDR is installed and running.
- Your FLEX-8600 is powered on and reachable on the same network.

## Steps

1. Click `Settings > Connect to Radio...`.
2. The connection dialog opens and scans the network for available FLEX-8600 radios.
3. Select your radio from the discovered list.
4. Click `Connect`.

To change startup connection behavior:

1. Click `Settings > Connect to Radio...`.
2. Check or uncheck `Connect to last radio on start up`.
   - **Checked (default):** AetherSDR attempts to connect automatically on startup using broadcast discovery and a routed-radio probe.
   - **Unchecked:** AetherSDR skips all automatic connection attempts on startup and opens the connection dialog immediately so you can select a radio manually.

## What each control does

| Control | Description | Default | AppSettings key |
|---|---|---|---|
| `Connect to last radio on start up` | When checked, AetherSDR auto-connects on startup. When unchecked, the connection dialog opens at startup for manual selection. | True | `AutoConnectToLastRadio` |

## Tips

- If you uncheck `Connect to last radio on start up`, the connection dialog launches automatically every time AetherSDR starts, so you do not need to navigate to `Settings > Connect to Radio...` manually on subsequent launches.

## Troubleshooting

- **No radios appear in the connection dialog** — Confirm the FLEX-8600 is powered on and connected to the same network segment as your computer. Check that no firewall is blocking broadcast UDP traffic. See [`enable-network.md`](enable-network.md) for network diagnostics.

## Related

- [Getting Started](getting-started.md)
- [Enable Network](enable-network.md)

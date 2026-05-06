# Network Diagnostics

Open the Network diagnostics window to view connection status and live log output for AetherSDR's network subsystems. Use this when troubleshooting radio connectivity, DX cluster feeds, or CW keying over the network.

## Before you start

- AetherSDR must be running.

## Steps

1. Click `Settings` in the menu bar.
2. Click `Network...`.

The Network Diagnostics dialog opens.

3. Click the **Logs** tab to view live log output.
4. Use the per-category filter checkboxes to show or hide log entries by category (for example, `aether.connection`, `aether.dxcluster`, `aether.cw`).

## What each control does

| Control | Description |
|---|---|
| **Logs** tab | Shows a live tail of log output scoped to diagnostic categories. Refreshes every 500 ms. |
| Category filter checkboxes | Each checkbox corresponds to a log category (`aether.connection`, `aether.dxcluster`, `aether.cw`, and others). Uncheck a category to hide its entries from the log tail. |

## Tips

- The Logs tab refreshes every 500 ms. There is no manual refresh control; output updates automatically.
- Filter by a single category such as `aether.connection` when diagnosing radio connection failures to reduce noise from unrelated subsystems.

## Related

- [Enable Connect to Radio](enable-connect-to-radio.md)
- [Getting Started](getting-started.md)

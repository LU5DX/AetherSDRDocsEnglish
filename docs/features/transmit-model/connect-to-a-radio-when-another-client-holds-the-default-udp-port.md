# Connect to a radio when another client holds the default UDP port

When another client already holds the default UDP port on your LAN, AetherSDR's UDP Port Registration Policy can automatically retry the connection on a different port so the connection does not get stuck.

## Before you start

- Confirm you are connecting over a LAN (not a WAN or USB connection). The retry policy applies only to LAN connections.
- Confirm the radio is powered on and reachable on the network.

## Steps

1. Attempt to connect to the radio normally. AetherSDR detects that the default UDP port is already registered by another client.
2. When the registration failure is detected, the UDP Port Registration Policy retries the registration automatically using a different port number. No action is required from you.
3. If the retry succeeds, the connection completes and the radio becomes available. If the retry fails, an error is reported in the connection log — check **Settings > Log** for details.

## What each control does

| Control | Behavior |
|---|---|
| UDP Port Registration Policy | Monitors UDP port registration on LAN connections. If the default port is already held by another client, retries registration on a different port. If all retries fail, reports a connection error. |

## Tips

- If connection still fails after the automatic retry, disconnect the other client that holds the default port, then try again.
- Check the connection log (**Settings > Log**) to confirm which port was used for the successful registration.

## Related

- [radio-connection.md](radio-connection.md)
- [troubleshoot-connection-errors.md](troubleshoot-connection-errors.md)
<!-- docmesh:llm version=V0.9.5.1 date=2026-05-04 -->

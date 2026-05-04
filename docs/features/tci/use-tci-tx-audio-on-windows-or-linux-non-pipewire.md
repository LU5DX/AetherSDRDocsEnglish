# Use TCI TX audio on Windows or Linux (non-PipeWire)

The TCI server routes TX audio from WSJT-X, JTDX, or MSHV over a WebSocket directly into a dedicated `dax_tx` stream on the radio. This stream is independent of SmartSDR DAX2 audio devices, so TCI TX audio works on Windows and Linux (non-PipeWire) without any additional audio driver setup.

## Before you start

- AetherSDR v0.9.5.1 or later is required.
- The radio must be connected and reachable.
- Your digital-mode software (WSJT-X, JTDX, or MSHV) must be configured to use TCI as its audio/CAT interface.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server panel.
2. In the **Port** field, confirm or enter the port your digital-mode software expects (default: `50001`).
3. Click **Enable** to start the TCI server. The status indicator changes to `:<port> (N clients)` once a client connects.
4. Set the **TX gain+meter** slider to the desired transmit level (default: `0.5`).
5. Begin transmitting from your digital-mode software. AetherSDR automatically opens the `dax_tx` stream and sends `dax=1` to the radio when TX starts — no further action is needed.

To start the TCI server automatically on launch, enable **Settings > Autostart TCI with AetherSDR**.

## What each control does

| Control | Behavior |
|---|---|
| **RX1..RX4 gain+meter** | Combined meter and slider. Drag to set the TCI RX gain for that channel (0.0–1.0, default 0.5). Changes are saved per channel (`TciRxGain1`–`TciRxGain4`). |
| **TX gain+meter** | Combined meter and slider. Drag to set the TCI TX gain (0.0–1.0, default 0.5). The value is persisted as `TciTxGain`; the slider reflects the stored value. |
| **Port** | Port the TCI WebSocket server listens on (1024–65535, default `50001`). Changing the port while the server is running restarts it. Values outside the valid range snap back to `50001`. |
| **Enable** | Toggle button. Starts or stops the TCI server. If the port is already in use, the toggle snaps back to off and the status shows `(port in use)`. |
| **RX/TX slice-assignment labels** | Read-only indicators showing which slice drives each RX/TX row (`—` when unassigned, otherwise `Slice <letter>`). Shares the DAX channel mapping. |

## Tips

- Multiple AetherSDR GUI clients can each register their own `dax_tx` stream slot, so running more than one client does not block TCI TX.
- If the status indicator turns red and shows `(port in use)`, choose a different port or stop the conflicting application before re-enabling.
- The `dax_tx` stream is only opened when TX actually starts; idle connections do not consume a stream slot.

## Related

- [DAX audio setup](dax-audio-setup.md)
- [TCI Server reference](tci-server-reference.md)
<!-- docmesh:llm version=v0.9.5.1 date=2026-05-04 -->

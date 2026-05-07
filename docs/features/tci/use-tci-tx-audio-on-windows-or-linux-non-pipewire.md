# Use TCI TX audio on Windows or Linux (non-PipeWire)

The TCI server routes TX audio from digital-mode software (WSJT-X, JTDX, MSHV) directly to the radio's `dax_tx` stream over WebSocket, bypassing Windows and Linux audio devices entirely. This means TCI TX works on Windows and Linux (non-PipeWire) exactly as it does on macOS.

## Before you start

- Install and configure your digital-mode software (WSJT-X, JTDX, or MSHV) to use TCI as its audio/CAT source.
- Know the port your digital-mode software expects (default: `50001`).

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server panel.
2. Set **Port** to the port your digital-mode software connects to (default `50001`; valid range 1024–65535).
3. Set **TX gain+meter** to your desired transmit level (drag the slider; default is `0.5`).
4. Click **Enable** to start the server. The status indicator changes to `:<port> (N clients)` once your digital-mode software connects.
5. Key up from your digital-mode software. If the slice is in a digital mode (DIGU, DIGL, RTTY, or FDV), TX audio is routed automatically through the TCI `dax_tx` stream — no additional configuration is needed.

> **Note:** If the status shows `(port in use)`, the **Enable** toggle snaps back to off. Choose a different port and try again.

## What each control does

| Control | Behavior |
|---|---|
| **Port** | Sets the WebSocket port the TCI server listens on. Changing the value restarts the server if it is already enabled. Values outside 1024–65535 snap to `50001`. |
| **Enable** | Starts or stops the TCI server. If the port cannot be bound, the toggle reverts to off and the status shows `(port in use)`. |
| **TX gain+meter** | Drag to set the TCI TX gain (0.0–1.0; default 0.5). The meter reflects the current outgoing audio level. |
| **RX1..RX4 gain+meter** | Drag to set the TCI RX gain for each channel (0.0–1.0; default 0.5). One control per channel (RX1–RX4). |
| **RX/TX slice-assignment labels** | Read-only indicators showing which slice drives each RX or TX row. Displays `—` when no slice is assigned, or `Slice <letter>` when one is. |

## Tips

- TX audio is routed through the TCI `dax_tx` stream **only** when the slice is in a digital mode (DIGU, DIGL, RTTY, or FDV). In voice modes (USB, LSB, AM, FM, CW), the radio uses its normal mic path so your PC mic selection is not affected.
- To start the TCI server automatically, enable **Settings > Autostart TCI with AetherSDR**.
- Multiple GUI clients can each register their own `dax_tx` stream slot simultaneously.

## Related

- [tci-server-reference.md](tci-server-reference.md)
- [dax-audio-overview.md](dax-audio-overview.md)
<!-- auto-updated version=V0.9.7 date=2026-05-07 -->

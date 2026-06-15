# Fix TCI TX Silent on Windows or Linux without PipeWire

TCI TX audio is routed through a dedicated `dax_tx` stream slot inside AetherSDR's TCI server, independent of the Windows SmartSDR DAX2 audio device path and independent of PipeWire. This means TCI TX should work on all platforms without any special configuration. This page helps you confirm the TCI server is set up correctly and the TX gain is not the cause of silence.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The third-party application sending TCI TX audio (for example, a digital-mode program) must be configured to connect to AetherSDR's TCI server, not to SmartSDR DAX2 or any other audio device.
- Make sure you are running AetherSDR v0.9.5.1 or later. Earlier versions had a platform-dependent TX audio policy that could block TX audio on Windows and Linux without PipeWire.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Check the server status label next to the Port field.
   - If it reads `(stopped)`, click **Enable** to start the server.
   - If it reads `(port in use)`, the chosen port is already bound by another process. Change the value in the **Port** field to a free port (valid range: 1024–65535; default: `50001`), then press Enter and click **Enable**.
3. Confirm the status label shows `:<port> (N clients)` with at least one client connected. If your TX application is not shown as a connected client, check its TCI host and port settings and ensure they match the **Port** field value.
4. Look at the **TX** row in the applet. Check the slice-assignment label next to the TX meter.
   - If it shows `—`, no slice is currently designated as the TX slice. Use the radio's slice controls to assign a TX slice.
   - If it shows `Slice <letter>` (with the slice letter rendered in rich text, e.g., colored or styled), the TX path is active.
5. Drag the **TX gain+meter** slider to confirm it is not set to `0.0`. The default is `0.5` (valid range: 0.0–1.0, persisted as `TciTxGain`). A value of `0.0` produces silence regardless of platform.
6. Key the transmitter from your third-party application and watch the **TX gain+meter** for level movement. If the meter shows activity, audio is reaching the server and the radio should be transmitting.
7. If you are using a digital mode that requires bit-exact tone fidelity, right-click the **TX gain+meter** slider to open the TX overflow handling menu. Select the desired mode to control how out-of-range (>1.0) samples from TCI clients are processed.

## What each control does

| Control | Default | Valid range | Setting key |
|---------|---------|-------------|-------------|
| **Port** | `50001` | 1024–65535 | `TciPort` |
| **Enable** | Off | On / Off | — |
| **TX gain+meter** | `0.5` | 0.0–1.0 | `TciTxGain` |
| **RX1 gain+meter** | `0.5` | 0.0–1.0 | `TciRxGain1` |
| **RX2 gain+meter** | `0.5` | 0.0–1.0 | `TciRxGain2` |
| **RX3 gain+meter** | `0.5` | 0.0–1.0 | `TciRxGain3` |
| **RX4 gain+meter** | `0.5` | 0.0–1.0 | `TciRxGain4` |
| **TX overflow mode (right-click)** | Clip | Clip (0), NaNGuard (1), Measure (2) | `TciTxOverflowMode` |

## TX overflow handling modes

Right-click the **TX gain+meter** slider to open the TX overflow handling context menu. This controls how out-of-range (>1.0) samples from TCI digital-mode clients are processed before reaching the radio. The default is **Clip** to maintain backward compatibility.

| Mode | Value | Description |
|------|-------|-------------|
| **Clip (saturating ±1.0)** | 0 | Hard-clamp overshoots to ±1.0. Defensive default; introduces harmonics on overshoot but protects downstream int16 conversion. |
| **NaN guard (zero NaN/Inf only)** | 1 | Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio. |
| **Measure only (true bypass)** | 2 | Never mutate samples. Count overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route. |

## Indicators

| Indicator | Possible states | Meaning |
|-----------|-----------------|---------|
| **Server status** | `(stopped)` | Server is not running. |
| | `:<port> (N clients)` | Server is running on the specified port with N connected clients. |
| | `(port in use)` | The chosen port is already bound by another process. |
| **RX/TX slice-assignment labels** | `—` | No slice is currently assigned. |
| | `Slice <letter>` | The specified slice is assigned to this channel. |

## Tips

- Out-of-range port values snap back to `50001` automatically.
- If you want the TCI server to start every time AetherSDR launches, enable `Settings > Autostart TCI with AetherSDR`. This sets the `AutoStartTCI` flag and also checks **Enable** on startup.
- The TX meter uses fast attack and slow decay smoothing, so a brief transmission will keep the meter visibly elevated for a moment after audio stops. No movement at all during a keyed transmission confirms audio is not arriving from the client.
- Slice assignment labels now support rich text rendering, so slice letters may appear with additional formatting (e.g., color) to indicate slice properties.
- For digital modes requiring bit-exact tone fidelity, use **NaN guard** or **Measure only** modes to avoid harmonic distortion from clipping.
- The applet container uses the theme system (`applet/tci`) for consistent styling across all themes.
- The TCI server is explicitly torn down when AetherSDR closes to prevent a use-after-free condition, fixed in v0.9.7.

## Troubleshooting

- **Status shows `(port in use)` and Enable snaps back to off** — Another application is bound to that port. Enter a different port number in the **Port** field, press Enter, and click **Enable** again.
- **Status shows the correct port and client count, but the radio is not transmitting audio** — Confirm the TX slice label in the **TX** row shows `Slice <letter>` and not `—`. If it shows `—`, designate a TX slice from the main UI. Also confirm the **TX gain+meter** is above `0.0`.
- **Third-party application cannot connect** — Verify the application is pointed at `localhost` (or AetherSDR's host IP) and the port number matches the **Port** field. Confirm no firewall rule is blocking the port.
- **TX meter shows no movement despite the client being connected and keyed** — The client application may be sending audio to a system audio device rather than over the TCI WebSocket. Check the client's audio output or TCI audio routing settings. AetherSDR does not use the Windows DAX2 audio device for TCI TX; audio must arrive over the WebSocket connection.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Change the TCI port](change-the-tci-port.md)
- [Autostart TCI on launch](autostart-tci-on-launch.md)
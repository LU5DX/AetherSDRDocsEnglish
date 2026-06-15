# TCI Server applet

The TCI Server applet runs an Expert-style TCI WebSocket server so third-party logging, digital-mode, and SDR software (Log4OM, SunSDR tools, etc.) can read and control the radio over the TCI protocol.

TCI TX audio is received over the WebSocket and fed into a dedicated dax_tx stream slot that is independent of the Windows SmartSDR DAX2 audio device path, so TCI TX works on all platforms including Windows and Linux without PipeWire.

## See how many TCI clients are connected

The TCI Server applet shows a live client count in its status indicator. Use this to confirm that Log4OM, SunSDR tools, or any other TCI client has successfully connected.

## Before you start

- AetherSDR must be connected to a radio. The TCI applet requires an active radio connection.
- The TCI server must be running (Enable toggled on). If it is stopped, the status shows `(stopped)` and no client count is available.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Read the status indicator next to the Port field.

When the server is running and at least one client is connected, the status reads:

```
:<port> (N clients)
```

For example, with two clients connected on the default port:

```
:50001 (2 clients)
```

When the server is running but no clients are connected, the status reads the port and `(0 clients)`. When the server is stopped, the status reads `(stopped)`.

## What each control does

| Control                        | Description                                                                                                                                                                                      | Notes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Port                           | Port the TCI WebSocket server listens on. Out-of-range values snap to `50001`.                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Enable                         | Starts or stops the TCI server.                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Server status                  | Displays `(stopped)`, `:<port> (N clients)`, or `(port in use)`. Turns red on bind failure.                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RX1–RX4 gain+meter             | Combined meter/slider; drag sets the TCI RX gain for the channel and emits `tciRxGainChanged`.                                                                                                   | Each slider has an accessible name "TCI RX gain" followed by the channel number (1–4) for screen reader compatibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| TX gain+meter                  | Drags set the TCI TX gain and emit tciTxGainChanged. Right-click opens TX overflow-mode picker (Clip / NaNGuard / Measure).                                                                      | TciServer::setTxGain persists TciTxGain internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). Right-click menu lets users choose how out-of-range (>1.0) samples from digital-mode clients are handled: Clip (saturating ±1.0, legacy default), NaNGuard (pass-through, only zero NaN/Inf), or Measure (true bypass with clip counting). Default is Clip so existing users see no behavior change (#3065). The slider has an accessible name "TCI TX gain" for screen reader compatibility. |
| TX overflow mode (right-click) | Right-click the TX gain meter/slider to open a context menu selecting the TX overflow handling mode. Emits `tciTxOverflowModeChanged`. Default is Clip so existing users see no behavior change. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| RX/TX slice-assignment labels  | Show which slice currently drives each RX/TX row. Displays `—` when no slice is assigned or `Slice <letter>` when a slice is mapped.                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
## TX overflow mode details

Right-click the TX gain meter/slider to open the TX overflow handling mode menu. This setting determines how out-of-range (>1.0) samples from TCI clients are handled before the radio sees them.

| Mode        | Value | Description                                                                                                                                                                                                 |
|-------------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clip        | 0     | Hard-clamp overshoots to ±1.0. Defensive default; introduces harmonics on overshoot but protects downstream int16 conversion.                                                                              |
| NaN guard   | 1     | Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio.                                                           |
| Measure     | 2     | Never mutate samples. Count overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route.                                                                          |

Clip is the default and preserves the legacy defensive limiter. NaNGuard and Measure are progressively less destructive for digital-mode tone fidelity. The mode is persisted as `TciTxOverflowMode` (0, 1, or 2).

## Tips

- The client count updates automatically whenever a client connects or disconnects — no need to refresh.
- When one client is connected the status reads `(1 client)` (singular); two or more reads `(N clients)` (plural).
- The status text turns blue when one or more clients are connected, making it easy to spot at a glance.

## Troubleshooting

- **Status shows `(port in use)`** — Another process is already bound to the configured port. Change the value in the Port field to an unused port in the range 1024–65535 and press Enter. The server restarts automatically if Enable is on.
- **Status stays `(stopped)` after clicking Enable** — The bind failed and Enable snapped back to off. Check the Port value and confirm no other application is using that port.
- **Client count stays at 0** — Confirm the third-party application is configured to connect to the correct host and port. The port in use is shown in the status indicator.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](../../features/tci/enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](../../features/tci/change-the-tci-port.md)
- [Autostart TCI on launch](../../features/tci/autostart-tci-on-launch.md)
- [TCI Server overview](../../features/tci/overview.md)
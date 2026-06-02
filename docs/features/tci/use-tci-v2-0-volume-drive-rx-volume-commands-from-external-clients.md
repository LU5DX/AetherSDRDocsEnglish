# Use TCI v2.0 volume/drive/rx_volume commands from external clients

External clients (logging software, digital-mode software, SDR programs) can control AetherSDR using TCI v2.0 `volume`, `drive`, and `rx_volume` commands when the TCI server is enabled and the radio is connected.

## Before you start

- Enable the TCI server (click the TCI tray button on the right sidebar, then click Enable).
- Connect to a radio.
- Configure your external client to connect to AetherSDR's TCI server on the port shown in the TCI applet (default: 50001).

## Steps

1. In the TCI applet, note the Port number or change it by editing the text field and pressing Enter. Valid range: 1024–65535.
2. Configure your external client to connect to AetherSDR's IP address and that port.
3. Send TCI v2.0 commands from your client:

   - **`volume`** — Sets the master RX volume. AetherSDR maps this to the RX gain for the currently active slice.
   - **`drive`** — Sets the TX drive level. AetherSDR maps this to `TciTxGain`.
   - **`rx_volume <channel>`** — Sets the RX gain for a specific DAX channel (1–4). AetherSDR maps this to `TciRxGain1` through `TciRxGain4`.

4. The TCI server receives these commands and updates the corresponding gain settings. The changes are reflected in the TCI applet's meter/slider controls and persisted to settings.

## What each control does

| Command                        | Mapped setting                                                                                                                       | Default                                                                                                                                                                                                                                        |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `volume`                       | Active slice RX gain                                                                                                                 | 0.5                                                                                                                                                                                                                                            |
| `drive`                        | `TciTxGain`                                                                                                                          | 0.5                                                                                                                                                                                                                                            |
| `rx_volume <channel>`          | `TciRxGain1`–`TciRxGain4`                                                                                                            | 0.5                                                                                                                                                                                                                                            |
| TX overflow mode (right-click) | Right-click the TX gain meter/slider to open a context menu selecting the TX overflow handling mode. Emits tciTxOverflowModeChanged. | New in v26.5.3. Clip clamps overshoots to ±1.0 with harmonic distortion; NaNGuard preserves bit-exact digital tones by only zeroing NaN/Inf; Measure counts overshoots for telemetry without mutation. Persisted as TciTxOverflowMode (0/1/2). |

## TCI applet controls

The TCI applet shows the current state and lets you adjust gain settings:

| Control | Description | Setting key |
|---------|-------------|-------------|
| **RX1 gain+meter** through **RX4 gain+meter** | Combined meter/slider for each DAX channel. Drag to set TCI RX gain. Emits `tciRxGainChanged`. | `TciRxGain1`, `TciRxGain2`, `TciRxGain3`, `TciRxGain4` |
| **TX gain+meter** | Combined meter/slider for TX gain. Drag to set TCI TX gain. Emits `tciTxGainChanged`. Right-click to open the TX overflow mode picker. | `TciTxGain` |
| **Port** | Text field for the WebSocket server port. Change and press Enter. Out-of-range values snap to 50001. | `TciPort` |
| **Enable** | Toggle button to start or stop the TCI server. If bind fails, snaps back to off and status shows "(port in use)". | None |

### TX overflow mode (right-click)

Right-click the **TX gain+meter** control to open a context menu for selecting how out-of-range (>1.0) samples from TCI clients are handled before reaching the radio. Emits `tciTxOverflowModeChanged`. The selected mode is persisted as `TciTxOverflowMode` (0/1/2).

| Mode | Value | Description |
|------|-------|-------------|
| Clip (saturating ±1.0) | 0 | Hard-clamp overshoots to ±1.0. Defensive default; introduces harmonics on overshoot but protects downstream int16 conversion. |
| NaN guard (zero NaN/Inf only) | 1 | Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio. |
| Measure only (true bypass) | 2 | Never mutate samples. Count overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route. |

Default is **Clip** so existing users see no behavior change.

### RX/TX slice assignment labels

| Label | Description | Format |
|-------|-------------|--------|
| **RX1..RX4** status | Shows which slice drives each RX DAX channel. Displays as "Slice <letter>" where the letter may appear as rich HTML text (e.g., with strikethrough for disabled slices). | `—` or rich HTML slice label |
| **TX** status | Shows which slice is the active TX slice. Displays as "Slice <letter>" with the same rich HTML formatting as RX labels. | `—` or rich HTML slice label |

### Server status indicator

| State | Meaning |
|-------|---------|
| `(stopped)` | Server is not running |
| `:<port> (N clients)` | Server is running on the specified port with N connected clients |
| `(port in use)` | Bind failed — the port is already in use by another application |

## Tips

- The TCI server supports bidirectional state sync — changes made locally via the TCI applet's sliders are also sent back to external clients that subscribe to gain updates.
- The `rx_volume` command accepts a channel number (1–4). Channel numbers correspond to the DAX channels displayed in the TCI applet's RX1–RX4 rows.
- TCI TX audio is always allowed regardless of platform or hosted-DAX availability (v0.9.5.1, #2276).
- Slice assignment labels now use rich HTML formatting (v26.5.2.1, #2606), so disabled or special-state slices may display with text formatting (e.g., strikethrough).
- For bit-exact digital-mode tone fidelity, use **NaN guard** or **Measure only** mode to avoid harmonic distortion from the Clip limiter.
- The TCI applet container now uses themed styling (v26.6.1) — colors adapt to the active theme.

## Related

- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [Change the TCI port](change-the-tci-port.md)
- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
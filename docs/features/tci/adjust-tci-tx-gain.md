# Adjust TCI TX gain

Set the output gain that the TCI server applies to the transmit audio stream before sending it to connected clients (Log4OM, SunSDR tools, and similar). Also configure how out-of-range samples from digital-mode clients are handled.

## Before you start

- AetherSDR must be connected to the radio. The TCI applet requires an active radio connection.
- The TCI server must be visible. If the applet panel is not showing the TCI section, click the **TCI** tray button on the right sidebar to reveal it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Locate the **TX:** row. The slice indicator to the right of the label shows which slice currently drives the TX channel (for example, `Slice A`), or `—` if no TX slice is assigned.
3. Drag the **TX gain+meter** slider left to reduce gain or right to increase gain. The valid range is `0.0` to `1.0`; the default is `0.5`.
4. Release the slider. The new value is saved immediately to `TciTxGain` and takes effect in the running server.

## Choose TX overflow handling mode

1. Right-click the **TX gain+meter** slider to open the context menu.
2. Select one of the following modes:
   - **Clip (saturating ±1.0)** — Hard-clamp overshoots to ±1.0. Defensive default; introduces harmonics on overshoot but protects downstream int16 conversion.
   - **NaN guard (zero NaN/Inf only)** — Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio.
   - **Measure only (true bypass)** — Never mutate samples. Count overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route.
3. The selection is saved immediately to `TciTxOverflowMode` and takes effect in the running server.

## What each control does

| Control                        | Default                                                                                                                     | Valid range                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TX gain+meter                  | Drags set the TCI TX gain and emit tciTxGainChanged. Right-click opens TX overflow-mode picker (Clip / NaNGuard / Measure). | TciServer::setTxGain persists TciTxGain internally; UI mirrors the stored value. TCI TX audio is always allowed regardless of platform or hosted-DAX availability (evaluateDaxTxPolicy now unconditionally allows DaxTxRequestReason::TciTxAudio, v0.9.5.1, #2276). Right-click menu lets users choose how out-of-range (>1.0) samples from digital-mode clients are handled: Clip (saturating ±1.0, legacy default), NaNGuard (pass-through, only zero NaN/Inf), or Measure (true bypass with clip counting). Default is Clip so existing users see no behavior change (#3065). |
| TX overflow mode (right-click) | Clip (0)                                                                                                                    | Clip (0), NaNGuard (1), Measure (2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

The **TX gain+meter** is a combined meter and slider. The meter portion reflects the live TX audio level from the active TX slice. The slider position sets the gain applied to that audio before it is sent to TCI clients.

The slice label next to **TX:** (for example, `Slice A` or `—`) is read-only. It shows which slice is currently assigned as the TX slice and updates automatically when the TX slice changes. Starting in v26.5.2.1, the slice label uses rich text formatting so that slice letters rendered as HTML display correctly (#2606).

## Server status indicator

The TCI Server applet shows a status label next to the Enable button. This label displays one of three states:

| State                         | Meaning                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------|
| `(stopped)`                   | Server is not running. The label uses the theme color `{{color.background.3}}` for text.  |
| `:<port> (N clients)`         | Server is running on the specified port with the given number of connected clients.       |
| `(port in use)`               | Server could not start because the port is already in use. The label turns red.           |

In v26.6.1, the status label styling was updated to use the theme color `{{color.background.3}}` instead of a hardcoded color, ensuring proper appearance with all AetherSDR themes.

## Tips

- If no slice label appears next to **TX:** (it shows `—`), no TX slice is assigned. Assign a TX slice on the radio before adjusting TX gain.
- The gain value persists across restarts. AetherSDR reads `TciTxGain` on launch and sets the slider to the stored value.
- Use **NaN guard** or **Measure only** when running digital modes that require bit-exact tone fidelity. The **Clip** mode may introduce harmonic distortion on overshoots.
- The **Measure only** mode is a true bypass and only counts overshoots for telemetry without modifying the audio stream.

## Related

- [Adjust TCI RX gain per channel](adjust-tci-rx-gain-per-channel.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
- [TCI Server overview](overview.md)
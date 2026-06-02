# Choose TCI TX overflow handling (Clip, NaNGuard, or Measure) for digital-mode tone fidelity

The TX overflow handling mode controls how AetherSDR processes audio samples from TCI client software that exceed the normal ±1.0 range. Digital-mode applications (FT8, RTTY, etc.) can produce out-of-range floating-point values; choosing the right mode preserves bit-exact tone fidelity or protects downstream hardware as needed.

## Before you start

- The TCI server must be running (Enable button is green, status shows `:<port>`).
- A TCI client (e.g., WSJT-X, Log4OM) must be connected and transmitting.

## Steps

1. Right-click the TX gain meter/slider in the TCI Server applet.
2. From the **TX overflow handling** context menu, select one of the three modes:
   - **Clip (saturating ±1.0)** — legacy default
   - **NaN guard (zero NaN/Inf only)**
   - **Measure only (true bypass)**

The selection is persisted as `TciTxOverflowMode` and takes effect immediately for all new audio from TCI clients.

## What each control does

| Mode                           | Enum Value                                                                                                                           | Behavior                                                                                                                                                                                                                                       |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clip (saturating ±1.0)         | 0                                                                                                                                    | Hard-clamps overshoots to ±1.0. Introduces harmonic distortion on overshoot but protects downstream int16 conversion.                                                                                                                          |
| NaN guard (zero NaN/Inf only)  | 1                                                                                                                                    | Passes samples through bit-exact; only zeros pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats reach the radio.                                                                                           |
| Measure only (true bypass)     | 2                                                                                                                                    | Never mutates samples. Counts overshoots for telemetry; downstream int16 conversion still clamps in the radio-native DAX route.                                                                                                                |
| TX overflow mode (right-click) | Right-click the TX gain meter/slider to open a context menu selecting the TX overflow handling mode. Emits tciTxOverflowModeChanged. | Clip clamps overshoots to ±1.0 with harmonic distortion; NaNGuard preserves bit-exact digital tones by only zeroing NaN/Inf; Measure counts overshoots for telemetry without mutation. Persisted as TciTxOverflowMode (0/1/2).                |

## Tips

- **Default is Clip (mode 0)** — existing users see no behavior change after upgrading.
- Digital-mode clients commonly send audio at precisely 0 dBFS; floating-point rounding can push values slightly above ±1.0. NaN guard preserves those tone edges while still protecting against corrupted NaN/Inf frames.
- The downstream int16 conversion in the radio-native DAX path always clamps regardless of this setting when using Measure mode.

## Related

- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
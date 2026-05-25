# Adjust TCI RX gain per channel

The TCI Server applet provides a gain slider for each of its four RX channels. Adjusting these lets you match the audio level that TCI clients (such as Log4OM or SunSDR tools) receive from each slice.

## Before you start

- The radio must be connected. The TCI applet requires an active radio connection.
- The TCI Server applet must be visible. If the applet panel is not showing, click the **TCI** tray button on the right sidebar to reveal it.

## Steps

1. Click the **TCI** tray button on the right sidebar to open the TCI Server applet.
2. Locate the **RX1**, **RX2**, **RX3**, or **RX4** row for the channel you want to adjust. The slice assignment label next to the channel name (for example, `Slice A`) shows which slice is driving that channel. A `—` means no slice is currently assigned.
3. Drag the meter/slider for that row left or right to set the gain. The value is saved immediately.
4. Repeat for any other RX channels you want to adjust.

## What each control does

| Control                        | Default | Valid range |
|--------------------------------|---------|-------------|
| RX1 gain meter/slider          | 0.5     | 0.0 – 1.0   |
| RX2 gain meter/slider          | 0.5     | 0.0 – 1.0   |
| RX3 gain meter/slider          | 0.5     | 0.0 – 1.0   |
| RX4 gain meter/slider          | 0.5     | 0.0 – 1.0   |
| TX gain+meter                  | 0.5     | 0.0 – 1.0   |
| Slice assignment label         | —       | — or `Slice <letter>` |
| TX overflow mode (right-click) | Clip    | Clip, NaNGuard, Measure |

Each meter/slider also displays a live RX or TX level using exponential smoothing — fast attack, slow decay — so the bar reflects signal activity on that channel while the drag position sets the gain.

The slice assignment labels now render slice letters with rich text formatting (#2606). This allows external slice indicators (for example, a colored or styled marker on the slice letter) to display correctly in the status label. The label text is generated using `SliceLabel::richText()` instead of a raw letter, ensuring any HTML formatting embedded in the slice's representation is preserved.

## Right-click the TX gain for overflow handling

The TX gain meter/slider has a right-click context menu that lets you choose how out-of-range (>1.0) audio samples from TCI clients are handled before they reach the radio.

1. Right-click anywhere on the **TX gain+meter** slider.
2. Select one of three overflow-handling modes:
   - **Clip (saturating ±1.0)** — Hard-clamp overshoots to ±1.0. This is the legacy default and introduces harmonic distortion on overshoots but protects downstream int16 conversion.
   - **NaN guard (zero NaN/Inf only)** — Pass samples through bit-exact; only zero pathological NaN/Inf values. Preserves digital-mode tone fidelity; out-of-range floats still reach the radio.
   - **Measure only (true bypass)** — Never mutate samples. Counts overshoots for telemetry; the downstream int16 conversion still clamps in the radio-native DAX route.

The selected mode is persisted as the `TciTxOverflowMode` setting (value 0, 1, or 2) and restored on next startup. Default is Clip so existing users see no behavior change (#3065).

## What each TX overflow mode does

| Mode        | Value | Behavior                                                                 |
|-------------|-------|--------------------------------------------------------------------------|
| Clip        | 0     | Saturates samples at ±1.0. Defensive default; introduces harmonics.      |
| NaNGuard    | 1     | Passes samples through unchanged except zeroing NaN/Inf. Bit-exact for digital tones. |
| Measure     | 2     | True bypass — never mutates samples. Counts overshoots for telemetry.    |

## Tips

- The slice assignment labels (for example, `Slice A`) follow the DAX channel mapping. If a slice's DAX channel assignment changes, the label updates automatically.
- Gain values are persisted as two-decimal floats (for example, `0.75`). They are restored the next time AetherSDR starts.
- The TX overflow mode is particularly useful for digital modes where out-of-range samples must be preserved without clipping for bit-exact tone fidelity. Use **NaN guard** for digital-mode operation and **Measure** for diagnostic telemetry.

## Troubleshooting

- **A channel shows `—` and passes no audio to the TCI client** — No slice is assigned to that DAX channel. Assign a slice to the corresponding DAX channel in your radio setup so TCI RX audio is routed to that channel.
- **TX overflow mode selection does not persist** — Check that AetherSDR has write permission to its settings file. The `TciTxOverflowMode` setting is stored in the application settings.

## Related

- [TCI Server overview](overview.md)
- [Adjust TCI TX gain](adjust-tci-tx-gain.md)
- [Enable the TCI server for Log4OM / SunSDR clients](enable-the-tci-server-for-log4om-sunsdr-clients.md)
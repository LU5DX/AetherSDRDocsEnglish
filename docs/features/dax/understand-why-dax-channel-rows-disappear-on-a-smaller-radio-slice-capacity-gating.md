# Understand why DAX channel rows disappear on a smaller radio (slice-capacity gating)

This page explains why the DAX applet hides certain DAX channel rows when connected to radios with fewer available slices, so you know that missing rows are expected behavior rather than a fault.

## Before you start

- Connected to a FLEX-8600 or another SmartSDR-compatible radio.
- DAX applet visible (toggle with the `DAO` tray button on the right sidebar if hidden).

## Steps

No action is required — this is informational. The DAX applet automatically hides RX channel rows that exceed the connected radio's slice capacity. For example:

- A 2-slice radio (like a FLEX-6300/6400) shows only DAX 1–2 rows.
- A 4-slice radio (like a FLEX-6600/8600) shows only DAX 1–4 rows.
- An 8-slice radio shows all DAX 1–8 rows.

The hidden rows are not destroyed; their visibility is toggled based on the radio's `maxSlices` value. This prevents dead gain sliders that would otherwise route nowhere.

## What each control does

| Control | Behavior | Persisted setting |
| --- | --- | --- |
| DAX 1–4 gain+meter | Always visible. Drag to set RX gain on DAX channels 1–4. | `DaxRxGain1`–`DaxRxGain4` (default `0.5`, range `0.0`–`1.0`) |
| DAX 5 gain+meter | Visible only when the connected radio supports at least 5 slices. | `DaxRxGain5` (default `0.5`, range `0.0`–`1.0`) |
| DAX 6 gain+meter | Visible only when the connected radio supports at least 6 slices. | `DaxRxGain6` (default `0.5`, range `0.0`–`1.0`) |
| DAX 7 gain+meter | Visible only when the connected radio supports at least 7 slices. | `DaxRxGain7` (default `0.5`, range `0.0`–`1.0`) |
| DAX 8 gain+meter | Visible only on an 8-slice-capable radio. | `DaxRxGain8` (default `0.5`, range `0.0`–`1.0`) |

The DAX Enable toggle, TX gain+meter, and slice-assignment status indicators are unaffected by slice-capacity gating — they remain visible on all radios.

## Tips

- If you expect a DAX row (e.g., DAX 5) but it's missing, check your radio's slice limit. The applet hides rows to keep the UI honest, not because of a bug.
- The `DaxChannel_Slice{letter}` settings persist per-slice DAX channel assignments; they are not tied to row visibility.

## Troubleshooting

- **A DAX channel row I expect is missing** — The connected radio doesn't support enough slices. Verify the radio model's slice capacity (e.g., FLEX-6300 = 2 slices, FLEX-6600 = 4, FLEX-8600 = 4). If you're on an 8-slice-capable radio and still see fewer rows, re-check the radio connection.

## Related

- [DAX Audio overview](overview.md)
- [Enable DAX to route slice audio to WSJT-X / FLDigi / other digital software](enable-dax-to-route-slice-audio-to-wsjt-x-fldigi-other-digital-software.md)
- [See which slice is currently using each DAX channel](see-which-slice-is-currently-using-each-dax-channel.md)
- [Understand why the DAX applet shows only a note on Windows (no built-in driver)](understand-why-the-dax-applet-shows-only-a-note-on-windows-no-built-in-driver.md)

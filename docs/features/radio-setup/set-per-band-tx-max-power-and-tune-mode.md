# Set per-band TX max power and tune mode

This page explains how to configure the transmit power ceiling and tune behavior for each amateur band on the FLEX-8600. Use these settings to protect amplifiers or comply with band-specific power limits without adjusting the main power control each time you change bands.

## Before you start

- AetherSDR must be connected to the radio. These controls are unavailable when no radio connection is active.
- Identify which bands you want to restrict and what power cap (as a percentage of full output) you want to apply to each.

## Steps

1. Open `Settings > Radio Setup...`.
2. Click the **TX** tab.
3. To set a radio-level power cap that applies regardless of band, adjust **Max Power:** to the desired value (0–100 %).
4. To configure per-band power and tune settings, click **TX Band Settings**. This opens the dedicated per-band power and tune dialog.
5. In the TX Band Settings dialog, locate the row for the band you want to configure.
6. Set the maximum TX power for that band using the power field in that row.
7. Set the tune behavior for that band using the tune mode field in that row.
8. Repeat steps 5–7 for each band you want to configure.
9. To set the tune behavior at the radio level (outside of per-band settings), return to the **TX** tab and select the desired option from **Tune Mode:**.
10. Close the dialog when finished. Settings are applied to the radio immediately.

## What each control does

| Control | Where | Behavior | Valid range | Default |
|---|---|---|---|---|
| **Max Power:** | TX tab | Sets a radio-level TX power ceiling. All transmissions are capped at this value regardless of slice or mode settings. | 0–100 % | — |
| **Tune Mode:** | TX tab | Selects how the tune function behaves when activated. | Combo box options (set by radio firmware) | — |
| **TX Band Settings** | TX tab | Opens the per-band power and tune dialog where each amateur band can be configured independently. | — | — |
| **Show TX in Waterfall:** | TX tab | When enabled, the transmitted signal is drawn in the waterfall display. | On / Off | — |
| **TX Follows Active Slice / Active Slice Follows TX** | TX tab | Mutually exclusive modes controlling whether the TX frequency tracks the active slice or vice versa. | Two options | — |

## Tips

- The **Max Power:** spinbox on the TX tab is a global ceiling. Per-band limits set in the TX Band Settings dialog operate within this global cap. If you set **Max Power:** to 50 %, a per-band setting of 100 % will still be limited to 50 % of the radio's full output.
- You can also reach the TX Band Settings dialog directly via `Settings > TX Band Settings...` without opening Radio Setup first.

## Related

- [overview.md](overview.md)
